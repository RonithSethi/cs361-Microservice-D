import json
import ijson  # Streaming JSON parser
from time import sleep

def get_food_by_index(index):
    """Efficiently fetch a food item by index using streaming parsing."""
    with open("../data/funfacts.json", "r") as file:
        food_iter = ijson.items(file, "item")  # Read items directly
        for i, food in enumerate(food_iter):
            if i == index:
                return json.dumps(food)  # Convert to JSON string and return
    return json.dumps({"error": "Index out of range"})  # If index not found

while True:
    sleep(0.1)  # Prevent excessive CPU usage

    with open("pipeD.txt", "r") as prng:
        x = prng.read().strip()  # Read and strip whitespace

    y = open("pipeD.txt", "w") # clear the txt file
    y.close()

    if x.isdigit():  # Ensure it's a valid integer
        index = int(x)

        result = get_food_by_index(index)  # Fetch food item

        with open("pipeD.json", "w") as out_file:
            out_file.write(result)  # Write JSON result back
