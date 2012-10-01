gestaltexp
==========

This script reproduces the partially occluded pictures described in
Doniger et al, 2000, Journal of Cognitive Neuroscience, "Activation
timecourse of ventral visual stream processes high density mapping of
perceptual closure processes." As per the author's specification, the
input images should be 256x256. The image is divided in a 16x16
grid. A (1 - 0.7^(LEVEL-1)) share of the grid elements that are not
totally white is then occluded with white (as the sample image appears
to have a white background), and the results are stored in BMP files.

Prerequisites: 

* Python 2.7 (direct downlaod for windows 32 bit:
  http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi)
* The Python Imaging Library (PIL) for Python 2.7 (direct download for
  windows: http://effbot.org/downloads/PIL-1.1.7.win32-py2.7.exe)


In this repo:

* the file elephant_256x256_clean.bmp, which is a sample input from
  the original paper.
* the script "script.py", to be run from your operating system's
  command-line. Usage information (also available by running script.py
  -h):

    Usage: script.py [-l LEVEL] [-o OUTPUT] filename

    Options:
      -h, --help            show this help message and exit
      -l LEVEL, --level=LEVEL
                            desired fragmentation level between 1 and 8
      -o OUTPUT, --output=OUTPUT
                            base output file name

Example:

python2 script.py elephant_256x256_clean.bmp

I tested the script on Windows 7 64bit, Windows XP 32bit, and Linux 32
bit, all worked as expected. I do not expect any difficulty on a Mac
either. However, if you find a bug, please do tell me.
