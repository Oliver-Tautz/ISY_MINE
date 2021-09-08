from os import listdir
import json
import numpy as np

for filename in listdir('.'):
    if 'json' in filename:
        print('----')
        d=json.load(open(filename,'r'))
        print(filename)
        d_rewards=d['reward']
        zeros = len(d_rewards)-np.count_nonzero(d_rewards)
        print(f"mean={np.mean(d_rewards)}\tstd={np.std(d_rewards)}\tmax={np.max(d_rewards)}\tmin={np.min(d_rewards)}\tno_zero={zeros}") 
