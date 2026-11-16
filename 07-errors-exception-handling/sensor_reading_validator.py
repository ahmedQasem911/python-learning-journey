# Sensor Readings Validator
# -------------------------
# A simple program that processes a list of sensor readings, skips the invalid
# ones, and calculates the average of the valid ones.
#
# How it works:
#     1. Stores the sensor readings as a list of dictionaries.
#     2. Parses each reading: reads the sensor name, converts the value to a
#        float, and rejects values outside the supported range (-50 to 100).
#     3. Catches errors for missing keys, wrong types, and bad values, and
#        prints a message for each invalid reading instead of crashing.
#     4. Calculates and prints the average of the valid readings, or
#        "No valid readings" if there are none.
#
# Concepts practiced:
#     - Lists of dictionaries
#     - Error handling with try / except (KeyError, TypeError, ValueError)
#     - Raising exceptions with raise
#     - Functions with return values (returning a tuple)
#     - Type conversion with float()
#     - Generator expressions with sum()
#     - Conditional logic (if / else)
#     - String formatting with f-strings

readings = [
    {"sensor": "greenhouse", "value": "23.5"},
    {"sensor": "freezer", "value": "not available"},
    {"value": "18.0"},
    {"sensor": "boiler", "value": "140"},
    {"sensor": "cooler", "value": None},
]


def parse_reading(reading):
    sensor = reading["sensor"]
    value = float(reading["value"])
    if value < -50 or value > 100:
        raise ValueError(f"{sensor} reported an unsupported value.")
    return sensor, value


valid_readings = []

for reading in readings:
    try:
        valid_readings.append(parse_reading(reading))
    except KeyError as error:
        message = f"Key Error: {error}"
        print(message)
    except TypeError as error:
        message = f"Type Error: {error}"
        print(message)
    except ValueError as error:
        message = f"Value Error: {error}"
        print(message)


if valid_readings:
    average = sum(value for _, value in valid_readings) / len(valid_readings)
    print(round(average, 1))
else:
    print("No valid readings")
