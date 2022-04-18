package com.justdan.math.methods;

import com.justdan.math.equations.Equation;
import com.justdan.math.exceptions.BordersException;
import com.justdan.math.exceptions.SameSignException;

public class Newton {

    private static boolean isGoodStart(double x, Equation equation) {
        return equation.calculateSecondDerivative(x) * equation.calculateEquation(x) > 0;
    }

    public static double calculate(double a, double b, double eps, Equation equation) throws SameSignException, BordersException {
        double xi = (a + b) / 2;
        if (a >= b)
            throw new BordersException();
        if (!equation.areSignsDifferent(a, b))
            throw new SameSignException();
        while (!isGoodStart(xi, equation) && xi >= a)
            xi = xi - eps;
        if (!isGoodStart(xi, equation)) {
            xi = (a + b) / 2;
            while (!isGoodStart(xi, equation) && xi <= b)
                xi = xi + eps;
        }
        if (!isGoodStart(xi, equation))
            xi = (a + b) / 2;
        while (Math.abs(equation.calculateEquation(xi) / equation.calculateFirstDerivative(xi)) > eps) {
            xi = xi - (equation.calculateEquation(xi) / equation.calculateFirstDerivative(xi));
        }
        return xi;
    }
}
