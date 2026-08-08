import requests
from bs4 import BeautifulSoup


def get_jobs():
    url = "https://weworkremotely.com/remote-jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    jobs = []

    try:
        response = requests.get(url, headers=headers, timeout=30)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            for job in soup.select("li"):
                link = job.find("a")

                if not link:
                    continue

                company = job.find(class_="company")
                title = job.find(class_="title")
                region = job.find(class_="region")

                jobs.append({
                    "Company": company.get_text(strip=True) if company else "",
                    "Position": title.get_text(strip=True) if title else "",
                    "Location": region.get_text(strip=True) if region else "Remote",
                    "Description": "",
                    "Apply": "https://weworkremotely.com" + link.get("href", "")
                })

    except Exception as e:
        print("WWR Error:", e)

    return jobs