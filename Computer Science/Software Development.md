Software development is the process of creating, designing, deploying and supporting software. Software development has a 'lifecycle', which constitutes the  process by which software is developed. As a result, there are several approaches to the software development lifecycle.
-  Waterfall
	In waterfall development, each stage must be completely finished before moving on to the next. This style of software development was more popular in the early 2000s, but has fallen off since then.
- Agile
	In agile development, development is split up into 'sprints'. Each sprint goes through the whole of the software development lifecycle, but in miniature, and all are generally done around the same time.

## The steps of the software development lifecycle
#### Analysis
- Understand the user requirements
	Mostly carried out by a *systems analyst*. Systems analysts work closely with the client to extract as much information as possible.
- Understand the purpose of the software
- What are the functional requirements of the software.
	This may include creating a table of inputs and outputs (Example shown below)
	
| Inputs           | Processes       | Outputs           |
| ---------------- | --------------- | ----------------- |
| Pupil First Name | Validate Age    | List of usernames |
| Pupil Surname    | Create Username |                   |
| Pupil age        |                 |                   |
#### Design
- Systems Architects are commonly used here
- This process usually leads to a design specification. This is a document that may include:
	1. Inputs and Outputs
	2. Security Features
	3. Hardware
	4. UI
	5. Data Storage
- This design may include both a high-level design, where an overarching plan is described, as well as a low-level design, which includes how every feature should work.
#### Implementation
- In this stage, code may be developed in several iterations, where each iteration includes the following
	- Programming
	- Testing
	- Documentation
#### Evaluation
- Evaluation can be carried out throughout a development project to inform later stages. However, there is usually a formal evaluation when the project is complete. At this point, the system is evaluated in terms of:
	- Functionality — does it do what it is supposed to do?
	- Effectiveness — how well does it perform?
	- Usability — is it intuitive to use? Is it appropriate for its intended users?
	- Reliability — how robust is the system?
	- Maintainability — how easy is it to fix problems?
	- Extendibility — how easy will it be to add new functionality?
#### Maintenance
- Maintenance is the last phase of the software lifecycle.
- Here, once the software is in operation, bugs are fixed and some new features or abilities may be added

## Testing
There are several methods of testing
- White Box / Structural
	- This method of testing identifies all the branching points and computation and exhaustively tests them all, ensuring all outcomes have been tested.
- Black Box / Functional
	- Black box testing works by giving a set of input parameters and testing the function against test cases. As these test cases may not always cover all possibilities, this method is non-exhaustive, but much easier.
- Unit / Integration
	- One module of a system is tested, to ensure it works with either black or white box testing. Once this is done, and all tests are passing, the units are placed together, and tested as a system.
- Acceptance
	- Testing of boundary conditions. This may be bundled with unit tests or black/white box tests.
- System
	- This includes multiple stages of software testing
		- Alpha - Testing performed before releasing to the public or customers.
		- Beta - Testing performed once users have access to the product, by the users during use.

## Software Development Tooling
#### IDEs
*Integrated Development Environments*, or IDEs are pieces of software used when developing your own software. They contain a text-editor and a way to run the code you write. This however, is the bare minimum. Most IDEs will also include other tooling for services such as SCM/GIT, build and [compiler options](The%20Compilation%20Toolchain.md), debuggers and profilers. An example of a modern IDE is for example *Visual Studio 2022*.

Below is a more exhaustive list of features offered by modern IDEs. All of these are provided by Visual Studio 2022 (at least for C#)
1. Text Editor
2. LSP (Language Server)
	- Code Autocomplete
	- Jump To / Peek Definition
	- Jump To / Peek Usage
	- Symbol Rename
	- Code Refactor Tools
	- Syntax Highlights
3. Complier / Linker / Intrpreter
4. Source Control
5. Debuggers
6. Profiler
7. REPL / Live code environment
8. Language Documentation