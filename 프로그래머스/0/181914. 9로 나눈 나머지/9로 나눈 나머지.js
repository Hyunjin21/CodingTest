function solution(number) {
    var answer = 0;
    var letter = [];
    for (let i = 0; i < number.length; i++){
        letter.push(number[i]);
    }
    var sum = 0;
    for (let j = 0; j < letter.length; j++){
        sum += Number(letter[j]);
    }
    answer = sum % 9;
    return answer;
}