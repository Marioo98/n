#!/usr/bin/env python3
# GitHub Lab 3: Recursive Tower of Hanoi

# Import Modules
import main as app

# Global Variables
value_input = []
value_actual = []
expected_msg = {
    1: ["Move disk 1 from peg {p1} to peg {p3}"],
    2: ["Move disk 1 from peg {p1} to peg {p2}","Move disk 2 from peg {p1} to peg {p3}","Move disk 1 from peg {p2} to peg {p3}"],
    3: ["Move disk 1 from peg {p1} to peg {p3}","Move disk 2 from peg {p1} to peg {p2}","Move disk 1 from peg {p3} to peg {p2}","Move disk 3 from peg {p1} to peg {p3}",
        "Move disk 1 from peg {p2} to peg {p1}","Move disk 2 from peg {p2} to peg {p3}","Move disk 1 from peg {p1} to peg {p3}"],
    4: ["Move disk 1 from peg {p1} to peg {p2}","Move disk 2 from peg {p1} to peg {p3}","Move disk 1 from peg {p2} to peg {p3}","Move disk 3 from peg {p1} to peg {p2}",
        "Move disk 1 from peg {p3} to peg {p1}","Move disk 2 from peg {p3} to peg {p2}","Move disk 1 from peg {p1} to peg {p2}","Move disk 4 from peg {p1} to peg {p3}",
        "Move disk 1 from peg {p2} to peg {p3}","Move disk 2 from peg {p2} to peg {p1}","Move disk 1 from peg {p3} to peg {p1}","Move disk 3 from peg {p2} to peg {p3}",
        "Move disk 1 from peg {p1} to peg {p2}","Move disk 2 from peg {p1} to peg {p3}","Move disk 1 from peg {p2} to peg {p3}"],
    5: ["Move disk 1 from peg {p1} to peg {p3}","Move disk 2 from peg {p1} to peg {p2}","Move disk 1 from peg {p3} to peg {p2}","Move disk 3 from peg {p1} to peg {p3}",
        "Move disk 1 from peg {p2} to peg {p1}","Move disk 2 from peg {p2} to peg {p3}","Move disk 1 from peg {p1} to peg {p3}","Move disk 4 from peg {p1} to peg {p2}",
        "Move disk 1 from peg {p3} to peg {p2}","Move disk 2 from peg {p3} to peg {p1}","Move disk 1 from peg {p2} to peg {p1}","Move disk 3 from peg {p3} to peg {p2}",
        "Move disk 1 from peg {p1} to peg {p3}","Move disk 2 from peg {p1} to peg {p2}","Move disk 1 from peg {p3} to peg {p2}","Move disk 5 from peg {p1} to peg {p3}",
        "Move disk 1 from peg {p2} to peg {p1}","Move disk 2 from peg {p2} to peg {p3}","Move disk 1 from peg {p1} to peg {p3}","Move disk 3 from peg {p2} to peg {p1}",
        "Move disk 1 from peg {p3} to peg {p2}","Move disk 2 from peg {p3} to peg {p1}","Move disk 1 from peg {p2} to peg {p1}","Move disk 4 from peg {p2} to peg {p3}",
        "Move disk 1 from peg {p1} to peg {p3}","Move disk 2 from peg {p1} to peg {p2}","Move disk 1 from peg {p3} to peg {p2}","Move disk 3 from peg {p1} to peg {p3}",
        "Move disk 1 from peg {p2} to peg {p1}","Move disk 2 from peg {p2} to peg {p3}","Move disk 1 from peg {p1} to peg {p3}"]
}

def mock_input(prompt):
    "Mock the Input Process"
    global value_input, value_actual
    value_actual.append(prompt)
    return str(value_input.pop(0))

def run_main_program():
    "Run the main() program and capture the results"
    global value_input, value_actual

    # Overwrite the input() function
    app.input = mock_input

    # Overwrite the print() function with 1 argument in the print()
    app.print = lambda arg1 : value_actual.extend([arg1])

    # Execute the main() function from the code
    app.main()

    return value_actual

