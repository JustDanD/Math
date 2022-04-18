package com.justdan.math.systemofequations;

public class SystemEquation2 implements SystemEquation{
    @Override
    public double calculateEquation(double x, double y) {
        return Math.pow(x, 3) - y;
    }

    @Override
    public double calculateDerivativeX(double x, double y) {
        return 3 * Math.pow(x, 2);
    }

    @Override
    public double calculateDerivativeY(double x, double y) {
        return -1;
    }

    @Override
    public String printDerivativeX() {
        return "2 * x";
    }

    @Override
    public String printDerivativeY() {
        return "2 * y";
    }

    @Override
    public String toString() {
        return "g(x, y) = x^3 - y";
    }
}
