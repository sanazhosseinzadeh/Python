import cv2
import numpy as np

# بارگذاری تصویر
image = cv2.imread('Python/Python-prj/pizza.jpg')

# ابعاد تصویر
height, width, _ = image.shape

# تقسیم تصویر به دو نیمه
half_width = width // 2

# ایجاد نسخه خاکستری تصویر
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image_colored = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

# قرار دادن نیمی از تصویر به رنگ خاکستری
image[:, half_width:] = gray_image_colored[:, half_width:]

# نمایش تصویر
cv2.imshow('Gray Half Image', image)

# ذخیره تصویر
cv2.imwrite('Python/Python-prj/pizza.jpg', image)

# منتظر ماندن تا کاربر یک کلید را فشار دهد
cv2.waitKey(0)
cv2.destroyAllWindows()