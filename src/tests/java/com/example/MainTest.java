package com.example;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
// Import the class you are testing. 
// If main.java is in the default package (no package declaration), 
// you cannot import it easily into a named package.
// RECOMMENDATION: Move main.java into a package or remove 'package tests;' 
// and keep everything in the default package for simple projects.

public class MainTest {
    @Test
    public void testGreeting() {
        // Assuming you refactor 'main' to be testable
        assertEquals("Hello World", new Main().getGreeting());
        // assertEquals(1, 1); // Simple placeholder test
    }
}