function solution(picture, k) {
    var answer = [];
    for(let i=0; i<picture.length; i++){
        var result = [];
        for(let j=0; j<picture[i].length; j++){
            result.push(picture[i][j].repeat(k));
        }
        for(let l=0; l<k; l++){
            answer.push(result.join(''));   
        }
    }
    return answer;
}