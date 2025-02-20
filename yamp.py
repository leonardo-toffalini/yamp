import sys

USAGE = """
Usage:
    uv run yamp.py <path>
"""


def parse(fpath: str) -> str:
    result = ""

    with open(fpath, "r") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))

    for line in lines:
        # Headings
        if line.startswith("###### "):
            result = result + "<h6>" + line[len("###### ") :] + "</h6>\n"
        if line.startswith("##### "):
            result = result + "<h5>" + line[len("##### ") :] + "</h5>\n"
        if line.startswith("#### "):
            result = result + "<h4>" + line[len("#### ") :] + "</h4>\n"
        if line.startswith("### "):
            result = result + "<h3>" + line[len("### ") :] + "</h3>\n"
        if line.startswith("## "):
            result = result + "<h2>" + line[len("## ") :] + "</h2>\n"
        if line.startswith("# "):
            result = result + "<h1>" + line[len("# ") :] + "</h1>\n"

        # Lists
        if line.startswith("- "):
            result = result + "<ul><li>" + line[len("- ") :] + "</li></ul>\n"
        if len(line) > 0 and line[0].isdigit() and line[1:3] == ". ":
            result = result + "<ol><li>" + line[len("1. ") :] + "</li></ol>\n"

    return result


def main(fpath: str):
    preamble = ""
    postamble = ""
    parsed_html = parse(fpath)
    return preamble + parsed_html + postamble


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(USAGE)
        exit(1)

    fpath = sys.argv[1]
    parsed = main(fpath)
    print(parsed)
