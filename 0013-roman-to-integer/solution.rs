impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        

        let mut total:i32 = 0;

        let mut chars: Vec<char> = s.chars().collect();

        let mut i:usize = 0;


        while i < chars.len() {


            match chars.get(i) {

                Some(&c) => {

                    match c {
                        'M' => total += 1000,
                        'D' => total += 500,
                        'C' => {
                            if i + 1 < chars.len() && chars[i + 1] == 'M' {
                                total += 900;
                                i += 1;
                            } else if i + 1 < chars.len() && chars[i + 1] == 'D' {
                                total += 400;
                                i += 1;
                            } else {
                                total += 100;
                            }
                        }
                        'L' => total += 50,
                        'X' => {
                            if i + 1 < chars.len() && chars[i + 1] == 'C' {
                                total += 90;
                                i += 1;
                            } else if i + 1 < chars.len() && chars[i + 1] == 'L' {
                                total += 40;
                                i += 1;
                            } else {
                                total += 10;
                            }
                        }
                        'V' => total += 5,
                        'I' => {
                            if i + 1 < chars.len() && chars[i + 1] == 'X' {
                                total += 9;
                                i += 1;
                            } else if i + 1 < chars.len() && chars[i + 1] == 'V' {
                                total += 4;
                                i += 1;
                            } else {
                                total += 1;
                            }
                        }
                        _ => println!("INVALID"),
                    }
                }
                None => println!("Index out of bounds"),
            }
            i += 1;
        }

        return total;

    }
}
