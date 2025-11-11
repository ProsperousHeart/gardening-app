# gardening-app

An app to help new gardeners determine what to plant in their yard.

It has been determined that Django and Render will be used to host this web app.

## Setup

This project uses `uv` for dependency management with `pyproject.toml`. See [docs/uvx-setup-guide.md](docs/uvx-setup-guide.md) for detailed setup instructions.

Resources:

- Miro [board](https://miro.com/app/board/uXjVLFJo2wg=/)

# Requirements

Below are the requirements for this project before crafting systems requirements documentation (effectively "initial requirements" not yet fully vetted):

1. A way to show different plant information

2. A way for logged in users to choose a plant and add to their "collection"

3. Each plant will include information on the following:

   - photo
   - common name
   - scientific name
   - suggested hardiness zone (with link to USDA hardiness site)
   - plant spacing
   - plant height
   - suggested container size
   - companion plants (if any)
   - medicinal benefits (if any)
   - links to additional guides or resources mentioning this plant
   - special aging information (e.g.: germination, days to maturity, etc)

4. Each guide / resource model will contain the following:
   - URL or where can find / purchase the material
   - title
   - author(s)
   - list of plants related to this resource

# Requirements Documentation

As I have been going through Cornell's [System's Design certification program](https://ecornell.cornell.edu/certificates/project-leadership-and-systems-design/systems-design/), I have utilized this app as the main focus for development.

As of 20250116, I have moved the original v1 into the [2024-Django-Attempt](/2024-Django-Attempt/) folder and will be leveraging [MKDocs](https://www.mkdocs.org/) for the documentation instead of the [GitHub project Wiki](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis).
