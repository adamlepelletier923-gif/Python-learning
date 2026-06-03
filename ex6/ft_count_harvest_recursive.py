def ft_count_harvest_recursive(i):
    if i == 0:
        return
    else:
        ft_count_harvest_recursive(i - 1)
        print("Day", i, " ")


""""
if __name__ == "__main__":
    day = int(input("Days until harvest: "))
    ft_count_harvest_recursive(day)
    print("Harvest time!")
"""
