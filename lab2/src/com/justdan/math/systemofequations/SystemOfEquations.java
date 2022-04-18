package com.justdan.math.systemofequations;

import com.justdan.math.equations.Equation;

import java.util.ArrayList;
import java.util.Map;

public class SystemOfEquations {
    ArrayList<SystemEquation> equations;

    public SystemOfEquations() {
        equations = new ArrayList<>();
        equations.add(new SystemEquation1());
        equations.add(new SystemEquation2());
    }
    public ArrayList<SystemEquation> getEquations() {
        return equations;
    }
    public SystemEquation getEquation(int id) {
        return equations.get(id);
    }
}
