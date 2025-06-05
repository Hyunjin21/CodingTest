function solution(s) {
    var answer = 0;
    const str = s.split(' ');
    for(let i=0; i<str.length; i++){
        if (str[i] == "Z"){
            answer -= str[i-1];
        } else {
            answer += Number(str[i]);
        }
    }
    return answer;
}