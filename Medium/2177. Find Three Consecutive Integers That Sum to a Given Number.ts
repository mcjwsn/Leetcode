function sumOfThree(num: number): number[] {
    if(num % 3 !== 0){return [];}
    const n = Math.floor(num / 3);
    return [n-1,n,n+1];
};