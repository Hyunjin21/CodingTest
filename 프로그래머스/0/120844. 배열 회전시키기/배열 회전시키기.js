function solution(numbers, direction) {
    if(direction === "right"){
        numbers.unshift(numbers.pop());
    }else{
        numbers.push(numbers.shift())
    }
    return numbers;
}
// function solution(numbers, direction) {
//     var answer = [];
//     if(direction == 'right'){
//         answer.push(numbers[numbers.length-1]);
//     } 
//     for(let i=0; i<numbers.length-1; i++){
//         if(direction == 'right'){
//             answer.push(numbers[i]);
//         } else if(direction == 'left'){
//             answer.push(numbers[i+1]);
//         }
//     }
//     if (direction == 'left'){
//         answer.push(numbers[0]);
//     }
//     return answer;
// }