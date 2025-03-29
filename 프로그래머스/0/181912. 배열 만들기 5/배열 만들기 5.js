function solution(intStrs, k, s, l) {
    var answer = [];
    for(let i=0; i<intStrs.length; i++){
        var strs = Number(intStrs[i].slice(s, s+l));
        if (k < strs){
            answer.push(strs);
        }
    }
    return answer;
}