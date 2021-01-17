function solution(n) {
    var answer = '';
    
    while((n--) != 0) {
        switch(n % 3) {
            case 0:
                answer = '1' + answer;
                break;
            case 1:
                answer = '2' + answer;
                break;
            case 2:
                answer = '4' + answer;
                break;
        }

        n = parseInt(n / 3);
    }
    
    return answer;
}
