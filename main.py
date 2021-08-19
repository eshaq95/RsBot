import numpy as np
from PIL import ImageGrab
import cv2
from Inventory import Inventory
import pyautogui
from hsvfilter import HsvFilter
from vision import Vision
from windowcapture import WindowCapture
import time
from threading import Thread

# Timing how long the Bot lapses.

def time_convert(sec):
                mins = sec // 60
                sec = sec % 60
                hours = mins // 60
                mins = mins % 60
                print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),int(sec)))


start_time = time.time()



# Getting relevant window
wincap = WindowCapture('Old School Runescape')

# Using vision class to find relevant ore
vision_limestone = Vision('ore/iron.PNG')
hsv_filter = HsvFilter(5, 145, 92, 19, 176, 255, 0, 4, 90, 0)


# Threading method used to run BOT
is_bot_in_action = False

def cut_ores(gs):
            targets = vision_limestone.get_click_points(rectangles)
            target = wincap.get_screen_position(targets[2])
            if target:
                try:
                    
                    pyautogui.moveTo(target[0],target[1])
                    pyautogui.click()
                    cv2.waitKey(5000)
            
                
                except IndexError:
                    pass
        

            

            global is_bot_in_action
            is_bot_in_action = False


# Starting the bot (Main Loop)

if __name__ == "__main__":
    # Loop for Bot
    while True:
        time_lapsed = time.time() - start_time
        time_convert(time_lapsed)
        
        #Grab inventory image
        inv_img = np.array(ImageGrab.grab((767, 779, 943, 1030)))
        
        # Initialize inventory
        the_inventory = Inventory(inv_img)
        
        #Update contents of inventory based on current status of Inventory(image)
        the_inventory.update()
        the_inventory.drop_all_ores()
        
        #the_inventory.banking() ---- BANKING OPTIONS

        # Grab game screen image
        screenshot = wincap.get_screenshot()
        processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)

        # Do object detection
        rectangles = vision_limestone.find(processed_image, 0.6)
        points = vision_limestone.get_click_points(rectangles)
        output_image = vision_limestone.draw_crosshairs(screenshot, points)
        # Output_image = vision_limestone.draw_rectangles(screenshot, rectangles) -- Draws rectangles around ores instead of crosshairs
        cv2.imshow('Processed', output_image)

        
        #print('There are now {logs} logs in the inventory!'.format(logs = the_inventory.num_ores)) -- Alternative to showcase how many logs there are in the inventory

        if not is_bot_in_action:
            is_bot_in_action = True
            t = Thread(target=cut_ores, args=(rectangles,))
            t.start()
        

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
        
        
        