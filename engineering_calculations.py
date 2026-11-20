def calculate_speed(distance, time):
    return distance / time
def calculate_force(mass, acceleration):
    return mass * acceleration
def calculate_power(force, velocity):
    return force * velocity
def calculate_acceleration(Velocity, time):
    return Velocity / time  
speed = calculate_speed(100, 5)
force = calculate_force(10, 9.81)
power = calculate_power(50, 4)
acceleration = calculate_acceleration(1000,40)
print("Speed:", speed, "m/s")
print("Force:", force, "N")
print("Power:", power, "W")
print("acceleration:", acceleration, "m/s^2")
