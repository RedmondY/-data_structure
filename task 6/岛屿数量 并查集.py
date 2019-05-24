class UnionFindSet(object):
    def __init__(self, grid):

        m, n = len(grid), len(grid[0])
        self.roots = [-1 for _ in range(m * n)]
        self.rank = [0 for _ in range(m * n)]
        self.count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.roots[i * n + j] = i * n + j
                    self.count += 1

    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        for root in tmp:
            self.roots[root] = member
        return member

    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1


class Solution(object):
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        ufs = UnionFindSet(grid)
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':

                    for k in range(4):
                        x = i + dx[k]
                        y = j + dy[k]

                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            ufs.union(i * n + j, x * n + y)
        # print ufs.roots

        return ufs.count
