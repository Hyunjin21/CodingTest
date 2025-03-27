function solution(l, r) {
    var answer = [];
    for (let i = l; i<=r; i++){
        var letter = i.toString().split('');
        if(letter.every((el) => el === '5' || el === '0')){
            answer.push(i);
        } 
    }
    return answer.length === 0 ? [-1] : answer;
    // if (answer == ''){
    //     answer.push(-1);
    // }
    // return answer;
}