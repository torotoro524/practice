import cv2
import matplotlib.pyplot as plt

obj = cv2.VideoCapture(0)
a = 0
b = 0
x = []
y = []
plt.ion()

plt.title('graph')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0,255)
plt.grid()

while True:
 _, img_1 = obj.read()
 img_2 = cv2.cvtColor(img_1,cv2.COLOR_RGB2GRAY)
 a = a + 1
 b = img_2.mean()
 x.append(a)
 y.append(b)
 plt.plot(x,y,color = 'blue')
 plt.draw()
 cv2.imshow('PUSH ENTER KEY',img_1)
 if cv2.waitKey(1) == 13: break

plt.close()
obj.release()
cv2.destroyAllwindows()
