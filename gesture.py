import math

from config import *

# ======================================
# Distance Between Two Points
# ======================================

def distance(p1, p2):

    x1, y1 = p1
    x2, y2 = p2

    return math.hypot(

        x2 - x1,

        y2 - y1

    )


# ======================================
# Get Landmark Point
# ======================================

def point(

    landmark_list,

    landmark_id

):

    return (

        landmark_list[landmark_id][1],

        landmark_list[landmark_id][2]

    )
    
# ======================================
# Cursor Movement
# ======================================

def move_cursor(

    fingers

):

    return fingers == [

        0,

        1,

        0,

        0,

        0

    ]


# ======================================
# Left Click
# ======================================

def left_click(

    landmark_list

):

    thumb = point(

        landmark_list,

        THUMB_TIP

    )

    index = point(

        landmark_list,

        INDEX_TIP

    )

    return distance(

        thumb,

        index

    ) < CLICK_DISTANCE
    
# ======================================
# Right Click
# ======================================

def right_click(

    landmark_list

):

    index = point(

        landmark_list,

        INDEX_TIP

    )

    middle = point(

        landmark_list,

        MIDDLE_TIP

    )

    return distance(

        index,

        middle

    ) < RIGHT_CLICK_DISTANCE


# ======================================
# Drag Gesture
# ======================================

def drag(

    fingers

):

    return fingers == [

        0,

        0,

        0,

        0,

        0

    ]
    
# ======================================
# Screenshot Gesture
# ======================================

def screenshot(

    fingers

):

    return fingers == [

        1,

        0,

        0,

        0,

        1

    ]


# ======================================
# Open Palm
# ======================================

def open_palm(

    fingers

):

    return fingers == [

        1,

        1,

        1,

        1,

        1

    ]
    
# ======================================
# Volume Control
# ======================================

def volume_control(

    landmark_list

):

    thumb = point(

        landmark_list,

        THUMB_TIP

    )

    index = point(

        landmark_list,

        INDEX_TIP

    )

    return distance(

        thumb,

        index

    )
    
# ======================================
# Gesture Name
# ======================================

def detect_gesture(

    fingers,

    landmark_list

):

    if move_cursor(

        fingers

    ):

        return "MOVE"

    if left_click(

        landmark_list

    ):

        return "LEFT_CLICK"

    if right_click(

        landmark_list

    ):

        return "RIGHT_CLICK"

    if drag(

        fingers

    ):

        return "DRAG"

    if screenshot(

        fingers

    ):

        return "SCREENSHOT"

    if open_palm(

        fingers

    ):

        return "PAUSE"

    return "NONE"