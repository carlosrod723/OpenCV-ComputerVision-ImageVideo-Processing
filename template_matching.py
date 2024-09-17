# Import necessary libraries and packages
import os
import cv2

class TemplateMatching:
    def __init__(self, image_path, template_path):

        # Initialize with the path to the image and template
        self.image_path= image_path
        self.template_path= template_path
        self.image= cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE) # Load the image in grayscale
        self.template= cv2.imread(self.template_path, cv2.IMREAD_GRAYSCALE) # Load the template in grayscale

    def match_template(self):
        '''Match the template in the image and draw a rectangle around the best match'''

        if self.image is None or self.template is None:
            print('Error: Image or template not found.')
            return None
        
        # Apply template matching
        result= cv2.matchTemplate(self.image, self.template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

        # Draw a rectangle around the matched region
        h, w= self.template.shape
        top_left= max_loc
        bottom_right= (top_left[0] + w, top_left[1] + h)
        matched_image= self.image.copy()
        cv2.rectangle(matched_image, top_left, bottom_right, 255, 2)

        return matched_image
    
# Testing the TemplateMatching class
if __name__ == '__main__':

    # Paths to the image and template
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test02.jpg'
    template_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test02_crop.jpg'

    # Path to save the output image
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for TemplateMatching
    template_matching= TemplateMatching(image_path, template_path)

    # Apply Template Matching
    matched_image= template_matching.match_template()
    if matched_image is not None:
        cv2.imshow('Template Matching', matched_image)
        cv2.imwrite(os.path.join(output_path, 'template_matching_result.jpg'), matched_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()