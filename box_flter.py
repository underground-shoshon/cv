from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np

def box_flter(src_path, dst_path, w, h):
    img = cv2.imread(src_path)
    bordered = cv2.copyMakeBorder(img, h, h, w, w, cv2.BORDER_REFLECT)

    P = np.zeros((bordered.shape[0]+1, bordered.shape[1]+1, bordered.shape[2]), np.uint64)
    for x in range(1, bordered.shape[0]+1):
        for y in range(1, bordered.shape[1]+1):
            P[x,y] = bordered[x-1,y-1] + P[x-1,y] + P[x,y-1] - P[x-1,y-1]

    res = np.zeros(img.shape, np.uint8)
    size = (2*w+1)*(2*h+1)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            res[x,y] = (P[x+2*h+1,y+2*w+1] + P[x,y] - P[x+2*h+1,y] - P[x,y+2*w+1]) // size

    cv2.imwrite(dst_path, res)
    
if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = int(argv[3])
    argv[4] = int(argv[4])
    assert argv[3] > 0
    assert argv[4] > 0

box_flter(*argv[1:])

