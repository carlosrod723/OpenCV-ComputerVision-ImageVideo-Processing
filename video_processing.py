# Import necessary libraries and packages
import os
import cv2

class VideoProcessing:
    def __init__(self, video_path, output_path):

        # Initialize with the path to the video and output directory
        self.video_path= video_path
        self.output_path= output_path

    def process_video(self, frame_interval= 30):
        '''Process the video and save every nth frame'''

        # Open the video file
        cap= cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            print('Error: Could not open video.')
            return
        
        frame_count= 0
        saved_frame_count= 0

        # Create the output directory
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        while True:
            ret, frame= cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0:

                # Save the frame
                frame_filename = f'frame_{saved_frame_count:04d}.jpg'
                cv2.imwrite(os.path.join(self.output_path, frame_filename), frame)
                saved_frame_count += 1

            frame_count += 1

        cap.release()
        print(f'Total frames saved: {saved_frame_count}')

# Testing the VideoProcessing class
if __name__ == '__main__':

    # Path to the video
    video_path = '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/test_video.mp4'

    # Path to save the output video
    output_path = '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images/video_frames'

    # Create an object for VideoProcessing
    video_processor= VideoProcessing(video_path, output_path)

    # Process the video
    video_processor.process_video(frame_interval= 30)
