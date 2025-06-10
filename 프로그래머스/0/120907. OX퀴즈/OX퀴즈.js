function solution(quiz) {
    var answer = [];
    for(let i = 0; i<quiz.length; i++){
        let cal = quiz[i].split(' = ');
        if (eval(cal[0]) == Number(cal[1])){
            answer.push("O");
        } else {
            answer.push("X");
        }
    }
    return answer;
}