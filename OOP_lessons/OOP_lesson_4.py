class Try_str:
    def __init__(self, a):
        self.a = a

    def __str__(self):
        return "My word is " + self.a


try_str = Try_str("privet")
print(try_str)
