function solution(n) {
    var num = 1;
    for (let i = 1; i<=n; i++){
        num *= i;
        if(num === n) {
            return i;
        } else if (num > n){
            return i-1;
        }
    }

}