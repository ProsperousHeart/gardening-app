# Data Directory

**Purpose**: Store initial seed data for database population

---

## Files

### `initial_plants.csv`

**Template for initial plant data** to seed the Plant model.

**Usage**:

```bash
python manage.py load_plants docs/data/initial_plants.csv
python manage.py load_plants docs/data/initial_plants.csv --clear  # Reset database
```

**Column Reference**:

The below information comes from the [Database Seeding Guide](../tutorials/general/database-seeding-guide.md#plant-field-ref).

--8<-- "tutorials/general/database-seeding-guide.md:plant-field-ref"

**Plant Type Codes**:

The below information comes from the [Database Seeding Guide](../tutorials/general/database-seeding-guide.md#plant-type-choices).

--8<-- "tutorials/general/database-seeding-guide.md:plant-type"

**Exposure Codes**:

The below information comes from the [Database Seeding Guide](../tutorials/general/database-seeding-guide.md#exposure-choices).

--8<-- "tutorials/general/database-seeding-guide.md:sun-exposure"

**Boolean Flags** (18 total):

The below information comes from the [Database Seeding Guide](../tutorials/general/database-seeding-guide.md#plant-boolean-flags).

--8<-- "tutorials/general/database-seeding-guide.md:plant-boolean-flags"

---

### Future Files

**These will be added when relationship handling is implemented:**

- `initial_plant_links.csv` - External resources (articles, videos, books)
- `initial_nurseries.csv` - Nursery suppliers and sources
- `initial_companion_plants.csv` - Beneficial plant pairings

See [`docs/tutorials/general/database-seeding-guide.md`](../tutorials/general/database-seeding-guide.md) for complete tutorial on handling relationships.

---

## Workflow

### Initial Setup

```bash
# 1. Edit initial_plants.csv with your plant data
# 2. Load plants into database
python manage.py load_plants docs/data/initial_plants.csv

# 3. Verify in Django shell
python manage.py shell
>>> from Plants.models import Plant
>>> Plant.objects.count()
>>> Plant.objects.get(name_common='Tomato')
```

### Adding New Plants

```bash
# 1. Add new rows to initial_plants.csv
# 2. Load without --clear to append
python manage.py load_plants docs/data/initial_plants.csv
```

### Reset Database

```bash
# Clear and reload all plants
python manage.py load_plants docs/data/initial_plants.csv --clear
```

---

## Best Practices

1. **UTF-8 Encoding** - Save CSV files as UTF-8 to preserve special characters
2. **Escape Commas** - Wrap descriptions with commas in quotes: `"Description, with commas"`
3. **Use Notes Column** - Add internal notes that won't be loaded to database
4. **Test Incrementally** - Add a few plants, test load, then add more
5. **Version Control** - Commit CSV files to git after validating data

---

## Related Documentation

### Requirements

- **Plant Database Scope**: [REQ-000b_Scope](../requirements/REQ-000b_Scope.md#starting-deliverable--plant-database) - Formal data needs and requirements
- **Data Management Requirements**: [REQ-000e_Requirements](../requirements/REQ-000e_Requirements.md) - CSV loading, validation, and integrity (OR3.N - OR7.N)

### Implementation Guides

- **Complete Seeding Guide**: `docs/tutorials/general/database-seeding-guide.md`
- **Plant Model**: `2024-Django-Attempt/Plants/models.py:21-104`
- **MVP Planning**: `docs/decisions/planning/SDD-Planning_MVP.md`
