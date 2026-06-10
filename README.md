# Derived Success Tutoring Platform

A full-stack tutoring management web application built with Django that allows students to connect with tutors, request tutoring sessions, and manage appointments through a role-based system.

## Overview

Derived Success is a tutoring platform created as part of a web development project. Inspired by a fictional company originally developed during a cybersecurity assignment, the project evolved into a complete web application focused on connecting students with tutors and simplifying the tutoring request process.

The application demonstrates full-stack web development concepts including user authentication, database management, role-based access control, and dynamic content rendering using Django.

## Features

### Student Features

- Create an account and securely log in
- Browse available tutors
- View tutor specialties and availability
- Submit tutoring session requests
- Track tutoring requests and appointments

### Tutor Features

- View pending tutoring requests
- View accepted tutoring sessions
- Manage and update session requests
- Access tutor-specific functionality through role-based permissions

### Administrative Features

- User and session management
- Database-backed content management

## Technologies Used

### Backend

- Python
- Django

### Frontend

- HTML
- Bootstrap
- JavaScript
- jQuery

### Database

- SQLite

## Key Concepts Demonstrated

- Full-stack web application development
- User authentication and authorization
- Role-based access control
- Database design and management
- CRUD operations
- Dynamic web page rendering
- Form validation and processing
- MVC/MVT architectural patterns
- Version control with Git and GitHub

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/derived-success.git
cd derived-success
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to:

```text
http://127.0.0.1:8000/
```

## Project Goals

The goal of this project was to gain practical experience building a real-world web application using Django while implementing common software engineering concepts such as authentication, authorization, database interaction, and user workflow management.

## Future Enhancements

- Tutor ratings and reviews
- Email notifications for session updates
- Calendar integration
- Online meeting links
- Advanced tutor search and filtering
- Session history and reporting

## Screenshots

### Home Page

![Home Page](<img width="2502" height="1305" alt="homepage" src="https://github.com/user-attachments/assets/0b8e87ac-e61a-4510-97b0-f2b4fa7cb9a5" />)

### Tutor Detail

![Tutor Directory](<img width="2510" height="1252" alt="tutordetail" src="https://github.com/user-attachments/assets/37370853-407f-4158-ab40-f7ca07d1347c" />)

### Session Request Form

![Session Request Form](<img width="2507" height="1070" alt="sessionrequest" src="https://github.com/user-attachments/assets/66049306-a894-4d9e-9a89-9f080b9e5b2f" />)

### Tutor Dashboard

![Tutor Dashboard](<img width="2502" height="1235" alt="tutordash" src="https://github.com/user-attachments/assets/42f40437-4651-48f5-afe5-be5c77c96233" />)

## Author

Developed by Joel Klein as part of a web development course project.
