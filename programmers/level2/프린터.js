function solution(priorities, location) {
    var answer = 0;
    
    var new_priorities = priorities
        .slice()
        .sort((a, b) => {
            if(a > b) return -1;
            else return 1;
        })
        .filter(priority => priority >= priorities[location]);
    
    var foundAnswer = false;
    var location_cur = -1;
    const priorities_length = priorities.length;
    for(var i = 0; !foundAnswer && i < new_priorities.length; i++) {
        var foundPrint = false;
        for(var j = 0; !foundPrint && j < priorities_length; j++) {
            location_cur++;
            if(location_cur >= priorities_length) location_cur -= priorities_length;
            
            if(priorities[location_cur] === new_priorities[i]) {
                answer++;
                foundPrint = true;
                if(location_cur === location) foundAnswer = true;
            }
        }
    }
    
    return answer;
}
