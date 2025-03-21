function solution(num_list) {
    var answer = 0;
    var oddNum = []; 
    var evenNum= [];
    for(let i=0; i<num_list.length; i++){
        if(num_list[i]%2 == 0){
            evenNum.push(num_list[i]);
        } else {
            oddNum.push(num_list[i]);
        }
    }
    answer = parseInt(oddNum.join(''))+parseInt(evenNum.join(''))
    return answer;
}