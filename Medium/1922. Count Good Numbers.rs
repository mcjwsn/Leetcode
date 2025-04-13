impl Solution {
    pub fn count_good_numbers(n: i64) -> i32 {

        fn modpow(mut val:i64, mut n:i64, modulo:i64) -> i64{
        let mut result :i64 = 1;
        val %= modulo;
        while n > 0{
            if n % 2 == 1{
                result = result * val % modulo;
            }
            val = val* val % modulo;
            n /= 2;
        }
        result
    }

        let mut result = modpow(20,n/2 as i64,1_000_000_007);
        if n % 2 == 1{
            result = 5 * result % 1_000_000_007;
        }
        result as i32
    }
}