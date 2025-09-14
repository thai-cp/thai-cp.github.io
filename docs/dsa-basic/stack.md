---
title: Stack 
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่เก็บล่าสุดออกมา เหมือนกับการวางจานซ้อนทับกันกองหนึ่ง คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Stack**

## Stack

**Stack** ใน C++ จะถูก include อยู่ใน library `<stack>` ซึ่ง Stack มีการทำงานแบบ "Last In First Out" (LIFO) นั่นคือ ช่องที่เรานำข้อมูลมาใส่ จะเป็นช่องเดียวกันกับทางที่เราดึงข้อมูลออกมา ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ [Time Complexity](/dsa-basic/complexity) เพียง $O(1)$

## Initialize
ลักษณะ Syntax จะเป็น
```cpp
stack <ชนิดข้อมูล> ชื่อที่ต้องการจะตั้ง;
```
เช่น
```cpp
stack <int> st_int; // จะได้ Stack สำหรับเก็บค่าชนิด Integer (จำนวนเต็ม)
stack <string> st_string; // จะได้ Stack สำหรับเก็บค่าชนิด String (สายอักขระ)
```

## Operations
- `push()`: ใช้ในการเพิ่มข้อมูลเข้า Stack
    ```cpp title="ตัวอย่างการใช้"
    st_int.push(5);
    ```
- `pop()`: ใช้ในการนำข้อมูลออกจาก Stack
    ```cpp title="ตัวอย่างการใช้"
    st_int.pop();
    ```
- `top()`: ใช้ในการเรียกค่าตัวบนของ Stack
    ```cpp title="ตัวอย่างการใช้"
    int t = st_int.top();
    ```
- `empty()`: ใช้ในการตรวจสอบว่า Stack ว่างหรือไม่
    ```cpp title="ตัวอย่างการใช้"
    if (st_int.empty()) {
        cout << "Stack is empty";
    }
    else {
        cout << "Stack is not empty";
    }
    ```
- `size()`: ใช้ในการเรียกขนาดของ Stack ณ ขณะนั้น
    ```cpp title="ตัวอย่างการใช้"
    int sz = st_int.size();
    ```
## โจทย์

!problems [prog-0003, prog-0004, prog-0010, prog-0016, prog-0020, prog-0021, prog-0025, prog-0030, prog-0033, prog-0035, prog-0043]
