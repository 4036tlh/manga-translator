#import csv
import cv2
import pytesseract
from PIL import Image
import json

record = False
show = True
ratio = 1/4

# define pytesseract exe path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'

def extract_text_from(image_path):
    # text extraction
    ret = pytesseract.image_to_boxes(Image.open(image_path), lang = 'jpn+ch')

    # record the text
    if record:
        with open('data.json', 'wb') as fp:
            for t in ret:
                fp.write(json.dumps(t[0], ensure_ascii=False).encode("utf8"))
    
    if show:
        # Draw the bounding box
        img = cv2.imread(image_path)
        h, w, _ = img.shape

        for b in ret.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

        # resize the image ready to show
        img = cv2.resize(img,(int(w*ratio),int(h*ratio)))

        # show annotated image and wait for keypress
        cv2.imshow('result', img)
        cv2.waitKey(0)
    
    return ret




