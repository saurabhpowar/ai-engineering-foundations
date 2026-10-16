def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")

# Write a generator called tea_counter() that waits for a tea name, prints Making: <tea name>, then pauses and waits for the next name.

# Start it with next(), then send it "Ginger Tea" and "Mint Tea" using .send().

def tea_counter():
    print("Welcome! What tea would you like?")
    tea_name = yield
    while True:
        print(f"Making: {tea_name}")
        tea_name = yield


tea = tea_counter()
next(tea)
tea.send("Ginger Tea")
tea.send("Mint Tea")
