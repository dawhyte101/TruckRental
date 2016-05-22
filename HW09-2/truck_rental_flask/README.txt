
This project demonstrates a simple application for truck rental management.

Slim Jim's Truck Rental manages three types of database entities: trucks, customers, and reservations. They would like to be able to manage this data from a central location, capable of adding, editing, or deleting any of the entity types. This is commonly known as a CRUD application (create, read, update, delete).

A minimal working example for managing trucks is provided. This includes listing trucks (on the home page -- home.html), adding and editing trucks (both done with edit-truck.html), and deleting trucks (does not require any HTML). The rental.py file uses Flask and the SQLAlchemy querying engine to manage these CRUD operations.


You should be able to run the code using the command:


pip install -r requirements.txt  
python rental.py



Some database objects have already been created and will be pulled in from the existing data.s3db file.
