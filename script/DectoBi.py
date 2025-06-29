def decimal_to_binary(decimal_num):
    """
    Converts a decimal integer to its binary representation.

    Args:
        decimal_num (int): The decimal integer to convert.

    Returns:
        str: The binary representation of the decimal number, prefixed with "0b".
             Returns an error message if the input is not a valid integer.
    """
    try:
        # Ensure the input is an integer
        num = int(decimal_num)

        # Python's built-in bin() function converts an integer to a binary string
        # The result is prefixed with "0b" (e.g., bin(10) returns '0b1010')
        binary_representation = bin(num)
        return binary_representation
    except ValueError:
        return "Error: Please enter a valid integer."
    except TypeError:
        return "Error: Input must be a number."

def decimal_to_binary_custom(decimal_num):
    """
    Converts a decimal integer to its binary representation using a custom algorithm.
    This function demonstrates the logic without using the built-in bin() function.

    Args:
        decimal_num (int): The decimal integer to convert.

    Returns:
        str: The binary representation of the decimal number.
             Returns an error message if the input is not a valid integer.
    """
    try:
        num = int(decimal_num)
        if num == 0:
            return "0"
        
        binary_string = ""
        temp_num = abs(num) # Work with absolute value for conversion

        while temp_num > 0:
            remainder = temp_num % 2
            binary_string = str(remainder) + binary_string
            temp_num //= 2 # Integer division

        # Add negative sign if original number was negative
        if num < 0:
            binary_string = "-" + binary_string
            
        return binary_string
    except ValueError:
        return "Error: Please enter a valid integer."
    except TypeError:
        return "Error: Input must be a number."


# --- User Input and Example Usage ---
if __name__ == "__main__":
    print("--- Decimal to Binary Converter ---")
    while True:
        user_input = input("Enter a decimal number (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting converter. Goodbye!")
            break

        # Using the built-in function
        binary_result_builtin = decimal_to_binary(user_input)
        print(f"Using built-in bin(): Decimal {user_input} is Binary {binary_result_builtin}")

        # Using the custom function
        binary_result_custom = decimal_to_binary_custom(user_input)
        print(f"Using custom logic:   Decimal {user_input} is Binary {binary_result_custom}")

        print("-" * 30) # Separator

