# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_return_type_single_tab.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/09 10:28:30 by charles           #+#    #+#              #
#    Updated: 2022/01/09 10:28:30 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import pytest

from c_formatter_42.formatters.return_type_single_tab import return_type_single_tab


def test_return_type_single_tab_basic():
    output = """\
int\tfoo()
char\tbar()
"""
    assert output == return_type_single_tab("""\
int foo()
char   bar()
""")
    assert output == return_type_single_tab("""\
int\t\t\t\t\t\tfoo()
char   bar()
""")
    assert output == return_type_single_tab("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""")
    assert output == return_type_single_tab("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""")


@pytest.mark.parametrize(
    "content",
    [
        """
int foo();
char   bar();
        """,
        """
int\t\t\t\t\t\tfoo();
char   bar();
        """,
        """
int\t\t\t         \t\t\tfoo();
char  \t bar();
        """,
        """
int\t\t\t         \t\t\tfoo();
char  \t bar();
        """,
    ]
)
def test_return_type_single_tab_no_prototype(content):
    assert content == return_type_single_tab(content)


def test_return_type_single_tab_no_func_typedef():
    input = """
typedef void\t\t\t\t\t*(*t_routine)(void *arg);

unsigned long long int foo();
int foo();
"""
    assert input == return_type_single_tab(input)
