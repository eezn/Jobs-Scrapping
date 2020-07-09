import csv


def save_to_file(jobs):
    # UnicodeEncodeError: 'cp949' codec can't encode character '\u4f1a' in position 17: illegal multibyte sequence -> encoding='utf-8-sig'
    file = open("jobs.csv", encoding='utf-8-sig', mode="w")
    writer = csv.writer(file)
    writer.writerow(["tltle", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return
