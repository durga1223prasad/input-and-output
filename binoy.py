x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 != x1:
    slope = (y2 - y1) / (x2 - x1)
    print(f"The slope of the line joining Ajay's house and Binoy's house is {slope:.2f}")
else:
    print("The line is vertical, slope is undefined")