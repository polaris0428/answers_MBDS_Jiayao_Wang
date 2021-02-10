# Read the file of polygon.
with open('input_question_6_polygon','r') as f1:
    polygon = [[int(num) for num in line.split(' ')] for line in f1]
# Read the file of points.
with open('input_question_6_points','r') as f2:
    points = [[int(num) for num in line.split(' ')] for line in f2]

# Define a function named 'is_inside' to judge whether a point is inside the polygon.
def is_inside(i):
    # Set the number of intersections between ray made through this point 
    # and edges of the polygon to the right of this point. The initial value is 0.
    num = 0
    # Set the coordinate of the point is (px, py).
    [px, py] = [points[i][0], points[i][1]]
    # Set the coordinate of the adjacent points of the polygon are (mx, ny) and (nx, ny).
    for j in range(len(polygon)):
        [mx, my] = [polygon[j][0], polygon[j][1]]
        # If j is the last point, it's adjacent to the first point.
        if j == len(polygon) - 1:
            [nx, ny] = [polygon[0][0], polygon[0][1]]
        # If j is not the last point, it's adjacent to the next point.
        else:
            [nx, ny] = [polygon[j + 1][0], polygon[j + 1][1]]
        # First, judge whether the point coincides with the vertex of the polygon.
        # If yes, the point is inside the polygon.
        if (mx == px and my == py) or (nx == px and ny == py):
            return True
        # If no, make X-axis parallel ray through this point, and judge whether there is an intersection point 
        # between this ray and the edge of the polygon on the right of this point.
        # Then, judge whether the endpoints of the edge of the polygon are on either side of the ray.
        elif (my < py and ny >= py) or (my >= py and ny < py):
            # If they're on either side of the ray, find the point on the edge that has the same y-coordinate as that point.
            x = mx + (py - my) * (nx - mx) / (ny - my)
            # If its x-coordinate is the same as the point, then the two points overlap and the point is inside the polygon.
            if x == px:
                return True
            # If its x-coordinate is to the right of the point, the ray intersects the edge of the polygon.
            elif x > px:
                num = num + 1
    # If the number of intersections is odd, the point is inside the polygon.
    if num % 2 == 1:
        return True
    # If the number of intersections is odd, the point is outside the polygon.
    else:
        return False   

# Iterate through all the points in the array.
# Add 'inside' to the array if the function returns True, otherwise, add 'outside'.
for i in range (len(points)):
    if is_inside(i):
        points[i].append('inside')
    else:
        points[i].append('outside')

# Write the array into a new file.
with open('output_question_6','w') as f3:
    for i in range(len(points)):
        for j in range(len(points[0])):
            f3.write(str(points[i][j]))
            f3.write(' ')
        f3.write('\n')
