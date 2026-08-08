from openpyxl import Workbook
from config import OUTPUT_FILE

def save_jobs(jobs):
    wb = Workbook()
    ws = wb.active
    ws.title = "Jobs"

    ws.append([
        "Company",
        "Position",
        "Location",
        "Apply",
        "Score"
    ])

    for job in jobs:
        ws.append([
            job.get("Company", ""),
            job.get("Position", ""),
            job.get("Location", ""),
            job.get("Apply", ""),
            job.get("Score", 0)
        ])

    wb.save(OUTPUT_FILE)
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")