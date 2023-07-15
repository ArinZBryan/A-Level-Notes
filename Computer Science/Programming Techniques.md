
## Procedural Programming
A type of programming typified by a style without flair - the code is just a series of well thought out steps and procedures. It contains a systematic order of statements, functions and commands. to complete a task. This style of programming generally has a few problems; these include:
1. Code written in this style tends to be harder to debug
2. Most data items are stored in more complex data structures (arrays, tuples, etc.)
3. Working with external modules and keeping variables private - management of scope is not always easy
4. In certain application, such as simulation or games, the series of events may not be clearly defined.

## Object-Oriented Programming
A type of programming typified by a style based around real-world objects or events.
For example, each object or class has attributes and methods.
When complex projects simulating many different items or objects interacting with each other are needed, OOP can be very useful.

### Related Definitions
- **Classes**  
    A class is a template upon which objects (class instances) are created. This definition of classes is most typified by JavaScript's treatment of classes as prototypes and use of prototypical inheritance. Classes will contain different attributes and methods.  
    Another definition of classes is that a class is a group of functions or subroutines, which are related through the use of the same variables (now called attributes). This is also referred to as the template instance of an object.
- **Methods**  
    A subroutine or function which works inside the object or class. Some methods can be used as ways of altering the behaviour of a given class (getters and setters).
- **Objects**
    An object is an instance of a class, i.e.. a copy of the data following the formula laid out by the class. This allows it to use various methods (class/static methods do not apply)
- **Attributes**  
    A variable / data structure that is shared across methods in an object
- **Instantiation**  
    The act of creating a copy of a given class, using that class as a base. This requires some form of constructor (or factory) to work.
- **Polymorphism**  
    Also known as method overloading, this is only made possible by use of name-mangling. It involves defining a function multiple times with different arguments or return types, with the correct version of the method chosen by the compiler at compile time.
- **Inheritance**  
    Inheritance is the act of creating a sub-class (child class). This also designates the top-level class as the parent (also known as the super class).
- **Encapsulation**
    Containing all the attributes and methods relating to a task in one part of a module. May also refer to the ability to make attributes / methods private to their given class.

### Writing Classes in Pseudocode
For a generic class for an orbiting body `OrbitingBody`, the class declaration in pseudocode is as follows:

```c
class OrbitingBody()
    public string name
    public float circumference
    public float radius
    public float avgTemp
    public procedure new(Name, Circumferece, Radius, AvgTemp)
        name = Name
        circumference = Circumference
        radius = Radius
        avgTemp = AvgTemp
    endprocedure
endclass
```
***NOTE***: The constructor ***MUST*** be marked as a ***PROCEDURE***, however, the `public` tag is considered optional.

***NOTE***: To instantiate a class, use the syntax:
```c
object1 = new ClassName(arg1, arg2, ... )
```

## Functional Programming
It exists, but is too maths-oriented to be discussed as part of the computer-science A-Level. Google it. Or don't. I don't care.