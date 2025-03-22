impl Solution {
    pub fn min_operations(mut nums: Vec<i32>) -> i32 {
        let mut start:usize = 0;
        let n:usize = nums.len();
        let mut cnt:i32 = 0;
        while (start < n - 2){
            if (nums[start] == 0)
            {
                nums[start] = 1;
                nums[start + 1]^=1; 
                nums[start + 2]^=1;
                cnt += 1;
            }
            start += 1;
        }
        if ( nums[n-2] == 0 || nums[n-1] == 0){
            return -1;
        }
        cnt
    }
}