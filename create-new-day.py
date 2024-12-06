import shutil
from pathlib import Path
import sys
import logging
from aocd.models import Puzzle
from datetime import date

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def create_day_folder(day_number: int, year: int = date.today().year) -> None:
    """
    Create a new day folder from template and fetch puzzle data.
    
    Args:
        day_number: The day number to create
        year: AOC year (defaults to current year)
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

        # Fetch puzzle data
        puzzle = Puzzle(year=year, day=day_number)
        input_data = puzzle.input_data
        input_path = new_day_dir / "input.txt"
        input_path.write_text(input_data)
        logger.info(f"Downloaded input data: {len(input_data)} bytes")

        # Fetch puzzle description
        puzzle_title = puzzle.title
        puzzle_desc = puzzle.answer_a
        readme_path = new_day_dir / "README.md"
        readme_content = f"""# Day {day_number}: {year}

{puzzle_title}
"""
        readme_path.write_text(readme_content)
        logger.info("Created README with puzzle description")

    except Exception as e:
        logger.error(f"Error creating day {day_number}: {e}")
        sys.exit(1)

def main() -> int:
    """Main program entry point."""
    if len(sys.argv) not in (2, 3):
        logger.error("Usage: python create_new_day.py <day_number> [year]")
        return 1
        
    try:
        day_number = int(sys.argv[1])
        year = int(sys.argv[2]) if len(sys.argv) > 2 else date.today().year
        create_day_folder(day_number, year)
        return 0
        
    except ValueError:
        logger.error("Day number and year must be integers")
        return 1

if __name__ == "__main__":
    sys.exit(main())