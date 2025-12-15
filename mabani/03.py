def get_valid_integer_input(prompt, must_be_odd=False):
    """
    Keeps asking the user for input until a valid integer is provided.
    """
    
    while True:
        user_input = input(prompt)
        
        try:
            # Try to convert to an integer
            value = int(user_input)
            
            # Check if it's a positive number
            if value <= 0:
                print("Error: Please enter a positive number (greater than zero).")
                continue # Ask again
                
            # Check if it must be odd (and if it is)
            if must_be_odd and value % 2 == 0:
                print("Error: This number must be an ODD number. Please try again.")
                continue # Ask again
                
            return value
            
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")
            
def get_tree_dimensions():
    """Gets tree, trunk, and pot dimensions from the user."""
    
    print("=== Please enter the tree dimensions ===")
    
    branch_length = get_valid_integer_input("Branch length (chars from trunk to tip): ")
    branch_height = get_valid_integer_input("Branch height (rows): ")
    branch_width = get_valid_integer_input("Max branch width at any level: ")
    trunk_height = get_valid_integer_input("Trunk height (rows): ")
    
    # Pass 'must_be_odd=True' for inputs that require it
    trunk_diameter = get_valid_integer_input("Trunk diameter (columns - must be odd): ", must_be_odd=True)
    pot_width = get_valid_integer_input("Pot width (columns - must be odd): ", must_be_odd=True)
    
    pot_height = get_valid_integer_input("Pot height (rows): ")
    
    return branch_length, branch_height, branch_width, trunk_height, trunk_diameter, (pot_width, pot_height)


def draw_branch(branch_length, branch_height, branch_width, trunk_center):
    """Generates a list of strings for the tree branches ('*')."""
    
    lines = []
    for level in range(branch_height):
        # Calculate how far the branch spreads at this level
        spread = (level + 1) * branch_length // branch_height
        width_at_level = min(spread * 2 + 1, branch_width)
        
        start = trunk_center - spread
        end = trunk_center + spread + 1
        
        # Create the line with a buffer
        line = [' '] * (trunk_center * 2 + branch_length + 10) 
        for i in range(max(0, start), min(len(line), end)):
            if width_at_level > 0:
                line[i] = '*'
        
        lines.append(''.join(line).rstrip())
        
    return lines


def draw_trunk(trunk_height, trunk_diameter, total_width):
    """Generates a list of strings for the tree trunk ('|')."""
    
    lines = []
    center = total_width // 2
    start = center - trunk_diameter // 2
    end = center + trunk_diameter // 2 + 1
    
    for _ in range(trunk_height):
        line = [' '] * total_width
        for i in range(start, end):
            line[i] = '|'
        lines.append(''.join(line))
        
    return lines


def draw_pot(pot_width, pot_height, student_name, total_width):
    """Generates a list of strings for the pot ('=' and '|') with the student's name."""
    
    lines = []
    center = total_width // 2
    half_width = pot_width // 2
    start = center - half_width
    end = center + half_width + 1
    
    # Top line of the pot
    top_line = [' '] * total_width
    for i in range(start, end):
        top_line[i] = '='
    lines.append(''.join(top_line))
    
    # Pot body
    mid_row = pot_height // 2
    # Center the name within the pot's inner width
    name_centered = student_name.center(pot_width - 2) 
    
    for row in range(1, pot_height - 1):
        line = [' '] * total_width
        line[start] = '|'
        line[end - 1] = '|'
        
        # Add the centered name to the middle row
        if row == mid_row and len(name_centered.strip()) > 0:
            name_start_index = start + 1
            for i, char in enumerate(name_centered):
                if name_start_index + i < end - 1:
                    line[name_start_index + i] = char
                    
        lines.append(''.join(line))
        
    # Bottom line of the pot
    bottom_line = [' '] * total_width
    for i in range(start, end):
        bottom_line[i] = '='
    lines.append(''.join(bottom_line))
    
    return lines


def main():
    """Main function to run the tree drawing program."""
    
    print("="*50)
    # print("      ASCII Art Tree Drawing Program")
    print("="*50)
    
    student_name = input("\nStudent's full name: ").strip()
    if not student_name:
        student_name = "Student"
        
    # Get all dimensions from the user
    (
        branch_length, 
        branch_height, 
        branch_width, 
        trunk_height, 
        trunk_diameter, 
        (pot_width, pot_height)
    ) = get_tree_dimensions()
    
    # Check if the pot width is sufficient for the name
    
    # +2 for the '|' walls on each side
    min_required_width = len(student_name) + 2
    
    # Ensure the minimum width is also an odd number for symmetry
    if min_required_width % 2 == 0:
        min_required_width += 1
        
    # Use the user's pot_width, unless the name requires a wider pot
    if pot_width < min_required_width:
        print(f"\n(Note: Pot width automatically increased from {pot_width} to {min_required_width} to fit the name.)")
        pot_width = min_required_width
    
    # Calculate the total width needed for the drawing *after* adjusting pot_width
    max_spread = branch_length + trunk_diameter // 2 + 10
    total_width = max(max_spread * 2, pot_width) + 20 # Add buffer
    trunk_center = total_width // 2
    
    # Generate the ASCII art for each part
    branch_lines = draw_branch(branch_length, branch_height, branch_width, trunk_center)
    trunk_lines = draw_trunk(trunk_height, trunk_diameter, total_width)
    
    # Draw the pot using the *new* (potentially larger) pot_width
    pot_lines = draw_pot(pot_width, pot_height, student_name, total_width)
    
    # Combine and print the final tree
    print("\n\n")
    
    for line in branch_lines:
        print(line)
        
    for line in trunk_lines:
        print(line)
        
    for line in pot_lines:
        print(line)
        
    print("\n\n")


# Run the program
if __name__ == "__main__":
    main()