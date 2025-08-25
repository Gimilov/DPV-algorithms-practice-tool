import sys
from .helpers import ScaffoldHelper, ColorsHelper

def main():
    if len(sys.argv) != 2:
        print(f"""
{ColorsHelper.colored_text('-' * 100, 'magenta')}
{ColorsHelper.colored_text('USAGE:', 'white', bold=True)}
    python -m src.scaffold <exercise_number>

{ColorsHelper.colored_text('ARGUMENT FORMAT:', 'white', bold=True)}
    <exercise_number> must be in format: CHAPTER.PROBLEM or CHAPTER_PROBLEM
    Examples: '4.5', '6_2', '8.11'
{ColorsHelper.colored_text('-' * 100, 'magenta')}
""")
        return 1
    
    exercise = sys.argv[1].replace('_', '.')
    ScaffoldHelper.generate_solution_file(exercise)
    return 0

if __name__ == '__main__':
    sys.exit(main())