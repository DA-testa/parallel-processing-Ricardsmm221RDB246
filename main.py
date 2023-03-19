# python3

import heapq

import heapq

def parallel_processing(n, m, data):
    # create a list to store the output pairs
    output = []

    # create a list to keep track of which threads are currently processing jobs
    processing = [False] * n

    for job_id, job_time in enumerate(data):
        # find the next available thread
        thread_id = next(i for i in range(n) if not processing[i])

        # calculate the start time for the job
        start_time = max(job_id, max(output[i][1] for i in range(len(output)) if output[i][0] == thread_id))

        # update the processing list and add the output pair to the output list
        processing[thread_id] = True
        output.append((thread_id, start_time))

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
