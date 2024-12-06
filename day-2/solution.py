from aocd import submit, AocdError
import sys

def is_safe(report):
    if len(report) <= 1:
        return True
    increasing = all(report[i] < report[i + 1] and 1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] and 1 <= report[i] - report[i + 1] <= 3 for i in range(len(report) - 1))
    return increasing or decreasing

def is_safe_with_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            print(f"Report {report} is made safe by removing level {report[i]}")
            return True
    return False

def count_safe_reports(filepath):
    print("Step 1: Reading the input file")
    safe_count = 0
    with open(filepath, 'r') as file:
        for line in file:
            try:
                report = list(map(int, line.split()))
                if is_safe_with_dampener(report):
                    safe_count += 1
            except ValueError:
                print(f"Warning: Skipping malformed report: {line.strip()}")
    print("Step 2: Counting safe reports")
    return safe_count

if __name__ == "__main__":
    filepath = "/Users/gevans/code/advent-of-code-2024/day-2/input.txt"
    print("Step 3: Starting main execution")
    safe_count = count_safe_reports(filepath)
    print(f"Step 4: Number of safe reports: {safe_count}")
    
    if len(sys.argv) > 1 and sys.argv[1] == "--send-it":
        print("Step 5: Submitting the result via aocd")
        try:
            submit(safe_count, part="2", day=2, year=2024)
            print("🌟️🌟️🌟️Gooooold starrrrrr!🌟️🌟️🌟️ Submission successful! The answer is correct. ")
        except AocdError as e:
            print(f"Submission failed: {e}")
            print("The answer might be incorrect or there was an issue with the submission.")
    else:
        print("Dry run: Result will not be submitted")