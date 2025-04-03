use std::cmp;
impl Solution {
    pub fn maximum_triplet_value(nums: Vec<i32>) -> i64 {
        let mut el:i64 = 0;
        let mut diff:i64 = 0;
        let mut trip:i64 = 0;
        for i in 0..nums.len() {
            trip = cmp::max(trip, (diff * nums[i] as i64));
            diff = cmp::max(diff,el - nums[i] as i64);
            el = cmp::max(el,nums[i] as i64);  
        }
        trip
    }
}