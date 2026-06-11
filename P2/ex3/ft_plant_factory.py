class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(self.name, ":", self.height, "cm,", self.age, "days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)

    plants = [rose, oak, cactus, sunflower, fern]

    print("=== Plant Factory Output ===")

    for plant in plants:
        print("Created:", end=" ")
        plant.show()
