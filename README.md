# Invisible-cloak

This project implements a basic "invisibility cloak" effect using OpenCV and Python. It captures the background and uses color masking to replace the selected color (the cloak) with the background, creating an illusion of invisibility.

---

## Features

- **Detects a specific color range (red by default) and masks it.**
- **Replaces the masked color with the captured background.**
- **Real-time processing using a webcam.**
- **Implements basic image processing techniques like masking, morphological transformations, and color segmentation.**

---

## Technology Used

- **Programming Language:** Python
- **Libraries:**
1. *OpenCV:* For image and video processing
2. *NumPy:* For numerical computations

---

## Prerequisites

- **Python:** Ensure you have Python 3.6 or above installed on your system.
- **Dependencies:** Install required libraries using the command below:
    *pip install -r requirements.txt*

---

## How It Works

- **Background Capture:**
The script captures the background when no objects or the user are present in the frame.

- **Color Detection:**
Detects the specific color range of the cloak (default: red) in the HSV color space.
Two masks are created to cover the red hue ranges in the HSV space.

- **Mask Refinement:**
Morphological transformations are applied to refine the mask and reduce noise.

- **Cloak Segmentation:**
The cloak area is replaced with the background using the mask.
The non-cloak area remains as is.

- **Final Output:**
The two segments are combined to create the invisibility effect in real time.

---

## Usage

- **Clone the repository:**
git clone https://github.com/heatblaze/Invisible-cloak.git
cd Invisible-cloak

- **Run the script:**
python invisible_cloak.py

- **Instructions:**
1. Allow the camera to capture the background.
2. Wear a red cloak and ensure it is fully visible to the camera.
3. Press q to quit the application.

---

## Configuration
To change the cloak color, modify the lower_red and upper_red values in the script to the desired HSV range.

---

## Troubleshooting
- **No Background Captured:**
Ensure you remain out of the frame during the background capture phase.

- **Inconsistent Masking:**
Adjust the HSV values in the script to better detect the desired cloak color.



