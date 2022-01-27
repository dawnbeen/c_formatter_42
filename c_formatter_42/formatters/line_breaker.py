import re


def line_breaker(content: str, column_limit: int = 80) -> str:
    lines = content.split("\n")
    lines = list(map(lambda s: insert_break(s, column_limit), lines))
    return "\n".join(lines)


def insert_break(line: str, column_limit: int) -> str:
    if line_length(line) <= column_limit:
        return line

    line_indent_level = indent_level(line)
    tabulation = "\t" * (line_indent_level + 1)

    # break at all breakable spaces (space after comma or space before binary operators)
    breakable_space_pattern = r"((?<=,) | (?=[+\-*/%])(?!\*+\S|\+\+|\-\-))"
    line = re.sub(breakable_space_pattern, "\n", line)
    segments = line.split("\n")

    # join as many segments as it doesn't exceed line length limit
    line = segments[0]
    current_line_length = line_length(segments[0])
    for segment in segments[1:]:
        current_line_length += line_length(segment) + 1
        if current_line_length > column_limit:
            line = ("\n" + tabulation).join([line, segment])
            current_line_length = line_length(tabulation + segment)
        else:
            line = " ".join([line, segment])

    return line


def line_length(line: str) -> int:
    line = line.expandtabs(4)
    return len(line)


def indent_level(line: str) -> int:
    last_tab_occurance = line.rfind("\t")
    if last_tab_occurance < 0:
        return 0

    line = line[: (last_tab_occurance + 1)]
    return int(len(line.expandtabs(4)) / 4)
