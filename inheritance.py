class MobilePhone:
    def __init__(self):
        self.screenType = "Touch"
        self.networkType = "4G/5G"

    def make_call(self):
        print("Calling...")

class Apple(MobilePhone):
    def __init__(self, model):
        super().__init__()
        self.model = model

class Samsung(MobilePhone):
    def __init__(self, model):
        super().__init__()
        self.model = model


# objects
iphone = Apple("iPhone 14")
samsung = Samsung("Galaxy S23")

iphone.make_call()
print(iphone.model)

samsung.make_call()
print(samsung.model)
