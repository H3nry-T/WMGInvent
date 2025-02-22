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

## Dependencies 
- Python 3.13.1
- pip 24.3.1
- ```pip install -r requirements.txt```

## Running the app 
- ```python app.py```

## Running the tests 
- ```python -m unittest tests.py```

## API Routes

- `GET /electronics/browse`: Browse and search products
- `GET /electronics/<id>`: View product details
- `POST /electronics/<id>/update`: Update product
- `POST /electronics/<id>/delete`: Delete product
- `GET /analytics`: View analytics dashboard

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

