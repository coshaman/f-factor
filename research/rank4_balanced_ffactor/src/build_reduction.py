"""Construct the proposed rank-four balanced-hypergraph reduction."""

from __future__ import annotations


def build(instance: tuple[list[str], list[str], list[str], list[tuple[str, str, str]]]):
    X, Y, Z, triples = instance
    edges: list[tuple[str, ...]] = []
    f: dict[str, int] = {v: 1 for v in X + Y + Z}
    for k, (x, y, z) in enumerate(triples):
        tag = f"e{k}"
        c = f"{tag}:c"
        hs = [f"{tag}:h{i}" for i in range(1, 5)]
        rs = [f"{tag}:r{i}" for i in range(1, 3)]
        f[c] = 5
        for v in hs + rs:
            f[v] = 1
        edges.extend((
            (c, hs[0]), (c, hs[1]), (c, hs[2]), (c, hs[3]),
            (c, hs[0], hs[1], rs[0]),
            (c, hs[2], hs[3], rs[1]),
            (c, rs[0], rs[1]),
            (c, x), (c, y), (c, z),
        ))
    return f, edges


def mode_edges(k: int, triple: tuple[str, str, str], on: bool):
    """Return the selected local edges, useful for a constructive witness."""
    x, y, z = triple
    tag = f"e{k}"
    c = f"{tag}:c"
    hs = [f"{tag}:h{i}" for i in range(1, 5)]
    rs = [f"{tag}:r{i}" for i in range(1, 3)]
    if on:
        return [(c, hs[0], hs[1], rs[0]), (c, hs[2], hs[3], rs[1]),
                (c, x), (c, y), (c, z)]
    return [(c, h) for h in hs] + [(c, rs[0], rs[1])]
