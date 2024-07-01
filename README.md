# HBnB Evolution: Part 2 (Database Persistence)

Database Integration and Security Enhancements for HBnB Evolution Project

In Part 2 of the HBnB Evolution project, you will enhance your application by integrating a relational database using SQLAlchemy, an Object-Relational Mapper (ORM), and by implementing security measures through JWT authentication. This phase aims to provide students with a real-world experience of upgrading an existing application to support more scalable and secure operations.

Learning Objectives

- Understand and Implement ORM: Students will learn how to integrate SQLAlchemy into a Flask application to handle database operations seamlessly.

- Database Management: Gain experience in configuring and managing a relational database, including schema design and migrations.

- Security Implementation: Learn to secure API endpoints using JWT authentication, ensuring that data access is regulated and secure.

- Adaptability and Scalability: Enhance the application’s adaptability by allowing dynamic switching between different persistence methods and preparing for scalable deployment.

Tasks to be Accomplished

1. Integrating SQLAlchemy:

- Modify the application to include SQLAlchemy, setting up models to interact with a database while keeping the option for file-based persistence.
- Ensure that all models are correctly transformed into SQLAlchemy ORM-compatible classes.
- Configure SQLAlchemy to connect to a SQLite database for development purposes.

2. Configurable Database Selection:

- Implement a configuration system that allows the application to toggle between using SQLite for development and a more robust database like PostgreSQL for production.
- Ensure the application can dynamically choose the database type based on environment settings or configuration files.

3. Implementing Authentication with JWT:

- Integrate Flask-JWT-Extended to add secure authentication mechanisms to the API.

- Create endpoints for user authentication that issue JWTs and use these tokens to control access to various API endpoints.

4. Database Schema Design and Migration:

- Design a database schema that accurately represents the data relationships and business rules.

- Create the SQL scripts for your database structure. Optionally, use tools like Alembic to manage database migrations.

5. Role-Based Access Control:

- Modify existing API endpoints to incorporate checks for user roles and permissions, restricting certain actions to authenticated users or administrators.

6. Docker Integration:

- Update the Docker configuration to support the new database and authentication functionalities.

- Ensure that the Docker environment is configured to handle different database types and authentication services.

Resources:

SQLAlchemy Documentation: Utilize the SQLAlchemy docs to understand ORM configuration and usage.

Flask-JWT-Extended Tutorial: Refer to resources on Flask-JWT-Extended to learn how to implement JWT in Flask applications.

Alembic for Migrations: Check out Alembic documentation for guidance on database migrations.

Environment Configuration: Use environment variables to manage database connections and other settings, ensuring flexibility across different deployment environments.

Security Best Practices: Learn about security best practices, particularly in storing passwords securely and managing user authentication.

As an enhancement to this part of the HBnB Evolution project, it’s crucial to integrate real-world database testing into your application development. Therefore, you will use a Docker container with MySQL or PostgreSQL as an external server to test their implementation.

Instructions for Using Docker with MySQL/PostgreSQL:

1. Choose a Database: Decide whether you want to use MySQL or PostgreSQL for your production database.
2. Pull the Docker Image:
For MySQL: docker pull mysql
For PostgreSQL: docker pull postgres
3. Run the Database in a Docker Container:
For MySQL: docker run --name mysql-db -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:latest
For PostgreSQL: docker run --name postgres-db -e POSTGRES_PASSWORD=my-secret-pw -d postgres Replace my-secret-pw with a secure password.
4. Configure Your Application:
Update your application’s configuration to connect to the database running in the Docker container.
Use the appropriate connection string for MySQL or PostgreSQL.
5. Test Your Application:
Ensure your application correctly connects to and interacts with the database within the Docker container.
Conduct all relevant tests to verify database operations.

Resources for Setup and Testing

Docker Official Documentation: Get Started with Docker
MySQL Docker Image Documentation: MySQL Docker Official Image
PostgreSQL Docker Image Documentation: PostgreSQL Docker Official Image
Connecting to MySQL/PostgreSQL from Python: Look into SQLAlchemy documentation for MySQL and PostgreSQL.




## Authors

- Albina Ismayilova [@Albinnich](https://github.com/Albinnich)
- Aziz Abbasov [@Az1z67](https://github.com/Az1z67)
