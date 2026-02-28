from __future__ import annotations

from typing import List

from decision_engine import Criterion, EvaluationResult, evaluate


def ask_int(prompt: str, min_value: int) -> int:
    while True:
        try:
            value = int(input(prompt).strip())
            if value < min_value:
                print(f"Enter a value >= {min_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer")


def ask_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number")


def ask_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty")


def ask_mode(prompt: str) -> str:
    while True:
        value = input(prompt).strip().lower()
        if value in {"benefit", "b", "higher", "h"}:
            return "benefit"
        if value in {"cost", "c", "lower", "l"}:
            return "cost"
        print("Type benefit (higher is better) or cost (lower is better)")


def get_options() -> List[str]:
    count = ask_int("How many options? (min 2): ", 2)
    options: List[str] = []
    for i in range(1, count + 1):
        while True:
            name = ask_text(f"Option {i} name: ")
            if name in options:
                print("Option name already exists")
                continue
            options.append(name)
            break
    return options


def get_criteria() -> List[Criterion]:
    count = ask_int("How many criteria? (min 1): ", 1)
    criteria: List[Criterion] = []

    for i in range(1, count + 1):
        while True:
            name = ask_text(f"Criterion {i} name: ")
            if any(c.name == name for c in criteria):
                print("Criterion name already exists")
                continue
            break

        weight = ask_float(f"Weight for '{name}' (positive number): ")
        while weight <= 0:
            print("Weight must be > 0")
            weight = ask_float(f"Weight for '{name}' (positive number): ")

        mode = ask_mode(f"Type for '{name}' [benefit/cost]: ")
        criteria.append(Criterion(name=name, weight=weight, mode=mode))

    return criteria


def get_scores(options: List[str], criteria: List[Criterion]):
    scores = {o: {} for o in options}
    print("\nEnter raw values (any numeric scale)")

    for option in options:
        print(f"\nOption: {option}")
        for criterion in criteria:
            value = ask_float(f"  {criterion.name}: ")
            scores[option][criterion.name] = value

    return scores


def print_results(results: List[EvaluationResult], criteria: List[Criterion]) -> None:
    print("\nRanked Recommendation")
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result.option} | score={result.final_score:.4f}")

    winner = results[0]
    print("\nWhy this is recommended")
    print(f"Top option: {winner.option}")

    criteria_map = {c.name: c for c in criteria}
    ordered = sorted(winner.criterion_scores.items(), key=lambda x: x[1], reverse=True)

    for name, contribution in ordered:
        c = criteria_map[name]
        print(
            f"- {name}: contribution={contribution:.4f}, "
            f"weight={c.weight:.2%}, type={c.mode}"
        )

    if len(results) > 1:
        margin = winner.final_score - results[1].final_score
        print(f"Margin vs 2nd place: {margin:.4f}")


def main() -> None:
    print("Decision Companion System - View 3 (General CLI)")
    print("Transparent weighted scoring. No AI dependency for ranking.")

    _ = input("Decision title (optional): ").strip()
    options = get_options()
    criteria = get_criteria()
    scores = get_scores(options, criteria)

    results, normalized_criteria = evaluate(options, criteria, scores)
    print_results(results, normalized_criteria)


if __name__ == "__main__":
    main()
