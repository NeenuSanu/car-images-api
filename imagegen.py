import json

# Initialize an empty list to store the objects
image_objects = []

# Loop through the range of numbers from 2 to 34
for i in range(2, 35):
    # Create a dictionary for each image with the name and URL
    image_object = {
        "name": str(i),
        "url": f"https://raw.githubusercontent.com/NeenuSanu/car-images-api/refs/heads/main/images/{i}.avif"
    }
    # Append the dictionary to the list
    image_objects.append(image_object)

# Convert the list of dictionaries to a JSON string for display
json_output = json.dumps(image_objects, indent=2)
print(json_output)
