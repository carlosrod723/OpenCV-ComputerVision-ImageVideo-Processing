# Import necessary libraries and packages
import cv2
import os

class ReadWriteDisplay:
    def __init__(self, image_path):
        self.image_path= image_path

    def read_image(self):
        '''Read an image in color and grayscale'''
        
        # Read the image in color
        image= cv2.imread(self.image_path)
        if image is None:
            print('Error: Image not found.')
            return None
        
        print(f'Image shape (Color): {image.shape}')

        # Read the image in grayscale
        grayscale_image= cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        print(f'Image shape (Grayscale): {grayscale_image.shape}')

        return image, grayscale_image
    
    def write_image(self, output_path):
        '''Write the image to a specified output path'''

        image= cv2.imread(self.image_path)
        if image is None:
            print('Error: Image not found.')
            return
        
        # Create the output directory
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Construct the full path for the output image
        output_file_path= os.path.join(output_path, 'output_image.jpg')

        # Writing the image to the output path
        success= cv2.imwrite(output_file_path, image)

        if success:
            print(f'Image successfully saved to {output_file_path}')
        else:
            print('Error: Image could not be saved.')

    def show_image(self):
        '''Display the image in a window'''

        image= cv2.imread(self.image_path)
        if image is None:
            print('Error: Image not found.')
            return
        
        cv2.imshow('Display image', image)
        cv2.waitKey()
        cv2.destroyAllWindows()

# Testing the ReadWriteDisplay class
if __name__ == '__main__':
    print('Starting the image processing script...')

    # Path to the image
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test.jpg'
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'
    
    # Create an object of ReadWriteDisplay
    rw_display= ReadWriteDisplay(image_path)
    print('Reading and displaying the image...')

    # Read and display the image
    rw_display.read_image()
    rw_display.show_image()
    print('Writing the image to the output path...')

    # Write the image to a file
    rw_display.write_image(output_path)
    print('Image processing script completed.')