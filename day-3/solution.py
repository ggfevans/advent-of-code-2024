import re
from aocd import submit, AocdError
import sys

def read_input(file_path: str) -> str:
    """Read input data from a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def extract_mul_instructions(data: str) -> list:
    """Extract valid mul instructions from the corrupted memory."""
    pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')
    pattern_do = re.compile(r'do\(\)')
    pattern_dont = re.compile(r"don't\(\)")
    
    instructions = []
    enabled = True  # Initially, mul instructions are enabled
    
    for line in data.splitlines():
        if pattern_do.search(line):
            enabled = True
        elif pattern_dont.search(line):
            enabled = False
        elif enabled:
            instructions.extend((int(x), int(y)) for x, y in pattern_mul.findall(line))
    
    return instructions

def part1(data: str) -> int:
    """Solve part 1 of the puzzle."""
    instructions = extract_mul_instructions(data)
    return sum(x * y for x, y in instructions)

def part2(data: str) -> int:
    """Solve part 2 of the puzzle."""
    instructions = extract_mul_instructions(data)
    return sum(x * y for x, y in instructions)

def main() -> None:
    """Main function to solve the puzzle."""
    input_data = read_input('input.txt')
    print(f"Part 1: {part1(input_data)}")
    print(f"Part 2: {part2(input_data)}")

    if len(sys.argv) > 1 and sys.argv[1] == "--send-it":
        print("Step 5: Submitting the result via aocd")
        try:
            submit(part1(input_data), part="2", day=3, year=2024)
            print("🌟️🌟️🌟️Gooooold starrrrrr!🌟️🌟️🌟️ Submission successful! The answer is correct. ")
        except AocdError as e:
            print(f"Submission failed: {e}")
            print("The answer might be incorrect or there was an issue with the submission.")
    else:
        print("Dry run: Result will not be submitted")

if __name__ == "__main__":
    main()