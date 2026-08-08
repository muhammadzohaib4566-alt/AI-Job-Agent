from modules.remoteok import get_jobs
from modules.job_filter import filter_jobs
from modules.ai_match import match_job
from modules.excel import save_jobs
from modules.alert import send_alert

print("=" * 50)
print("      AI JOB AGENT")
print("=" * 50)

# Get Jobs
jobs = get_jobs()
print(f"Total Jobs Found: {len(jobs)}")

# Filter Jobs
filtered_jobs = jobs
print(f"Filtered Jobs: {len(filtered_jobs)}")

# AI Score
final_jobs = []

for job in filtered_jobs:
    score = match_job(job)
    job["Score"] = score

    if score > 0:
        final_jobs.append(job)

print(f"AI Matched Jobs: {len(final_jobs)}")

# High Match Alert
high_match_jobs = [
    job for job in final_jobs
    if job.get("Score", 0) >= 40
]

print(f"High Match Jobs (40+): {len(high_match_jobs)}")

for job in high_match_jobs:
    send_alert(job)

# Sort by highest score
final_jobs.sort(key=lambda job: job["Score"], reverse=True)

# Keep top 10 jobs
final_jobs = final_jobs[:10]

# Save Excel
save_jobs(final_jobs)

print("=" * 50)
print("Done Successfully")
print("=" * 50)