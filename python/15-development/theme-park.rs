use std::io;

fn get_daily_totals() {
    let mut totals: [u16; 7] = Default::default();
    println!("Enter the number of visitors for each day...");
    for i in 0..7 {
        
    }
}

fn get_valid_inut(day: u8) {
    let mut input = String::new();
    print!("Enter tickets purchased for ");
    io::stdin().read_line(&mut input).unwrap();
    let ticket = input.trim().parse::<u16>().unwrap();
}

fn get_minimum(totals: [u16; 7]) {

}

fn get_weekday_by_index(index: u8) -> String {
    let values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    return values[index as usize].to_string();
}

