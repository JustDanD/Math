package com.justdan.math.equations;

public class Equation2 implements Equation{
    @Override
    public double calculateEquation(double x) {
        return Math.log10(x) - 1/x;
    }

    @Override
    public double calculateFirstDerivative(double x) {
        return (x + 1)/Math.pow(x, 2);
    }

    @Override
    public double calculateSecondDerivative(double x) {
        return -(x+2)/Math.pow(x, 3);
    }

    @Override
    public String toString() {
        return "lg(x) - 1/x = 0";
    }
}
