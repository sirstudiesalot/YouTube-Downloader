import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Function to handle the download button click
def download_video():
    try:
        url = entry_url.get()
        yt = YouTube(url)
        title = yt.title
        views = yt.views

        title_label.config(text="Title: " + title)
        views_label.config(text="Views: " + str(views))

        yd = yt.streams.get_highest_resolution()
        yd.download()

        messagebox.showinfo("Download Complete", "Video has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: " + str(e))

# Create the main application window
app = tk.Tk()
app.title("YouTube Video Downloader")

# Set the window size
app.geometry("400x300")  # Width x Height

# Create and pack labels
welcome_label = tk.Label(app, text="Hello, Welcome to Tarang's video downloader.")
welcome_label.pack()

url_label = tk.Label(app, text="Please enter the URL:")
url_label.pack()

# Create and pack an entry field for URL
entry_url = tk.Entry(app)
entry_url.pack()

# Create and pack labels to display Title and Views
title_label = tk.Label(app, text="")
title_label.pack()
views_label = tk.Label(app, text="")
views_label.pack()

# Create and pack a download button
download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack()

# Start the GUI main loop
app.mainloop()
