package com.justdan.math.equations;

public class Equation3 implements Equation{
    @Override
    public double calculateEquation(double x) {
        return Math.sin(x) - Math.tan(x) + 5*x;
    }

    @Override
    public double calculateFirstDerivative(double x) {
        return 5 + Math.cos(x) - 1/Math.pow(Math.cos(x), 2);
    }

    @Override
    public double calculateSecondDerivative(double x) {
        return -Math.sin(x) - (2*Math.sin(x)/Math.pow(Math.cos(x), 3));
    }

    @Override
    public String toString() {
        return "sin(x) - tg(x) + 5x = 0";
    }
}