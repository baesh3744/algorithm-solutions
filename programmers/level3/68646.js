function solution(a) {
    var answer = 2;
    var leftIdx = 0;
    var leftMin = a[leftIdx];
    var rightIdx = a.length-1;
    var rightMin = a[rightIdx];
    
    while(rightIdx - leftIdx > 1) {
        if(rightMin > leftMin && a[--rightIdx] < rightMin) {
            rightMin = a[rightIdx];
            answer++;
        }
        if(leftMin > rightMin && a[++leftIdx] < leftMin) {
            leftMin = a[leftIdx];
            answer++;
        }
    }
    
    return answer;
}
