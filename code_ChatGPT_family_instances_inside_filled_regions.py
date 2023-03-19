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

def MapFamilyInstancesToFilledRegions(doc):
    # Get the built-in category for filled regions
    filled_regions_category = BuiltInCategory.OST_FilledRegion

    # Get all the filled regions in the document
    filled_regions = FilteredElementCollector(doc).OfClass(FilledRegion).WhereElementIsNotElementType().ToElements()
    # Create a dictionary to map family instances to filled regions
    family_instance_to_region = {}

    # Loop through all the filled regions
    for region in filled_regions:
        # Get the boundaries of the filled region
        options = SpatialElementBoundaryOptions()
        boundaries = region.GetBoundaries()

        # Loop through all the boundaries of the filled region
        for boundary in boundaries:
            # Check if any family instances intersect the boundary
            filter = ElementIntersectsSolidFilter(boundary.GetCurve().CreateTransformed(Transform.Identity))
            instances = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).OfClass(FamilyInstance).WherePasses(filter).ToElements()

            # Add the family instances to the dictionary
            for instance in instances:
                if instance not in family_instance_to_region:
                    family_instance_to_region[instance] = region

    # Print the family instances and the filled regions they are in
    for instance, region in family_instance_to_region.items():
        name = instance.Name
        region_name = region.Name
        print("{0} is in {1}".format(name, region_name))

# Execute the function
doc = __revit__.ActiveUIDocument.Document
MapFamilyInstancesToFilledRegions(doc)
