import os.path

# Replace "data" and "genes.txt" with whatever directory and file (respectively) you would like to work with. 
data_file = os.path.join("data", "genes.txt")

# Check if file exists
if os.path.exists(data_file):
    print("file", data_file, "exists")
    with open(data_file) as f:
        newdict = {}
        first_line = f.readline()
        for row in f:
            y = row.split('	')
            newdict[y[0]] = (int(y[2])-int(y[1]))
            print(str(y[0]) + ' is ' + str(int(y[2]) - int(y[1])) + ' nucleotides long.')
else:
    print("file", data_file, "not found!")

# Write dictionary to new CSV. Replace "newtest.csv" with file you want to create.
with open('newtest.csv', 'w') as f:
    writer = csv.writer(f)
    for row in newdict.items():
        writer.writerow(row)
