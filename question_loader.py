import csv
from validation import validate_question

def load_questions(file_name: str) -> list[dict]:
    """Loads a set of questions from the provided CSV file"""
    questions = []
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            validate_question(row)
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


if __name__ == "__main__":
    print(load_questions("questions.csv"))