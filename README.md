# 3d-reconstruction-processing---intel-LiDAR-Sensor
3d reconstruction use LiDAR sensor

# Hardware Information (datasheet)

![hardward image](./readme.images/lidar_camera_gallery_6.jpg)

| Features |  |  |  
| ------- | --- | --- |
|  *Use Environment* | *Technology* | *Ideal range* |
| Indoor | Laser Scanning | .25m to 9m (Range affected by reflectivity) |

| Depth |  |  |  | | |
| ------- | --- | --- | --- | --- | --- |
|  *Depth technology* | *Depth Field of View (FOV)* | *Minimum depth distance (Min-Z) at max resolution* | *Depth output resolution* | *Depth Accuracy* | *Depth frame rate* |
| LiDAR | 70° × 55° (±3°) | ~25cm | Up to 1024*768 | ~5 mm to ~14 mm thru 9m**2 | 30fps |

| RGB | | | | | 
| ------- | --- | --- | --- | --- |
| *RGB frame resolution* | *RGB sensor FOV(H\*V)* | *RGB frame rate* | *RGB sensor resolution* | *RGB sensor technology* |
| 1920 * 1080 | 70° × 43° (±3°) | 30 fps | 2 MP | Rolling Shutter |

| Major Components | | 
| --- | --- |
| *Processing* | *Optical Board* |
| Intel RealSense Vision ASIC | Laser & MEMS Mirror |

| Physical | | | |
| --- | --- | --- | --- |
| *Form Factor* | *Connectors* | *Diameter \* Height* | *Mounting mechanism* |
| Camera Peripheral | USB-C\*3.1 Gen 1\* | 61mm * 26 mm | One 1/4‑20 UNC thread mounting point. & Two M3 thread mounting points. & Tripod



# Process work

```
1. Hardware Settings
- Intrinsic Parameter
- LiDAR depth limit(?)
- Etc.
2. Export data (image & depth)
- export RGB(.jpg) & Depth (.png)
3. Make Fragments (.ply)
4. Make 3D-Object
```

# Environment settings

- Python 3.8, open3d 0.15.1 with conda environment 
```

```

# Result

# Reference
- Paper
```
```
- Blog Posting & Etc.
```
- https://www.intelrealsense.com/lidar-camera-l515/
- http://www.open3d.org/docs/release/tutorial/sensor/realsense.html
```