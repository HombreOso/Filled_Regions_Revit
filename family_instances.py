import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

# Get the current Revit document
doc = __revit__.ActiveUIDocument.Document

# Get all family instances in the document
collector = FilteredElementCollector(doc)
elements = collector.OfClass(FamilyInstance).ToElements()

# Create a dictionary to store the family instances by family type
familyInstancesByType = {}

# Loop through all the family instances and add them to the dictionary based on their family type
for instance in elements:
    familyName = instance.Symbol.Family.Name

    if familyName not in familyInstancesByType:
        familyInstancesByType[familyName] = []

    familyInstancesByType[familyName].append(instance)

# Print out the family instances by family type
for familyName, instances in familyInstancesByType.items():
    print("Family type:", familyName)

    for instance in instances:
        print("\tInstance:", instance.Id.IntegerValue)
