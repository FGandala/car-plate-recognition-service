import cv2
import easyocr 


class OCRService:
    def __init__(self, image):
        self._cv2Color = cv2.COLOR_BGR2GRAY
        self._thresholding_type = cv2.THRESH_BINARY_INV
        self._thresh = 64
        self._maxval = 255
        self._reader = easyocr.Reader(['en'], gpu=False)
        pass


    def _format_license_plate(text):
        
        formated_text = list(text)

        dict_char_to_int = {'O': '0',
                    'I': '1',
                    'J': '3',
                    'A': '4',
                    'G': '6',
                    'S': '5'}

        dict_int_to_char = {'0': 'O',
                    '1': 'I',
                    '3': 'J',
                    '4': 'A',
                    '6': 'G',
                    '5': 'S'}
        
        for  i in range(len(text)):
            if (i < 3 and text[i].isdigit()):
                text[i] = dict_int_to_char[text[i]]
            
            if (i == 3 and text[i].isalpha()):
                text[i] = dict_char_to_int[text[i]]
            
            if (i == 4 and text[i].isdigit()):
                text[i] = dict_int_to_char[text[i]]
            
            if(5<= i <7 and text[i].isalpha()):
                text[i] = dict_char_to_int[text[i]]
        
        return "".join(formated_text)



    def _verify_license_plate_format(text):

        first_part = text[0:3]
        second_part = text[3]
        third_part = text[4]
        fourth_part = text[5:7]

        if(len(text) != 7):
            return False
        
        if not (first_part.isalpha() and
         second_part.isdigit() and
         third_part.isalpha() and
         fourth_part.isdigit()):
            return False
        
        return True


    def process_license_plate(self, license_plate_image):
        license_plate_crop_gray = cv2.cvtColor(license_plate_image,self._cv2Color)
        license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, self._thresh, self._maxval, self._thresholding_type)


        detections = self._reader.readtext(license_plate_crop_thresh)

        for detection in detections:
            bbox, text, score = detection

            text = text.upper()
            is_license_plate_format_validy = self._verify_license_plate_format(text)

            if(is_license_plate_format_validy):
                return self._format_license_plate(text), score
            
            raise Exception("Formato da placa inválido!")
