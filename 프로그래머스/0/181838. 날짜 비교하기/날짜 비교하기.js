function solution(date1, date2) {
    const [y1, m1, d1] = date1;
    const [y2, m2, d2] = date2;
    if (y1 < y2) return 1;
    else if (y1 == y2) {
        if (m1 < m2) return 1;
        else if (m1 == m2) {
            if (d1 < d2) return 1;
        }
    }
    return 0;
    // var answer = 0;
    // for(let i = 0; i<date1.length; i++){
    //     if (date1[i] < date2[i]){
    //         answer = 1;
    //         break;
    //     } else if (date1[i] > date2[i]){
    //         answer = 0;
    //         break;
    //     }
    // }
    // return answer;
}