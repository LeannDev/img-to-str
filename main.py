import os
import sys

from pdf2image import convert_from_path
from PIL import Image
import pytesseract

# |-----> install tesseract-ocr <-----|

# Si no tiene el ejecutable tesseract en su RUTA, incluya lo siguiente:
#pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

# |-----> descargar idioma español <-----|
# https://github.com/tesseract-ocr/tessdata/raw/4.00/spa.traineddata
# en la ruta /usr/share/tesseract-ocr/4.00/tessdata
lang = 'spa'


# PDF file to convert
file = 'archivo2.pdf'

pages = convert_from_path(file, 500) #500
contador = 1

# Convert PDF to images
for page in pages:
    page.save('./images/page_' + str(contador) + '.jpg', 'JPEG')
    contador += 1

file_limit = contador - 1

# Extract text from images
for i in range(1, file_limit + 1):

    outfile = './out_txt/msj_' + str(i) + '.txt'
    filename = './images/page_' + str(i) + '.jpg'

    # # open img in RGB mode
    img = Image.open(filename)

    # # size of the image in pixels
    # width, height = img.size

    # # point for cropped image
    # left = 0
    # top = 0
    # right = width
    # bottom = 1900

    # # cropped image
    # img = img.crop((left, top, right, bottom))

    # # save the cropped image
    # img.save(filename)

    # open txt file
    f = open(outfile, 'w')

    # extract text from image using pytesseract with a custom fonts
    text = str(pytesseract.image_to_string(img, lang=lang, config='--psm 6 --oem 3 -c tessedit_char_whitelist=DOTMATRI.TTF'))


    #text = str(pytesseract.image_to_string(img, lang=lang, )) 
    text = text.replace('-\n', '')

    # write text to file
    f.write(text)

    # remove old file and close txt file
    #os.remove(filename)
    f.close()

# iterate over the list of files
for i in range(1, file_limit + 1):
    # open file
    f = open('./out_txt/msj_' + str(i) + '.txt', 'r')

    # search for the word 'Unit'
    word1 = 'Serie Nro:'
    for line in f:
        if word1 in line:
            # position of the word 'Unit' in line
            pos = line.find(word1)
            # position end of the word 'Unit' in line
            pos_end = pos + len(word1)
            # extract the rest of the line
            rest = line[pos_end:]

            print(rest)

    # close file
    f.close()


print('Done')
