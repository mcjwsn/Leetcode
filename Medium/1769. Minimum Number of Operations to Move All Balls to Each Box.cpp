class Solution {
    public:
        vector<int> minOperations(string boxes) {
            int n = boxes.size();
            vector<int> T(n, 0);
            int cnt;
            for(int i=0;i<n;i++){
                cnt = 0;
                for(int j=0;j<n;j++){
                    if (boxes[j] == '1'){
                        cnt += abs(i-j);
                    }
                }
                T[i] = cnt;
            }
            return T;
        }
    };