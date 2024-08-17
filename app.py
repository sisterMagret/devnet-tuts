def my_decorator(fun):
    def wrapper():
        print("perform task before function calls")
        fun()
        print("perform task after function calls")
    return wrapper


@my_decorator
def greet():
    print("Greetings!")
    

greet()