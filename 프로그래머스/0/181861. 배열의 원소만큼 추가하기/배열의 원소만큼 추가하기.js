function solution(arr) {
    var answer = [];
    for (let i=0; i<arr.length; i++){
        var count = arr[i];
        for (let j=0; j<count; j++){
            answer.push(arr[i]);
        }
    }
    return answer;
}