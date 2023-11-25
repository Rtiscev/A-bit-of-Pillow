import cv2
from PIL import Image

window_name = "window"
# cv2.namedWindow("window", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
  
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

# vc.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
# vc.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
# check, frame = vc.read()
# frame = cv2.resize(frame, (1200, 1000))
# color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

# pilIMG = Image.fromarray(color_converted)
# pilIMG.show()

# while True:
#     rval, frame = vc.read()
#     print(type(frame))
#     newFr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("preview", newFr)

#     key = cv2.waitKey(20)
#     if key == 27:  # exit on ESC
#         break

# vc.release()
# cv2.destroyWindow("preview")
