class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int cnt = 0;
        long int i = 1;
        while (i*i<=n){
            if (n%i==0){
                if (i%2==1){cnt++;}
                if (i!=(n/i) && (n/i)%2==1) {cnt++;}
                }
            i++;}
        return cnt;
    }
};