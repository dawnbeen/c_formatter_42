# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_run.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/09 18:15:56 by cacharle          #+#    #+#              #
#    Updated: 2020/10/09 18:41:48 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from run import parenthesize_return, space_before_semi_colon


def test_run_space_before_semi_colon():
    assert space_before_semi_colon("return ;") == "return ;"
    assert space_before_semi_colon("break ;") == "break ;"
    assert space_before_semi_colon("continue ;") == "continue ;"


def test_run_parenthesize_return():
    assert parenthesize_return("return a;") == "return (a);"
    assert parenthesize_return("return \n\na;") == "return (a);"
    assert parenthesize_return("return a\n\n;") == "return (a);"
    assert parenthesize_return("return \na\n;") == "return (a);"
    assert parenthesize_return("return    a   ;") == "return (a);"
    assert parenthesize_return("return \t\ta\t  ;") == "return (a);"
    assert parenthesize_return("return  a\n\t\n ;") == "return (a);"
    assert parenthesize_return("return foo();") == "return (foo());"
    assert parenthesize_return("return \n\nfoo();") == "return (foo());"
    assert parenthesize_return("return foo()\n\n;") == "return (foo());"
    assert parenthesize_return("return \nfoo()\n;") == "return (foo());"
