function solution(myString) {
    var answer = '';
    answer = myString.replaceAll(/[a-k]/g, 'l');
    return answer;
}