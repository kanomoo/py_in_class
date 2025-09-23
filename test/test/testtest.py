# # รับคำศัพท์จากผู้ใช้ โดยให้คั่นแต่ละคำด้วยช่องว่าง
# words = input("กรอกคำศัพท์ (คั่นแต่ละคำด้วยช่องว่าง): ")

# print("คำที่ซ้ำกันและจำนวน:")

# checked = ""  # สตริงสำหรับเก็บคำที่ตรวจสอบไปแล้ว

# # วนลูปแต่ละคำในสตริงที่ผู้ใช้กรอก (แยกคำด้วย split)
# for word in words.split():
#     # ถ้าคำนี้ยังไม่ถูกตรวจสอบ (ยังไม่มีใน checked)
#     if word not in checked:
#         # นับจำนวนครั้งที่คำนี้ปรากฏในสตริง
#         count = words.split().count(word)
#         # ถ้าคำนี้มีมากกว่า 1 ครั้ง แสดงผล
#         if count > 1:
#             print(f"{word}: {count} ครั้ง")
#         # เพิ่มคำนี้ลงใน checked เพื่อไม่ให้ตรวจซ้ำ
#         checked += word

# word = input("กรอกคำศัพท์ (คั่นแต่ละคำด้วยช่องว่าง): ")
# for w in word.split():
#     if word.split().count(w) > 1:
#         print(f"{w}: {word.split().count(w)} ครั้ง")


word = input("Enter word: ")
for w in word.split():
    if word.split().count(w) > 1:
        print(f"{w}: {word.split().count(w)}")
        break