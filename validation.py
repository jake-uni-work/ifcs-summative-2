import re

# This Regex will match 
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