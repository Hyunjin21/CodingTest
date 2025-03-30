function solution(my_string, m, c) {
    var answer = '';
    for (let i = c-1; i < my_string.length; i+=m){
        answer += my_string[i];
    }
    // var arr = [];
    // for (let i = 0; i < my_string.length;){
    //     arr.push(my_string.slice(i, m+i));
    //     i += m;
    // }
    // for (let row of arr){
    //     answer += row[c-1];
    // }
    return answer;
}