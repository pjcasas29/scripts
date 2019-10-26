import time
import sys
import os
import os.path
import subprocess
from subprocess import call
import argparse
from tqdm import tqdm
import audio2cqt
import scipy.misc

parser = argparse.ArgumentParser(description='''
This script will convert all audio into cqt while maintaining input folder structure.''')

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

#os.environ["LD_LIBRARY_PATH"] = "/local/scratch/DeepLearning/tools/music2image/linux";


for root, subdirs, files in os.walk(input_dir):
    for name in tqdm(files):
        
        if os.path.splitext(name)[1] == ".wav":
            iname = "%s/%s" % (root,name);
            root_out = root.replace(input_dir, output_dir)
            if not os.path.exists(root_out):
                os.makedirs(root_out)

            oname = "%s/%s.png" % (root_out,name[:-4]);
        
            cmd = "python3 audio2cqt.py '%s' '%s' &"% (iname,oname)
        
            #process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            #process.wait()
            #time.sleep(0.01)
            
            call(cmd, shell=True);

print ("Done!\n");
