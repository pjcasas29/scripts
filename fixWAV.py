import sys
import os
from subprocess import call
import argparse

parser = argparse.ArgumentParser(description='''

Used to fix wav file headers

''')

parser.add_argument('input_folder', help="Folder contaning wav files", action='store')
parser.add_argument('output_folder', help="Output folder", action='store')

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



files = os.listdir(input_dir);

for name in files:
    if name.endswith('.wav'):
        n = name.split(".");
        iname = "%s%s" % (input_dir,name);
        oname = "%s%s.wav" % (output_dir,n[0]);
        cmd = "ffmpeg -i '%s' -map_metadata -1 -fflags +bitexact -flags:v +bitexact -flags:a +bitexact '%s' &"% (iname,oname);
        call(cmd, shell=True);

print ("Done\n");
