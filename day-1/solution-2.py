from typing import List, Tuple
from collections import Counter
import logging
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
    """
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            
        left_list, right_list = zip(*(
            map(int, line.strip().split()) 
            for line in lines if line.strip()
        ))
        return list(left_list), list(right_list)
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {filepath}")
    except ValueError as e:
        raise ValueError(f"Invalid input format: {e}")

def calculate_similarity_score(left_list: List[int], right_list: List[int]) -> int:
    """
    Calculate similarity score based on frequency of left numbers in right list.
    
    Each number in left list is multiplied by its frequency in right list.
    
    Args:
        left_list: List of numbers to check
        right_list: List to count frequencies from
        
    Returns:
        Total similarity score
    """
    # Create frequency counter for right list
    right_frequencies = Counter(right_list)
    
    # Calculate score: sum of (number * its frequency in right list)
    return sum(num * right_frequencies[num] for num in left_list)

def main() -> int:
    """Main program entry point."""
    try:
        # Test with example data first
        example_left = [3, 4, 2, 1, 3, 3]
        example_right = [4, 3, 5, 3, 9, 3]
        example_score = calculate_similarity_score(example_left, example_right)
        logger.info(f"Example similarity score: {example_score}")
        assert example_score == 31, f"Example failed: got {example_score}, expected 31"
        
        # Process actual input
        input_path = Path('input.txt')
        left_list, right_list = read_input(input_path)
        result = calculate_similarity_score(left_list, right_list)
        logger.info(f"Final similarity score: {result}")
        return 0
        
    except (FileNotFoundError, ValueError, AssertionError) as e:
        logger.error(f"Error: {e}")
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())