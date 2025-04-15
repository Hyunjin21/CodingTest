function solution(num_str) {
    var answer = 0;
    var num = num_str.split('');
    answer = num.reduce((a,b) => Number(a)+Number(b));
    return answer;
}