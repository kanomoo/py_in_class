import os
from random import randint

def InputNumber_ppl():
    num = int(input("Input Number of vote (1000 - 5000) : "))
    if num <= 1000:
        num = 1000
    else:
        num = 5000
    return num

def Random_Vote(num):
    print("Start Random . . .")
    datas = []
    for i in range(7):
        data = []
        for n in range(num):
            vote = randint(0,3)
            data.append(vote)
        datas.append(data)
    input("Press any key to continue . . .")
    return datas

def Display(datas):
    t_nv,tv1,tv2,tv3 = 0,0,0,0
    mess = ""
    n = 0
    for i in datas:
        n += 1
        n_v,v1,v2,v3 = i.count(0), i.count(1),i.count(2),i.count(3)
        t_nv += n_v
        tv1 += v1
        tv2 += v2
        tv3 += v3
        total = n_v + v1 + v2 + v3
        mess += (f"   {n:<6}|{n_v:^10}|  {n_v / total * 100:.2f} % |{v1:^10}|  {v1/ total * 100:.2f} % |"
                 f"{v2:^10}|  {v2 / total * 100:.2f} % |{v3:^10}|  {v3 / total * 100:.2f} % |\n")
    total = t_nv + tv1 + tv2 + tv3
    t_nv,tv1,tv2,tv3 = t_nv / total * 100, tv1 / total * 100, tv2 / total * 100, tv3 / total * 100
    head = f"District |  no Vote | ({t_nv:.2f}%) |  Vote 1  | ({tv1:.2f}%) |  Vote 2  | ({tv2:.2f}%) |  Vote 3  | ({tv3:.2f}%) |"
    print()
    print("=" * 39,"Summation of Vote","=" * 40)
    print(head)
    print("-" * len(head))
    print(mess,end="")
    print("=" * len(head))
    input("Press any key to continue . . .")
def main():
    while True:
        os.system("cls")
        print("=================================")
        print(f"{"Main Program":^33}")
        print("=================================")
        print(" 1. Input Number Vote ( 1000 - 5000 )\n 2. Start Random . . .\n 3. Display\n 4. Exit Program")
        print("=================================")
        choice = input("Select your choice : ( 1 - 4 ) : ")
        match choice:
            case "1":
                num = InputNumber_ppl()
            case "2":
                try:
                    datas = Random_Vote(num)
                except UnboundLocalError:
                    input("Please Input Number Vote . . .")
            case "3":
                try:
                    Display(datas)
                except UnboundLocalError:
                    input("Please Start Random . . .")
            case "4":
                print("Exit Program") 
                exit()
            case _:
                input("Please select your choice . . .")
        print()
if __name__ == "__main__":
    main()





# import random
#
# # ฟังก์ชันรับจำนวนผู้ลงคะแนน
# def InputNumber_ppl():
#     try:
#         num = int(input("กรุณาใส่จำนวนผู้มีสิทธิ์ลงคะแนน (1000 - 5000): "))
#         if num < 1000:
#             print("จำนวนผู้มีสิทธิ์น้อยเกินไป กำหนดเป็น 1000 คน")
#             return 1000
#         elif num > 5000:
#             print("จำนวนผู้มีสิทธิ์มากเกินไป กำหนดเป็น 5000 คน")
#             return 5000
#         else:
#             return num
#     except ValueError:
#         print("กรุณาใส่ตัวเลขเท่านั้น")
#         return 1000
#
# # ฟังก์ชันสุ่มโหวตให้ทั้ง 7 เขต
# def Random_Vote(num_voters):
#     votes_by_zone = []
#     for zone in range(7):
#         zone_votes = [random.randint(0, 3) for _ in range(num_voters)]
#         votes_by_zone.append(zone_votes)
#     print("** สุ่มคะแนนเสียงเรียบร้อยแล้ว **")
#     return votes_by_zone
#
# # ฟังก์ชันแสดงผลคะแนน
# def Display(votes_by_zone):
#     if not votes_by_zone:
#         print("** ยังไม่ได้สุ่มโหวต กรุณาทำการสุ่มก่อน **")
#         return
#
#     print("\nผลการลงคะแนนในแต่ละเขต:")
#     print("=" * 70)
#     print("{:<10} {:>10} {:>10} {:>10} {:>10}".format(
#         "เขต", "ไม่โหวต", "ผู้สมัคร 1", "ผู้สมัคร 2", "ผู้สมัคร 3"))
#     print("=" * 70)
#
#     for idx, zone_votes in enumerate(votes_by_zone, 1):
#         total = len(zone_votes)
#         no_vote = zone_votes.count(0)
#         vote1 = zone_votes.count(1)
#         vote2 = zone_votes.count(2)
#         vote3 = zone_votes.count(3)
#
#         print("เขต {:<5} {:>6} ({:>5.1f}%) {:>6} ({:>5.1f}%) {:>6} ({:>5.1f}%) {:>6} ({:>5.1f}%)".format(
#             idx,
#             no_vote, (no_vote / total) * 100,
#             vote1, (vote1 / total) * 100,
#             vote2, (vote2 / total) * 100,
#             vote3, (vote3 / total) * 100
#         ))
#     print("=" * 70)
#
# # ฟังก์ชันหลักของโปรแกรม
# def main():
#     votes_by_zone = []
#     num_voters = 0
#
#     while True:
#         print("\n===== เมนูเลือกตั้งจำลอง =====")
#         print("1. Input Number of Votes")
#         print("2. Random Vote")
#         print("3. Display Results")
#         print("4. Exit Program")
#
#         choice = input("เลือกเมนู (1-4): ")
#
#         if choice == "1":
#             num_voters = InputNumber_ppl()
#         elif choice == "2":
#             if num_voters == 0:
#                 print("** กรุณาใส่จำนวนผู้ลงคะแนนก่อน **")
#             else:
#                 votes_by_zone = Random_Vote(num_voters)
#         elif choice == "3":
#             Display(votes_by_zone)
#         elif choice == "4":
#             print("ออกจากโปรแกรม...")
#             break
#         else:
#             print("กรุณาเลือกเมนู 1-4 เท่านั้น")
#
# # เรียกใช้โปรแกรมหลัก
# if __name__ == "__main__":
#     main()
