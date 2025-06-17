import cv2
import numpy as np

# Global variable to store mouse position
mouse_x, mouse_y = 0, 0

# Function to get color name based on HSV values
def get_color_name(h, s, v):
    if v < 75:
        return 'Black'
    elif v > 190 and s < 27:
        return 'White'
    elif s < 53 and v < 185:
        return 'Gray'
    
    # Custom color ranges
    if h < 10:
        return 'Red'
    elif 10 <= h < 20 and v > 100:
        return 'Sandal'
    elif 10 <= h < 20 and v <= 100:
        return 'Brown'
    elif 20 <= h < 30:
        return 'Yellow'
    elif 30 <= h < 45:
        return 'Light Green'
    elif 45 <= h < 85:
        return 'Green'
    elif 85 <= h < 100:
        return 'Aqua'
    elif 100 <= h < 125:
        return 'Blue'
    elif 125 <= h < 145:
        return 'Purple'
    elif 145 <= h < 165:
        return 'Pink'
    elif h >= 165:
        return 'Red'
    
    return 'Unknown'

# Mouse callback function
def mouse_move(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

# Start webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', mouse_move)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    # Get the pixel under the mouse
    pixel_bgr = frame[mouse_y, mouse_x]
    pixel_hsv = cv2.cvtColor(np.uint8([[pixel_bgr]]), cv2.COLOR_BGR2HSV)[0][0]
    color_name = get_color_name(pixel_hsv[0], pixel_hsv[1], pixel_hsv[2])

    # Display color name
    cv2.putText(frame, f'Color: {color_name}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Show frame
    cv2.imshow('Color Detector', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
