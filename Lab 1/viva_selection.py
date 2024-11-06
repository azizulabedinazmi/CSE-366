import random

def load_student_ids(filename):
    """Load student IDs from a file and return them as a list."""
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file if line.strip()]
        return student_ids
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

def viva_selection(student_ids):
    """Select students for viva until all have been chosen, then reset the list."""
    selected_count = 0  # Counter for Viva numbers
    while student_ids:
        # Randomly select a student
        student = random.choice(student_ids)
        selected_count += 1
        print(f"Viva #{selected_count}: {student}")
        
        # Remove the selected student from the list
        student_ids.remove(student)
        
        # If list is empty, reset
        if not student_ids:
            print("\nAll students have been selected. Resetting list...\n")
            student_ids = load_student_ids('student_ids.txt')

def main():
    # Load student IDs from file
    student_ids = load_student_ids('student_ids.txt')
    
    # Proceed if student IDs were successfully loaded
    if student_ids:
        viva_selection(student_ids)
    else:
        print("No student IDs to select from. Please check the file.")

# Run the main function
if __name__ == "__main__":
    main()
