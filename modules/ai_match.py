from modules.profile import PROFILE


def match_job(job):
    title = job.get("Position", job.get("position", "")).lower()
    description = job.get("Description", job.get("description", "")).lower()

    text = title + " " + description

    engineering_keywords = [
        "building",
        "architect",
        "architectural",
        "engineering",
        "engineer",
        "civil",
        "construction",
        "site",
        "drafting",
        "draftsman"
    ]

    technical_keywords = [
        "autocad",
        "sketchup",
        "revit",
        "2d drawing",
        "3d modeling",
        "drafting"
    ]

    sales_keywords = [
        "sales",
        "sales executive",
        "sales representative",
        "business development"
    ]

    customer_keywords = [
        "customer service",
        "customer support",
        "call center",
        "customer care"
    ]

    telecom_keywords = [
        "telecom",
        "internet",
        "network",
        "isp"
    ]

    remote_keywords = [
        "remote",
        "work from home"
    ]

    def count_matches(keywords):
        return len([word for word in keywords if word in text])

    engineering_match = count_matches(engineering_keywords)
    technical_match = count_matches(technical_keywords)
    sales_match = count_matches(sales_keywords)
    customer_match = count_matches(customer_keywords)
    telecom_match = count_matches(telecom_keywords)
    remote_match = count_matches(remote_keywords)

    # Category scores
    engineering_score = min(engineering_match * 8, 25)
    technical_score = min(technical_match * 8, 20)
    sales_score = min(sales_match * 8, 20)
    customer_score = min(customer_match * 8, 20)
    telecom_score = min(telecom_match * 5, 10)
    remote_score = min(remote_match * 5, 5)

    score = (
        engineering_score
        + technical_score
        + sales_score
        + customer_score
        + telecom_score
        + remote_score
    )

    matched_skills = []

    for keyword in (
        engineering_keywords
        + technical_keywords
        + sales_keywords
        + customer_keywords
        + telecom_keywords
        + remote_keywords
    ):
        if keyword in text:
            matched_skills.append(keyword)

    job["Engineering Score"] = engineering_score
    job["Technical Score"] = technical_score
    job["Sales Score"] = sales_score
    job["Customer Score"] = customer_score
    job["Telecom Score"] = telecom_score
    job["Remote Score"] = remote_score
    job["Matched Skills"] = ", ".join(sorted(set(matched_skills)))

    return score