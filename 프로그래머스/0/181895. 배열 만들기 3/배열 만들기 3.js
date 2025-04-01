function solution(arr, intervals) {
    var answer = [];
    for (let i = 0; i < intervals.length; i++){
        const start = intervals[i][0];
        const end = intervals[i][1];
        answer.push(arr.slice(start, end+1));
    }
    return answer.flat();
}