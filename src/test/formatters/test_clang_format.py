# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_clang_format.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/05 07:37:20 by cacharle          #+#    #+#              #
#    Updated: 2020/10/05 07:43:20 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from formatters.clang_format import clang_format


def test_clang_format_missing_closing_delimiter():
    assert clang_format("int main() {") == "int main()\n{"
    assert clang_format("int main() { int fd[2; }") == "int main()\n{ int fd[2;\n}"


def test_clang_format_gibberish():
    assert clang_format("qwasfjkahskluhiouhcjkvzhxcklhvklxzhv") == "qwasfjkahskluhiouhcjkvzhxcklhvklxzhv"
    assert clang_format("qwa()sfahskl{}[]uhcjkvzhxcklhv[]xzhv") == "qwa() sfahskl{}[] uhcjkvzhxcklhv[] xzhv"


def test_clang_format_empty():
    assert clang_format("") == ""
