# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_run.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/08 19:56:48 by charles           #+#    #+#              #
#    Updated: 2021/02/11 20:27:07 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import pytest

from c_formatter_42.run import run_all


@pytest.mark.skip()
def test_run_align_break_column_max():
    input = """
typedef struct\t\t\ts_tok_lst
{
\tchar\t\t\t\t*content;
\tstruct s_tok_lst\t*next;
\tenum e_tok\t\t\ttag;
}\t\t\t\t\t\tt_tok_lst;

t_tok_lst\t\t\t\t*tok_lst_new(enum e_tok tag, char *content);
t_tok_lst\t\t\t\t*tok_lst_new_until(
\t\t\t\t\t\t\tenum e_tok tag, char *content, size_t n);
t_tok_lst\t\t\t\t*tok_lst_push_front(
\t\t\t\t\t\t\tt_tok_lst **tokens, t_tok_lst *pushed);
t_tok_lst\t\t\t\t*tok_lst_uncons(t_tok_lst **tokens);
"""
    output = """
typedef struct\t\t\ts_tok_lst
{
\tchar\t\t\t\t*content;
\tstruct s_tok_lst\t*next;
\tenum e_tok\t\t\ttag;
}\t\t\t\t\t\tt_tok_lst;

t_tok_lst\t\t\t\t*tok_lst_new(enum e_tok tag, char *content);
t_tok_lst\t\t\t\t*tok_lst_new_until(enum e_tok tag,
\t\t\t\t\t\t\t\t\t\t\tchar *content,
\t\t\t\t\t\t\t\t\t\t\tsize_t n);
t_tok_lst\t\t\t\t*tok_lst_push_front(t_tok_lst **tokens,
\t\t\t\t\t\t\t\t\t\t\tt_tok_lst *pushed);
t_tok_lst\t\t\t\t*tok_lst_uncons(t_tok_lst **tokens);
"""
    assert output == run_all(input)


def test_run_func_decl_single_tab_and_global_aligned():
    pass


def test_run_long_aligned_func_decl():
    # This function declaration is already aligned and should not be modified
    input = """
typedef struct s_foo
{
\tlong int\tbar;
}\t\t\t\tt_foo;

long int\t\tfoooooooooooooooooooooooooooooo(t_foo *foooooooo1,
\t\t\t\t\tt_foo *foooooooo2, int barrrrrrrr1, int barrrrrrrr2);
"""
    assert input == run_all(input)


def test_basic():
    input = """
int main(int argc, char*argv[]){
	return 0;
}
"""
    output = """
int\tmain(int argc, char *argv[])
{
	return (0);
}
"""
    assert output == run_all(input)
