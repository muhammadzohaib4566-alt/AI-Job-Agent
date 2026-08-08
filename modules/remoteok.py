import requests

def get_jobs():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    jobs = []

    if response.status_code == 200:

        data = response.json()[1:]

        for job in data:

            jobs.append({

                "Company": job.get("company"),

                "Position": job.get("position"),

                "Location": job.get("location"),

                "Apply": job.get("apply_url")

            })

    return jobs