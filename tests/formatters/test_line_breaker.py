# from c_formatter_42.formatters.line_breaker import line_breaker, indent_level
from c_formatter_42.formatters.line_breaker import *

def test_line_indent_depth_basic_1():
    input = """\
\t\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
"""
    assert 3 == indent_level(input)

def test_line_indent_depth_basic_2():
    input = """\
looooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
"""
    assert 0 == indent_level(input)

def test_line_indent_depth_basic_3():
    input = """\
\t\t\t + 2 + 2 + 2\t
"""
    assert 4 == indent_level(input)


def test_insert_line_break_basic_1():
    output = """\
\t\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
\t\t\t\t+ 2 + 2 + 2;
"""
    assert output == line_breaker("""\
\t\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
""")

def test_insert_line_break_basic_2():
    output = """\
looooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
"""
    assert output == line_breaker("""\
looooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
""")

def test_insert_line_break_basic_3():
    output = """\
\t\t\t\treturn (fooooooooooooooooooooooooo(a, b, cccccccccccc,
\t\t\t\t\t\tddddddddddddd, eeeeeeeeeeeeeeee, fffffffffffffff,
\t\t\t\t\t\tgggggggggggg, hhhhhhhhhhhhhhhhhh));
"""
    assert output == line_breaker("""\
\t\t\t\treturn (fooooooooooooooooooooooooo(a, b, cccccccccccc, ddddddddddddd, eeeeeeeeeeeeeeee, fffffffffffffff, gggggggggggg, hhhhhhhhhhhhhhhhhh));
""")

def test_insert_line_break_basic_4():
    output = """\
void\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
\t\t\t+ 2 + 2 + 2;
"""
    assert output == line_breaker("""\
void\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
""")

def test_insert_line_break_basic_5():
    output = """\
int\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
\t\t\t+ 2 + 2;
"""
    assert output == line_breaker("""\
int\t\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
""")

def test_insert_line_break_basic_6():
    output = """\
int\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
\t\t+ 2 + 2;
"""
    assert output == line_breaker("""\
int\tlooooooooooooooooooooooong = 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2;
""")

def test_insert_line_break_basic_7():
    output = """\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhhh
"""
    assert output == line_breaker("""\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhhh
""")

def test_insert_line_break_basic_8():
    output = """\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhh
"""
    assert output == line_breaker("""\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh hhhhhhhhhhhhhhh
""")

def test_insert_line_break_basic_9():
    output = """\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
\t+ hhhhhhhhhhhhhh
"""
    assert output == line_breaker("""\
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh + hhhhhhhhhhhhhh
""")

def test_insert_line_break_basic_10():
    output = "aaaa\n\t+ b"
    assert output == line_breaker("aaaa + b", 7)

def test_insert_line_break_basic_11():
    output = "aaaa\n\t- b"
    assert output == line_breaker("aaaa - b", 7)

def test_insert_line_break_basic_12():
    output = "aaaa\n\t* b"
    assert output == line_breaker("aaaa * b", 7)

def test_insert_line_break_basic_13():
    output = "aaaa\n\t/ b"
    assert output == line_breaker("aaaa / b", 7)

def test_insert_line_break_basic_14():
    output = "aaaa\n\t% b"
    assert output == line_breaker("aaaa % b", 7)

def test_insert_line_break_basic_15():
    output = "aaaa\n\t+ *b"
    assert output == line_breaker("aaaa + *b", 7)

def test_insert_line_break_basic_16():
    output = "aaaa\n\t+ b*"
    assert output == line_breaker("aaaa + b*", 7)

def test_insert_line_break_basic_17():
    output = "aaaa\n\t* *b"
    assert output == line_breaker("aaaa * *b", 7)

def test_insert_line_break_basic_18():
    output = "aaaa\n\t* b*"
    assert output == line_breaker("aaaa * b*", 7)

def test_insert_line_break_basic_19():
    output = "aaaa*\n\t* b"
    assert output == line_breaker("aaaa* * b", 7)

def test_insert_line_break_basic_20():
    output = "*aaaa\n\t* b"
    assert output == line_breaker("*aaaa * b", 7)

def test_insert_line_break_basic_21():
    output = ",\n\taaaa *b"
    assert output == line_breaker(", aaaa *b", 7)

def test_insert_line_break_basic_22():
    output = ",\n\taaaa* b"
    assert output == line_breaker(", aaaa* b", 7)

def test_insert_line_break_basic_23():
    output = "foooooo(bar\n\t\t* baz)"
    assert output == line_breaker("foooooo(bar * baz)", 7)


def test_insert_line_break_long_function_declaration():
    input = """
static void\tst_merge_fields_in_curr(char *strs[3], t_tok_lst **curr, t_tok_lst *fields)
"""
    output = """
static void\tst_merge_fields_in_curr(char *strs[3], t_tok_lst **curr,
\t\tt_tok_lst *fields)
"""
    assert line_breaker(input) == output

def test_insert_line_break_control_statement_1():
    input = """\
\twhile (true + false)
"""
    output = """\
\twhile (true
\t\t+ false)
"""
    assert line_breaker(input, 7) == output

def test_insert_line_break_control_statement_2():
    input = """\
\tif (true + false)
"""
    output = """\
\tif (true
\t\t+ false)
"""
    assert line_breaker(input, 5) == output
