An operating system manages the operation of the computer (duh.)

>Not all operating systems are capable of [multitasking](Multitasking.md). Those that cannot may not need such advanced memory or cpu management, as in those cases, device drivers and other critical functions may be largely managed by the program.

The operating system has the requirement of being able to:
- Manage memory (ram, cache and virtual memory) between programs (paging and segmentation)
    - ### Paging
        Paging uses fixed sizes of memory (usually around 4kb) each, and a process or file may be stored in several non-continuous pages. These pages are fixed, and cannot move once allocated, though they can be freed when not in use..  
        The use of paging is often extended to both RAM and [secondary storage](File%20Systems.md)
        In mechanical drives, the access of files split across many parts of the drive may result in drive thrashing, which may shorten the life of the drive.
    - ### Segmentation
        Segmentation is the logical division of address space into varying length segments, the length of these being function of the program structure ( if and when it calls malloc() ). The length of these segments may change during the runtime of a program. As a result, programs are almost always contained within only one segment (unless vMem/swap space is in use), resulting in largely sequential reads and writes which may speed up some iterative operations (though this really only matters when applied to an [HDD](File%20Systems.md) as it can in some cases cause disk thrashing, which is rare).
    - ### Intermediate Access Store (IAS)
        This includes the registers, cache, RAM and primary memory built into the computer. This is not a technique for managing memory, but a general term for the built in primary memory blocks.
- Provide a user interface to allow for some kind of user interaction, may come in the form of a GUI, TUI or Terminal. Any interaction between the user and the computer is facilitated by the operating system
- Provide a [file system](File%20Systems.md) (This is an example of a logical view / visualization, the files are not actually stored this way)
>A logical view or visualization is the process of assisting a human to understand a problem by its often visual representation
- Peripheral API management ([device drivers](#device-drivers)). This may include networking, and the song and dance required for that.
- User access management
- Split CPU time between programs (if [multitasking](./Multitasking.md))
- Managing ISRs (Interrupt Service Routines)
- Error Handling
### Device Drivers
A device driver is a piece of software that is used to translate signals between two pieces of hardware or software. If it is translating for a piece of software, then it may be called an API or [library](#system-libraries)
### Schedulers (aka Job Scheduler)
***See [Multitasking](Multitasking.md)***   
The operating system uses scheduling algorithms which allocate processing time to each task / process / thread that is currently needing to be service.
The scheduler may use one of five algorithms that we need to know  
* Queue (aka first come first serve)- The order in which the tasks arrive, regardless of how long the tasks may take. Tasks which are time intensive may monopolize processor time.
* Shortest Job First - The scheduler will always prioritize jobs that are known to take the least time that is available. Jobs will then be executed in this order
* Round Robin - Each task is given a set amount of CPU time. Once this has elapsed, the job may be paused or completed, and the next job begun.
* Shortest Time Remaining - Like Shortest job first, except it takes into account how long it has left to be completely done
* Multi-level Feedback queues - There are a number of different queues. Processes may move up and down queues in order of priority due to different factors.
### The Kernel
The lowest level of the operating system and the most vital. (Kernel can also refer to the lowest level of user access.)  
* It responds to [syscalls / kernel calls](#system-libraries), hardware interrupts, software interrupts, exceptions, controls and interacts with hardware using [drivers](#device-drivers), manipulates processor states and maps virtual addresses to programs.  
* Generally, this process is kept isolated, so that no untrusted code is run.
### System Libraries
These 'hook' into the kernel, and allow for certain very basic features to be accessed.
This term can also be applied to [device drivers](#device-drivers)
* An example may include access to the system clock, or the ability to allocate and copy memory
* In windows, these may take the form of *.dll files, though such dlls can be also applications
### Dual Booting
In some circumstances, it may be beneficial to have multiple bootable drives or partitions. These may contain the same or different operating system. Though similar to using a VM from a user facing perspective, it is entirely driven by hardware, and no virtualisation or emulation occurs. An example of this is the dual booting of Windows and some flavour of Linux.
### Different types of operating system

- **Real-Time**  
    Real-time operating systems are systems that must produce an answer or immediate response to a problem posed. These operating systems are generally used in mission-critical or life-threatening situations, such as on planes, or in hospitals for patients on life support.  
    _Real-Time processing systems_ - These are generally, embedded systems, monitoring values from physical sensors, and making changes in the real world using motors, servos and actuators.  
    _Interactive processing systems_ - These may only be pseudo-real time, ie. involving transactions. Each transaction may take place in real time with some user interaction
- **Distributed / Network**  
    The functionality of a network operating system is distributed over a number of multiple computer servers and devices. Though this may not qualify as an operating system in the traditional sense (it is pretty much just a network of computers in a data-centre-esque way), it is still one anyway.
    In some cases, the computers in this network may be able to pool and share system resources to form a far more powerful computer.
- **Embedded**  
    ***See [Machine Architecture](Machine%20Architecture.md)***   
    This type of operating system is generally purpose built to perform one or several fixed task. It may not have 'drivers' or other such concepts, as due to its purpose built nature, it will only ever run on one type of hardware.  
    In some cases these operating systems can be considered to be applications in of themselves. Despite this they often may contain a minimal or no user interface.  
    As with all embedded devices, the requirements to run the operating system are generally quite low, similarly, there is often no need to store data permanently.
- BIOS  
	This is not *really* a type of operating system. It would be more accurate to lump it in with embedded operating systems or even with real-time operating systems. However, it is largely distinct from the other operating systems that one may find running. It is a very simple operating system, usually stored on the motherboard, in some section of ROM/RAM which is booted into before booting the main operating system.
 
