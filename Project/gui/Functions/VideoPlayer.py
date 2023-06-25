import tkinter as tk
import tkinter.ttk as ttk
import cv2
from PIL import Image, ImageTk


class VideoPlayer:
    def __init__(self, videoPath, frameRate, width, height,root,x,y):
        self.videoPath = videoPath
        self.frameRate = frameRate
        self.width = width
        self.height = height
        self.root=root
        self.x=x
        self.y=y

        self.video_label = ttk.Label(self.root)
        self.video_label.place(x=self.x,y=self.y)

        self.cap = cv2.VideoCapture(self.videoPath)
        self.update_video()

        # self.root.mainloop()

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = self.resize_frame(frame)  # Resize the frame
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=image)
            self.video_label.configure(image=photo)
            self.video_label.image = photo
            self.video_label.after(self.frameRate, self.update_video)
        else:
            self.replay_video()  # Call the replay function at the end of the videos

    def replay_video(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Reset the videos to the beginning
        self.update_video()

    def resize_frame(self, frame):
        return cv2.resize(frame, (self.width, self.height))


# Usage Example

# root1 = tk.Tk()
# root1.title("Video Player demo")
# root1.geometry('600x600')
#
# video_player = VideoPlayer("video.mp4", 25, 500, 500,root1,0,0)
# video_player.update_video()
#
# root1.mainloop()
#

