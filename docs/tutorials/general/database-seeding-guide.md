# Database Seeding Guide

**Purpose**: Guide for seeding initial plant data and handling relationships (PlantLinks, Nurseries, companion plants)

**Related Files**:

- Plant Model: `2024-Django-Attempt/Plants/models.py:21-104`
- Initial Data: `docs/data/initial_plants.csv`
- Management Commands: `2024-Django-Attempt/Plants/management/commands/`

---

## Table of Contents

- [Overview](#overview)
- [Basic Plant Data Seeding](#basic-plant-data-seeding)
- [Handling Relationships](#handling-relationships)
    - [PlantLinks (Many-to-Many)](#plantlinks-many-to-many)
    - [Nurseries (Many-to-Many)](#nurseries-many-to-many)
    - [Companion Plants (Self-Referential Many-to-Many)](#companion-plants-self-referential-many-to-many)
- [Complete Workflow Examples](#complete-workflow-examples)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

This guide covers three seeding approaches:

1. **Basic CSV seeding** - Simple plant attributes (current implementation)
2. **Relationship seeding** - PlantLinks, Nurseries, companion plants (future enhancement)
3. **Hybrid approach** - CSV for plants + separate files for relationships

**Recommended approach**: Start with CSV for plants, add relationship files as needed.

---

## Basic Plant Data Seeding

### Current Implementation

**File**: `docs/data/initial_plants.csv`

**Fields**: All Plant model fields except relationships (companion_plants, links are commented out in model)

### CSV Structure

```csv
name_common,name_scientific,plant_type,exposure,description,is_hybrid,...,germination_days,maturity_days
Tomato,Solanum lycopersicum,an,fs,"Popular garden vegetable",0,...,7,80
```

### Field Reference

<!-- --8<-- [start:plant-field-ref] -->

Note that the system is intended to be metric by default, but user can change to imperial units. This will update for all items, so it does not need to be stored in the database.

| Field | Type | Description | Valid Values | Required | Notes |
|-------|------|---|--------------|-------|-------|
| `name_common` | Text | Common plant name | Any string | ✅ Yes ||
| `name_scientific` | Text | Scientific (Latin) name | Any string | ❌ Optional | can be blank |
| `plant_type` | Choice | Plant type code | `an`, `bi`, `pe`, `tp`, `sh`, `tr`, `vi`, `un` | ✅ Yes | Default: `un` (unknown) |
| `exposure` | Choice | Sun exposure code | `fs`, `fp`, `pu`, `pd`, `sh` | ✅ Yes | Default: `fs` (full sun) |
| `description` | Text | Plant description | Any string | ✅ Yes ||
| `is_*` (boolean flags) | Boolean | Plant characteristics (`0` or `1`) | `0` or `1` | ❌ Optional | Default: `0` (false) |
| `hardiness_zone_low` | Choice | Minimum hardiness zone (e.g., `5a`) | `1a` to `13b`, `na` | ✅ Yes| Default: `8b` |
| `hardiness_zone_high` | Choice | Maximum hardiness zone (e.g., `10b`) | `1a` to `13b`, `na` |✅ Yes | Default: `8b` |
| `spacing_min` | Integer | Minimum spacing | 0-999 | ❌ Optional | Default: `0`<br>Should provide choice of measurement (e.g. inches, cm, feet, etc) based on imperial or metric in personal settings |
| `spacing_max` | Integer | Maximum spacing | 0-999 | ❌ Optional | Default: `0`<br>Should provide choice of measurement (e.g. inches, cm, feet, etc) based on imperial or metric in personal settings |
| `height_min` | Integer | Minimum height | 0-999 | ❌ Optional | Default: `0`<br>Should provide choice of measurement (e.g. inches, cm, feet, etc) based on imperial or metric in personal settings |
| `height_max` | Integer | Maximum height | 0-999 | ❌ Optional | Default: `0`<br>Should provide choice of measurement (e.g. inches, cm, feet, etc) based on imperial or metric in personal settings |
| `suggested_container_size` | Integer | Container size | 0-999 | ❌ Optional | Default: `0`<br>Should provide choice of measurement in gallons or liters (metric or imperial) |
| `medicinal_benefits` | Choice | list of alleged medicinal benefits & properties | Any string | ❌ Optional | These benefits could be on any plant. If no plants, it should not be listed as a possible medicinal benefit. |
| `germination_days` | Integer | Days to germination | 0-999 days | ❌ Optional | Default: `0` |
| `maturity_days` | Integer | Days to maturity | 0-999 days | ❌ Optional |Default: `0` |

<!-- --8<-- [end:plant-field-ref] -->

### Plant Type Choices

<!-- --8<-- [start:plant-type] -->

| Code | Description |
|------|-------------|
| `an` | Annual |
| `bi` | Biennial |
| `pe` | Perennial |
| `tp` | Tender Perennial |
| `sh` | Shrub |
| `tr` | Tree |
| `vi` | Vine |
| `un` | Unknown |

<!-- --8<-- [end:plant-type] -->

### Exposure Choices

<!-- --8<-- [start:sun-exposure] -->

| Code | Description |
|------|-------------|
| `fs` | Full Sun (6+ hours) |
| `fp` | Full to Partial Sun (4-6 hours) |
| `pu` | Partial Sun (morning, 4-6 hours) |
| `pd` | Partial Shade (morning, ≤4 hours) |
| `sh` | Shade |

<!-- --8<-- [end:sun-exposure] -->

### Plant Boolean Flags

<!-- --8<-- [start:plant-boolean-flags] -->

All boolean fields accept `0` (false) or `1` (true):

- `is_hybrid` - Hybrid variety
- `is_deadhead_suggested` - Remove spent flowers for continued blooming
- `is_good_for_border` - Suitable for garden borders
- `is_good_for_container` - Suitable for container gardening
- `is_good_for_landscape` - Suitable for landscape planting
- `is_good_for_rock_garden` - Suitable for rock gardens
- `is_good_for_shrubs` - Suitable for shrub borders
- `is_butterfly_attractor` - Attracts butterflies
- `is_pollinator_friendly` - Attracts pollinators (bees, hummingbirds)
- `is_deer_resistant` - Deer tend to avoid
- `is_mosquito_repellent` - Repels mosquitoes
- `is_rabbit_resistant` - Rabbits tend to avoid
- `is_drought_tolerant` - Tolerates drought conditions
- `is_heat_tolerant` - Tolerates high heat
- `is_earth_kind` - Earth-Kind certified variety
- `is_waterwise` - Efficient water usage
- `is_organic` - Organic variety
- `is_non_gmo` - Non-GMO variety

<!-- --8<-- [end:plant-boolean-flags] -->

### Management Command

**File**: `2024-Django-Attempt/Plants/management/commands/load_plants.py`

```bash
# Load plants from CSV
python manage.py load_plants docs/data/initial_plants.csv

# Clear existing plants and reload
python manage.py load_plants docs/data/initial_plants.csv --clear
```

---

## Handling Relationships

### PlantLinks (Many-to-Many)

**Model**: `PlantLink` (`2024-Django-Attempt/Plants/models.py:123-166`)

PlantLinks represent external resources related to plants (articles, videos, books, nursery info).

#### Approach 1: Separate CSV for PlantLinks

Create `docs/data/initial_plant_links.csv`:

```csv
title,url,type,plant_common_names
"Growing Tomatoes - Extension Guide",https://extension.example.edu/tomatoes,aa,"Tomato"
"Best Herbs for Beginners",https://gardening.example.com/herbs-guide,bl,"Basil|Rosemary|Lavender"
"Marigolds as Companion Plants",https://www.youtube.com/watch?v=example,yt,"Marigold"
"Johnny's Selected Seeds - Zinnia",https://johnnyseeds.com/zinnia,nu,"Zinnia"
```

**Link Type Codes**:
- `aa` - Academic Article
- `bl` - Blog
- `bk` - Book
- `mg` - Master Gardener
- `nu` - Nursery Information
- `yt` - YouTube
- `ot` - Other

#### Management Command for PlantLinks

Create `2024-Django-Attempt/Plants/management/commands/load_plant_links.py`:

```python
"""
ABOUTME: Django management command to load PlantLinks from CSV
ABOUTME: Associates resource links with plants using common names
"""
import csv
from django.core.management.base import BaseCommand
from Plants.models import Plant, PlantLink


class Command(BaseCommand):
    help = 'Load plant links from CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to CSV file with plant link data'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing plant links before loading'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        if options['clear']:
            self.stdout.write('Clearing existing plant links...')
            PlantLink.objects.all().delete()

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            created_count = 0

            for row in reader:
                # Create the PlantLink
                plant_link = PlantLink.objects.create(
                    title=row['title'],
                    url=row['url'],
                    type=row['type']
                )

                # Associate with plants (pipe-delimited list)
                plant_names = row['plant_common_names'].split('|')
                for name in plant_names:
                    name = name.strip()
                    try:
                        plant = Plant.objects.get(name_common=name)
                        plant_link.plant.add(plant)
                        self.stdout.write(f'  Linked to: {plant.name_common}')
                    except Plant.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f'  Plant not found: {name}')
                        )

                created_count += 1
                self.stdout.write(f'Created link: {plant_link.title}')

        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {created_count} plant links'
        ))
```

**Usage**:
```bash
python manage.py load_plant_links docs/data/initial_plant_links.csv
```

---

### Nurseries (Many-to-Many)

**Model**: `Nursery` (`2024-Django-Attempt/Plants/models.py:9-18`)

Nurseries represent suppliers or sources for plants.

#### Approach: Separate CSV for Nurseries

Create `docs/data/initial_nurseries.csv`:

```csv
name,url,plant_common_names
"Johnny's Selected Seeds",https://johnnyseeds.com,"Tomato|Basil|Zinnia"
"Burpee",https://burpee.com,"Marigold|Zinnia|Black-Eyed Susan"
"High Country Gardens",https://highcountrygardens.com,"Lavender|Purple Coneflower|Black-Eyed Susan"
"Mountain Valley Growers",https://mountainvalleygrowers.com,"Rosemary|Lavender|Basil"
```

#### Management Command for Nurseries

Create `2024-Django-Attempt/Plants/management/commands/load_nurseries.py`:

```python
"""
ABOUTME: Django management command to load Nursery data from CSV
ABOUTME: Associates nurseries with plants they carry using common names
"""
import csv
from django.core.management.base import BaseCommand
from Plants.models import Plant, Nursery


class Command(BaseCommand):
    help = 'Load nurseries from CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to CSV file with nursery data'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing nurseries before loading'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        if options['clear']:
            self.stdout.write('Clearing existing nurseries...')
            Nursery.objects.all().delete()

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            created_count = 0

            for row in reader:
                # Create the Nursery
                nursery = Nursery.objects.create(
                    name=row['name'],
                    url=row['url']
                )

                # Associate with plants (pipe-delimited list)
                plant_names = row['plant_common_names'].split('|')
                for name in plant_names:
                    name = name.strip()
                    try:
                        plant = Plant.objects.get(name_common=name)
                        nursery.plants.add(plant)
                        self.stdout.write(f'  Added plant: {plant.name_common}')
                    except Plant.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(f'  Plant not found: {name}')
                        )

                created_count += 1
                self.stdout.write(f'Created nursery: {nursery.name}')

        self.stdout.write(self.style.SUCCESS(
            f'Successfully loaded {created_count} nurseries'
        ))
```

**Usage**:
```bash
python manage.py load_nurseries docs/data/initial_nurseries.csv
```

---

### Companion Plants (Self-Referential Many-to-Many)

**Note**: Currently commented out in the Plant model (`2024-Django-Attempt/Plants/models.py:99`)

When uncommented, companion plants represent beneficial plant pairings.

#### Future Approach: Separate CSV for Companion Plants

Create `docs/data/initial_companion_plants.csv`:

```csv
plant_common_name,companion_common_names
Tomato,"Basil|Marigold"
Basil,"Tomato"
Marigold,"Tomato|Zinnia"
Lavender,"Rosemary"
Rosemary,"Lavender"
```

#### Future Management Command

Create `2024-Django-Attempt/Plants/management/commands/load_companion_plants.py`:

```python
"""
ABOUTME: Django management command to load companion plant relationships
ABOUTME: Creates bidirectional relationships between companion plants
"""
import csv
from django.core.management.base import BaseCommand
from Plants.models import Plant


class Command(BaseCommand):
    help = 'Load companion plant relationships from CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'csv_file',
            type=str,
            help='Path to CSV file with companion plant data'
        )

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            relationship_count = 0

            for row in reader:
                try:
                    # Get the primary plant
                    plant = Plant.objects.get(
                        name_common=row['plant_common_name']
                    )

                    # Associate companion plants (pipe-delimited list)
                    companion_names = row['companion_common_names'].split('|')
                    for name in companion_names:
                        name = name.strip()
                        try:
                            companion = Plant.objects.get(name_common=name)
                            plant.companion_plants.add(companion)
                            relationship_count += 1
                            self.stdout.write(
                                f'{plant.name_common} → {companion.name_common}'
                            )
                        except Plant.DoesNotExist:
                            self.stdout.write(
                                self.style.WARNING(
                                    f'  Companion not found: {name}'
                                )
                            )

                except Plant.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Plant not found: {row["plant_common_name"]}'
                        )
                    )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully created {relationship_count} companion relationships'
        ))
```

**Usage**:
```bash
python manage.py load_companion_plants docs/data/initial_companion_plants.csv
```

---

## Complete Workflow Examples

### Example 1: Fresh Database Setup

```bash
# 1. Load plants first (relationships require plants to exist)
python manage.py load_plants docs/data/initial_plants.csv

# 2. Load nurseries and associate with plants
python manage.py load_nurseries docs/data/initial_nurseries.csv

# 3. Load plant links and associate with plants
python manage.py load_plant_links docs/data/initial_plant_links.csv

# 4. (Future) Load companion plant relationships
# python manage.py load_companion_plants docs/data/initial_companion_plants.csv
```

### Example 2: Reset and Reload

```bash
# Clear and reload everything
python manage.py load_plants docs/data/initial_plants.csv --clear
python manage.py load_nurseries docs/data/initial_nurseries.csv --clear
python manage.py load_plant_links docs/data/initial_plant_links.csv --clear
```

### Example 3: Add New Plants

```bash
# Add new plants to initial_plants.csv, then run:
python manage.py load_plants docs/data/initial_plants.csv

# Note: Without --clear, this appends new plants (no duplicates if same name_common)
```

---

## Best Practices

### Data Organization

```
docs/data/
├── initial_plants.csv              # Core plant data
├── initial_plant_links.csv         # Plant resource links
├── initial_nurseries.csv           # Nursery suppliers
└── initial_companion_plants.csv    # Companion plant relationships (future)
```

### CSV Editing Best Practices

1. **Use spreadsheet software** - Excel, Google Sheets, LibreOffice Calc
2. **UTF-8 encoding** - Ensure special characters display correctly
3. **Escape commas in descriptions** - Use quotes: `"Description with, commas"`
4. **Test incrementally** - Add a few plants, test load, then add more
5. **Version control** - Commit CSV files to git after validating data

### Validation Strategy

1. **Load small batches first** - Test with 5-10 plants initially
2. **Check Django admin** - Verify data appears correctly
3. **Test queries** - Ensure filters and searches work as expected
4. **Validate relationships** - Check that PlantLinks and Nurseries are associated

### Data Maintenance

1. **Single source of truth** - CSV files are the canonical source
2. **Reload from CSV** - Use `--clear` flag to reset database to CSV state
3. **Document changes** - Add comments to CSV (in a separate column if needed)
4. **Backup before major changes** - Export current database before large updates

---

## Troubleshooting

### Common Issues

#### Issue: "Plant not found" when loading relationships

**Cause**: Referenced plant doesn't exist in database

**Solution**:
```bash
# Ensure plants are loaded first
python manage.py load_plants docs/data/initial_plants.csv

# Then load relationships
python manage.py load_plant_links docs/data/initial_plant_links.csv
```

#### Issue: Duplicate plants on reload

**Cause**: Running load command without `--clear` flag

**Solution**:
```bash
# Use --clear to remove existing plants first
python manage.py load_plants docs/data/initial_plants.csv --clear
```

#### Issue: Boolean fields not saving correctly

**Cause**: Using `True`/`False` instead of `1`/`0` in CSV

**Solution**: Use `0` for false, `1` for true in CSV files

#### Issue: CSV encoding errors

**Cause**: File not saved as UTF-8

**Solution**:
- In Excel: Save As → CSV UTF-8 (Comma delimited) (*.csv)
- In Google Sheets: Download as CSV (automatically UTF-8)

#### Issue: Commas in description field breaking CSV

**Cause**: Unescaped commas in text fields

**Solution**: Wrap fields with commas in quotes:
```csv
"Description with, commas inside",0,1,0
```

### Debugging Commands

```bash
# Check how many plants loaded
python manage.py shell
>>> from Plants.models import Plant
>>> Plant.objects.count()

# Check specific plant data
>>> plant = Plant.objects.get(name_common='Tomato')
>>> print(plant.description)
>>> print(plant.is_pollinator_friendly)

# Check relationships
>>> from Plants.models import PlantLink
>>> link = PlantLink.objects.first()
>>> link.plant.all()  # Shows all associated plants
```

---

## Next Steps

1. **Populate `docs/data/initial_plants.csv`** - Add your plants (use provided template)
2. **Test basic loading** - Run `python manage.py load_plants docs/data/initial_plants.csv`
3. **Create relationship files** - When ready, create `initial_plant_links.csv` and `initial_nurseries.csv` in `docs/data/`
4. **Create management commands** - Implement `load_plant_links.py` and `load_nurseries.py`
5. **Document your process** - Add notes to this guide as you discover improvements

---

## Related Documentation

- **Plant Model**: `2024-Django-Attempt/Plants/models.py`
- **Dependency Management**: `docs/tutorials/general/dependency-management.md`
- **Makefile Guide**: `docs/tutorials/general/makefile-guide.md`
- **MVP Planning**: `docs/decisions/planning/SDD-Planning_MVP.md`

---

**Last Updated**: 2025-12-27
