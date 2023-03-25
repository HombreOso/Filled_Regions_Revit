def point_in_polygon(point, polygon):
    # Unpack the point coordinates
    x, y = point
    
    # Number of vertices in the polygon
    n = len(polygon)
    
    # Boolean to keep track of whether the point is inside the polygon or not
    inside = False
    
    # Starting vertex of the current side of the polygon
    p1x, p1y = polygon[0]
    
    # Loop over all sides of the polygon
    for i in range(n + 1):
        # Ending vertex of the current side of the polygon
        p2x, p2y = polygon[i % n]
        
        # Check if the current side intersects with a horizontal line
        # drawn from the point to the right
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        # Calculate the x-coordinate of the intersection
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        # If an intersection is found, flip the inside status
                        inside = not inside
        # Move to the next side of the polygon
        p1x, p1y = p2x, p2y
        
    # Return the final inside status
    return inside



# point = (x, y)
# polygon = [(x1, y1), (x2, y2), ..., (xn, yn)]
# result = point_in_polygon(point, polygon)