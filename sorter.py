def sort(width, height, length, mass):
    
    # Determine if package is bulky
    volume = width * height * length
    is_bulky = (volume >= 1_000_000) or (width >= 150 or height >= 150 or length >= 150)
    
    # Determine if package is heavy
    is_heavy = (mass >= 20)
    
    # Return the correct stack
    return "REJECTED" if (is_bulky and is_heavy) else ("SPECIAL" if (is_bulky or is_heavy) else "STANDARD")


if __name__ == "__main__":

    print(sort(10, 10, 10, 5))       # STANDARD
    print(sort(200, 10, 10, 10))     # SPECIAL (bulky due to dimension)
    print(sort(50, 50, 50, 20))      # SPECIAL (heavy)
    print(sort(200, 200, 200, 30))   # REJECTED (both heavy and bulky)
