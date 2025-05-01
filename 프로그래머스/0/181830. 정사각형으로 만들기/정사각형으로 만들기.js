function solution(arr) {
    const row = arr.length;    // 행
    const col = arr[0].length; // 열

    if(row > col){
        for(let i=0; i<row; i++){
            while(arr[i].length < row){
                arr[i].push(0);
            }
        }
    }
    else if (row < col){
        while (arr.length < col) {
            // arr.push(new Array(col).fill(0));
            let newRow = [];
            for (let j = 0; j < col; j++) {
                newRow.push(0);
            }
            arr.push(newRow);
        }
    }
    return arr;
}