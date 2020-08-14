# python3

from collections import namedtuple
from queue import PriorityQueue 

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


  


def assign_jobs(n_workers, jobs):
    q=PriorityQueue()
    for i in range (n_workers):
        q.put((0,i))
    result=[]
    for job in jobs:
        priority,thread=q.get()
        result.append(AssignedJob(thread,priority))
        q.put((priority+job,thread))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
