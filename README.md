# Description

This is a bot created for automizing the MMORPG game Runescape using OpenCV in Python. OpenCV is an open source computer vision library with hundreds of functions for processing and understanding images. We have used Object Detection and Mouse logic (from another library) to first detect the desired object and subsequently automize the mouse actions required. In this case the object detectection has been programmed to find an "Iron ore", the mouse logic to mine the ores and finally drop all ores once a certain threshold has been reached. In the sections below I will first give a quick explanation of the coding processes involved and finally show the application of the code:

## Processes and code logic (Not necessarily in order):


1. Match template: Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose. It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image. This was used in detecting the ores. 

2. Fast Window Capture: The goal is to capture screenshots as fast as possible and display them in an OpenCV window, so that we get a real time video stream of the game we're interested in. This will set us up to begin processing image data with OpenCV in real-time. Next step is simply to combine the Window Capture with the Match Template code.


3. HSV Color Range Thresholding: In the previous steps, we apply OpenCV's matchTemplate() to a video game in real-time. This code achieves object detection, but in many situations it was proved to be inaccurate. We can get better results by first processing our images before sending them through to the match template stage. One such method for pre-processing is Hue-Saturation-Value filtering (HSV range thresholding). We use color filtering (or range thresholding) to reduce the chance of false-positives, which in turn allows us to lower the match threshold we give match template and effectively increase accuracy of object detection. Hence, the overall script's performance is increased.


4. Real time object detection and Mouse logic: By combining all three previous steps, we can detect our object in real-time. The script gives the alternative of either a rectangle to be shown around the object or crosshair at centrepoint of the object. Once the centrepoint of the object is calculated, the mouse will move to this position and click (with the options of random mouse movement, adjustment of mouse speed etc). Keyboard- and mouse logic is finally used to drop ores once the inventory reaches a certain (adjustable) threshold. Below are examples of the script in action.

## Implementation of script with examples:


#### HSV color detection processed screenshot: 
The image below show a snap of real-time window showing the color filtering process in action (right) alongside the real client (left)
![ProcessedACC](https://user-images.githubusercontent.com/72145252/130072585-03fc2d02-fd88-4109-9e81-0772c50ed588.png)
                                          *(Colour filtering)*

#### Output image with crosshairs screenshot:
Image below show a snap of a real-time window showing the crosshairs as a result of match template (right) alongside the real client (left):
![OutputImage](https://user-images.githubusercontent.com/72145252/130072823-2dbd2840-cd63-41bc-94f2-c928528c0d5d.png)
*(Real-time object detection)*

#### Output video (real-time object detection): 
https://user-images.githubusercontent.com/72145252/130074400-da27737e-a34d-4f7e-a8da-41835848460a.mp4
*(Real-time object detection)*

#### Mining ores:
The video below show the mining process. 
https://user-images.githubusercontent.com/72145252/130077310-71b7c029-6cb8-4a08-99ee-27e1e661c5f6.mp4
*(Mining in action)*

##### Dropping ores: Below is a video of the script dropping the ores from the inventory:
https://user-images.githubusercontent.com/72145252/129974088-b1c096cf-862a-4c4a-93ca-c7762e307e2c.mp4
*(Dropping ores)*
