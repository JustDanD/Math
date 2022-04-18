package com.justdan.math.exceptions;

public class NoSolutionException extends Exception{
    public NoSolutionException() {
        super("На данном отрезке нет решения");
    }
}
