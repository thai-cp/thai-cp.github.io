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

```cpp
#include <iostream>

using namespace std;

void hello() { 
    cout << "Hello!\n";
}

int main() {
    hello(); // เรียกใช้ฟังก์ชัน
}
// output คือ Hello!
```

โดยในตัวอย่างได้ทำการประกาศฟังก์ชันชื่อ `hello` เมื่อทำการเรียกใช้ `hello()` จะรันคำสั่งภายใน นั่นก็คือ `cout << "Hello!\n";` นั่นเอง

สามารถเรียกใช้ฟังก์ชันหลายๆ ครั้งได้ เช่น

```cpp
#include <iostream>

using namespace std;

void hello() { 
    cout << "Hello!\n";
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

```cpp
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

```cpp
#include <iostream>

using namespace std;

// มี parameter แต่ไม่มี return
void printSum(int a, int b) { 
    cout << a << " + " << b << " = " << a+b << '\n';
}

int main() {
    printSum(5, 7); // output คือ "5 + 7 = 12"
}
```

**หมายเหตุ:** ค่าที่เราใส่ไปในฟังก์ชัน เช่น `5, 7` ใน `printSum(5, 7)` จะเรียกว่า อาร์กิวเมนต์ (argument)

แต่ถ้าเกิดต้องการนำค่าผลรวมไปใช้ด้วย จำเป็นต้องมีทั้ง return และ parameter เช่น

```cpp
#include <iostream>

using namespace std;

// มี parameter และมี return
int add(int x, int y) { 
    return x+y; 
}

int main() {
    int result = add(10, 20); // สามารถนำค่านี้ไปใช้ต่อได้
    cout << result << '\n'; // output คือ 30
}
```

### ตัวอย่าง

โค้ดด้านล่าง จะเป็นสรุปวิธีการเขียนของฟังก์ชันแต่ละชนิด

```cpp
#include <iostream>

using namespace std;

// ไม่มี parameter และไม่มี return
void hello() { 
    cout << "Hello!\n"; 
}

// มี parameter แต่ไม่มี return
void printSum(int a, int b) { 
    cout << a << " + " << b << " = " << b << '\n';
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
    cout << num << '\n'; // output คือ 42
    
    int result = add(10, 20);
    cout << result << '\n'; // output คือ 30
}
```

!!! info "การใช้ `return` เพื่อหยุดการทำงานของฟังก์ชัน"
    คำสั่ง `return` เป็นคำสั่งที่ใช้ในการคืนค่าในฟังก์ชัน (ถ้ามี) แต่หลังจากนั้นจะหยุดการทำงานของฟังก์ชันไปเลย ดังนั้น เราสามารถใช้ `return` เป็นการหยุดฟังก์ชันไปในตัวได้

    พิจารณาโค้ดตัวอย่างต่อไปนี้

    ```cpp
    void checkAge(int age) {
        if(age < 18) {
            cout << "Not allowed\n";
        } else {
            cout << "Allowed\n";
        }
    }
    ```

    ```cpp
    void checkAge(int age) {
        if(age < 18) {
            cout << "Not allowed\n";
            return; // หยุดการทำงานของฟังก์ชันไปในตัว
        }
        cout << "Allowed\n";
    }
    ```

    ฟังก์ชัน 2 ฟังก์ชันนี้จะแสดงผลลัพธ์เหมือนกัน

!!! note "โจทย์ตัวอย่าง"
    จงเขียนฟังก์ชันเพื่อคำนวณพื้นที่สามเหลี่ยมสูง H ฐานยาว B (H และ B เป็นจำนวนเต็ม) โดยคืนค่าออกมาเป็นทศนิยม 2 ตำแหน่ง
??? note "เฉลย"
    ```cpp
    #include <iostream>
    #include <iomanip>

    using namespace std;

    float triangle_area(int H, int B) { // ประกาศฟังก์ชัน ชื่อว่า "triangle_area" ซึ่งรับค่าเป็นจำนวนเต็ม 2 ตัว และคืนค่าออกมาเป็นทศนิยม
        return ((float) H) * B / 2; // เปลี่ยน H ให้เป็นทศนิยมก่อน เพื่อที่จะได้คำตอบออกมาเป็นทศนิยม แล้วนำไปเข้าสูตร พื้นที่ = 1/2 * ฐาน * สูง
    }

    int main() {
        cout << fixed << setprecision(2) << triangle_area(5, 10); // จะได้ output ออกมาเป็น 25.00
    }
    ```

## ขอบเขตของตัวแปร

ตัวแปรในภาษา C/C++ จะมีขอบเขตที่สามารถใช้งานได้ (เรียกว่า scope)

