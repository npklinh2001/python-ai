"""
    Định nghĩa 1 class tên là Circle.
    Định nghĩa phương thức khởi tạo với tham số đầu vào là bán kính của hình tròn
    Định nghĩa 2 phương thức của class, lần lượt để tính chu vi và diện tích của
    hình tròn tương ứng

    Yêu cầu người dùng nhập vào 1 số thực dương. Tính chu vi và diện tích của hình tròn
    với bán kính tương ứng
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def calculate_area(self):
        area = self.pi * self.pi ** 2
        return area
    def calculate_perimeter(self):
        perimeter = 2 * self.pi * self.pi
        return perimeter


radius = int(input("Enter the radius of the circle: "))

circle = Circle(radius)
area = circle.calculate_area()
perimeter = circle.calculate_perimeter()

print("Area of the circle:", area)
print("Perimeter of the circle:", perimeter)