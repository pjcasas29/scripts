#!/usr/bin/python

import sys
import os
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description='''
This script will normalize all wav files in a folder to a given value''')

parser.add_argument('dB', help='Normaization Value', action='store')
parser.add_argument('input_folder', help='Folder contaning all wav files', action='store')
parser.add_argument('output_folder', help='Output folder', action='store')

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


def sh_escape(s):
   return s.replace("(","\\(").replace(")","\\)")

os.environ["LD_LIBRARY_PATH"] = "/local/scratch/DeepLearning/tools/music2image/linux";

norm_value = args.dB
input_dir = args.input_folder
output_dir = args.output_folder

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
    for name in files:

        iname = "%s/%s" % (root,name);
        root_out = root.replace(input_dir, output_dir)
        if not os.path.exists(root_out):
            os.makedirs(root_out)
        oname = "%s/%s" % (root_out,name);
        
        cmd = sh_escape("sox --norm=" + norm_value + " " + iname.replace(' ', '\\ ') + " " + oname.replace(' ', '\\ '))
        #print cmd
        call(cmd, shell=True);

print ("Done!\n");
