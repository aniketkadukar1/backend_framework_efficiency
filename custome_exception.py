class LessThanOne(Exception):
    def __init__(self, message="LessThanOneException occur"):
        self.message = message
    
    def __str__(self):
        return self.message


def sub(a, b):
    if a-b > 1:
        return 10
    else:
        raise LessThanOne("heuyyy")

try:
    sub(10, 12)
except Exception as e:
    print(e)
else:
    print("Do this if not exception...")
finally:
    print("Must do...")    