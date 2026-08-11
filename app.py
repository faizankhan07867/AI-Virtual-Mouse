import os
import streamlit as st
import pandas as pd

from config import *

# ======================================
# Streamlit Configuration
# ======================================

st.set_page_config(

    page_title="AI Virtual Mouse",

    page_icon="🖱️",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ======================================
# Custom CSS
# ======================================

st.markdown("""

<style>

.main{

background:#F5F7FA;

}

h1{

color:#1565C0;

}

.stButton>button{

width:100%;

background:#1565C0;

color:white;

border-radius:10px;

font-size:16px;

}

</style>

""", unsafe_allow_html=True)

# ======================================
# Sidebar
# ======================================

st.sidebar.title(

    "🖱️ AI Virtual Mouse"

)

page = st.sidebar.radio(

    "Navigation",

    [

        "Home",

        "Gesture Guide",

        "Screenshots",

        "Settings",

        "About"

    ]

)

# ======================================
# Home Page
# ======================================

if page == "Home":

    st.title(

        "🖱️ AI Virtual Mouse"

    )

    st.success(

        "Real-Time Hand Gesture Controlled Virtual Mouse"

    )

    st.markdown("""

### Features

- 🖱️ Cursor Control
- 👆 Left Click
- ✌️ Right Click
- ✊ Drag & Drop
- 📸 Screenshot Gesture
- 🔊 Volume Gesture
- 📊 FPS Counter
- 🎥 Real-Time Webcam Tracking

""")
    
    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Camera",

            "Ready"

        )

    with col2:

        st.metric(

            "Tracking",

            "MediaPipe"

        )

    with col3:

        st.metric(

            "Resolution",

            f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}"

        )
        
    st.info("""

To start the AI Virtual Mouse run:

python virtual_mouse.py

Press **Q** or **ESC**
to exit the application.

""")
    
# ======================================
# Gesture Guide
# ======================================

elif page == "Gesture Guide":

    st.title("🎮 Gesture Guide")

    gesture_df = pd.DataFrame({

        "Gesture":[

            "☝️ Index Finger",

            "🤏 Thumb + Index",

            "✌️ Index + Middle",

            "✊ Closed Fist",

            "🤟 Thumb + Pinky",

            "✋ Open Palm",

            "🤏 Pinch"

        ],

        "Action":[

            "Move Cursor",

            "Left Click",

            "Right Click",

            "Drag & Drop",

            "Take Screenshot",

            "Pause Mouse",

            "Volume Control"

        ]

    })

    st.dataframe(

        gesture_df,

        use_container_width=True,

        hide_index=True

    )
    st.subheader("🖱️ Gesture Reference")

    for _, row in gesture_df.iterrows():

        st.info(

            f"**{row['Gesture']}** → {row['Action']}"

        )
        
    st.subheader("📌 Best Usage Tips")

    st.success("""

• Use a plain background.

• Ensure good lighting.

• Keep one hand visible.

• Maintain 40–70 cm distance from camera.

• Avoid fast hand movements.

• Use HD webcam for best tracking.

""")
    
    st.subheader("📷 Recommended Camera Settings")

    camera_df = pd.DataFrame({

        "Setting":[

            "Resolution",

            "FPS",

            "Camera Position",

            "Lighting"

        ],

        "Recommended":[

            "1280 × 720",

            "30 FPS",

            "Eye Level",

            "Bright Room"

        ]

    })

    st.table(

        camera_df

    )
    st.subheader("💻 System Requirements")

    requirement_df = pd.DataFrame({

        "Component":[

            "Python",

            "RAM",

            "Webcam",

            "Operating System"

        ],

        "Requirement":[

            "3.10+",

            "4 GB or Higher",

            "720p USB/Integrated",

            "Windows 10/11"

        ]

    })

    st.table(

        requirement_df

    )
    
    st.warning("""

If gesture detection is unstable:

• Clean your webcam lens.

• Increase room lighting.

• Keep only one hand in front of the camera.

• Restart the application if camera freezes.

""")
    
# ======================================
# Screenshot Gallery
# ======================================

elif page == "Screenshots":

    st.title("📸 Screenshot Gallery")

    image_files = [

        file for file in os.listdir(

            SCREENSHOT_DIR

        )

        if file.lower().endswith(

            (".png", ".jpg", ".jpeg")

        )

    ]

    if len(image_files) == 0:

        st.warning(

            "No screenshots available."

        )

    else:

        st.success(

            f"{len(image_files)} Screenshot(s) Found"

        )
        
        st.subheader("🖼 Screenshot Preview")

        columns = st.columns(3)

        for index, image_name in enumerate(image_files):

            image_path = os.path.join(

                SCREENSHOT_DIR,

                image_name

            )

            with columns[index % 3]:

                st.image(

                    image_path,

                    caption=image_name,

                    use_container_width=True

                )
                
        st.subheader("🗑 Delete Screenshot")

        selected = st.selectbox(

            "Select Screenshot",

            image_files

        )

        if st.button(

            "Delete Selected Screenshot"

        ):

            os.remove(

                os.path.join(

                    SCREENSHOT_DIR,

                    selected

                )

            )

            st.success(

                "Screenshot Deleted Successfully"

            )

            st.rerun()
            
        st.subheader("📊 Screenshot Statistics")

        total_size = sum(

            os.path.getsize(

                os.path.join(

                    SCREENSHOT_DIR,

                    image

                )

            )

            for image in image_files

        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Total Images",

                len(image_files)

            )

        with col2:

            st.metric(

                "Storage Used",

                f"{total_size/1024:.2f} KB"

            )
            
