function solution(my_string) {
    var str = my_string.replace(/[a-z]/g,'').split('').map(Number);
    str.sort((a, b) => a - b);
    return str;
}