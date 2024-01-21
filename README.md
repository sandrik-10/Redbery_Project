# Redbery Project
This project provides a Django Rest frameword-based API for managing blogs and categories.

## project Description
This project is intended for blogs, the user can read blogs, filter by categories, and if the user logs in, he can add a new blog.
As in real life, when a user enters the site without registration, he cannot delete additions and other similar operations, he can only read, and in this preokt, when a person is not registered, he can only read blogs, 
if he registers, he can also create a new blog, which is completely logical.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)
- [Endpoints](#endpoints)
- [Authentication](#authentication)
- [Acknowledgements](#acknowledgements)

## Introduction
The Redbery Project is a Django REST framework-based project that allows users to manage blogs and categories through a RESTful API.

## Getting Started
To get started with the Redbery Project, follow these steps:
1. **Clone the Repository:**
   git clone  https://github.com/sandrik-10/Redbery_Project

## Running the Server
In case to run server follow these code:
python manage.py runserver

## Configuration
This project uses default SQLite database.

## Endpoints
Blogs:
  GET /blogs/: Retrieve all blogs or filter by category.
  GET /blogs/{id}/: Retrieve a specific blog.
  POST /blogs/: Create a new blog.
  PUT /blogs/{id}/: Update a blog.
  DELETE /blogs/{id}/: Delete a blog.
Categories:
  GET /categories/: Retrieve all categories.
  GET /categories/{id}/: Retrieve a specific category.
  POST /categories/: Create a new category.
  PUT /categories/{id}/: Update a category.
  DELETE /categories/{id}/: Delete a category.
User Authentication:
  POST /login/: User login and token generation.

But this project has permisshions, as I mentioned above, if a person is not authenticated in both the blog and categories, he can only use the get method.
And if authenticated, only the get method can be used in the categories, and the get and post methods in the blog.

## Authentication
user authentication is required for creating and read blogs.Use the /login/ endpoint to obtain a token for authentication.

## Acknowledgements
1. Django REST framework
2. Django


