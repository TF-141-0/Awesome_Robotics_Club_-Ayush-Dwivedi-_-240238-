import math
from math import sin, cos, acos, atan2

# ================================
# Arm segment lengths
# ================================
L1 = 5.0   # coxa (rotates in XY plane)
L2 = 10.0  # femur (vertical plane)
L3 = 15.0  # tibia (extends from femur)

# ================================
# Round off small angles to zero
# ================================
def clean_angle(angle, threshold=1e-4):
    return 0.0 if abs(angle) < threshold else round(angle, 2)

# ================================
# Function to calculate joint angles
# ================================
def inverse_kinematics(x, y, z):
    alpha = math.degrees(atan2(y, x))  # phi1 (base rotation)
    
    # i m establishing a local frame for better understanding 

    x_local = math.sqrt(x**2 + y**2) - L1
    z_local = z
    dist = math.sqrt(x_local**2 + z_local**2)

    # Reachability check using triangle inequality
    if dist > (L2 + L3) or dist < abs(L2 - L3):
        return None

    try:
        gamma = -math.degrees(acos((dist**2 - L2**2 - L3**2) / (2 * L2 * L3)))  # Notice HERE if i take gamma to be +/- overall configuration of arm will with elbow down/up(read hexapod.md)
    except ValueError:# I have explained about this with visual repesentation in hexapod.md
        return None

    beta = math.degrees(
        atan2(z_local, x_local) -
        atan2(L3 * sin(math.radians(gamma)), L2 + L3 * cos(math.radians(gamma)))
    )  # phi2

    return [clean_angle(alpha), clean_angle(beta), clean_angle(gamma)]

# ================================
# Run inverse kinematics for specific input (optional)
# ================================

# Uncomment to enable manual input
# x = float(input("Target Coordinate x: "))
# y = float(input("Target Coordinate y: "))
# z = float(input("Target Coordinate z: "))
# angles = inverse_kinematics(x, y, z)

# if angles is None:
#     print("Unreachable: Invalid target for leg.")
# else:
#     phi1, phi2, phi3 = angles
#     print(f"Target Coordinates: ({x}, {y}, {z})")
#     print("Coordinates are reachable")
#     print(f"Joint Angles: phi1 = {phi1}°, phi2 = {phi2}°, phi3 = {phi3}°")

# ================================
# Test cases
# ================================

def Test1_inverse_kinematics():
    x, y, z = 5.0, 5.0, 5.0
    angles = inverse_kinematics(x, y, z)
    if angles is None:
        print("Test1: Unreachable")
    else:
        print(f"Target Coordinates: ({x}, {y}, {z})")
        print(f"Joint Angles: {angles}°")
        print("Coordinates are reachable")   

def Test2_inverse_kinematics():
    x, y, z = 0.1, 0.1, 0.1
    angles = inverse_kinematics(x, y, z)
    if angles is None:
        print("Test2: Unreachable")
    else:
        print(f"Target Coordinates: ({x}, {y}, {z})")
        print(f"Joint Angles: {angles}°")
        print("Coordinates are reachable")

def Test3_inverse_kinematics():
    x, y, z = L1 + L2 + L3, 0.0, 0.0
    angles = inverse_kinematics(x, y, z)
    if angles is None:
        print("Test3: Unreachable")
    else:
        print(f"Target Coordinates: ({x}, {y}, {z})")
        print(f"Joint Angles: {angles}°")
        print("Coordinates are reachable")

def Test4_inverse_kinematics():
    x, y, z = 100.0, 100.0, 100.0
    angles = inverse_kinematics(x, y, z)
    if angles is None:
        print("Test4: Unreachable")
    else:
        print(f"Target Coordinates: ({x}, {y}, {z})")
        print(f"Joint Angles: {angles}°")
        print("Coordinates are reachable")

def Test5_inverse_kinematics():
    x, y, z = 5.0, 5.0, -10.0
    angles = inverse_kinematics(x, y, z)
    if angles is None:
        print("Test5: Unreachable")
    else:
        print(f"Target Coordinates: ({x}, {y}, {z})")
        print(f"Joint Angles: {angles}°")
        print("Coordinates are reachable")

# ================================
# Run selected test
# ================================
#Test1_inverse_kinematics()
#Test2_inverse_kinematics()
#Test3_inverse_kinematics()
#Test4_inverse_kinematics()
#Test5_inverse_kinematics()
