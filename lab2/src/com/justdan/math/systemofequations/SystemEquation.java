package com.justdan.math.systemofequations;

public interface SystemEquation {

    double calculateEquation(double x, double y);

    double calculateDerivativeX(double x, double y);

    double calculateDerivativeY(double x, double y);

    String printDerivativeX();

    String printDerivativeY();
}
