# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_run.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yaassila <yaassila@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/08 19:56:48 by charles           #+#    #+#              #
#    Updated: 2023/08/31 14:00:00 by yaassila         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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


@pytest.mark.timeout(15)
def test_function_call_in_comment():
    input = """
#include "libft.h"

/*
The  bzero()  function  erases  the data in the n bytes of the memory starting at the location pointed to by s, by writing zeros (bytes containing '\0') to that area.

The explicit_bzero() function performs the same task as bzero().  It differs from bzero() in  that  it  guarantees that compiler optimizations will not remove the erase operation if the compiler deduces that the operation is "un-necessary".
*/
void	bzero(void *s, size_t n)
{
                    unsigned char *ptr_s;
}
"""
    run_all(input)
