function solution(strArr) {
    let arr = Array(31).fill(0); 
    for (let i = 0; i < strArr.length; i++) {
        let len = strArr[i].length; 
        arr[len]++; 
    }
    let max = 0;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i]; 
        }
    }
    return max;
    
    // 1번 풀이
    // var answer = 0;
    // var max = 0;
    // for(let i=0; i<strArr.length; i++){
    //     if(strArr[i].length > max){
    //         max = strArr[i].length;   
    //     }
    // }
    // for(let j=1; j<=max; j++){
    //     var count = 0;
    //     for(let k=0; k<strArr.length; k++){
    //         if(strArr[k].length === j){
    //             count++;
    //         }
    //     }
    //     if (count > answer){
    //         answer = count;
    //     }
    // }
    // return answer;
    
    // 2번풀이
    // let arr = Array(31).fill(0);
    // for (let s of strArr) arr[s.length]++
    // return Math.max(...arr);

}