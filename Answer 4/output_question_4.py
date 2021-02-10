# Read the file of data.
with open('input_question_4','r') as f1:
    data = [[int(num) for num in line.split('\t')] for line in f1]
# Initialize an array to store all the nonzero neighbors connected to the point.
coordinate = []
# Initialize all 1 in the array to -1.
for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                data[i][j] = -1

# Define a function to add nonzero neighbors around the current point.
def adding(i, j, coordinate):
    if i != 0 and data[i - 1][j] != 0 and [i - 1, j] not in coordinate:
        coordinate.append([i - 1, j])
    if i != len(data) - 1 and data[i + 1][j] != 0 and [i + 1, j] not in coordinate:
        coordinate.append([i + 1, j])
    if j != 0 and data[i][j - 1] != 0 and [i, j - 1] not in coordinate:
        coordinate.append([i, j - 1])
    if j != len(data[0]) - 1 and data[i][j + 1] != 0 and [i, j + 1] not in coordinate:
        coordinate.append([i, j + 1])

# Define a funtion to judge whether all nonzero neighbors join in to the array.
def judge(coordinate):
    tmp = []
    for i in range(len(coordinate)):
        tmp.append(coordinate[i])
    for i in range(len(coordinate)):
        adding(coordinate[i][0], coordinate[i][1], coordinate)
    # If not, repeat this function until nonzero neighbors are all added up.
    if tmp != coordinate:
        judge(coordinate)

# Define a function to modify the point with its nonzero neighbors to the correct number.
def modify(i, j, n):
    coordinate = []
    adding(i, j, coordinate)
    # If the point doesn't have nonzero neighbors, modify it to the correct number directly.
    if coordinate == []:
        data[i][j] = n
    else:
        judge(coordinate)
        data[i][j] = n
        for i in range(len(coordinate)):
            data[coordinate[i][0]][coordinate[i][1]] = n

# Set a correct number to which all points need to be modified. The initial value is 1.
n = 1
# Iterate all -1 numbers through the array and modify them.
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == -1:
            modify(i, j, n)
            n = n + 1

# Write the answer into a new file
with open('output_question_4','w') as f2:
    for i in range(len(data)):
        for j in range(len(data[0])):
            f2.write(str(data[i][j]))
            f2.write('\t')
        f2.write('\n')