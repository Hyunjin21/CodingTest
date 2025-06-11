function solution(array) {
    var answer = 0;
    let str = String(array.join('')).split('');
    for(let i = 0; i<str.length; i++){
        if(str[i] == '7'){
            answer++;
        }
    }
    return answer;
}