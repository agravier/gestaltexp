#!/usr/bin/env python2

# Copyright Alexandre Gravier 2012 (al.gravier@gmail.com)

# This script reproduces the partially occluded pictures described in
# Doniger et al, 2000, Journal of Cognitive Neuroscience, "Activation
# timecourse of ventral visual stream processes high density mapping
# of perceptual closure processes"

import os
from PIL import Image
from optparse import OptionParser
from random import randint

all_levels = range(1, 9)

def main():
    parser = OptionParser("Usage: script.py [-l LEVEL] [-o OUTPUT] filename")
    parser.add_option("-l", "--level", type=int, dest="level",
                      help="desired fragmentation level between 1 and 8", metavar="LEVEL")
    parser.add_option("-o", "--output", dest="output_base",
                      help="base output file name", metavar="OUTPUT")
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments: you must give one file.")
    if options.output_base == None:
        options.output_base = os.path.splitext(args[0])[0]
    if options.level == None:
        options.level = all_levels
    elif not options.level in all_levels:
        parser.error("The processing level should be between 1 and 8.")
    else:
        options.level = [options.level]

    try:
        img = Image.open(args[0])
    except IOError:
        parser.error("Could not open the file " + args[0])

    dims = img.size[0], img.size[1]
    if dims != (256, 256):
        parser.error("The image file is not 256x256, but " + dims[0] + "x" + dims[1])

    for l in options.level:
        m = generate_occluded(img, l);
        i = reconstruct(m)
        i.save(options.output_base + "_level_" + str(l) + ".bmp", "BMP")


def generate_occluded(img, l):
    proportion_of_deleted_segments = 1 - 0.7**(l-1)
    # split up the image in 16x16
    segments_with_drawings = []
    mat = [[None for i in xrange(16)] for j in xrange(16)]
    for y in range(0, 256, 16):
        for x in range(0, 256, 16):
            i, j = x/16, y/16
            mat[i][j] = Image.new("RGB", [16, 16], (255, 255, 255))
            tile = img.crop((x, y, x+16, y+16))
            mat[i][j].paste(tile, (0, 0))
            colors = mat[i][j].getcolors()
            if not (len(colors) == 1 and colors[0][1] == (255, 255, 255)):
                segments_with_drawings.append((i, j))
    n_segments_to_remove = \
        int(round(proportion_of_deleted_segments * len(segments_with_drawings), 0))
    indices_to_remove = []
    if n_segments_to_remove >= len(segments_with_drawings):
        raise RuntimeError("The drawing will be empty.")
    while len(indices_to_remove) < n_segments_to_remove:
        r = randint(0, len(segments_with_drawings)-1)
        idx = segments_with_drawings[r]
        if not idx in indices_to_remove:
            indices_to_remove.append(idx)
    blank_img = Image.new("RGB", [16, 16], (255, 255, 255))
    for index in indices_to_remove:
        mat[index[0]][index[1]] = blank_img
    return mat


def reconstruct(m):
    img = Image.new("RGB", [256, 256], (255, 255, 255))
    for y in range(0, 256, 16):
        for x in range(0, 256, 16):
            i, j = x/16, y/16
            img.paste(m[i][j], (x, y))
    return img
    
    
if __name__ == "__main__":
    main()
