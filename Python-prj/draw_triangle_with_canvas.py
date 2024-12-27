from tkinter import Tk, Canvas

# ایجاد پنجره اصلی برنامه
root = Tk()
root.title("رسم مثلث")

# تنظیمات Canvas
canvas_width = 400
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# مختصات رأس‌های مثلث
x1, y1 = 100, 300  # گوشه پایین سمت چپ
x2, y2 = 300, 300  # گوشه پایین سمت راست
x3, y3 = 200, 100  # رأس بالا

# رسم مثلث
canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill="purple", outline="white", width=2)

# اجرای برنامه
root.mainloop()
