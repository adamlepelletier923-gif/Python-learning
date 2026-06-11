def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    elif age <= 60:
        print("Plant needs more time to grow")


"""
if __name__ == "__main__":
    ft_plant_age()
"""
