# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_hoist.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:29:07 by cacharle          #+#    #+#              #
#    Updated: 2021/02/07 14:08:27 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #


from formatters.hoist import hoist


def scoped(s):
    return "\n{\n" + s + "\n}\n"


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
{
\tint\ta;

\ta = 1;

\tputs("bonjour");

}
"""
    output = """
{
\tint\ta;

\ta = 1;
\tputs("bonjour");
}
"""
    assert output == hoist(input)

    input = """
{

\tputs("bonjour");

}
"""
    output = """
{
\tputs("bonjour");
}
"""
    assert output == hoist(input)

    input = """
{
\tint a = 1;

\tputs("bonjour");

}
"""
    output = """
{
\tint\ta;

\ta = 1;
\tputs("bonjour");
}
"""
    assert output == hoist(input)


def test_hoist_pointer():
    input = """
{
\tint *a = 1;
}
"""
    output = """
{
\tint\t*a;

\ta = 1;
}
"""
    assert output == hoist(input)


# TODO test on weird types
