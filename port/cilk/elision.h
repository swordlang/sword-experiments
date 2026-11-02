/*
 * The Cilk-5 library as the serial elision of a program sees it: one
 * worker, no clock, locks that are never contended. Included in place of
 * <cilk-lib.cilkh> by run.sh.
 */
#include <stdio.h>
#include <stdlib.h>
#include <alloca.h>
#include <string.h>

#define cilk_main main
#define Cilk_alloca alloca
#define Cilk_active_size 1
#define Self 0
#define SYNCHED 1
#define Cilk_exit(ret) exit(ret)
#define Cilk_die(msg) (fprintf(stderr, "%s", msg), exit(1))
#define Cilk_assert(ex) ((void)0)

typedef long long Cilk_time;
#define Cilk_get_wall_time() 0LL
#define Cilk_wall_time_to_sec(t) 0.0
#define Cilk_time_to_sec(t) 0.0
#define Cilk_user_work 0LL
#define Cilk_user_critical_path 0LL

typedef volatile int Cilk_lockvar[1];
#define Cilk_lock_init(v) ((void)0)
#define Cilk_lock(v) ((void)0)
#define Cilk_unlock(v) ((void)0)

int Cilk_rand(void);
void Cilk_srand(unsigned int seed);
