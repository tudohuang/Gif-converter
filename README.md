# File Converter Application

This is a GUI application that enables conversion between MP4 video files and GIF files. The application is built with Python and utilizes libraries such as tkinter for the GUI, moviepy for handling video files, and imageio for handling GIFs.

## Features
- MP4 to GIF conversion
- GIF to MP4 conversion
- Progress bar to visualize the conversion process
- User-friendly GUI
- Ability to select a custom save path for the converted files

## How to use
1. Start the application by running the script.
2. Enter a custom name for the converted file in the provided text box.
3. Select the conversion type from the drop-down menu ("MP4->GIF" or "GIF->MP4").
4. Click the "Browse for file(you want to convert)" button to select the file you want to convert.
5. Click the "Browse save path" button to select the directory where the converted file should be saved.
6. Click the "Convert" button to start the conversion. The progress bar below will show the progress of the conversion.

## Installation
Make sure you have Python installed on your machine. If not, download and install Python from the official website. 

Next, install the required Python libraries with pip:

```
pip install moviepy imageio tkinter ttkthemes configparser threading
```

You also need to have FFMPEG installed on your system as it's a dependency for moviepy. You can download it from the official FFMPEG website.

## Configuration
The application reads from a configuration file (`settings.ini`) to get the default download directory. You can modify this file to change the default directory.

## Contributions
Contributions are always welcome. Please open a new issue if you find a bug or have suggestions for improvements.

## License
This project is licensed under the MIT license. 
