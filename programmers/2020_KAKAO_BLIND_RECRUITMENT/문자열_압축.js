function compressString(s, unit) {
    const splitString = [];
    for(var i = 0; i < s.length; i += unit) {
        splitString.push(s.substring(i, i+unit));
    }
    
    var ret = 0;
    var pastString = "";
    var repeat = 1;
    splitString.forEach(str => {
        if(str === pastString) {
            repeat++;
        }
        
        if(str !== pastString) {
            if(repeat !== 1) ret += repeat.toString().length;
            ret += str.length;
            pastString = str;
            repeat = 1;
        }
    });
    if(repeat !== 1) ret += repeat.toString().length;

    return ret;
}

function solution(s) {
    var answer = 1000;
    
    for(var i = 1; i <= s.length/2; i++) {
        answer = Math.min(answer, compressString(s, i));
    }
    if(s.length === 1) answer = 1;
    
    return answer;
}
