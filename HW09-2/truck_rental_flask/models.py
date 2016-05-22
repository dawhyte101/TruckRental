from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(150))

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        
class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100))
    mileage = db.Column(db.Integer)
    
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage
        
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    truck_id = db.Column(db.Integer, db.ForeignKey("truck.id"))
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    
    def __init__(self, customer_id, truck_id, start_time, end_time):
        self.customer_id = customer_id
        self.truck_id = truck_id
        self.start_time = start_time
        self.end_time
