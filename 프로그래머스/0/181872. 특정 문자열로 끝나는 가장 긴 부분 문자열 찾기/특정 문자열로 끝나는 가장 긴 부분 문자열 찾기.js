function solution(myString, pat) {
    var answer = '';
    var len = myString.length;
    for (let i = len-1; i<=len-1; i--){
        answer = myString.slice(0, i+1);
        if (answer.endsWith(pat)){
            return answer;
        }
    }
}