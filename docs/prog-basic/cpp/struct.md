---
title: ตัวแปรโครงสร้าง (Struct)
author: Lufychop & Pakin Olanraktham
---

Struct คล้ายกับตัวแปรประเภทหนึ่ง ซึ่งมีไว้สำหรับการมัดข้อมูลหลายตัวเข้าด้วยกัน เพื่อความสะดวกในการเก็บข้อมูล เช่น ข้อมูลนักเรียน ซึ่งประกอบไปด้วย ชื่อ เลขประจำตัว อายุ เป็นต้น

การประกาศ Struct มีโครงสร้างดังนี้

```cpp
struct name {
    type_1 name_1;
    type_2 name_2;
    type_3 name_3;
    .
    .
};
```

โดยที่ `name` คือชื่อของ Struct ที่ต้องการจะสร้าง ซึ่งภายใน Struct จะมีการประกาศตัวแปรต่างๆ ตามที่ต้องการ

เช่น การประกาศ Struct เพื่อเก็บข้อมูลนักเรียน

```cpp
struct student {
    string name;
    int id;
    int age;
}; // อย่าลืม semicolon
```

ต่อมา ถ้าหากเราต้องการจะประกาศตัวแปรประเภท struct ที่เราสร้างไว้ มีวิธีการดังนี้

```cpp
struct_name variable_name = {var_1_value, var_2_value, ...};
// เช่น
student A = {"Penguin", 1234, 2000};
```

แต่หากเรายังไม่รู้ค่าที่แน่นอนของ Struct เราไม่จำเป็นต้องมี `= {var_1_value, var_2_value, ...}` ก็ได้

แล้วถ้าเราอยาก Access แต่ละค่าล่ะ เราสามารถทำได้โดยการ `variable_name.var_i` เช่น

```cpp
cout << A.name << ' ' << A.id << ' ' << A.age << '\n'; // จะส่งออก Penguin 1234 2000
```

