# Import necessary libraries and packages
import os
import cv2

class FaceEyeDetection:
    def __init__(self, image_path, face_cascade_path, eye_cascade_path):

        # Initialize with the path to the image and the Haar cascade files
        self.image_path= image_path
        self.face_cascade_path= face_cascade_path
        self.eye_cascade_path= eye_cascade_path
        self.image= cv2.imread(self.image_path)
        self.face_cascade= cv2.CascadeClassifier(self.face_cascade_path)
        self.eye_cascade= cv2.CascadeClassifier(self.eye_cascade_path)

    def detect_faces_and_eyes(self):
        '''Detect faces and eyes in the image and draw rectangles around them'''

        if self.image is None:
            print('Error: Image not found.')
            return None
        
        # Convert the image to grayscale
        gray_image= cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces= self.face_cascade.detectMultiScale(gray_image, scaleFactor= 1.1, minNeighbors= 10, minSize= (20,20))
        print(f'Detected {len(faces)} faces.')

        # Draw rectangles around the face and detect eyes within the face region
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x,y), (x+w, y+h), (255,0,0), 2)
            roi_gray= gray_image[y: y+h, x: x+w]
            roi_color= self.image[y: y+h, x: x+w]

            # Restrict eye detection to the upper half of the face region
            roi_gray_upper= roi_gray[:h//2, :]
            roi_color_upper= roi_color[:h//2, :]

            # Detect eyes within the upper half of the face region
            eyes= self.eye_cascade.detectMultiScale(
                roi_gray_upper,
                scaleFactor= 1.1,
                minNeighbors= 5,
                minSize= (20,20),
                maxSize= (70,70)
            )
            print(f'Detected {len(eyes)} eyes in the face.')

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color_upper, (ex,ey), (ex+ew, ey+eh), (255,0,0), 2)

        return self.image

# Testing the FaceEyeDetection class
if __name__ == '__main__':

    # Paths to the image and Haar cascade files
    image_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/face.jpg'
    face_cascade_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/haarcascade_frontalface_default.xml'
    eye_cascade_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/haarcascade_eye.xml'

    # Path to save the output image
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for FaceEyeDetection
    face_eye_detector= FaceEyeDetection(image_path, face_cascade_path, eye_cascade_path)

    # Perform face and eye detection
    detected_image= face_eye_detector.detect_faces_and_eyes()
    if detected_image is not None:
        cv2.imshow('Face and Eye Detection', detected_image)
        cv2.imwrite(os.path.join(output_path, 'face_eye_detection.jpg'), detected_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
