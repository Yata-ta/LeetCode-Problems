impl Solution {
    
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {


        let mut vect: Vec<i32> = Vec::new();

        for i in 0..nums.len() {
    
            
            for j in i + 1..nums.len(){ // cant use the same element twice
    
                if nums[i] + nums[j] == target {

                    vect.push(i as i32);
                    vect.push(j as i32);
                    return vect;    // exactly one solution,
                }
            }
        }

        return vect; // Return an empty vector if no two elements sum up to the target.
    }
}
