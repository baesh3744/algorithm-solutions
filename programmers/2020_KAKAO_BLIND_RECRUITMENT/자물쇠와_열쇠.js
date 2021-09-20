function rotateKey(key) {
    const key_length = key.length;
    var rotated_key = Array.from(Array(key_length), () => Array(key_length));
    for(var i = 0; i < key_length; i++) {
        for(var j = 0; j < key_length; j++) {
            rotated_key[j][key_length-i-1] = key[i][j];
        }
    }
    return rotated_key;
}

function isAnswer(board, lock_length) {
    for(var i = lock_length; i < 2*lock_length; i++) {
        for(var j = lock_length; j < 2*lock_length; j++) {
            if(board[i][j] !== 1) return false;
        }
    }
    return true;
}

function solution(key, lock) {
    var answer = false;
    const key_length = key.length;
    const lock_length = lock.length;
    const board_length = 3 * lock_length;
    
    const board_origin = Array.from(Array(board_length), () => Array(board_length).fill(0));
    for(var i = lock_length; i < 2*lock_length; i++) {
        for(var j = lock_length; j < 2*lock_length; j++) {
            board_origin[i][j] = lock[i-lock_length][j-lock_length];
        }
    }
    
    for(var i = 0; i < 4; i++) {
        key = rotateKey(key);
        
        const end_value = board_length - key_length + 1;
        for(var start_i = 0; !answer && start_i < end_value; start_i++) {
            for(var start_j = 0; !answer && start_j < end_value; start_j++) {
                var board = board_origin.map(arr => arr.slice());
                
                for(var key_i = 0; key_i < key_length; key_i++) {
                    for(var key_j = 0; key_j < key_length; key_j++) {
                        board[start_i+key_i][start_j+key_j] += key[key_i][key_j];
                    }
                }
                
                if(isAnswer(board, lock_length)) answer = true;
            }
        }
    }
    
    return answer;
}
