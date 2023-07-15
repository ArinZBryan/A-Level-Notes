## From source to executable
There are three (five, but the first may not be needed at A-Level, and the third is generally part of the second) stages of compilation that code must pass through to get from a source text file to an executable
<dl>
    <dt><b>1. The Preprocessor</b><dt>
    <blockquote>At A-Level, this is lumped in with the lexer</blockquote>
    <dd><li>Removes comments and whitespace</li><dd>
    <dd><li>Runs preprocessor directives</li>
        <ul>
            <li>#include, #define, ect.</li>
        </ul>
    <dd>
    <dt><b>2. The Lexer</b></dt>
    <dd><li>Parses through the code, character by character and tokeniseses the code. This is called <i>lexical analysis</i></li></dd>
    <dd><li>This finds keywords, operators, variables and literals (aka compile-time constants). This is done purely using pattern recognition, and so it is possible for faulty code to make it past this section.
    <blockquote>There is a fifth thing found: assignments. Though these are generally included as part of the operators, they are kept separate as part of the A-Level</blockquote>
    <ul>
        <li>These are then converted into a list format for each line. This defines the order of operations to be performed.</li>
        <li>Variables' scope is defined in a separate dictionary. This allows for variables to be kept to their scope. It is called the 'data dictionary' or 'symbol table'. It contains metadata about the variables in the program</li>
        <blockquote>Note that the symbol table generated specifies more than just scope. It also specifies the type of element that the symbol is (function / variable). If the symbol is a variable, a type / class may be specified in static languages. If the symbol is a function, then the function's signature is specified (parameters, their types and return types)</blockquote>
    </li></dd>
    <dt><b>2A.  The Syntax Analyzer</b></dt>
    <blockquote>This is generally implemented as part of 
    the lexer or compiler.</blockquote> 
    <br/>
    <blockquote>It has not been included as part of the three (five) stages as it generally is a part of the lexer (or sometimes compiler). 
    It was originally included in the three as given by Mr T.
    </blockquote>
    <dd><li>Check to see if keywords used in the program code are correct</li></dd>
    <dd><li>Check if the grammar conforms with the required grammar for the language.
        <ul>
            <li>BNF (Backus Naur Form) is a way of specifying the grammar of a programming language. It defines the rules which a must be followed in order for source code to be syntactically correct,
            </li>
        </ul>
    </li></dd>
    <dt><b>2B. Creating the AST</b><dt>
    <blockquote>Like the syntax analyzer, this is generally implemented as part of the lexer as opposed to the syntax analyzer or as an independent stage.</blockquote>
    <dd><li>The AST (Abstract Syntax Tree) is a tree created from the list of instructions where the order of precedence of instructions is established.</li><dd>
    <dd><li>The nodes at the bottom of the tree are requirements for the nodes above them.</li></dd>
    <dd><li>To execute or compile this a depth-
    first sweep of the entire tree is used.</li><dd>
    <dd><li>All maths is converted to RPN (Reverse Polish Notation), which is based on the token and tree structure.</li></dd>
    <dd><li>The result of this step is an object file <code>*.o</code>, these may be linked together with various libraries to make the entire codebase to be compiled.</li></dd>
    <dt><b>3. The Compiler</b><dt>
    <dd><li>The compiler, depending on setting, will go through many rounds of optimization of the AST. In some cases, such as when using <code>-O2</code> this can be upwards of 50 steps long. Using <code>-OFast</code> or <code>-O3</code> are even longer, and may result in code optimized too far, such that it no longer works.</li></dd>
    <dd><li>The optimizing part of the compiler can be said to have performed semantic analysis. For this reason, it may be called the <i>semantic analyzer</i>. This also results in new code being generated once this is done. As a result of performing code generation, it may also sometimes be called the <i>code generator</i>.</li></dd>
    <blockquote>This is considered a separate step from the compiler only by Mr. T. In optimizing compilers, it is generally not a separate step.</blockquote>
    <dd><li>The compiler can now begin to translate the higher-level code to the relevant assembly. Generally, each line of a higher-level language will correspond to multiple lines of assembly, though this is not always true. (ie. <code>a & b</code> would translate to a single bitwise and instruction as long as <code>a</code> and <code>b</code> were in the registers)</li></dd>
</dl>