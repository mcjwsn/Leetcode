public class Solution {
    public int NumberOfAlternatingGroups(int[] colors, int k) {
        int left = 0;
        int right = 0;
        int cnt = 0;
        int n = colors.Length;
        for(int i=1;i<n+k;i++){
            if (colors[i%n] == colors[(i-1)%n]){
                left = right - 1;
            }
            else{
                right += 1;
            }
            if (right - left >= k){cnt+=1;}
        }
        return cnt;
    }
}