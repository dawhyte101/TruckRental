from flask import Flask
from flask import request, redirect
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy
from models import *

# set up the application and point it at the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.s3db'
db.init_app(app)

@app.route("/")
def index():
    """ Create a view with all of the data """
    
    # retrieve all of the customers, trucks, and reservations
    all_cust = db.session.query(Customer).all()
    all_trucks = db.session.query(Truck).all()
    all_reservations = db.session.query(Reservation).all()
    
    # populate the template with these lists and return the rendered template
    return render_template("home.html", customers = all_cust, 
        trucks = all_trucks, 
        reservations = all_reservations)

@app.route("/delete-truck", methods=["POST"])
def delete_truck():
    """ Removes a truck from the database by ID """
    truck_id = request.args.get("id", None)
    truck = db.session.query(Truck).get(truck_id)
    db.session.delete(truck)
    db.session.commit()
    
    return redirect("/")
        
@app.route("/edit-truck", methods=["GET", "POST"])
def edit_truck():      
    """ On GET, creates a view that can be used to add or edit a truck.
        On POST, saves or updates a truck and redirects to the index.
    """
    if request.method == "GET":
    
        # check for the truck Id parameter, if supplied, load the existing truck
        truck_id = request.args.get("id", None)
        if truck_id:
            truck = db.session.query(Truck).get(truck_id)
        else: # no truck Id, this is an add
            truck = None
        return render_template("edit-truck.html", truck=truck)
    else:
        model = request.form["model"]
        mileage = request.form["mileage"]
        # check if the truck already exists, and do an update if so
        if request.form["id"]:
            existing_truck = db.session.query(Truck).get(request.form["id"])
            existing_truck.model = model
            existing_truck.mileage = mileage
            db.session.commit()
        else:
            new_truck = Truck(model, mileage)
            db.session.add(new_truck)
            db.session.commit()
            
        return redirect("/")
        
# run the application if this was started from the command line    
if __name__ == "__main__":

    # create any new database objects
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)

