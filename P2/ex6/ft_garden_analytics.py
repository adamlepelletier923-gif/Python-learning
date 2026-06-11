class Plant:

    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self):
            print(
                "Stats:",
                self.grow_count,
                "grow,",
                self.age_count,
                "age,",
                self.show_count,
                "show"
            )

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(age):
        return age > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0, 0)

    def grow(self):
        self._height += 0.8
        self._stats.grow_count += 1

    def age(self):
        self._age += 1
        self._stats.age_count += 1

    def show(self):
        self._stats.show_count += 1
        print(
            self.name,
            ":",
            round(self._height, 1),
            "cm,",
            self._age,
            "days old"
        )

    def display_stats(self):
        self._stats.display()


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print("Color:", self.color)

        if self.bloomed:
            print(self.name, "is blooming beautifully!")
        else:
            print(self.name, "has not bloomed yet")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def produce_shade(self):
        self.shade_count += 1

        print(
            "Tree",
            self.name,
            "now produces a shade of",
            self._height,
            "cm long and",
            self.trunk_diameter,
            "cm wide."
        )

    def show(self):
        super().show()
        print("Trunk diameter:", self.trunk_diameter, "cm")

    def display_stats(self):
        super().display_stats()
        print(self.shade_count, "shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self):
        super().grow()
        self.nutritional_value += 1

    def age(self):
        super().age()
        self.nutritional_value += 1

    def show(self):
        super().show()
        print("Harvest season:", self.harvest_season)
        print("Nutritional value:", self.nutritional_value)


def display_plant_statistics(plant):
    print("[statistics for", plant.name + "]")
    plant.display_stats()


if __name__ == "__main__":

    print("=== Check year-old ===")
    print(Plant.is_older_than_year(30))
    print(Plant.is_older_than_year(400))

    print()

    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    display_plant_statistics(rose)

    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print()

    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    display_plant_statistics(oak)

    oak.produce_shade()
    display_plant_statistics(oak)

    print()

    sunflower = Vegetable("Sunflower", 80, 45, "July")

    sunflower.grow()
    sunflower.age()

    sunflower.show()
    display_plant_statistics(sunflower)

    print()

    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_plant_statistics(anonymous)
