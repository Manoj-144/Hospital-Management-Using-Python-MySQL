Hospital Management System
This project is a basic Hospital Management System developed as a final-year high school project. The code may be amateurish, reflecting early learning in programming, and is intended as an introductory example for public use. The system uses Tkinter for the user interface and MySQL for backend database management, offering essential tools to manage hospital records.

Features
User Authentication: Login functionality for secure access.
Responsive GUI: Developed with Tkinter, including custom background and logo images.
Database Management: Uses MySQL to store and manage hospital records.
Record Management: CRUD (Create, Read, Update, Delete) functionalities for handling hospital data.
Custom Interface Design: Unique layout with background and logo images.
Project Structure
main_screen.py: Core script that initiates the GUI, handles authentication, and connects to MySQL for record operations.
Images: Background and logo images for the interface.
Requirements
Python 3.x
Tkinter (included with Python)
PIL (Pillow) for image processing: pip install pillow
MySQL Connector: pip install mysql-connector-python
MySQL Database for storing hospital records
Setup Instructions
Install required packages:

bash
Copy code
pip install pillow mysql-connector-python
Set up the MySQL Database:

Create a new database in MySQL (e.g., hospital_db).
Use SQL commands to create tables as required by the application (for example, tables for patients, staff, appointments, etc.).
Here’s a simple example for table creation:
sql
Copy code
CREATE DATABASE hospital_db;
USE hospital_db;

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    contact VARCHAR(15),
    address VARCHAR(255)
);

CREATE TABLE staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    role VARCHAR(50),
    contact VARCHAR(15),
    address VARCHAR(255)
);

-- Add more tables as needed for your requirements.
Update MySQL Credentials:

Modify the MySQL connection section in main_screen.py to use your MySQL username and password:
python
Copy code
mydb = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="hospital_db"
)
Run the Program:

bash
Copy code
python main_screen.py
Screenshots
(Add application screenshots here)

Future Improvements
Expanding modules to include appointment scheduling, billing, and discharge summaries.
Upgrading the interface for enhanced usability.
Adding data encryption for security.
Authors
Madhusudhanan K
Nitin S
Manoj R
License
This project is open for public use and serves as a learning resource for those interested in Python and MySQL for basic application development.
