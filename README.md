# OCR Date Extractor

Flask API to extract dates from documents

## How to use

The API is provided with 2 routes:

* If you want to pass Base64 encoded image, send a POST request with payload `{"base_64_image_content": <base_64_image_bytes>}` to

```
https://ocr-date-extractor.herokuapp.com/extract_date
```

* If you want to pass image file, send a POST request with payload `{'image': <image_file>}` to

```
https://ocr-date-extractor.herokuapp.com/extract_date_from_image
```

Python sample code to test out the API:

```python
import requests, base64
img_url = <path_to_image>
with open(img_url, 'rb') as f:
    img = base64.b64encode(f.read())
response = requests.post('https://ocr-date-extractor.herokuapp.com/extract_date', data={'base_64_image_content':img})
print(response.content)
```

## Working

The project performs the following steps for any given image:

* Re-scales the image if its too big in size
* Performs thresholding to separate foreground (the document) and the background
* Find contours and draws a bounding box on the document present in the image
* Crops the image to keep only the document
* Performs thresholding again to separate text from the background
* Apply OCR to extract text
* Use regex to extract out the date
* Date is then parsed and returned in `YYYY-MM-DD` format 

## Supported Date Formats

Following date format are supported with some flexibility:

* dd-mm-yyyy
* mm-dd-yyyy
* yyyy-mm-dd
* dd/mm/yyyy
* mm/dd/yyyy
* yyyy/mm/dd
* Aug23'19
* Feb 24, 2019
* 24 May'19

## References

I took help from the following resources:

* Improving OCR Accuracy [Medium](https://medium.com/cashify-engineering/improve-accuracy-of-ocr-using-image-preprocessing-8df29ec3a033)
* [OpenCV Docs](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
* Automatic Canny Edge [PyImageSearch](https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/)
