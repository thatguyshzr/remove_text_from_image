# Detect and remove text from image using Keras-ocr
<img src="https://img.shields.io/badge/Python-3.7.9-brightgreen">

## Setup
```
pip install -r requirements.txt
```
-----------------------------------------
## detect_text.py
Extract text from image.

Input: ![Input image](assets/billboard.jpg "Input image")
Output: 
```
['top', '15', 'freelance', 'billboard', 'lulu', 'new', 'designers', 'summer', 'collection', '2022', 'for', 'hire', 'in', 'designhill']
```

-------------------------------------------
## rem_text.py
Remove text from image using cv2's inpaint function.

| Input | Output |
| ------|--------|
| ![Input image](assets/london.jpg "Input image") | ![Input image](assets/rem_text_output.jpg "Output image")