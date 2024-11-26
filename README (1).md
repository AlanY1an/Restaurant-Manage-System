# Restaurant Management System

## Overview
The **Restaurant Management System** is a full-stack web application built using **Django** and **Python**. It offers a comprehensive platform for managing restaurant operations, including:
- Real-time table reservations
- Meal ordering
- Integrated blog platform

This project is designed to enhance customer experience and streamline operational efficiency for restaurant management.

## Features
- **Table Reservations**: Customers can check table availability and make reservations in real-time.
- **Meal Ordering**: A user-friendly interface for browsing the menu and placing orders.
- **Blog Platform**: An integrated blog system to share restaurant updates, promotions, and culinary stories.

## Technologies Used
- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development) and PostgreSQL (production)
- **Development Tools**: Git, GitHub

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtualenv (optional but recommended)
- PostgreSQL (if deploying to production)

## Setup and Installation
### 1. Clone the Repository
```bash
git clone https://github.com/AlanY1an/Restaurant-Manage-System.git
cd Restaurant-Manage-System
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
Set up the database by applying migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
Create an admin account for accessing the Django admin interface:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```
Access the application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Deployment
For production, configure the project to use PostgreSQL and a WSGI server like Gunicorn.

### Steps:
1. **Set Up PostgreSQL**: Update the `DATABASES` setting in `settings.py` to use PostgreSQL.
2. **Collect Static Files**:
   ```bash
   python manage.py collectstatic
   ```
3. **Configure a Web Server**: Use Nginx or Apache as a reverse proxy to serve the application.
4. **Deploy with Gunicorn**:
   ```bash
   gunicorn project_name.wsgi:application
   ```

Refer to Django’s [deployment checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/) for more details.

## Usage
- Navigate to the homepage to browse the menu and make reservations.
- Log in as an admin to manage reservations, orders, and blog posts.
- Use the blog platform to share updates and engage with customers.

## Contributing
Contributions are welcome! If you’d like to contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add some feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact
For questions or support, feel free to contact:
- **Email**: yiange131@gmail.com
- **GitHub**: [AlanY1an](https://github.com/AlanY1an)
- **Website**: [whyian.dev](https://www.whyian.dev/about/)

