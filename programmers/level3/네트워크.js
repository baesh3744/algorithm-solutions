function solution(n, computers) {
    var answer = 0;
    
    const dfs = (i, j) => {
        computers[i][j] = computers[j][i] = 0;
        
        computers[i].forEach((computer, index) => {
            if(computer == 1) dfs(i, index);
        });
        
        computers[j].forEach((computer, index) => {
            if(computer == 1) dfs(j, index);
        });
    };
    
    computers.forEach((computer, indexi) => {
        computer.forEach((com, indexj) => {
            if(com == 1) {
                dfs(indexi, indexj);
                answer++;
            }
        });
    });
    
    return answer;
}
