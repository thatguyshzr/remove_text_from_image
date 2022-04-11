import keras_ocr

def text_detector_1000(img_path):
    """Extract text from image

    Args:
        img_path (string): path to image

    Returns:
        list: list of words in the image
    """
    img = keras_ocr.tools.read(img_path)
    pipeline= keras_ocr.pipeline.Pipeline()
    prediction_groups = pipeline.recognize([img])
    return [i[0] for i in prediction_groups[0]]

print(text_detector_1000('billboard.jpg'))