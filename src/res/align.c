int                      a();
int   b();
int 				c();
int				 d();
int   e();
int 						f();
int 		g();
char    a();
char          b();
char    c();
char d();
char				e();
char	f();
char							g();
uint64_t					a();
uint64_t  b();
uint64_t c();
uint64_t										d();
uint64_t											e();
uint64_t                  f();
uint64_t	g();

int										f()
{
	int a = 0;
}
int			              g()
{
	int a;
	int    b;
	int           a;
	int                a;
	char   a;

}
char									a()
{
	int                                                        a;
	int    b;
	int           a;
	int                a;
	char   a;
	uint64_t              a;
}
char				f()
{
	t_very_looooooooooooooooooooooooooooooooooooooooooooooong yo;
	int i;
}
char g()
{

}
uint64_t   a()
{

}
uint64_t			b()
{

}


unsigned foo()
{
}
unsigned int foo()
{
}
long foo()
{
}
long long foo()
{
}
long long int foo()
{
}

static long long int foo()
{
}

static short short int foo()
{
}
static short int foo()
{
}

int qq()
{
	unsigned foo;
	unsigned int foo;
	long foo;
	long long foo;
	long long int foo;
	static long long int foo;
	static short short int foo;
	static short int foo;

	register long long int foo;
	volatile short short int foo;
}

int qq()
{
	unsigned foo[2];
	unsigned int foo[2][2];
	long foo[BUFFER_SIZE];
	long long foo[A][B][C];
	long long int foo[A][B][C];
	static long long int foo[A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C];
	static short short int foo[1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3];

	register long long int foo[10000000000000000000000000000000000000000];
	volatile short short int foo[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA];
}

int *ptr()
{
}

int ***********ptr()
{
}

int ***********ptr(char ********************a)
{
}

int qa()
{
	int (*func)(int a, int b);
	int (*func2)(int, int);
	void (*func2)(int, int);
	unsigned long long int (*func2)();
	unsigned long long int (*func2)(void*);
	unsigned long long int (*func2)(void**********);
}
