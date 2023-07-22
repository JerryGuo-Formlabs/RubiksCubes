from enum import Enum
import random

# Assuming the 'Color' class is defined in the 'magiccube.cube_base' module
# Make sure to import 'Color' from the correct module if it's different.

class Face(Enum):
    UP = 0
    LEFT = 1
    FRONT = 2
    RIGHT = 3
    BACK = 4
    DOWN = 5

def solve_face_with_color_sequence(cube, target_color_sequence):
    target_face = Face.UP
    movements = []
    
    # Step 1: Rotate the cube to find a piece with the first color in the target sequence on the UP face
    found = False
    for _ in range(4):
        up_face = cube.get_face(target_face)
        if target_color_sequence[0] in up_face[0] and target_color_sequence[0] in up_face[-1]:
            found = True
            break
        cube.rotate("U")
        movements.append("U")
    
    if not found:
        print("First color in the target sequence not found on the UP face.")
        return

    # Step 2: Rotate the cube until the target piece is in one of the corners of the UP face
    target_piece_coords = None
    for x in [0, cube.size - 1]:
        for z in [0, cube.size - 1]:
            if up_face[x][z] == target_color_sequence[0]:
                target_piece_coords = (x, z)
                break
        if target_piece_coords:
            break

    if not target_piece_coords:
        print("Target piece not found on the corners of the UP face.")
        return

    # Step 3: Rotate the cube to bring the target piece to the front left corner of the UP face
    if target_piece_coords != (0, 0):
        movements += _move_to_corner(cube, target_piece_coords)

    # Step 4: Rotate the cube to bring other pieces with the target color sequence to the UP face
    while not _is_up_face_solved(cube, target_color_sequence):
        movements += _bring_color_sequence_to_up_face(cube, target_color_sequence)

    return movements

def _is_up_face_solved(cube, target_color_sequence):
    up_face = cube.get_face(Face.UP)
    return all(color in row for row in up_face for color in target_color_sequence)

def _move_to_corner(cube, target_piece_coords):
    movements = []
    x, z = target_piece_coords

    if x == 0:
        movements.append("U'")
    elif x == cube.size - 1:
        movements.append("U")

    if z == 0:
        movements.append("L'")
    elif z == cube.size - 1:
        movements.append("L")

    return movements

def _bring_color_sequence_to_up_face(cube, target_color_sequence):
    movements = []
    found = False

    for face in [Face.FRONT, Face.RIGHT, Face.BACK, Face.LEFT]:
        if _check_edge_for_target_color_sequence(cube, face, target_color_sequence):
            found = True
            break

    if not found:
        raise Exception("Unable to find an edge piece with the target color sequence.")

    if face == Face.FRONT:
        movements.append("F'")
    elif face == Face.RIGHT:
        movements.append("R'")
    elif face == Face.BACK:
        movements.append("B'")
    elif face == Face.LEFT:
        movements.append("L'")

    movements.append("U")
    movements.append("U")

    if face == Face.FRONT:
        movements.append("F")
    elif face == Face.RIGHT:
        movements.append("R")
    elif face == Face.BACK:
        movements.append("B")
    elif face == Face.LEFT:
        movements.append("L")

    movements.append("U'")

    return movements

def _check_edge_for_target_color_sequence(cube, face, target_color_sequence):
    edge_coords = [(0, 1), (1, 0), (1, 2), (2, 1)]
    edge_colors = [cube.get_piece(coord).get_piece_colors_str(no_loc=True)[1] for coord in edge_coords]
    return all(color in edge_colors for color in target_color_sequence)

# Example usage:
if __name__ == "__main__":
    # Initialize the Rubik's Cube
    cube = Cube(size=3)
    cube.scramble()  # Scramble the cube

    # Input the target color sequence (e.g., "RRRRRRRRR" for all red, "GGGGGGGGG" for all green, etc.)
    target_color_sequence = "RRRRRRRRR"

    print("Scrambled Cube:")
    print(cube)

    # Solve the "UP" face for the given color sequence
    movements = solve_face_with_color_sequence(cube, target_color_sequence)

    print("\nSolving movements:")
    print(" ".join(movements))

    print("\nSolved Cube:")
    print(cube)
