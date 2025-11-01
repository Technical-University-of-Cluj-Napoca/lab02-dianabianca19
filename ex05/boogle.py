from trie import Trie

class Boggle:
    def __init__(self, grid, words):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.trie = Trie()
        self.trie.build_from_list(words)
        self.results = set()

    def _dfs(self, i, j, visited, prefix):
        if (i < 0 or j < 0 or i >= self.rows or j >= self.cols or (i, j) in visited):
            return

        prefix += self.grid[i][j].lower()


        if not self.trie.starts_with(prefix):
            return

        if len(prefix) > 1 and self.trie.search(prefix):
            self.results.add(prefix)

        visited.add((i, j))


        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di != 0 or dj != 0:
                    self._dfs(i + di, j + dj, visited, prefix)

        visited.remove((i, j))

    def find_words(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self._dfs(i, j, set(), "")
        return sorted(self.results)
