# python3

from collections import namedtuple
from queue import PriorityQueue 

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

# Import the heap functions from python library 
from heapq import heappush, heappop, heapify  
  


def assign_jobs(n_workers, jobs):
    q=PriorityQueue()
    for i in range (n_workers):
        q.put((0,i))
    result=[]
    for job in jobs:
        a,b=q.get()
        result.append(AssignedJob(b,a))
        q.put((a+job,b))
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
