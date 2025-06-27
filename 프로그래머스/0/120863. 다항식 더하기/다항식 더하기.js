function solution(polynomial) {
    let poly = polynomial.split('+').map(p => p.trim());
    let xSum = 0
    let nSum = 0
    for(let i = 0; i<poly.length; i++){
        if (poly[i].includes('x')){
            if (poly[i] === 'x'){
                xSum += 1
            } else {
                xSum += Number(poly[i].replace('x',''));
            }
        } else {
            nSum += Number(poly[i]);
        }
    }
    let result = [];
    if (xSum > 0) {
        result.push(xSum === 1 ? "x" : `${xSum}x`);
    }
    if (nSum > 0) {
        result.push(nSum);
    }
    return result.join(" + ");
}