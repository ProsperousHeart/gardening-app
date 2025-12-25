# Requirements Definition

This is the centralized information related to the requirements outlined in [UCBDs](/docs/requirements/REQ-000d_UCBDs.md) file.

## Legend

### Template

| Component | Unique ID | Description |
| --- | --- | --- |
| **System.SubComponent.Deliverable** | ORX.N | TBD |

### Example

| Component | Unique ID | Description |
| --- | --- | --- |
| **System.GenUser.PlantSearch** | OR1.N | Used for original requirements of the **plant search** component all users have access to. |
| **System.GenUser.PlantFilter** | OR2.N | Used for original requirements of the **plant search filtering** component all users have access to. |
| **TBD** | OR3.N | TBD |

## Full Requirements Table

| Component | Deliverable | Deliverable Unique ID | Requirement Unique ID | Description |
| --- | --- | --- | --- | --- |
| **System.GenUser** | Plant Search | OR.1 | OR1.1 | The system shall display the plant list view with **max_visible_plants_num** showing in the same state the user last searched for a plant. | display_plants_all |
| **System.GenUser** | Plant Search | OR.2 | OR1.2 | The system shall filter out all plants that do not at least partially match the search term. | plant_search_by_name |
| **System.GenUser** | Plant Search | OR.3 | MULTI | If no plants in the database match search criteria, the system shall provide a clear message about this to the user. | msg_plant_404 |
| **System.GenUser** | Plant Filter | OR.4 | OR2.1 | The system shall show all plants that match 1 or more criteria. | filter_any |
| **System.GenUser** | Plant Filter | OR.5 | OR2.2 | The system shall only show plants that match all requested criteria. | filter_exact |
