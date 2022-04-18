package com.justdan.math;

import com.justdan.math.IO.IOUnit;
import com.justdan.math.equations.Equation;
import com.justdan.math.equations.Storage;
import com.justdan.math.methods.Chord;
import com.justdan.math.methods.Newton;
import com.justdan.math.methods.NewtonForSystem;
import com.justdan.math.systemofequations.SystemOfEquations;

import java.util.InputMismatchException;



public class Main {
    public static void main(String[] args) {
        Storage storage = new Storage();
        SystemOfEquations system  = new SystemOfEquations();
        while (true) {
            IOUnit io = new IOUnit();
            try {
                IOUnit.printIntro();
                switch (io.getNumber()) {
                    case 1: {
                        io.printEquations(storage);
                        Equation equation = storage.getEquation(io.getNumber());
                        double eps = io.getEps();
                        double[] borders = io.getBorders();
                        double resultChord = Chord.calculate(borders[0], borders[1], eps, equation);
                        io.printString("Метод Хорд:\nx: " + resultChord);
                        double resultNewton = Newton.calculate(borders[0], borders[1], eps, equation);
                        io.printString("Метод Ньютона:\nx: " + resultNewton);
                        io.printString("Разница ответов:\nx: " + Math.abs(resultChord - resultNewton));
                        break;
                    }
                    case 2: {
                        io.printSystem(system);
                        double eps = io.getEps();
                        double[] approximation = io.getApproximation();
                        double[] result = NewtonForSystem.calculate(system, eps, approximation);
                        io.printString("Решение системы:");
                        io.printString("x: " + result[0]);
                        io.printString("y: " + result[1]);
                        break;
                    }
                    case 3:
                        System.out.println("До свидания!");
                        System.exit(2);
                        break;
                    default:
                        System.out.println("Введите валидное значение");
                        break;
                }
            } catch (InputMismatchException e) {
                System.out.println("Введите валидное значение");
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
