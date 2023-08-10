# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_hoist.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
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
    assert output == hoist(
        """\
void	*foo()
{
	if ()
		return NULL;
}
"""
    )

    # TODO test on weird types
    output = """\
void foo()
{
\tt_list\t*bar;

\tbar = (t_list *)malloc(sizeof(t_list) * (count_elements(baz) + 1));
}
"""
    assert output == hoist(
        """\
void foo()
{
\tt_list\t*bar = (t_list *)malloc(sizeof(t_list) * (count_elements(baz) + 1));
}
"""
    )


def test_hoist_empty_function():
    input = """
void empty_function(void)
{
}

int **function()
{
\tint **tab = malloc(4 * sizeof(int *));
\tint i = -1;
\twhile (++i < 4)
\t{
\t\ttab[i] = malloc(4 * sizeof(int));
\t\tint j = -1;
\t\twhile (++j < 4)
\t\t\ttab[i][j] = i * j;
\t}
\treturn (tab);
}
"""
    output = """
void empty_function(void)
{
}

int **function()
{
\tint\t**tab;
\tint\ti;
\tint\tj;

\ttab = malloc(4 * sizeof(int *));
\ti = -1;
\twhile (++i < 4)
\t{
\t\ttab[i] = malloc(4 * sizeof(int));
\t\tj = -1;
\t\twhile (++j < 4)
\t\t\ttab[i][j] = i * j;
\t}
\treturn (tab);
}
"""
    assert output == hoist(input)


def test_hoist_array_initialization():
    input = """
void foo(void)
{
\tint\txs[4] = {1, 2, 3, 4};
\txs[0] = -1;
}
"""
    output = """
void foo(void)
{
\tint\txs[4] = {1, 2, 3, 4};

\txs[0] = -1;
}
"""
    assert output == hoist(input)


def test_hoist_array_initialization_multiple_variable():
    input = """
void foo(void)
{
\tint\ta = 1;
\ta++;
\tint\txs[4] = {1, 2, 3, 4};
\txs[0] = -1;
\tint\tb = 2;
\tb++;
}
"""
    output = """
void foo(void)
{
\tint\ta;
\tint\txs[4] = {1, 2, 3, 4};
\tint\tb;

\ta = 1;
\ta++;
\txs[0] = -1;
\tb = 2;
\tb++;
}
"""
    assert output == hoist(input)


def test_hoist_array_initialization_issue_56_example():
    input = """
int main(void)
{
\tint\tlength;
\tint\tval;
\tint\tarray[] = {1, 2, 3, 4};
\tlength = sizeof(array) / sizeof(array[0]);
\tval = 2;
\treturn (0);
}
"""
    output = """
int main(void)
{
\tint\tlength;
\tint\tval;
\tint\tarray[] = {1, 2, 3, 4};

\tlength = sizeof(array) / sizeof(array[0]);
\tval = 2;
\treturn (0);
}
"""
    assert output == hoist(input)


@pytest.mark.skip()
def test_hoist_array():
    pass


@pytest.mark.skip()
def test_hoist_func_ptr():
    pass
