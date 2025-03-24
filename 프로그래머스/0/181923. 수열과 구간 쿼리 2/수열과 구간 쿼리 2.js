function solution(arr, queries) {
    var answer = [];
    for (let i=0; i<queries.length; i++){
        const [s, e, k] = queries[i];
        
        var minArr = [];
        for (let j = s; j <= e; j++){
            if(arr[j] > k){
                minArr.push(arr[j]);
            }
        }
        
        if (minArr.length == 0){
            answer.push(-1);
        } else {
            answer.push(Math.min(...minArr));
        }

    }
    return answer;

}