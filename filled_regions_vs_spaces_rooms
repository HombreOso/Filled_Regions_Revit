import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
import sys

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Import DocumentManager and TransactionManager
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

# Import RevitAPI
import Autodesk

doc = __revit__.ActiveUIDocument.Document


# __________________________________________________________________
def do_polygons_overlap(polygon1, polygon2):
    """
    Check if two polygons with different numbers of vertices overlap.

    Parameters:
        polygon1 (list): A list of tuples representing the vertices of polygon1.
        polygon2 (list): A list of tuples representing the vertices of polygon2.

    Returns:
        True if the polygons overlap, False otherwise.
    """

    # Check if the polygons intersect.
    for i in range(len(polygon1)):
        for j in range(len(polygon2)):
            if do_line_segments_intersect(polygon1[i], polygon1[(i+1)%len(polygon1)],
                                          polygon2[j], polygon2[(j+1)%len(polygon2)]):
                return True

    # Check if one polygon is inside the other.
    if is_polygon_inside_other(polygon1, polygon2) or is_polygon_inside_other(polygon2, polygon1):
        return True

    # Check if any of the vertices of one polygon is inside the other.
    if is_polygon_vertex_inside_other(polygon1, polygon2) or is_polygon_vertex_inside_other(polygon2, polygon1):
        return True

    # Check if any of the edges of one polygon cross the other.
    if is_edge_of_polygon_crossing_other(polygon1, polygon2) or is_edge_of_polygon_crossing_other(polygon2, polygon1):
        return True

    return False


def do_line_segments_intersect(line1_start, line1_end, line2_start, line2_end):
    """
    Check if two line segments intersect.

    Parameters:
        line1_start (tuple): A tuple representing the starting point of line segment 1.
        line1_end (tuple): A tuple representing the ending point of line segment 1.
        line2_start (tuple): A tuple representing the starting point of line segment 2.
        line2_end (tuple): A tuple representing the ending point of line segment 2.

    Returns:
        True if the line segments intersect, False otherwise.
    """

    # Calculate the orientation of three points.
    def calculate_orientation(p1, p2, p3):
        return (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])

    # Check if the orientations of the line segments are different.
    orientation1 = calculate_orientation(line1_start, line1_end, line2_start)
    orientation2 = calculate_orientation(line1_start, line1_end, line2_end)
    if orientation1 * orientation2 >= 0:
        return False

    # Check if the orientations of the other line segments are different.
    orientation3 = calculate_orientation(line2_start, line2_end, line1_start)
    orientation4 = calculate_orientation(line2_start, line2_end, line1_end)
    if orientation3 * orientation4 >= 0:
        return False

    return True


def is_polygon_inside_other(polygon1, polygon2):
    """
    Check if one polygon is completely inside the other.

    Parameters:
        polygon1 (list): A list of tuples representing the vertices of polygon1.
        polygon2 (list): A list of tuples representing the vertices of polygon2.

    Returns:
        True if one polygon is inside the other, False otherwise.
    """

    # Check if all vertices of polygon1 are inside polygon2.
    for vertex in polygon1:
        if not is_point_inside_polygon(vertex, polygon2):
            return False

    return True
def do_polygons_overlap(polygon1, polygon2):
    """
    Check if two polygons with different numbers of vertices overlap.

    Parameters:
        polygon1 (list): A list of tuples representing the vertices of polygon1.
        polygon2 (list): A list of tuples representing the vertices of polygon2.

    Returns:
        True if the polygons overlap, False otherwise.
    """

    # Check if the polygons intersect.
    for i in range(len(polygon1)):
        for j in range(len(polygon2)):
            if do_line_segments_intersect(polygon1[i], polygon1[(i+1)%len(polygon1)],
                                          polygon2[j], polygon2[(j+1)%len(polygon2)]):
                return True

    # Check if one polygon is inside the other.
    if is_polygon_inside_other(polygon1, polygon2) or is_polygon_inside_other(polygon2, polygon1):
        return True

    # Check if any of the vertices of one polygon is inside the other.
    if is_polygon_vertex_inside_other(polygon1, polygon2) or is_polygon_vertex_inside_other(polygon2, polygon1):
        return True

    # Check if any of the edges of one polygon cross the other.
    if is_edge_of_polygon_crossing_other(polygon1, polygon2) or is_edge_of_polygon_crossing_other(polygon2, polygon1):
        return True

    return False


def do_line_segments_intersect(line1_start, line1_end, line2_start, line2_end):
    """
    Check if two line segments intersect.

    Parameters:
        line1_start (tuple): A tuple representing the starting point of line segment 1.
        line1_end (tuple): A tuple representing the ending point of line segment 1.
        line2_start (tuple): A tuple representing the starting point of line segment 2.
        line2_end (tuple): A tuple representing the ending point of line segment 2.

    Returns:
        True if the line segments intersect, False otherwise.
    """

    # Calculate the orientation of three points.
    def calculate_orientation(p1, p2, p3):
        return (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])

    # Check if the orientations of the line segments are different.
    orientation1 = calculate_orientation(line1_start, line1_end, line2_start)
    orientation2 = calculate_orientation(line1_start, line1_end, line2_end)
    if orientation1 * orientation2 >= 0:
        return False

    # Check if the orientations of the other line segments are different.
    orientation3 = calculate_orientation(line2_start, line2_end, line1_start)
    orientation4 = calculate_orientation(line2_start, line2_end, line1_end)
    if orientation3 * orientation4 >= 0:
        return False

    return True


