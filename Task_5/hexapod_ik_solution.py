#include <stdio.h>
#include <math.h>

const double L1 = 5.0;
const double L2 = 10.0;
const double L3 = 15.0;

 //Round off Small angles to zero (i need to add this cause in some of my independent checks i realised this)

double angle(double a, double threshold) {
    return (fabs(a) < threshold) ? 0.0 : round(a * 100.0) / 100.0;
}

int inverse_kinematics(double x, double y, double z, double* alpha_out, double* beta_out, double* gamma_out)
    {
    double alpha = atan2(y, x) * 180.0 / M_PI;

    double x_local = sqrt(x * x + y * y) - L1;
    double z_local = z;
    double dist = sqrt(x_local * x_local + z_local * z_local);

    if (dist > (L2 + L3) || dist < fabs(L2 - L3)) {
        return 0;
    }

    double cos_gamma = (dist * dist - L2 * L2 - L3 * L3) / (2 * L2 * L3);
    if (cos_gamma < -1.0 || cos_gamma > 1.0) {
        return 0;
    }

    double gamma = -acos(cos_gamma) * 180.0 / M_PI; // # Notice HERE if i take gamma to be +/- overall configuration of arm will change as elbow down/up(read hexapod.md)

    double gamma_rad = gamma * M_PI / 180.0;
    double beta = atan2(z_local, x_local) - atan2(L3 * sin(gamma_rad), L2 + L3 * cos(gamma_rad));
    beta = beta * 180.0 / M_PI;

    *alpha_out = angle(alpha, 1e-4);
    *beta_out = angle(beta, 1e-4);
    *gamma_out = angle(gamma, 1e-4);

    return 1;
}

void start_test(double x, double y, double z) {
    double alpha, beta, gamma;
    printf("Target Coordinates: (%.2f, %.2f, %.2f)\n", x, y, z);
    if (inverse_kinematics(x, y, z, &alpha, &beta, &gamma)) {
        printf("  Joint Angles: [%.2f°, %.2f°, %.2f°]\n", alpha, beta, gamma);
        printf("  Coordinates are reachable\n");
    } else {
        printf("  Warning: Invalid target for leg\n");
    }
    printf("\n");
}

void Test1_inverse_kinematics() { start_test(5.0, 5.0, 5.0); }
void Test2_inverse_kinematics() { start_test(0.1, 0.1, 0.1); }
void Test3_inverse_kinematics() { start_test(0.0, 30.0, 0.0); }
void Test4_inverse_kinematics() { start_test(100.0, 100.0, 100.0); }
void Test5_inverse_kinematics() { start_test(5.0, 5.0, -10.0); }

int main() {
    Test1_inverse_kinematics();
    Test2_inverse_kinematics();
    Test3_inverse_kinematics();
    Test4_inverse_kinematics();
    Test5_inverse_kinematics();
    return 0;
}
