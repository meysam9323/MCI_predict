# usage: python SAD_longWav.py ../test_data/50010_031512_1b.wav
import sys , wave , pdb
from comboSAD import combosad
import numpy as np
import func as fun

wavFilename =sys.argv[1] 
weight = 0.5 
DEFAULT_FRAME_RATE = 0.01
DEFAULT_FRAME_SIZE = 0.025
duration=1 #length in minute

fp = wave.open(wavFilename)
nt = fp.getnframes()
fs = fp.getframerate()
wav_len = nt/(fs*60) #length in minute
fp.close()
#if nt == 0: # making sure that wav length is not zero
#    VuV = None
#    continue
if wav_len > duration:
    VuV=[]
    step=0
    for i in xrange(int(np.ceil(wav_len/duration))):
        vad_estimate = combosad (wavFilename,weight,int(step*60*fs),int(duration*60*fs))
        VuV.append(vad_estimate)
        step = step + duration
    VuV = np.row_stack(VuV)
else:
    VuV = combosad (wavFilename, weight)

np.savetxt(wavFilename.split('.wav')[0]+'.db',VuV,fmt='%d')
