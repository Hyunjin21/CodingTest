function solution(n) {
    var answer = 0;
    if(n%2 != 0){
        for(var i=1; i<=n;){
            answer += i;
            i += 2;
        }
    } else if (n%2 == 0){
        for(var i=0; i<=n;){
            answer += i ** 2;
            i += 2;
        }
    }
    return answer;
}