import numpy as np

b = np.load('face.npz')

for i in b.files :
    pass
print(b['a'][0][0][0].size)