function solution(num_list) {
    var answer = [];
    var sorted = num_list.sort((a, b) => a-b);
    for(let i = 0; i<5; i++){
        answer.push(sorted[i]);
    }
    return answer;
}