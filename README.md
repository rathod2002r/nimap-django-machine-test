# Nimap Django Machine Test

This repo contains a Django REST API for managing Users, Clients, and Projects.

- Uses Django REST Framework  
- PostgreSQL as database  
- Features:  
  - Register clients  
  - Edit/Delete clients  
  - Create projects for clients and assign users  
  - Retrieve projects assigned to logged-in user

---

## How to run

1. Setup Python virtual environment  
2. Install dependencies: `pip install -r requirements.txt`  
3. Configure Postgres DB in `nimap_project/settings.py`  
4. Run migrations: `python manage.py migrate`  
5. Create superuser: `python manage.py createsuperuser`  
6. Run server: `python manage.py runserver`  
7. Use APIs at `http://localhost:8000/`

---

