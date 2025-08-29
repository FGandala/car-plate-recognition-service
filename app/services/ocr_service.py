import cv2


class OCRService:
    def __init__(self, image):
        self._cv2Color = cv2.COLOR_BGR2GRAY
        self._thresholding_type = cv2.THRESH_BINARY_INV
        self._thresh = 64
        self._maxval = 255
        pass

    def process_license_plate(self, license_plate_image):
        license_plate_crop_gray = cv2.cvtColor(license_plate_image,self._cv2Color)
        license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, self._thresh, self._maxval, self._thresholding_type)
