# DevTrack

A Django-based backend API for tracking engineering issues. Engineers can create reporters, file issues, assign priorities, and track issue status.

## Features

* Create and retrieve Reporters
* Create and retrieve Issues
* Filter Issues by status
* JSON-based storage
* OOP design using inheritance and polymorphism
* Validation using abstract base classes

## Project Structure

```text
devtrack/
│
├── manage.py
├── issues.json
├── reporters.json
│
├── devtrack/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── issues/
    ├── models.py
    ├── views.py
    ├── urls.py
```

## Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project

```bash
cd devtrack
```

3. Create and activate virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

4. Install Django

```bash
pip install django
```

5. Run the server

```bash
python manage.py runserver
```

6. Open

```text
http://127.0.0.1:8000/
```

## API Endpoints

### Reporter Endpoints

#### Create Reporter

POST

```text
/api/reporters/
```

#### Get All Reporters

GET

```text
/api/reporters/
```

#### Get Reporter By ID

GET

```text
/api/reporters/?id=1
```

### Issue Endpoints

#### Create Issue

POST

```text
/api/issues/
```

#### Get All Issues

GET

```text
/api/issues/
```

#### Get Issue By ID

GET

```text
/api/issues/?id=1
```

#### Filter Issues By Status

GET

```text
/api/issues/?status=open
```

## Design Decision

The application uses JSON files (`issues.json` and `reporters.json`) instead of a database. This decision was made because the project requirements focus on OOP concepts, inheritance, validation, and API development rather than database integration. JSON storage keeps the solution simple while demonstrating object-oriented design and REST API principles.

## Postman Testing

### Successful Request

Add screenshot here:

* screenshots/success-create-reporter.png

### Failed Request

Add screenshot here:

* screenshots/failure-create-reporter.png
