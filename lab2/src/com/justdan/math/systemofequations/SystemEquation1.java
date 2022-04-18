package com.justdan.math.systemofequations;

public class SystemEquation1 implements SystemEquation {
    @Override
    public double calculateEquation(double x, double y) {
        return Math.pow(x, 2) + Math.pow(y, 2) -1;
    }

    @Override
    public double calculateDerivativeX(double x, double y) {
        return 2 * x;
    }

    @Override
    public double calculateDerivativeY(double x, double y) {
        return 2 * y;
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
        return "f(x, y) = x^2 + y^2 - 1";
    }
}
