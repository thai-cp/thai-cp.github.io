---
title: Sorting Algorithms
author: Pasit Sangprachathanarak
level: Normal
---

!resources [(Introduction to Sorting, https://usaco.guide/bronze/intro-sorting, USACO), (Sorting (ใช้อ้างอิงบทเรียนนี้), https://usaco.guide/CPH.pdf#page=35, CPH)]

## Sorting Algorithms คืออะไร

Sorting Algorithms หรืออัลกอริทึมการเรียงลำดับข้อมูล
เป็นอัลกอริทึมที่ใช้เรียงลำดับข้อมูลจากมากไปน้อยหรือน้อยไปมากโดยอัลกอริทึมการเรียงลำ
ดับข้อมูลที่ดีคสรทำงานในเวลา [$\mathcal{O}(n\log n)$](https://thai-cp.github.io/dsa-basic/complexity/)

## Bubble Sort

การเรียงลำดับข้อมูบแบบ Bubble Sort ประกอบด้วย $n$ รอบ โดยในแต่ละรอบ อัลกอริทึมจะวนซ้ำผ่านแต่ละค่าในอาร์เรย์ เมื่อใดก็ตามที่ค่าสองค่าที่เรียงต่อกันไม่อยู่ในลำดับที่ถูกต้อง อัลกอริทึมจะสลับค่าเหล่านั้น โดยมีรูปแบบการใช้งานดังนี้:

```cpp
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n-1; j++) {
        if (array[j] > array[j+1]) {
            swap(array[j],array[j+1]);
        }
    }
}
```

### ตัวอย่างการทำงาน Bubble Sort

<div style="margin: 1em 0;">
    <video controls muted loop style="max-width:480px; width:100%; border:1px solid #ccc; border-radius:6px;">
        <source src="../../assets/bubble-sort.mp4" type="video/mp4" />
    เบราว์เซอร์ของคุณไม่รองรับการเล่นวิดีโอนี้
    </video>
</div>

!!! info "แหล่งที่มาวิดีโอ"
    วิดีโอตัวอย่างการทำงานของ Bubble Sort นำมาจาก [YouTube (ลิงก์ต้นฉบับ)](https://www.youtube.com/watch?v=0BkoXZBbhfU) เพื่อใช้ประกอบการเรียนรู้

## qsort

qsort เป็นฟังก์ชั่น Quick Sort อย่างง่ายในภาษา C ที่อยู่ใน library `stdlib.h` โดยมี Average [Time Complexity](https://thai-cp.github.io/dsa-basic/complexity/) อยู่ที่ $\mathcal{O}(n\log n)$ แต่ Worse Case อยู่ที่ $\mathcal{O}(n^2)$ จึงนิยมใช้ std::sort ของ C++ มากกว่า

### รูปแบบการใช้งาน

```c
void qsort(
    void *base,          // ตำแหน่งเริ่มอาเรย์
    size_t nitems,       // จำนวนสมาชิก
    size_t size,         // ขนาดของหนึ่งสมาชิก เช่น sizeof(int)
    int (*compar)(const void *, const void *) // ฟังก์ชันเปรียบเทียบ
);
```

ฟังก์ชันเปรียบเทียบต้องคืนค่า:

* `< 0` ถ้า a ควรมาก่อน b
* `= 0` ถ้าเท่ากัน (ลำดับไม่สำคัญ)
* `> 0` ถ้า a ควรมาหลัง b

!!! info "โจทย์"
    จงเรียงอาเรย์จำนวนเต็มจากน้อยไปมาก แล้วจากมากไปน้อย
    ??? info "เฉลย"
        ```c
        #include <stdio.h>
        #include <stdlib.h>

        int cmp_asc(const void *p1, const void *p2) {
            int a = *(const int*)p1;
            int b = *(const int*)p2;
            return a - b; // น้อยไปมาก
        }

        int cmp_desc(const void *p1, const void *p2) {
            int a = *(const int*)p1;
            int b = *(const int*)p2;
            return b - a; // มากไปน้อย (สลับลำดับ)
        }

        int main() {
            int asc[] = {5, 2, 9, 1, 5, 6};
            int desc[] = {5, 2, 9, 1, 5, 6};
            int n = sizeof(asc)/sizeof(asc[0]);

            qsort(asc, n, sizeof(int), cmp_asc);
            qsort(desc, n, sizeof(int), cmp_desc);

            printf("Ascending : ");
            for(int i=0;i<n;i++) printf("%d ", asc[i]);
            printf("\n");

            printf("Descending: ");
            for(int i=0;i<n;i++) printf("%d ", desc[i]);
            printf("\n");
        }
        /*
        ผลลัพธ์
        Ascending : 1 2 5 5 6 9 
        Descending: 9 6 5 5 2 1
        */
        ```
