import re

from c_formatter_42.formatters import helper


def line_breaker(content: str, column_limit: int = 80) -> str:
    lines = content.split("\n")
    lines = [insert_break(line, column_limit) for line in lines]
    return "\n".join(lines)


def insert_break(line: str, column_limit: int) -> str:
    if line_length(line) <= column_limit:
        return line

    # Break at all breakable spaces (space after comma or space before binary
    # operators or logical AND or OR)
    breakable_space_pattern = r"((?<=,) | (?=[+\-*/%]|\|\||&&)(?!\*+\S|\+\+|\-\-))"
    line = re.sub(breakable_space_pattern, "\n", line)
    segments = line.split("\n")

    line_indent_level = indent_level(line)
    nest_indent_level = additional_nest_indent_level(line)

    # Join as many segments as it doesn't exceed line length limit
    line = segments[0]
    current_line_length = line_length(segments[0])
    for segment in segments[1:]:
        current_line_length += line_length(segment) + 1
        if current_line_length > column_limit:
            tabulation = "\t" * (
                line_indent_level + additional_indent_level(line, nest_indent_level)
            )
            line = ("\n" + tabulation).join([line, segment])
            current_line_length = line_length(tabulation + segment)
        else:
            line = " ".join([line, segment])

    return line


# The additional indent level increases in proportion to the corresponding parentheses depth
#
# Examples:
#   -----------------------------------------------------------------------------------
#   foo() * bar() * baz()
#   ~~~~~~~~~~~~~^~~~~~~~   When line breaks here,
#   foo() * bar()
#   >   * baz()             Next line should be indented with 1 tab (default)
#   -----------------------------------------------------------------------------------
#   foo(bar() * baz())
#   ~~~~~~~~~^~~~~~~~~      When line breaks here,
#   foo(bar()
#   >   * baz())            Next line should be indented with 1 tab (paren depth is 1)
#   -----------------------------------------------------------------------------------
#   (foo(bar() * baz()))
#   ~~~~~~~~~~^~~~~~~~~~    When line breaks here,
#   (foo(bar()
#   >   >   * baz()))       Next line should be indented with 2 tabs (paren depth is 2)
#   -----------------------------------------------------------------------------------
def additional_indent_level(s: str, nest_indent_level: int = 0) -> int:
    paren_depth = 0
    is_surrounded_sq = False
    is_surrounded_dq = False
    for c in s:
        if c == "'":
            is_surrounded_sq = not is_surrounded_sq
        elif c == '"':
            is_surrounded_dq = not is_surrounded_dq
        elif c == "(" and not is_surrounded_sq and not is_surrounded_dq:
            paren_depth += 1
        elif c == ")" and not is_surrounded_sq and not is_surrounded_dq:
            paren_depth -= 1

    if paren_depth > 0:
        return nest_indent_level + paren_depth
    else:
        return 1  # 1 is the default additional indent level


def additional_nest_indent_level(line: str) -> int:
    # An exceptional rule for variable assignment
    # https://github.com/42School/norminette/blob/921b5e22d991591f385e1920f7e7ee5dcf71f3d5/norminette/rules/check_assignation_indent.py#L59
    align_pattern = r"^\s*({decl})((\.|->){decl})*\s+=\s+(.|\n)*?;"
    align_pattern = align_pattern.format(decl=helper.REGEX_DECL_NAME)
    return 1 if re.match(align_pattern, line) is not None else 0


def line_length(line: str) -> int:
    line = line.expandtabs(4)
    return len(line)


def indent_level(line: str) -> int:
    # An exceptional rule for function declaration
    # https://github.com/42School/norminette/blob/921b5e22d991591f385e1920f7e7ee5dcf71f3d5/norminette/rules/check_assignation_indent.py#L61
    align_pattern = r"^(static\s+)?{type}\s+{name}\((.|\n)*?\);$"
    align_pattern = align_pattern.format(type=helper.REGEX_TYPE, name=helper.REGEX_NAME)
    if re.match(align_pattern, line):
        last_tab_index = line.rfind("\t")
        if last_tab_index == -1:
            return 0
        return line_length(line[: last_tab_index + 1]) // 4

    return line.count("\t")
