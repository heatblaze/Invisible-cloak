import cv2
import numpy as np
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)
time.sleep(2)  # Allow the camera to warm up

# Capture the background
print("Capturing background. Please remove any objects or yourself from the frame.")
for i in range(30):
    ret, background = cap.read()

# Flip the background for consistency
background = np.flip(background, axis=1)

print("Background captured. You can now wear the cloak.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame for consistency
    frame = np.flip(frame, axis=1)

    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for the cloak (e.g., red color)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combine masks
    mask = mask1 + mask2

    # Refine the mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Inverse mask
    mask_inverse = cv2.bitwise_not(mask)

    # Segment out the cloak from the frame
    res1 = cv2.bitwise_and(background, background, mask=mask)

    # Segment out the non-cloak area
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inverse)

    # Combine the two
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
