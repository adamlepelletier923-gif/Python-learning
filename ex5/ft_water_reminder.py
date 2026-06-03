def ft_water_reminder():
    day = int(input("Days since last watering: "))
    if day > 2:
        print("Water the plants!")
    elif day <= 2:
        print("Plants are fine")


"""
if __name__ == "__main__":
    ft_water_reminder()
"""
