
import pyautogui


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





def drop_all_ores(self):

        if self.num_ores >= self.capacity:

            """Drops all ores from the player's inventory"""
            cv2.waitKey(4000)
            first_ore_x, first_ore_y = self.ores[0][0], self.ores[0][1]
            pyautogui.doubleClick(first_ore_x, first_ore_y)

            for ore_coord in self.ores:
                x_coord, y_coord = pyautogui.center(ore_coord)
                pyautogui.keyDown('shift')
                pyautogui.moveTo(x_coord, y_coord)
                pyautogui.click(x_coord, y_coord)
                pyautogui.keyUp('shift')
                self.num_ores -= 1
                print(self.num_ores)
                cv2.waitKey(400)
            self.ores = []



def ores():
        """
        Initialize the player's inventory based on its initial state represented by <image>
        :param image: The initial state of the player's inventory.
        """

        # List of all ores currently in inventory
        
        orez = [ore
                     for ore in pyautogui.locateAllOnScreen('oreimg.PNG', confidence=0.9)
                     if 765 <=  ore[0] <= 945]
        

        print(orez)


        ores = []

        find_iron =  list (pyautogui.locateAllOnScreen('oreimg.PNG', confidence=0.9))
        find_copper = list (pyautogui.locateAllOnScreen('copper.PNG', confidence=0.9))

        for ore in find_iron:
            ores.append(ore)
        for ore in find_copper:
            ores.append(ore)

        print(ores)

ores()