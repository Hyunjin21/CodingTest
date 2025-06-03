function solution(my_string) {
    var answer = '';
    let str = my_string.split('');
    let arr = ['a', 'e', 'i', 'o', 'u'];
    answer = str.filter((char)=> !arr.includes(char)).join('');
    return answer;
}