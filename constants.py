WINDOW_BG_COLOUR = '#a7a8ce'
TEXT_FG_COLOUR = '#05182a'

WINDOW_INIT_WIDTH=640
WINDOW_INIT_HEIGHT=480

WINDOW_MIN_WIDTH=WINDOW_INIT_WIDTH
WINDOW_MIN_HEIGHT=WINDOW_INIT_HEIGHT


def font(size=20, bold=False):
    """Helper function to ensure a consistent font across the UI"""
    return ("Arial", size) if not bold else ("Arial", size, "bold")