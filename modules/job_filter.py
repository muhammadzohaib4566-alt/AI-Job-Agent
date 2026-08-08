from config import JOB_TITLES

def filter_jobs(jobs):
    filtered = []

    for job in jobs:
        position = str(job.get("Position", "")).lower()

        for title in JOB_TITLES:
            if title.lower() in position:
                filtered.append(job)
                break

    return filtered