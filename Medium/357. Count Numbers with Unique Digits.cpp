class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n==0){ return 1;}
        if(n==1){return 10;}
        if(n==2){return 9*9 + 10;}
        if(n==3){return 91 + 9*9*8;}
        if(n==4){return 91 + 9*9*8 + 9*9*8*7;}
        if(n==5){return 91 + 9*9*8 + 9*9*8*7 + 9*9*8*7*6;}
        if(n==6){return 91 + 9*9*8 + 9*9*8*7 + 9*9*8*7*6*6;}
        if(n==7){return 91 + 9*9*8 + 9*9*8*7 + 9*9*8*7*6*(1+5*(4+1));}
        return 91 + 9*9*8 + 9*9*8*7 + 9*9*8*7*6*(1+5*(1+4*(1+3)));
    }
};