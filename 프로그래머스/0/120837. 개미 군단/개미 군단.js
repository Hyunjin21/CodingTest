function solution(hp) {
    var answer = 0;
    let generalAnt = Math.floor(hp / 5);
    let soldierAnt = Math.floor((hp%5)/3);
    let wokerAnt = (hp%5)%3;
    answer = generalAnt + soldierAnt + wokerAnt;
    return answer;
}