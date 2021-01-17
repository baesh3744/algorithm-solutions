function solution(N, number) {
    const arr = [];
    
    for(var i = 1; i <= 8; i++) {
        arr[i] = new Set([Number(N.toString().repeat(i))]);
        
        for(var j = 1; j < i; j++) {
            for(const element1 of arr[j]) {
                for(const element2 of arr[i-j]) {
                    arr[i].add(element1 + element2);
                    arr[i].add(element1 - element2);
                    arr[i].add(element1 * element2);
                    if(element2) arr[i].add(element1 / element2);
                }
            }
        }
        
        if(arr[i].has(number)) return i;
    }
    
    return -1;
}
