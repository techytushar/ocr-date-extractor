import pytesseract
from PIL import Image
import numpy as np
import datetime
import re
from dateparser import parse

from utils import rescale_image, threshold, crop_img, find_bbox, remove_noise_and_smooth


def find_date(text):
    regex = r"((19|20)?\d{1,2}\s?[-/]\s?\d{1,2}\s?[-/]\s?(19|20)?\d{2})|"\
    r"((Jan|Feb|Mar|Apr|May|Jun|June|Jul|Aug|Sept|Sep|Oct|Nov|Dec)"\
    r"\s?\d{1,2}\s?[,']?\s?(19|20)?\d{2})|(\d{1,2}\s?[-/]?\s?"\
    r"(Jan|Feb|Mar|Apr|May|Jun|June|Jul|Aug|Sept|Sep|Oct|Nov|Dec)"\
    r"\s?[',-/]?\s?(19|20)?\d{1,2})"
    pattern = re.compile(regex, flags=re.IGNORECASE)
    matches = list(re.finditer(pattern, text))
    if len(matches)==0:
        return None
    date = matches[0].group(0)
    return parse(date)

def pipeline(img_name):
    path = f'./static/uploaded_images/{img_name}.jpeg'
    try:
        img = Image.open(path)
    except:
        return ValueError
    # preprocessing image
    img = rescale_image(img)
    thresh = threshold(img)
    cnts, bbox = find_bbox(thresh)
    img = crop_img(img, bbox)
    final_img = remove_noise_and_smooth(img)
    # finding text in image
    text = pytesseract.image_to_string(final_img)
    # searching for dates
    date = find_date(text)
    if date is None:
        return date
    return date.strftime("%Y-%m-%d")
