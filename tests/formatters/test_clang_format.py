# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_clang_format.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/05 07:37:20 by cacharle          #+#    #+#              #
#    Updated: 2021/02/25 19:10:23 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import os
import tempfile
from contextlib import contextmanager

from c_formatter_42.formatters.clang_format import clang_format


def test_clang_format_missing_closing_delimiter():
    assert clang_format("int main() {") == "int main()\n{"
    assert clang_format("int main() { int fd[2; }") == "int main()\n{ int fd[2;\n}"


def test_clang_format_gibberish():
    assert (clang_format("qwasfjkahskluhiouhcjkvzhxcklhvklxzhv") ==
            "qwasfjkahskluhiouhcjkvzhxcklhvklxzhv")
    assert (clang_format("qwa()sfahskl{}[]uhcjkvzhxcklhv[]xzhv") ==
            "qwa() sfahskl{}[] uhcjkvzhxcklhv[] xzhv")


def test_clang_format_empty():
    assert clang_format("") == ""


# def test_clang_format_dont_join_lines():
#     input = """
# if (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# \t|| bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb
# \t|| cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc)
# """
#     output = """
# if (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ||
# \tbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ||
# \tcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc)
# """
#     assert clang_format(input) == output
# 
#     input = """
# if (aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ||
# \tbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ||
# \tcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc)
# """
#     assert clang_format(input) == input
# 

def test_clang_format_non_array_assignment_packing():
    input = """
static char *g_sep_str_lookup[] = {
\t[TAG_END] = ";",
\t[TAG_OR] = "||",
\t[TAG_REDIR_IN] = "<",
\t[TAG_REDIR_APPEND] = ">>",
\t[TAG_PARENT_CLOSE] = ")",
\t[TAG_AND] = "&&",
\t[TAG_PIPE] = "|",
\t[TAG_REDIR_OUT] = ">",
\t[TAG_PARENT_OPEN] = "(",
};
"""
    assert clang_format(input) == input


@contextmanager
def change_temp_dir_context():
    tempdir = tempfile.mkdtemp("c_formatter_42")
    current = os.getcwd()
    os.chdir(tempdir)
    yield
    os.chdir(current)


def test_clang_format_config_file():
    with change_temp_dir_context():
        assert not os.path.exists(".clang-format")
        assert clang_format("int main() { return 0; }") == "int main()\n{\n\treturn 0;\n}"
        assert not os.path.exists(".clang-format")

    with change_temp_dir_context():
        with open(".clang-format", "w") as f:
            f.write("bonjour")
        assert clang_format("int main() { return 0; }") == "int main()\n{\n\treturn 0;\n}"
        assert os.path.exists(".clang-format")
        with open(".clang-format") as f:
            assert f.read() == "bonjour"
