function solution(my_string, indices) {
    var answer = '';
    for (let i = 0; i<my_string.length; i++){
        if (indices.includes(i) == true){
            continue;
        } else {
            answer += my_string[i];
        }
    }
    return answer;
}