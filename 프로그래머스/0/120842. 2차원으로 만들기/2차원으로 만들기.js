function solution(num_list, n) {
    let answer = [];
    for(let i=0; i<num_list.length; ){
        let result = [];
        for(let j=0; j<n; j++){
            result.push(num_list[i]);
            i++;
        }
        answer.push(result);
    }
    return answer;
}