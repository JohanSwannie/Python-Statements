
# * Write a Flat File from a List

data = [
    ["James Mower walks down the street, singing with the birds"],
    ["Carol Brown laughs at the funny clown on a TV program"],
    ["Gary Mayson sings a beautiful song while playing the guitar"],
    ["Caroline Barrett leads a team of programmers to better"],
]


output_file1 = "output.txt"
delimiter = ","

with open(output_file1, "w") as file1:
    for row in data:
        line = delimiter.join(row) + "\n" 
        file1.write(line) 

print(f"Data written to {output_file1}")

# * Read from one Flat File & Write to another Flat File

input_file = "input.txt"

with open(input_file, "r") as textFile:
    linesRead = textFile.readlines()
    
output_file2 = "output2.txt"
    
with open(output_file2, "w") as file2:
        for line in linesRead:
            outputLine = line.strip() + "\n"
            file2.write(outputLine) 
        
print(f"Data written to {output_file2}")

# * Write a Flat File from a JSON File

import json

def flattenJson(y):
    out = {}
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
    flatten(y)
    return out

with open('input.json', 'r') as inputJson:
    jsonData = json.load(inputJson)

flattenedData = flattenJson(jsonData)

with open('output3.txt', 'w') as file3:
    for key, value in flattenedData.items():
        file3.write(f"{key}: {value}\n")
        
