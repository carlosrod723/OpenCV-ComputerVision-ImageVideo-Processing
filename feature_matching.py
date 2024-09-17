# Import necessary libraries and packages
import os
import cv2

class FeatureMatching:
    def __init__(self, image_path1, image_path2):

        # Initialize with the path to the images
        self.image_path1= image_path1
        self.image_path2= image_path2
        self.image1= cv2.imread(self.image_path1, cv2.IMREAD_GRAYSCALE)
        self.image2= cv2.imread(self.image_path2, cv2.IMREAD_GRAYSCALE)

    def sift_feature_matching(self):
        '''Perform SIFT feature matching'''

        if self.image1 is None or self.image2 is None:
            print('Error: One or both images not found.')
            return None
        
        # Initialize the SIFT detector
        sift= cv2.SIFT_create()

        # Detect keypoints and descriptors
        keypoints1, descriptors1= sift.detectAndCompute(self.image1, None)
        keypoints2, descriptors2= sift.detectAndCompute(self.image2, None)

        # Determine FLANN parameters
        index_params= dict(algorithm= 1, trees= 5)
        search_params= dict(checks= 50)
        flann= cv2.FlannBasedMatcher(index_params, search_params)
        matches= flann.knnMatch(descriptors1, descriptors2, k= 2)

        # Store all the good matches as per Lowe's ratio test
        good_matches= []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good_matches.append(m)

        # Draw matches
        matched_image= cv2.drawMatches(self.image1, keypoints1, self.image2, keypoints2, good_matches, None, flags= cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        return matched_image
    

    def orb_feature_matching(self):
        '''Perform ORB feature matching'''

        if self.image1 is None or self.image2 is None:
            print('Error: One or both images not found.')
            return None
        
        # Initialize the ORB detector
        orb= cv2.ORB_create()

        # Detect keypoints and descriptors
        keypoints1, descriptors1= orb.detectAndCompute(self.image1, None)
        keypoints2, descriptors2= orb.detectAndCompute(self.image2, None)

        # Use BFMatcher for ORB (since descriptors are binary)
        bf= cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck= True)
        matches= bf.match(descriptors1, descriptors2)

        # Sort them in the order of their distance
        matches= sorted(matches, key= lambda x: x.distance)

        # Draw matches
        matched_image= cv2.drawMatches(self.image1, keypoints1, self.image2, keypoints2, matches[:50], None, flags= cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        return matched_image
    
# Testing the FeatureMatching class
if __name__ == '__main__':

    # Paths to the images
    image_path1= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/early_morning.jpg'
    image_path2= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/ProjectProFiles/data_2/natural_reflection.jpg'

    # Path to save the output images
    output_path= '/Users/carlos72386/Desktop/ProjectPro/Computer_Vision_1/OpenCV-ComputerVision-ImageVideo-Processing/images'

    # Create an object for FeatureMatching
    feature_matching= FeatureMatching(image_path1, image_path2)

    # Perform SIFT feature matching
    sift_matched_image= feature_matching.sift_feature_matching()
    if sift_matched_image is not None:
        cv2.imshow('SIFT Feature Matching', sift_matched_image)
        cv2.imwrite(os.path.join(output_path, 'sift_feature_matching.jpg'), sift_matched_image)
        cv2.waitKey(0)

    # Perform ORB feature matching
    orb_matched_image= feature_matching.orb_feature_matching()
    if orb_matched_image is not None:
        cv2.imshow('ORB Feature Matching', orb_matched_image)
        cv2.imwrite(os.path.join(output_path, 'orb_feature_matching.jpg'), orb_matched_image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
