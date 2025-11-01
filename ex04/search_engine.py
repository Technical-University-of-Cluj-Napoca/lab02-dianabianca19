import os
import time


def _get_char_unix():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch

def _get_char_windows():
    import msvcrt
    ch = msvcrt.getwch()
    return ch

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def search_loop(tree, max_suggestions=10, prompt="Search: "):
    if os.name == 'nt':
        getch = _get_char_windows
    else:
        getch = _get_char_unix

    prefix = ""
    try:
        while True:
            clear_console()
            print(prompt + prefix)
            if prefix:
                suggestions = tree.autocomplete(prefix)[:max_suggestions]
                print("\nSuggestions ({}):".format(len(suggestions)))
                for s in suggestions:
                    print("  " + s)
            else:
                print("\nType to get suggestions. Backspace to delete. Ctrl-C to exit.")

            ch = getch()
            if ch in ('\x03',):  # Ctrl-C
                print("\nExiting.")
                break
            if ch in ('\r', '\n'):
                print("\nYou selected:", prefix)
                time.sleep(0.5)
                break
            if ch in ('\x7f', '\x08'):
                prefix = prefix[:-1]
                continue
            if len(ch) == 1 and ch.isprintable():
                prefix += ch
                continue

    except KeyboardInterrupt:
        print("\nInterrupted.")
