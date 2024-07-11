package com.example;

import static org.junit.jupiter.api.Assertions.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.junit.jupiter.api.Test;

public class ListingTest {
    
    @Test
    public void testTrimString() {
        String input = " hello world ";
        String expected = "hello world";
        String actual = input.trim();
        assertEquals(expected, actual, "The trimmed string should match the expected output.");
    }

    @Test
    public void testImmutableList() {
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("cherry");

        List<String> immutableList = Collections.unmodifiableList(list);
        List<String> expected = new ArrayList<>(list);

        assertEquals(expected, immutableList, "The immutable list should match the expected list.");
    }

    @Test
    public void testUppercaseList() {
        List<String> list = new ArrayList<>();
        list.add("apple");
        list.add("banana");
        list.add("cherry");

        List<String> upperList = new ArrayList<>();
        for (String item : list) {
            upperList.add(item.toUpperCase());
        }

        List<String> expected = new ArrayList<>();
        expected.add("APPLE");
        expected.add("BANANA");
        expected.add("CHERRY");

        assertEquals(expected, upperList, "The uppercase list should match the expected list.");
    }

    @Test
    public void testLoadMain() {
        Listing.main(null);
    }
}
