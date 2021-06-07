# This is a script that calculates WER of different decades in vks_kotus_sample.json. 
# There are currently some decades not analysed, as we got sufficient picture when
# we just ensured that there are no excessive gaps of several decades.
# Also the current corpus is temporally relatively limited, so this is a minor issue. 
# In the further work more data from all decades should be included. 
# Currently missing decades are 1690, 1720, 1740 and 1770. 

from mikatools import *
from collections import Counter
from random import sample, random
from jiwer import wer
import matplotlib.pyplot as plt

test = json_load("old_literary_finnish.json")

x = []
y = []

for year in test:
    
    ground_truth = []
    hypothesis = []
    
    for s in year:
        
        if 'language' not in s:
        
            ground_truth.append(s['sentence_gt'])
            hypothesis.append(s['sentence_n'])

    error = wer(ground_truth, hypothesis)
    
    print(year[0]['decade'], error)
    
    if error > 0.0:
    
        x.append(year[0]['decade'])
        y.append(error)

plt.plot(x, y)

