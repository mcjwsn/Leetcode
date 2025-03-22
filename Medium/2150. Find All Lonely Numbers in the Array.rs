use std::collections::HashMap;

impl Solution {
    pub fn find_lonely(nums: Vec<i32>) -> Vec<i32> {
        let mut ve = Vec::new();
        let mut mp = HashMap::new();
        for v in &nums{ 
            *mp.entry(v).or_insert(0) += 1;
            }
        for (key,val) in &mp{
            if *val < 2 && !(mp.contains_key(&(**key+1))) && !(mp.contains_key(&(**key-1)))
            {
                ve.push(**key);
            }
        }
        ve
    }
}