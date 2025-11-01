class Node:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class BST:
    def __init__(self, source=None, url=False, file=False, **kwargs):

        self.root = None
        words = []

        if source is None:
            self.words = []
            return

        if url and file:
            raise ValueError("Options url and file cannot both be True.")

        if url:
            from urllib import request
            resp = request.urlopen(source)
            raw = resp.read().decode('utf-8', errors='ignore')
            words = [w.strip() for w in raw.splitlines() if w.strip()]
        elif file:
            with open(source, 'r', encoding='utf-8', errors='ignore') as f:
                words = [line.strip() for line in f if line.strip()]
        else:
            if isinstance(source, (list, tuple)):
                words = list(source)
            else:
                try:
                    with open(source, 'r', encoding='utf-8', errors='ignore') as f:
                        words = [line.strip() for line in f if line.strip()]
                except Exception:
                    raise ValueError("Unknown source type and file not found.")


        words = sorted(set(words))
        self.words = words
        if words:
            self.root = self._build_balanced(words, 0, len(words)-1)

    def _build_balanced(self, arr, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        node = Node(arr[mid])
        node.left = self._build_balanced(arr, l, mid-1)
        node.right = self._build_balanced(arr, mid+1, r)
        return node

    def autocomplete(self, prefix):
        results = []
        if not self.root or prefix is None:
            return results
        self._collect(self.root, prefix, results)
        return results

    def _collect(self, node, prefix, results):
        if node is None:
            return


        if node.word < prefix:
            self._collect(node.right, prefix, results)
            return


        if node.word.startswith(prefix):
            self._collect(node.left, prefix, results)
            results.append(node.word)
            self._collect(node.right, prefix, results)
            return

        self._collect(node.left, prefix, results)
