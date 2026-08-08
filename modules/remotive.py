import requests


def get_jobs():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30
    )

    jobs = []

    if response.status_code == 200:
        data = response.json()

        for job in data.get("jobs", []):
            jobs.append({
                "Company": job.get("company_name", ""),
                "Position": job.get("title", ""),
                "Location": job.get("candidate_required_location", ""),
                "Description": job.get("description", ""),
                "Apply": job.get("url", "")
            })

    return jobs