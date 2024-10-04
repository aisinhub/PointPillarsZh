import argparse
import numpy as np
import os
import torch
import pdb
from tqdm import tqdm

from utils import setup_seed, keep_bbox_from_image_range, \
    keep_bbox_from_lidar_range, write_pickle, write_label, \
    iou2d, iou3d_camera, iou_bev
from dataset import Kitti, get_dataloader
# from model import PointPillars
# from model import PointPillarsNoCenterXyz as PointPillars
from model import PointPillarsLaterCenterXyz as PointPillars


def main(args):
# modelをPPに設定する
    if not args.no_cuda:
        model = PointPillars(nclasses=args.nclasses).cuda()
        model.load_state_dict(torch.load(args.ckpt))
    else:
        model = PointPillars(nclasses=args.nclasses)
        model.load_state_dict(
            torch.load(args.ckpt, map_location=torch.device('cpu')))

model.eval()

#引数を用意
            batched_pts = data_dict['batched_pts']
            batched_gt_bboxes = data_dict['batched_gt_bboxes']
            batched_labels = data_dict['batched_labels']
            batched_difficulty = data_dict['batched_difficulty']
# 実際に推論するところ
            batch_results = model(batched_pts=batched_pts, 
                                  mode='val',
                                  batched_gt_bboxes=batched_gt_bboxes, 
                                  batched_gt_labels=batched_labels)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Configuration Parameters')
    #
    parser.add_argument('--data_root', default='/mnt/ssd1/lifa_rdata/det/kitti', 
                        help='your data root for kitti')
    #
    parser.add_argument('--ckpt', default='pretrained/epoch_160.pth', help='your checkpoint for kitti')
    
    #
    parser.add_argument('--saved_path', default='results', help='your saved path for predicted results')
    parser.add_argument('--batch_size', type=int, default=1)
    parser.add_argument('--num_workers', type=int, default=4)
    parser.add_argument('--nclasses', type=int, default=3)
    parser.add_argument('--no_cuda', action='store_true',
                        help='whether to use cuda')
    #
    args = parser.parse_args()

    main(args)
