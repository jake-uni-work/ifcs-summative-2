import csv

def load_questions(file_name: str) -> list[dict]:
    questions = []
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # TODO: validate questions against schema
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