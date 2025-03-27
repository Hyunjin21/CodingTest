function solution(a, b, c, d) {
    const dice = [a, b, c, d];
    dice.sort((x, y) => x - y);
    
    const [x, y, z, w] = dice;
    
    if (x === w){
        return 1111*x;
    } else if (x === z || y === w){
        const p = x === z ? x : w;
        const q = x === z ? w : x;
        return (10*p + q)**2;
    } else if (x === y && z === w){
        return (x + z)*Math.abs(x - z);
    } else if (x === y || y === z || z === w){
        var p;
        var others = [];
        if (x === y){
            p = x;
            others = [z, w];
        } else if (y === z){
            p = y;
            others = [x, w];
        } else if (z === w){
            p = z;
            others = [x, y];
        }
        return others[0]*others[1];
    } else {
        return x;
    }
}