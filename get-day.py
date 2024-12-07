
"""
get-day.py

This script is inspired by and references code from get_input.py by Jonathan  Paulson.
Source: https://github.com/jonathanpaulson/AdventOfCode/tree/master

Author: Gareth Evans
Date: 2024-12-06
"""
from datetime import date
import shutil
from pathlib import Path
import sys
import logging
import argparse
import subprocess
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
SESSION = os.getenv('SESSION')
useragent = 'https://github.com/ggfevans/advent-of-code-2024/blob/master/create-new-day.py by hi@gmail.com'

def create_day_folder(day_number: int, year: int) -> None:
    """
    Create a new day folder from template and fetch puzzle data.
    
    Args:
        day_number: The day number to create
        year: AOC year
    """
    template_dir = Path('template-day')
    new_day_dir = Path(f'day-{day_number}')
    
    # Validate inputs
    if not template_dir.exists():
        logger.error("Template directory not found!")
        sys.exit(1)
    
    if new_day_dir.exists():
        logger.error(f"Day {day_number} already exists!")
        sys.exit(1)

    try:
        # Create folder structure
        shutil.copytree(template_dir, new_day_dir)
        logger.info(f"Created new day: {new_day_dir}")

        # Fetch puzzle input data
        cmd = f'curl https://adventofcode.com/{year}/day/{day_number}/input --cookie "session={SESSION}" -A \'{useragent}\''
        input_data = subprocess.check_output(cmd, shell=True).decode('utf-8')
        input_path = new_day_dir / "input.txt"
        input_path.write_text(input_data)
        logger.info(f"Downloaded input data: {len(input_data)} bytes")

    except Exception as e:
        logger.error(f"Error creating day {day_number}: {e}")
        sys.exit(1)

def main() -> int:
    """Main program entry point."""
    parser = argparse.ArgumentParser(description='Create a new Advent of Code day folder')
    parser.add_argument('day_number', type=int, help='The day number to create')
    parser.add_argument('--year', type=int, default=date.today().year, help='AOC year (defaults to current year)')
    args = parser.parse_args()

    create_day_folder(args.day_number, args.year)
    return 0

if __name__ == "__main__":
    sys.exit(main())