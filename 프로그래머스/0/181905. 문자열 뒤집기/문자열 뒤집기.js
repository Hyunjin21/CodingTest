function solution(my_string, s, e) {
    var arr = my_string.slice(s, e+1).split('').reverse().join('');
    var front = my_string.slice(0, s);
    var back = my_string.slice(e+1);
    return front + arr + back;
}