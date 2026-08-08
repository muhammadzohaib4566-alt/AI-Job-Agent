def match_job(job):
    title = job.get("Position", "").lower()

    keywords = [
        "python",
        "ai",
        "automation",
        "developer",
        "data"
    ]

    score = 0

    for word in keywords:
        if word in title:
            score += 20

    return score