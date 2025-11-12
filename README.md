# py_in_class
โปรเจคชุดนี้เป็นโค้ด Python สำหรับงานในชั้นเรียน — รวมสคริปต์ตัวอย่าง การประมวลผลข้อมูล และชุดทดสอบที่ช่วยให้เรียนรู้และพัฒนาได้อย่างเป็นระบบ

## คุณสมบัติหลัก
- ตัวอย่างสคริปต์เพื่อสาธิตแนวคิด/อัลกอริทึม
- โครงงานที่แยกเป็นโมดูลเพื่อความอ่านง่ายและทดสอบได้
- ชุดทดสอบพื้นฐาน (pytest/unittest) เพื่อยืนยันพฤติกรรมหลัก

## ข้อกำหนดล่วงหน้า
- Python 3.8+
- แนะนำใช้ virtual environment
- ไฟล์ dependencies: requirements.txt (ถ้ามี)

## ติดตั้ง
1. โคลนรีโปหรือคัดลอกโฟลเดอร์โปรเจค
   git clone https://github.com/kanomoo/py_in_class.git
2. สร้างและเปิดใช้งาน virtual environment (แนะนำ)
   - Windows:
     python -m venv .venv
     .venv\Scripts\activate
   - macOS/Linux:
     python -m venv .venv
     source .venv/bin/activate

## ใช้งาน (ตัวอย่าง)
- รันสคริปต์หลัก (ปรับชื่อไฟล์ตามโปรเจค)
  python main.py
- รันโมดูลเฉพาะ
  python -m src.module_name arg1 arg2

## ทดสอบ
- ติดตั้ง pytest (ถ้ายังไม่มี)
  pip install pytest
- รันเทสต์
  pytest
