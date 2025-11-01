import sys
import argparse
from BST import BST
from search_engine import search_loop

def main():
    parser = argparse.ArgumentParser(description="Search Engine Suggestions demo")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="Local wordlist file path", metavar="PATH")
    group.add_argument("--url", help="URL to a wordlist (one word per line)", metavar="URL")
    parser.add_argument("--max", type=int, default=10, help="Max number of suggestions to display")
    args = parser.parse_args()

    if args.file:
        print("Loading words from file:", args.file)
        tree = BST(source=args.file, file=True)
    else:
        print("Loading words from URL:", args.url)
        tree = BST(source=args.url, url=True)

    print("Loaded {} words.".format(len(tree.words)))
    print("Starting interactive search. Press Ctrl-C to quit.")
    try:
        search_loop(tree, max_suggestions=args.max)
    except Exception as e:
        print("Error during interactive loop:", e)

if __name__ == "__main__":
    main()
