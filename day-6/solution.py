from aocd import submit, AocdError
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def read_input(file_path: str) -> str:
    """Read input data from a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    grid = [list(line) for line in data.split('\n') if line]
    rows, cols = len(grid), len(grid[0])
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    
    # Find the initial position and direction of the guard
    guard_pos = None
    guard_dir = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = grid[r][c]
                break
        if guard_pos:
            break
    
    if not guard_pos:
        logging.error("Guard's initial position not found.")
        return 0
    
    visited = set()
    steps = 0
    max_steps = 10000  # Limit the number of steps to prevent infinite loops
    
    while 0 <= guard_pos[0] < rows and 0 <= guard_pos[1] < cols and steps < max_steps:
        visited.add(guard_pos)
        logging.info(f"Step {steps}: Guard at {guard_pos} facing {guard_dir} | Distinct positions visited: {len(visited)}")
        dr, dc = directions[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)
        
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols and grid[next_pos[0]][next_pos[1]] != '#':
            guard_pos = next_pos
        else:
            guard_dir = turns[guard_dir]
            logging.info(f"Obstacle encountered, turning to {guard_dir} | Distinct positions visited: {len(visited)}")
        
        steps += 1
    
    if steps >= max_steps:
        logging.warning("Maximum steps reached, stopping to prevent infinite loop.")
    
    logging.info(f"Total distinct positions visited: {len(visited)}")
    return len(visited)

def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    # ...existing code...
    return 0

def main() -> None:
    """Main function to solve the puzzle."""
    input_data = read_input('input.txt')
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")

    if len(sys.argv) > 1 and sys.argv[1] == "--send-it":
        print("Step 5: Submitting the result via aocd")
        try:
            submit(part1(input_data), part="1", day=1, year=2024)
            print("🌟️🌟️🌟️Gooooold starrrrrr!🌟️🌟️🌟️ Submission successful! The answer is correct. ")
        except AocdError as e:
            print(f"Submission failed: {e}")
            print("The answer might be incorrect or there was an issue with the submission.")
    else:
        print("Dry run: Result will not be submitted")

def test_part1():
    """Test function for part 1."""
    test_data = """....#.....
..........
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
    expected_output = 41
    result = part1(test_data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
    print("Test passed!")

if __name__ == "__main__":
    main()
    test_part1()