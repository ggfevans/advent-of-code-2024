from typing import List, Tuple
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def read_input(filepath: Path) -> Tuple[List[int], List[int]]:
    """
    Read and parse input file containing two columns of numbers.
    
    Args:
        filepath: Path to input file
        
    Returns:
        Tuple of two lists containing left and right numbers
        
    Raises:
        FileNotFoundError: If input file doesn't exist
        ValueError: If input file has invalid format
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
        # Use list comprehension for cleaner parsing
        try:
            left_list, right_list = zip(*(
                map(int, line.strip().split()) 
                for line in lines if line.strip()
            ))
            return list(left_list), list(right_list)
        except ValueError as e:
            raise ValueError(f"Invalid input format: {e}")
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {filepath}")

def calculate_distance(left_list: List[int], right_list: List[int]) -> int:
    """
    Calculate total distance between paired numbers from two sorted lists.
    
    Args:
        left_list: First list of numbers
        right_list: Second list of numbers
        
    Returns:
        Total distance between paired numbers
        
    Raises:
        ValueError: If lists have different lengths
    """
    if len(left_list) != len(right_list):
        raise ValueError("Lists must have equal length")
        
    # Sort and calculate distances in one line
    return sum(abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list)))

def main() -> int:
    """Main program entry point."""
    try:
        input_path = Path('input.txt')
        left_list, right_list = read_input(input_path)
        result = calculate_distance(left_list, right_list)
        logger.info(f"Total distance: {result}")
        return 0
        
    except (FileNotFoundError, ValueError) as e:
        logger.error(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())