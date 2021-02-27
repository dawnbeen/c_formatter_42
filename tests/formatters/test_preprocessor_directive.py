# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_preprocessor_directive.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: charles <me@cacharle.xyz>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/02/07 15:52:25 by charles           #+#    #+#              #
#    Updated: 2021/02/11 20:27:53 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from c_formatter_42.formatters.preprocessor_directive import preprocessor_directive


def test_preprocessor_directive_ifdef():
    input = """
#ifdef foo
#define foo 1
#endif
"""
    output = """
#ifdef foo
# define foo 1
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_ifndef():
    input = """
#ifndef foo
#define foo 1
#endif
"""
    output = """
#ifndef foo
# define foo 1
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_if():
    input = """
#if foo
#define foo 1
#endif
"""
    output = """
#if foo
# define foo 1
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_if_else():
    input = """
#if foo
#define foo 1
#else
#define foo 2
#endif
"""
    output = """
#if foo
# define foo 1
#else
# define foo 2
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_if_elif_else():
    input = """
#if foo
#define foo 1
#elif t1
#define foo 2
#elif t2
#define foo 3
#elif t3
#define foo 4
#else
#define foo 5
#endif
"""
    output = """
#if foo
# define foo 1
#elif t1
# define foo 2
#elif t2
# define foo 3
#elif t3
# define foo 4
#else
# define foo 5
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_random_indent():
    input = """
#                if foo
#define foo 1
#         elif t1
#   define foo 2
#     elif t2
#  define foo 3
#                elif t3
#     define foo 4
#       else
#define foo 5
#           endif
"""
    output = """
#if foo
# define foo 1
#elif t1
# define foo 2
#elif t2
# define foo 3
#elif t3
# define foo 4
#else
# define foo 5
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_nested():
    input = """
#if foo
#define a 1
#if bar
#define b 2
#else
#define c 3
#endif
#elif baz
#define d 4
#elif baz
#define e 5
#else
#define f 6
#endif
"""
    output = """
#if foo
# define a 1
# if bar
#  define b 2
# else
#  define c 3
# endif
#elif baz
# define d 4
#elif baz
# define e 5
#else
# define f 6
#endif
"""
    assert output == preprocessor_directive(input)


def test_preprocessor_directive_nested_10():
    input = """
#if a
#if b
#if c
#if d
#if e
#if f
#if g
#if h
#if i
#if j
#define foo 1
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
#endif
"""
    output = """
#if a
# if b
#  if c
#   if d
#    if e
#     if f
#      if g
#       if h
#        if i
#         if j
#          define foo 1
#         endif
#        endif
#       endif
#      endif
#     endif
#    endif
#   endif
#  endif
# endif
#endif
"""
    assert output == preprocessor_directive(input)
