"""
    Auto-generated simulation code.
"""
import onscale as on

with on.Simulation('None') as sim:

    # General simulation settings
    on.Scalar(length=0.001, time=0, mass=0)
    on.settings.DisabledPhysics(["thermal", "fluid", "electrical"])

    # Define geometry
    geometry = on.CadFile('connecting-rod.step')

    # Define material database and materials
    materials = on.CloudMaterials('onscale')
    structural_steel = materials['Structural steel']
    structural_steel >> geometry.parts[0]

    # Define and apply loads
    restraint = on.loads.Restraint(x=True, y=True, z=True, alias='Fixture 1')
    restraint >> geometry.parts[0].faces[65]
    pressure = on.loads.Pressure(2000000, alias='Pressure Load 1')
    pressure >> geometry.parts[0].faces[63]

    # Define meshing
    on.meshes.MeshFile('medium_mesh_volume.msh')

    # Define output variables
    on.fields.Displacement()
    on.fields.Stress()
    on.fields.Strain()
    on.fields.VonMises()
    on.fields.PrincipalStress()
    on.fields.PrincipalStrain()
    probe = on.probes.ResultantForce(geometry.parts[0].faces[65])
