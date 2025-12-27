# Initial Plant View

Due to the amount of data, please note that we are only showing a few columns from the related datasets.

Please review [mkdocs-extensions-guide](../tutorials/mkdocs/mkdocs-extensions-guide.md#mkdocs-table-reader-plugin---import-tables-from-external-files) for more on the table reader plugin utilized to create the below view.

## Initial Plant Data

When using the `[initial_plants.csv](../data/initial_plants.csv)` to display the below subset, we are only using the following columns:

- `name_common`
- `name_scientific`
- `plant_type`
- `exposure`

{{ read_csv('data/initial_plants.csv'), usecols=['name_common', 'name_scientific', 'plant_type', 'exposure'] }}