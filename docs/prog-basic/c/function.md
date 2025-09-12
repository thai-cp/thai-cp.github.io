---
title: ฟังก์ชัน
author: Pakin Olanraktham, njoop
level:
---

## ฟังก์ชันคืออะไร

Function (ฟังก์ชัน) คือกลุ่มของคำสั่งที่เรานำมารวมกันไว้ เพื่อให้สามารถเรียกใช้งานได้เมื่อต้องการ

หนึ่งในฟังก์ชันที่เห็นได้บ่อยที่สุด ก็คือ `main()` โดยฟังก์ชันนี้จะเป็นจุดเริ่มต้นของโปรแกรม

ประโยชน์หลักๆ ในการเขียนฟังก์ชัน คือเราไม่จำเป็นต้องเขียนโค้ดซ้ำๆ หลายครั้ง สามารถเขียนครั้งเดียวแล้วเรียกใช้กี่ครั้งก็ได้ ตามที่ต้องการ

ฟังก์ชัน สามารถประกาศได้ ดังนี้

```c
#include <stdio.h>

void hello() { 
    printf("Hello!\n"); 
}

int main() {
    hello(); // เรียกใช้ฟังก์ชัน
}
// output คือ Hello!
```

โดยในตัวอย่างได้ทำการประกาศฟังก์ชันชื่อ `hello` เมื่อทำการเรียกใช้ `hello()` จะรันคำสั่งภายใน นั่นก็คือ `printf("Hello!\n")` นั่นเอง

สามารถเรียกใช้ฟังก์ชันหลายๆ ครั้งได้ เช่น

```c
#include <stdio.h>

void hello() { 
    printf("Hello!\n"); 
}

int main() {
    hello();
    hello();
    hello();
}
/*
output คือ
Hello!
Hello!
Hello!
*/
```

## โครงสร้างของฟังก์ชัน

แน่นอนว่า ฟังก์ชันสามารถรับค่าเข้าไปประมวลผล และคืนค่าออกมาได้ ลองดูโครงสร้างฟังก์ชันดังต่อไปนี้

```c
return_type function_name(parameter1, parameter2, ...) {
    // คำสั่งต่าง ๆ
    return value; // ส่งค่ากลับ (ถ้ามี)
}
```

1. **return_type** คือ ชนิดข้อมูลที่ฟังก์ชันจะส่งค่ากลับ เช่น `int`, `float`, `char`, `void`
2. **function_name** คือ ชื่อฟังก์ชัน (ตั้งชื่อได้เอง แต่ห้ามซ้ำกับชื่อที่สงวนไว้ เช่น `main`)
3. **parameter** คือ ตัวแปรที่ส่งเข้ามาให้ฟังก์ชันทำงาน (จะไม่มีหรือมีกี่ค่าก็ได้)
4. **value** คือ ค่าที่ส่งกลับออกไป (ถ้า `void` ไม่จำเป็นต้องใช้ `return`)

นี่เป็นฟังก์ชันตัวอย่าง หากต้องการแสดงผลรวมของเลข 2 เลขที่ใส่เข้าไป เราไม่จำเป็นต้องมีค่าส่งกลับ (return) จึงประกาศเป็นชนิด `void` แต่ต้องมี parameter นั่นก็คือเลขที่ต้องการใส่เข้าไป

```c
#include <stdio.h>

// มี parameter แต่ไม่มี return
void printSum(int a, int b) { 
    printf("%d + %d = %d\n", a, b, a+b); 
}

int main() {
    printSum(5, 7); // output คือ "5 + 7 = 12"
}
```

**หมายเหตุ:** ค่าที่เราใส่ไปในฟังก์ชัน เช่น `5, 7` ใน `printSum(5, 7)` จะเรียกว่า อาร์กิวเมนต์ (argument)

แต่ถ้าเกิดต้องการนำค่าผลรวมไปใช้ด้วย จำเป็นต้องมีทั้ง return และ parameter เช่น

```c
#include <stdio.h>

// มี parameter และมี return
int add(int x, int y) { 
    return x+y; 
}

int main() {
    int result = add(10, 20); // สามารถนำค่านี้ไปใช้ต่อได้
    printf("%d\n", result); // output คือ 30
}
```

### ตัวอย่าง

โค้ดด้านล่าง จะเป็นสรุปวิธีการเขียนของฟังก์ชันแต่ละชนิด

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