def is_point_inside_polygon(point, polygon):
    """
    Check if a point is inside a polygon.

    Parameters:
        point (tuple): A tuple representing the point to be checked.
        polygon (list): A list of tuples representing the vertices of the polygon.

    Returns:
        True if the point is inside the polygon, False otherwise.
    """

    # Check if the point is on the boundary of the polygon.
    for i in range(len(polygon)):
        if do_points_overlap(point, polygon[i]):
            return True

    # Check if the point is inside the polygon.
    i, j = 0, len(polygon) - 1
    inside = False
    while i < len(polygon):
        if ((polygon[i][1] > point[1]) != (polygon[j][1] > point[1])) and \
           (point[0] < (polygon[j][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / 
            (polygon[j][1] - polygon[i][1]) + polygon[i][0]):
            inside = not inside
        j = i
        i += 1

    return inside


def do_points_overlap(point1, point2):
    """
    Check if two points overlap.

    Parameters:
        point1 (tuple): A tuple representing the first point.
        point2 (tuple): A tuple representing the second point.

    Returns:
        True if the points overlap, False otherwise.
    """

    return point1 == point2


def is_edge_of_polygon_crossing_other(edge, polygon):
    """
    Check if an edge of a polygon is crossing any of the other edges of the polygon.

    Parameters:
        edge (tuple): A tuple representing the edge to be checked.
        polygon (list): A list of tuples representing the vertices of the polygon.

    Returns:
        True if the edge is crossing any of the other edges of the polygon, False otherwise.
    """

    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if do_edges_overlap(edge, (p1, p2)):
            return True

    return False


def do_edges_overlap(edge1, edge2):
    """
    Check if two edges overlap.

    Parameters:
        edge1 (tuple): A tuple representing the first edge.
        edge2 (tuple): A tuple representing the second edge.

    Returns:
        True if the edges overlap, False otherwise.
    """
    (p1, q1), (p2, q2) = edge1, edge2

    # Find orientations of the four points.
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    # p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def orientation(p, q, r):
    """
    Find the orientation of three points (p, q, r) in a plane.

    Parameters:
        p (tuple): A tuple representing the first point.
        q (tuple): A tuple representing the second point.
        r (tuple): A tuple representing the third point.

    Returns:
        0 if the points are collinear, 1 if the points are in clockwise order, and 2 if the points are in counter-clockwise order.
    """

    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
    
def is_edge_of_polygon_crossing_other(edge, polygon):
    """
    Check if an edge of a polygon is crossing any of the other edges of the polygon.

    Parameters:
        edge (tuple): A tuple representing the edge to be checked.
        polygon (list): A list of tuples representing the vertices of the polygon.

    Returns:
        True if the edge is crossing any of the other edges of the polygon, False otherwise.
    """

    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        if do_edges_overlap(edge, (p1, p2)):
            return True

    return False


def do_edges_overlap(edge1, edge2):
    """
    Check if two edges overlap.

    Parameters:
        edge1 (tuple): A tuple representing the first edge.
        edge2 (tuple): A tuple representing the second edge.

    Returns:
        True if the edges overlap, False otherwise.
    """

    (p1, q1), (p2, q2) = edge1, edge2

    # Find orientations of the four points.
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    # p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def orientation(p, q, r):
    """
    Find the orientation of three points (p, q, r) in a plane.

    Parameters:
        p (tuple): A tuple representing the first point.
        q (tuple): A tuple representing the second point.
        r (tuple): A tuple representing the third point.

    Returns:
        0 if the points are collinear, 1 if the points are in clockwise order, and 2 if the points are in counter-clockwise order.
    """

    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def on_segment(p, q, r):
    """
    Check if a point q lies on the segment pr.

    Parameters:
        p (tuple): A tuple representing the first point of the segment.
        q (tuple): A tuple representing the point to be checked.
        r (tuple): A tuple representing the second point of the segment.

    Returns:
        True if q lies on the segment pr, False otherwise.
    """
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    else:
        return False

def is_polygon_vertex_inside_other(polygon1, polygon2):
    """
    Check if any vertex of polygon1 is inside polygon2.

    Parameters:
        polygon1 (list): A list of tuples representing the vertices of the first polygon.
        polygon2 (list): A list of tuples representing the vertices of the second polygon.

    Returns:
        True if any vertex of polygon1 is inside polygon2, False otherwise.
    """

    for vertex in polygon1:
        if is_point_inside_polygon(vertex, polygon2):
            return True

    return False


# __________________________________________________________________


def do_polygons_intersect(polygon1, polygon2):
    def line_intersect(line1, line2):
        def ccw(x1, y1, x2, y2, x3, y3):
            return (y3-y1)*(x2-x1) > (y2-y1)*(x3-x1)

        x1, y1 = line1
        x2, y2 = line1[1], line1[0]
        x3, y3 = line2
        x4, y4 = line2[1], line2[0]
        return ccw(x1, y1, x3, y3, x4, y4) != ccw(x2, y2, x3, y3, x4, y4) and ccw(x1, y1, x2, y2, x3, y3) != ccw(x1, y1, x2, y2, x4, y4)

    def get_edges(polygon):
        return [(polygon[i], polygon[(i+1)%len(polygon)]) for i in range(len(polygon))]

    edges1 = get_edges(polygon1)
    edges2 = get_edges(polygon2)

    for edge1 in edges1:
        for edge2 in edges2:
            if line_intersect(edge1, edge2):
                return True
    return False


def is_left(A,B,C):
    # returns True if C is on the left of the line AB
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def polygon_clip(subjectPolygon, clipPolygon):
    def inside(p):
        # returns True if point p is inside the clip polygon
        return (cp2[0]-cp1[0])*(p[1]-cp1[1]) > (cp2[1]-cp1[1])*(p[0]-cp1[0])

    def computeIntersection(s, e):
        # calculates the intersection of line segement subject and line cp1,cp2
        dc = [ cp1[0] - cp2[0], cp1[1] - cp2[1] ] # difference between cp1 and cp2
        dp = [ s[0] - e[0], s[1] - e[1] ] # difference between s and e
        n1 = cp1[1] * cp2[0] - cp1[0] * cp2[1] # cross product of dc and cp1,cp2
        n2 = s[1] * e[0] - s[0] * e[1] # cross product of dp and s,e 
        n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
        return [ (n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3 ]

    def clip(subjectPolygon, clipPolygon):
        outputList = subjectPolygon
        cp1 = clipPolygon[-1]

        for clipVertex in clipPolygon:
            cp2 = clipVertex
            inputList = outputList
            outputList = []
            s = inputList[-1]

            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e):
                    if not inside(s):
                        outputList.append(computeIntersection(s, e))
                    outputList.append(e)
                elif inside(s):
                    outputList.append(computeIntersection(s, e))
                s = e
            cp1 = cp2
        return(outputList)

    # Clip the subject polygon against each edge of the clip polygon
    outputPolygon = subjectPolygon
    cp1 = clipPolygon[-1]  # Define cp1 outside the for loop
    for i in range(len(clipPolygon)):
        cp2 = clipPolygon[i]
        edge = [clipPolygon[i-1], cp2]
        outputPolygon = clip(outputPolygon, edge)
        cp1 = cp2  # Update cp1 for the next iteration

    # Calculate the area of the clipped polygon
    if len(outputPolygon) < 3:
        # The clipped polygon has less than 3 vertices, so it is not a valid polygon
        return 0
    else:
        # Use the Shoelace formula to calculate the area of the clipped polygon
        area = 0.0
        j = len(outputPolygon) - 1
        for i in range(len(outputPolygon)):
            area += (outputPolygon[j][0] + outputPolygon[i][0]) * (outputPolygon[j][1] - outputPolygon[i][1])
            j = i
        return abs(area / 2.0)



# Get all the 2D filled regions in the document
filled_regions = FilteredElementCollector(doc).OfClass(FilledRegion).WhereElementIsNotElementType().ToElements()

# Get all rooms and spaces
all_spaces_and_rooms = FilteredElementCollector(doc).OfClass(SpatialElement).WhereElementIsNotElementType().ToElements()

# Dictionary to store the room and spaces ids covered by each filled region
spaces_rooms_inside_filled_region = {}


print(all_spaces_and_rooms)

for filled_region in filled_regions:
    # Get the boundary curve loop of the filled region
    boundary_curve_loop = filled_region.GetBoundaries()[0]
			
	# Get the vertices of the boundary curves and convert them into a polygon
    vertices = [(list(boundary_curve_loop.GetCurveLoopIterator())[i].GetEndPoint(0).X, list(boundary_curve_loop.GetCurveLoopIterator())[i].GetEndPoint(0).Y) for i in range(boundary_curve_loop.NumberOfCurves())]

    for space_room in all_spaces_and_rooms:
        parameters_map = space_room.GetParameters('Number')[0].AsString()
        print('room number', parameters_map)
        boundary_options = SpatialElementBoundaryOptions()
        boundary_segments = space_room.GetBoundarySegments(boundary_options)
        vertices_coordinates = []
        if boundary_segments:
            for boundary_segm_list in boundary_segments:
                for boundary_segm in boundary_segm_list:
                    start_point_room = boundary_segm.GetCurve().GetEndPoint(0)
                    end_point_room = boundary_segm.GetCurve().GetEndPoint(1)
                    vertices_coordinates.append((start_point_room.X, start_point_room.Y))
        
    
        print(vertices_coordinates)
        print('Length_vertices: ', len(vertices_coordinates))
        print('filled region polygon', vertices)
        print('room polygon', vertices_coordinates)
        if vertices_coordinates and do_points_overlap(vertices, vertices_coordinates):

            
            intesection_area = polygon_clip(vertices, vertices_coordinates)

            print('intesection_area: ', intesection_area)

            print('\n\n')