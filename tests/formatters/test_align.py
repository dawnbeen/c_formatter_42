# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_align.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:19:45 by cacharle          #+#    #+#              #
#    Updated: 2021/02/11 20:35:54 by charles          ###   ########.fr        #
#                                                                              #
# ############################################################################ #

import pytest

from c_formatter_42.formatters.align import align, align_scope, align_local, Scope


def test_align_global_basic():
    output = """\
int\t\tfoo();
char\tbar();
"""
    assert output == align_scope(
        """\
int foo();
char   bar();
""",
        scope=Scope.GLOBAL,
    )
    assert output == align_scope(
        """\
int\t\t\t\t\t\tfoo();
char   bar();
""",
        scope=Scope.GLOBAL,
    )
    assert output == align_scope(
        """\
int\t\t\t         \t\t\tfoo();
char  \t bar();
""",
        scope=Scope.GLOBAL,
    )
    assert output == align_scope(
        """\
int\t\t\t         \t\t\tfoo();
char  \t bar();
""",
        scope=Scope.GLOBAL,
    )


def test_align_local_basic():
    output = """
int foo()
{
\tint\t\tfoo;
\tchar\tbar;
}
"""

    assert output == align_local(
        """
int foo()
{
\tint foo;
\tchar   bar;
}
"""
    )
    assert output == align_local(
        """
int foo()
{
\tint\t\t\t\t\t\tfoo;
\tchar   bar;
}
"""
    )
    assert output == align_local(
        """
int foo()
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
"""
    )
    assert output == align_local(
        """
int foo()
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
"""
    )


def test_align_global_prototypes_basic():
    input = """
int                      a();
int   b();
int \t\t\t\tc();
int\t\t\t\t d();
int   e();
int \t\t\t\t\t\tf();
int \t\tg();
char    a();
char          b();
char    c();
char d();
char\t\t\t\te();
char\tf();
char\t\t\t\t\t\t\tg();
uint64_t\t\t\t\t\ta();
uint64_t  b();
uint64_t c();
uint64_t\t\t\t\t\t\t\t\t\t\td();
uint64_t\t\t\t\t\t\t\t\t\t\t\te();
uint64_t                  f();
uint64_t\tg();
"""
    output = """
int\t\t\ta();
int\t\t\tb();
int\t\t\tc();
int\t\t\td();
int\t\t\te();
int\t\t\tf();
int\t\t\tg();
char\t\ta();
char\t\tb();
char\t\tc();
char\t\td();
char\t\te();
char\t\tf();
char\t\tg();
uint64_t\ta();
uint64_t\tb();
uint64_t\tc();
uint64_t\td();
uint64_t\te();
uint64_t\tf();
uint64_t\tg();
"""
    assert output == align(input)


def test_align_local_multiple_functions():
    input = """
int\t\t\t\t\t\t\t\t\t\tf()
{
\tint a = 0;
}
int\t\t\t              g()
{
\tint a;
\tint    b;
\tint           a;
\tint                a;
\tchar   a;
}
char\t\t\t\t\t\t\t\t\ta()
{
\tint                                                        a;
\tint    b;
\tint           a;
\tint                a;
\tchar   a;
\tuint64_t              a;
}
char\t\t\t\tf()
{
\tt_very_looooooooooooooooooooooooooooooooooooooooooooooong yo;
\tint i;
}
char g()
{
}
uint64_t   a()
{
}
uint64_t\t\t\tb()
{
}
"""
    output = """
int\t\t\tf()
{
\tint a = 0;
}
int\t\t\tg()
{
\tint\t\ta;
\tint\t\tb;
\tint\t\ta;
\tint\t\ta;
\tchar\ta;
}
char\t\ta()
{
\tint\t\t\ta;
\tint\t\t\tb;
\tint\t\t\ta;
\tint\t\t\ta;
\tchar\t\ta;
\tuint64_t\ta;
}
char\t\tf()
{
\tt_very_looooooooooooooooooooooooooooooooooooooooooooooong\tyo;
\tint\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ti;
}
char\t\tg()
{
}
uint64_t\ta()
{
}
uint64_t\tb()
{
}
"""
    assert output == align(input)


