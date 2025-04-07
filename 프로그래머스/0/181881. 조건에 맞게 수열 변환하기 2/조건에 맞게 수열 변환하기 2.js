function solution(arr) {
    var answer = 0;
    while(true){
        var newArr = [];
        var changed = false;
        var next;
        
        for (let i = 0; i<arr.length; i++){
            if (arr[i]>=50 && arr[i]%2==0){
                next = arr[i]/2;
            } else if (arr[i]<50 && arr[i]%2!=0){
                next = arr[i]*2+1;
            } else {
                next = arr[i];
            }
            
            if (next !== arr[i]){
                changed = true;
            }
            newArr.push(next);
        }
        if (!changed){
            break;
        } 
        arr = newArr;
        answer++;
    }
    return answer;
}