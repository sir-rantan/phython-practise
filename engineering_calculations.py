def calculate_speed(distance, time):
    return distance / time
def calculate_force(mass, acceleration):
    return mass * acceleration
def calculate_power(force, velocity):
    return force * velocity
speed = calculate_speed(100, 5)
force = calculate_force(10, 9.81)
power = calculate_power(50, 4)
print("Speed:", speed, "m/s")
print("Force:", force, "N")
print("Power:", power, "W")
