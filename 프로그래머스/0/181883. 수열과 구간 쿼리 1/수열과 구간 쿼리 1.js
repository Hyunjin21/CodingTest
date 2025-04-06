function solution(arr, queries) {
    for (let i = 0; i < queries.length; i++){
        var [start, end] = queries[i];
        for (let j = start; j <= end; j++){
            arr[j] += 1;
        }
    }

    return arr;
}