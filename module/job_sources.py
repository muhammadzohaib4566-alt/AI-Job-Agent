from modules.remoteok import get_jobs

def get_all_jobs():
    jobs = []

    try:
        jobs.extend(get_jobs())
    except Exception as e:
        print("RemoteOK Error:", e)

    return jobs