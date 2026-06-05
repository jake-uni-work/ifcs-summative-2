def determine_count(categories: int) -> int:
    """Determines how many categories should be shown on the end screen, based on how many categories there are."""
    if categories < 2:
        return 0
    elif categories < 4:
        return 1
    elif categories < 8:
        return 2
    else:
        return 3


def strongest_and_weakest_categories(score_by_category: dict[str, int]) -> tuple[list[str], list[str]]:
    """Calculates the strongest and weakest categories using a dictionary of """
    count = determine_count(len(score_by_category))

    if count == 0:
        return ([], [])

    sorted_list = [tuple_[0] for tuple_ in sorted(
        [(category, score) for category, score in score_by_category.items()], key=lambda tuple_: tuple_[1])]
    if count == 1:
        strongest = [sorted_list[-1]]
        weakest = [sorted_list[0]]
    else:
        strongest = list(reversed(sorted_list[-count:]))
        weakest = sorted_list[0:count]

    return (strongest, weakest)


def calculate_categories(questions: list[dict], scores: list[int]) -> dict[str, int]:
    """From a list of questions and the list of scores, returns a dictionary containing the score per category"""
    score_by_category: dict[str, int] = {}
    for idx, question in enumerate(questions):
        category = question.get("category", None)
        if category:
            score_by_category.setdefault(category, 0)
            if scores[idx] > 0: 
                score_by_category[category] += 1

    return score_by_category
