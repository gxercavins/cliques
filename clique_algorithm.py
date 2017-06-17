# Group developers into cliques given an adjacency graph. This implementation is based in the recursive algorithm
# proposed by Bron and Kerbosch in 1973 and adapted from the pseudocode in
# https://en.wikipedia.org/wiki/Bron-Kerbosch_algorithm


def bron_kerbosch(r, p, x, graph, cliques):
    if not p and not x:
        cliques.append(r)
    else:
        for v in p.copy():
            bron_kerbosch(r.union([v]), p.intersection(graph[v]), x.intersection(graph[v]), graph, cliques)
            p.remove(v)
            x.add(v)
    return cliques
