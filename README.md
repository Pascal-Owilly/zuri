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

    * `git clone https://github.com/Pascal-Owilly/zuri.git`
    * `cd zuri-training`
    * `virtualenv venv`
    * `source venv/bin/activate`
    * `cd zuri`
    * `pip install django`
    * `pip install djangorestframework`
    * `python manage.py runserver`

## Usage

This is an API endpoint which can be used to create, read, update and delete names
just hed to 

### API Endpoints

`/api/persons` - This will list the names created and stored in the database
`api/persons/1` - Retrieves the first name of the list
`api/persons/2` - Retrieves the second name of the list etc

#### Create a New Person

- **URL:** `/api/persons/`
- **Method:** POST
- **Request Body:**

  ```json
  {
    "name": "Jane Doe",
  }
