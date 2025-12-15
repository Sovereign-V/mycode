#!/usr/bin/env python3
"""Ghostbusters Lab | Step 3"""

def report_ghost_sighting(ghost_name, location="New York City"):
    """Prints details about the ghost sighting."""
    print(f"{ghost_name} has been sighted at {location}! Who you gonna call?")

def calculate_catch_rate(ghost_name):
    """Returns a catch rate based on the ghost's name."""
    return len(ghost_name) * 10
    #len() is a built in function that counts the number of 'pieces' to an object.


# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")
report_ghost_sighting("Stay Puft")

# Calls the funtion and store result
rate = calculate_catch_rate("slimer")
# Print the result
print("the catch rate for this is:", rate)
