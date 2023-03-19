# python3

import heapq

def parallel_processing(n, m, data):
    output = []
    threads = [0] * n
    job_queue = [(0, i) for i in range(m)]
    heapq.heapify(job_queue)
    while job_queue:
        processing_time, job_index = heapq.heappop(job_queue)
        thread_index = threads.index(min(threads))
        start_time = threads[thread_index]
        output.append((thread_index, start_time))
        threads[thread_index] += processing_time
        if job_queue:
            next_processing_time, next_job_index = job_queue[0]
            while next_job_index == job_index:
                heapq.heappop(job_queue)
                if job_queue:
                    next_processing_time, next_job_index = job_queue[0]
                else:
                    break
    return output



def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    result = parallel_processing(n, m, data)
    for thread_index, start_time in result:
        print(thread_index, start_time)

    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
