class Plant:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def grow(self):
        self.height += 0.8

    def old(self):
        self.age += 1

    def show(self):
        print(self.name, ": ", round(self.height, 1),
              "cm,", self.age, "days old")


if __name__ == "__main__":
    rose = Plant("Rose", 30, 25)

    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print("=== Day ", day, "===")
        rose.grow()
        rose.old()
        rose.show()

    print("Growth this week:", round(rose.height - initial_height, 1))
