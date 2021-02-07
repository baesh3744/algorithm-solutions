function solution(jobs) {
    var answer = 0;
    var currentTime = 0;
    const totalJobs = jobs.length;

    while (jobs.length > 0) {
        const newJobs = jobs
            .filter((job) => job[0] <= currentTime)
            .sort((a, b) => a[1] - b[1]);
        if (newJobs.length === 0) {
            currentTime++;
        } else {
            const executed = newJobs[0];
            currentTime += executed[1];
            answer += currentTime - executed[0];
            jobs.splice(
                jobs.findIndex(
                    (job) => job[0] === executed[0] && job[1] === executed[1]
                ),
                1
            );
        }
    }

    return parseInt(answer / totalJobs);
}
