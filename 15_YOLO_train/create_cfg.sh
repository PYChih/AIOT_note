#!/bin/bash
# This script copy and create darknet training config
# Download pretrain weights darknet53
cp /home/pychih/darknet/cfg/yolov3.cfg yolo_config/test_yolo.cfg
sed -i 's/batch=1/batch=64/' yolo_config/test_yolo.cfg
sed -i 's/subdivisions=1/subdivisions=16/' yolo_config/test_yolo.cfg
sed -i 's/max_batches = 500200/max_batches = 4000/' yolo_config/test_yolo.cfg
sed -i '610 s@classes=80@classes=1@' yolo_config/test_yolo.cfg
sed -i '696 s@classes=80@classes=1@' yolo_config/test_yolo.cfg
sed -i '783 s@classes=80@classes=1@' yolo_config/test_yolo.cfg
sed -i '603 s@filters=255@filters=18@' yolo_config/test_yolo.cfg
sed -i '689 s@filters=255@filters=18@' yolo_config/test_yolo.cfg
sed -i '776 s@filters=255@filters=18@' yolo_config/test_yolo.cfg
# number of anchors = 3 in each output feature map
# number of classes = 1
# filters = (4+1+1)*3 = 18
echo "create training cfg on yolo_config/test_yolo.cfg"
echo -e "face\n" > yolo_config/test_yolo.names
echo "create test_yolo.names"
echo -e 'classes= 1\ntrain  = dataset/train.txt\nvalid  = dataset/test.txt\nnames = dataset/test_yolo.names\nbackup = /mydrive/training_example/test_backup' > yolo_config/test_yolo.data
echo "create test_yolo.data"
# cp training config
# cp dataset/test_yolo.data /mydrive/training_example/test_yolo.data
# cp dataset/test_yolo.names /mydrive/training_example/test_yolo.names
# cp cfg/test_yolo.cfg /mydrive/training_example/test_yolo.cfg