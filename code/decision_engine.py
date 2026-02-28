from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Criterion:
    name: str
    weight: float
    mode: str  # benefit (higher better) or cost (lower better)


@dataclass
class EvaluationResult:
    option: str
    final_score: float
    criterion_scores: Dict[str, float]


def _normalize_weights(criteria: List[Criterion]) -> List[Criterion]:
    total = sum(c.weight for c in criteria)
    if total <= 0:
        raise ValueError("Total weight must be > 0")
    return [Criterion(c.name, c.weight / total, c.mode) for c in criteria]


def _normalize_values(values: List[float], mode: str) -> List[float]:
    min_v = min(values)
    max_v = max(values)

    if min_v == max_v:
        return [1.0 for _ in values]

    if mode == "benefit":
        return [(v - min_v) / (max_v - min_v) for v in values]
    if mode == "cost":
        return [(max_v - v) / (max_v - min_v) for v in values]

    raise ValueError(f"Invalid mode: {mode}")


def evaluate(
    options: List[str],
    criteria: List[Criterion],
    raw_scores: Dict[str, Dict[str, float]],
) -> Tuple[List[EvaluationResult], List[Criterion]]:
    normalized_criteria = _normalize_weights(criteria)
    totals = {o: 0.0 for o in options}
    breakdown = {o: {} for o in options}

    for criterion in normalized_criteria:
        column = [raw_scores[option][criterion.name] for option in options]
        normalized_column = _normalize_values(column, criterion.mode)

        for option, norm_value in zip(options, normalized_column):
            contribution = norm_value * criterion.weight
            totals[option] += contribution
            breakdown[option][criterion.name] = contribution

    results = [
        EvaluationResult(option=o, final_score=totals[o], criterion_scores=breakdown[o])
        for o in options
    ]
    results.sort(key=lambda r: r.final_score, reverse=True)
    return results, normalized_criteria