เช่น ตัวแปรที่ถูกประกาศใช้ใน `if` จะสามารถใช้ได้แค่ใน `if` เท่านั้น ไม่สามารถใช้นอก `if` ได้

```cpp
#include <iostream>

using namespace std;

int main() {
    int x = 5;
    if(x == 5) {
        int y = 2;
    }
    cout << y; // compile error
}
```
สังเกตว่า `cout` จะไม่สามารถคอมไพล์ได้ เพราะตัวแปร y ไม่สามารถใช้นอก `if` ได้

สามารถเขียนโค้ดข้างบนให้คอมไฟล์ผ่านได้ดังนี้

```cpp
#include <iostream>

using namespace std;

int main() {
    int x = 5, y;
    if(x == 5) {
        y = 2;
    }
    cout << y; // output คือ 2
}
```
ในทำนองเดียวกัน ตัวแปรที่ถูกประกาศภายในฟังก์ชัน จะใช้งานได้แค่ในฟังก์ชันที่ตัวแปรถูกประกาศเท่านั้น

### ตัวแปรประเภท global
เราสามารถประกาศตัวแปรไว้ข้างนอกฟังก์ชันใดๆ ได้ โดยตัวแปรนี้ (เรียกว่า ตัวแปรประเภท global) ทุกฟังก์ชัน จะสามารถเข้าถึงได้ สามารถเปลี่ยนแปลงค่าได้ เช่น
```cpp
#include <iostream>

using namespace std;

int count = 0;

void increase_count() {
    count = count + 1; // เพิ่มค่า count ด้วย 1
}

int main() {
    increase_count(); // count = 0 + 1 = 1
    increase_count(); // count = 1 + 1 = 2
    increase_count(); // count = 2 + 1 = 3
    cout << count << '\n'; // output จะได้ 3
}
```
    
## การประกาศฟังก์ชัน

การประกาศฟังก์ชัน สามารถแบ่งได้เป็น 2 วิธี คือ 

1. ประกาศก่อนใช้งาน
2. ประกาศหลังใช้งาน

ในตัวอย่างด้านบน ได้ทำการประกาศฟังก์ชันไว้ก่อนฟังก์ชัน `main()` ซึ่งถือเป็นการประกาศก่อนใช้งาน

ถ้าเกิดต้องการประกาศหลัง `main()` จำเป็นต้องประกาศ prototype ไว้ก่อน แล้วค่อยเขียนฟังก์ชันทีหลัง เช่น

```cpp
#include <iostream>

using namespace std;

int add(int, int);

int main() {
    cout << add(1, 2); // output คือ 3
}

int add(int x, int y) {
    return x+y;
}
```

prototype เป็นเหมือนประโยคที่บอกข้อมูลต่างๆ เกี่ยวกับฟังก์ชัน เช่น ชื่อ พารามีเตอร์ โดยไม่จำเป็นต้องบอกทั้งฟังก์ชัน แต่เป็นข้อมูลคร่าวๆ ให้โปรแกรมรู้ว่ามีฟังก์ชันนี้อยู่ โดยในโค้ดด้านบน `int add(int, int);` เป็น prototype แบบหนึ่ง

ถ้าเกิดประกาศฟังก์ชันหลัง `main()` และไม่ประกาศ prototype โปรแกรมจะ compile error

## Recursive Function

Recursive Function คือฟังก์ชันที่ เรียกใช้งานตัวเอง ภายในฟังก์ชันเดียวกัน ใช้เมื่อปัญหาสามารถแบ่งออกเป็นปัญหาย่อยๆ ที่มีลักษณะเหมือนกัน

```cpp
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

```cpp
#include <iostream>

using namespace std;

int factorial(int n) {
    if (n == 0) return 1;        // base case คือ เมื่อ n เป็น 0 ให้คืนค่า 1
    return n * factorial(n - 1); // recursive case คือ เมื่อ n > 0 ให้คืนค่า n * factorial(n-1) [จาก n! = n * (n-1)!]
}

int main() {
    int num = 5;
    cout << num << "! = " << factorial(num); // จะได้ output คือ "5! = 120"
    return 0;
}
```

ในโค้ดด้านบน สมมติว่าเราเรียกใช้ `factorial(5)` สามารถมองเป็นแผนภาพได้ดังนี้
```cpp
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

    ```cpp
    #include <iostream>

    int factorial(int n) {
        return n * factorial(n - 1);
    }

    int main() {
        int num = 5;
        cout << num << "! = " << factorial(num);
        return 0;
    }
    ```

    หากลองรัน จะพบว่า โค้ดนี้จะไม่แสดงผลใดๆ และเกิดข้อผิดพลาดระหว่างการทำงาน

!problems [prog-0019]