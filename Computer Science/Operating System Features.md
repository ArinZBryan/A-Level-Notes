## Utility Programs

#### Defragmentation Programs
- Runs over several passes, collating files and groups of related files into close physical proximity on the disk. 
- Often these groups may be organized by file metadata such as name, author, file structure and frequency of access.
- This should only be used on mechanical drives, and not on solid state drives as it can shorten their longevity.

#### Compression Programs
- Reduces the size of the file either on disk or in a buffer to be transmitted.
- This may use one of two types of compression:
    - **Lossy**  
        Permanent loss of data held in the file. This will affect the quality of the file in some way, and depending on the quantity of data removed, this may be more or less noticeable  
    - **Lossless**  
        No loss of data in the file. Various algorithms are used to find patterns in the data of the file, and use those to reduce the total file size.  
        ***See [Compression Algorithms](./Algorithms_Compression.md)***   

#### Backup Programs
- May create a complete copy of the disk image, or may backup changes incrementally.

#### Anti-Malware Programs
- Scans RAM and Secondary storage for files.
- Checks these files against a known good database of malware files.
- Removes / Isolates any programs / files that match. 
- May attempt to repair files affected by malware.
- Often uses AI / "heuristics" to determine which files are unwanted.  
> Heuristics are the properties of a file.  
> Heuristics are a way to use known matches to find similar programs using patterns obtained from the known good match.
- Firewalls perform similar tasks, though they monitor incoming network traffic.

#### Encryption Programs
- Takes an item of data (usually a network packet or file) and scramble it into a form that is unrecognizable to any third parties to the transaction.
- To 'unscramble' or encrypt the file, the recipient must have a 'key' 
- An algorithm can be applied to change the data item into a scrambled (encrypted) form.

### User Interfaces
##### Graphical User Interfaces (GUI)
This is the most common type of user interface in the modern day. In a GUI, users must interact via touch or mouse input predominantly. As such, it can be very flexible, and easy to learn. However, due to limited screen real-estate, only so much information can be surfaced to the user at once, limiting the speed of interaction with a graphical user interface.
##### Text User Interface (TUI)
A text user interface is similar in concept to a GUI, involving surfacing information to the user via the use of some sort of graphic. However, in the case of a TUI, this is done via using large walls of text, usually in the terminal. This also means that most movement and selection must be done via the keyboard rather than the mouse. One example of this is VIM, and its derivatives which run in the terminal.
##### Command Line Interface (CLI)
A command line interface is a method of interacting with a program via 'arguments' and 'flags'. This type of interface is highly efficient, as very few movements need to be made by the user, and complex actions can be completed by typing names. Thus, this is the preferred method of the *poweruser* and also an easy way for programs to interact with each other.
