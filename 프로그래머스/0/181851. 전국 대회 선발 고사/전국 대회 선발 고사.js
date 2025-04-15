function solution(rank, attendance) {
    var answer = 0;
    var attend = [];
    for(let i = 0; i<rank.length; i++){
        if(attendance[i] == true){
            attend.push([i, rank[i]]);
        }
    }
    attend.sort((a,b) => a[1]-b[1]);
    var a = attend[0][0];
    var b = attend[1][0];
    var c = attend[2][0];
    answer = 10000*a + 100*b + c;
    return answer;
}