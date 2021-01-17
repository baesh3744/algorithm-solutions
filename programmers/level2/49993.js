function solution(skill, skill_trees) {
    var answer = 0;
    
    skill_trees.forEach((skill_tree) => {
        const skill_tree_length = skill_tree.length;
        var learning_idx = 0;
        var possible = true;
        
        for(var i = 0; i < skill_tree_length; i++) {
            const idx = skill.indexOf(skill_tree[i]);
            
            if(idx == -1) continue;
            
            if(learning_idx == idx) learning_idx++;
            else {
                possible = false;
                break;
            }
        }
        
        if(possible) answer++;
    });
    
    return answer;
}
