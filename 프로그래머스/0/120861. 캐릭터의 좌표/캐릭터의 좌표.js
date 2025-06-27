function solution(keyinput, board) {
    var answer = [0, 0];
    let x = Math.floor(board[0]/2);
    let y = Math.floor(board[1]/2);
    for(let i = 0; i<keyinput.length; i++){
        if (keyinput[i] == "up" && answer[1] < y){
            answer[1] += 1;
        } else if (keyinput[i] == "down" && answer[1] > -y){
            answer[1] -= 1;
        } else if (keyinput[i] == "left" && answer[0] > -x){
            answer[0] -= 1;
        } else if (keyinput[i] == "right" && answer[0] < x){
            answer[0] += 1;
        }
        
    }
    return answer;
}