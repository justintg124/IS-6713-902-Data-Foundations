#First, save the small_sample json file to your project folder

#Import the correct package
import json

json_data = []

#Open the file using open()
with open("small_sample.json", "r") as file:
    # Read the file line by line and parse each line as a separate JSON object
    for line in file:
        if line.strip():  # Skip empty lines
            json_data.append(json.loads(line))
        
print(len(json_data))

# Change the bracketed number to see more comments
print(json.dumps(json_data[:3], indent=2))  


print("\nComments with spacing:")
for item in json_data:
    if "comment" in item:
        print(item["comment"])
        print()  
