# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_align.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:19:45 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 12:28:07 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from formatters.align import *


def test_align_global():
    output = """\
int\t\tfoo()
char\tbar()
"""

    assert output == align_scope("""\
int foo()
char   bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t\t\t\tfoo()
char   bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""", scope="global")


def test_align_local():
    output = """
{
\tint\t\tfoo;
\tchar\tbar;
}
"""

    assert output == align_local("""
{
\tint foo;
\tchar   bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t\t\t\tfoo;
\tchar   bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
""")
