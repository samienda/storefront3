# Django Storefront Project

This is a Django project for building an e-commerce storefront. It provides a platform for managing products, orders, and customer information.

## Features
- **User Authentication**: Enables users to create accounts and log in to access their storefronts.
- **Storefront Creation**: Allows users to create their own storefronts with custom branding and design.
- **Product Management**: Users can add, edit, and delete products in their storefronts.
- **Inventory Tracking**: Keeps track of product inventory and alerts users when stock is low.
- **Order Processing**: Users can view and process orders placed by customers.

## Technologies
- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django REST Framework**: A powerful and flexible toolkit for building Web APIs.
- **Redis**: An open-source, in-memory data structure store used as a database, cache, and message broker.
- **Celery**: A distributed task queue that is used to process background tasks asynchronously.
- **MySQL**: An open-source relational database management system that is used to store data.
- **Silk**: A live profiling and inspection tool for the Django framework.
- **Locust**: An open-source load testing tool that is used to test the performance of the application.

## Installation

1. **Clone the repository**: 
    ```sh
    git clone https://github.com/samienda/storefront3.git
    ```

2. **Navigate to the project directory**: 
    ```sh
    cd storefront
    ```

3. **Install Pipenv**: 
    ```sh
    pip install pipenv
    ```

4. **Install the project dependencies using Pipenv**: 
    ```sh
    pipenv install
    ```

5. **Activate the Pipenv shell**: 
    ```sh
    pipenv shell
    ```

6. **Install MySQL**: Ensure that MySQL is installed and running on your machine. Create a database for the project:
    ```sh
    mysql -u root -p
    CREATE DATABASE storefront;
    ```

7. **Configure the database settings**: Update the `DATABASES` setting in `storefront/settings.py` with your MySQL database credentials.

8. **Run database migrations**: 
    ```sh
    python manage.py migrate
    ```

9. **Start the Redis server**: Make sure Redis is installed and running. You can start the Redis server using the command:
    ```sh
    redis-server
    ```

10. **Start the Celery worker**: 
    ```sh
    celery -A storefront worker --loglevel=info
    ```

11. **Start the development server**: 
    ```sh
    python manage.py runserver
    ```

## Usage

Once the development server is running, you can access the storefront by visiting `http://localhost:8000` in your web browser. From there, you can browse products, add them to your cart, and place orders.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch: 
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them: 
    ```sh
    git commit -m "Add your commit message"
    ```
4. Push to the branch: 
    ```sh
    git push origin feature/your-feature-name
    ```
5. Open a pull request
