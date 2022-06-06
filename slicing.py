import image_bbox_slicer as ibs

im_src = './dataset'
an_src = './dataset'
im_dst = './dataset_sliced'
an_dst = './dataset_sliced'

slicer = ibs.Slicer()
slicer.config_dirs(img_src=im_src, ann_src=an_src, 
                   img_dst=im_dst, ann_dst=an_dst)

slicer.keep_partial_labels = True

slicer.ignore_empty_tiles = False

slicer.slice_by_number(number_tiles=4)
slicer.visualize_random()

