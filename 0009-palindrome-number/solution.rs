impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        
        if x < 0 {
            return false; // Negative numbers cant be palindromes
        }

        let mut x = x;
        let mut digits:Vec<i16> = Vec::new();
        let mut i:i16 = 0;

        while (x > 0){
              
            let digit:i16 = (x % 10) as i16;
            x /= 10;

            digits.push(digit);
            i += 1;
        }

        let length = digits.len();

        for i in 0..length{

            if !(digits[i] == digits[length - i - 1]){
                return false;
            }
        }
        return true;

        
    }
}
