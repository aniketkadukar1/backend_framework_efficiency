def functionality(func):
    def wrapper(a, b):
        print("Before Addition ...")
        func(a, b)
        print("After Addition...")
        return func
    return wrapper

@functionality
def add(a, b):
    print(a + b)

add(19, 1)