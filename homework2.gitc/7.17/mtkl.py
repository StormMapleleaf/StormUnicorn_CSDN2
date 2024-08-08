import random
def calculate_pi(num_points):
    num = 0 
    for _ in range(num_points):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            num += 1
    return num / num_points * 4

num_points = 1000000
print("π的数值：", calculate_pi(num_points))