// The six programs of the diagnostics table in Rust, with the standard library
// only. Every one compiles with no warning, and the borrow checker accepts it:
// none has a data race, and its answer can still change from one run to the
// next.
//
//   diagnose pool|senders|poll|ticket|clock|ccall
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::mpsc::{self, TryRecvError};
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Instant;

fn pool() -> f64 {
    let (tx, rx) = mpsc::sync_channel::<f64>(16);
    let rx = Arc::new(Mutex::new(rx));
    let workers: Vec<_> = (0..4)
        .map(|_| {
            let rx = Arc::clone(&rx);
            thread::spawn(move || {
                let mut s = 0.0;
                loop {
                    let next = rx.lock().unwrap().recv();
                    match next {
                        Ok(v) => s = s * 0.5 + v,
                        Err(_) => return s,
                    }
                }
            })
        })
        .collect();
    for i in 0..10000 {
        tx.send(i as f64 * 0.1).unwrap();
    }
    drop(tx);
    workers.into_iter().map(|w| w.join().unwrap()).fold(0.0, |r, s| r * 3.0 + s)
}

fn senders() -> f64 {
    let (tx, rx) = mpsc::sync_channel::<f64>(16);
    for base in [1.0, 2.0] {
        let tx = tx.clone();
        thread::spawn(move || {
            for i in 0..5000 {
                tx.send(base + i as f64 * 0.001).unwrap();
            }
        });
    }
    drop(tx);
    rx.iter().fold(0.0, |s, v| s * 0.5 + v)
}

fn poll() -> f64 {
    let (tx, rx) = mpsc::sync_channel::<u64>(16);
    let producer = thread::spawn(move || {
        for i in 0..10000 {
            tx.send(i).unwrap();
        }
    });
    let (mut got, mut empty) = (0u64, 0u64);
    while got < 10000 {
        match rx.try_recv() {
            Ok(_) => got += 1,
            Err(TryRecvError::Empty) => empty += 1,
            Err(TryRecvError::Disconnected) => break,
        }
    }
    producer.join().unwrap();
    empty as f64
}

fn ticket() -> f64 {
    let counter = Arc::new(AtomicU64::new(0));
    let drawn: Vec<u64> = (0..16)
        .map(|_| {
            let counter = Arc::clone(&counter);
            thread::spawn(move || counter.fetch_add(1, Ordering::SeqCst) + 1)
        })
        .collect::<Vec<_>>()
        .into_iter()
        .map(|t| t.join().unwrap())
        .collect();
    drawn.iter().fold(0u64, |h, &t| h.wrapping_mul(31).wrapping_add(t)) as f64
}

fn refine(x: f64) -> f64 {
    let start = Instant::now();
    let (mut guess, mut steps) = (x, 0u64);
    while start.elapsed().as_nanos() < 200_000 {
        guess = 0.5 * (guess + x / guess);
        steps += 1;
    }
    guess + steps as f64
}

fn seeded(n: u32) -> f64 {
    let mut z = std::process::id() as u64;
    for _ in 0..n {
        z = z.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
    }
    z as f64
}

fn main() {
    let what = std::env::args().nth(1).unwrap_or_default();
    let r = match what.as_str() {
        "pool" => pool(),
        "senders" => senders(),
        "poll" => poll(),
        "ticket" => ticket(),
        "clock" => refine(2.0),
        "ccall" => seeded(10),
        _ => {
            eprintln!("usage: diagnose pool|senders|poll|ticket|clock|ccall");
            std::process::exit(2);
        }
    };
    println!("{:?}", r);
}
