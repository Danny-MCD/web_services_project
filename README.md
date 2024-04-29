
# **Actor Management System**

## **Overview**
This project implements a simple Actor Management System using Flask for the backend server and HTML, CSS and JavaScript for the frontend interface. The system allows users accessing the website to perform **CRUD** (Create, Read, Update and Delete) operations on actor details stored in a MYSQL database. 

## **Project Structure**
The project consists of the following components:

1. **Flask Server:** The backend server is implemented using Flask, a lightweight Python web framework. The server exposes RESTful API endpoints to handle CRUD operations on actor data. THe server code is located in **'server.py'**.
2. **Actor Data Access Object (DAO):** The DAO class('ActorDAO') provides methods to interact with the MYSQL database. It handles database connections, executes SQL queries, and returns results. The DAO code is located in the **'ActorDAO.py'**.
3. **HTML, CSS, and JavaScript:** The frontend interface is implemented using HTML for structure, CSS for styling and JavaScript for dynamic behaviour. The frontend code is located in **'actorviewer.html'**.
4. **Database Configuration:** Database configuration settings are stored in **'bdconfig.py'**.

## **Functionality**
The Actor Management System offers the following functionality:

- **View Actors:** Users can view a list of all actors in the database. The functionality is implemented using the **'getAll'** endpoint.
- **View Actor Details:** Users can view details of a specific actor by providing the actor's ID. This functionality is implemented using the **'findById'** endpoint.
- **Add Actor:** Users can add a new actor to the database by providing the actors filmography, name and age. This functionality is imiplemented using the **'create'** endpoint.
- **Update Actor Details:** Users can update details of an existing actor by providing the actor's ID and updated information. This functionality is implemented using the **'update'** endpoint.
- **Delete Actor:** Users can delete an existing actor from the database by providing the actor's ID. This dunctionality is implemented using the **'delete'** endpoint.

## **Usage**
To run the actor management system open the following URL address in any browser or click on the link below.

[### **_Actor Management System_**]: (https://DanielMcDonagh.eu.pythonanywhere.com/actors)

