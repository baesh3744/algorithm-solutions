/* https://programmers.co.kr/learn/courses/30/lessons/42583?language=javascript */

function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    var crossing_weights = [];
    var total_crossing_weights = 0;
    
    truck_weights.forEach((truck_weight, index) => {
        // 지나간 트럭은 제외한다.
        const crossing_weights_tmp = crossing_weights.filter((crossing_weight) => {
            crossing_weight.time--;
            if(crossing_weight.time === 0) {
                total_crossing_weights -= crossing_weight.truck_weight;
                return false;
            }
            return true;
        });
        crossing_weights = crossing_weights_tmp;
        
        // 다음 트럭이 건너갈 수 있을 때까지, 트럭을 한 대씩 지나가게 한다.
        while(total_crossing_weights + truck_weight > weight) {
            const firstTruck = crossing_weights[0];
            crossing_weights.shift();
            
            crossing_weights.forEach((crossing_weight) => {
                crossing_weight.time -= firstTruck.time;
            });
            answer += firstTruck.time;
            total_crossing_weights -= firstTruck.truck_weight;
        }
        
        // 대기 트럭 한 대가 다리를 건넌다.
        crossing_weights.push({
            time: bridge_length,
            truck_weight
        });
        answer++;
        total_crossing_weights += truck_weight;
    });
    
    // 대기 트럭이 없을 때, 다리를 건너는 트럭이 지나가는데 걸리는 시간을 더해준다.
    answer += crossing_weights[crossing_weights.length - 1].time;
    
    return answer;
}
