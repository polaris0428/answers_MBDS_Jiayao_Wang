m = [9, 9, 9, 9, 90000, 90000]
n = [9, 9, 9, 9, 100000, 100000]
data = [65, 72, 90, 110, 87127231192, 5994891682]
# Use a particular solution to solve the problem.    
for i in range(len(m)):
    # The numbers 1 through m must contain at least one in the array. First, calculate them.
    num = 0
    for j in range(m[i]):
        num = num + 1 + j
    k = n[i] - 1 # The number of rest numbers left.
    l = data[i] - num # The sum of rest numbers left.
    # Allocate the rest numbers to k or k + 1.
    start = l // k 
    rest = l % k 
    order = []
    for j in range(k - rest):
        order.append(start)
    for j in range(rest):
        order.append(start + 1)
    # Add the numbers to the list, add the initial number 1 - 9, and sort them.
    for j in range(m[i]):
        order.append(j+1)
        order.sort()
    # Match numbers with letters 'R' and 'D'.
    for j in range(len(order) - 1):
        if order[j] == order[j + 1]:
            order[j] = 'R'
        else:
            order[j] = 'D' 
    order.pop()
    # Convert the list to a string.
    result = ''.join(order)
    # Wirte the answer into a new file.
    with open('output_question_1','a') as f:
        f.write(str(data[i]))
        f.write(' ')
        f.write(result)
        f.write('\n')
