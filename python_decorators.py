
def add_dec(func):
    def wrapper(*args, **kwargs):
        print("Before Addition...")
        func(*args)
        print("After Addition...")
        return func
    return wrapper



def addition(a, b):
    print(a + b)

add_dec(addition(11, 23))