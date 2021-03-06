[L1, L2] = [50, 57]
# Read the file of indexs.
with open('input_index_7_1.txt','r') as f1:
        index=[]
        for line in f1.readlines():
            line = line.strip('\n')
            index.append(line)
# Create a new array to store the coordinates of the points.
coordinates=[['x1','x2']]
# Iterate through all the indexs in the array and convert them to coordinates according to the formula.
for i in range(1, len(index)):
    coordinates.append([int(index[i]) % L1, int(index[i]) // L1])
# Write the result into a new file.
with open('output_coordinates_7_1.txt','w') as f2:
    for i in range(len(coordinates)):
        for j in range(len(coordinates[0])):
            f2.write(str(coordinates[i][j]))
            f2.write('\t')
        f2.write('\n')
