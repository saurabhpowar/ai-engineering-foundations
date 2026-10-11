seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air conditioned, comfy ride")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")


# Practice Program: Train Seat Selection

Train_Seat_Preferance = input("Enter your train seat preference (lower/upper/middle/side)").lower()

match Train_Seat_Preferance:
    case "lower":
        print("Lower berth - Comfortable and easy to access")
    case "upper":
        print("Upper berth - Good for sleeping, but harder to access")
    case "middle":
        print("Middle berth - Less comfortable, but still a good option")
    case "side":
        print("Side berth - Cheapest option, but less privacy")
    case _:
        print("Invalid train seat preference")