function solution(arr, queries) {
    var answer = [];
    for (let i=0; i<queries.length; i++){
        var s = queries[i][0];
        var e = queries[i][1];
        var k = queries[i][2];
        let minValue = Infinity;
        
        for (let j = s; j <= e; j++){
            if(arr[j] > k && arr[j] < minValue){
                minValue = arr[j];
            }
        }
        answer.push(minValue === Infinity ? -1 : minValue);
    }
    return answer;

}