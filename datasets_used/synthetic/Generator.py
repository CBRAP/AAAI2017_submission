# -*- coding: utf-8 -*-

import numpy as np

nbArms = 100
nbUsers = 20
nbFeatures = 100
sparsity = 0.5
#nbFeedback=np.random.randint(nbArms*nbUsers*0.3)
nbFeedback=np.random.randint(nbArms*nbUsers*0.2,high=nbArms*nbUsers*0.4)
with open("ft.txt",'w') as f:
    for i in range(nbArms):
        a = np.random.rand(nbFeatures)  
        sparse_number = sparsity*nbFeatures
        sequence = np.random.choice(nbFeatures, int(sparse_number), replace=False) # sample without replacement
        for pos in sequence:
            a[pos] = 0.0
        f.writelines(["%s " % item  for item in a])
        f.write('\n')
        
with open("fb.txt",'w') as f:
    for i in range(nbFeedback):
        f.write(''+str(np.random.randint(nbUsers))+' '+str(np.random.randint(nbArms)) +' 1')
        f.write('\n')