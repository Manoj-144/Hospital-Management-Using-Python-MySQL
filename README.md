# Hospital Management System

This project is a basic Hospital Management System developed as a final-year high school project. The code may be amateurish, reflecting early learning in programming, and is intended as an introductory example for public use. The system uses **Tkinter** for the user interface and **MySQL** for backend database management, offering essential tools to manage hospital records.

## Features

- **User Authentication**: Login functionality for secure access.
- **Responsive GUI**: Developed with Tkinter, including custom background and logo images.
- **Database Management**: Uses MySQL to store and manage hospital records.
- **Record Management**: CRUD (Create, Read, Update, Delete) functionalities for handling hospital data.
- **Custom Interface Design**: Unique layout with background and logo images.

## Project Structure

- **main_screen.py**: Core script that initiates the GUI, handles authentication, and connects to MySQL for record operations.
- **Images**: Background and logo images for the interface.

## Requirements

- **Python 3.x**
- **Tkinter** (included with Python)
- **PIL (Pillow)** for image processing
- **MySQL Connector**
- **MySQL Database** for storing hospital records

## Setup Instructions

1. **Install required packages**: Pillow for image handling and MySQL connector for database connectivity.
2. **Set up the MySQL Database**:
   - Create a new database in MySQL (e.g., `hospital_db`).
   - Use SQL commands to create tables as required by the application (for example, tables for patients, staff, appointments, etc.).
3. **Update MySQL Credentials**:
   - Modify the MySQL connection section in `main_screen.py` to use your MySQL username and password.
4. **Run the Program**

## Screenshots

*(Add application screenshots here)*

## Future Improvements

- Expanding modules to include appointment scheduling, billing, and discharge summaries.
- Upgrading the interface for enhanced usability.
- Adding data encryption for security.

## Authors

- **Madhusudhanan K**
- **Nitin S**
- **Manoj R**

## License

This project is open for public use and serves as a learning resource for those interested in Python and MySQL for basic application development.
