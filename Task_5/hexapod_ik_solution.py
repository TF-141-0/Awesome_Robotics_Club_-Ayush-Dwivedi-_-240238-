import math
from math import sin, cos, acos, atan2

# Arm segment lengths
# ================================
L1 = 5.0   # coxa (rotates in XY plane)
L2 = 10.0  # femur (vertical plane)
L3 = 15.0  # tibia (extends from femur)

# Round off Small angles to zero (i need to add this cause in some of my independent checks i realised this)
# ================================
def angle(angle, threshold=1e-4):
    return 0.0 if abs(angle) < threshold else round(angle, 2)

# Function to Calculate joint angles
# ================================
def inverse_kinematics(x, y, z):
    alpha = math.degrees(atan2(y, x))  # phi1 (base rotation)
    
    # i m establishing a local frame for better understanding of DOF
    x_local = math.sqrt(x**2 + y**2) - L1
    z_local = z
    dist = math.sqrt(x_local**2 + z_local**2)
    
    if dist > (L2 + L3) or dist < abs(L2 - L3):
        return None

    try:
        gamma = -math.degrees(acos((dist**2 - L2**2 - L3**2) / (2 * L2 * L3)))  # Notice HERE if i take gamma to be +/- overall configuration of arm will change as elbow down/up(read hexapod.md)
    except ValueError:                                                          # I have explained about this with visual repesentation in hexapod.md
        return None

    beta = math.degrees(atan2(z_local, x_local)-atan2(L3 * sin(math.radians(gamma)), L2 + L3 * cos(math.radians(gamma))))  # phi2

    return [angle(alpha), angle(beta), angle(gamma)]

# Test executer
# ================================
def start_test(x, y, z):
    angles = inverse_kinematics(x, y, z)
    print(f"Target Coordinates: ({x}, {y}, {z})")
    if angles is None:
        print(" Warning: Invalid target for leg")
    else:
        print(f"  Joint Angles: {angles}°")
        print("  Coordinates are reachable")

# Test cases
# ================================

def Test1_inverse_kinematics():
    x, y, z = 5.0, 5.0, 5.0
    start_test(x, y, z)

def Test2_inverse_kinematics():
    x, y, z = 0.1, 0.1, 0.1
    start_test(x, y, z)

def Test3_inverse_kinematics():
    x, y, z = 0.0, 30.0, 0.0
    start_test(x, y, z)

def Test4_inverse_kinematics():
    x, y, z = 100.0, 100.0, 100.0
    start_test(x, y, z)

def Test5_inverse_kinematics():
    x, y, z = 5.0, 5.0, -10.0
    start_test(x, y, z)

# Run selected test by removing #
# ================================

#Test1_inverse_kinematics()
#Test2_inverse_kinematics()
#Test3_inverse_kinematics()
#Test4_inverse_kinematics()
#Test5_inverse_kinematics()
