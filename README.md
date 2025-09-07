🏗 Material Quality Monitoring System (MQMS)

A web-based system for logging, analyzing, and monitoring the quality of construction materials such as concrete, steel, and aggregates.
It provides engineers and project managers with dashboards, reports, and automated PDF generation for better decision-making.

🚀 Features

🔑 User authentication (JWT-based login/register)

📂 Project management (create, update, delete projects)

🧱 Material quality tests (Concrete, Steel, Aggregates, etc.)

📊 Dashboards & PDF report generation (via ReportLab)

🌐 REST API endpoints for integration with frontend

⚙️ Admin dashboard (Django Admin interface)

🛠 Tech Stack

Backend: Django, Django REST Framework

Database: SQLite (default) → can be extended to PostgreSQL

Frontend: React.js or Django Templates (to be implemented)

Authentication: JWT (djangorestframework-simplejwt)

Reporting: ReportLab (PDF generation)

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/MaterialQualityMonitoringSystem.git
cd MaterialQualityMonitoringSystem/mqms


Create and activate a virtual environment

python -m venv .venv
# On Linux/Mac
source .venv/bin/activate  
# On Windows
.venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run migrations & start server

python manage.py migrate
python manage.py runserver

🔑 Authentication (Getting a Token)

Use the JWT authentication endpoint:

POST → http://127.0.0.1:8000/api/auth/token/

{
  "username": "admin",
  "password": "yourpassword"
}


Response:

{
  "access": "youraccesstoken",
  "refresh": "yourrefreshtoken"
}


Copy the access token and include it in your request headers:

Authorization: Bearer youraccesstoken

📡 API Endpoints
Users

GET /users/ → List users

POST /users/ → Create user

Projects

GET /projects/ → List projects

POST /projects/ → Create a project

Example (POST)

{
  "name": "Bridge Project",
  "location": "Accra",
  "client_name": "ABC Constructions"
}

Material Types

GET /materials/types/ → List material types

POST /materials/types/ → Add material type

Example (POST)

{
  "name": "Concrete",
  "description": "Standard grade concrete"
}


or

{
  "name": "Steel"
}

Material Tests

GET /materials/tests/ → List tests

POST /materials/tests/ → Add new test

Example (POST)

{
  "project": 1,
  "material_type": 2,
  "test_type": "Compressive",
  "test_date": "2025-09-06"
}

Reports

GET /reports/ → View available reports

POST /reports/ → Generate/download report

🖥 Usage Workflow

🔑 Login as Engineer/Admin using JWT

📂 Create a new Project

🧱 Define Material Types (e.g., Concrete, Steel)

🧪 Add Material Tests linked to projects and material types

📊 View dashboards and download PDF reports