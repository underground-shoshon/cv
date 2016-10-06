from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np

def gamma_correction(src_path, dst_path, a, b):
    img = cv2.imread(src_path, 0)
    res = np.zeros((img.shape), np.uint8)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            res[x,y] = int(255*a*(img[x,y]/255.0)**b)
    cv2.imwrite(dst_path, res)

if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

gamma_correction(*argv[1:])
