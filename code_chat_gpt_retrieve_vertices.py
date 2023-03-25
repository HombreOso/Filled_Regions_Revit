import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *

doc = __revit__.ActiveUIDocument.Document
uidoc = __revit__.ActiveUIDocument

# Select a filled region element
ref = uidoc.Selection.PickObject(ObjectType.Element, "Select a filled region")

# Retrieve the geometry of the selected filled region
elem = doc.GetElement(ref.ElementId)
geom = elem.GetGeometryObjectFromReference(ref)

# Loop through the geometry of the filled region to retrieve the coordinates of the vertices
for geo in geom:
    if isinstance(geo, Solid):
        faces = geo.Faces
        for face in faces:
            if face.MaterialElementId == elem.MaterialElementId:
                loops = face.EdgeLoops
                for loop in loops:
                    for edge in loop:
                        start = edge.AsCurve().GetEndPoint(0)
                        end = edge.AsCurve().GetEndPoint(1)
                        print("Start point: ({}, {})".format(start.X, start.Y))
                        print("End point: ({}, {})".format(end.X, end.Y))
