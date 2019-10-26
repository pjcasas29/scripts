import librosa
import argparse
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt 
import imageio
import scipy.misc

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="path of the audio file")
    parser.add_argument("out_path", help= "Output file path")
    parser.add_argument("-d", "--display_graph", help="Will display a matplotlib graph if set to true", action="store_true")
    parser.add_argument("-sr", "--sample_rate", type=int, default=None, help="Manually set the sample rate of the audio")
    args = parser.parse_args()
    return args

def audio2cqt(file_path, sample_rate=None, hop_l=256, fmin=librosa.note_to_hz('C1'), n_bins= 48, filter_scale=0.8, display=False):
    
    y, sr = librosa.load(file_path, sr=sample_rate)
    q_transform = librosa.core.cqt(y, sr=sr, hop_length=hop_l, fmin=fmin, n_bins=n_bins, filter_scale=filter_scale)
    #print(sr)
    if(display):
        
        C = np.abs(q_transform)
        librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), sr=sr, x_axis='time', y_axis='cqt_note') 
        plt.colorbar(format='%+2.0f dB')
        plt.title('Constant-Q power spectrum')
        plt.tight_layout()
        plt.show()
        
    return q_transform

if __name__ == '__main__':
    args = parse_arguments()
    q_transform = audio2cqt(args.file_path, sample_rate=args.sample_rate, display=args.display_graph)
    imageio.imwrite(args.out_path, np.abs(q_transform))
    #scipy.misc.imsave(args.out_path, np.abs(q_transform))
