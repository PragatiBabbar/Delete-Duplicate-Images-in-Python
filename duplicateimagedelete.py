#               code by - @PragatiBabbar

"""
Lets Understand the logic first::

1. At first, we open the directory where we are going to work. This is done by changing the current directory to chdir(ie child directory)
2. We then initialize a list and a dictionary
3. Then we create a hash value for each image in that folder using hashlib.md5. this creates a 32-bit hash value.
4. After this, with the help of this hash value, we store it in either a dictionary or a list.
5. I am plotting the same images again for your better understanding in the try block. You can skip this part if you want.
6. Finally, I am removing the duplicate images using os.remove
"""

# code implementation

import hashlib
from scipy.misc import imread, imresize, imshow
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import os
def file_hash(filename):
    with open(filename,'rb') as f:
        return md5(f.read()).hexdigest()

os.getcwd()
os.chdir(r'D:\pytest')
os.getcwd()

files_list = os.listdir('.')
print (len(files_list))

duplicates=[]
hash_keys=dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]=index
        else:
            duplicates.append((index,hash_keys[filehash]))
print(duplicates)
for file_indexes in duplicates[:30]:
    try:
        plt.subplot(121),plt.imshow(imread(files_list[file_indexes[1]]))
        plt.title(file_indexes[1]),plt.xticks([]),plt.yticks([])

        plt.subplot(122),plt.imshow(imread(files_list[file_indexes[0]]))
        plt.title(str(file_indexes[0])+ 'duplicate'),plt.xticks([]),plt.yticks([])
        plt.show()

    except OSError as e:
        continue

for index in duplicates:
    os.remove(files_list[index[0]])