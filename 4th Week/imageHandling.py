import numpy as np
import cv2
import matplotlib.pyplot as plt

# 이미지 파일 불러오기
# 상대 경로의 기준이 어떻게되는걸까?
image = cv2.imread(
    "4th Week/images/profileImage.jpg", cv2.IMREAD_UNCHANGED)

# 이미지의 높이, 너비, 채널 값 저장
height, width, channel = image.shape

# 이미지 회전(오른쪽으로 90도)
matrix = cv2.getRotationMatrix2D((width/2, height/2), -90, 1)
imageRotated = cv2.warpAffine(image, matrix, (width, height))

# 사이즈 조정
# 축소할 때에는 대개 INTER_AREA
imageResized = cv2.resize(imageRotated, dsize=(
    100, 100), interpolation=cv2.INTER_AREA)

# 흑백 전환
imageToGray = cv2.cvtColor(imageResized, cv2.COLOR_BGR2GRAY)

cv2.imshow("Lee", imageToGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
