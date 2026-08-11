import os
import time

import pyautogui

from PIL import ImageGrab

from config import *

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


class MouseController:

    def __init__(self):

        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

        self.prev_x = 0
        self.prev_y = 0

        self.dragging = False
        
    # ======================================
    # Move Cursor
    # ======================================

    def move(

        self,

        x,

        y

    ):

        smooth_x = self.prev_x + (

            x - self.prev_x

        ) / SMOOTHENING

        smooth_y = self.prev_y + (

            y - self.prev_y

        ) / SMOOTHENING

        pyautogui.moveTo(

            smooth_x,

            smooth_y

        )

        self.prev_x = smooth_x

        self.prev_y = smooth_y
        
    # ======================================
    # Mouse Clicks
    # ======================================

    def left_click(self):

        pyautogui.click()


    def right_click(self):

        pyautogui.rightClick()


    def double_click(self):

        pyautogui.doubleClick()
        
    # ======================================
    # Drag & Drop
    # ======================================

    def drag_start(self):

        if not self.dragging:

            pyautogui.mouseDown()

            self.dragging = True


    def drag_stop(self):

        if self.dragging:

            pyautogui.mouseUp()

            self.dragging = False
            
    # ======================================
    # Scroll
    # ======================================

    def scroll_up(self):

        pyautogui.scroll(300)


    def scroll_down(self):

        pyautogui.scroll(-300)
        
    # ======================================
    # Screenshot
    # ======================================

    def screenshot(self):

        filename = (

            f"{SCREENSHOT_PREFIX}_"

            f"{int(time.time())}"

            f"{SCREENSHOT_FORMAT}"

        )

        path = os.path.join(

            SCREENSHOT_DIR,

            filename

        )

        image = ImageGrab.grab()

        image.save(path)

        return path
    
    # ======================================
    # Keyboard Shortcuts
    # ======================================

    def copy(self):

        pyautogui.hotkey(

            "ctrl",

            "c"

        )


    def paste(self):

        pyautogui.hotkey(

            "ctrl",

            "v"

        )


    def undo(self):

        pyautogui.hotkey(

            "ctrl",

            "z"
        )
        
# ======================================
# Test
# ======================================

if __name__ == "__main__":

    controller = MouseController()

    print("Mouse Controller Ready")

    print(

        "Screen Resolution :",

        controller.screen_width,

        "x",

        controller.screen_height

    )

    print(

        "Screenshot Folder :",

        SCREENSHOT_DIR

    )