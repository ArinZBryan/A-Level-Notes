### ~1940s
All processors that exist today are based on the original design of Von Neumann in the 1940s
Programming involved binary representation used to represent machine code instructions that consist of two parts
* Opcode      - The instruction
* Operand     - Pointer to memory

Each individual processor in existence has its own instruction set.

There was no ASM, so Programming involved manipulating the bits by hand.

### ~1950
ASM invented. ASM is a partially readable language that can be easily translated into machine code.

#### Inside the CPU there are a number of registers.
* Specific registers to perform a single task
* General purpose registers to store the content of currently running programs

#### Registers
* Program Counter - stores the address of the next instructions
* Memory Address Register - stores the address of the next data item to be fetched from memory.
* Memory Data Register - Stores the contents of the data item specified by the MAR
* Current Instruction Register - Stores the binary representation of the next instruction to be decoded
* Control Unit - Houses the clock (sometimes) and synchronizes the operations of the CPU
* ALU - Performs arithmetic, and bitwise operations
    - Can perform only Addition, Bit Shifts, and other bitwise operations

#### Registers in the ALU
* Complimentor
* Shifter
* Status flag

## A Von Neumann Processor must have:
* only one stage pipeline and one logical core (only one part of the [FDER Cycle](Fetch,%20Decode,%20Execute,%20Reset%20Cycle.md) at a time)
* instructions and data share the same memory

In the 50's this was fine, but as time passed, a problem came to light.
This problem is known as the Von Neumann bottleneck - that an instruction can only be executed after the last had completely finished. This bottleneck was fixed by adding more wire between main-memory and the CPU. This allowed for basic parralelism (concurrency of operations in this case) thus, increasing throughput of instructions.

By the 70s, personal computers became more available in the home.
with it, computer games became far more prevalent, as the challenges of rendering graphics came to the fore.

Processors were developed which are more specialized (array processors, DMA processors, coprocessors)
Memory in terms of sharing between instructions and data items.
further changes such as FPUs and GPUs and the parralelism that comes with that (pain)
* CISC -> Complex instruction set computer
* RISC -> Reduced instruction set computer

### Harvard Processors
Theses are generally like Von-Neumann, except that program memory (rom) and runtime memory (ram) are stored separately. This may take the form of different memory chips, a separated address space, or both.

## CISC vs RISC

#### CISC
- Multi-cycle instructions
- Variable format instructions (arm vs thumb)
- Various addressing Modes
- SIMD for processing large datasets in parallel
- Lower MIPS, but more actual instructions are executed in the same time.

#### RISC
- Single-cycle instructions
- Single format instructions
- Various addressing modes
- Higher MIPS, but lower actual instructions are executed in the same time.