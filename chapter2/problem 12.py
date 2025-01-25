#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point liesinside the circle, on the circle or outside the circle.
def check_point(x, y, cx, cy, r):
    # Calculate the distance from the point to the center
    dist = (x - cx)**2 + (y - cy)**2
    radius = r**2
    
    # Check if the point is inside, on, or outside the circle
    if dist < radius:
        return "Inside"
    elif dist == radius:
        return "On the circle"
    else:
        return "Outside"

# Example usage
x, y = 3, 4   # Point coordinates
cx, cy = 0, 0  # Circle center
r = 5          # Circle radius

print(check_point(x, y, cx, cy, r))
