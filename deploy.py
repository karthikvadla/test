import os
from PIL import Image
from array import *
import numpy
from krypton import logger
from io import BytesIO

def prep_image(input):
    logger.info("input: {}".format(input))
    format = Image.open(BytesIO(input)).format
    if format is 'PNG':
        tmp_file_name = '/tmp/input_image.png'
    else:
        tmp_file_name = '/tmp/input_image.jpg'
    jpg_file = open(tmp_file_name, 'w+')
    jpg_file.write(input)
    jpg_file.close()
    os.system('./single-resize-script.sh {}'.format(tmp_file_name))
    filename = '/tmp/input_image.png'
    data_image = array('B')
    Im = Image.open(filename)
    pixel = Im.load()
    width, height = Im.size
    for x in range(0,width):
        for y in range(0,height):
            data_image.append(pixel[y,x])
    image_ndarray =  numpy.frombuffer(data_image, dtype=numpy.uint8)
    image = image_ndarray.reshape(1, image_ndarray.shape[0])
    return {"images": image}

def preprocess(input, model):
    return prep_image(input)

def predict(data, predict_fn):
    return predict_fn(data)['scores']

def postprocess(output, input):
    return numpy.argmax(output)
