function solution(n) {
    const answer = [];
    for (let i = 0; i < n; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            row.push(0);
        }
        answer.push(row);
    }

    let num = 1;
    let top = 0, bottom = n - 1, left = 0, right = n - 1;
    while (top <= bottom && left <= right) {
        // 왼 → 오
        for (let i = left; i <= right; i++) answer[top][i] = num++;
        top++;

        // 위 → 아래
        for (let i = top; i <= bottom; i++) answer[i][right] = num++;
        right--;

        // 오 → 왼
        for (let i = right; i >= left; i--) answer[bottom][i] = num++;
        bottom--;

        // 아래 → 위
        for (let i = bottom; i >= top; i--) answer[i][left] = num++;
        left++;
    }
    return answer;
}