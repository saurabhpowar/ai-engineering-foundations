device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal")
else:
    print("Device is offline")

#Practice Program: Temperature Check
temperature_Minus = -20

if temperature_Minus < 0:
    print("Temperature is below freezing point")
    if temperature_Minus < -10:
        print("Extreme cold alert!")
    else:
        print("Moderate cold alert!")
else:
    print("Temperature is above freezing point")
