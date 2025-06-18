# Initialize variables to store results
numbers = []           # List to store all numbers from file
total_sum = 0         # Sum of all numbers
count = 0             # Count of numbers
minimum = None        # Minimum value
maximum = None        # Maximum value
frequency = {}        # Dictionary to track frequency of each number
duplicates = []       # List to store numbers that appear more than once

# Read numbers.txt line by line
try:
    with open('numbers.txt', 'r') as file:
        for line in file:
            # Convert each line to integer and add to list
            number = int(line.strip())  # strip() removes whitespace/newlines
            numbers.append(number)
            
            # Update sum and count
            total_sum += number
            count += 1
            
            # Update minimum and maximum
            if minimum is None or number < minimum:
                minimum = number
            if maximum is None or number > maximum:
                maximum = number
            
            # Update frequency dictionary
            if number in frequency:
                frequency[number] += 1
            else:
                frequency[number] = 1

    # Find duplicates using conditionals
    for number, freq in frequency.items():
        if freq > 1:  # If number appears more than once
            duplicates.append(number)

    # Sort duplicates for consistent output
    duplicates.sort()

    # Write report to report.txt
    with open('report.txt', 'w') as report_file:
        report_file.write(f"Count: {count}\n")
        report_file.write(f"Sum: {total_sum}\n")
        report_file.write(f"Min: {minimum}\n")
        report_file.write(f"Max: {maximum}\n")
        
        # Convert duplicates list to comma-separated string
        duplicates_str = ', '.join(map(str, duplicates)) if duplicates else ""
        report_file.write(f"Duplicates: {duplicates_str}\n")

    # Display results to console (optional)
    print(f"Numbers read: {numbers}")
    print(f"Sum: {total_sum}")
    print(f"Count: {count}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Average: {total_sum / count if count > 0 else 0}")
    print(f"Frequency dictionary: {frequency}")
    print(f"Duplicates: {duplicates}")
    
    # Print completion message
    print("Report generated")

except FileNotFoundError:
    print("Error: numbers.txt file not found!")
except ValueError as e:
    print(f"Error: Invalid number format in file - {e}")
except Exception as e:
    print(f"An error occurred: {e}")