!!! info "การใช้ `return` เพื่อหยุดการทำงานของฟังก์ชัน"
    คำสั่ง `return` เป็นคำสั่งที่ใช้ในการคืนค่าในฟังก์ชัน (ถ้ามี) แต่หลังจากนั้นจะหยุดการทำงานของฟังก์ชันไปเลย ดังนั้น เราสามารถใช้ `return` เป็นการหยุดฟังก์ชันไปในตัวได้

    พิจารณาโค้ดตัวอย่างต่อไปนี้

    ```c
    void checkAge(int age) {
        if(age < 18) {
            printf("Not allowed\n");
        } else {
            printf("Allowed\n");
        }
    }
    ```

    ```c
    void checkAge(int age) {
        if(age < 18) {
            printf("Not allowed\n");
            return; // หยุดการทำงานของฟังก์ชันไปในตัว
        }
        printf("Allowed\n");
    }
    ```

    ฟังก์ชัน 2 ฟังก์ชันนี้จะแสดงผลลัพธ์เหมือนกัน

!!! note "โจทย์ตัวอย่าง"
    จงเขียนฟังก์ชันเพื่อคำนวณพื้นที่สามเหลี่ยมสูง H ฐานยาว B (H และ B เป็นจำนวนเต็ม) โดยคืนค่าออกมาเป็นทศนิยม 2 ตำแหน่ง
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

## ขอบเขตของตัวแปร

ตัวแปรในภาษา C/C++ จะมีขอบเขตที่สามารถใช้งานได้ (เรียกว่า scope)

เช่น ตัวแปรที่ถูกประกาศใช้ใน `if` จะสามารถใช้ได้แค่ใน `if` เท่านั้น ไม่สามารถใช้นอก `if` ได้

```c
#include <stdio.h>

int main() {
    int x = 5;
    if(x == 5) {
        int y = 2;
    }
    printf("%d", y) // compile error
}
```

สังเกตว่า `printf` จะไม่สามารถคอมไพล์ได้ เพราะตัวแปร y ไม่สามารถใช้นอก `if` ได้

สามารถเขียนโค้ดข้างบนให้คอมไฟล์ผ่านได้ดังนี้

```c
#include <stdio.h>

int main() {
    int x = 5, y;
    if(x == 5) {
        y = 2;
    }
    printf("%d", y); // output คือ 2
}
```

ในทำนองเดียวกัน ตัวแปรที่ถูกประกาศภายในฟังก์ชัน จะใช้งานได้แค่ในฟังก์ชันที่ตัวแปรถูกประกาศเท่านั้น

### ตัวแปรประเภท global

เราสามารถประกาศตัวแปรไว้ข้างนอกฟังก์ชันใดๆ ได้ โดยตัวแปรนี้ (เรียกว่า ตัวแปรประเภท global) ทุกฟังก์ชัน จะสามารถเข้าถึงได้ สามารถเปลี่ยนแปลงค่าได้ เช่น

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

## การประกาศฟังก์ชัน

การประกาศฟังก์ชัน สามารถแบ่งได้เป็น 2 วิธี คือ

1. ประกาศก่อนใช้งาน
2. ประกาศหลังใช้งาน

ในตัวอย่างด้านบน ได้ทำการประกาศฟังก์ชันไว้ก่อนฟังก์ชัน `main()` ซึ่งถือเป็นการประกาศก่อนใช้งาน

ถ้าเกิดต้องการประกาศหลัง `main()` จำเป็นต้องประกาศ prototype ไว้ก่อน แล้วค่อยเขียนฟังก์ชันทีหลัง เช่น

```c
#include <stdio.h>

int add(int, int);

int main() {
    printf("%d", add(1, 2)); // output คือ 3
}

int add(int x, int y) {
    return x+y;
}
```

prototype เป็นเหมือนประโยคที่บอกข้อมูลต่างๆ เกี่ยวกับฟังก์ชัน เช่น ชื่อ พารามีเตอร์ โดยไม่จำเป็นต้องบอกทั้งฟังก์ชัน แต่เป็นข้อมูลคร่าวๆ ให้โปรแกรมรู้ว่ามีฟังก์ชันนี้อยู่ โดยในโค้ดด้านบน `int add(int, int);` เป็น prototype แบบหนึ่ง

ถ้าเกิดประกาศฟังก์ชันหลัง `main()` และไม่ประกาศ prototype โปรแกรมจะ compile error

## Recursive Function

Recursive Function คือฟังก์ชันที่ เรียกใช้งานตัวเอง ภายในฟังก์ชันเดียวกัน ใช้เมื่อปัญหาสามารถแบ่งออกเป็นปัญหาย่อยๆ ที่มีลักษณะเหมือนกัน

