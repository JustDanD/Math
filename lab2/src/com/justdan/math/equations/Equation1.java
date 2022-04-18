package com.justdan.math.equations;

public class Equation1 implements Equation {
    @Override
    public double calculateEquation(double x) {
        return Math.pow(x, 4) + 2 * Math.pow(x, 3) + 5 * x - 4;
    }

    @Override
    public double calculateFirstDerivative(double x) {
        return 4*Math.pow(x, 3) + 6 * Math.pow(x, 2) + 5;
    }

    @Override
    public double calculateSecondDerivative(double x) {
        return 12 * x * (x + 1);
    }

    @Override
    public String toString() {
        return "x^4 + 2 * x^3 + 5 * x - 4 = 0";
    }
}
