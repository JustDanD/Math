package com.justdan.math.methods;

import com.justdan.math.systemofequations.SystemEquation;
import com.justdan.math.systemofequations.SystemOfEquations;

import java.util.Arrays;

public class NewtonForSystem {

    private static double[][] getJacobian(double[] values, SystemEquation eq1, SystemEquation eq2) {
        double[][] jacobian = new double[2][2];
        jacobian[0][0] = eq1.calculateDerivativeX(values[0], values[1]);
        jacobian[0][1] = eq1.calculateDerivativeY(values[0], values[1]);
        jacobian[1][0] = eq2.calculateDerivativeX(values[0], values[1]);
        jacobian[1][1] = eq2.calculateDerivativeY(values[0], values[1]);
        return jacobian;
    }
    private static double[] getColumn(double[] values, SystemEquation eq1, SystemEquation eq2) {
        double[] column = new double[2];
        column[0] = -eq1.calculateEquation(values[0], values[1]);
        column[1] = -eq2.calculateEquation(values[0], values[1]);
        return column;
    }

    public static double[] calculate(SystemOfEquations system, double eps, double[] approximation) {
        double[][] jacobian;
        double[] results = approximation;
        double[] prevResults;
        double[] column, deltas;
        SystemEquation eq1 = system.getEquation(0);
        SystemEquation eq2 = system.getEquation(1);

        do {
            prevResults = Arrays.copyOf(results, results.length);
            jacobian = getJacobian(prevResults, eq1, eq2);
            column = getColumn(prevResults, eq1, eq2);
            deltas = Gauss.getResultColumn(jacobian, column);
            results[0] = results[0] + deltas[0];
            results[1] = results[1] + deltas[1];
        } while (Math.abs(results[0] - prevResults[0]) > eps || Math.abs(results[1] - prevResults[1]) > eps);
        return results;
    }
}
