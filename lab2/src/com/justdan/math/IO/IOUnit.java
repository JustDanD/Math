package com.justdan.math.IO;

import com.justdan.math.equations.Storage;
import com.justdan.math.systemofequations.SystemOfEquations;

import java.util.Locale;
import java.util.Scanner;

public class IOUnit {
    private final Scanner scanner = new Scanner(System.in);

    public IOUnit() {
        scanner.useLocale(Locale.US);
    }
    public static void printIntro() {
        System.out.println("Выберите, что хотите сделать:");
        System.out.println("1) Решить равнение");
        System.out.println("2) Решить систему уравнений");
        System.out.println("3) Выйти");
    }

    public int getNumber() {
        return scanner.nextInt();
    }

    public double getEps() {
        System.out.println("Введите желаемую точность:");
        return scanner.nextDouble();
    }

    public double[] getBorders() {
        double[] borders = new double[2];
        System.out.println("Введите отрезок изоляции корня:");
        System.out.println("Левая граница:");
        borders[0] = scanner.nextDouble();
        System.out.println("Правая граница:");
        borders[1] = scanner.nextDouble();
        return borders;
    }
    public double[] getApproximation() {
        double[] approximation = new double[2];
        System.out.println("Введите первое приближение:");
        System.out.println("X:");
        approximation[0] = scanner.nextDouble();
        System.out.println("Y:");
        approximation[1] = scanner.nextDouble();
        return approximation;
    }

    public void printEquations(Storage storage) {
        System.out.println("Выберите уравнение:");
        for (int i = 1; i < storage.getStorage().size() + 1; i++)
            System.out.println(i + ") " + storage.getEquation(i).toString());
    }

    public void printSystem(SystemOfEquations system) {
        System.out.println("Система нелинейных уравнений:");
        for (int i = 0; i < system.getEquations().size(); i++)
            System.out.println(system.getEquation(i).toString());
    }

    public void printString(String str) {
        System.out.println(str);
    }
}
