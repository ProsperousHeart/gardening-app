# Use Case Behavior Diagrams

This file is a continuation of the [Use Cases](./REQ-000c_UseCases.md) file. It will provide the behavior diagrams of the different use cases.

This section is not yet complete as of December 2024. This is a working document, as progression is made throughout the solution based on prioritized work.

Excluding the [Guidelines](#ucbd-guidelines) & [Template](#ucbd-template) sections, each section below relates to a specific sub-system as outlined in the [Scope Tree](/docs/requirements/REQ-000b_Scope.md#scope-tree):

1.	General User

2.	Admin Access

3.	Community Member


## Identifying Top High Priority Use Cases

When identifying high use case needs for this course, consider ones that:

- Directly address stakeholder's primary needs

- Have a significant influence on the performance of your system

- Address situations considered to be high risk, including ones that focus on undesired occurrences

- Require your system to perform complex and important tasks

- Occur very frequently

The XLSX for this is here.

| PRIORITY | ACTOR | ACTION | How Critical? (H/M/L) | UC Diagram (miro) | UCBD |
| --- | --- | --- | --- | --- | --- |
| 1 | general system user | Searches for information on a specific plant. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) | Plant Search |
| 2 | general system user | Provides feedback or reports an error | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) | 1. Gives Feedback<br>2. Reports Error |
| 3 | System admin | Manages all accounts | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) | 1. Create Community Lead<br>2. Add Community Lead<br>3. Make Account Inactive for Specific Community<br>4. Create general user account<br>5. Delete account |
| 4 | System admin | Creates city admin accounts | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607727412356&cot=14) | See #3’s #1 |
| 5 | Gardener – Community (member) | Access community announcements. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) | Access Announcements |
| 6 | Gardener – Community (member) | Includes all **general system user** actions & access is based on a unique community ID | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) | ? |
| 7 | general system user | Cannot access any community-specific training, materials, or special information that only members or specific teams can see UNLESS they are also a member of that community. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) | ? |
| 8 | City Admin – Community Lead | Assigns teams & chores to their community gardeners. | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607735882431&cot=14) | ? |
| 9 | Gardener – Community (member) | Turn on/off ability to be seen by other community members. (Does not apply to **City admins**.) | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607446135000&cot=14) | ? |
| 10 |  | System provides a way to filter plants based on user selection criteria (e.g.: color, seeding date, etc) | High | [here](https://miro.com/app/board/uXjVLFJo2wg=/?moveToWidget=3458764607290502924&cot=14) | Plant Filtering |

## UCBD Guidelines

1.	Write as shall statements

2.	Write as correct statements (what you’re saying is accurate)

3.	Write clear & precise statements
    - One idea per requirement
    - If “and” or similar conjunction in requirements, considered better to split

4.	Write unambiguous statements (only 1 way to interpret)

5.	Write objective statements (if anything is subjective, qualify with some quantifiable measure)

6.	Write verifiable statements (some measurable way to say requirement is met)

7.	Write consistent statements (does not contradict another requirement)

Some organizations may also include the following as their best practices:

1.	Implementation independent (functional, not structural)

2.	Achievable (feasible)

3.	Conforming (consistent with regulations imposed by stakeholders & any other governing entity)

## UCBD Template

_**NOTE:**  Utilize mermaid documentation [here](https://mermaid.js.org/syntax/sequenceDiagram.html) when designing your SysML to work within MarkDown and on GitHub_

**Use Case Name:**  TBD

**Initial Conditions:**

1. TBD

```mermaid
---
title: Title Here
config:
    theme: dark
---
sequenceDiagram
    autonumber
    actor User as Human
    participant System as "The System"
    %% links System: {"Requirements": ""}
    User->>+System: Step 1
    System-->>User: Step 2 ...
```
<br>

**Ending Conditions:**

1. TBD

**Notes:**

1. TBD

## System Actions

The subitems in this section all belong to the GeneralUser system actions set.

### GPS Permissions

**Use Case Name:**  System Requests Access to GPS – Get User Approval

**Initial Conditions:**

1. First time running the system as a new user or user tries to use GPS modules within the app (e.g.: checking weather, turning on weather-based gardening notifications) without permissions

**Mermaid Diagram:**

```mermaid
---
title: System Requests Access to GPS – Get User Approval
config:
    theme: dark
---
sequenceDiagram
    autonumber
    actor User as Human
    participant System as "The System"
    %% links System: {"Requirements": ""}
    User->>+System: One of the initial conditions are triggered.
    System->>Settings: Checks if GPS permissions approved
    Settings-->>System: Returns FALSE
    System-->>User: The system asks if the user would like to use GPS<br />to determine USDA zone (where applicable)<br>and local regional weather updates.
    User->>System: User chooses to automate their USDA zone via GPS.
    System-->>User:  System requests GPS permissions with information on how the data will be used.
    User->>System: User approves GPS permissions.
    System->>Settings: Updates GPS permissions
    Settings-->>System: Returns GPS settings
    System-->>-User: System provides a notice inquiring if the user wants the system<br>to always be scanning GPS if it’s on, only check once a day (and if so when),<br>or only when they manually request updates requiring GPS (default).
    User->>+System: User provides GPS preference settings.
    System->>Settings: Updates GPS settings
    Settings-->>System: Returns GPS settings
    System-->>-User: System provides a thank you message with reminder that weather updates<br>for gardening alerts will only work when GPS is turned on & that<br>they can change their preferences under their settings.
    User->>System: User closes notification & if no prior screen to return to is returned to “home”.
```
<br>

**Ending Conditions:**

1. GPS permissions are turned on
2. Unique user’s profile has auto-update USDA zone turned on
3. Unique user’s USDA zone field is filled in and user unable to edit
4. Unique user’s profile settings are set to user’s preference and editable in their profile

**Notes:**

1. Need to create a general system UCBD for when user declines.
2. Need to ensure that use case diagrams & scope trees are updated, as the GPD settings is new.
3. “home” is either their profile or an area user can locate all components they have access to.

**Identifying Missed Functionality:**

| Additional Grouping of Requirements | Description |
| ----------------------------------- | ----------- |
| \* | “System checks for approval” |
| \*\* | “System notifies user” |
| \*\*\* | “System uses GPS data for weather or USDA zone needs” |

Identifying Missed Functionality – the system shall be able to:
- *Check if GPS permissions are approved
- **Notify user when GPS is required and not yet approved
- **If unable to connect to GPS, notify user
- **If unable to connect to GPS and no USDA zone saved, will force user to manually provide USDA zone
- ***(with proper permissions & based on frequency settings) automatically check GPS when attempting to pull current or past weather data
- ***will ensure either GPS or manual USDA zone is utilized


## General User Actions

### ?

?

### ?

?

### ?

?

### ?

?

### ?

?

### ?

?

### ?

?

## Admin (Elevated User) Access

### ?

?

### ?

?

### ?

?

### ?

?

### ?

?

## Community Member

This is not fully fleshed out at the moment, as there are some elevated user access to be considered.

### ?

?
