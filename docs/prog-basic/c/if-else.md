---
title: คำสั่ง if - else
author: Pakin Olanraktham & Pasit Sangprachathanarak
level:
---

คำสั่ง `if - else` ใช้สำหรับการกำหนดเงื่อนไขต่างๆ ในโปรแกรม เพื่อให้โปรแกรมเลือกทำงานอย่างใดอย่างหนึ่ง ขึ้นอยู่กับเงื่อนไขที่กำหนด เช่น คุณต้องการตรวจสอบว่านาย ก. มีอายุมากกว่า 18 ปีหรือไม่, ต้องการตรวจสอบว่าจำนวนเต็มนี้ หารด้วยสองลงตัวหรือไม่

## โครงสร้างของคำสั่ง `if - else`

```c
if (เงื่อนไข 1) {
    // คำสั่งที่จะทำเมื่อเงื่อนไขเป็นจริง
} else if (เงื่อนไข 2) {
    // คำสั่งที่จะทำเมื่อเงื่อนไขเป็นจริง หากเงื่อนไขก่อนหน้านี้ทั้งหมดเป็นเท็จ
} else {
    // คำสั่งที่จะทำเมื่อเงื่อนไขก่อนหน้านี้ทั้งหมดเป็นเท็จ
}
```

!!! note "คำแนะนำ"
    - สามารถมี `else if` ได้หลายตัว
    - ไม่จำเป็นต้องมี `else if` หรือ `else`
    - ถ้าค่าในเงื่อนไขเท่ากับ 1 หมายถึงเป็นเงื่อนไขเป็นจริง และ 0 หมายถึงเงื่อนไขเป็นเท็จ

คำสั่ง `switch` ใช้สำหรับเลือกทำงานหลายกรณี จากค่าเดียวที่เราต้องการตรวจสอบ โดยจะเทียบค่ากับรายการ `case` ต่างๆ ตามลำดับ ถ้าตรงก็จะเริ่มทำคำสั่งตั้งแต่จุดนั้นไปจนกว่าจะเจอ `break` (หรือจบ `switch`) หากไม่ตรงกับทุก `case` และมี `default` ก็จะทำในส่วนนั้นแทน

## โครงสร้างของคำสั่ง `switch`

```c
switch (expression) {
    case ค่าที่1:
        // คำสั่งเมื่อ expression มีค่าเท่ากับ ค่าที่1
        break; // ออกจาก switch
    case ค่าที่2:
        // คำสั่งเมื่อ expression มีค่าเท่ากับ ค่าที่2
        break;
    /* ... */
    default:
        // คำสั่งเมื่อไม่ตรงกับทุก case ข้างบน (ไม่จำเป็นต้องมี)
}
```

!!! note "สำคัญ"
    - `expression` ต้องเป็นชนิด *integer type* (เช่น `int`, `char`);
    **ใช้กับชนิดทศนิยม (`float`, `double`) ไม่ได้**
    - ค่าหลัง `case` ต้องเป็นค่าคงที่ เช่น `1`, `'A'`, `10+2` แต่ **ห้ามเป็นตัวแปรที่เปลี่ยนค่าได้**
    - ไม่สามารถมี `case` ซ้ำกันได้
    - `default` จะอยู่ตำแหน่งไหนก็ได้ (นิยมไว้ท้ายสุด) และมีได้แค่หนึ่งอัน

### ตัวอย่าง `if - else`

รับเลข 1–7 แล้วพิมพ์ชื่อย่อของวัน (จันทร์–อาทิตย์)

```c
#include <stdio.h>

int main() {
    int d;
    scanf("%d", &d);
    if(d == 1) printf("Monday");
    else if(d == 2) printf("Tuesday");
    else if(d == 3) printf("Wednesday");
    else if(d == 4) printf("Thursday");
    else if(d == 5) printf("Friday");
    else if(d == 6) printf("Saturday");
    else if(d == 7) printf("Sunday");
    else printf("Invalid");
}
```

### ตัวอย่าง `switch`

รับเลข 1–7 แล้วพิมพ์ชื่อย่อของวัน (จันทร์–อาทิตย์)

```c
#include <stdio.h>

int main() {
    int d;
    scanf("%d", &d);
    switch (d) {
        case 1: printf("Monday"); break;
        case 2: printf("Tuesday"); break;
        case 3: printf("Wednesday"); break;
        case 4: printf("Thursday"); break;
        case 5: printf("Friday"); break;
        case 6: printf("Saturday"); break;
        case 7: printf("Sunday"); break;
        default: printf("Invalid");
    }
}
```

!!! warning "ข้อผิดพลาดที่พบบ่อย"
    - ลืม `break;` โดยไม่ได้ตั้งใจ ทำให้ทำงานหลาย `case` ต่อเนื่อง
    - ใช้กับชนิดที่ไม่รองรับ เช่น `double`
    - ใส่ค่าซ้ำในหลาย `case`

โดยทั่วไป `switch` จะอ่านง่ายขึ้นเมื่อมีหลายกรณีตรวจค่าเท่ากับ (เช่น เมนู 1–9) และลดความซ้ำซ้อนของ `else if` ยาวๆ

## โจทย์

!problems [prog-0001, TU1-problem-if-else-1, TU1-problem-if-else-2]
