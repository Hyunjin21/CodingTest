function solution(sides) {
    var answer = 0;
    sides.sort((a, b) => a - b);
    if(sides[2] < sides[0]+sides[1]){
        answer = 1;
    } else {
        answer = 2;
    }
    return answer;
}