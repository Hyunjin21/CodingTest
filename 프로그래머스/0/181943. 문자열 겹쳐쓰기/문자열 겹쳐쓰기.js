function solution(my_string, overwrite_string, s) {
    var answer = '';
    const mystr = my_string.split('');
    const overstr = overwrite_string.split('');
    mystr.splice(s,overstr.length,overstr.join(''));
    answer = mystr.join('');
    return answer;
}