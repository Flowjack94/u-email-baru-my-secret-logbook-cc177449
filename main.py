"""My Secret Logbook — one diary line.

Writes the logbook line to the entry file and nothing else.
"""

import os

MIN_LEN = 1
MAX_LEN = 200


def build_line():
    opener = "Dear logbook: today my agent deleted 2,314 emails,"
    middle = "told the CEO the deploy was 'fine', and git blame still says I did it"
    closer = "\u2014 ticket #4821, day 47."
    return " ".join([opener, middle, closer])


def check_line(line):
    if line != line.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if not MIN_LEN <= len(line) <= MAX_LEN:
        raise ValueError("entry length %d outside %d-%d" % (len(line), MIN_LEN, MAX_LEN))
    if any(ord(ch) < 32 and ch not in "\n\t" for ch in line):
        raise ValueError("control character in entry")
    return line


def publish(line):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line:
            raise ValueError("round-trip mismatch")
    return path


def main():
    publish(check_line(build_line()))


if __name__ == "__main__":
    main()
