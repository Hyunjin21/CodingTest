function solution(n) {
    var answer = 0;
    for (let i = 2; i <= n; i++){
        let count = 0;
        for (let j = 0; j<=i; j++){
            if(i%j == 0) {
                count++;
            }
        }
        if(count>=3){
            answer++;
        }
    }
    return answer;
}