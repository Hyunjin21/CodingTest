function solution(my_string, m, c) {
    var answer = '';
    var arr = [];
    for (let i = 0; i < my_string.length;){
        arr.push(my_string.slice(i, m+i));
        i += m;
    }
    for (let row of arr){
        answer += row[c-1];
    }
    return answer;
}