def test_case1():
    "Case 1: Test the number of Moves Returned"
    assert app.tower_of_hanoi(1, 'A', 'C', 'B') == len(expected_msg[1])
    assert app.tower_of_hanoi(2, 'R', 'T', 'S') == len(expected_msg[2])
    assert app.tower_of_hanoi(3, 'X', 'Z', 'Y') == len(expected_msg[3])
    assert app.tower_of_hanoi(4, 'M', 'O', 'N') == len(expected_msg[4])
    assert app.tower_of_hanoi(5, 'B', 'D', 'C') == len(expected_msg[5])

def test_case2(capsys):
    "Case 2: Test that the correct messages are printed during the function call only"
    
    # 1 Disk
    app.tower_of_hanoi(1, 'B', 'D', 'C')
    captured = capsys.readouterr()
    expected_output = "\n".join(expected_msg[1]).format(p1="B",p2="C",p3="D")+"\n"
    assert captured.out == expected_output

    # 2 Disks
    app.tower_of_hanoi(2, 'M', 'O', 'N')
    captured = capsys.readouterr()
    expected_output = "\n".join(expected_msg[2]).format(p1="M",p2="N",p3="O")+"\n"
    assert captured.out == expected_output

    # 3 Disks
    app.tower_of_hanoi(3, 'X', 'Z', 'Y')
    captured = capsys.readouterr()
    expected_output = "\n".join(expected_msg[3]).format(p1="X",p2="Y",p3="Z")+"\n"
    assert captured.out == expected_output

    # 4 Disks
    app.tower_of_hanoi(4, 'R', 'T', 'S')
    captured = capsys.readouterr()
    expected_output = "\n".join(expected_msg[4]).format(p1="R",p2="S",p3="T")+"\n"
    assert captured.out == expected_output

    # 5 Disks
    app.tower_of_hanoi(5, 'R', 'O', 'I')
    captured = capsys.readouterr()
    expected_output = "\n".join(expected_msg[5]).format(p1="R",p2="I",p3="O")+"\n"
    assert captured.out == expected_output

def test_case3():
    "Case 3: Test for Known Input Values"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["3"]
    value_actual = []
    expected_output = ["# of Disks: "]
    for i in range(len(expected_msg[int(value_input[0])])):
        expected_output.append(expected_msg[int(value_input[0])][i].format(p1="A",p2="B",p3="C"))
    expected_output.append(f"Total moves: {len(expected_msg[int(value_input[0])])}")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == expected_output

def test_case4():
    "Case 4: Test for Known Input Values"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["4"]
    value_actual = []
    expected_output = ["# of Disks: "]
    for i in range(len(expected_msg[int(value_input[0])])):
        expected_output.append(expected_msg[int(value_input[0])][i].format(p1="A",p2="B",p3="C"))
    expected_output.append(f"Total moves: {len(expected_msg[int(value_input[0])])}")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == expected_output

def test_case5():
    "Case 5: Test for Known Input Values"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["5"]
    value_actual = []
    expected_output = ["# of Disks: "]
    for i in range(len(expected_msg[int(value_input[0])])):
        expected_output.append(expected_msg[int(value_input[0])][i].format(p1="A",p2="B",p3="C"))
    expected_output.append(f"Total moves: {len(expected_msg[int(value_input[0])])}")

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == expected_output

def test_case6():
    "Case 6: Test for Invalid Input Value"
    
    # Setup IO Variables
    global value_input, value_actual
    value_input = ["three"]
    value_actual = []
    expected_output = ["# of Disks: ", "Please enter a valid number of disks to start the game."]

    # Save Result of Main Program Execution
    value_actual = run_main_program()

    # Test the Actual result equal to the Expected result
    assert value_actual == expected_output