package com.justdan.math.equations;

import java.util.HashMap;
import java.util.Map;

public class Storage {
    private final Map<Integer, Equation> storage;

    public Storage() {
        storage= new HashMap<>();
        storage.put(1, new Equation1());
        storage.put(2, new Equation2());
        storage.put(3, new Equation3());
    }

    public Map<Integer, Equation> getStorage() {
        return storage;
    }


    public Equation getEquation(int id) {
        return storage.get(id >= 1 && id <= storage.size() ? id : 1);
    }
}
