# grade planning for semester courses

# def calculate_required_grades(current_gpa: float, target_gpa: float, credits: list[int]) -> list[str]:
#     # 3.2 = (2.8 + 3.6) / 2
#     # k = (2.8 + 3.6) / 2
#     n = (3.2 * 2) - 2.8
#     k = (2.8 + n) / 2
#
#     return k
# current_gpa = 2.8
# target_gpa = 3.2
# credits = [3,4,3,2,3]
# print(calculate_required_grades(current_gpa, target_gpa, credits))












#
# def calculate_required_grades(current_gpa: float, target_gpa: float, credits: list[int]) -> list[str]:
#     # กำหนดเกรดและคะแนน grade points
#     grade_scale = {'A': 4.0,'B+': 3.5,'B': 3.0,'C+': 2.5,'C': 2.0,'D+': 1.5,'D': 1.0,}
#
#     total_credits = sum(credits) #15
#
#     # สมมติ GPA ปัจจุบันครอบคลุมหน่วยกิตเท่ากับ total_credits
#     # (ในกรณีนี้ถ้าต้องการปรับให้สมจริงต้องมีข้อมูลหน่วยกิตสะสมก่อนหน้าแยก)
#
#     # หาผลรวม grade points ที่ต้องได้ทั้งหมด
#     total_grade_points_needed = target_gpa * total_credits #48.0 = 3.2 * 15
#
#     # ผลรวม grade points ที่มีตอนนี้
#     current_total_grade_points = current_gpa * total_credits #42.0 = 2.8 * 15
#
#     # ผลรวม grade points ที่ต้องได้เพิ่มใน 5 วิชาใหม่
#     required_grade_points = total_grade_points_needed - current_total_grade_points # 6 = 48.0 - 42.0
#
#     # ถ้าเกรดเป้าหมายต่ำกว่าหรือเท่ากับปัจจุบัน ให้เกรดต่ำสุด (D)
#     if required_grade_points <= 0: # 6 <= 0 notttt
#         min_grade_point = grade_scale['D']
#     else:
#         # เกรดเฉลี่ยที่ต้องได้ในแต่ละวิชา (สมมติเท่า ๆ กัน)
#         min_grade_point = required_grade_points / total_credits # 0.4 = 6.0 / 15
#
#         # หาคะแนนเกรดที่เท่ากับหรือสูงกว่า min_grade_point ที่ต่ำที่สุด
#         possible_grades = sorted(grade_scale.items(), key=lambda x: x[1]) #เหมือนใช้ . item
#         # [('D', 1.0), ('D+', 1.5), ('C', 2.0), ('C+', 2.5), ('B', 3.0), ('B+', 3.5), ('A', 4.0)]
#         for grade, point in possible_grades:
#             if point >= min_grade_point: # 1 >= 0.4
#                 min_grade_point = point # 1 = 1
#                 break
#         else:
#             # ถ้าไม่เจอเกรดที่สูงกว่า ให้เลือกเกรดสูงสุด (A)
#             min_grade_point = 4.0
#
#     # หาเกรดตัวหนังสือจากคะแนน
#     #dict_items([('A', 4.0), ('B+', 3.5), ('B', 3.0), ('C+', 2.5), ('C', 2.0), ('D+', 1.5), ('D', 1.0)])
#     for grade, point in grade_scale.items():
#         if point == min_grade_point:
#             min_grade = grade
#             break
#
#     # คืนค่าเป็นรายวิชา 5 วิชาเกรดเท่ากัน
#     return [min_grade] * 5
#
#
# # ทดสอบ
# current_gpa = 2.8
# target_gpa = 3.2
# credits = [3, 4, 3, 2, 3]
#
# print(calculate_required_grades(current_gpa, target_gpa, credits))  # ['B+', 'B+', 'B+', 'B+', 'B+']



































