def exam_grade(score):
	if score > 95 and score <= 100:
		grade = "Top Score"
	elif score >= 60 and score <= 95:
		grade = "Pass"
	elif score > 100:
		grade = "Score out of range"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(125)) # Should be Score out of range
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail