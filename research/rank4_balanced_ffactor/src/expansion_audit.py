"""Independent vertex-expansion and perfect-cover checks."""

from __future__ import annotations

from itertools import product
from functools import lru_cache


def expand(f, edges):
    """Build H^f directly from the definition, including all edge copies."""
    clones = {v: [f"{v}^{i}" for i in range(f[v])] for v in f}
    expanded_edges = []
    for edge in edges:
        for choices in product(*(clones[v] for v in edge)):
            expanded_edges.append(tuple(choices))
    expanded_f = {clone: 1 for copies in clones.values() for clone in copies}
    return expanded_f, expanded_edges


def has_perfect_matching(vertices, edges):
    """Exact cover search for a 0/1 perfect hyperedge matching."""
    incidence = {v: [] for v in vertices}
    for i, edge in enumerate(edges):
        for v in edge:
            incidence[v].append(i)
    uncovered = set(vertices)
    used = set()

    def visit():
        if not uncovered:
            return True
        v = min(uncovered, key=lambda w: sum(i not in used for i in incidence[w]))
        for i in incidence[v]:
            if i in used:
                continue
            edge = edges[i]
            if any(w not in uncovered for w in edge):
                continue
            used.add(i)
            uncovered.difference_update(edge)
            if visit():
                return True
            uncovered.update(edge)
            used.remove(i)
        return False

    return visit()


def has_perfect_matching_bitset(vertices, edges):
    """Memoized exact-cover solver used for the exhaustive expansion audit."""
    index = {v: i for i, v in enumerate(vertices)}
    masks = [sum(1 << index[v] for v in edge) for edge in edges]
    incidence = [[] for _ in vertices]
    for i, mask in enumerate(masks):
        for j in range(len(vertices)):
            if mask >> j & 1:
                incidence[j].append(i)
    full = (1 << len(vertices)) - 1

    @lru_cache(maxsize=None)
    def visit(remaining):
        if remaining == 0:
            return True
        best = None
        best_options = None
        for j in range(len(vertices)):
            if remaining >> j & 1:
                options = [i for i in incidence[j] if masks[i] & remaining == masks[i]]
                if not options:
                    return False
                if best_options is None or len(options) < len(best_options):
                    best, best_options = j, options
        return any(visit(remaining ^ masks[i]) for i in best_options)

    return visit(full)


def project(matching, expanded_edges):
    """Project selected expanded edges to original labels before the ^ clone."""
    return [tuple(v.rsplit("^", 1)[0] for v in edge) for edge in matching]