def test_align_prototypes_type_spaces():
    input = """
unsigned foo();
unsigned int foo();
long foo();
long long foo();
long long int foo();
static long long int foo();
static short short int foo();
static short int foo();
"""
    output = """
unsigned\t\t\t\tfoo();
unsigned int\t\t\tfoo();
long\t\t\t\t\tfoo();
long long\t\t\t\tfoo();
long long int\t\t\tfoo();
static long long int\tfoo();
static short short int\tfoo();
static short int\t\tfoo();
"""
    assert output == align(input)


def test_align_local_type_spaces():
    input = """
int qq()
{
\tunsigned foo;
\tunsigned int foo;
\tlong foo;
\tlong long foo;
\tlong long int foo;
\tstatic long long int foo;
\tstatic short short int foo;
\tstatic short int foo;
\tregister long long int foo;
\tvolatile short short int foo;
}
"""
    output = """
int\tqq()
{
\tunsigned\t\t\t\t\tfoo;
\tunsigned int\t\t\t\tfoo;
\tlong\t\t\t\t\t\tfoo;
\tlong long\t\t\t\t\tfoo;
\tlong long int\t\t\t\tfoo;
\tstatic long long int\t\tfoo;
\tstatic short short int\t\tfoo;
\tstatic short int\t\t\tfoo;
\tregister long long int\t\tfoo;
\tvolatile short short int\tfoo;
}
"""
    assert output == align(input)


def test_align_local_type_array():
    input = """
int qq()
{
\tunsigned foo[2];
\tunsigned int foo[2][2];
\tlong foo[BUFFER_SIZE];
\tlong long foo[A][B][C];
\tlong long int foo[A][B][C];
\tstatic long long int foo[A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B];
\tstatic short short int foo[1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1];
\tregister long long int foo[10000000000000000000000000000000000000000];
\tvolatile short short int foo[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA];
\tvolatile short short int foo[TEST + 1];
\tvolatile short short int foo[TEST - 1];
\tvolatile short short int foo[TEST * 1];
\tvolatile short short int foo[TEST / 1];
\tvolatile short short int foo[TEST == 0 ? 1 : 0];
}
"""
    output = """
int\tqq()
{
\tunsigned\t\t\t\t\tfoo[2];
\tunsigned int\t\t\t\tfoo[2][2];
\tlong\t\t\t\t\t\tfoo[BUFFER_SIZE];
\tlong long\t\t\t\t\tfoo[A][B][C];
\tlong long int\t\t\t\tfoo[A][B][C];
\tstatic long long int\t\tfoo[A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B];
\tstatic short short int\t\tfoo[1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1];
\tregister long long int\t\tfoo[10000000000000000000000000000000000000000];
\tvolatile short short int\tfoo[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA];
\tvolatile short short int\tfoo[TEST + 1];
\tvolatile short short int\tfoo[TEST - 1];
\tvolatile short short int\tfoo[TEST * 1];
\tvolatile short short int\tfoo[TEST / 1];
\tvolatile short short int\tfoo[TEST == 0 ? 1 : 0];
}
"""
    assert output == align(input)


def test_align_ptr_type():
    input = """
int *ptr()
{
\tint *a;
\tint ******a;
\tint *****************a;
\tchar *****************a;
}
int ***********ptr();
char ***********ptr(char ********************a);
uint64_t ***********ptr(char ********************a);
"""
    output = """
int\t\t\t*ptr()
{
\tint\t\t*a;
\tint\t\t******a;
\tint\t\t*****************a;
\tchar\t*****************a;
}
int\t\t\t***********ptr();
char\t\t***********ptr(char ********************a);
uint64_t\t***********ptr(char ********************a);
"""
    assert output == align(input)


def test_align_function_ptr():
    input = """
int qa()
{
\tint *(*func)(int a, int b);
\tint (*func2)(int, int);
\tvoid (*func2)(int, int);
\tunsigned long long int (*func2)();
\tunsigned long long int (*func2)(void*);
\tunsigned long long int (*func2)(void**********);
}
"""
    output = """
int\tqa()
{
\tint\t\t\t\t\t\t*(*func)(int a, int b);
\tint\t\t\t\t\t\t(*func2)(int, int);
\tvoid\t\t\t\t\t(*func2)(int, int);
\tunsigned long long int\t(*func2)();
\tunsigned long long int\t(*func2)(void*);
\tunsigned long long int\t(*func2)(void**********);
}
"""
    assert output == align(input)


