class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def grow(self):
        self._height += 0.8

    def set_height(self, height):
        if height >= 0:
            self._height = height
        else:
            print("Error: height can't be negative")

    def get_height(self):
        return self._height

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Error: age can't be negative")

    def get_age(self):
        return self._age

    def show(self):
        print(self.name, ":", round(self._height, 1),
              "cm,", self._age, "days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)

    rose.show()

    rose.set_height(40)
    rose.set_age(35)

    rose.show()

    print("Height =", rose.get_height())
    print("Age =", rose.get_age())

    rose.set_height(-10)
    rose.set_age(-5)

    rose.show()
