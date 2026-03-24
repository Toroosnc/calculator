#include <iostream>

extern "C" {
    double tambah(double a, double b) {
        return a + b;
    }
    double kurang(double a, double b) {
        return a - b;
    }
    double kali(double a, double b) {
        return a * b;
    }
    double bagi (double a, double b) {
        if (b == 0.0) {
            return 0.0;
        }
        return a / b;
    }
}