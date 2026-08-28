"""Independent exact checks for tiny instances and strong odd cycles."""

from __future__ import annotations

from itertools import combinations

from build_reduction import build


def has_factor(f, edges):
    # Exact branch-and-bound, selecting the most constrained unsatisfied
    # vertex. This is independent of the gadget equations and avoids the
    # unnecessary 2^m scan once the tiny exhaustive audit grows.
    incidence = {v: [] for v in f}
    for i, edge in enumerate(edges):
        for v in edge:
            incidence[v].append(i)
    chosen = [False] * len(edges)
    deg = {v: 0 for v in f}

    def visit():
        pending = [v for v in f if deg[v] < f[v]]
        if not pending:
            return True
        v = min(pending, key=lambda w: sum(not chosen[i] for i in incidence[w]))
        for i in incidence[v]:
            if chosen[i] or any(deg[w] >= f[w] for w in edges[i]):
                continue
            chosen[i] = True
            for w in edges[i]:
                deg[w] += 1
            if visit():
                return True
            for w in edges[i]:
                deg[w] -= 1
            chosen[i] = False
        return False

    return visit()


def has_3dm(X, Y, Z, triples):
    n = len(X)
    for chosen in combinations(triples, n):
        if len({x for x, _, _ in chosen}) == n and len({y for _, y, _ in chosen}) == n and len({z for _, _, z in chosen}) == n:
            return True
    return False


def has_strong_odd_cycle(f, edges):
    incidence = {v: [] for v in f}
    for i, edge in enumerate(edges):
        for v in edge:
            incidence[v].append(i)
    vertices = sorted(f)
    for start in vertices:
        def dfs(current, vs, used_edges):
            for i in incidence[current]:
                if i in used_edges:
                    continue
                edge = edges[i]
                for nxt in edge:
                    if nxt == start:
                        if len(vs) >= 3 and len(vs) % 2 == 1:
                            cycle = set(vs)
                            if all(set(edges[j]).intersection(cycle) == {vs[p], vs[(p + 1) % len(vs)]}
                                   for p, j in enumerate(used_edges + [i])):
                                return True
                    elif nxt not in vs and nxt >= start:
                        if dfs(nxt, vs + [nxt], used_edges + [i]):
                            return True
            return False
        if dfs(start, [start], []):
            return True
    return False


def check_instance(instance):
    X, Y, Z, triples = instance
    f, edges = build(instance)
    return has_3dm(X, Y, Z, triples) == has_factor(f, edges), not has_strong_odd_cycle(f, edges)


def has_odd_two_regular_submatrix(f, edges):
    """Incidence-matrix audit: find an odd square submatrix with row/column sum 2."""
    rows = list(f)
    for k in range(3, min(len(rows), len(edges)) + 1, 2):
        for rs in combinations(rows, k):
            rset = set(rs)
            eligible = [j for j, edge in enumerate(edges)
                        if len(rset.intersection(edge)) == 2]
            for cs in combinations(eligible, k):
                if all(sum(v in edges[j] for j in cs) == 2 for v in rs):
                    return True
    return False
