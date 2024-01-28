use std::io;
use std::convert::TryFrom;

fn main() {
    let mut tickets: [u16; 7] = Default::default();
    let mut total = 0;
    for i in 0..7 {
        let mut input = String::new();
        println!("Enter da numba of da ticket for da day {}: ", i + 1);
        io::stdin().read_line(&mut input).unwrap();

        let ticket = input.trim().parse::<u16>().unwrap();
        total += ticket;
        tickets[i] = ticket;
    }

    let average = total / 7;
    let mut min: usize = 0;
    let mut max: usize = 0;

    for i in 0..7 {
        let num: usize = i as usize;
        if tickets[num] < tickets[min] {
            min = num;
        }
        if tickets[num] > tickets[max] {
            max = num;
        }
    }

    println!("Average: {}", average);
    println!("Min: {} (day {})", tickets[min], min + 1);
    println!("Max: {} (day {})", tickets[max], max + 1);
}
