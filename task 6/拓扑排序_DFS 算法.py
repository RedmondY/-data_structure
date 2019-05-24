def naiveTopoSort(G, S=None):
    if S is None:
        S = set(G.keys())
    if len(S) == 1:
        return list(S)
    s = S.pop()
    seq = naiveTopoSort(G, S)
    min_index = 0
    for i, v in enumerate(seq):
        if s in G[v]:
            min_index = i + 1
    seq.insert(min_index, s)
    return seq


# 有向无环图的邻接字典
G = {
    'a': {'b', 'c', 'd', 'e', 'f'},
    'b': {'c', 'd', 'e', 'f'},
    'c': {'d', 'e', 'f'},
    'd': {'e', 'f'},
    'e': {'f'},
    'f': {}
}

res = naiveTopoSort(G)
print(res)
