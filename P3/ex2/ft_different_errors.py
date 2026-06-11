def garden_operations(operation_number: int):
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        return (10/0)
    elif (operation_number == 2):
        return (open("/non/existent/file"))
    elif (operation_number == 3):
        return ("stt" + 3)
    elif (operation_number == 4):
        return ("Operation completed successfully")


def test_error_types():
    for i in range(0, 5):
        print(f"Testing operation {i} ")
        try:
            result = garden_operations(i)
            print(f"{result}")
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, TypeError) as e:
            print(f"Caught {type(e).__name__}: {e}")


if __name__ == "__main__":
    test_error_types()
