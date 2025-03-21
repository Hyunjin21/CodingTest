function solution(num_list) {
    var num_len = num_list.length;
    if(num_list[num_len-1]>num_list[num_len-2]){
        var plus = num_list[num_len-1]-num_list[num_len-2];
        num_list.push(plus);
    } else {
        var plus = num_list[num_len-1]*2;
        num_list.push(plus);
    }
    return num_list;
}