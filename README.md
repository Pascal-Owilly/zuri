# Zuri Stage 2 Training

## Project Flow

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

* You need the following to get started:
  1. IDE (Text editor e.g visual studio code, atom etc )
  2. Terminal for executing your commands
  3. Computer with 4gb ram and above

### Prerequisites

You need `python version 3.9` and above, `Django 4.2`

### Installation and execution

    `git clone https://github.com/Pascal-Owilly/zuri.git`
    `cd zuri-training`
    `virtualenv venv`
    `source venv/bin/activate`
    `cd zuri`
    `pip install django`
    `pip install djangorestframework`
    `pip install drf-yasg` - This is a swagger doc which will provide the request and response 
    `python manage.py runserver`

## API Usage

This is an API endpoint which can be used to create, read, update and delete names and store them in the database.
Just head to `https://enceptics.pythonanywhere.com/api/` 

### API Endpoints
 [https://enceptics.pythonanywhere.com/api](https://enceptics.pythonanywhere.com/api)
 [Visit Google](https://www.google.com)

 - Lists the names created and stored in the database
 [https://enceptics.pythonanywhere.com/api/1](https://enceptics.pythonanywhere.com/api/1)
 - Retrieves the first name of the list and performs CRUD operations to it (replace `1` with any ID to perform this on a different person)

#### Documentation with swagger

 [https://enceptics.pythonanywhere.com/swagger/](https://enceptics.pythonanywhere.com/swagger/)
 - The documentation explaining full details and usage of the endpoints

#### Create a New Person

- **URL:** `/api/persons/`
- **Method:** POST
- **Request Body:**

  ```json
  {
    "name": "Jane Doe",
  }
