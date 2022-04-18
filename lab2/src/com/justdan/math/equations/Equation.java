package com.justdan.math.equations;

public interface Equation {
    double calculateEquation(double x);

    double calculateFirstDerivative(double x);

    double calculateSecondDerivative(double x);

    default boolean areSignsDifferent(double a, double b) {
        if ((a == 0 && b != 0) || (a != 0 && b == 0))
            return true;
        return (calculateEquation(a) * calculateEquation(b) < 0);
    }
}
