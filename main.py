import tkinter as tk
from tkinter import ttk
from pytube import YouTube

# function definitions

def video(url):
    """
    Creates video stream for the youtube video ready for download
    """
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    return video

def download_video():
    """Downloads the youtube video"""
    vid = video(entry.get())
    vid.download()

window = tk.Tk()
root = window

window.title("Rahaman and Lesego yt downloader")
window.configure(bg='maroon')


custom_font = ("Poppins", 24)  # Replace "Helvetica" with your desired font and 16 with the desired font size
heading = tk.Label(text="Youtube downloader", foreground="#ffffff", font=custom_font)
heading.configure(bg="maroon")
heading.pack(pady=30)

window.geometry("300x100")


style = ttk.Style()
style.configure('Padded.TEntry', padding=(0, 10))  # Adjust the vertical padding as needed

entry = ttk.Entry(root, style='Padded.TEntry', width=50)
entry.pack()

button = tk.Button(text = "Download video", fg="#000000", command=download_video)
button.configure(bg="#ffffff")
button.pack(pady=30)

window.mainloop()