def fetch_sales():
    print("Fetching the sales data")


def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summarizing sales data")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready")


generate_report()


#Practise

def skoda():
    print("Skoda is a car brand")

def engine_type(a):
    print(f"Skoda has {a} engine type")

def car_color(color):
    print(f"Skoda has {color} color")


def car_details(engine, color):
    skoda()
    engine_type(engine)
    car_color(color)
    print("Car details are ready")  

car_details("Petrol", "Silver")