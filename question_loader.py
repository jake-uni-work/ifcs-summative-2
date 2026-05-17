import csv

def load_questions(file_name: str) -> list[dict]:
    questions = []
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            validate_row(row)
            questions.append({
                "question": row["question"],
                "options": {
                    "a": row["option_a"].strip(),
                    "b": row["option_b"].strip(),
                    "c": row["option_c"].strip(),
                    "d": row["option_d"].strip()
                },
                "correct": row["correct"],
                "category": row.get("category", None)
            })
    return questions


def validate_row(row: dict) -> None:
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
    
    # TODO: maybe have c and d be optional?
    
    if "option_c" not in row:
        raise ValueError("Question is missing option C")
    
    if "option_d" not in row:
        raise ValueError("Question is missing option D")
    
    if "correct" not in row:
        raise ValueError("Question is missing the correct answer")
    
    if row['correct'] not in ("a", "b", "c", "d"):
        raise ValueError("Correct answer must be a, b, c or d")


if __name__ == "__main__":
    print(load_questions("questions.csv"))