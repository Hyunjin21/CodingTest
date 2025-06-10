function solution(s1, s2) {
    let count = 0;
    for(let i of s1){
        if(s2.includes(i)){
            count++;
        }
    }
    return count;
    // var answer = 0;
    // s1.sort();
    // s2.sort();
    // for(let i = 0; i<s1.length; i++){
    //     for(let j = 0; j<s2.length; j++){
    //         if(s1[i] === s2[j]){
    //             answer += 1;
    //         }
    //     }
    // }
    // return answer;
}