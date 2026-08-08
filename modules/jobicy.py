import requests


def get_jobs():
    url = "https://jobicy.com/api/v2/remote-jobs"

    jobs = []

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        if response.status_code == 200:
            data = response.json()

            for job in data.get("jobs", []):
                jobs.append({
                    "Company": job.get("companyName", ""),
                    "Position": job.get("jobTitle", ""),
                    "Location": job.get("jobGeo", "Remote"),
                    "Description": job.get("jobDescription", ""),
                    "Apply": job.get("url", "")
                })

    except Exception as e:
        print("Jobicy Error:", e)

    return jobs