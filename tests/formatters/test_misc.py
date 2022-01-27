# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_misc.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/05 14:53:05 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 20:27:44 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from c_formatter_42.formatters.misc import (
    parenthesize_return,
    space_before_semi_colon,
    remove_multiline_condition_space,
    insert_void,
)


def test_run_space_before_semi_colon():
    assert "return ;" == space_before_semi_colon("return ;")
    assert "break ;" == space_before_semi_colon("break ;")
    assert "continue ;" == space_before_semi_colon("continue ;")


def test_run_parenthesize_return_1():
    assert "return (a);" == parenthesize_return("return a;")
    assert "return (a);" == parenthesize_return("return \n\na;")
    assert "return (a);" == parenthesize_return("return a\n\n;")
    assert "return (a);" == parenthesize_return("return \na\n;")
    assert "return (a);" == parenthesize_return("return    a   ;")
    assert "return (a);" == parenthesize_return("return \t\ta\t  ;")
    assert "return (a);" == parenthesize_return("return  a\n\t\n ;")
    assert "return (foo());" == parenthesize_return("return foo();")
    assert "return (foo());" == parenthesize_return("return \n\nfoo();")
    assert "return (foo());" == parenthesize_return("return foo()\n\n;")
    assert "return (foo());" == parenthesize_return("return \nfoo()\n;")
    assert "return;" == parenthesize_return("return;")
    assert "return ;" == parenthesize_return("return ;")
    assert "return ();" == parenthesize_return("return ();")
    assert "return (bar(a++ + ++b[34]);" == parenthesize_return(
        "return bar(a++ + ++b[34];"
    )
    assert "return (func(a, b));" == parenthesize_return("return func(a, b);")
    assert "return ((void *)p);" == parenthesize_return("return (void *)p;")
    assert "\t\treturn (NULL);" == parenthesize_return("\t\treturn NULL;")


def test_run_parenthesize_return_2():
    output = """\
return ;
return (NULL);
"""
    assert output == parenthesize_return("""\
return ;
return NULL;
""")


def test_run_space_in_condition():
    input = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t   input->tag & TAG_STICK &&
\t   input->next != NULL && input->next->tag & TAG_IS_STR)
    """
    output = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t\tinput->tag & TAG_STICK &&
\t\tinput->next != NULL && input->next->tag & TAG_IS_STR)
    """
    assert output == remove_multiline_condition_space(input)

    input = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t  input->tag & TAG_STICK &&
\t  input->next != NULL && input->next->tag & TAG_IS_STR)
    """
    output = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t\tinput->tag & TAG_STICK &&
\t\tinput->next != NULL && input->next->tag & TAG_IS_STR)
    """
    assert output == remove_multiline_condition_space(input)
    input = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t input->tag & TAG_STICK &&
\t input->next != NULL && input->next->tag & TAG_IS_STR)
    """
    output = """
while (input != NULL && input->tag & TAG_IS_STR &&
\t\tinput->tag & TAG_STICK &&
\t\tinput->next != NULL && input->next->tag & TAG_IS_STR)
    """
    assert output == remove_multiline_condition_space(input)


def test_insert_void():
    assert "int main()" == insert_void("int main()")
    assert "void func  ( )" == insert_void("void func  ( )")
    assert "int	main(void)" == insert_void("int	main()")
    assert "void	func  (void)" == insert_void("void	func  ( )")
    assert "void		func  (void)" == insert_void("void		func  ( )")
