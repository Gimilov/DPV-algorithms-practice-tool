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