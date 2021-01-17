function solution(n) {
    var cache = [0, 1, 2];
    
    for(var i = 3; i <= n; i++) {
        cache[i] = (cache[i-1] + cache[i-2]) % 1000000007;
    }
    
    return cache[n];
}
