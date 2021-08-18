import cv2
import pyautogui
import win32gui, win32ui, win32con

#Class representing the state of the player's inventory.

class Inventory:

    def __init__(self, image):
        """
        Initialize the player's inventory based on its initial state represented by <image>
        :param image: The initial state of the player's inventory.
        """

        self.image = image
        # List of all ores currently in inventory
        self.ores = []
        find_iron =  list (pyautogui.locateAllOnScreen('oreimg.PNG', confidence=0.9))
        find_copper = list (pyautogui.locateAllOnScreen('copper.PNG', confidence=0.9))

        for ore in find_iron:
            self.ores.append(ore)
        for ore in find_copper:
            self.ores.append(ore)
        
        self.num_ores = len(self.ores)
        
        #print('You have have gained {xp} xp!'.format(xp = self.xp_gained))
        # Max capacity of inventory
        self.capacity = 25


    def drop_all_ores(self):

        if self.num_ores >= self.capacity:
            """Drops all ores from the player's inventory"""
            cv2.waitKey(4000)
            first_ore_x, first_ore_y = self.ores[0][0], self.ores[0][1]
            pyautogui.doubleClick(first_ore_x, first_ore_y)
        
            x_coord, y_coord = 793, 800
            pyautogui.keyDown('shift')

            # 1st column
            pyautogui.moveTo(x_coord, y_coord)
            pyautogui.click(x_coord, y_coord)

            pyautogui.moveTo(x_coord, y_coord + 35,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord, y_coord + 70,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord, y_coord + 105,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord, y_coord + 140,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord, y_coord + 175,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord, y_coord + 210,0.2)
            pyautogui.click()
           
            
            

            #2nd colum
            pyautogui.moveTo(x_coord + 42, y_coord,0.5)
            pyautogui.click()

            pyautogui.moveTo(x_coord+ 42, y_coord + 35,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 42, y_coord + 70,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 42, y_coord + 105,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 42, y_coord + 140,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 42, y_coord + 175,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 42, y_coord + 210,0.2)
            pyautogui.click()
            
            

            # 3rd column
            pyautogui.moveTo(x_coord + 84, y_coord, 0.5)
            pyautogui.click()

            
            pyautogui.moveTo(x_coord+ 84, y_coord + 35,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 84, y_coord + 70,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 84, y_coord + 105,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 84, y_coord + 140,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 84, y_coord + 175,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 84, y_coord + 210,0.2)
            pyautogui.click()
          
            #4th column
            pyautogui.moveTo(x_coord + 126, y_coord, 0.5)
            pyautogui.click()

            
            pyautogui.moveTo(x_coord+ 126, y_coord + 35,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 126, y_coord + 70,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 126, y_coord + 105,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 126, y_coord + 140,0.2)
            pyautogui.click()
            pyautogui.moveTo(x_coord+ 126, y_coord + 175,0.2)
            pyautogui.click()
           
            
            
            
            pyautogui.keyUp('shift')
            #self.num_ores -= 1
            #print(self.num_ores)
            cv2.waitKey(400)
        self.ores = []

            
        
    def banking(self):
        if self.num_ores >= self.capacity:
            cv2.waitKey(1000)
            # Initial location before going to the bank
            x1, y1, w1, h1 = pyautogui.locateOnScreen('compass.png', confidence=0.70)
            pyautogui.moveTo(x1 + 20, y1 + 10)
            pyautogui.click()
            cv2.waitKey(1000)
            x2, y2, w2, h2 = pyautogui.locateOnScreen('MiningIcon.png', confidence=0.80)
            pyautogui.moveTo(x2, y2, 1)
            pyautogui.click()
            cv2.waitKey(2000)
            # Find recorder window, open, and start mouse automatic recorder.
            hwnd = win32gui.FindWindow(None, 'Macro Recorder 2.0.69f - Macro')
            win32gui.SetForegroundWindow(hwnd)
            cv2.waitKey(4000)
            x2, y2, w2, h2 = pyautogui.locateOnScreen('MousPlayButton.png', confidence=0.90)
            pyautogui.moveTo(x2, y2, 1)
            pyautogui.click()
            cv2.waitKey(180000)
            x2, y2, w2, h2 = pyautogui.locateOnScreen('MiningIcon.png', confidence=0.80)
            pyautogui.moveTo(x2, y2, 1)
            pyautogui.click()
            cv2.waitKey(2000)


    def is_empty(self):
        """
        Returns True if the player's inventory is empty, otherwise returns false
        """
        return self.num_ores == 0

    def is_full(self):

        # Returns True if the player's inventory is full, otherwise returns false
        
        return self.num_ores >= self.capacity

    def process_inventory(self):
        
        # Outlines all ores present in inventory

        if len(self.ores) > 0:
            # ore_coord = (left, top, width, height)
            first_ore_x, first_ore_y = self.ores[0][0], self.ores[0][1]
            for ore_coord in self.ores:
            # print(ore_coord)
                x1, y1, width1, height1 = ore_coord
                cv2.rectangle(self.image,
                            (x1 - first_ore_x + 8, y1 - first_ore_y + 5),
                            (x1 - first_ore_x + width1 + 3, y1 - first_ore_y + height1),
                            (0, 255, 0), 1)
        return self.image

    def update(self):
        """ Updates the state of the inventory as items are added and removed"""
        processed_inventory = self.process_inventory()
        cv2.imshow('inventory', cv2.cvtColor(processed_inventory, cv2.COLOR_BGR2RGB))
