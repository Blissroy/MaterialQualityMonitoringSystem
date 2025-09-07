# MaterialQualityMonitoringSystem
A web app for logging and analyzing construction material test results (Concrete, Steel, Aggregate).
A web-based system for logging, analyzing, and monitoring the quality of construction materials 
such as concrete, steel, and aggregates. It provides engineers and project managers with 
dashboards, reports, and automated PDF generation for better decision-making.
## 🚀 Features
- User authentication (register/login with JWT)
- Project management (create, update, delete projects)
- Material quality tests (concrete, steel, aggregates, etc.)
- PDF report generation
- REST API endpoints
- Admin dashboard
## 🛠 Tech Stack
- Backend: Django, Django REST Framework
- Database: SQLite (can be extended to PostgreSQL)
- Frontend: React.js / Django Templates (to be implemented)
- Authentication: JWT (djangorestframework-simplejwt)
- Reporting: ReportLab (PDF generation)
## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/MaterialQualityMonitoringSystem.git
   cd MaterialQualityMonitoringSystem/mqms
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
GETTING THE TOKEN(LOGIN)
API: http://127.0.0.1:8000/api/auth/token/
{
  "username": "admin",
  "password": "yourpassword"
}
API: http://127.0.0.1:8000/materials/types/
{
  "name": "Concrete",
  "description": "Standard grade concrete"
}
OR
{
  "name": "Steel"
}

Running a test 
http://127.0.0.1:8000/materials/tests/
{
  "project": 1,
  "material_type": 2,
  "test_type": "Compressive",
  "test_date": "2025-09-06"
}


### 6. API Endpoints  
Document your APIs (at least a few examples).  
```markdown
## 📡 API Endpoints

- `http://127.0.0.1:8000/users/` → User API  
- `http://127.0.0.1:8000/projects/` → Projects API  
- `http://127.0.0.1:8000/materials/` → Materials API  
- `http://127.0.0.1:8000/reports/` → Reports API  
## 🖥 Usage
- Login as an engineer
- Add a project
- Upload/enter material test results
- View dashboards and download PDF reports
