from chemical_jobs.core import Job, summarize


if __name__ == "__main__":
    record = Job.create("demo", "v1", "draft", "operator", {"场景": "登记工艺任务并生成任务摘要"})
    print(summarize(record))

