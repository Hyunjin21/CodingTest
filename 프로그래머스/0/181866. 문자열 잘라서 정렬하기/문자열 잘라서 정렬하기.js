function solution(myString) {
    var answer = [];
    answer = myString.split('x').filter(Boolean).sort();
    return answer;
}