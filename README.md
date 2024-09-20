

/api/bookings/
/api/menu/


Little Lemon Web Application - API Documentation
Overview
This project provides a REST API for managing the menu and table bookings for the Little Lemon
restaurant.
It supports user registration, authentication using JWT tokens, and allows CRUD operations for
menu items and bookings.

Setup Instructions
1. Clone the repository from GitHub.
2. Set up the virtual environment and install dependencies:
 pip install -r requirements.txt
3. Run the migrations:
 python manage.py migrate
4. Create a superuser to access the Django admin:
 python manage.py createsuperuser
5. Start the development server:
 python manage.py runserver

API Endpoints
1. User Registration and Authentication
- Register a new user: POST /auth/users/
 Example request body:
 {
 "username": "newuser",
 "password": "password123",
 "email": "newuser@example.com"
 }
- Login and obtain JWT token: POST /auth/jwt/create/
 Example request body:
 {
 "username": "newuser",
 "password": "password123"
 }
- Refresh the JWT token: POST /auth/jwt/refresh/
 Example request body:
 {
 "refresh": "<refresh_token>"
 }
- View the authenticated user's information: GET /auth/users/me/
 Authorization: Bearer token required.

2. Menu Management
- List all menu items: GET /api/menu/
 Authorization: Bearer token required.
- Create a new menu item: POST /api/menu/
 Example request body:
 {
 "name": "Pizza Margherita",
 "description": "A classic pizza with mozzarella and basil.",
 "price": 15.99,
 "availability": true
 }
 Authorization: Bearer token required.
- Retrieve a specific menu item by ID: GET /api/menu/{id}/
 Authorization: Bearer token required.
- Update a specific menu item by ID: PUT /api/menu/{id}/
 Example request body (same as creation).
 Authorization: Bearer token required.
- Delete a specific menu item by ID: DELETE /api/menu/{id}/
 Authorization: Bearer token required.
 
3. Booking Management
- List all bookings: GET /api/booking/
 Authorization: Bearer token required.
- Create a new booking: POST /api/booking/
 Example request body:
 {
 "customer_name": "John Doe",
 "table_number": 5,
 "date": "2024-09-30",
 "time": "18:00"
 }
 Authorization: Bearer token required.
- Retrieve a specific booking by ID: GET /api/booking/{id}/
 Authorization: Bearer token required.
- Update a specific booking by ID: PUT /api/booking/{id}/
 Example request body (same as creation).
 Authorization: Bearer token required.
- Delete a specific booking by ID: DELETE /api/booking/{id}/
 Authorization: Bearer token required.
Notes
- Ensure you include the Bearer token in the Authorization header for all secured endpoints.
- You can create, retrieve, update, and delete both menu items and bookings.