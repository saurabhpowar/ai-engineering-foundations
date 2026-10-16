
chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()

#Practise

def vehiceltype():
    vehicle_type = "Car"
    def update_vehicle():
        nonlocal vehicle_type
        vehicle_type = "Bike"
    update_vehicle()
    print("After update", vehicle_type)


vehiceltype()