# Python Basics — Lab Programs

Twelve beginner Python programs covering variables, control flow, functions, lists, graphs, and a student report card.

## Programs

| # | File | Description |
|---|------|-------------|
| 1 | `01_variables_datatypes.py` | Variables and data types (int, float, str, bool, list, tuple, dict, set) |
| 2 | `02_calculator.py` | Menu-driven calculator (+, −, ×, ÷, %, **) |
| 3 | `03_positive_negative_zero.py` | Check if a number is positive, negative, or zero |
| 4 | `04_largest_of_three.py` | Find the largest of three numbers |
| 5 | `05_print_1_to_10.py` | Print numbers from 1 to 10 (for / while / list) |
| 6 | `06_multiplication_table.py` | Multiplication table of a given number |
| 7 | `07_tables_1_to_10.py` | Multiplication tables from 1 to 10 |
| 8 | `08_circle_area.py` | Function to compute area of a circle |
| 9 | `09_list_operations.py` | List ops: append, remove, insert, merge, sort, slice |
| 10 | `10_graph_adjacency_list.py` | Graph as adjacency list; print vertices & edges |
| 11 | `11_graph_adjacency_matrix.py` | Graph as adjacency matrix; print vertices & edges |
| 12 | `12_student_report_card.py` | Report card: 2 semesters × 5 subjects (theory + lab), % / SGPA / CGPA |

## How to Run

```bash
cd python_basics

python3 01_variables_datatypes.py
python3 02_calculator.py
python3 03_positive_negative_zero.py
python3 04_largest_of_three.py
python3 05_print_1_to_10.py
python3 06_multiplication_table.py
python3 07_tables_1_to_10.py
python3 08_circle_area.py
python3 09_list_operations.py
python3 10_graph_adjacency_list.py
python3 11_graph_adjacency_matrix.py
python3 12_student_report_card.py
```

For the report card (`12`), choose **option 2** for a quick demo with sample data, or **option 1** for full interactive input.

## Report Card Logic (Program 12)

- Each semester has **5 subjects**.
- Each subject has **Theory** (default /100) + **Lab/Practice** (default /50).
- Subject % = `(theory + lab) / (max_theory + max_lab) × 100`
- Grade points (10-point scale): O=10, A+=9, A=8, B+=7, B=6, C=5, F=0
- **SGPA** = average grade points of 5 subjects in that semester
- **CGPA** = average of SGPA1 and SGPA2
- Overall % = average of both semester percentages
