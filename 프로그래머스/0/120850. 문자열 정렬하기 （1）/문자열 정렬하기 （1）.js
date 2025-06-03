function solution(my_string) {
    var str = my_string.replace(/[a-zA-Z]/g,'').split('').map(Number);
    str.sort((a, b) => a - b);
    return str;
}