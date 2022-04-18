package com.justdan.math.methods;

import com.justdan.math.equations.Equation;
import com.justdan.math.exceptions.BordersException;
import com.justdan.math.exceptions.NoSolutionException;
import com.justdan.math.exceptions.SameSignException;

public class Chord {
    public static double calculate(double a, double b, double eps, Equation equation) throws SameSignException, BordersException, NoSolutionException {
        double xi, ai = a, bi = b;
        if (a >= b)
            throw new BordersException();
        if (!equation.areSignsDifferent(a, b))
            throw new SameSignException();
        do {
            xi = (ai * equation.calculateEquation(bi) - bi * equation.calculateEquation(ai)) / (equation.calculateEquation(bi) - equation.calculateEquation(ai));
            if (equation.areSignsDifferent(ai, xi))
                bi = xi;
            else if (equation.areSignsDifferent(xi, bi))
                ai = xi;
            else
                throw new NoSolutionException();
        } while (Math.abs(equation.calculateEquation(xi)) > eps);
        return xi;
    }
}
