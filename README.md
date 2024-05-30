# GitHub Lab 3: Recursive Tower of Hanoi

## Student Information

* Name
* Semester/Year
* CRN

## Description

The Tower of Hanoi is a classic mathematical puzzle that consists of three pegs and a number of disks of different sizes. The goal of the puzzle is to move all the disks from the starting peg to the target peg while following these rules:

1. Only one disk can be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.
3. In this version of the game, the source peg will be the left most peg and the target to finish the game will be the right most peg.

```text
    |          |          |
   ===         |          |
    |          |          |
  =====        |          |
    |          |          |
 =======       |          |
---------  ---------  ---------
    A          B          C
```

## Instructions

In this lab, you will implement the function `tower_of_hanoi()` to solve the Tower of Hanoi puzzle using recursion. The function should take the number of disks as input and print the step-by-step instructions to move the disks from the starting peg to the target peg. As you proceed through the game, it should count the number of moves made during the recursion and return that value back. For example, three disks will have a minimum of 7 moves to complete the game.

The `main()` function will accept user input for an integer value and will output the messages as part of the `tower_of_hanoi()` function as well as a total number of moves. The output messages will include:

1. `Move disk # from peg ORIGIN to peg TARGET`, were the # is the disk number, ORIGIN is the disk source starting point, and TARGET is the disk is target to move to.
2. `Total moves: #`, were # is the total number of moves that took place during the recursion.

The Tower of Hanoi puzzle can be efficiently solved using recursion. The recursive algorithm follows these steps:

1. If there is only one disk, move it directly from the starting peg to the target peg.
2. If there are more than one disk, follow these steps recursively:
   a. Move the top n-1 disks from the starting peg to the auxiliary peg.
   b. Move the largest disk from the starting peg to the target peg.
   c. Move the n-1 disks from the auxiliary peg to the target peg.

### Tips

* Give the [Tower of Hanoi](https://www.mathsisfun.com/games/towerofhanoi.html) a try at Math is Fun and think about each component as you play.
* Do not modify the provided prompt inside the `input()` statement.
* Read the Unit Test to see how it will be tested in pytest then break the programming down incrementally into smaller elements.
* Zero points will be awarded for the entire lab if recursion is not used.

---

## Lab Questions

Do not provide code for any of the questions. You need to provide answers to each of the questions in normal written language answering each of the questions.

### Question 1

**Explain the base case and recursive step in the Tower of Hanoi recursive algorithm.**

YOUR ANSWER HERE

### Question 2

**How does recursion help in solving the Tower of Hanoi puzzle?**

YOUR ANSWER HERE

### Question 3

**What is the time complexity of the recursive Tower of Hanoi algorithm, and why does it grow exponentially with the number of disks?**

YOUR ANSWER HERE

### Question 4

**Suppose you have five disks in the Tower of Hanoi puzzle. How many moves would be required to solve the puzzle using the recursive algorithm?** Hint, you must give me the formula with solution, not just the answer. Knowing the time complexity will help you identify the formula and answer

YOUR ANSWER HERE

---

## Assistance at Rio Hondo

Need help? Contact the [Math, Science, & Engineering Center](https://www.riohondo.edu/mathematics-and-sciences/math-science-center/) for tutoring assistance. Any form of sharing or uploading of this assignment on external websites is strictly prohibited.

## Rubric / Grading Criteria

See [Canvas](https://riohondo.instructure.com) for specific points breakdown in the assignment rubric.

Grading is done via a combination of automatic grading in GitHub and manual testing by the instructor. Points may be deducted based on the following criteria:

* Must contain working Python code
  * Code follows all instructions listed above
  * Code is well structured, formatted, and commented
  * Code is able to be manually run without errors
  * Code uses concepts as covered in the current topic for the lab
  * Provided unit tests pass test with partial credit available for 1 or more passed tests
* More than 1 commit made by the student per GitHub Repo
* Tools such as the Measure of Software Similarity (MOSS) may be used to detect plagiarism

Points may still be deducted based on the grading criteria above even if the assignment passes the Auto Grading unit tests. **Creating code that is well structured, formatted, and commented cannot be tested automatically. So you can pass all your auto grading tests, but still lose points.**

## Testing & Auto Grading

Always try running your code in your local environment before submitting for grading and use the provided criteria for testing. Troubleshooting and debugging code is a process that you must learn to be an effective programmer as you will not be given test cases in real world programming, you will have to write them yourself. Find more information on testing on the code read the [TESTS.md](TESTS.md) file.

Auto Grading may use a combination of automated Input/Output testing, Unit Tests using pytest, or both via GitHub Classroom depending on the assignment. Scores in GitHub are not communicated to your Canvas lab assignment. The instructor must still manually grade each one then enter a grade.
