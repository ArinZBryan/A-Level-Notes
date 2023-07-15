## Components of a modern(ish) desktop
- CPU / This is the CPU, what else is there to say?
- Motherboard / contains the chipset, and any options of expansion, such as DIMM sockets
- GPU or iGPU / Does the interfacing between the computer and the display. It is also used to build frames from vertices and matrices
- Chipset / A coprocessor that interfaces with much of the hardware on the motherboard. They can come in two variants
  * Northbridge - Interfaces between the RAM and the CPU  (This is usually integrated onto the CPU nowadays)
  * Southbridge - Interfaces between all other devices and the CPU. (The CPU may sometimes perform some or all of the tasks of the southbridge natively)
- PSU / The power supply, usually supplies 12v, 12v(stdby), 5v, 3.3v
- Storage / non-volatile storage of varying speeds.
  * HDD / Spinning magnetic disks, which can be read by a magnetic head. Generally slow
  * SSD / Solid state (no moving parts) which consist of DRAM chips, a controller, and sometimes a cache of RAM

## Virtual Machines
A virtual machine is a program that can entirely simulate a physical machine. Sometimes this is done using only software, though in some cases dedicated hardware may be passed through to them.

Generally, the machines that VMs are run on have hardware that is more powerful than the machine it is virtualizing. It is expected that there will generally be significantly more ram, and usually several more processing cores.

Though this is generally used to run x86/x64 machines, it may also be used to run a machine of any architecture. In the case of running a foreign architecture, it is generally called 'emulation' and almost always, everything must be simulated in software, as the processor architecture and peripherals may be of a completely different one to the host machine.

Virtual machines are most commonly found as part of a datacentre. These can then be rented out, and connected to over the internet using FTP and SSH. In these datacentres, one physical computer may have upwards of 32 cores, and a TB of RAM.

Virtual machines may be used to make an environment that is like a 'pseudo-dual-booting environment' However, unlike a real dual booting environment, almost everything is handled in software, which will result in a far slower machine overall.

Virtual machines are also used to standardize running / testing environments for CI. This is generally done via the use of Docker, and docker containers of small Linux VMs.

## Virtual Machines' application in programming
Generally, when a high-level language is translated to be compatible with the instruction set of the machine it is running on. This is the generally accepted paradigm of compiled programs.

However, some compiled programs (and most interpreted programs) are first compiled to an arbitrary bytecode. This bytecode is then run on a virtual machine that is built specifically for the physical machine it is running on. Though this is generally slower, it has become increasingly common, as it allows for a 'write once, run anywhere' approach, which can severely cut down on development time for a product.

An example of this is the JVM, on which Java bytecode can be run, the various implementations of WebAssembly, or the CLR, on which C# and F# bytecode can be run.

This is similar to JIT compiling, and may be combined with it to allow for even faster speeds. In fact, the JVM and CLR are largely just JIT compilers for their respective bytecodes.