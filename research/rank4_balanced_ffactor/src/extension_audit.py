"""Clean-room checks for bounded degree and vertex expansion."""

from __future__ import annotations

from collections import Counter

from build_reduction import build
from exact_audit import has_factor
from expansion_audit import expand, has_perfect_matching, project


def degrees(vertices, edges):
    d = Counter()
    for edge in edges:
        d.update(edge)
    return {v: d[v] for v in vertices}


def enumerate_perfect_matchings(vertices, edges):
    incidence = {v: [] for v in vertices}
    for i, edge in enumerate(edges):
        for v in edge:
            incidence[v].append(i)
    uncovered = set(vertices)
    used = set()
    selected = []

    def visit():
        if not uncovered:
            yield tuple(selected)
            return
        v = min(uncovered, key=lambda w: sum(i not in used for i in incidence[w]))
        for i in incidence[v]:
            if i in used or any(w not in uncovered for w in edges[i]):
                continue
            used.add(i)
            uncovered.difference_update(edges[i])
            selected.append(i)
            yield from visit()
            selected.pop()
            uncovered.update(edges[i])
            used.remove(i)

    yield from visit()


def audit(instance):
    f, edges = build(instance)
    hf, hedges = expand(f, edges)
    source_max = max(degrees(f, edges).values(), default=0)
    expanded_max = max(degrees(hf, hedges).values(), default=0)
    rank_ok = max(map(len, hedges), default=0) <= 4
    return {
        "target_delta": source_max,
        "expanded_delta": expanded_max,
        "rank_ok": rank_ok,
        "equivalent": has_perfect_matching(list(hf), hedges) == has_factor(f, edges),
    }


def projected_degree_vector(matching_indices, hedges):
    projected = project([hedges[i] for i in matching_indices], hedges)
    counts = Counter(projected)
    return counts
