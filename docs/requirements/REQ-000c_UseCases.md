# Use Cases

## Actors

_See also the [stakeholders](./REQ-000a_General.md#stakeholders) section._

1.	General system user (no special access)
2.	Community Composter (non-member)
3.	Gardener – Community (Member)
4.	Gardener – Community (Supporter)
5.	Gardener – Community (Team Member)
6.	Gardener – Community (Chore Member)
7.	Gardener – Community (Gardener)
8.	Gardener – Community (Apprentice)
9.	City Admin – Community Lead
10.	System admin
11.	Volunteer Developer 

## UC Table

| ACTOR | ACTION | How Critical? (L/M/H) | UC Diagram (Miro) |
| --- | --- | --- | --- |
|  | Provides clear warnings if user tries to access locations they cannot and how they can (if it’s possible) | Low |  |
|  | If trying to access a part of the system that requires location information but only has USDA zone information, provides clear notice that a default location in their USDA zone will be chosen to provide potential responses for their true location. | Medium |  |
|  | The system monitors the weather (or periodically checks weather API) to provide warnings & suggestions for mitigating inclement weather risks. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607733520251&cot=14) |
|  | System utilizes USDA zone to suggest certain plants during particular times of the year based on their location. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | System utilizes USDA zone for user’s location to calculate first and last frost dates. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | System utilizes first and last frost dates to calculate estimated planting dates based on specific plant data. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | System provides reminders to plant based on user’s preferred plants, their location, and related frost dates. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) |
|  | System provides a way to filter plants based on user selection criteria (e.g.: color, seeding date, etc) | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | System provides historical weather to show average hot/cold & precipitation for each month. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607733520251&cot=14) |
|  | System provides a secure way for community garden groups to easily track their progress and know when / where additional help may be needed in the garden. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
|  | System provides an easy way to add, edit, or delete plants for a particular user. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) |
|  | Provides free resources to help gardeners have better crops. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | The system provides an area with affiliate links to additional resources. (e.g.: fish emulsion, hoop houses, etc) | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
|  | The system is extended by ensuring that inactive accounts effectively turn off all permissions except **general system user** permissions. | High |  |
|  | Track apprentice program action completion dates. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| general system user | Cannot access any community-specific training, materials, or special information that only members or specific teams can see UNLESS they are also a member of that community. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Searches for information on a specific plant. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Searches for information a plant’s companion plants. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Searches for plants based on specific criteria (e.g.: color, size, benefits, etc) | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Provides feedback or reports an error | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Provides current location to pull USDA zone information & suggested plants currently in the database that are within range of that zone | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Stores user specific data that can be retrieved later. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Saves and/or sends file to backup user’s local data (no login or security options needed) | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Utilizes login option of the system to create an account that syncs their user data. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Views current local weather conditions checked daily on first system access of the day OR on manual refresh via weather API | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607733520251&cot=14) |
| general system user | View suggestions for upcoming protection planning based on weather predictions checked daily on first system access of the day via weather API | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607733520251&cot=14) |
| general system user | Create, edit, delete plants for their personal (local) account. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) |
| general system user | Can submit plant suggestions for the main system that volunteer developers are able to approve and get automatically updated in the system. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| general system user | Able to track what plants were planted where and when. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) |
| general system user | Able to see a history of the plants they have planted & their related data, including but not limited to amount of shade. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) |
| general system user | Saves plants as favorites. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) |
| Any user that is more than just a **general system user** | Extra roles with their respective permissions extends the system. | High | multiple |
| Community Composter (non-member) | Includes all **general system user** actions & access is based on a unique community ID | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Community Composter (non-member) | Views all expected compost turning options in the community garden, including date, time, and contact for help. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Community Composter (non-member) | Turn on/off notifications about composting opportunities | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Includes all **general system user** actions & access is based on a unique community ID | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Includes all **Gardener – Community (Apprentice)** actions. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Manages visibility in relation to other community gardener members within their unique community. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Receives all general community garden notifications based on a unique community ID | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Posts in unique community bulletin a date with timeframe they are seeking help from others in the community. Can also indicate if it helps specific teams. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Turn on/off notifications about other community gardeners seeking help. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Access to monthly workday list of things that need to be done in the community garden. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Add to monthly workday list things that need to be done in the community garden. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Edit items they added to the workday list. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | View all items in the workday list. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Access community announcements. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Review data about their own tracked hours for teams or chores. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Turn on/off ability for other community garden members to see what teams or chores they are assigned to. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | View who is on what team or chore, if they allow themselves to be seen. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Turn on/off ability to be seen by other community members. (Does not apply to **City admins**.) | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Access to community's private apprentice training program | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Turn on/off ability for assigned mentor (if they have one) to view progress in apprentice training program. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Mark when completed tasks within the apprentice training program. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Watch or review any community garden specific materials | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | View all available compost turning dates & times | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Turn on/off notifications about composting opportunities. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | View all in person training announcements provided by mentor team. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Create announcement of any class they are giving the community would enjoy – including date, time, and location. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (member) | Notifies Mentor team of plot release & updates available plots | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (member) | Notifies Mentor team of plot request | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Supporter) | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Supporter) | Checks for any special events at the community garden people provide notice of. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Supporter) | Views available plots | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Supporter) | Create plot support request gardeners can reach out to | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
|  | Notifies plot owner of support request / release | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Team Member) | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Team Member)<br>_Communications Team_ | Create community announcement that all unique community members will get notified of when they next open the system. (Archives found in a single location with a time limit for storage.) | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Team Member)<br>_Compost Team_ | Create, edit, or delete compost event. Notifies Compost Supporters, compost team members, & other community gardeners who have this turned on. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Member) | View who is assigned upcoming deliveries to where. Self-assign for delivery if empty. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Team Member)<br>_Delivery Team_ | Add their name to a delivery timeslot that is not already taken. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Educator) | Builds out training content & ensures proper access as required. | High | Multiple diagrams |
| Gardener – Community (Team Member)<br>_Mentor Team_ | Assign mentor to mentee (only 1 mentor to 1 mentee) | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Member) | View assigned mentor & turn on/off their ability to see progress. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Team Member)<br>_Mentor Team_ | Review their assigned mentee’s apprentice training progress (if they have shared with their mentor) | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Team Member)<br>_Mentor Team_ | Create, edit, or delete own training announcements for required trainings for apprentice graduation that all members can see. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Team Member)<br>_Plot Team_ | View plot requests | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Team Member)<br>_Plot Team_ | Approve plot requests | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Team Member)<br>_Plot Team_ | Create / remove plot availability announcements | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| … | … | … |  |
| Gardener – Community (Chore Member) | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Chore Member) | Track time spent on their chore or team. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| Gardener – Community (Gardener) | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Gardener) | Views available plots | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Gardener) | Complete plot request for ownership | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Gardener) | Requests release of plot, which alerts another team to complete the process | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Gardener) | Create plot support requests to alert supporters if they are needed. | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Apprentice) | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Apprentice) | Includes all **Gardener – Community (Supporter)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Apprentice) | Views available plots | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Apprentice) | Complete plot request for ownership | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Apprentice) | Requests release of plot, which alerts another team to complete the process | Low | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) |
| Gardener – Community (Apprentice) | View personal progress within apprentice training program. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| Gardener – Community (Apprentice) | Receive notification of in-person training announcements for required trainings for apprentice graduation. It will be in their announcements section, but if they are missing that option in their progress it will also be a banner reminder to check training requirement item in announcements. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| City Admin – Community Lead | Includes all **Gardener – Community (member)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) |
| City Admin – Community Lead | Includes all **Gardener – Community (Team Member - Communications)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| City Admin – Community Lead | View all community garden members of their assigned community. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| City Admin – Community Lead | Assigns teams & chores to their community gardeners. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| City Admin – Community Lead | Mark community garden members as inactive – this means they are effectively back to **general system user** only. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| City Admin – Community Lead | Edit anything in the workday list for their specific community | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| City Admin – Community Lead | View apprentice training program progress of any community garden member in their assigned community. | Medium | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) |
| System admin | Includes all **general system user** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| System admin | Includes all **Gardener – Community (Educator)** actions | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| System admin | Creates city admin accounts | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| System admin | Manages all accounts | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) |
| Volunteer Developer | Uses GitHub & GitHub Actions to improve the code behind the app, including but not limited to approvals of plants to the database | High |  |
| Volunteer Developer | Writes & utilizes unit tests to ensure proper working system with at least 80% of testing covered. | High |  |

