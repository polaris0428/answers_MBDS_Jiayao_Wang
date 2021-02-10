[L1, L2] = [50, 57]
# Read the file of coordinates.
with open('input_coordinates_7_1.txt','r') as f1:
        coordinates=[]
        for line in f1.readlines():
            line=line.strip('\n')
            data=line.split('\t')
            coordinates.append(data)
# Create a new array to store the indexs of the points.
index=['index']
# Iterate through all the coordinates in the array and convert them to indexs according to the formula.
for i in range(1, len(coordinates)):
    index.append(int(coordinates[i][0]) + int(coordinates[i][1]) * L1)
# Write the result into a new file.
with open('output_index_7_1.txt','w') as f2:
    for i in range (len(index)):
        f2.write(str(index[i]))
        f2.write('\n')