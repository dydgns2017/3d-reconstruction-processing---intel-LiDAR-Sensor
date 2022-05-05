import open3d as o3d
folder = "../datasets/L515_test"
bag_filename = f"{folder}/L515_test.bag"
bag_reader = o3d.t.io.RSBagReader()
bag_reader.open(bag_filename)
im_rgbd = bag_reader.next_frame()
while not bag_reader.is_eof():
    # process im_rgbd.depth and im_rgbd.color
    im_rgbd = bag_reader.next_frame()

bag_reader.close()