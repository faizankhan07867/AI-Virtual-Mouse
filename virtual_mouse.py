import cv2

from config import *
from hand_tracker import HandTracker
from mouse_controller import MouseController
from gesture import *
from utils import *

# ======================================
# Initialize
# ======================================

cap = cv2.VideoCapture(CAMERA_ID)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

tracker = HandTracker()
mouse = MouseController()
fps = FPSCalculator()

# ======================================
# Main Loop
# ======================================

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    frame = tracker.findHands(frame)
    landmark_list = tracker.findPosition(frame, draw=False)

    status = "Waiting..."

    if len(landmark_list):
        fingers = tracker.fingersUp(landmark_list)
        gesture_name = detect_gesture(fingers, landmark_list)
        status = gesture_name

        index_x = landmark_list[INDEX_TIP][1]
        index_y = landmark_list[INDEX_TIP][2]

        screen_x, screen_y = map_coordinates(
            index_x, index_y, FRAME_WIDTH, FRAME_HEIGHT
        )
        screen_x, screen_y = clamp_coordinates(screen_x, screen_y)

        # ======================================
        # Gesture Handling
        # ======================================

        if gesture_name == "MOVE":
            mouse.move(screen_x, screen_y)

        elif gesture_name == "LEFT_CLICK":
            mouse.left_click()
            cv2.waitKey(150)

        elif gesture_name == "RIGHT_CLICK":
            mouse.right_click()
            cv2.waitKey(150)

        elif gesture_name == "DRAG":
            mouse.drag_start()

        elif gesture_name == "SCREENSHOT":
            path = mouse.screenshot()
            status = "Screenshot Saved"
            print(f"Screenshot saved: {path}")
            cv2.waitKey(300)

        else:
            mouse.drag_stop()

        # ======================================
        # Volume Control
        # ======================================

        pinch_distance = volume_control(landmark_list)

        if pinch_distance < PINCH_THRESHOLD:
            status = "Volume Gesture"
            # Volume control logic can be added here
            # Example:
            # mouse.volume_up()
            # mouse.volume_down()

        # ======================================
        # Draw Pointer
        # ======================================

        draw_crosshair(frame, index_x, index_y)

    # ======================================
    # Status & FPS
    # ======================================

    draw_status(frame, status)
    draw_fps(frame, fps.get_fps())

    # ======================================
    # Display
    # ======================================

    cv2.imshow("AI Virtual Mouse", frame)

    # ======================================
    # Exit
    # ======================================

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord("q"):
        break

# ======================================
# Cleanup
# ======================================

cap.release()
cv2.destroyAllWindows()

print()
print("=" * 60)
print("AI Virtual Mouse Closed Successfully")
print("=" * 60)