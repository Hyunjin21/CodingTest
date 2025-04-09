function solution(myString, pat) {
    var answer = 0;
    var plen = pat.length;
    for (let i = 0; i<=myString.length-plen; i++){
        if (myString.slice(i, i + plen) === pat){
            answer++;
        }
    }
    return answer;
}