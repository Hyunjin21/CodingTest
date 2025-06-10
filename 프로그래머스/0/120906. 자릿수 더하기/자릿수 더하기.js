function solution(n) {
    var answer = 0;
    let str = String(n).split('');
    for(let i of str){
        answer += Number(i);
    }
    return answer;
}