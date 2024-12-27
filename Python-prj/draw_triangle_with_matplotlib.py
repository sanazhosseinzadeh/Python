import matplotlib.pyplot as plt

# مختصات رأس‌های مثلث
x = [1, 4, 2.5, 1]  # مختصات x
y = [1, 1, 4, 1]    # مختصات y

# رسم مثلث
plt.figure(figsize=(6, 6))
plt.plot(x, y, marker='o', color='purple', linestyle='-')  # خط و نقطه‌های مثلث
plt.fill(x, y, color='gray', alpha=0.5)  # رنگ‌آمیزی داخل مثلث

# تنظیمات نمودار
plt.title("Draw triangle With Matplotlib", fontsize=14)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.axis('equal')  # مقیاس برابر
plt.show()
