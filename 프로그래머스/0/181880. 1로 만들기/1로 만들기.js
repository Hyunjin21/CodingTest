function solution(num_list) {
    var answer = 0;
    for(let i = 0; i<num_list.length; i++){
        var num = num_list[i];
        while(num !== 1){
            if(num%2==0){
                num = num/2;
            } else {
                num = (num-1)/2;
            }
            answer++;
        }

    }
    return answer;
}
// function solution(num_list) {
//     var answer = 0;
//     for(let i = 0; i<num_list.length; i++){
//         var num = num_list[i];
//         while(num > 1){
//             num = Math.floor(num/2);
//             answer++;
//         }

//     }
//     return answer;
// }