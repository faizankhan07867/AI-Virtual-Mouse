import cv2
import math
import time

from config import *


# ======================================
# FPS Calculator
# ======================================

class FPSCalculator:

    def __init__(self):

        self.previous_time = time.time()

    def get_fps(self):

        current_time = time.time()

        fps = 1 / (current_time - self.previous_time + 1e-6)

        self.previous_time = current_time

        return int(fps)
    
# ======================================
# Distance Between Two Points
# ======================================

def distance(

    x1,

    y1,

    x2,

    y2

):

    return math.hypot(

        x2 - x1,

        y2 - y1

    )
# ======================================
# Coordinate Mapping
# ======================================

def map_coordinates(

    x,

    y,

    frame_width,

    frame_height

):

    screen_x = int(

        x * SCREEN_WIDTH / frame_width

    )

    screen_y = int(

        y * SCREEN_HEIGHT / frame_height

    )

    return screen_x, screen_y

# ======================================
# Screen Boundary
# ======================================

def clamp(

    value,

    minimum,

    maximum

):

    return max(

        minimum,

        min(

            value,

            maximum

        )

    )


def clamp_coordinates(

    x,

    y

):

    x = clamp(

        x,

        0,

        SCREEN_WIDTH - 1

    )

    y = clamp(

        y,

        0,

        SCREEN_HEIGHT - 1

    )

    return x, y

# ======================================
# Draw Text
# ======================================

def draw_text(

    image,

    text,

    x,

    y,

    color=GREEN

):

    cv2.putText(

        image,

        text,

        (x, y),

        cv2.FONT_HERSHEY_SIMPLEX,

        FONT_SCALE,

        color,

        FONT_THICKNESS

    )
    
# ======================================
# Draw Circle
# ======================================

def draw_circle(

    image,

    x,

    y,

    color=GREEN,

    radius=8

):

    cv2.circle(

        image,

        (x, y),

        radius,

        color,

        cv2.FILLED

    )
    
# ======================================
# Draw Rectangle
# ======================================

def draw_rectangle(

    image,

    start,

    end,

    color=BLUE,

    thickness=2

):

    cv2.rectangle(

        image,

        start,

        end,

        color,

        thickness

    )
    
# ======================================
# Status Banner
# ======================================

def draw_status(

    image,

    status

):

    cv2.rectangle(

        image,

        (0, 0),

        (350, 45),

        (40, 40, 40),

        -1

    )

    draw_text(

        image,

        status,

        10,

        30,

        YELLOW

    )
    
# ======================================
# Draw FPS
# ======================================

def draw_fps(

    image,

    fps

):

    draw_text(

        image,

        f"FPS : {fps}",

        10,

        65,

        GREEN

    )
    
# ======================================
# Draw Crosshair
# ======================================

def draw_crosshair(

    image,

    x,

    y,

    size=12,

    color=RED

):

    cv2.line(

        image,

        (x-size, y),

        (x+size, y),

        color,

        2

    )

    cv2.line(

        image,

        (x, y-size),

        (x, y+size),

        color,

        2
    )
# ======================================
# Test
# ======================================

if __name__ == "__main__":

    fps = FPSCalculator()

    print(

        "FPS :", fps.get_fps()

    )

    x, y = map_coordinates(

        320,

        240,

        640,

        480

    )

    print(

        "Mapped Coordinates:",

        x,

        y

    )

    print(

        "Distance:",

        distance(

            0,

            0,

            100,

            100

        )

    )