def process_scores(students):
    averages = {}
    
    for name, scores in students.items():
        if len(scores) > 0:
            avg = round(sum(scores) / len(scores), 2)
        else:
            avg = 0.0
        averages[name] = avg
    
    return averages

def classify_grades(averages):
    
    # Grading thresholds (defined locally)
    A_threshold = 90
    B_threshold = 75
    C_threshold = 60
    
    classified = {}
    
    for name, avg in averages.items():
        if avg >= A_threshold:
            grade = "A"
        elif avg >= B_threshold:
            grade = "B"
        elif avg >= C_threshold:
            grade = "C"
        else:
            grade = "F"
        
        classified[name] = (avg, grade)
    
    return classified

def generate_report(classified, passing_avg=70):
    
    print("===== Student Grade Report =====")
    
    total_students = len(classified)
    passed = 0
    
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        
        if status == "PASS":
            passed += 1
        
        print(f"{name:<10} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    
    failed = total_students - passed
    
    print("================================")
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    
    return passed

if __name__ == "__main__":
    
    students = {
        "Alice": [85, 90, 84],
        "Bob": [60, 65, 62.5],
        "Clara": [95, 97, 96]
    }
    
    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
