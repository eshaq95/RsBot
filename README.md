# Runescape Mining Bot with Computer Vision

## Description

This project implements an advanced bot for automating mining tasks in the MMORPG Runescape, utilizing computer vision techniques with OpenCV in Python. The bot uses object detection and mouse automation to identify iron ores, mine them, and manage the player's inventory efficiently.

## Key Features

- Real-time object detection for iron ores
- Automated mining and inventory management
- HSV color filtering for improved accuracy
- Fast window capture for real-time processing
- Inventory tracking and ore dropping

## Technologies Used

- Python
- OpenCV for computer vision
- PyAutoGUI for mouse and keyboard control
- NumPy for numerical operations
- Win32GUI for window management

## Project Structure

- `main.py`: The entry point and main loop of the bot
- `Inventory.py`: Manages the player's inventory state
- `vision.py`: Implements computer vision functionality
- `windowcapture.py`: Handles capturing screenshots of the game window
- `dropping.py`: Contains functions for dropping ores from the inventory
- `hsvfilter.py`: Defines the HSV filter data structure
- `settings.json`: Configuration file for Python environment

## Key Processes and Code Logic

1. **Match Template**: Uses OpenCV's `cv.matchTemplate()` for searching and finding ore locations.
2. **Fast Window Capture**: Captures real-time screenshots of the game window for processing.
3. **HSV Color Range Thresholding**: Pre-processes images to improve object detection accuracy.
4. **Real-time Object Detection**: Combines previous steps for accurate ore detection.
5. **Mouse and Keyboard Automation**: Uses PyAutoGUI to control in-game actions.

## Implementation Highlights

### HSV Color Detection
![ProcessedACC](https://user-images.githubusercontent.com/72145252/130072585-03fc2d02-fd88-4109-9e81-0772c50ed588.png)
*Color filtering process*

### Output Image with Crosshairs
![OutputImage](https://user-images.githubusercontent.com/72145252/130072823-2dbd2840-cd63-41bc-94f2-c928528c0d5d.png)
*Real-time object detection*

### Mining Ores
[Mining Demo Video](https://user-images.githubusercontent.com/72145252/130077310-71b7c029-6cb8-4a08-99ee-27e1e661c5f6.mp4)

### Dropping Ores
[Ore Dropping Demo](https://user-images.githubusercontent.com/72145252/129974088-b1c096cf-862a-4c4a-93ca-c7762e307e2c.mp4)

## Setup and Usage

1. Ensure you have Python installed (path specified in `settings.json`)
2. Install required libraries: `opencv-python`, `pyautogui`, `numpy`, `win32gui`
3. Run `main.py` to start the bot

## Disclaimer

This bot is for educational purposes only. Using bots in online games may violate terms of service and result in account bans. Use at your own risk.

## Contributing

Contributions to improve the bot or add new features are welcome. Please feel free to fork the repository and submit pull requests.

