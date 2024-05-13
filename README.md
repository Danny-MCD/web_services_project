
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
The python programs are being hosted on the website [**PythonAnywhere**]: (https://eu.pythonanywhere.com/)
To run the Actor Management System open the following URL address in any browser or click on the links provided.

#### **Actor Management System**
URL = https://DanielMcDonagh.eu.pythonanywhere.com/actorviewer.html
Link = [### **_Actor Management System_**]: (https://DanielMcDonagh.eu.pythonanywhere.com/actorviewer.html)

#### **Sample Database**
URL = https://DanielMcDonagh.eu.pythonanywhere.com/actors
Link = [### **_Database_**]: (https://DanielMcDonagh.eu.pythonanywhere.com/actors)

## **Execution of Code**
All code for these assignments was written on Visual Studio Code ver.1.88 and executed using Python 3.10 interpreter. 


## **Software Requirement and Links**
Below are links to the free software packages you will need to install on your own PC to be able to run and execute the code.

**Anaconda** - An open-source and free platform that will let you install and manage thousands of Python packages and enviroments.
https://www.anaconda.com/download/success

**Visual Studio Code** - A free and lightweight code editor for building applications.
https://code.visualstudio.com/Download





## **References**
All python, HTML, CSS and JavaScript code has been referenced extensivly from Andrew Beatty's lectures in the module **Web Services and Applications**.

