## From source to executable
There are three (five, but the first may not be needed at A-Level, and the third is generally part of the second) stages of compilation that code must pass through to get from a source text file to an executable
#### 1. The Preprocessor
> At A-Level, this is lumped in with the lexer
- Removes comments and whitespace
- Runs preprocessor directives
	- `#include`, `#define`, ect.
#### 2A. The Lexer
- Parses through the code, character by character and tokeniseses the code. This is called *lexical analysis*
- This finds *keywords*, *operators*, *variables*, *literals* (aka compile-time constants) and *assignments*. This is done purely using pattern recognition, and so it is possible for faulty code to make it past this section.
- These are then converted into a list format for each line. This defines the order of operations to be performed.
- Variables' scope is defined in a separate dictionary. This allows for variables to be kept to their scope. It is called the 'data dictionary' or 'symbol table'. It contains metadata about the variables in the program
> Note that the symbol table generated specifies more than just scope. It also specifies the type of element that the symbol is (function / variable). If the symbol is a variable, a type / class may be specified in static languages. If the symbol is a function, then the function's signature is specified (parameters, their types and return types)
#### 2B. The Syntax Analyser
>This is generally implemented as part of the lexer or compiler.
> It has not been included as part of the three (five) stages as it generally is a part of the lexer (or sometimes compiler). It was originally included in the three as given by Mr T.
- Check to see if keywords used in the program code are correct
- Check if the grammar conforms with the required grammar for the language.
    - BNF (Backus-Naur Form) is a way of specifying the grammar of a programming language. It defines the rules which a must be followed in order for source code to be syntactically correct.
#### 2C. Creating the AST
> Like the syntax analyser, this is generally implemented as part of the lexer as opposed to the syntax analyser or as an independent stage.
- The AST (Abstract Syntax Tree) is a tree created from the list of instructions where the order of precedence of instructions is established.
- The nodes at the bottom of the tree are requirements for the nodes above them.
- To execute or compile this a depth- first sweep of the entire tree is used.
- All maths is converted to RPN (Reverse Polish Notation), which is based on the token and tree structure.
- The result of this step is an object file `*.o` or `*.obj`, these may be linked together with various libraries to make the entire codebase to be compiled.
#### 3. The compiler
- The compiler, depending on setting, will go through many rounds of optimization of the AST. In some cases, such as when using `-O2` this can be upwards of 50 steps long. Using `-OFast` or `-O3` are even longer, and may result in code optimized too far, such that it no longer works.
- The optimizing part of the compiler can be said to have performed semantic analysis. For this reason, it may be called the _semantic analyser_. This also results in new code being generated once this is done. As a result of performing code generation, it may also sometimes be called the _code generator_.
> This is considered a separate step from the compiler only by Mr. T. In optimizing compilers, it is generally not a separate step.
- The compiler can now begin to translate the higher-level code to the relevant assembly. Generally, each line of a higher-level language will correspond to multiple lines of assembly, though this is not always true. (i.e. `a & b` would translate to a single bitwise and instruction as long as `a` and `b` were in the registers)