Generate specs for a gardener app using @templates/spec-template.md Build the specs in such a way that the different pieces or milestones can be built independently instead of all at once.

This app will have 3 main sections that people might be able to engage with. Section 1 is the main item that all users can access. This GeneralUser section is the main portion of the app related to plants and details about how and when to grow, tend, and harvest based on one's zone. There are weather alerts based onyour location, notifications, ability to save settings, and more for this      
level of access.

The next level of access are the community garden groups. They will have special level of access to their assigned community garden(s) but not to others. Each GardenGroup will have different teams (such as compost, orchard, etc) where they will only be able to make changes to that particular team's information if they are on the team. There will be a community notifications board so people are aware of announcements and more for their community.

The final level of access is only for administrators - AdminAccess portion that allows only certain people to be able to create the different community GardenGroup groups.

This spec should be saved to general-app-spec.md in @specs/ folder.

# Context
- access to admin panel is through a menu option\
- default screen is the plant database with search & favorites ability\
- used by gardeners of all skill and experience levels for planning & caring for plants in their area\
- some sections used by community garden members to more effectively collaborate & communicate\

# Requirements

## Plant Database
- show: common name, scientific name, germination information, planting information, etc\
- able to search by plant properties, favorites, and growing zone
## General
- responsive design (mobile and desktop)
- async and mobile focused
- API to share plant information
- weather widget
# Constraints
- Python Django
- Next.js 15 App Router with React 19
- Tailwind for CSS styling
- Props:  plant object with typed interface

Be sure to split this up so that the first spec is teh general layout of the app with placeholders for the different needs. These placeholders will be dynamically updated when the component is ready. Each major component for this application should have it's own spec doc so each piece can be worked on a piece at a time.