function solution(my_string) {
    var answer = [];
    answer = my_string.split(' ').filter(Boolean);
    return answer;
    // return my_string.trim().split(/ +/);
}