import shutil
from pathlib import Path
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def create_day_folder(day_number: int) -> None:
    """
    Create a new day folder from template.
    
    Args:
        day_number: The day number to create
    """
    template_dir = Path('template-day')
    new_day_dir = Path(f'day-{day_number}')
    
    # Check if template exists
    if not template_dir.exists():
        logger.error("Template directory not found!")
        sys.exit(1)
        
    # Check if day already exists
    if new_day_dir.exists():
        logger.error(f"Day {day_number} already exists!")
        sys.exit(1)
        
    try:
        # Copy template to new day folder
        shutil.copytree(template_dir, new_day_dir)
        logger.info(f"Created new day: {new_day_dir}")
        
    except Exception as e:
        logger.error(f"Error creating day {day_number}: {e}")
        sys.exit(1)

def main() -> int:
    """Main program entry point."""
    if len(sys.argv) != 2:
        logger.error("Usage: python create_new_day.py <day_number>")
        return 1
        
    try:
        day_number = int(sys.argv[1])
        create_day_folder(day_number)
        return 0
        
    except ValueError:
        logger.error("Day number must be an integer")
        return 1

if __name__ == "__main__":
    sys.exit(main())