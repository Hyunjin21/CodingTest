function solution(my_string) {
    var answer = [];
    var len = my_string.length;
    for(let i = len-1; i >= 0; i--){
        answer.push(my_string.slice(i));
    }
    answer.sort();
    return answer;
}