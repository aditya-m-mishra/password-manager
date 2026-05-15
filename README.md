# Password Manager 

## Project Overview

Password Manager is a desktop-based application developed using **Python** and **Tkinter** that helps users securely manage their login credentials in a simple and efficient way. The application allows users to generate strong passwords, save website credentials locally, and retrieve saved passwords whenever needed through an easy-to-use graphical interface.

The main goal of this project was to build a practical cybersecurity-focused application while gaining hands-on experience with Python GUI development, file handling, and data management.

The application provides a clean interface where users can:
- Store website login credentials
- Generate secure random passwords
- Retrieve saved credentials using a search feature
- Automatically copy generated passwords to the clipboard

All credentials are stored locally in a structured JSON file, making the application lightweight and easy to manage without requiring a database setup.

### Key Functionalities

#### Secure Password Generation
The application can generate strong passwords containing:
- Uppercase letters
- Lowercase letters
- Numbers
- Special symbols

Passwords are randomized and shuffled to improve security and reduce predictability.

#### Credential Storage
Users can save:
- Website name
- Email/Username
- Password

The data is stored in a `JSON` format for easy access and management.

#### Search Functionality
The application includes a search feature that allows users to quickly retrieve saved credentials for a particular website.

#### Clipboard Integration
Generated passwords are automatically copied to the clipboard using the `pyperclip` library, improving user convenience.

#### Error Handling & Validation
The project includes:
- Empty field validation
- File handling exceptions
- User confirmation popups
- Error messages for missing credentials

### Learning Outcomes

This project helped in improving understanding of:
- Python GUI development using Tkinter
- JSON file operations
- Exception handling
- User input validation
- Randomized password generation
- Desktop application workflow

The project also provided practical exposure to building real-world utility software with a focus on usability and functionality.

---

## Technologies Used

- Python
- Tkinter
- JSON
- Pyperclip

---

## How to Run

```bash
pip install pyperclip
python main.py
