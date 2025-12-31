---
title: Specification Driven Development Process
description: The process and workflow for SDD (specification driven development) in this project.
---
# SDD Process

!!! info
    Status as of 20251224.

This document tracks the development and refinement of the Specification-Driven Development (SDD) workflow used in this project.

**Tool Focus**: Currently optimized for Claude Code. Once v1 workflow is validated, will adapt for GitHub Copilot compatibility.

---

## General Spec Creator

To get the general spec made:

1. ensured the [spec-template.md](./templates/spec-template.md) was made

2. ran `/init` for Claude to pick up on what I've already built out for reference

3. created the [general-app-spec-ORIGINAL.md](./specs/general-app-spec-ORIGINAL.md)

4. created [`general-app-requirements`](../docs/requirements/for-sdd/general-app-requirements.md)

   ```
   Generate specs for a gardener app using @templates/spec-template.md Build the specs in such a way that the different pieces or milestones can be built independently instead of all at once.

   This app will have 3 main sections that people might be able to engage with. Section 1 is the main item that all users can access. This GeneralUser section is the main portion of the app related to plants and details about how and when to grow, tend, and harvest based on one's zone. There are weather alerts based onyour location, notifications, ability to save settings, and more for this level of access.

   The next level of access are the community garden groups. They will have special level of access to their assigned community garden(s) but not to others. Each GardenGroup will have different teams (such as compost, orchard, etc) where they will only be able to make changes to that particular team's information if they are on the team. There will be a community notifications board so people are aware of announcements and more for their community.

   The final level of access is only for administrators - AdminAccess portion that allows only certain people to be able to create the different community GardenGroup groups.

   This spec should be saved to general-app-spec.md in @specs/ folder.

   # Context
   - access to admin panel is through a menu option
   - default screen is the plant database with search & favorites ability
   - used by gardeners of all skill and experience levels for planning & caring for plants in their area
   - some sections used by community garden members to more effectively collaborate & communicate

   # Requirements

   ## Plant Database
   - show: common name, scientific name, germination information, planting information, etc
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
   ```

5. created command `make-spec-from-req.md`

   ```
   ---
   argument-hint: [component-name] [req-file]
   description:  Create a spec file from requirements file
   ---

   ## Context

   - TBD

   ## Your Task

   Generate a spec for $1 using @templates/spec-template.md and $2

   Add a section to your spec titled "Integration Architecture" that includes:
   - component interaction diagram (in text/markdown)
   - data flow description
   - key integration points
   - dependencies on previously created specs
   ```

6. ran the following in Claude for optimization of command:

   ```
   How might I improve @commands\make-spec-from-req.md to build a spec from @templates\spec-template.md and  a requirement file? how should requirement file be set up? Please provide an example template in @templates
   ```

7. ```
   Generate a spec for a gardener app. This app will have 3 main sections that people might be able to engage
   with. Section 1 is the main item that all users can access. This GeneralUser section is the main portion of
   the app related to plants and details about how and when to grow, tend, and harvest based on one's zone.
   There are weather alerts based onyour location, notifications, ability to save settings, and more for this
   level of access.\
   \
   The next level of access are the community garden groups. They will have special level of access to their
   assigned community garden(s) but not to others. Each GardenGroup will have different teams (such as compost,
   orchard, etc) where they will only be able to make changes to that particular team's information if they
   are on the team. There will be a community notifications board so people are aware of announcements and more
   for their community.\
   \
   The final level of access is only for administrators - AdminAccess portion that allows only certain people
   to be able to create the different community GardenGroup groups.\
   \
   This spec should be saved to general-app-spec.md in @specs/ folder.\
   \
   # Context\
   - access to admin panel is through a menu option\
   - default screen is the plant database with search & favorites ability\
   - used by gardeners of all skill and experience levels for planning & caring for plants in their area\
   - some sections used by community garden members to more effectively collaborate & communicate\
   \
   # Requirements\
   ## Plant Database\
   - show: common name, scientific name, germination information, planting information, etc\
   - able to search by plant properties, favorites, and growing zone\\
   ## General
   - responsive design (mobile and desktop)\
   - async and mobile focused\
   - API to share plant information\
   - weather widget\
   # Constraints\
   - Python Django\
   - Next.js 15 App Router with React 19\
   - Tailwind for CSS styling\
   - Props:  plant object with typed interface\
   \
   Be sure to split this up so that the first spec is teh general layout of the app with placeholders for the different needs. These placeholders will be dynamically updated when the component is ready. Each major component for this application should have it's own spec doc so each piece can be worked on a piece at a time.
   ```

## Developing Requirements

This section is not to explain how [REQ-000x](./requirements/) markdown files - those were developed with the original project description & stakeholders in mind.

The current section is to walk you through what I did to build out the repo after I:

- took what I learned from a specification driven development workshop (similar to digitized delivery) and created my own base from it
- got an initial outline for MVP planning with help of AI - still need to complete review & update as needed for appropriate MVP plan

This is still being worked on, but you can see the initial documentation [here](./requirements/README.md).

After developing the [scope](./requirements/REQ-000b_Scope.md) and others, able to determine that there are 3 main modules or sub-systems as outlined in [here](./requirements/req-by-subsys-idx.md). This is what determines the part after REQ or SPEC in the file name. Then the portion after that is the individual requirement. For example:  `req_genuser_plant-search`

I was then able to use this and the mkdocs metadata to my advantage to automatically generate indexes with interactive tables for showing the files.

As I continued to improve on what I wanted my own dashboard and documentation to look like in preparation for the SDD work, I continued learning several new amazing things. I then would utilize AI recap to create tutorials or lessons learned, often tweaking or correcting the process and my exeperiences.

---

## Historical Context

This section preserves the history of how this SDD workflow was developed and refined.

### Developing Requirements

This section documents the background of requirement development, not the current workflow.

The REQ-000x markdown files were developed with the original project description and stakeholders in mind, based on:

- Specification-driven development workshop learning (similar to digitized delivery)
- Initial MVP planning with AI assistance
- Cornell's Systems Design certification program methodology

The current requirement creation workflow is documented in **Phase 1** above.

**Initial documentation**: [requirements/README.md](./requirements/README.md)

### Evolution of Process Documentation

This document has evolved from tracking ad-hoc steps to documenting a comprehensive, repeatable SDD workflow:

**Version 1 (Initial)**: Manual, exploratory approach

- Created templates
- Manually generated specs
- Ad-hoc command creation

**Version 2 (Workflow Commands)**: Automation begins

- Created `/make-spec-from-req` command
- Automated spec generation
- Manual architecture and threat modeling

**Version 3 (Orchestration)**: Complete automation

- Workflow orchestration prompts
- Multiple artifacts generated together
- Approval gates added

**Version 4 (Current)**: Modular process documentation

- Process snippets for each phase
- Clear workflow order
- Comprehensive documentation

---

## Related Documentation

See the final optimized workflow via [here](./sdd-workflow.md).

---

## Next Steps

As the project evolves, this document will continue to track:

1. **Workflow Refinements**: Improvements to the SDD process
2. **Lessons Learned**: What worked, what didn't, and why
3. **Tool Adaptations**: Updates for GitHub Copilot and other AI assistants

For current workflow usage, always refer to the **Master Workflow** and **Phase-specific documentation** outlined [here](./sdd-workflow.md).
