import re


def line_breaker(content: str, column_limit: int = 80) -> str:
    lines = content.split("\n")
    lines = list(map(lambda s: insert_break(s, column_limit), lines))

    return "\n".join(lines)


def insert_break(line: str, column_limit: int) -> str:
    if line_length(line) <= column_limit:
        return line

    # break at all breakable spaces (space after comma or space before binary operators)
    breakable_space_pattern = r"((?<=,) | (?=[+\-*/%])(?!\*+\S|\+\+|\-\-))"
    line = re.sub(breakable_space_pattern, "\n", line)
    segments = line.split("\n")

    # additional indent level increases in proportion to corresponds paren depth
    #
    # (examples)
    # foo() * bar() * baz()
    # ~~~~~~~~~~~~~^~~~~~~~ when line breaks here,
    # foo() * bar()
    # >   * baz()           next line should be indented with 1 tab
    # ===
    # (foo(bar() * baz()))
    # ~~~~~~~~~~^~~~~~~~~    when line breaks here,
    # (foo(bar()
    # >   >   >   * baz()))  next line should be indented with 3 tabs

    line_indent_level = indent_level(line)

    # join as many segments as it doesn't exceed line length limit
    line = segments[0]
    current_line_length = line_length(segments[0])
    for segment in segments[1:]:
        current_line_length += line_length(segment) + 1
        if current_line_length > column_limit:
            tabulation = "\t" * (line_indent_level + additional_indent_level(line))
            line = ("\n" + tabulation).join([line, segment])
            current_line_length = line_length(tabulation + segment)
        else:
            line = " ".join([line, segment])

    return line


def additional_indent_level(s: str) -> int:
    additional_indent_level = 1
    is_surrounded_sq = False
    is_surrounded_dq = False

    for c in s:
        if c == "'":
            is_surrounded_sq = not is_surrounded_sq
        elif c == '"':
            is_surrounded_dq = not is_surrounded_dq
        elif c == "(" and not is_surrounded_sq and not is_surrounded_dq:
            additional_indent_level += 1
        elif c == ")" and not is_surrounded_sq and not is_surrounded_dq:
            additional_indent_level -= 1

    return additional_indent_level


def line_length(line: str) -> int:
    line = line.expandtabs(4)
    return len(line)


def indent_level(line: str) -> int:
    return line.count("\t")
