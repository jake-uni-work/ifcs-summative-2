import re

VALID_NAME_RE = re.compile(r"^[a-zA-Z\-' ]+$")    
    
def validate_name_length(name: str) -> bool:
    """Checks whether the provided name is a valid length, which is between 3 and 50 characters long"""
    return 2 <= len(name) <= 50

def validate_name_characters(name: str) -> bool:
    """Checks whether the provided name has any invalid characters"""
    return VALID_NAME_RE.match(name) is not None

def format_name(name: str) -> str:
    """Removes any whitespace from a name and converts the name to title case"""
    return name.strip().title()

def validate_question(row: dict) -> None:
    """
    Validates a provided CSV row to check it contains all of the required data.
    
    Will raise ValueError if any errors are found.
    
    This function does not return anything
    """
    if "question" not in row:
        raise ValueError("Question is missing the question")
    
    if "option_a" not in row:
        raise ValueError("Question is missing option A")
    
    if "option_b" not in row:
        raise ValueError("Question is missing option B")
        
    if "option_c" not in row:
        raise ValueError("Question is missing option C")
    
    if "option_d" not in row:
        raise ValueError("Question is missing option D")
    
    if "correct" not in row:
        raise ValueError("Question is missing the correct answer")
    
    if row['correct'] not in ("a", "b", "c", "d"):
        raise ValueError("Correct answer must be a, b, c or d")