# from typing import List
#
#
# def calculate_required_grades(current_gpa: float, target_gpa: float, credits: List[int]) -> List[str]:
#     """
#     Calculate the minimum letter grades required in each course to achieve a target GPA.
#
#     Args:
#         current_gpa: Student's current GPA
#         target_gpa: Target GPA to achieve
#         credits: List of credit hours for each of the 5 courses
#
#     Returns:
#         List of minimum letter grades required for each course
#     """
#     # Grade points mapping
#     grade_points = {
#         'A': 4.0,
#         'B+': 3.5,
#         'B': 3.0,
#         'C+': 2.5,
#         'C': 2.0,
#         'D+': 1.5,
#         'D': 1.0
#     }
#
#     # Convert grade points to ordered list for easier calculation
#     grades = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D']
#     points = [grade_points[grade] for grade in grades]
#
#     # Calculate total credits for the semester
#     total_credits = sum(credits)
#
#     # Calculate total grade points needed for target GPA
#     total_points_needed = target_gpa * total_credits
#
#     # Try all possible combinations of grades starting from the lowest
#     # We'll use a greedy approach: start with the lowest grade and increase as needed
#
#     def try_grade_combination(grade_assignment):
#         """Calculate GPA for a given grade assignment"""
#         total_points = sum(grade_points[grade] * credit for grade, credit in zip(grade_assignment, credits))
#         return total_points / total_credits
#
#     # Start with all D grades and work our way up
#     result_grades = ['D'] * 5
#
#     # Try to find the minimum grades needed
#     for i in range(5):
#         # For each course, find the minimum grade needed
#         for grade in grades:
#             test_grades = result_grades.copy()
#             test_grades[i] = grade
#
#             # Calculate what GPA we'd get with remaining courses at minimum
#             if try_grade_combination(test_grades) >= target_gpa:
#                 # Check if we can achieve target with remaining courses at D
#                 remaining_points_needed = total_points_needed - sum(
#                     grade_points[test_grades[j]] * credits[j] for j in range(i + 1)
#                 )
#                 remaining_credits = sum(credits[i + 1:])
#
#                 if remaining_credits == 0 or remaining_points_needed <= remaining_credits * 1.0:
#                     result_grades[i] = grade
#                     break
#
#     # More systematic approach using dynamic programming-like logic
#     # We need to ensure the combination actually achieves the target
#
#     # Let's use a more direct approach
#     def find_minimum_grades():
#         # Try all possible combinations systematically
#         # Start with all grades as 'D' and increase as needed
#
#         # Calculate minimum total points needed
#         min_points_needed = target_gpa * total_credits
#
#         # Use a greedy approach: distribute grades to minimize overall grades
#         # while meeting the target
#
#         best_grades = ['A'] * 5  # Start with worst case
#
#         # Try different combinations
#         for a_count in range(6):  # 0 to 5 A's
#             for bp_count in range(6 - a_count):  # remaining can be B+ or lower
#                 for b_count in range(6 - a_count - bp_count):
#                     for cp_count in range(6 - a_count - bp_count - b_count):
#                         for c_count in range(6 - a_count - bp_count - b_count - cp_count):
#                             # Remaining are D+ and D
#                             remaining = 5 - a_count - bp_count - b_count - cp_count - c_count
#
#                             # Create grade assignment
#                             grade_list = (['A'] * a_count + ['B+'] * bp_count +
#                                           ['B'] * b_count + ['C+'] * cp_count +
#                                           ['C'] * c_count + ['D+'] * remaining)
#
#                             if len(grade_list) == 5:
#                                 # Calculate GPA for this combination
#                                 total_points = sum(grade_points[grade] * credit
#                                                    for grade, credit in zip(grade_list, credits))
#                                 gpa = total_points / total_credits
#
#                                 if gpa >= target_gpa:
#                                     return grade_list
#
#         # If no combination works, return all A's
#         return ['A'] * 5
#
#     # Simpler and more direct approach
#     def calculate_minimum_grades_direct():
#         # Calculate exactly what we need
#         total_points_needed = target_gpa * total_credits
#
#         # Sort courses by credit hours (descending) to optimize grade distribution
#         course_indices = sorted(range(5), key=lambda i: credits[i], reverse=True)
#
#         result = ['D'] * 5
#         current_points = sum(1.0 * credits[i] for i in range(5))  # All D's initially
#
#         # For each course, determine minimum grade needed
#         for idx in course_indices:
#             for grade in reversed(grades):  # Start from A and work down
#                 # Calculate points if we assign this grade to current course
#                 test_points = current_points - (1.0 * credits[idx]) + (grade_points[grade] * credits[idx])
#
#                 if test_points >= total_points_needed:
#                     result[idx] = grade
#                     current_points = test_points
#                     break
#
#         return result
#
#     return calculate_minimum_grades_direct()
#
#
# # Test the function with the provided example
# def test_grade_calculator():
#     # Test case from the problem
#     current_gpa = 2.8
#     target_gpa = 3.2
#     credits = [3, 4, 3, 2, 3]
#
#     result = calculate_required_grades(current_gpa, target_gpa, credits)
#     print(f"Input: current_gpa={current_gpa}, target_gpa={target_gpa}, credits={credits}")
#     print(f"Output: {result}")
#
#     # Verify the calculation
#     grade_points = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D+': 1.5, 'D': 1.0}
#     total_points = sum(grade_points[grade] * credit for grade, credit in zip(result, credits))
#     actual_gpa = total_points / sum(credits)
#     print(f"Calculated GPA: {actual_gpa:.2f}")
#     print(f"Target achieved: {actual_gpa >= target_gpa}")
#     print()
#
#
# # Run the test
# if __name__ == "__main__":
#     test_grade_calculator()
#
#     # Additional test cases
#     print("Additional test cases:")
#
#     # Test case 2: Lower target
#     result2 = calculate_required_grades(2.0, 2.5, [3, 3, 3, 3, 3])
#     print(f"Test 2 - Target 2.5: {result2}")
#
#     # Test case 3: Higher target
#     result3 = calculate_required_grades(3.0, 3.8, [4, 4, 3, 3, 3])
#     print(f"Test 3 - Target 3.8: {result3}")
#
#     # Test case 4: Different credit distribution
#     result4 = calculate_required_grades(2.5, 3.0, [1, 2, 3, 4, 5])
#     print(f"Test 4 - Varied credits: {result4}")
#
# current_gpa = 2.8
# target_gpa = 3.2
# credits = [3, 4, 3, 2, 3]
#
# print(calculate_required_grades(current_gpa, target_gpa, credits))  # ['B+', 'B+', 'B+', 'B+', 'B+']
