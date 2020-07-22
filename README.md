# superimg
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
    
# License
MIT