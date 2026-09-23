"""
Program 12: Student Report Card (2 Semesters, 5 Subjects each)

For each semester:
  - Input 5 subject names
  - For each subject: Theory marks + Lab (practice) marks
  - Compute subject total, percentage, grade points
  - Compute Semester Percentage and SGPA

Finally:
  - CGPA = average of both SGPAs
  - Overall percentage = average of both semester percentages
"""

# Grade point scale based on percentage (common 10-point scale)
GRADE_SCALE = [
    (90, 10, "O"),   # Outstanding
    (80, 9, "A+"),
    (70, 8, "A"),
    (60, 7, "B+"),
    (50, 6, "B"),
    (40, 5, "C"),
    (0, 0, "F"),     # Fail
]


def get_grade_point(percentage):
    """Return (grade_point, letter_grade) for a given percentage."""
    for min_pct, gp, letter in GRADE_SCALE:
        if percentage >= min_pct:
            return gp, letter
    return 0, "F"


def get_float(prompt, min_val=0, max_val=100):
    """Read a float within [min_val, max_val]."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  Invalid number. Try again.")


def get_nonempty(prompt):
    """Read a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  Input cannot be empty. Try again.")


def input_semester(sem_no, max_theory=100, max_lab=50):
    """
    Collect data for one semester.
    Each subject has theory + lab marks.
    Subject max total = max_theory + max_lab (default 150).
    """
    print("\n" + "=" * 55)
    print(f"  SEMESTER {sem_no} — Subject Details")
    print("=" * 55)
    print(f"  (Theory max = {max_theory}, Lab max = {max_lab})")

    subjects = []
    for i in range(1, 6):
        print(f"\n  --- Subject {i} ---")
        name = get_nonempty(f"  Subject {i} name: ")
        theory = get_float(f"  Theory marks (0-{max_theory}): ", 0, max_theory)
        lab = get_float(f"  Lab/Practice marks (0-{max_lab}): ", 0, max_lab)

        total = theory + lab
        max_total = max_theory + max_lab
        percentage = (total / max_total) * 100
        gp, letter = get_grade_point(percentage)

        subjects.append({
            "name": name,
            "theory": theory,
            "lab": lab,
            "total": total,
            "max_total": max_total,
            "percentage": percentage,
            "grade_point": gp,
            "letter": letter,
        })

    return subjects


def compute_semester_result(subjects):
    """Compute semester percentage and SGPA from subject list."""
    total_obtained = sum(s["total"] for s in subjects)
    total_max = sum(s["max_total"] for s in subjects)
    sem_percentage = (total_obtained / total_max) * 100

    # SGPA = average of grade points (equal credit assumption)
    sgpa = sum(s["grade_point"] for s in subjects) / len(subjects)

    return {
        "subjects": subjects,
        "total_obtained": total_obtained,
        "total_max": total_max,
        "percentage": sem_percentage,
        "sgpa": sgpa,
    }


def print_semester_report(sem_no, result):
    """Display a formatted semester report."""
    print("\n" + "-" * 70)
    print(f"  SEMESTER {sem_no} RESULT")
    print("-" * 70)
    print(f"  {'Subject':<18} {'Theory':>8} {'Lab':>8} {'Total':>8} "
          f"{'%':>7} {'GP':>5} {'Grade':>6}")
    print("  " + "-" * 66)

    for s in result["subjects"]:
        print(
            f"  {s['name']:<18} "
            f"{s['theory']:>8.1f} "
            f"{s['lab']:>8.1f} "
            f"{s['total']:>8.1f} "
            f"{s['percentage']:>6.1f}% "
            f"{s['grade_point']:>5} "
            f"{s['letter']:>6}"
        )

    print("  " + "-" * 66)
    print(
        f"  {'SEMESTER TOTAL':<18} "
        f"{'':>8} {'':>8} "
        f"{result['total_obtained']:>8.1f} / {result['total_max']:<.0f}"
    )
    print(f"  Semester Percentage : {result['percentage']:.2f}%")
    print(f"  SGPA                : {result['sgpa']:.2f}")


