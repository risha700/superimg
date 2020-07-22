import argparse

from PIL import Image
import math
import sys

class SuperImage(object):
    """
    class utilizes Pillow to compress and resize images through cli interface
    :parameter
    - src : path for the image ->str
    - output: name and image output path ->str
    - rotate: rotates angle ->int
    - xval: value of x axis to crop ->int
    - yval: value of y axis to crop ->int
    - quality: rate of quality ->int

    usage:
    python superimg.py -h
    python superimg.py -i test_imgs/blue_me.jpeg -r -90 -x 50 -y 30 --q 30
    """
    def __init__(self, src, *args, **kwargs):
        args = parser.parse_args() or sys.argv
        self.src = args.input
        self.output = lambda:args.output or self.src[:-4]+'_out.'+self.src[-4:]
        self.rotate = args.rotate
        self.xval = args.xval
        self.yval = args.yval
        self.quality = args.quality
        self.image = None

    def load_image(self):
        try:
            self.image = Image.open(self.src)
        except Exception as e:
            print('ERROR: %s' %e)
            print('src path must be specified -i ..filepath or --input ..filepath')
            return False

    def compress(self):
        self.load_image()
        x, y = self.image.size
        nx, ny = math.floor(x - self.xval), math.floor(y - self.yval)
        self.image = self.image.resize((nx, ny), Image.ANTIALIAS
                                       ).rotate(self.rotate, fillcolor=None, expand=True)
        file_name = self.output()
        self.image.save(file_name, quality=self.quality, optimize=True)
        self.image.show()
        print("new image saved %s" % file_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input','-i', help="input image src path")
    parser.add_argument('--output','-o', help="name or full path of output:optional ")
    parser.add_argument('--rotate','-r', help="rotate value:optional ", type=int, default=0)
    parser.add_argument('--xval','-x', help="X coordinate value to trim", type=int, default=0)
    parser.add_argument('--yval','-y', help="Y coordinate value to trim", type=int, default=0)
    parser.add_argument('--quality','-q', help="chosen quality defaults to 50", type=int, default=50)
    args = parser.parse_args()

    SuperImage(src=args.input, out=args.output, rotate=args.rotate,
             xval=args.xval, yval=args.yval, quality=args.quality).compress()
