# Basic Event Planner

## Overview

This project implements a Basic Command Line Event Planner software that allows users to manage users, events, and invitations. It integrates with a cloud database, specifically Firebase Firestore, for storing and retrieving data. The software provides functionalities to add, update, delete, and retrieve users, events, and invitations. 

The purpose of this software is to demonstrate proficiency in Python programming and integration with cloud services.

## Cloud Database

The project utilizes Firebase Firestore as the cloud database. Firestore is a flexible, scalable database for mobile, web, and server development from Firebase and Google Cloud Platform.

The structure of the database includes collections for users, events, and invitations. Each collection contains documents representing individual entities, with fields for relevant information such as user details, event details, and invitation statuses.

## Development Environment

The tools and technologies used in developing this software include:

- Python: Programming language used for the backend logic.
- Firebase Admin SDK: Used to integrate the Python application with Firebase Firestore.
- dotenv: Python library for loading environment variables from a .env file.

## Setup and Usage

1. **Clone the Repository**: Clone the project repository from GitHub to your local machine.

2. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where you cloned the repository.

3. **Create a Virtual Environment**: Create a virtual environment using `venv` or `virtualenv`.

    ```
    python -m venv env
    ```

4. **Activate the Virtual Environment**: Activate the virtual environment.

    - **Windows**:
    
        ```
        .\env\Scripts\activate
        ```

    - **MacOS / Linux**:
    
        ```
        source env/bin/activate
        ```

5. **Install Dependencies**: Install the required Python dependencies using pip.

    ```
    pip install -r requirements.txt
    ```

6. **Set Up Environment Variables**: Create a `.env` file in the project directory and set up the necessary environment variables.

    ```
    GOOGLE_APPLICATION_CREDENTIALS=/path/to/serviceAccount.json
    ```

7. **Run the Program**: Run the main Python script to start the program.

    ```
    python main.py
    ```

8. **Interact with the Program**: Follow the on-screen instructions to interact with the Basic Event Planner application.

9. **Deactivate the Virtual Environment**: Once done, deactivate the virtual environment.

    ```
    deactivate
    ```

## Useful Websites

- [Firebase Documentation](https://firebase.google.com/docs/firestore)
- [Python dotenv Documentation](https://pypi.org/project/python-dotenv/)

## Future Work

- Implement user authentication and authorization.
- Improve error handling and validation of user inputs.
- Enhance the user interface for better user experience.
- Add support for more advanced features such as notifications and reminders.
