function solution(n) {
    var answer = [];
    answer.push(n);
    while (n > 0){
        if(n === 1){
            break;
        } else {
            if(n%2 == 0){
                n = n/2;
                answer.push(n);
                continue;
            } else {
                n = 3*n + 1;
                answer.push(n);
                continue;
            }
        }
    }
    return answer;
}