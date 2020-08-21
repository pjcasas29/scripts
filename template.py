import argparse
import os 

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', type=str, default='0', help='Specify which GPUs to use separated by a comma. Ex: 2,3')

opt = parser.parse_args()

os.environ['CUDA_VISIBLE_DEVICES']=opt.gpu
