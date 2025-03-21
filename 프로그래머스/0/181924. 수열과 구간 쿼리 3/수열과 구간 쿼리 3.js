function solution(arr, queries) {
    for(let i =0; i<queries.length; i++){
        var a = queries[i][0];
        var b = queries[i][1];
        var temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    return arr;
}