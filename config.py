import os
from screeninfo import get_monitors

# ======================================
# Base Directory
# ======================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

# ======================================
# Assets
# ======================================

ASSETS_DIR = os.path.join(
    BASE_DIR,
    "assets"
)

SCREENSHOT_DIR = os.path.join(
    BASE_DIR,
    "screenshots"
)

# ======================================
# Create Directories
# ======================================

os.makedirs(
    ASSETS_DIR,
    exist_ok=True
)

os.makedirs(
    SCREENSHOT_DIR,
    exist_ok=True
)

# ======================================
# Camera Configuration
# ======================================

CAMERA_ID = 0

FRAME_WIDTH = 1280

FRAME_HEIGHT = 720

FPS = 30

# ======================================
# Screen Resolution
# ======================================

monitor = get_monitors()[0]

SCREEN_WIDTH = monitor.width

SCREEN_HEIGHT = monitor.height

# ======================================
# Mouse Settings
# ======================================

SMOOTHENING = 7

CLICK_DISTANCE = 35

RIGHT_CLICK_DISTANCE = 45

DRAG_DISTANCE = 30

SCROLL_DISTANCE = 25

# ======================================
# Gesture Thresholds
# ======================================

PINCH_THRESHOLD = 30

OPEN_PALM_THRESHOLD = 120

FIST_THRESHOLD = 50

# ======================================
# Volume Control
# ======================================

VOLUME_STEP = 2

# ======================================
# Drawing Mode
# ======================================

DRAW_COLOR = (0, 255, 0)

DRAW_THICKNESS = 5

# ======================================
# Landmark IDs
# ======================================

THUMB_TIP = 4

INDEX_TIP = 8

MIDDLE_TIP = 12

RING_TIP = 16

PINKY_TIP = 20

INDEX_MCP = 5

WRIST = 0

# ======================================
# Colors
# ======================================

GREEN = (0, 255, 0)

RED = (0, 0, 255)

BLUE = (255, 0, 0)

YELLOW = (0, 255, 255)

WHITE = (255, 255, 255)

# ======================================
# Fonts
# ======================================

FONT_SCALE = 0.8

FONT_THICKNESS = 2

# ======================================
# Screenshot Settings
# ======================================

SCREENSHOT_PREFIX = "screenshot"

SCREENSHOT_FORMAT = ".png"

# ======================================
# Configuration Summary
# ======================================

print("=" * 60)

print("AI Virtual Mouse Configuration")

print("=" * 60)

print("Resolution :", SCREEN_WIDTH, "x", SCREEN_HEIGHT)

print("Camera :", CAMERA_ID)

print("FPS :", FPS)

print("Screenshot Folder :", SCREENSHOT_DIR)

print("=" * 60)