def test_align_function_ptr_array():
    input = """
int qa()
{
\tint *(*func[2])(int a, int b);
\tint (*func2[A])(int, int);
\tvoid (*func2[11111111111110000000000000000000])(int, int);
\tunsigned long long int (*func2[aaaaaaaaaaaaaaaaaaaaaaaaaa])();
}
"""
    output = """
int\tqa()
{
\tint\t\t\t\t\t\t*(*func[2])(int a, int b);
\tint\t\t\t\t\t\t(*func2[A])(int, int);
\tvoid\t\t\t\t\t(*func2[11111111111110000000000000000000])(int, int);
\tunsigned long long int\t(*func2[aaaaaaaaaaaaaaaaaaaaaaaaaa])();
}
"""
    assert output == align(input)


def test_align_global_variable():
    input = """
int g_a = 1;
char f();
"""
    output = """
int\t\tg_a = 1;
char\tf();
"""
    assert output == align(input)


def test_align_number_label():
    input = """
uint64_t foo64()
{
\tuint64_t foo64;
\tc5 foo65;
}
"""
    output = """
uint64_t\tfoo64()
{
\tuint64_t\tfoo64;
\tc5\t\t\tfoo65;
}
"""
    assert output == align(input)


def test_align_underscore():
    input = """
____ ___()
{
\t______ __fgffd234__;
\t_ ____;
}
"""
    output = """
____\t___()
{
\t______\t__fgffd234__;
\t_\t\t____;
}
"""
    print(align(input))
    assert output == align(input)


def test_align_struct():
    input = """
struct s_bonjour
{
\tint a;
\tchar b;
};
int f();
"""
    output = """
struct\t\ts_bonjour
{
\tint\t\ta;
\tchar\tb;
};
int\t\t\tf();
"""
    assert output == align(input)


def test_align_enum():
    input = """
enum e_bonjour
{
\tBONJOUR_A,
\tBONJOUR_B,
};
int f();
"""
    output = """
enum\te_bonjour
{
\tBONJOUR_A,
\tBONJOUR_B,
};
int\t\tf();
"""
    assert output == align(input)


def test_align_union():
    input = """
union u_bonjour
{
\tint a;
\tchar b;
};
int f();
"""
    output = """
union\t\tu_bonjour
{
\tint\t\ta;
\tchar\tb;
};
int\t\t\tf();
"""
    assert output == align(input)


def test_align_typedef():
    input = """
typedef struct s_bonjour
{
\tint a;
\tchar b;
} t_bonjour;
int f();
"""
    output = """
typedef struct s_bonjour
{
\tint\t\ta;
\tchar\tb;
}\t\t\tt_bonjour;
int\t\t\tf();
"""
    assert output == align(input)
    input = """
typedef enum e_bonjour
{
\tBONJOUR_A,
\tBONJOUR_B,
} t_bonjour;
int f();
"""
    output = """
typedef enum e_bonjour
{
\tBONJOUR_A,
\tBONJOUR_B,
}\tt_bonjour;
int\tf();
"""
    assert output == align(input)
    input = """
typedef union u_bonjour
{
\tint a;
\tchar b;
} t_bonjour;
int f();
"""
    output = """
typedef union u_bonjour
{
\tint\t\ta;
\tchar\tb;
}\t\t\tt_bonjour;
int\t\t\tf();
"""
    assert output == align(input)


