function solution(num_list) {
    var len = num_list.length;
    if(len >= 11){
        var sum = 0;
        for (let i = 0; i<len; i++){
            sum += num_list[i];
        }
        return sum;
    } else {
        var multi = num_list[0];
        for (let j = 1; j<len; j++){
            multi *= num_list[j];
        }
        return multi;
    }
}