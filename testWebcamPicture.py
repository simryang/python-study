import cv2

# 0이면 노트북 내장 웹캠 숫자를 올리면 추가된 웹캠을 이용할 수 있다.
cap = cv2.VideoCapture(0)
# 3은 가로 4는 세로 길이. 1080x720 == hd
# cap.set(3, 720)
# cap.set(4, 1080)
ret, frame = cap.read()  # 사진 촬영
cap.release()
frame = cv2.flip(frame, 1)  # 좌우 대칭

cv2.imwrite("sr.png", frame)
cv2.imshow("picture", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
# https://jinho-study.tistory.com/234