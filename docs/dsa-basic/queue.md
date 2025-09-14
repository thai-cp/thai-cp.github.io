---
title: Queue
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่อยู่หน้าสุดออกมา เหมือนกับการต่อคิวเพื่อเข้าร้านอาหาร คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Queue**

## Queue

**Queue** ใน C++ จะถูก include อยู่ใน library `<queue>` ซึ่ง Queue มีการทำงานแบบ "First In First Out" (FIFO) นั่นคือ เราจะนำข้อมูลใหม่มาใส่ตรงท้ายแถว แล้วเวลาจะนำข้อมูลออก จะนำออกมาทางด้านหน้าแถว ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ [Time Complexity](/dsa-basic/complexity) เพียง $O(1)$

## Initialize
ลักษณะ Syntax จะเป็น
```cpp
queue <ชนิดข้อมูล> ชื่อที่ต้องการจะตั้ง;
```
เช่น
```cpp
queue <int> q_int; // จะได้ Queue สำหรับเก็บค่าชนิด Integer (จำนวนเต็ม)
queue <string> q_qring; // จะได้ Queue สำหรับเก็บค่าชนิด qring (สายอักขระ)
```

## Operations
- `push()`: ใช้ในการเพิ่มข้อมูลเข้า queue
    ```cpp title="ตัวอย่างการใช้"
    q_int.push(5);
    ```
- `pop()`: ใช้ในการนำข้อมูลออกจาก queue
    ```cpp title="ตัวอย่างการใช้"
    q_int.pop();
    ```
- `front()`: ใช้ในการเรียกค่าด้านหน้าของ queue
    ```cpp title="ตัวอย่างการใช้"
    int t = q_int.top();
    ```
- `empty()`: ใช้ในการตรวจสอบว่า queue ว่างหรือไม่
    ```cpp title="ตัวอย่างการใช้"
    if (q_int.empty()) {
        cout << "queue is empty";
    }
    else {
        cout << "queue is not empty";
    }
    ```
- `size()`: ใช้ในการเรียกขนาดของ queue ณ ขณะนั้น
    ```cpp title="ตัวอย่างการใช้"
    int sz = q_int.size();
    ```
## โจทย์

!problems [prog-0003, prog-0004, prog-0010, prog-0016, prog-0020, prog-0021, prog-0025, prog-0030, prog-0033, prog-0035, prog-0043]
