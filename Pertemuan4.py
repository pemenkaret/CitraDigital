# test_opencv.py
import cv2
print("OpenCV version:", cv2.__version__)


import numpy as np

img = cv2.imread('C:/Users/Pandu/OneDrive/Dokumen/Perkuliahan smster 5/CitraDigital/assets/king.jpeg')



print (img)

H, W = img.shape[:2]
grey = np.zeros((H, W), np.uint8)

for i in range(H):
        for j in range(W):
            # Menghitung nilai grayscale
            grey[i, j] = np.clip(0.299 * img[i, j, 0] + 0.587 * img[i, j, 1] + 0.114 * img[i, j, 2], 0, 255)
           
    
print("\nGrayscale :")
print(grey)

cv2.imshow("RGB", img)
cv2.imshow("Grayscale", grey)
cv2.waitKey(0)
cv2.destroyAllWindows()
