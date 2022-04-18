package com.justdan.math.exceptions;

public class SameSignException extends Exception {
    public SameSignException() {
        super("На концах выбранного отрезка знак ф-ии одинаковый");
    }
}
