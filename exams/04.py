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
            

def get_student_name():
    """
    This function reads the student's first and last name from the input
    and returns it.
    """
    name = input("Please enter your first and last name: ")
    return name

def get_tree_dimensions(student_name):
    """
    This function (the main function required by the assignment)
    gets 4 main dimensions, calculates 2 others,
    and returns all six variables.
    
    Input: student_name (to calculate the pot width)
    """
    print("\n--- Tree Dimensions Setup ---")
    
    branch_height, trunk_height, trunk_width, pot_height = map(int, input().split())
    
    
    tree_list = [branch_height, trunk_height, trunk_width, pot_height]

    tree_dict = {
        "t_branch_height": tree_list[0],
        "t_trunk_height": tree_list[1],
        "t_trunk_width": tree_list[2],
        "t_pot_height": tree_list[3]
    }
    
    # branch_height = get_valid_integer_input("What is the branch height? (e.g., 7): ")
    # trunk_height = get_valid_integer_input("What is the trunk height? (e.g., 3): ")
    # trunk_width = get_valid_integer_input("What is the trunk width? (e.g., 3): ", must_be_odd=True)
    # pot_height = get_valid_integer_input("What is the pot height? (e.g., 3): ", must_be_odd=True)

    max_branch_width = tree_dict["t_trunk_width"] * 2 - 1
    name_pot_width = len(student_name) + 2
    default_pot_width = tree_dict["t_trunk_width"] + 4
    pot_width = max(name_pot_width, default_pot_width)

    return tree_dict["t_branch_height"], max_branch_width, tree_dict["t_trunk_height"], tree_dict["t_trunk_width"], tree_dict["t_pot_height"], pot_width

def draw_branches(height, total_canvas_width):
    """
    This function draws the tree branches (triangle) with '*'.
    total_canvas_width helps center the triangle on the main canvas.
    """
    for i in range(height):
        stars = '*' * (i * 2 + 1)
        print(stars.center(total_canvas_width))

def draw_trunk(height, width, total_canvas_width):
    """
    This function draws the tree trunk with '|'.
    total_canvas_width is used to center the trunk.
    """
    
    trunk_shape = '|' * width
    
    for i in range(height):
        print(trunk_shape.center(total_canvas_width))

def draw_pot(height, width, total_canvas_width, student_name):
    """
    This function draws the pot and places the student's name in the middle.
    The pot 'width' is guaranteed to be wide enough for the name.
    'total_canvas_width' is used to center the entire pot.
    """
    
    top_edge = '=' * width
    print(top_edge.center(total_canvas_width))

    middle_line = (height - 1) // 2 

    for i in range(height):
        if i == middle_line:
            inner_space = width - 2 
            centered_name = student_name.center(inner_space)
            
            print( ('|' + centered_name + '|').center(total_canvas_width) )
            
        else:
            inner_space = ' ' * (width - 2)
            print( ('|' + inner_space + '|').center(total_canvas_width) )

    bottom_edge = '=' * width
    print(bottom_edge.center(total_canvas_width))


def main():
    """
    The main function of the program, which calls
    the other functions in order.
    """
    
    name = get_student_name()
    
    (branch_h, branch_w, 
     trunk_h, trunk_w, 
     pot_h, pot_w) = get_tree_dimensions(name)

    total_width = max(branch_w, pot_w)

    print("\n...Drawing your tree...\n")
    
    draw_branches(branch_h, total_width)
    draw_trunk(trunk_h, trunk_w, total_width)
    draw_pot(pot_h, pot_w, total_width, name)

main()
