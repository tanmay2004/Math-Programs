import cv2 # Included in opencv-python library

# Gets the middle frame of any given video and puts it in a predefined folder with a given name (.jpg format)
def create_frame(video_title, img_name):

  # Read the video from specified path
  cam = cv2.VideoCapture("C:\\Users\\Admin\\Videos\\" + video_title)
  
  total_frames = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
  cam.set(1, total_frames/2) # Set the midpoint frame
  
  name = "C:/Users/Admin/Videos/" + img_name + ".jpg"
  
  # reading from frame
  ret, frame = cam.read()
  
  # writing the extracted image
  cv2.imwrite(name, frame)

  # Release all space and windows once done
  cam.release()
  cv2.destroyAllWindows()

create_frame("name_of_video.mp4", "output_mid_frame") # format of calling the function

# Helped by https://www.geeksforgeeks.org/extract-images-from-video-in-python/
# Other ways to extract frames from a video: https://www.raymond.cc/blog/extract-video-frames-to-images-using-vlc-media-player/
