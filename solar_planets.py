import cv2
readImage = cv2.imread("solar-system.jpg")
text = "Sun"
cv2.putText(readImage, text, (20,250), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Mecury"
cv2.putText(readImage, text, (100,250), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Venus"
cv2.putText(readImage, text, (190,260), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Earth"
cv2.putText(readImage, text, (270,270), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Mars"
cv2.putText(readImage, text, (370,250), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Jupiter"
cv2.putText(readImage, text, (530,380), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Saturn"
cv2.putText(readImage, text, (760,320), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Uranus"
cv2.putText(readImage, text, (950,300), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
text = "Netune"
cv2.putText(readImage, text, (1100,300), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (255,255,255))
cv2.imshow("Planets", readImage)
cv2.waitKey(0)
