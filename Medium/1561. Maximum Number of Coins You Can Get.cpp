class Solution {
    public:
        int maxCoins(vector<int>& piles) {
            int cnt = 0;
            int start = 0;
            int end = piles.size();
            sort(piles.begin(),piles.end());
            while (start < end) { 
                end -= 2;
                start += 1;
                cnt += piles[end];
            }
            return cnt;
    }};