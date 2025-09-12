---
title: Time Complexity
author: Pakin Olanraktham & Pasit Sangprachathanarak
level: 
---

!resources [(Time Complexity, https://usaco.guide/bronze/time-comp, USACO), (Time complexity (ใช้อ้างอิงบทเรียนนี้), https://usaco.guide/CPH.pdf#page=27, CPH)]

เนื่องจากใน Competitive Programming เราต้องการโปรแกรมที่มีประสิทธิภาพดี นั่นคือโปรแกรมสามารถทำงานได้อย่างรวดเร็ว หากโปรแกรมทำงานช้าเกินไป อาจโดนตัดคะแนน หรือไม่ได้คะแนนเลยก็ได้

Time Complexity คือ การประมาณจำนวน "ขั้นตอน" ที่อัลกอริทึมใช้กับ input ขนาด $n$ โดยไม่ต้องรันโค้ดจริง เราจะเขียนในรูปฟังก์ชันของ $n$ แล้วประมาณค่าเฉพาะพฤติกรรมเมื่อ $n$ โตมากๆ โดยเครื่องมือมาตรฐานที่ใช้คือ Big O notation โดยใน 1 วินาที C++ จะสามารถทำได้ประมาณ $5\times 10^8$ ขั้นตอน

## Big O คืออะไร

Big O (บิ๊กโอ) ใช้บอกขอบเขตบนของจำนวนขั้นตอนในกรณีที่แย่ที่สุด (worst case) เราเขียนว่า $\mathcal{O}(f(n))$ โดยละทิ้งค่าคงที่ และเทอมอันดับต่ำกว่า

ตัวอย่าง: ถ้าจำนวนขั้นตอนจริง ๆ คือ $3n^2 + 5n + 100$ เราเขียนสั้น ๆ ว่า $\mathcal{O}(n^2)$

!!! info "สรุป"
    Big O คือ ภาษาย่อที่ช่วยบอกความเร็วโดยไม่สนใจรายละเอียดเล็ก ๆ (ค่าคงที่ / เทอมเล็ก) ทำให้เราประเมิน feasibility ได้เร็ว

## ตัวอย่างพื้นฐาน

โค้ดต่อไปนี้เป็น $\mathcal{O}(1)$ (จำนวนคำสั่งคงที่ ไม่ขึ้นกับ $n$)

```cpp
int a = 5;
int b = 7;
int c = 4;
int d = a + b + c + 153;
```

### ลูปเดี่ยว

จำนวนรอบลูป = เวลา (ถ้าภายในเป็นงาน $\mathcal{O}(1)$)

```cpp
for (int i = 1; i <= n; i++) {
    // O(1)
}

int i = 0;
while (i < n) {
    // O(1)
    i++;
}
```

ทั้งสองกรณีเป็น $\mathcal{O}(n)$

เรามองข้ามค่าคงที่กับเทอมเล็ก ดังนั้น:

```cpp
for (int i = 1; i <= 5*n + 17; i++) { /* O(1) */ }
for (int i = 1; i <= n + 457737; i++) { /* O(1) */ }
```

ก็ยังเป็น $\mathcal{O}(n)$

### ลูปซ้อน (Nested Loops)

คูณกันตามจำนวนรอบของแต่ละลูป:

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
        // O(1)
    }
}
```

= $\mathcal{O}(n\times m)$

กรณีจำนวนรอบลูปชั้นในขึ้นอยู่กับตัวแปรชั้นนอก:

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j++) {
        // O(1)
    }
}
```

ลูปในรันประมาณ $n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2} = \mathcal{O}(n^2)$

### หลายบล็อกต่อกัน

Complexity รวมคือ max ของแต่ละบล็อก:

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) { 
        /* O(1) */ 
    }
}
for (int i = 1; i <= n + 58834; i++) { 
    /* O(1) */ 
}
```

บล็อกแรก $\mathcal{O}(n^2)$ บล็อกสอง $\mathcal{O}(n)$ ดังนั้นรวม = $\mathcal{O}(n^2)$

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
            /* O(1) */ 
    }
}
for (int i = 1; i <= m; i++) {
    /* O(1) */ 
}
```

รวม = $\mathcal{O}(n^2 + m)$ (ยังไม่สามารถตัดเหลือ $\max(n^2, m)$ ถ้าไม่รู้ความสัมพันธ์ระหว่าง $n$ กับ $m$)

## Complexity ที่พบบ่อย

| รูปแบบ | ตัวอย่าง | Complexity |
|--------|----------|------------|
| คำนวณสูตรคณิต | ตอบค่าโดยตรง | $\mathcal{O}(1)$ |
| Binary Search | หาตำแหน่งในอาร์เรย์เรียง | $\mathcal{O}(\log n)$ |
| เช็คจำนวนเฉพาะ | ตรวจหารากสูงสุด | $\mathcal{O}(\sqrt{n})$ |
| อ่าน input n ตัว | scanning | $\mathcal{O}(n)$ |
| เดิน array/list | loop เดียว | $\mathcal{O}(n)$ |
| Sorting (ทั่วไป) |  qsort ใน C / std::sort ใน C++ | $\mathcal{O}(n \log n)$ |
| ทุก permutation | next_permutation | $\mathcal{O}(n!)$ |

## ตารางประเมินความเป็นไปได้

โดยทั่วไป (ภายใต้ time limit ประมาณ 1 วินาที ในภาษา C++) จะรองรับได้ประมาณนี้:

| ขนาด $n$ (สูงสุด) | Complexities ที่ยังพอเป็นไปได้ |
|--------------------|----------------------------------|
| $\le 10$ | $\mathcal{O}(n!)$, $\mathcal{O}(n^7)$, $\mathcal{O}(n^6)$ |
| $\le 20$ | $\mathcal{O}(2^n n)$, $\mathcal{O}(n^5)$ |
| $\le 80$ | $\mathcal{O}(n^4)$ |
| $\le 400$ | $\mathcal{O}(n^3)$ |
| $\le 7.5 \times 10^3$ | $\mathcal{O}(n^2)$ |
| $\le 7 \times 10^4$ | $\mathcal{O}(n \sqrt n)$ |
| $\le 5 \times 10^5$ | $\mathcal{O}(n \log n)$ |
| $\le 5 \times 10^6$ | $\mathcal{O}(n)$ |
| $\le 10^{18}$ | $\mathcal{O}(\log^2 n)$, $\mathcal{O}(\log n)$, $\mathcal{O}(1)$ |

## Constant Factor คืออะไร

แม้สองอัลกอริทึมจะอยู่ในคลาสเดียวกัน (เช่น $\mathcal{O}(n)$) ตัวคูณข้างหน้าก็ต่างกันได้ เช่น ทำ 1 การบวก เร็วกว่าทำ 1 ล้านการบวก แม้ทั้งคู่เป็น $\mathcal{O}(1)$ เพราะมี Constant Factor ที่ไม่เท่ากัน
