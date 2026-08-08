def match_job(job):
    title = job.get("Position", job.get("position", "")).lower()

    keywords = [
        "building",
        "architect",
        "architectural",
        "engineering",
        "engineer",
        "civil",
        "construction",
        "site",
        "sales",
        "sales executive",
        "customer",
        "customer support",
        "customer service",
        "telecom",
        "call center",
        "remote"
    ]

    score = 0

    for word in keywords:
        if word in title:
            score += 10

    return score