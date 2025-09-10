---
title: ฟังก์ชัน
author: Pakin Olanraktham
---

Function (ฟังก์ชัน) คือกลุ่มของคำสั่งที่เรานำมารวมกันไว้ เพื่อให้สามารถเรียกใช้งานซ้ำได้ง่ายขึ้น โดยไม่ต้องเขียนโค้ดซ้ำๆ หลายครั้ง

## โครงสร้างของฟังก์ชัน
```c
return_type function_name(parameter1, parameter2, ...) {
    // คำสั่งต่าง ๆ
    return value; // ส่งค่ากลับ (ถ้ามี)
}
```

1. **return_type** คือ ชนิดข้อมูลที่ฟังก์ชันจะส่งค่ากลับ เช่น `int`, `float`, `char`, `void`
2. **function_name** คือ ชื่อฟังก์ชัน (ตั้งชื่อได้เอง แต่ห้ามซ้ำกับชื่อที่สงวนไว้)
3. **parameter** คือ ตัวแปรที่ส่งเข้ามาให้ฟังก์ชันทำงาน (จะมีหรือไม่มีก็ได้)
4. **return value** คือ ค่าที่ส่งกลับออกไป (ถ้า `void` ไม่ต้อง return)

โดยทั่วไป เราจะเขียนฟังก์ชัน ไว้ข้างนอกและก่อน **main()**

### ตัวอย่าง

```c
#include <stdio.h>

// ไม่มี parameter และไม่มี return
void hello() { 
    printf("Hello!\n"); 
}

// มี parameter แต่ไม่มี return
void printSum(int a, int b) { 
    printf("%d + %d = %d\n", a, b, a+b); 
}

// ไม่มี parameter แต่มี return
int getNum() { 
    return 42; 
}

// มี parameter และมี return
int add(int x, int y) { 
    return x+y; 
}

int main() {
    // เรียกใช้แต่ละฟังก์ชัน
    hello(); // output คือ "Hello!"
    
    printSum(5, 7); // output คือ "5 + 7 = 12"
    
    int num = getNum();
    printf("%d\n", num); // output คือ 42
    
    int result = add(10, 20);
    printf("%d\n", result); // output คือ 30
}
```

!!! note "โจทย์ตัวอย่าง"
    จงเขียนฟังก์ชันเพื่อคำนวณพื้นที่สามเหลี่ยมสูง H ฐานยาว B โดยคืนค่าออกมาเป็นทศนิยม
??? note "เฉลย"
    ```c
    #include <stdio.h>

    float triangle_area(int H, int B) { // ประกาศฟังก์ชัน ชื่อว่า "triangle_area" ซึ่งรับค่าเป็นจำนวนเต็ม 2 ตัว และคืนค่าออกมาเป็นทศนิยม
        return ((float) H) * B / 2; // เปลี่ยน H ให้เป็นทศนิยมก่อน เพื่อที่จะได้คำตอบออกมาเป็นทศนิยม แล้วนำไปเข้าสูตร พื้นที่ = 1/2 * ฐาน * สูง
    }

    int main() {
        printf("%.2f\n", triangle_area(5, 10)); // จะได้ output ออกมาเป็น 25.00
    }
    ```

!!! note "เพิ่มเติม"
    เราสามารถประกาศตัวแปรไว้ข้างนอก `main()` ได้ โดยตัวแปรนี้ ทุกฟังก์ชัน จะสามารถเข้าถึงได้ สามารถเปลี่ยนแปลงค่าได้ เช่น
    ```c
    #include <stdio.h>

    int count = 0;

    void increase_count() {
        count = count + 1; // เพิ่มค่า count ด้วย 1
    }

    int main() {
        increase_count(); // count = 0 + 1 = 1
        increase_count(); // count = 1 + 1 = 2
        increase_count(); // count = 2 + 1 = 3
        printf("%d\n", count); // output จะได้ 3
    }
    ```

## Recursive Function

Recursive Function คือฟังก์ชันที่ เรียกใช้งานตัวเอง ภายในฟังก์ชันเดียวกัน ใช้เมื่อปัญหาสามารถแบ่งออกเป็นปัญหาย่อยๆ ที่มีลักษณะเหมือนกัน

```c
return_type function_name(parameters) {
    if (เงื่อนไขหยุดทำงาน)  // base case
        return ค่าบางอย่าง;
    else
        return function_name(ค่าที่เล็กลง); // recursive case
}
```

1. **Base case** คือ เงื่อนไขหยุด recursion (สำคัญมาก ถ้าไม่มีก็จะวนไม่รู้จบ)
2. **Recursive case** ส่วนที่ฟังก์ชันเรียกตัวเอง

### ตัวอย่าง
ต้องการหาค่า factorial(n) เมื่อ n เป็นจำนวนเต็มที่ไม่ติดลบ

```c
#include <stdio.h>

int factorial(int n) {
    if (n == 0) return 1;        // base case คือ เมื่อ n เป็น 0 ให้คืนค่า 1
    return n * factorial(n - 1); // recursive case คือ เมื่อ n > 0 ให้คืนค่า n * factorial(n-1) [จาก n! = n * (n-1)!]
}

int main() {
    int num = 5;
    printf("%d! = %d\n", num, factorial(num)); // จะได้ output คือ "5! = 120"
    return 0;
}
```

!problems [prog-0019]