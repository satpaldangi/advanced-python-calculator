# Statement of Purpose: Advanced Python Calculator

## 1. Problem Statement
Basic calculations are an everyday requirement for students, engineers, and general users. Standard command-line evaluation scripts often lack structured user interfaces, error management, and interactive loops, leading to program crashes upon unexpected inputs (such as dividing by zero or taking square roots of negative numbers). There is a need for a lightweight, interactive, user-friendly, and robust command-line calculation tool that handles common mathematical operations smoothly while maintaining state through continuous execution and preventing runtime crashes through basic error validation.

## 2. Scope of the Project
The scope of the **Advanced Python Calculator** project includes:
* **Interactive CLI Interface:** A terminal-driven interface featuring clear screen rendering, operation menus, and prompt navigation.
* **Core Mathematical Operations:** Support for fundamental arithmetic (addition, subtraction, multiplication, division), exponential powers, percentage computations, and square roots.
* **Built-in Error Handling:** Input validation and defensive checks for mathematical edge cases, including division by zero and operations on invalid ranges (e.g., negative numbers under square roots).
* **Execution Loop & Control Flow:** Continuous operational loop allowing sequential operations until explicit exit by the user.

*Out of Scope for Current Version:* Graphical User Interfaces (GUI), storage of calculation history to external databases/files, symbolic mathematics, and multi-variable equation solvers.

## 3. Target Users
* **Students & Educators:** Individuals seeking a simple, clear, and dependable command-line utility to compute mathematical expressions quickly without launching complex software.
* **Developers & Testers:** Users looking for a light modular script demo for simple utility tasks or terminal-based interactive workflows.
* **General Users:** Anyone needing standard arithmetic and scientific calculations directly within a terminal environment.

## 4. High-Level Features
* **Interactive Menu System:** Clean console UI formatted with dynamic terminal clearing to provide a distraction-free experience.
* **Arithmetic & Power Engine:** Fast evaluation of basic calculations ($a + b$, $a - b$, $a \times b$, $a / b$) and exponentiation ($a^b$).
* **Percentage Evaluator:** Dedicated function to compute the exact percentage fraction of a given target value.
* **Square Root Calculator:** Integrates standard mathematical operations (`math.sqrt`) with guard conditions for negative values.
* **Graceful Exception Control:** Explicit safety messages on zero-division attempts or negative inputs to maintain program continuity without breaking the event loop.
* **Clean Session Termination:** Explicit menu choice allowing users to terminate execution cleanly.
*