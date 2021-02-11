# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_run.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/08 19:56:48 by charles           #+#    #+#              #
#    Updated: 2021/02/10 18:45:30 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import pytest

from run import run_all


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
