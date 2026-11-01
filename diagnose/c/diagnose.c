// The six programs of the diagnostics table in C, each the usual way of
// writing it. Every one compiles with -Wall -Wextra -pedantic and no warning,
// and its answer can change from one run to the next.
//
//   diagnose pool|senders|poll|ticket|clock|ccall
#include <pthread.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

// A queue of n values behind a mutex, the C stand-in for a channel.
enum { Cap = 16 };
struct queue {
  pthread_mutex_t lock;
  pthread_cond_t changed;
  double items[Cap];
  int head, count, closed;
};

static void put(struct queue *q, double v) {
  pthread_mutex_lock(&q->lock);
  while (q->count == Cap) pthread_cond_wait(&q->changed, &q->lock);
  q->items[(q->head + q->count++) % Cap] = v;
  pthread_cond_broadcast(&q->changed);
  pthread_mutex_unlock(&q->lock);
}

static void close_queue(struct queue *q) {
  pthread_mutex_lock(&q->lock);
  q->closed = 1;
  pthread_cond_broadcast(&q->changed);
  pthread_mutex_unlock(&q->lock);
}

// Waits for the next value; 0 when the queue is closed and empty.
static int take(struct queue *q, double *v) {
  pthread_mutex_lock(&q->lock);
  while (q->count == 0 && !q->closed) pthread_cond_wait(&q->changed, &q->lock);
  int got = q->count > 0;
  if (got) {
    *v = q->items[q->head];
    q->head = (q->head + 1) % Cap;
    q->count--;
    pthread_cond_broadcast(&q->changed);
  }
  pthread_mutex_unlock(&q->lock);
  return got;
}

// Answers at once: 0 when nothing is there yet.
static int try_take(struct queue *q, double *v) {
  pthread_mutex_lock(&q->lock);
  int got = q->count > 0;
  if (got) {
    *v = q->items[q->head];
    q->head = (q->head + 1) % Cap;
    q->count--;
    pthread_cond_broadcast(&q->changed);
  }
  pthread_mutex_unlock(&q->lock);
  return got;
}

static struct queue q = {PTHREAD_MUTEX_INITIALIZER, PTHREAD_COND_INITIALIZER, {0}, 0, 0, 0};

static double folded[4];

static void *work(void *arg) {
  double s = 0.0, v;
  while (take(&q, &v)) s = s * 0.5 + v;
  folded[(intptr_t)arg] = s;
  return NULL;
}

static double pool(void) {
  pthread_t t[4];
  for (intptr_t k = 0; k < 4; k++) pthread_create(&t[k], NULL, work, (void *)k);
  for (int i = 0; i < 10000; i++) put(&q, i * 0.1);
  close_queue(&q);
  for (int k = 0; k < 4; k++) pthread_join(t[k], NULL);
  double r = 0.0;
  for (int k = 0; k < 4; k++) r = r * 3.0 + folded[k];
  return r;
}

static void *produce(void *arg) {
  double base = *(double *)arg;
  for (int i = 0; i < 5000; i++) put(&q, base + i * 0.001);
  return NULL;
}

static double senders(void) {
  double one = 1.0, two = 2.0, s = 0.0, v;
  pthread_t a, b;
  pthread_create(&a, NULL, produce, &one);
  pthread_create(&b, NULL, produce, &two);
  for (int k = 0; k < 10000; k++) {
    take(&q, &v);
    s = s * 0.5 + v;
  }
  pthread_join(a, NULL);
  pthread_join(b, NULL);
  return s;
}

static void *produce_counts(void *arg) {
  (void)arg;
  for (int i = 0; i < 10000; i++) put(&q, i);
  return NULL;
}

static double poll_queue(void) {
  pthread_t a;
  pthread_create(&a, NULL, produce_counts, NULL);
  long got = 0, empty = 0;
  double v;
  while (got < 10000) {
    if (try_take(&q, &v)) got++;
    else empty++;
  }
  pthread_join(a, NULL);
  return (double)empty;
}

static atomic_ulong counter;
static unsigned long drawn[16];

static void *draw(void *arg) {
  drawn[(intptr_t)arg] = atomic_fetch_add(&counter, 1) + 1;
  return NULL;
}

static double ticket(void) {
  pthread_t t[16];
  for (intptr_t k = 0; k < 16; k++) pthread_create(&t[k], NULL, draw, (void *)k);
  for (int k = 0; k < 16; k++) pthread_join(t[k], NULL);
  unsigned long h = 0;
  for (int k = 0; k < 16; k++) h = h * 31 + drawn[k];
  return (double)h;
}

static double since_ns(struct timespec t0) {
  struct timespec t;
  clock_gettime(CLOCK_MONOTONIC, &t);
  return (t.tv_sec - t0.tv_sec) * 1e9 + (t.tv_nsec - t0.tv_nsec);
}

static double refine(double x) {
  struct timespec t0;
  clock_gettime(CLOCK_MONOTONIC, &t0);
  double guess = x;
  unsigned long steps = 0;
  while (since_ns(t0) < 200000) {
    guess = 0.5 * (guess + x / guess);
    steps++;
  }
  return guess + (double)steps;
}

static double seeded(int n) {
  uint64_t z = (uint64_t)getpid();
  for (int i = 0; i < n; i++) z = z * 6364136223846793005ULL + 1442695040888963407ULL;
  return (double)z;
}

int main(int argc, char **argv) {
  const char *what = argc > 1 ? argv[1] : "";
  double r;
  if (!strcmp(what, "pool")) r = pool();
  else if (!strcmp(what, "senders")) r = senders();
  else if (!strcmp(what, "poll")) r = poll_queue();
  else if (!strcmp(what, "ticket")) r = ticket();
  else if (!strcmp(what, "clock")) r = refine(2.0);
  else if (!strcmp(what, "ccall")) r = seeded(10);
  else {
    fprintf(stderr, "usage: diagnose pool|senders|poll|ticket|clock|ccall\n");
    return 2;
  }
  printf("%.17g\n", r);
  return 0;
}