def test_align_typedef_anonymous():
    input = """
typedef struct
{
\tint a;
\tchar b;
} t_bonjour;
int f();
"""
    output = """
typedef struct
{
\tint\t\ta;
\tchar\tb;
}\t\t\tt_bonjour;
int\t\t\tf();
"""
    assert output == align(input)
    input = """
typedef enum
{
\tBONJOUR_A,
\tBONJOUR_B,
} t_bonjour;
int f();
"""
    output = """
typedef enum
{
\tBONJOUR_A,
\tBONJOUR_B,
}\tt_bonjour;
int\tf();
"""
    assert output == align(input)
    input = """
typedef union
{
\tint a;
\tchar b;
} t_bonjour;
int f();
"""
    output = """
typedef union
{
\tint\t\ta;
\tchar\tb;
}\t\t\tt_bonjour;
int\t\t\tf();
"""
    assert output == align(input)


@pytest.mark.skip()
def test_align_nested_typedecl():
    input = """
struct s_bonjour
{
\tint a;
\tchar b;
\tunion
\t{
\t\tint a;
\t\tchar b;
\t} u;
};
int f();
"""
    output = """
struct\t\t\ts_bonjour
{
\tint\t\t\ta;
\tchar\t\tb;
\tunion
\t{
\t\tint\t\ta;
\t\tchar\tb;
\t}\t\t\tu;
};
int\t\t\t\tf();
"""
    assert output == align(input)


def test_align_struct_field_array():
    input = """
struct s_bonjour
{
\tint a[1];
\tchar b[0][1][2][ASDF + 1];
};
int f();
"""
    output = """
struct\t\ts_bonjour
{
\tint\t\ta[1];
\tchar\tb[0][1][2][ASDF + 1];
};
int\t\t\tf();
"""
    assert output == align(input)


def test_align_struct_field_func_ptr():
    input = """
struct s_bonjour
{
\tint *(*a[1])(int);
\tchar (*b[0][1][2][ASDF])(int a, char buf[2048], t_type);
};
int f();
"""
    output = """
struct\t\ts_bonjour
{
\tint\t\t*(*a[1])(int);
\tchar\t(*b[0][1][2][ASDF])(int a, char buf[2048], t_type);
};
int\t\t\tf();
"""
    assert output == align(input)


def test_align_struct_field_array_func_ptr():
    input = """
struct s_bonjour
{
\tint *(*a[1])(int);
\tchar (*b[0][1][2][ASDF])(int a, char buf[2048], t_type);
};
int f();
"""
    output = """
struct\t\ts_bonjour
{
\tint\t\t*(*a[1])(int);
\tchar\t(*b[0][1][2][ASDF])(int a, char buf[2048], t_type);
};
int\t\t\tf();
"""
    assert output == align(input)


def test_align_struct_singleton():
    input = """
struct s_bonjour;
int f();
char f2();
"""
    output = """
struct s_bonjour;
int\t\tf();
char\tf2();
"""
    assert output == align(input)


def test_align_union_singleton():
    input = """
union s_bonjour;
int f();
char f2();
"""
    output = """
union s_bonjour;
int\t\tf();
char\tf2();
"""
    assert output == align(input)


def test_align_enum_singleton():
    input = """
enum s_bonjour;
int f();
char f2();
"""
    output = """
enum s_bonjour;
int\t\tf();
char\tf2();
"""
    assert output == align(input)


def test_align_multiline_func_decl():
    input = """
t_parsed *parse_pipeline(t_tok_lst *input)
static t_parsed *st_parse_op_build(
\t\t\tt_parsed *left, t_parsed *right, enum e_tok sep_tag)
"""
    output = """
t_parsed\t\t*parse_pipeline(t_tok_lst *input)
static t_parsed\t*st_parse_op_build(
\t\t\tt_parsed *left, t_parsed *right, enum e_tok sep_tag)
"""
    assert output == align(input)


def test_align_global_array():
    input = """
static char *g_sep_str_lookup[] = {};
static t_parsed *st_parse_op_build(t_parsed *left)
"""
    output = """
static char\t\t*g_sep_str_lookup[] = {};
static t_parsed\t*st_parse_op_build(t_parsed *left)
"""
    assert output == align(input)


def test_align_func_typedef():
    input = """
typedef void *(*t_routine)(void *arg);

unsigned long long int foo();
int bar();
"""
    output = """
typedef void\t\t\t*(*t_routine)(void *arg);

unsigned long long int\tfoo();
int\t\t\t\t\t\tbar();
"""
    assert output == align(input)
