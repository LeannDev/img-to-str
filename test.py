import os

from PIL import Image
import pytesseract

filename = 'archivo2.pdf'
outfile = 'test-txt.txt'

# open txt file
f = open(outfile, 'w')

# extract text from image
text = str(pytesseract.image_to_string(Image.open(filename), lang='spa'))
text = text.replace('-\n', '')

# write text to file
f.write(text)