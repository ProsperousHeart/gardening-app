# Project Description

I am part of a local community garden where we grow food for local food pantries. In our community garden, we have supporters (who are not official gardeners but support with chores and teams), gardener apprentices who must complete a training program before they can be official gardeners, official gardeners who are like supporters but also have at least 1 plot they are in charge of, and then the city official(s) who manage the Google group for discussion and anything we need from the city.

Our community garden is fairly “old school” and leverages a Google group that some people may or may not be a part of. Often it can be difficult to try to plan for plots throughout the year let alone work on volunteer teams - especially for new gardeners.

We need a simple system that allows for easy garden planning as well as a secure system to collaborate on needs within the community.

_Progress is notated [here](progress.md)._

## Stakeholders

Here you will find the list of stakeholders and how they are expected to impact the design or use of the system.

- Volunteer developers

- Gardeners of all experience levels

    - New “budding” gardeners / apprentices

    - Master Gardeners

    - “Local” gardeners (relative to location)

    - Community Gardeners (general gardeners)

    - Community Gardeners (apprentices)

    - Community Gardeners (supporters)

    - Community Gardeners (specific teams)

    - Community Gardeners (specific chore groups)

- People looking for gardening apps or tools to improve their knowledge & experience

- Local nurseries & “big box” stores

- Plants to be grown or tended to

## Scenarios & Needs

Below is the initial general outlines & expectations of what this solution should do.

- Provide a way to pull data about specific plants based on the user’s USDA zone

- Provide information about a specific plant (e.g.: scientific name, germination time, size, etc) that is easy to locate, digest, and utilize

- Provide notifications to protect plants based on local weather conditions

- Provide information about the sun trajectory and light angle for planning of beds based on current / specific location

- Provide for a way to more easily find plants to work with based on time of year, zone, plant type, etc

- Provide for a way to add additional plants without having duplicates (e.g.: automated way to create tickets / solutions)

- Provide possible nursery and gardening store locations based on current location

- Create a secure location for local community gardener members to understand where they are in their journey

- Have a central communication tool for community garden announcements that won't be lost in emails

- Be open source so others can improve and support community

# Project Layout

You can find the systems requirement documentation in the following:

1. [Scope](scope.md)

2. [System Requirements](system-requirements.md)

3. [System Architecture](architecture.md)

Below is the structure as seen on GitHub.

    2024-Django-Attempt             # v1 made in a rush with no planning (2024)
    gardening-docs                  # Mkdocs for documentation site
        mkdocs.yml                  # The configuration file.
        docs/
            img/                    # static images
                favicon.ico
            architecuture.md        # architecture of the sytem (FFBDs)
            index.md                # The documentation homepage & initial requirements
            progress.md             # where solution stands & next steps
            resources.md            # resources that help make the site or app
            scope.md                # UCBDs, scope tree, SysMLs, etc
            system-requirements.md  # requirements documentation (IN PROGRESS)
    .gitignore
    CHANGELOG.md
    LICENSE
    README.md
    requirements.txt
