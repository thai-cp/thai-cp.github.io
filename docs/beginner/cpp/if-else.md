---
title: คำสั่ง if - else
author: Pakin Olanraktham & Pasit Sangprachathanarak
level:
---

คำสั่ง `if - else` ใช้สำหรับการกำหนดเงื่อนไขต่างๆ ในโปรแกรม เพื่อให้โปรแกรมเลือกทำงานอย่างใดอย่างหนึ่ง ขึ้นอยู่กับเงื่อนไขที่กำหนด เช่น คุณต้องการตรวจสอบว่านาย ก. มีอายุมากกว่า 18 ปีหรือไม่, ต้องการตรวจสอบว่าจำนวนเต็มนี้ หารด้วยสองลงตัวหรือไม่

## โครงสร้างของคำสั่ง `if - else`

```cpp
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

```cpp
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

!!! note "โจทย์ตัวอย่าง"
    จงรับเลข 1–7 แล้วพิมพ์ชื่อของวันนั้นๆ (จันทร์–อาทิตย์)
??? note "เฉลย `if - else`"
    ```cpp
    #include <iostream>

    using namespace std;

    int main() {
        int d;
        cin >> d;
        if(d == 1) cout << "Monday";
        else if(d == 2) cout << "Tuesday";
        else if(d == 3) cout << "Wednesday";
        else if(d == 4) cout << "Thursday";
        else if(d == 5) cout << "Friday";
        else if(d == 6) cout << "Saturday";
        else if(d == 7) cout << "Sunday";
        else cout << "Invalid";
    }
    ```

??? note "เฉลย `switch`"
    ```cpp
    #include <iostream>

    using namespace std;

    int main() {
        int d;
        cin >> d;
        switch (d) {
            case 1: cout << "Monday"; break;
            case 2: cout << "Tuesday"; break;
            case 3: cout << "Wednesday"; break;
            case 4: cout << "Thursday"; break;
            case 5: cout << "Friday"; break;
            case 6: cout << "Saturday"; break;
            case 7: cout << "Sunday"; break;
            default: cout << "Invalid";
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
