# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_hoist.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:29:07 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 14:13:03 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #


from textwrap import dedent

from formatters.hoist import *


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
    pass
