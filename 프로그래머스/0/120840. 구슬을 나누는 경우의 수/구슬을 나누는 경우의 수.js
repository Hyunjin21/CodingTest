function solution(balls, share) {
    let n = 1;
    let m = 1;
    let n_m = 1;
    
    for(let i = 1; i<=balls; i++){
        n *= i;
    }
    for(let i = 1; i<=share; i++){
        m *= i;
    }
    for(let i = 1; i<=(balls-share); i++){
        n_m *= i;
    }
    
    return Math.round(n / (m*n_m));
    
}