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

doc = DocumentManager.Instance.CurrentDBDocument
# uiapp = DocumentManager.Instance.CurrentUIApplication
# app = uiapp.Application

doc = __revit__.ActiveUIDocument.Document

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
    
    print("inside ", inside)
    return inside

# Get all the 2D filled regions in the document
filled_regions = FilteredElementCollector(doc).OfClass(FilledRegion).WhereElementIsNotElementType().ToElements()

print(filled_regions)

# Dictionary to store the family instances inside each filled region
family_instances_inside_filled_region = {}


for filled_region in filled_regions:
    # Get the boundary curve loop of the filled region
    boundary_curve_loop = filled_region.GetBoundaries()[0]
			
	# Get the vertices of the boundary curves and convert them into a polygon
    vertices = [(list(boundary_curve_loop.GetCurveLoopIterator())[i].GetEndPoint(0).X, list(boundary_curve_loop.GetCurveLoopIterator())[i].GetEndPoint(0).Y) for i in range(boundary_curve_loop.NumberOfCurves())]
    # Get all the family instances in the document
    collector = FilteredElementCollector(doc)
    family_instances = collector.OfClass(FamilyInstance).ToElements()
    
    print(vertices)
    
    # Check if the family instance lies inside the polygon
    for family_instance in family_instances:
        location_point = family_instance.Location.Point
        print(location_point.X)
        if point_in_polygon((location_point.X, location_point.Y), vertices):
            # Store the family instance inside the filled region
            if filled_region.Id.IntegerValue not in family_instances_inside_filled_region:
                family_instances_inside_filled_region[filled_region.Id.IntegerValue] = []
            family_instances_inside_filled_region[filled_region.Id.IntegerValue].append(family_instance)
            
print(family_instances_inside_filled_region)      
