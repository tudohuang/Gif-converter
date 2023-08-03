from moviepy.editor import VideoFileClip
import imageio
from tkinter import filedialog
import os
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
import threading
import time


# 進度條更新函數
def progress_bar():
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.01)

def gif_to_mp4():
    try:
        gif_file = file_directory.get()
        save_path = download_directory.get()
        filename = file_name_entry.get()

        if not os.path.isfile(gif_file) or not gif_file.lower().endswith('.gif'):
            tk.messagebox.showerror("Error", "Please select a valid GIF file.")
            return

        clip = VideoFileClip(gif_file)

        mp4_output = os.path.join(save_path, filename + '.mp4')
        clip.write_videofile(mp4_output, codec='libx264', bitrate='3000k')

        status_label.config(text="Conversion completed.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred during conversion: {str(e)}")
    finally:
        conversion_button.config(text="convert", state="normal")

def mp4_to_gif():
    try:
        mp4_file = file_directory.get()
        save_path = download_directory.get()
        filename = file_name_entry.get()

        if not os.path.isfile(mp4_file) or not mp4_file.lower().endswith('.mp4'):
            tk.messagebox.showerror("Error", "Please select a valid MP4 file.")
            return

        clip = VideoFileClip(mp4_file)

        if clip.duration > 180:
            tk.messagebox.showerror("Error", "The MP4 file duration should not exceed 3 minutes.")
            return

        video = imageio.get_reader(mp4_file)
        fps = video.get_meta_data()['fps']
        gif_output = os.path.join(save_path, filename + '.gif')
        gif_writer = imageio.get_writer(gif_output, mode='I', fps=fps)

        for frame in video:
            gif_writer.append_data(frame)

        gif_writer.close()
        status_label.config(text="Conversion completed.")
    except Exception as e:
        tk.messagebox.showerror("Error", f"An error occurred during conversion: {str(e)}")
    finally:
        conversion_button.config(text="convert", state="normal")

def set_download_directory():
    # 讓使用者選擇下載目錄
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        download_directory.set(selected_directory)

def set_file_directory():
    # 讓使用者選擇要轉換的檔案
    selected_file = filedialog.askopenfilename()
    if selected_file:
        file_directory.set(selected_file)

def start_conversion():
    save_path = download_directory.get()
    filename = file_name_entry.get()
    conversion_button.config(text="converting...", state="disabled")

    if not filename:
        status_label.config(text="Please enter a file name.")
        conversion_button.config(text="convert", state="normal")
        return

    selected_quality = quality_var.get()
    if selected_quality == "MP4->GIF":
        threading.Thread(target=mp4_to_gif).start()
        threading.Thread(target=progress_bar).start()
    else:
        threading.Thread(target=gif_to_mp4).start()
        threading.Thread(target=progress_bar).start()

root = ThemedTk(theme="classic")
root.title("File Converter")
root.geometry("700x500")
root.configure(bg="#F9FBE7")

title_label = ttk.Label(root, text="File Converter", font=("Helvetica", 32, "bold"), background="#F9FBE7", foreground="#008C95")
title_label.pack(pady=10)

file_name_label = ttk.Label(root, text="Please enter custom file name:", font=("Arial", 16), background="#F9FBE7")
file_name_label.pack(pady=5)
file_name_entry = ttk.Entry(root, width=60, font=("Arial", 16))
file_name_entry.pack(pady=5)

quality_options = ["MP4->GIF", "GIF->MP4"]
quality_var = tk.StringVar()
quality_menu = ttk.Combobox(root, textvariable=quality_var, values=quality_options)
quality_var.set(quality_options[0])
quality_menu.pack()

conversion_button = ttk.Button(root, text="Convert", command=start_conversion)
conversion_button.pack(pady=10)

download_directory = tk.StringVar()
download_directory.set(os.getcwd())  # 將下載目錄設為當前工作目錄
set_directory_button = ttk.Button(root, text="Browse save path", command=set_download_directory)
set_directory_button.pack()

file_directory = tk.StringVar()
file_directory.set(os.getcwd())  # 將下載目錄設為當前工作目錄
file_directory_button = ttk.Button(root, text="Browse for file(you want to convert)", command=set_file_directory)
file_directory_button.pack()


status_label = ttk.Label(root, background="#F9FBE7")
status_label.pack(pady=10)

progress = ttk.Progressbar(root, orient = 'horizontal', length = 100, mode = 'determinate')
progress.pack(pady=10)

root.mainloop()
