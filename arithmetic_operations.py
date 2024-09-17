# Import necessary libraries and packages
import os
import cv2

class ArithmeticOperations:
    def __init__(self, image_path_1, image_path_2):

        # Initialize with paths to the two images
        self.image_path_1= image_path_1
        self.image_path_2= image_path_2
        self.image1= cv2.imread(self.image_path_1)
        self.image2= cv2.imread(self.image_path_2)

    def add_images(self):
        '''Add two images'''

        if self.image1 is None or self.image2 is None:
            print('Error: One or both images not found.')
            return None
        
        # Adding images
        added_image= cv2.add(self.image1, self.image2)
        return added_image
    
    def subtract_images(self):
        '''Subtract one image from another'''

        if self.image1 is None or self.image2 is None:
            print('Error: One or both images not found')
            return None
        
        # Subtracting images
        subtracted_image= cv2.subtract(self.image1, self.image2)
        return subtracted_image
    
    def blend_images(self, alpha= 0.5, beta= 0.5, gamma= 0):
        '''Blend two images with given weights'''

        if self.image1 is None or self.image2 is None:
            print('Error: One or both images not found')
            return None
        
        # Blending images
        blended_image= cv2.addWeighted(self.image1, alpha, self.image2, beta, gamma)
        return blended_image
    
# Testing the ArithmeticOperations
if __name__== '__main__':

    # Paths to the two images
    image_path_1= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/modular_code_2/output/data/frame3229.jpg'
    image_path_2= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/modular_code_2/output/data/frame3484.jpg'

    # Path to save the output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for ArithmeticOperations
    arith_ops= ArithmeticOperations(image_path_1, image_path_2)

    # Verify if images are loaded
    if arith_ops.image1 is None or arith_ops.image2 is None:
        print('Error: One or both images could not be loaded.')
    else:
        print('Images loaded successfully.')
        print(f'Image 1 Shape: {arith_ops.image1.shape}')
        print(f'Image 2 Shape: {arith_ops.image2.shape}')

    # Check if the images are the same size
    if arith_ops.image1.shape == arith_ops.image2.shape: 
        print(f'Images are the same size: {arith_ops.image1.shape}')

        # Perform addition
        added_image= arith_ops.add_images()
        if added_image is not None:
            cv2.imshow('Added Image', added_image)
            cv2.imwrite(os.path.join(output_path, 'added_image.jpg'), added_image)
            cv2.waitKey(0)

        # Perform subtraction
        subtracted_image= arith_ops.subtract_images()
        if subtracted_image is not None:
            cv2.imshow('Subtracted Image', subtracted_image)
            cv2.imwrite(os.path.join(output_path, 'subtracted_image.jpg'), subtracted_image)
            cv2.waitKey(0)

        # Perform blending
        blended_image= arith_ops.blend_images(alpha= 0.7, beta= 0.3)
        if blended_image is not None:
            cv2.imshow('Blended Image', blended_image)
            cv2.imwrite(os.path.join(output_path, 'blended_image.jpg'), blended_image)
            cv2.waitKey(0)

        cv2.destroyAllWindows()
    else:
        print(f'Images are different sizes: {arith_ops.image1.shape} and {arith_ops.image2.shape}')