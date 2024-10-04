#!/bin/bash
START_TIME=$(date +%s%3N)

# 実行するPythonスクリプト

#ノーマル
python3 /home/PointPillarsZh/evaluate_time.py --data_root /home/data_v2/KITTI/kitti_data_PointPillarsZh --num_workers 12 --ckpt /home/PointPillarsZh/my_output/my_pillar_logs/git_ori_160_5freq/checkpoints/epoch_60.pth

#z hist Early Fusion
python3 /home/PointPillarsZh/evaluate_time.py --data_root /home/data_v2/KITTI/kitti_data_PointPillarsZh --num_workers 12 --ckpt /home/PointPillarsZh/my_output/my_pillar_logs/z_hist_normalized/checkpoints/epoch_10.pth

#z hist Late Fusion
python3 /home/PointPillarsZh/evaluate_time.py --data_root /home/data_v2/KITTI/kitti_data_PointPillarsZh --num_workers 12 --ckpt /home/PointPillarsZh/my_output/my_pillar_logs/late_fusion_normalized_zhist_double_bn/checkpoints/epoch_60.pth

END_TIME=$(date +%s%3N)
EXECUTION_TIME=$(($END_TIME - $START_TIME))

echo "Execution time: $EXECUTION_TIME milliseconds"
