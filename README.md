# Electronics Inventory Management System

A Flask-based web application for managing electronic products inventory with advanced search, analytics, and user authentication.

## Features

- **Product Management**
  - CRUD operations for electronic products
  - Detailed product specifications
  - Image upload support
  - Stock tracking

- **Search & Filtering**
  - Keyword search across name, description, and specifications
  - Price range filtering
  - Stock status filtering (in stock, low stock, out of stock)
  - Sorting options (price, stock levels)

- **Analytics Dashboard**
  - Price distribution histograms
  - Stock level analysis
  - Manufacturer comparisons
  - Interactive charts and graphs

- **User Management**
  - Role-based access control (Admin/User)
  - Secure authentication
  - Protected routes

## Tech Stack

- **Backend**: Flask
- **Database**: SQLAlchemy
- **Forms**: WTForms
- **Frontend**: HTML/CSS/JavaScript
- **Charts**: Chart.js
- **Testing**: Pytest

## Project Structure
```
WMGInvent/
├── app.py # Application entry point
├── config.py # Configuration settings
├── global_db_object.py # Database instance
├── seed.py # Database seeding script
│
├── forms/ # Form definitions
│ ├── electronics_form.py # Electronics input form
│ ├── LoginForm.py # User login form
│ └── RegisterForm.py # User registration form
│
├── models/ # Database models
│ ├── Category.py # Product categories
│ ├── ElectronicModel.py # Electronics model
│ ├── ProductModel.py # Base product model
│ └── UserModel.py # User model
│
├── repositories/ # Data access layer
│ ├── ElectronicsRepository.py
│ ├── InventoryRepository.py
│ ├── IRepository.py # Repository interface
│ └── UserRepository.py
│
├── routes/ # API endpoints
│ ├── analytics_routes.py # Analytics endpoints
│ ├── auth_routes.py # Authentication routes
│ └── electronics_routes.py # Product management routes
│
├── services/ # Business logic layer
│ ├── AuthService.py # Authentication service
│ ├── ElectronicsService.py # Electronics management
│ └── InventoryService.py # Inventory operations
│
└── tests/ # Test suite
├── test_auth.py # Authentication tests
└── test_electronics_service.py
```

### 📊 File Statistics
- Total Python Files: 23
- Key Components:
  - Models: 4 files
  - Services: 3 files
  - Repositories: 4 files
  - Routes: 3 files
  - Forms: 3 files
  - Tests: 2 files


## Dependencies 
- Python 3.13.1
- pip 24.3.1
## Extensions 
- alembic==1.14.1
- blinker==1.9.0
- click==8.1.8
- dnspython==2.7.0
- email_validator==2.2.0
- Flask==3.1.0
- Flask-Login==0.6.3
- Flask-Migrate==4.1.0
- Flask-SQLAlchemy==3.1.1
- Flask-WTF==1.2.2
- idna==3.10
- itsdangerous==2.2.0
- Jinja2==3.1.5
- Mako==1.3.9
- MarkupSafe==3.0.2
- narwhals==1.27.1
- numpy==2.2.3
- packaging==24.2
- pandas==2.2.3
- plotly==6.0.0
- python-dateutil==2.9.0.post0
- python-dotenv==1.0.1
- pytz==2025.1
- six==1.17.0
- SQLAlchemy==2.0.38
- typing_extensions==4.12.2
- tzdata==2025.1
- Werkzeug==3.1.3
- WTForms==3.2.1

- ```pip install -r requirements.txt```

## Running the app 
- ```python app.py```
- ```python seed.py```

## Running the tests 
- ```python -m unittest tests.py```

## API Routes

- `GET /electronics/browse`: Browse and search products
- `GET /electronics/<id>`: View product details
- `POST /electronics/<id>/update`: Update product
- `POST /electronics/<id>/delete`: Delete product
- `GET /analytics`: View analytics dashboard


## License
This project is licensed under the MIT License - see the LICENSE file for details.

