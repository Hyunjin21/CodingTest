function solution(strArr) {
    var answer = 0;
    var count = [];
    for(let i = 0; i<strArr.length; i++){
        var num = strArr[i].length;
        if (count[num] == undefined){
            count[num] = 1;
        } else {
            count[num]++;
        }
        if(count[num] > answer){
            answer = count[num];
        }
    }
    return answer;
}