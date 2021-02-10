[L1,L2,L3,L4,L5,L6]=[4,8,5,9,6,7]
# Read the file of coordinates.
with open('input_coordinates_7_2.txt','r') as f1:
        coordinates=[]
        for line in f1.readlines():
            line=line.strip('\n')
            data=line.split('\t')
            coordinates.append(data)
# Create a new array to store the indexs of the points.
index=['index']
# Iterate through all the coordinates in the array and convert them to indexs according to the formula.
for i in range(1, len(coordinates)):
    index.append(int(coordinates[i][0]) + int(coordinates[i][1]) * L1 
    + int(coordinates[i][2]) * L1 * L2 + int(coordinates[i][3]) * L1 * L2 * L3 
    + int(coordinates[i][4]) * L1 * L2 * L3 * L4 + int(coordinates[i][5]) * L1 * L2 * L3 * L4 * L5)
# Write the result into a new file.
with open('output_index_7_2.txt','w') as f2:
    for i in range (len(index)):
        f2.write(str(index[i]))
        f2.write('\n')