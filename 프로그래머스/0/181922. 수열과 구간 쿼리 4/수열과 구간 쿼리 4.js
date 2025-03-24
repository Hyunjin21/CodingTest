function solution(arr, queries) {
    for (let i = 0; i<queries.length; i++){
        var s = queries[i][0];
        var e = queries[i][1];
        var k = queries[i][2];
        for (let j = s; j <= e; j++){
            if(j % k == 0){
                arr[j] += 1
            }
        }
    }
    return arr;
}