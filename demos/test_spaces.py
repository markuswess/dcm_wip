from ngsolve import *
import dualcellspaces as dcs


print("### 2d spaces ###")
print('')
mesh = Mesh(unit_square.GenerateMesh())

print("number of elements = {}".format(mesh.ne))
print("number of vertices (= number of dual elements) = {}".format(mesh.nv))
print("number of edges = {}".format(mesh.nedge))
print('')
h1primal = dcs.H1PrimalCells(mesh,order=0)
print("number of H1PrimalCells dofs = {}".format(h1primal.ndof))
h1dual = dcs.H1DualCells(mesh,order=0)
print("number of H1DualCells dofs = {}".format(h1dual.ndof))
hDivprimal = dcs.HDivPrimalCells(mesh,order=0)
print("number of HDivPrimalCells dofs = {}".format(hDivprimal.ndof))
#hDivdual = dcs.HDivDualCells(mesh,order=0)
#print("number of HDivDualCells dofs = {}".format(hDivdual.ndof))
hCurlprimal = dcs.HCurlPrimalCells(mesh,order=0)
print("number of HCurlPrimalCells dofs = {}".format(hCurlprimal.ndof))
hCurldual = dcs.HCurlDualCells(mesh,order=0)
print("number of HCurlDualCells dofs = {}".format(hCurldual.ndof))
print('')
print('')
print("### 3d spaces ###")
print('')
mesh3d = Mesh(unit_cube.GenerateMesh())

print("number of elements = {}".format(mesh3d.ne))
print("number of vertices (= number of dual elements) = {}".format(mesh3d.nv))
print("number of edges = {}".format(mesh3d.nedge))
print("number of faces = {}".format(mesh3d.nface))
print('')
h1primal = dcs.H1PrimalCells(mesh3d,order=0)
print("number of H1PrimalCells dofs = {}".format(h1primal.ndof))
h1dual = dcs.H1DualCells(mesh3d,order=0)
print("number of H1DualCells dofs = {}".format(h1dual.ndof))
hDivprimal = dcs.HDivPrimalCells(mesh3d,order=0)
print("number of HDivPrimalCells dofs = {}".format(hDivprimal.ndof))
#hDivdual = dcs.HDivDualCells(mesh3d,order=0)
#print("number of HDivDualCells dofs = {}".format(hDivdual.ndof))
hCurlprimal = dcs.HCurlPrimalCells(mesh3d,order=0)
print("number of HCurlPrimalCells dofs = {}".format(hCurlprimal.ndof))
hCurldual = dcs.HCurlDualCells(mesh3d,order=0)
print("number of HCurlDualCells dofs = {}".format(hCurldual.ndof))
