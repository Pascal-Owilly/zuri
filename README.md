# Zuri Stage 2 Training

## Getting Started

To get started, make sure you have the following:

1. IDE (Text editor e.g. Visual Studio Code, Atom, etc.)
2. Terminal for executing your commands
3. Computer with 4GB RAM or above

### Prerequisites

You'll need the following software installed:

- Python version 3.9 and above
- Django 4.2

### Installation and Execution

1. Clone the repository: `git clone https://github.com/Pascal-Owilly/zuri.git`

2. Navigate to the project directory: `cd zuri-training`

3. Create a virtual environment (venv): `virtualenv venv`

4. Activate the virtual environment: `source venv/bin/activate`

5. Navigate to the Django project folder: `cd zuri`

6. Install Django: `pip install django`

7. Install Django Rest Framework: `pip install djangorestframework`

8. Install drf-yasg (Swagger documentation): `pip install drf-yasg`

9. Run the Django development server: `python manage.py runserver`


### API Endpoints and Usage

- **List of Names:**
- URL: `https://enceptics.pythonanywhere.com/api/`
- Description: Lists the names created and stored in the database

- **Retrieve and CRUD Operations on a Name:**
- URL: `https://enceptics.pythonanywhere.com/1/`
- Description: Retrieves the first name in the list and performs CRUD operations on it. You can replace `1` with any id to perform these operations on a different person.

- **List a Specific Name with a Query Parameter:**
- URL: `https://enceptics.pythonanywhere.com/api/?filter_param=name`
- Description: Lists a specific name passed as a query parameter. For example, [https://enceptics.pythonanywhere.com/api/?filter_param=pascal](https://enceptics.pythonanywhere.com/api/?filter_param=pascal) returns the name `pascal`.

#### Documentation with Swagger

You can access the API documentation using Swagger at [https://enceptics.pythonanywhere.com/swagger/](https://enceptics.pythonanywhere.com/swagger/).

#### Create a New Person

- **URL:** `/api/`
- **Method:** POST
- **Request Body:**

```json
{
"name": "Jane Doe"
}

#### [pascalouma54@gmail.com](mailto:pascalouma54@gmail.com)
