function durationStrToInt(strDurationTime) {
    const splitStrDurationTime = strDurationTime.split(".");
    
    const durationSec = parseInt(splitStrDurationTime[0]);
    var strDurationMS = splitStrDurationTime[1];
    
    var durationMS;
    if(strDurationMS) {
        while(strDurationMS.length < 3) {
            strDurationMS = strDurationMS.concat('0');
        }
        durationMS = parseInt(strDurationMS);
    } else {
        durationMS = 0;
    }
    
    return durationSec * 1000 + durationMS;
}

function isRange(indexStart, indexEnd, iStart, iEnd) {
    if(iEnd < indexStart || indexEnd < iStart) return false;
    return true;
}

function solution(lines) {
    var answer = 0;
    
    const logs = lines.map((line) => {
        const splitLine = line.split(" ");
        
        const strEndDay = splitLine[0];
        const strEndTime = splitLine[1];
        const end = new Date(strEndDay + " " + strEndTime).getTime();
        
        const duration = durationStrToInt(splitLine[2].split("s")[0]);
        
        const start = end - duration + 1;
        const before = start - 1000 + 1;
        const after = start + 1000 - 1;
        
        return {
            before,
            start,
            after,
            end,
        };
    });

    logs.forEach((log) => {
        var beforeThroughput = 0;
        var afterThroughput = 0;
        for(var i = logs.length-1; i >= 0; i--) {
            const logsI = logs[i];
            
            if(logsI.end < log.before) break;
            
            if(isRange(log.before, log.start, logsI.start, logsI.end)) beforeThroughput++;
            if(isRange(log.start, log.after, logsI.start, logsI.end)) afterThroughput++;
        }
        
        if(answer < beforeThroughput) answer = beforeThroughput;
        if(answer < afterThroughput) answer = afterThroughput;
    });
    
    return answer;
}
