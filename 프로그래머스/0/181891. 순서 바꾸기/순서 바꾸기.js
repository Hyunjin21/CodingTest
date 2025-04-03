function solution(num_list, n) {
    var answer = [];
    var after = num_list.slice(n);
    var before = num_list.slice(0, n);
    answer.push(after);
    answer.push(before);
    
    return answer.flat();
    
    // for(let i=n; i<num_list.length; i++){
    //     answer.push(num_list[i])
    // }
    // for(let i=0; i<n; i++){
    //     answer.push(num_list[i])
    // }
    // return answer;
}