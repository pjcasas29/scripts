#!/usr/bin/python

import sys
import os
from subprocess import call
import argparse
from tqdm import tqdm
import wave
import contextlib


parser = argparse.ArgumentParser(description='''
This script will split the wav files into smaller files of a given length''')

parser.add_argument('length', help='Amount to split the file by', action='store')
parser.add_argument('input_folder', help='Folder contaning all wav files', action='store')
parser.add_argument('output_folder', help='Output folder', action='store')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


def sh_escape(s):
   return s.replace("(","\\(").replace(")","\\)")

os.environ["LD_LIBRARY_PATH"] = "/local/scratch/DeepLearning/tools/music2image/linux";


input_dir = args.input_folder
output_dir = args.output_folder
length = args.length



if not os.path.exists(input_dir):
    print("Directory does not exist")
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
        if os.path.splitext(name)[1] == ".wav":  
            iname = "%s/%s" % (root,name);
            with contextlib.closing(wave.open(iname,'r')) as f:
                frames = f.getnframes()
                rate = f.getframerate()
                duration = frames / float(rate)
                print(duration)
            

            root_out = root.replace(input_dir, output_dir)
            if not os.path.exists(root_out):
                os.makedirs(root_out)
            count = 0
            for i in range(0, int(duration), int(length)): 
                oname = "%s/%s%s" % (root_out,str(count),name);
        
                cmd = sh_escape("sox " + iname.replace(' ', '\\ ') + " " + oname.replace(' ', '\\ ') + " trim " + str(i) + " " + str(length))

                #cmd = sh_escape("sox " + iname.replace(' ', '\\ ') + " " + oname.replace(' ', '\\ ') + " trim " + start + " " + end)
                #print(cmd)
                call(cmd, shell=True);
                count += 1

print ("Done!\n");
