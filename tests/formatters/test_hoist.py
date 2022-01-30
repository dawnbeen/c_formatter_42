# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_hoist.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         # +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:29:07 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 22:16:57 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import pytest

from c_formatter_42.formatters.hoist import hoist


def scoped(s):
    return "int foo()\n{\n" + s + "\n}\n"


def test_assignment_splitting():
    output = scoped("\tint\ta;\n\n\ta = 1;")
    assert output == hoist(scoped("\tint a = 1;"))
    assert output == hoist(scoped("\tint a                = 1;"))
    assert output == hoist(scoped("\tint a =                1;"))
    assert output == hoist(scoped("\tint a\t\t\t\t\t\t\t\t= 1;"))
    assert output == hoist(scoped("\tint a =\t\t\t\t\t\t\t\t1;"))
    assert output == hoist(scoped("\tint a\t\t    \t\t\t\t= 1;"))
    assert output == hoist(scoped("\tint a =\t\t\t    \t\t\t1;"))


def test_hoist():
    output = scoped("int a;\n\nfoo();\nbar();")
    assert output == hoist(scoped("foo();\nbar();\nint a;"))
    assert output == hoist(scoped("foo();\nint a;\nbar();"))


def test_remove_empty_line():
    input = """
int foo()
{
\tint\ta;

\ta = 1;

\tputs("bonjour");

}
"""
    output = """
int foo()
{
\tint\ta;

\ta = 1;
\tputs("bonjour");
}
"""
    assert output == hoist(input)

    input = """
int foo()
{

\tputs("bonjour");

}
"""
    output = """
int foo()
{
\tputs("bonjour");
}
"""
    assert output == hoist(input)

    input = """
int foo()
{
\tint a = 1;

\tputs("bonjour");

}
"""
    output = """
int foo()
{
\tint\ta;

\ta = 1;
\tputs("bonjour");
}
"""
    assert output == hoist(input)


def test_hoist_pointer():
    input = """
int foo()
{
\tint *a = 1;
}
"""
    output = """
int foo()
{
\tint\t*a;

\ta = 1;
}
"""
    assert output == hoist(input)


def test_hoist_ex():
    output = """\
void	*foo()
{
	if ()
		return NULL;
}
"""
    assert output == hoist("""\
void	*foo()
{
	if ()
		return NULL;
}
""")

# TODO test on weird types
    output = """\
void foo()
{
\tt_list\t*bar;

\tbar = (t_list *)malloc(sizeof(t_list) * (count_elements(baz) + 1));
}
"""
    assert output == hoist("""\
void foo()
{
\tt_list\t*bar = (t_list *)malloc(sizeof(t_list) * (count_elements(baz) + 1));
}
""")

@pytest.mark.skip()
def test_hoist_array():
    pass


@pytest.mark.skip()
def test_hoist_func_ptr():
    pass
