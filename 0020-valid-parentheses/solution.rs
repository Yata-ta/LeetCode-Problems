impl Solution {
    pub fn is_valid(s: String) -> bool {
        


        // open brackets
        // (    [   {


        // close brackets
        // )    ]   }

        let mut stack: Vec <char> = Vec::new();

        for character in s.chars(){


            match character{

                '(' => stack.push('('),
                '[' => stack.push('['),
                '{' => stack.push('{'),
                
                ')' => if (stack.pop() != Some('(')){return false},
                ']' => if (stack.pop() != Some('[')){return false},
                '}' => if (stack.pop() != Some('{')){return false},
                      
                _ => return false
           }
        }


        if (stack.is_empty()){
            return true
        }
        return false

    }
}
