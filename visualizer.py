import numpy as np
import open3d as o3d
import argparse

if __name__ == "__main__":
    ## parsing args
    parser = argparse.ArgumentParser(description="visualizing custom")
    parser.add_argument("--filename", help="*.ply filename", type=str, default="None")
    args = parser.parse_args()
    filename = args.filename
    if ( filename == "None" ):
        print("not specified filename, use with flag --filename [filename]")
        exit()

    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud(filename)
    o3d.visualization.draw_geometries([pcd])
