import rhinoscriptsyntax as rs


def point_polyline(curve):
    
    pts = []
    
    ### Start Point
    start_ = rs.CurveStartPoint(curve)
    pts.append(start_)
    
    ### Mid Points
    mid_points = rs.CurveDiscontinuity(curve, 2)
    for i in xrange(len(mid_points)):
        pts.append(mid_points[i])
    
    ### End Point
    # end_ = rs.CurveEndPoint(curve)
    # pts.append(end_)
    
    return pts



def construct_mesh_step(points):
    
    meshes = []
    
    ### step
    for i in xrange(1, len(points) - 1):
        vertex_ = [(0, int(i), int(i)+1, int(i)+1)]
        m = rs.AddMesh(points, vertex_)
        meshes.append(m)
        
    mesh_joined = rs.JoinMeshes(meshes)
    
    return mesh_joined



def construct_mesh_center(points):
    
    meshes = []
    
    ### calc center point
    bbox = rs.BoundingBox(points)
    line = rs.AddLine(bbox[0], bbox[6])
    c = rs.CurveMidPoint(line)
    
    ### set new point list
    points.append(c)
    
    ###
    c_index = len(points) - 1
    # print(c_index)
    
    for j in xrange(len(points) - 1):
        if j < (len(points) - 2):
            vertex_ = [(c_index, int(j), int(j)+1, int(j)+1)]
            # print(vertex_)
            m = rs.AddMesh(points, vertex_)
            meshes.append(m)
        else:
            vertex_ = [(c_index, int(j), 0, 0)]
            # print(vertex_)
            m = rs.AddMesh(points, vertex_)
            meshes.append(m)
    
    mesh_joined = rs.JoinMeshes(meshes)
    
    return mesh_joined



points = point_polyline(CURVE)
# print(points)


point_cp_0 = rs.coerce3dpointlist(rs.CopyObjects(points))
point_cp_1 = rs.coerce3dpointlist(rs.CopyObjects(points))


step = construct_mesh_step(point_cp_0)
center = construct_mesh_center(point_cp_1)



POINTS_ = points
MESH_STEP_ = step
MESH_CENTER_ = center
