import argparse 
from audio_utilities import reconstruct_signal_griffin_lim as grif 
import audio_utilities
import numpy as np
import time
import sys
import os
import librosa as lr
import os.path
import subprocess
from subprocess import call
import argparse
from tqdm import tqdm
import scipy.misc

parser = argparse.ArgumentParser(description='''                                                                                                                                                            
This script will convert all spectrograms into wavs using the griffin lim algorithm while maintaining input folder structure.''')

parser.add_argument('input_folder', help='Folder contaning all wav files', action='store')
parser.add_argument('output_folder', help='Output folder', action='store')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
input_dir = args.input_folder
output_dir = args.output_folder

if not os.path.exists(input_dir):
    print("Input directory does not exist")
    sys.exit()
if input_dir[-1] != "/":
    input_dir = input_dir + '/'

if not os.path.exists(output_dir):
    print("Output directory created")
    os.makedirs(output_dir)
if output_dir[-1] != "/":
    output_dir = output_dir + '/'


for root, subdirs, files in os.walk(input_dir):
    for name in tqdm(files):

        if name.endswith(".npy"):
            iname = "%s/%s" % (root,name);
            root_out = root.replace(input_dir, output_dir)
            if not os.path.exists(root_out):
                os.makedirs(root_out)

            oname = "%s/%s-griffinlim-reconstructed.wav" % (root_out,name[:-4]);

            S = np.load(iname)
            y_inv = lr.griffinlim(S)
            audio_utilities.save_audio_to_file(y_inv, sr, outfile=oname)


print ("Done!\n");
