import cv2
import numpy as np
import pytesseract as tes
cap=cv2.VideoCapture(1)
i=0
while True:
    ret,frame=cap.read()
    print(frame.shape)
    row=480
    column=640
    if i==0:
        frame = cv2.bitwise_not(frame)
    if not ret:
        break
    for r in range(row):
        for c in range(column):
            pix=frame[r,c]
            if np.array_equal(pix,[0,0,0]):
                a=r+10
                b1=c+10
                b2=c-10
                for j in range(a):
                    for h in range(b1-b2) :
                        print("black frame") 
    cv2.putText(
        frame,                    # Image/frame to draw on
        "well Hello There!",          # Text string
        (300,300),                  # Position (x, y) from top-left
        cv2.FONT_HERSHEY_SIMPLEX, # Font type
        1,                        # Font scale
        (0, 255, 0),               # Color (B, G, R) -> green
        2                         # Thickness of text
    )
    cv2.imshow("Phone Camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
