function solution(array, commands) {
    var answer = [];
    
    for (var i=0; i<commands.length; i++){
        var command = commands[i];
        var start = command[0]-1;
        var end = command[1];
        var k = command[2]-1;
        
        var sliced = array.slice(start,end);
        
        sliced.sort(function(a, b){
            return a - b;
        })
        answer.push(sliced[k])
        
    }
    return answer;
}