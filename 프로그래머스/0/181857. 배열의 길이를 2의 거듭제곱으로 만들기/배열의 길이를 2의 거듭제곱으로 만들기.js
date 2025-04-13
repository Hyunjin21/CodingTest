function solution(arr) {
    var answer = arr;
    var len = arr.length;
    var power = 1;
    while(power < len){
        power = power * 2;
    }
    while(answer.length < power){
        answer.push(0);
    }
    
    return answer;
}