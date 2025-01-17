# gardening-app
An app to help new gardeners determine what to plant in their yard.

It has been determined that Django and Render will be used to host this web app.

# Requirements

Below are the requirements for this project:

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

# How To Launch Locally

Once you have a local copy of the code, in the main folder run: `python manage.py runserver`
