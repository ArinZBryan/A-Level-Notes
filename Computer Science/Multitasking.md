## The Scheduler
***See '[The Operating System](The_Operating_System.md#schedulers-aka-job-scheduler)'***  

The operating system uses scheduling algorithms which allocate processing time to each task / process / thread that is currently needing to be service.
The scheduler may use one of five algorithms that we need to know.

* [Queue](Datastructures.md#queues) (aka first come first serve)- The order in which the tasks arrive, regardless of how long the tasks may take. Tasks which are time intensive may monopolize processor time.
* Shortest Job First - The scheduler will always prioritize jobs that are known to take the least time that is available. Jobs will then be executed in this order
* Round Robin - Each task is given a set amount of CPU time. Once this has elapsed, the job may be paused or completed, and the next job begun.
* Shortest Time Remaining - Like Shortest job first, except it takes into account how long it has left to be completely done
* Multi-level Feedback [queues](Datastructures.md#queues) - There are a number of different queues. Processes may move up and down queues in order of priority due to different factors.

When the CPU receives an [interrupt](./Interrupts.md#interrupts), the scheduler is usually paused, and the interrupt is handled before it can resume.

In practice, this is largely theoretical, as the actual processor time split is heavily influenced by what programs the user has open. As such, these more idealistic algorithms are largely reserved for background tasks.

## Processes
Each process represents one whole, or part of a program. On windows, each process is set up to render using windows UI, so it is inadvisable to start new processes when parallelism is needed. This does not apply to Unix derivatives however, where starting new processes is the faster way to go.

## Threads
A thread is always the child of a process. It can usually communicate only with the parent process though in some cases some important threads may be shared by multiple processes (such as a render thread), and can execute arbitrary program code. It is generally used for parallel compute. In windows, it is generally preferable to start new threads when more compute is necessary. 

## Handles
Much like how a thread is the child of a process, a handle is the child of a thread. Similarly, one thread may have many handles. However, these will only ever communicate with their parent thread.  

A 'Handle' can also refer to file handles, which are built using similar technology. They consist largely of a single pointer, and a promise to the program that the resources it is accessing is only being accessed by itself. This use of the work is not found in the A-Level specification.

## Concurrency
***See [Pipelining](Computer%20Science/Fetch,%20Decode,%20Execute,%20Reset%20Cycle)***
The idea of a computer process performing operations in parallel.
Generally, multiple processes / threads / handles will be running concurrently
