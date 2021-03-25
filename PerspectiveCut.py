import numpy as np
import pandas as pd
import open3d as o3d

print("To cut the perspective of the original PCD")

pcd = o3d.io.read_point_cloud("./test1.pcd")
# o3d.visualization.draw_geometries([pcd])

max_dis = 0.90
max_x = 0.20
max_y = 0.20
pcd_points = np.asarray(pcd.points)
pcd.clear()
pcd_points = pcd_points[(pcd_points[:, 2] < max_dis)]
pcd_points = pcd_points[(pcd_points[:, 0] < max_x)]
pcd_points = pcd_points[(pcd_points[:, 0] > -max_x)]
pcd_points = pcd_points[(pcd_points[:, 1] < 0.1)] # down
pcd_points = pcd_points[(pcd_points[:, 1] > -0.2)] # up

pcd.points = o3d.utility.Vector3dVector(pcd_points)
o3d.visualization.draw_geometries([pcd])
