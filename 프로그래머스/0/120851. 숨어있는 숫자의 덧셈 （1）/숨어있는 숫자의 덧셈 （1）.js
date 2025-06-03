function solution(my_string) {
    var answer = 0;
    let str = my_string.replace(/[a-zA-Z]/g,'').split('').map(Number);
    for(const i of str) {
        answer += i;
    }
    return answer;
}