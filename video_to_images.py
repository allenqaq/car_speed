import cv2
import os


def frame_capture(input_path, output_path):
    # Path to video file
    video = cv2.VideoCapture(input_path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        success, image = video.read()

        image = cv2.imread('0.png')
        image_cropped = image[106:370, 33:561]
        image_after = cv2.resize(image_cropped, (220, 66), interpolation=cv2.INTER_AREA)

        # Saves the frames with frame-count
        cv2.imwrite(os.path.join(output_path, '%d.png') % count, image_after)
        count += 1


if __name__ == '__main__':

    # Calling the function
    print "start----"
    frame_capture("train.mp4", "train_images")
    print "part1--done"
    frame_capture("test.mp4", "test_images")
    print "part2--done"
