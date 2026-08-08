def match_job(job):
    title = job.get("Position", job.get("position", "")).lower()
    description = job.get("Description", job.get("description", "")).lower()

    text = title + " " + description

    keywords = {
        "building": 10,
        "architect": 10,
        "architectural": 10,
        "engineering": 10,
        "engineer": 10,
        "civil": 10,
        "construction": 10,
        "site": 8,
        "autocad": 15,
        "sketchup": 15,
        "revit": 15,
        "drafting": 12,
        "sales": 8,
        "sales executive": 10,
        "customer service": 8,
        "customer support": 8,
        "telecom": 6,
        "call center": 6,
        "remote": 5
    }

    score = 0

    for keyword, points in keywords.items():
        if keyword in text:
            score += points

    if score > 100:
        score = 100

    return score