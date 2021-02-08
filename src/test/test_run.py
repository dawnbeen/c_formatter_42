# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_run.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/08 19:56:48 by charles           #+#    #+#              #
#    Updated: 2021/02/08 20:03:18 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from run import run_all

def test_run_align_break_column_max():
    input = """
typedef struct			s_tok_lst
{
	char				*content;
	struct s_tok_lst	*next;
	enum e_tok			tag;
}						t_tok_lst;

t_tok_lst				*tok_lst_new(enum e_tok tag, char *content);
t_tok_lst				*tok_lst_new_until(
							enum e_tok tag, char *content, size_t n);
t_tok_lst				*tok_lst_push_front(
							t_tok_lst **tokens, t_tok_lst *pushed);
t_tok_lst				*tok_lst_uncons(t_tok_lst **tokens);
"""
    output = """
typedef struct			s_tok_lst
{
	char				*content;
	struct s_tok_lst	*next;
	enum e_tok			tag;
}						t_tok_lst;

t_tok_lst				*tok_lst_new(enum e_tok tag, char *content);
t_tok_lst				*tok_lst_new_until(enum e_tok tag,
											char *content,
											size_t n);
t_tok_lst				*tok_lst_push_front(t_tok_lst **tokens,
											t_tok_lst *pushed);
t_tok_lst				*tok_lst_uncons(t_tok_lst **tokens);
"""
    assert output == run_all(input)
