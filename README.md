# Zuri Stage 2 Training


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


### API Endpoints and Usage

`https://enceptics.pythonanywhere.com/api/` - Lists the names created and stored in the database
`https://enceptics.pythonanywhere.com/1/` - Retrieves the first name of the list and perfoms CRUD 
operations to it (replace `1` with any id to perform this on a different person)
`https://enceptics.pythonanywhere.com/api/?filter_param=name` 
 Lists a specific name passed inside the query for example [https://enceptics.pythonanywhere.com/api/?filter_param=pascal](https://enceptics.pythonanywhere.com/api/?filter_param=pascal) returns the name `pascal`

#### Documentaton with swagger

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
