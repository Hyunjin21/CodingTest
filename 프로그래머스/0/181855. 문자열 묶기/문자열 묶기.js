function solution(strArr) {
    var answer = 0;
    var max = 0;
    for(let i=0; i<strArr.length; i++){
        if(strArr[i].length > max){
            max = strArr[i].length;   
        }
    }
    for(let j=1; j<=max; j++){
        var count = 0;
        for(let k=0; k<strArr.length; k++){
            if(strArr[k].length === j){
                count++;
            }
        }
        if (count > answer){
            answer = count;
        }
    }
    return answer;
    // var answer = 0;
    // var count = [];
    // for(let i = 0; i<strArr.length; i++){
    //     var num = strArr[i].length;
    //     if (count[num] == undefined){
    //         count[num] = 1;
    //     } else {
    //         count[num]++;
    //     }
    //     if(count[num] > answer){
    //         answer = count[num];
    //     }
    // }
    // return answer;
}