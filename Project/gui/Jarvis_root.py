import tkinter as tk
import time
from PIL import ImageTk, Image
from Project.gui.Functions.Temperature import fetch_temperature
from Project.gui.Functions.VideoPlayer import VideoPlayer
from Project.gui.Functions.AudioPlayer import play_sound
from Project.gui.Functions.ListGenerator import ListGenerator
import threading
from Project.Face_Recognition.PermissionGranted import SystemFaceRecognition
from Project.gui.Root import JarvisWindow

jarvis=JarvisWindow()

class Jarvis():
    def __init__(self):
        self.root=jarvis.root
        self.image = Image.open("..\\Resources\\images\\background.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.background_label = tk.Label(self.root, image=self.photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.new_window = None
        self.game_window = None

        self.logo = Image.open("images/cot_logo.png")
        # Create a PhotoImage object from the loaded image
        resized_image = self.logo.resize((120, 120))
        self.logo_photo = ImageTk.PhotoImage(resized_image)
        image_label = tk.Label(self.root, image=self.logo_photo)
        image_label.place(x=1000,y=240)

        self.time_label = tk.Label(self.root, font=('Helvetica', 48), bg='black', fg='white')
        self.time_label.pack(padx=20, pady=20)

        self.video_label = tk.Label(self.root)
        self.video_label.pack(side='left', padx=30)

        self.temperature_label = tk.Label(self.root, font=('Helvetica', 24), bg='black', fg='white')
        self.temperature_label.pack(side='right', padx=20, pady=20)

        sound_thread = threading.Thread(target=play_sound)

        # Start the thread
        sound_thread.start()

    def on_new_window_close(self):

        print("clickeddddd")
        self.buttonDesc.place(x=800, y=600)


    def open_new_window(self):
        self.new_window = tk.Toplevel(self.root) # Create a new window
        self.new_window.title("New Window")
        self.new_window.geometry("800x600")
        self.buttonDesc.place_forget()
        self.new_window.bind("<Destroy>", lambda event: self.on_new_window_close())
        # self.labeldisplay("move Cursor",500,10)


    def open_game_window(self):
        self.game_window = tk.Toplevel(self.root)  # Create a new window
        self.game_window.title("Snakegame")
        self.game_window.geometry("800x600")
        self.GameButton.place_forget()
        self.game_window.bind("<Destroy>", lambda event: self.on_new_window_close())

    def update_time(self):
        current_time = time.strftime('%H:%M:%S')
        self.time_label.config(text=current_time)
        self.time_label.after(1000, self.update_time)

    def update_temperature(self):
        current_temp = fetch_temperature()
        print(current_temp)
        self.temperature_label.config(text=f'Temperature: {current_temp}°C')
        self.temperature_label.after(100000, self.update_temperature)

    def run_video_players(self):
        objVdo1 = VideoPlayer("..\\Resources\\videos\\video.mp4", 30, 300, 300, self.root, 10, 400)
        objVdo1.update_video()
        objVdo2 = VideoPlayer("..\\Resources\\videos\\video3.mp4", 100, 200, 200, self.root, 25, 50)
        objVdo2.update_video()
        objVdo3 = VideoPlayer("..\\Resources\\videos\\sound-wave-waves.mp4", 30, 200, 100, self.root, 1130, 470)
        objVdo3.update_video()
        objVdo3 = VideoPlayer("..\\Resources\\videos\\video4.mp4", 60, 200, 200, self.root, 1130, 100)
        objVdo3.update_video()
        objVdo3 = VideoPlayer("..\\Resources\\videos\\video5.mp4", 60, 200, 100, self.root, 1130, 600)
        objVdo3.update_video()

    def generate_list(self):
        items1 = ['Group Members', '  __  ', 'Ritik', 'Shipu', 'Vikas']
        items2 = ['Processing', '  __  ', 'Processing.....', 'Processing...........', 'Processing...............','Processing...................']
        list_generator1 = ListGenerator(self.root, width=20, height=5, x=310, y=50)
        list_generator2 = ListGenerator(self.root, width=40, height=6, x=850, y=10)
        listThread1 = threading.Thread(list_generator1.start_generation(items1))
        listThread2 = threading.Thread(list_generator2.start_generation(items2))
        listThread1.start()
        listThread2.start()

    def run_face_recognition(self):
        recognition_system = SystemFaceRecognition()
        recognition_system.run_recognition_system()

    def minimize_window(self):
        self.root.iconify()

    def run_minimise_thread(self):
        minimiseThread = threading.Thread(target=self.run_face_recognition)
        minimiseThread.start()

    def run_jarviss(self):
        self.update_time()
        self.update_temperature()
        self.run_video_players()
        self.generate_list()
        self.run_minimise_thread()
        self.root.mainloop()

# Usage example
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run_jarviss()
