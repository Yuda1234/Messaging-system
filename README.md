Messaging System
Overview
This is a simple REST API backend system for handling messages between users. 
Each message includes information about the sender, receiver, message content, subject, and creation date.
The API provides endpoints for writing messages, getting all messages for a specific user, getting all unread messages for a specific user, reading a single message, and deleting messages.

Technologies Used
Django: A high-level Python web framework.
Django Rest Framework (DRF): A powerful and flexible toolkit for building Web APIs in Django.
Database: SQLite is used as the default database.

Setup Instructions
Clone the Repository:
https://github.com/Yuda1234/Messaging-system/tree/master

Create a Virtual Environment:
python -m venv venv

Activate the Virtual Environment:
.\venv\Scripts\activate

Apply Migrations:
python manage.py migrate

Run the Development Server:
python manage.py runserver

API Endpoints
Write a Chet Message:
Send a POST request to http://localhost:8000/chetmessages/write/ with the required data in the request body.

Get Chet Messages:
Send a GET request to http://localhost:8000/chetmessages/get/ to retrieve all Chet messages.

Get Unread Chet Messages:
Send a GET request to http://localhost:8000/chetmessages/get_unread/ to retrieve unread Chet messages.

Read a Chet Message:
Send a GET request to http://localhost:8000/chetmessages/read/{message_id}/ to read a specific Chet message.

Delete a Chet Message:
Send a DELETE request to http://localhost:8000/chetmessages/delete/{message_id}/ to delete a specific Chet message.




