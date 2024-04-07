# Alternative Travels API

Welcome to Alternative Travels API set up using Django REST Framework for the Alternative Travels front-end application, a social media for sharing images, videos of alternative travels with the help of geolocation data and tags. The social media is provided as well with a marketplace section with rare products found by the users during their trips.

Here below the links to the API and the Frontend:

<strong>Backend</strong>

[Live link](https://alternative-travels-debb28d8ca03.herokuapp.com/)

<strong>Frontend</strong>

[Repository here](https://github.com/aedoardo1990/alternative-travels/)
[Live website here](https://alternative-travel-54fe13e24a2a.herokuapp.com/)


## Table of Contents
  - [User Stories](#user-stories)


### User Stories

The back-end section of the project focuses on the administration side and covers the user stories from the point of view of a developer and/or superuser. The User Stories are divided into the following categories:

#### Login and Registration
- As a developer I want to access an API endpoint that allows users to register by providing their username and password
- As a developer I want to have a user profile to be automatically created, when a new user signs up
- As a developer I want to access an API endpoint that allows users to log in, obtain an authentication token, and access user-specific content

#### Profiles
- As a developer I want to be able to create, read, update, and delete user profiles via the API

#### Posts with Images or Videos
- As a developer I want to be able to create, read, update, and delete posts with images about travels
- As a developer I want uploaded images to not exceed a size format limit
- As a developer I want to be able to create, update and delete post with videos about travels
- As a developer I want uploaded videos to be automatically converted to a consistent format, trimmed and compressed if they exceed a specific file size

#### Comments
- As a developer I want to have access for creating, reading, updating, and deleting comments

#### Likes
- As a developer I want to have access for creating, reading and deleting likes

#### Marketplace
- As a developer I want to be able to create, read, update and delete posts about products to be sold on the marketplace section of the site

#### Likes and Comments of the Marketplace (apps are called Loves and Opinions)
- As a developer I want to have access for creating, reading, updating, and deleting comments and likes as well under the posts of the marketplace

#### Followers
- As a developer I want to have access for creating, reading and deleting follow relationships between users

#### Tags
- As a developer I want to posts to have a tag field, so that users can tag their created posts (valid just for normal Posts and not those in the Marketplace)
- As a developer I want to display a list of tags of all the users

#### Search and Filter
- As a developer I want to have a functionality for filtering and sorting results, in order to have more control over what data to display to the user

#### Geolocation
- As a developer I want to have the possibility to add a geolocation for each post so that users can create posts with a geolocation and update it if necessary (valid just for normal Posts and not those in the Marketplace)


### Data Models

I have created the following models for the Alternative Travels API

| Models | Scope |
| :---------------------------------: | :------------------------------:|
| User | the Django standard User model |
| Profiles | to create, update, store and delete profile data |
| Posts | to create posts with images or videos, with geolocation and tag |
| Comments | to make comments about the posts |
| Likes | to like posts |
| Followers | to follow other users and be updated about their posts |
| Marketplace | to post products to sell |
| Opinions | to make comments about the posts of products on sale |
| Loves | to like posts of products on sale |

The relationships between the models is summarized in the followed entity relationship diagram.

![Diagram](assets/readme/diagram-database.png)



