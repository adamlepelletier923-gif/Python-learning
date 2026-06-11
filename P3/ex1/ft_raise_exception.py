def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if (temp > 40):
        raise ValueError(f"{temp} is too hot for plant (max 40°C)")
    elif (temp < 0):
        raise ValueError(f"{temp} is too cold for plant (min 0°C)")
    return (temp)


def test_temperature(temp_str: str) -> None:
    print(f"Input data is {temp_str}")
    try:
        value = input_temperature(temp_str)
        print(f"Temperature is now {value}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")
