function solution(dots) {
    let x = [];
    let y = [];
    for (let pos of dots) {
        x.push(pos[0]);
        y.push(pos[1]);
    }
    return (Math.max(...x) - Math.min(...x)) * (Math.max(...y) - Math.min(...y));
    
//     let width = 0;
//     let height = 0;
//     if (dots[0][0] != dots[1][0]){
//         width = dots[1][0] - dots[0][0];
//     } else if (dots[0][0] != dots[2][0]){
//         width = dots[2][0] - dots[0][0];
//     } else if (dots[0][0] != dots[3][0]){
//         width = dots[3][0] - dots[0][0];
//     }
    
//     if (dots[0][1] != dots[1][1]){
//         height = dots[1][1] - dots[0][1];
//     } else if (dots[0][1] != dots[2][1]){
//         height = dots[2][1] - dots[0][1];
//     } else if (dots[0][1] != dots[3][1]){
//         height = dots[3][1] - dots[0][1];
//     } 
//     let answer = Math.abs(width) * Math.abs(height);
//     return answer;
}