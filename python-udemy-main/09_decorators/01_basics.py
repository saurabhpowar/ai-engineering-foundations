from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")


greet()
print(greet.__name__)


#Practise code
def function_greet_deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@function_greet_deco
def greet_user(name):
    print(f"Hello {name} from decorators class from chaicode")  

greet_user("Aman")