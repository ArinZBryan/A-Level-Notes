This refers to the way in which the [operating system](The%20Operating%20System.md) directs and retrieves data items held in memory

[Machine code](Fetch,%20Decode,%20Execute,%20Reset%20Cycle.md#Decode) instructions consist of two parts, the opcode and operand. The operand may contain either an address in memory from which data should be loaded, or a literal value to be used.

There are four (five) different modes of addressing:

## 1. Immediate Addressing (Pass by Value)
This refers to where the data is kept as part of the operand. This is roughly analogous to passing a variable by value. In some cases, even smaller `struct` instances can be kept entirely in registers and operands, though usually, this is just used for `uint`, `single` and `double` instances.
```c++
int value = 3;
```
## 2. Direct Addressing
This refers to the address reference (memory address) where the item is located. The value is then loaded from this place in memory. More specifically, the pointer to the item is the operand, and from there, the value is loaded.
```c++
int value = *(int*)0xdeadbeef;
```

## 3. Indirect Addressing (Pass by Reference)
This refers to the use of pointers. The operand contains the address of a variable (This is [direct addressing](#2-direct-addressing)) that contains the memory address of the desired value. This variable is called a pointer, and may have any type associated with it, though they are usually actually just a <code>uint64</code> or <code>uint32</code> depending on whether thy system is 32 or 64bit. [Linked Lists](./Datastructures.md#linked-lists) and [Graphs](./Datastructures.md) requires such indirect addressing. 

In the exam, when indirect addressing is being used, the memory address of the pointer is prefixed with an '@' symbol (eg. <code>LDA @4F72</code>)
```c++
int value = *valuePointer;
```

## 4. Indexed Addressing (Iterators & SIMD)
This is used to load multiple data items into the CPU, usually for SIMD commands. Generally, this would be most appropriate when dealing with arrays or hashmaps (dictionaries). A base address of the start of the array is held, and an offset is then added to determine the actual address of the desired data. This is often incremented, to iterate through the array.
```c++
int value = *(valuePointer + index);
```

## 5. Relative Addressing
This is refers to the jumping to the next instruction. It is specific to jumping by offset (i.e., jump 20B ahead) as opposed to jumping to an immediate address