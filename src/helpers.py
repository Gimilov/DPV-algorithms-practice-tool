import importlib


class ColorsHelper:
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    white = '\033[97m'
    reset = '\033[0m'
    blue = '\033[94m'
    magenta = '\033[95m'
    cyan = '\033[96m'

    @staticmethod
    def colored_text(text, color, bold=False):
        base_code = getattr(ColorsHelper, color.lower())
        bold_code = '\033[1m' if bold else ''
        reset_code = ColorsHelper.reset
        return f'{bold_code}{base_code}{text}{reset_code}'
    

class ScaffoldHelper:
    @staticmethod
    def generate_solution_file(exercise_number):
        """Overwrite user_solution.py with exercise description and function signature"""
        try:
            # Load exercise data
            chapter = exercise_number.split('.')[0]
            exercise_module = importlib.import_module(f'scaffold.dpv_chapter_{chapter}_description')
            exercise_data = exercise_module.exercise_details[exercise_number]
            
            template = f'''"""
DPV {exercise_number}:

{exercise_data['description']}
"""
{exercise_data['user_solution_scaffold']}
'''
            with open('user_solution.py', 'w', encoding='utf-8') as f:
                f.write(template)
                
            print(ColorsHelper.colored_text(f"✓ user_solution.py scaffolded for exercise {exercise_number}", 'magenta', bold=True))
            
        except (ImportError, KeyError) as e:
            print(ColorsHelper.colored_text(f"✗ Could not find exercise {exercise_number}: {e}", 'red', bold=True))
