function solution(num_list) {
    var num1 = 1;
    var num2 = null;
    for(let i=0; i<num_list.length; i++){
        num1 *= num_list[i]
        num2 += num_list[i]
    }

    if (num1 < num2**2){
        return 1;
    } else {
        return 0;
    }

}