function solution(n) {
    var answer = [];
    
    var triangle = Array(n).fill(0);
    triangle = triangle.map((element, index) => (Array(index+1).fill(0)));
    
    var cover = 0;
    var num = 1;
    while(n > 0) {
        const startI = 2 * cover;
        const startJ = cover;
        
        // 삼각형의 왼쪽 변을 채운다.
        for(var i = 0; i < n; i++) {
            triangle[startI+i][startJ] = num++;
        }
        
        // 삼각형의 아래 변을 채운다.
        for(var j = 1; j < n; j++) {
            triangle[startI+n-1][startJ+j] = num++;
        }
        
        // 삼각형의 오른쪽 변을 채운다.
        for(var k = n-2; k > 0; k--) {
            triangle[startI+k][startJ+k] = num++;
        }
        
        cover += 1;
        n -= 3;
    }
    
    triangle.forEach(row => {
        row.forEach(element => {
            answer.push(element);
        });
    });
    
    return answer;
}
