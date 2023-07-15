## The role of interrupts
Interrupts can be defined as a routine which requires attention from the processor. Examples of interrupts can include malware, (D)DOS attacks, hardware failure or any signal deemed to be system critical.
Interrupts usually require some form of user input.

## Interrupts and their role in the [FDER cycle](Fetch,%20Decode,%20Execute,%20Reset%20Cycle.md)
At the end of each processor cycle, a check is made to see if there is any interrupts to handle.

```
is there anything I need to do?
    if is_interrupt
        if interrupt_priority > current_priority
            place current instructions and data in a stack
            Jump to interrupt service routine
            pop interrupt stuff off stack.
        else
            place interrupt in stack/
go back to beginning
```

For managing tasks across multiple logical cores, there is a job scheduler.  
A job scheduler is a program / algorithm / a set of algorithms that distributes jobs / interrupts across the various logical cores.  
In most cases, this is part of the operating system

## Common types of interrupts:
- Illegal Instruction encountered
- Division by zero
- Arithmetic overflow
- I/O registers (when not using polling)
- Buffer nearly full / empty (see stacks and queues as part of [Datastructures](Datastructures.md))
- Completion of a data transfer by a DMA or other such item.