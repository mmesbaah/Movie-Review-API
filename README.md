# Movie Review API

A RESTful API built with Django and Django REST Framework for managing movie reviews.

## Features

- User authentication and authorization
- CRUD operations for movie reviews
- Search and filter reviews by movie title and rating
- Pagination and sorting
- JWT token-based authentication

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following variables:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
- POST /api/token/ - Get JWT tokens
- POST /api/token/refresh/ - Refresh JWT token

### Users
- POST /api/users/ - Create a new user
- GET /api/users/me/ - Get current user details
- PUT /api/users/me/ - Update current user details

### Reviews
- GET /api/reviews/ - List all reviews
- POST /api/reviews/ - Create a new review
- GET /api/reviews/{id}/ - Get review details
- PUT /api/reviews/{id}/ - Update review
- DELETE /api/reviews/{id}/ - Delete review
- GET /api/reviews/movie/{title}/ - Get reviews for a specific movie
- GET /api/reviews/search/ - Search reviews by title or rating

## Deployment

The API can be deployed on Heroku or PythonAnywhere. Make sure to set the appropriate environment variables in your deployment platform.

## License

MIT