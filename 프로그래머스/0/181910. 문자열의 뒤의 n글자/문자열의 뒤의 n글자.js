function solution(my_string, n) {
    var answer = '';
    var len = my_string.length;
    answer = my_string.slice(len-n, len);
    return answer;
}