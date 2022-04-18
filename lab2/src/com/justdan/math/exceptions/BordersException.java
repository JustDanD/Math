package com.justdan.math.exceptions;

public class BordersException extends Exception {
    public BordersException() {
        super("Левая граница больше правой");
    }
}