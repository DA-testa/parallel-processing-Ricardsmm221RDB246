# python3

import heapq

import heapq

def parallel_processing(n, m, data):
    # create a priority queue of (available_time, thread_id)
    queue = [(0, i) for i in range(n)]

    # create a list to store the output pairs
    output = []

    for job_id, job_time in enumerate(data):
        # get the earliest available thread from the priority queue
        available_time, thread_id = heapq.heappop(queue)

        # calculate the time when the job will be completed
        start_time = max(job_time, available_time)
        finish_time = start_time + job_time

        # add the output pair to the output list
        output.append((thread_id, start_time))

        # add the thread back to the priority queue with the updated available time
        heapq.heappush(queue, (finish_time, thread_id))

    return output




def main():
    # read input from the user
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # call the parallel_processing function
    result = parallel_processing(n, m, data)

    # print the output pairs
    for thread_id, start_time in result:
        print(thread_id, start_time)


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
