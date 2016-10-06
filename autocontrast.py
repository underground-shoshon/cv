from __future__ import print_function
from sys import argv
import os.path
import cv2
import numpy as np


def autocontrast(src_path, dst_path, white_perc, black_perc):
    img = cv2.imread(src_path, 0)
    res = np.zeros((img.shape), np.uint8)
    L = [(img[x,y], x, y) for x in range(img.shape[0]) for y in range(img.shape[1])]
    L.sort()
    n, m = int(img.size * black_perc), int(img.size * (1 - white_perc))
    a, b = L[n][0], L[m][0]

    for (i,x,y) in L[:n]:
        res[x,y] = 0
    for (i,x,y) in L[n:m]:
        res[x,y] = int((img[x,y] - a) * 255.0 / (b - a))
    for (i,x,y) in L[m:]:
        res[x,y] = 255

    cv2.imwrite(dst_path, res)

if __name__ == '__main__':
    assert len(argv) == 5
    assert os.path.exists(argv[1])
    argv[3] = float(argv[3])
    argv[4] = float(argv[4])

    assert 0 <= argv[3] < 1
    assert 0 <= argv[4] < 1
    assert argv[3] + argv[4] <= 1

autocontrast(*argv[1:])
