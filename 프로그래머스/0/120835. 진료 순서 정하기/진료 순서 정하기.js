function solution(emergency) {
    var answer = [];
    let sorted = [...emergency].sort((a, b) => b - a);
    for (let i = 0; i < emergency.length; i++) {
        let rank = sorted.indexOf(emergency[i]) + 1;
        answer.push(rank);
    }
    return answer;
}