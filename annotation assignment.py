#Import the correct package
import json

json_data = []

#Open the file using open()
with open("small_sample.json", "r") as infile:
    for line in infile:
        json_data.append(json.loads(line))

#Print first 5 comments - You can adjust as needed
for i in range(5):
    print(json_data[i])
    print("\n---\n")