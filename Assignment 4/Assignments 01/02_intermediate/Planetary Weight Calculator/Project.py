"""
Planetary Weight Calculator

This program prompts the user for a weight on Earth
and a planet (in separate inputs). It then prints
the equivalent weight on that planet.
"""

# Gravitational constants for each planet relative to Earth
GRAVITY = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    try:
        # Prompt the user for their weight on Earth
        earth_weight = float(input("Enter a weight on Earth: "))
        
        # Prompt the user for the name of a planet
        planet = input("Enter a planet: ")
        
        # Validate user input
        while planet not in GRAVITY:
            print("Invalid planet name. Please enter one of the following:")
            print(", ".join(GRAVITY.keys()))
            planet = input("Enter a planet: ")
        
        # Calculate the equivalent weight on the selected planet
        planetary_weight = round(earth_weight * GRAVITY[planet], 2)

        # Print the result
        print(f"The equivalent weight on {planet}: {planetary_weight}")
        
        # Performance messages
        if planetary_weight == earth_weight:
            print("Wow! Your weight remains the same!")
        elif planetary_weight > earth_weight:
            print("Whoa! You would weigh more on this planet!")
        else:
            print("Nice! You'd be lighter on this planet!")
    
    except ValueError:
        print("Invalid input! Please enter a numerical value for weight.")

if __name__ == "__main__":
    main()