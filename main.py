import numpy as np
import cv2
import time
import tkinter as tk


from PIL import ImageGrab, Image
from sklearn.metrics import jaccard_score
from pygame._sdl2 import get_num_audio_devices, get_audio_device_name #Get playback device names
from pygame import mixer #Playing sound
from tkinter import filedialog


# GLOBAL VARIABLES
device_name = 'CABLE Input (VB-Audio Virtual Cable)' # device name, DO NOT MESS WITH!!!!


# gui popup handling
def submit_values():
    res_h.set(entry_res_h.get())
    res_w.set(entry_res_w.get())
    file_url.set(entry_file_url.get())    
    root.destroy()  # Close the GUI window
    
    # You can perform any further operations with res_h, res_w, and file_path here
    # For example, print them to the console
    #print("res_h:", res_h)
    #print("res_w:", res_w)
    #print("File Path:", file_path)

def browse_file():
    file_url = filedialog.askopenfilename()
    entry_file_url.delete(0, tk.END)
    entry_file_url.insert(tk.END, file_url)

root = tk.Tk()

# ur screens resolution
res_w = tk.IntVar()
res_h = tk.IntVar()
file_url = tk.StringVar()

root.title("Variable Input")

# Create the labels and entry fields for res_h, res_w, and file_path
label_res_w = tk.Label(root, text="Enter Resolution width:")
label_res_w.pack()

entry_res_w = tk.Entry(root)
entry_res_w.pack()

label_res_h = tk.Label(root, text="Enter Resolution height:")
label_res_h.pack()

entry_res_h = tk.Entry(root)
entry_res_h.pack()

label_file_url = tk.Label(root, text="Select Sound File:")
label_file_url.pack()

entry_file_url = tk.Entry(root)
entry_file_url.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_values)
submit_button.pack()

root.mainloop()

# VIEWBOX COMMANDS, these are special numbers to find where death text is displayed DO NOT MESS WITH!!!
left = res_w.get() * .44921875
upper = res_h.get() * .5555555556
right = res_w.get() * .546875
lower = res_h.get() * .6597222222

# PRINTS INFO
print('\033[31mJamoos BattleBit death script is currently running\033[0m\n\n')

print('\033[92mConfigured Resolution:\033[0m {}x{}' .format(res_w.get(), res_h.get()))
print('\033[92mRunning on:\033[0m {}' .format(device_name))
print('\033[92mPlaying sound:\033[0m {}' .format(file_url.get()))


mixer.init() #Initialize the mixer, this will allow the next command to work
[get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))] #Returns playback devices
mixer.quit() #Quit the mixer as it's initialized on your main playback device


# https://chayanvinayak.blogspot.com/2013/03/bounding-box-in-pilpython-image-library.html
def capture_images(): # grabs two images and saves them to local directory to be compared, spaced out 15 ms. used to detect death and drastic changes
    cap = ImageGrab.grab(bbox =(left, upper, right, lower))
    cap.save('test_image1.png')

    time.sleep(15) # wait 15 ms

    cap2 = ImageGrab.grab(bbox =(left, upper, right, lower))
    cap2.save('test_image2.png')

# https://12ft.io/proxy?q=https%3A%2F%2Fpub.towardsai.net%2Fhow-to-detect-image-differences-with-python-9ea04859084c
def compare_images(): # compares the two previously captured images and rates their array versions on similarities
    img1 = cv2.imread(r'test_image1.png')
    img2 = cv2.imread(r'test_image2.png')

    img1ravel = img1.ravel()
    img2ravel= img2.ravel()


    jac = jaccard_score(img1ravel, img2ravel, average=None) # similarity

    mean = np.mean(jac) # means the jac array
    
    return mean # returns mean of the two captured pictures

while True:
    capture_images()
    if(compare_images() < .01): # if the images are less than x% identical play noise
        mixer.init(devicename=device_name) #Initialize it with the correct device
        mixer.music.load(file_url.get()) #Load the mp3
        mixer.music.play() #Play it
        while mixer.music.get_busy():
            pass
        mixer.quit()
        time.sleep(20000) # waits 20 seconds