The next few sections will be to provide the use case diagrams of different users and roles.
Use cases were originally identified because they were one or more of the following:

- High-level use cases & high priority

- Sub-use cases included in high level user case

- Special cases extending other use cases

## Use Case Behavior Diagrams

All latest updates are in [this location](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764609898919690&cot=14) of the related Miro board.

### General System User

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) for the specific actor:  **General System User**

![Use Case Diagram:  General System User](/docs/diagrams/REQ000/UC_General-System-User.jpg)

### General Use Component:  Weather

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607733520251&cot=14) for the specific internal system component:  **Weather**

![Use Case Diagram:  Weather Component](/docs/diagrams/REQ000/UC_Weather.jpg)

### General Use Component:  Saving Plants

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607734155500&cot=14) for the specific internal system component:  **Saving Plants Component**

![Use Case Diagram:  Saving Plants Component](/docs/diagrams/REQ000/UC_Saving-Plants.jpg)

### Elevated User Component:  System Admin, Community Lead, Educator

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) for the specific actor:  **System Admin (+ special access needs)**

![Use Case Diagram:  Elevated Access Component](/docs/diagrams/REQ000/UC_Elevated-Users.jpg)

### Community Role Component:  General Member

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) for the specific actor:  **Gardener – Community (Member)**

![Use Case Diagram:  Community Garden (Member)](/docs/diagrams/REQ000/UC_Community-Gardener-Member.jpg)

### Community Role Component:  Role Assignment (Team or Chore)

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) for the specific actor:  **Gardener – Community (assigned team or chore)**

![Use Case Diagram:  Community Garden Team / Chore](/docs/diagrams/REQ000/UC_Community-Gardener-TeamAndChores.jpg)

### Community Role Component:  Plot Assignment

Here is the [use case diagram](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607743142890&cot=14) for the specific actor:  **Gardener – Community (Plots)**

![Use Case Diagram:  Community Garden (Plot Assignment)](/docs/diagrams/REQ000/UC_PlotAssignments.jpg)
