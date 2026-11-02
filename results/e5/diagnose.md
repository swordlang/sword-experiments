## Answers in repeated runs

Distinct answers out of the runs; *refused* means it did not compile.

| program | language | gh-linux-arm64 | gh-linux-x86_64 | gh-macos-arm64 |
|---|---|---:|---:|---:|
| pool | sword-det | refused | refused | refused |
| pool | sword | 20 of 20 | 20 of 20 | 20 of 20 |
| pool | c | 20 of 20 | 20 of 20 | 20 of 20 |
| pool | rust | 20 of 20 | 20 of 20 | 20 of 20 |
| senders | sword-det | refused | refused | refused |
| senders | sword | 2 of 20 | 2 of 20 | 3 of 20 |
| senders | c | 2 of 20 | 4 of 20 | 3 of 20 |
| senders | rust | 4 of 20 | 2 of 20 | 7 of 20 |
| poll | sword-det | refused | refused | refused |
| poll | sword | 20 of 20 | 20 of 20 | 20 of 20 |
| poll | c | 20 of 20 | 20 of 20 | 20 of 20 |
| poll | rust | 20 of 20 | 20 of 20 | 20 of 20 |
| ticket | sword-det | refused | refused | refused |
| ticket | sword | 7 of 20 | 10 of 20 | 5 of 20 |
| ticket | c | 4 of 20 | 5 of 20 | 14 of 20 |
| ticket | rust | 17 of 20 | 20 of 20 | 20 of 20 |
| clock | sword-det | refused | refused | refused |
| clock | sword | 19 of 20 | 11 of 20 | 18 of 20 |
| clock | c | 13 of 20 | 7 of 20 | 15 of 20 |
| clock | rust | 19 of 20 | 10 of 20 | 9 of 20 |
| ccall | sword-det | refused | refused | refused |
| ccall | sword | 20 of 20 | 20 of 20 | 20 of 20 |
| ccall | c | 20 of 20 | 20 of 20 | 20 of 20 |
| ccall | rust | 20 of 20 | 20 of 20 | 20 of 20 |

Warnings from the compilers that accepted them: none.

## What Sword says with det

From gh-linux-arm64; the messages are the same on every platform.

```
== pool.sword
pool.sword:22:5: error: 'spread' is marked det, but what it answers can depend on more than its arguments
pool.sword:24:5: note: spread lets more than one task at a time receive from channel 'jobs'
== senders.sword
senders.sword:22:5: error: 'merged' is marked det, but what it answers can depend on more than its arguments
senders.sword:25:5: note: merged lets more than one task at a time send on channel 'ch'
== poll.sword
poll.sword:26:5: error: 'polled' is marked det, but what it answers can depend on more than its arguments
poll.sword:31:20: note: polled calls drain, which is not det
poll.sword:17:27: note: drain asks channel 'ch' something only the timing knows (TryRecv)
== ticket.sword
ticket.sword:10:5: error: 'tickets' is marked det, but what it answers can depend on more than its arguments
ticket.sword:14:23: note: tickets calls draw, which is not det
ticket.sword:7:26: note: draw reads or writes an atomic
== clock.sword
clock.sword:7:5: error: 'refine' is marked det, but what it answers can depend on more than its arguments
clock.sword:8:22: note: refine calls time.Now, which is not det
std/time/time.sword:67:39: note: time.Now calls out of the language
== ccall.sword
ccall.sword:7:5: error: 'seeded' is marked det, but what it answers can depend on more than its arguments
ccall.sword:8:24: note: seeded calls out of the language
```
