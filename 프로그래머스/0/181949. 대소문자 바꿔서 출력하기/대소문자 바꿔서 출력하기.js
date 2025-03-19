const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    let swapped = ""
    for (let i = 0; i<str.length; i++){
        const char = str[i];
        if (char === char.toUpperCase()){
            swapped += char.toLowerCase();
        } else {
            swapped += char.toUpperCase();
        }
    }
    console.log(swapped);
});