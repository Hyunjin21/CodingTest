function solution(arr) {
    var stk = [];
    for (let i = 0; i <arr.length;){
        var len = stk.length;
        if(len == 0){
            stk.push(arr[i]);
            i += 1;
        } else {
            if (stk[len-1] < arr[i]){
                stk.push(arr[i]);
                i += 1;
            } else {
                stk.pop();
            }
        }
    }
    return stk;
}