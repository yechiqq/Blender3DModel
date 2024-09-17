import bpy

geometry_name = ''
vertices = []
edges = []
faces = []

def generate_data(name):
    global geometry_name, vertices, edges, faces
    geometry_name = name
    match name:
        case 'Tetrahedron':
            #(sqrt(8/9),0,-1/3), (-sqrt(2/9), -sqrt(2/3), -1/3), (-sqrt(2/9), sqrt(2/3), -1/3), (0, 0, 1)
            vertices = [(0.943,0,-0.333), (-0.471,-0.816,-0.333), (-0.471,0.816,-0.333), (0, 0, 1)]
            faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
            
        case 'Cube':
            #(±1, ±1, ±1)
            vertices = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1)]
            faces = [(0, 1, 2, 3), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7), (4, 5, 6, 7)]
            
        case 'Octahedron':
            vertices = [(0, 0, -1), (-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
            faces = [(0, 1, 2), (0, 2, 3), (0, 3, 4), (0, 4, 1), (5, 1, 2), (5, 2, 3), (5, 3, 4), (5, 4, 1)]
        
        case 'Dodecahedron':
            #gold ratio r = 1.618, 1/r = 0.618, (±1, ±1, ±1), (0, ±r, ±1/r), (±1/r, 0, ±r), (±r, ±1/r, 0)
            vertices = [(1, 1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1), (1, 1, -1), (1, -1, -1), (-1, -1, -1), (-1, 1, -1),
            (0, 1.618, 0.618), (0, -1.618, 0.618), (0, -1.618, -0.618), (0, 1.618, -0.618),
            (0.618, 0, 1.618), (-0.618, 0, 1.618), (-0.618, 0, -1.618), (0.618, 0, -1.618), 
            (1.618, 0.618, 0), (-1.618, 0.618, 0), (-1.618, -0.618, 0), (1.618, -0.618, 0)]
            faces = [(8, 11, 4, 16, 0), (8, 11, 7, 17, 3), (9, 10, 5, 19, 1), (9, 10, 6, 18, 2),
            (12, 13, 3, 8, 0), (12, 13, 2, 9, 1), (15, 14, 7, 11, 4), (15, 14, 6, 10, 5),
            (16, 19, 1, 12, 0), (16, 19, 5, 15, 4), (17, 18, 2, 13, 3), (17, 18, 6, 14, 7)]
            #rotation x 31.7 degree to level up 2 faces
            
        case 'Icosahedron':
            #gold ratio r = 1.618, (0, ±1, ±r), (±r, 0, ±1), (±1, ±r, 0)
            vertices = [(0, 1, 1.618), (0, -1, 1.618), (0, 1, -1.618), (0, -1, -1.618),
            (1.618, 0, 1), (1.618, 0, -1), (-1.618, 0, 1), (-1.618, 0, -1),
            (1, 1.618, 0), (-1, 1.618, 0), (1, -1.618, 0), (-1, -1.618, 0)]
            faces = [(0, 1, 4), (0, 1, 6), (2, 3, 5), (2, 3, 7),
            (4, 5, 8), (4, 5, 10), (6, 7, 9), (6, 7, 11),
            (8, 9, 0), (8, 9, 2), (10, 11, 1), (10, 11, 3),
            (0, 4, 8), (1, 4, 10), (1, 6, 11), (0, 6, 9),
            (2, 5, 8), (3, 5, 10), (3, 7, 11), (2, 7, 9)]
            #rotation y 20.9 degree to level up 2 faces

# make mesh
#generate_data('Tetrahedron')
generate_data('Cube')
#generate_data('Octahedron')
#generate_data('Dodecahedron')
#generate_data('Icosahedron')
new_mesh = bpy.data.meshes.new(geometry_name)
new_mesh.from_pydata(vertices, edges, faces)
new_mesh.update()

# make object from mesh
new_object = bpy.data.objects.new(geometry_name, new_mesh)
bpy.context.view_layer.active_layer_collection.collection.objects.link(new_object)


