import argparse
from urllib import request
from boogle import Boggle

def load_words(source, url=False, file=False):
    words = []
    if url:
        resp = request.urlopen(source)
        text = resp.read().decode('utf-8', errors='ignore')
        words = [w.strip().lower() for w in text.splitlines() if w.strip()]
    elif file:
        with open(source, 'r', encoding='utf-8', errors='ignore') as f:
            words = [line.strip().lower() for line in f if line.strip()]
    else:
        raise ValueError("Specify file or url for word list.")
    return words

def main():
    parser = argparse.ArgumentParser(description="Boggle Search (Trie-based)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Path to local dictionary file")
    group.add_argument("--url", help="URL for dictionary list")
    args = parser.parse_args()

    # Load words
    print("Loading words...")
    if args.file:
        words = load_words(args.file, file=True)
    else:
        words = load_words(args.url, url=True)
    print(f"Loaded {len(words)} words.")


    grid = [
        ['d', 'a', 'n', 's'],
        ['v', 'a', 'l', 's'],
        ['p', 'a', 's', 'o'],
        ['t', 'g', 'p', 's']
    ]

    print("\nGrid:")
    for row in grid:
        print(" ".join(row))

    b = Boggle(grid, words)
    found = b.find_words()
    print("\nFound words:")
    for w in found:
        print(w)
    print(f"\nTotal found: {len(found)}")

if __name__ == "__main__":
    main()