```c
return_type function_name(parameters) {
    if (เงื่อนไขหยุดทำงาน)  // base case หรือกรณีฐาน
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

ในโค้ดด้านบน สมมติว่าเราเรียกใช้ `factorial(5)` สามารถมองเป็นแผนภาพได้ดังนี้

```c
factorial(5)
= 5 * factorial(4)
= 5 * 4 * factorial(3)
= 5 * 4 * 3 * factorial(2)
= 5 * 4 * 3 * 2 * factorial(1)
= 5 * 4 * 3 * 2 * 1 * factorial(0) // ไม่เรียกฟังก์ชันต่อ เพราะคำสั่ง if (n == 0) return 1;
= 5 * 4 * 3 * 2 * 1 * 1
= 120
```

!!! warning "ข้อควรระวัง"
    ข้อผิดพลาดที่พบเห็นได้บ่อย เวลาเขียน recursive นั่นก็คือ ลืมใส่กรณีฐาน หรือ base case ซึ่งอาจทำให้โปรแกรมรันไปเรื่อยๆ โดยไม่รู้จบ เช่นโค้ดดังนี้

    ```c
    #include <stdio.h>

    int factorial(int n) {
        return n * factorial(n - 1);
    }

    int main() {
        int num = 5;
        printf("%d! = %d\n", num, factorial(num));
        return 0;
    }
    ```

    หากลองรัน จะพบว่า โค้ดนี้จะไม่แสดงผลใดๆ และเกิดข้อผิดพลาดระหว่างการทำงาน

!problems [prog-0019]

## Built-in Fucntion

!resources [(อ่านฟังก์ชันต่างๆ ได้เพิ่มที่นี่, https://en.cppreference.com/w/c.html, CPP Reference)]

ในภาษา C เรามีฟังก์ชันสำเร็จรูป ที่สามารถนำมาใช้ได้ โดยที่เราไม่ต้องเขียนฟังก์ชันเอง ซึ่งก่อนจะใช้ เราต้อง import Library นั้นๆ มาก่อน โดย Library ที่ใช้หลักๆ ได้แก่

### `stdio.h` (Input/Output)

ซึ่งก็คือ Library ซึ่งมีฟังก์ชันสำหรับการนำเข้า ส่งออก ข้อมูลต่างๆ ที่เราเคยใช้กันอยู่แล้ว เช่น

* `scanf("%d", &x);`
* `printf("%d\n", x);`

### `math.h` (Math Functions)

!resources [(อ่านเพิ่มเติม, https://en.cppreference.com/w/c/header/math.html, CPP Reference)]

เป็น Library ที่มีฟังก์ชันทางคณิตศาสตร์อยู่ เช่น

* `sqrt(x)` หารากที่สอง
* `pow(x, y)` คำนวณเลขยกกำลัง $x^y$
* `fabs(x)` หาค่าสัมบูรณ์ $|x|$
* `fmin(x, y)`, `fmax(x, y)` หาค่าน้อยสุด/มากสุด ตามลำดับ

โดยที่ฟังก์ชันข้างต้นทั้งหมด จะคืนค่าออกมาเป็น float และ parameter ของฟังก์ชัน สามารถใส่ได้ทั้ง int และ float (x, y อาจเป็น int หรือ float ก็ได้)

```cpp
#include <stdio.h>
#include <math.h>

int main() {
    printf("%.2f\n", fmin(5, 108)); // 5.00
    printf("%.2f\n", pow(2, 10)); // 1024.00
    printf("%.2f\n", sqrt(2)); // 1.41
    printf("%.2f\n", fabs(-728)); // 728.00
}
```
### `string.h` (String Functions)

เป็น Library ซึ่งมีฟังก์ชันสำหรับการทำงานเกี่ยวกับ string

* `strlen(s)` หาความยาว string (จะนับจากตัวแรกจนถึง '\0' ไม่ได้นับความยาวของ Array เช่น `char str[5] = "IJK";` จะคืนค่า 3)
* `strcmp(a, b)` เป็นการเทียบสตริง
    * หาก a มาก่อน b ตามลำดับพจนานุกรม จะคืนค่าที่น้อยกว่า 0
    * หาก a เหมือนกับ b (เป็น string เดียวกัน) จะคืนค่า 0
    * หาก a มาหลัง b ตามลำดับพจนานุกรม จะคืนค่าที่มากกว่า 0
* `strcpy(dest, src)` คือการ copy string ของ src ไปใส่ dest เช่น 
```c
char dest[5] = "abcd", src[5] = "mno";
strcpy(dest, src);
printf("%s\n", dest); // จะได้ "mno"
```
* `strcat(dest, src)` คือการนำ string ของ src ไปต่อกับ dest เช่น
```c
char dest[10] = "abcd", src[3] = "efg";
strcat(dest, src);
printf("%s\n", dest); // จะได้ "abcdefg"
```