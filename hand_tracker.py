import cv2
import mediapipe as mp
import time


class HandTracker:

    def __init__(
        self,
        mode=False,
        maxHands=1,
        detectionCon=0.7,
        trackCon=0.6
    ):

        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )

        self.mpDraw = mp.solutions.drawing_utils

        self.results = None
        
    # ======================================
    # Detect Hands
    # ======================================

    def findHands(
        self,
        img,
        draw=True
    ):

        imgRGB = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2RGB
        )

        self.results = self.hands.process(
            imgRGB
        )

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                if draw:

                    self.mpDraw.draw_landmarks(

                        img,

                        handLms,

                        self.mpHands.HAND_CONNECTIONS

                    )

        return img
    
    # ======================================
    # Landmark Positions
    # ======================================

    def findPosition(
        self,
        img,
        handNo=0,
        draw=True
    ):

        landmark_list = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[handNo]

            h, w, _ = img.shape

            for idx, landmark in enumerate(hand.landmark):

                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                landmark_list.append(

                    [idx, cx, cy]

                )

                if draw:

                    cv2.circle(

                        img,

                        (cx, cy),

                        5,

                        (255, 0, 255),

                        cv2.FILLED

                    )

        return landmark_list
    
    # ======================================
    # Finger Status
    # ======================================

    def fingersUp(
        self,
        landmark_list
    ):

        if len(landmark_list) == 0:

            return []

        tips = [

            4,

            8,

            12,

            16,

            20

        ]

        fingers = []

        # Thumb

        if landmark_list[4][1] > landmark_list[3][1]:

            fingers.append(1)

        else:

            fingers.append(0)

        # Other Fingers

        for tip in tips[1:]:

            if landmark_list[tip][2] < landmark_list[tip-2][2]:

                fingers.append(1)

            else:

                fingers.append(0)


        return fingers
    
    # ======================================
    # Distance Between Landmarks
    # ======================================

    def findDistance(
        self,
        p1,
        p2,
        landmark_list,
        img,
        draw=True
    ):

        x1, y1 = landmark_list[p1][1:]
        x2, y2 = landmark_list[p2][1:]

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        if draw:

            cv2.line(

                img,

                (x1, y1),

                (x2, y2),

                (255, 0, 255),

                2

            )

            cv2.circle(

                img,

                (x1, y1),

                6,

                (255, 0, 255),

                cv2.FILLED

            )

            cv2.circle(

                img,

                (x2, y2),

                6,

                (255, 0, 255),

                cv2.FILLED

            )

        length = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

        return length, img
    
# ======================================
# Test
# ======================================

def main():

    cap = cv2.VideoCapture(0)

    tracker = HandTracker()

    previous_time = 0

    while True:

        success, img = cap.read()

        if not success:
            break

        img = tracker.findHands(img)

        landmark_list = tracker.findPosition(img)

        current_time = time.time()

        fps = 1 / (current_time - previous_time + 1e-6)

        previous_time = current_time

        cv2.putText(

            img,

            f"FPS : {int(fps)}",

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            1,

            (0, 255, 0),

            2

        )

        cv2.imshow(

            "Hand Tracker",

            img

        )

        if cv2.waitKey(1) & 0xFF == ord("q"):

            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":

    main()