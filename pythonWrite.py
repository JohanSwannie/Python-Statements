
# * Write from a list

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

# * Read from one Text File & Write to another Text File

input_file = "input.txt"

with open(input_file, "r") as textFile:
    linesRead = textFile.readlines()
    
output_file2 = "output2.txt"
    
with open(output_file2, "w") as file2:
        for line in linesRead:
            outputLine = line.strip()
            file2.write(outputLine + "\n") 
        
print(f"Data written to {output_file1} and {output_file2}")