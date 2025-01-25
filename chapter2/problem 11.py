def check_collinearity(x1, y1, x2, y2, x3, y3):
    # Calculate the area of the triangle formed by the points
    # If the area is zero, the points are collinear
    area = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    if area == 0:
        return "The points are collinear."
    else:
        return "The points are not collinear."

# Example usage
x1, y1 = 1,2
x2, y2 = 2,4
x3, y3 = 3,6

print(check_collinearity(x1, y1, x2, y2, x3, y3))