# ======================================
# Settings
# ======================================

elif page == "Settings":

    st.title("⚙️ Virtual Mouse Settings")

    st.subheader("🖥 Current Configuration")

    config_df = pd.DataFrame({

        "Parameter":[

            "Camera ID",

            "Resolution",

            "FPS",

            "Screen Width",

            "Screen Height",

            "Smoothening",

            "Click Distance"

        ],

        "Value":[

            CAMERA_ID,

            f"{FRAME_WIDTH} x {FRAME_HEIGHT}",

            FPS,

            SCREEN_WIDTH,

            SCREEN_HEIGHT,

            SMOOTHENING,

            CLICK_DISTANCE

        ]

    })

    st.table(

        config_df

    )
    
    st.subheader("🎨 Gesture Thresholds")

    threshold_df = pd.DataFrame({

        "Setting":[

            "Click Distance",

            "Right Click Distance",

            "Pinch Threshold",

            "Drag Distance"

        ],

        "Value":[

            CLICK_DISTANCE,

            RIGHT_CLICK_DISTANCE,

            PINCH_THRESHOLD,

            DRAG_DISTANCE

        ]

    })

    st.table(

        threshold_df

    )
    
    st.info("""

These values are loaded from **config.py**.

To customize gesture sensitivity:

• Edit config.py

• Save the file

• Restart virtual_mouse.py

""")
# ======================================
# About Page
# ======================================

elif page == "About":

    st.title("🖱️ About AI Virtual Mouse")

    st.markdown("""

## 🖱️ AI Virtual Mouse using Computer Vision

AI Virtual Mouse allows users to control the mouse pointer
using real-time hand gestures without touching a physical mouse.

### Features

✅ Cursor Movement

✅ Left Click

✅ Right Click

✅ Drag & Drop

✅ Screenshot Capture

✅ Gesture Recognition

✅ Real-Time Hand Tracking

✅ Streamlit Dashboard

""")
    
st.divider()

st.subheader("🏗️ Project Architecture")

architecture = pd.DataFrame({

    "Module":[

        "Hand Tracking",

        "Gesture Recognition",

        "Mouse Controller",

        "Utilities",

        "Dashboard"

    ],

    "Technology":[

        "MediaPipe",

        "Custom Gesture Engine",

        "PyAutoGUI",

        "OpenCV",

        "Streamlit"

    ]

})

st.table(architecture)
st.divider()

st.subheader("🛠 Technology Stack")

tech_df = pd.DataFrame({

    "Technology":[

        "Python",

        "OpenCV",

        "MediaPipe",

        "PyAutoGUI",

        "NumPy",

        "Streamlit"

    ],

    "Purpose":[

        "Programming",

        "Computer Vision",

        "Hand Tracking",

        "Mouse Automation",

        "Numerical Operations",

        "Dashboard"

    ]

})

st.table(tech_df)

st.divider()

st.subheader("🎮 Supported Gestures")

gesture_table = pd.DataFrame({

    "Gesture":[

        "☝️ Index Finger",

        "🤏 Thumb + Index",

        "✌️ Index + Middle",

        "✊ Closed Fist",

        "🤟 Thumb + Pinky",

        "✋ Open Palm"

    ],

    "Action":[

        "Move Cursor",

        "Left Click",

        "Right Click",

        "Drag & Drop",

        "Screenshot",

        "Pause"

    ]

})

st.table(gesture_table)


st.divider()

st.subheader("🚀 Future Improvements")

st.success("""

• Multi-Hand Support

• Brightness Control

• Air Drawing

• Media Controller

• Browser Gesture Control

• AI Gesture Learning

• Custom Gesture Training

• Voice + Gesture Hybrid Control

• Cross Platform Support

""")

st.divider()

st.subheader("👨‍💻 Developer")

st.info("""

Name : Faizan Khan

Project :
AI Virtual Mouse

Technology Stack

• Python

• OpenCV

• MediaPipe

• PyAutoGUI

• NumPy

• Streamlit

Academic Project

B.Tech Information Technology

""")

# ======================================
# Footer
# ======================================

st.divider()

st.markdown("""

<div style="text-align:center;
padding:15px;
font-size:18px;">

🖱️ AI Virtual Mouse

Made with ❤️ using Python, OpenCV & MediaPipe

© 2026 Faizan Khan

</div>

""", unsafe_allow_html=True)