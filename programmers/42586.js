/* https://programmers.co.kr/learn/courses/30/lessons/42586?language=javascript */

function solution(progresses, speeds) {
    var answer = [];
    var remainingDays = [];
    const days = progresses.length;
    
    for(var i = 0; i < days; i++) {
        remainingDays.push(Math.ceil((100 - progresses[i]) / speeds[i]));
    }
    
    for(var i = 0; i < days; ) {
        var next;
        for(next = i+1; next < days; next++) {
            if(remainingDays[i] < remainingDays[next]) break;
        }
        answer.push(next - i);
        i = next;
    }
    
    return answer;
}
