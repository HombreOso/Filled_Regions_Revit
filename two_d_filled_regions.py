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
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

doc = __revit__.ActiveUIDocument.Document

# Get all the 2D filled regions in the document
filled_regions = FilteredElementCollector(doc).OfClass(FilledRegion).WhereElementIsNotElementType().ToElements()

# Dictionary to store the family instances inside each filled region
family_instances_inside_filled_region = {}

for filled_region in filled_regions:
    # Get the boundary curve loop of the filled region
    boundary_curve_loop = filled_region.GetBoundaries()[0]
			
	# Get the vertices of the boundary curves and convert them into a polygon
    vertices = [list(boundary_curve_loop.GetCurveLoopIterator())[i] for i in range(boundary_curve_loop.NumberOfCurves())]
    polygon = Polygon.ByPoints(vertices)
    
    # Get all the family instances in the document
    family_instances = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).OfClass(FamilyInstance).ToElements()
    
    # Check if the family instance lies inside the polygon
    for family_instance in family_instances:
        location_point = family_instance.Location.Point
        if polygon.Contains(Point(location_point.X, location_point.Y)):
            # Store the family instance inside the filled region
            if filled_region.Id.IntegerValue not in family_instances_inside_filled_region:
                family_instances_inside_filled_region[filled_region.Id.IntegerValue] = []
            family_instances_inside_filled_region[filled_region.Id.IntegerValue].append(family_instance)
