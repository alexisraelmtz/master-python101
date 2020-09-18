allScores = {
    "Paulina": {"Math": 8.0, "History": 7.8, "Geography": 9.3},
    "Santi": {"Math": 6.5, "History": 7.8, "Geography": 8.1},
    "Shaddai": {"Math": 9.5, "History": 9.8, "Geography": 9.9},
}


def AverageScore(scores, assignment):
    score_sum = 0
    passed_classes = 0
    for _, value in scores.items():
        score_sum += value.get(assignment, 0) * (1 / len(scores))
        if value.get(assignment, 0) >= 5:
            passed_classes += 1
    return [score_sum, passed_classes]


def StudentPlacement(scores):
    survey = ""
    num_passed = 0
    for student, grades in scores.items():
        classResult = []
        for classroom, score in grades.items():
            result = grades.get(classroom)
            classResult.append(result)
            if score >= 5:
                num_passed += 1
            for key, _ in grades.items():
                if len(classResult) == len(grades):
                    survey += f"In {key} they graded: {classResult} and {num_passed} students passed.\n"

    return survey


math_score = AverageScore(allScores, "Math")
print(
    f"Math score off all students averages: {math_score[0]}. And {math_score[1]} students passed the class."
)
classes = StudentPlacement(allScores)
print(classes)