def print_final_report(student_name, roll, sem1, sem2):
    """Display full report card with CGPA."""
    cgpa = (sem1["sgpa"] + sem2["sgpa"]) / 2
    overall_pct = (sem1["percentage"] + sem2["percentage"]) / 2

    print("\n" + "=" * 70)
    print("                    STUDENT REPORT CARD")
    print("=" * 70)
    print(f"  Student Name : {student_name}")
    print(f"  Roll Number  : {roll}")
    print("=" * 70)

    print_semester_report(1, sem1)
    print_semester_report(2, sem2)

    print("\n" + "=" * 70)
    print("                    OVERALL SUMMARY")
    print("=" * 70)
    print(f"  Semester 1 Percentage : {sem1['percentage']:.2f}%")
    print(f"  Semester 1 SGPA       : {sem1['sgpa']:.2f}")
    print(f"  Semester 2 Percentage : {sem2['percentage']:.2f}%")
    print(f"  Semester 2 SGPA       : {sem2['sgpa']:.2f}")
    print("-" * 70)
    print(f"  Overall Percentage    : {overall_pct:.2f}%")
    print(f"  CGPA (avg of SGPAs)   : {cgpa:.2f}")
    print("=" * 70)

    # Result status
    if cgpa >= 5 and overall_pct >= 40:
        status = "PASS"
    else:
        status = "FAIL / NEEDS IMPROVEMENT"
    print(f"  Final Status          : {status}")
    print("=" * 70)


def run_demo():
    """Run with sample data so the program can be tested without long input."""
    student_name = "Riya Sharma"
    roll = "CS2024-042"

    sem1_subjects = [
        {"name": "Mathematics", "theory": 78, "lab": 40},
        {"name": "Physics", "theory": 72, "lab": 38},
        {"name": "Chemistry", "theory": 65, "lab": 35},
        {"name": "English", "theory": 80, "lab": 42},
        {"name": "Programming", "theory": 88, "lab": 48},
    ]
    sem2_subjects = [
        {"name": "Data Structures", "theory": 82, "lab": 45},
        {"name": "Digital Logic", "theory": 70, "lab": 36},
        {"name": "Discrete Math", "theory": 75, "lab": 40},
        {"name": "Communication", "theory": 68, "lab": 38},
        {"name": "Python Lab", "theory": 90, "lab": 49},
    ]

    def finalize(raw_list):
        subjects = []
        for s in raw_list:
            total = s["theory"] + s["lab"]
            max_total = 150
            pct = (total / max_total) * 100
            gp, letter = get_grade_point(pct)
            subjects.append({
                **s,
                "total": total,
                "max_total": max_total,
                "percentage": pct,
                "grade_point": gp,
                "letter": letter,
            })
        return compute_semester_result(subjects)

    sem1 = finalize(sem1_subjects)
    sem2 = finalize(sem2_subjects)
    print_final_report(student_name, roll, sem1, sem2)


def main():
    print("=" * 55)
    print("  STUDENT REPORT CARD GENERATOR")
    print("  (2 Semesters × 5 Subjects × Theory + Lab)")
    print("=" * 55)

    mode = input(
        "\nEnter mode:\n"
        "  1 - Interactive input (full)\n"
        "  2 - Demo with sample data\n"
        "Choice (1/2): "
    ).strip()

    if mode == "2":
        run_demo()
        return

    # Interactive mode
    student_name = get_nonempty("\nEnter student name: ")
    roll = get_nonempty("Enter roll number: ")

    print("\nMark scheme defaults: Theory out of 100, Lab out of 50.")
    custom = input("Use custom max marks? (y/n): ").strip().lower()
    if custom == "y":
        max_theory = get_float("  Max theory marks: ", 1, 500)
        max_lab = get_float("  Max lab marks: ", 1, 500)
    else:
        max_theory, max_lab = 100, 50

    sem1_subjects = input_semester(1, max_theory, max_lab)
    sem2_subjects = input_semester(2, max_theory, max_lab)

    sem1 = compute_semester_result(sem1_subjects)
    sem2 = compute_semester_result(sem2_subjects)

    print_final_report(student_name, roll, sem1, sem2)


if __name__ == "__main__":
    main()
