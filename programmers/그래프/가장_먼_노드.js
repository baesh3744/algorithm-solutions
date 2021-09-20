function solution(n, edge) {
    const visited = [ 1 ];
    const current = [ 1 ];
    const next = Array.from(Array(n+1), () => Array());
    
    edge.forEach(vertex => {
        const first = vertex[0];
        const second = vertex[1];
        
        next[first].push(second);
        next[second].push(first);
    });
    
    while(visited.length !== n) {
        const currentLength = current.length;
        for(var i = 0; i < currentLength; i++) {
            const currentNode = current.shift();

            next[currentNode].forEach(node => {
                if(!visited.includes(node)) {
                    visited.push(node);
                    current.push(node);
                }
            });
        }
    }
    
    return current.length;
}
