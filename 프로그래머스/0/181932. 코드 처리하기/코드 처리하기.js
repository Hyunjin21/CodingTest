function solution(code) {
    var answer = '';
    var mode = 0;
    for(var idx=0; idx<code.length; idx++){
        if(mode == '0'){
            if(code[idx] != '1' && idx%2==0){
                answer += code[idx]
            } else if (code[idx] == '1'){
                mode = 1;
            }
        } else if(mode == '1'){
            if(code[idx] != '1' && idx%2!=0){
                answer += code[idx]
            } else if (code[idx] == '1'){
                mode = 0;
            }
        } else if (answer == "") {
            answer += "EMPTY";
        }  
    }
    
    return answer ? answer : "EMPTY";
}