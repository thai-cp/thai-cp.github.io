---
title: Time Complexity
author: Pakin Olanraktham & Pasit Sangprachathanarak
level: 
---

!resources [(Time Complexity, https://usaco.guide/bronze/time-comp, USACO), (Time complexity, https://usaco.guide/CPH.pdf#page=27, CPH)]

เนื่องจากใน Competitive Programming เราต้องการโปรแกรมที่มีประสิทธิภาพดี นั่นคือโปรแกรมสามารถทำงานได้อย่างรวดเร็ว หากโปรแกรมทำงานช้าเกินไป อาจโดนตัดคะแนน หรือไม่ได้คะแนนเลยก็ได้

Time Complexity คือ การประมาณจำนวน "ขั้นตอน" ที่อัลกอริทึมใช้กับ input ขนาด $n$ โดยไม่ต้องรันโค้ดจริง เราจะเขียนในรูปฟังก์ชันของ $n$ แล้วประมาณค่าเฉพาะพฤติกรรมเมื่อ $n$ มีค่ามากๆ โดยเครื่องมือมาตรฐานที่ใช้คือ Big O notation โดยใน 1 วินาที C++ จะสามารถทำได้ประมาณ $5\times 10^8$ ขั้นตอน

## Big O คืออะไร

Big O (บิ๊กโอ) ใช้บอกขอบเขตบนของจำนวนขั้นตอนในกรณีที่แย่ที่สุด (worst case) เราเขียนว่า $\mathcal{O}(f(n))$ โดยละทิ้งค่าคงที่ และพจน์อันดับต่ำกว่า

ตัวอย่าง: ถ้าจำนวนขั้นตอนจริง ๆ คือ $3n^2 + 5n + 100$ เราเขียนสั้น ๆ ว่า $\mathcal{O}(n^2)$

!!! info "สรุป"
    Big O คือ ภาษาย่อที่ช่วยบอกความเร็วโดยไม่สนใจรายละเอียดเล็ก ๆ (ค่าคงที่) ทำให้เราประเมินจำนวน "ขั้นตอน" ได้เร็ว

## ตัวอย่างพื้นฐาน

โค้ดต่อไปนี้เป็น $\mathcal{O}(1)$ (จำนวนคำสั่งคงที่ ไม่ขึ้นกับ $n$)

```cpp
int a = 5;
int b = 7;
int c = 4;
int d = a + b + c + 153;
```

### ลูปเดี่ยว

หากภายใน Loop มี Complexity $\mathcal{O}(1)$ และ Loop ทำงาน $n$ รอบ เราจะได้ Complexity รวมคือ $n\times\mathcal{O}(1)$ หรือก็คือ $\mathcal{O}(n)$

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

ค่าคงที่ ไม่มีผลต่อการคำนวณ Complexity โดยโค้ดด้านล่าง ทั้งสอง ก็ยังคงมี Complexity เท่ากันคือ $\mathcal{O}(n)$ เหมือนเดิม

```cpp
for (int i = 1; i <= 5*n + 17; i++) { /* O(1) */ }
for (int i = 1; i <= n + 457737; i++) { /* O(1) */ }
```

### ลูปซ้อน (Nested Loops)

เราจะใช้วิธีเดียวกับการคำนวณ Complexity ของ Loop ปกติ

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= m; j++) {
        // O(1)
    }
}
```

จากโค้ดข้างต้น เรารู้ว่าลูปด้านใน มี Complexity เท่ากับ $\mathcal{O}(m)$ แต่ลูปนี้ ทำงาน $n$ รอบเนื่องจากมีลูปอีกอันครอบอยู่ ดังนั้น Complexity รวมจะเท่ากับ $n\times\mathcal{O}(m)$ หรือก็คือ $\mathcal{O}(nm)$ นั่นเอง

### หลายลูป

Complexity รวมคือ max ของแต่ละลูป:

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

ลูปแรก $\mathcal{O}(n^2)$ ลูปสอง $\mathcal{O}(n)$ ดังนั้นรวม = $\mathcal{O}(n^2)$

### กรณีมี input หลายขนาด เช่น $n$ และ $m$

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

!!! note "คำแนะนำ"
    ในทางปฏิบัติ เราไม่จำเป็นต้องย่อให้เหมือนเป๊ะกับ Big O notation ที่กล่าวมาข้างต้นทั้งหมดก็ได้ เอาแค่ให้รู้คร่าวๆ ว่าโปรแกรมทำงานได้เร็วหรือช้าแค่ไหน เช่น $\mathcal{O}(n^2)$ ก็สามารถที่จะรู้ได้แล้ว ว่าโปรแกรม สามารถทำงานได้ทัน ตามขอบเขตข้อมูลหรือไม่

## Quiz

จงหา Complexity (Big O) ของโค้ดดังต่อไปนี้

```cpp
for (int i = 1; i <= 12345; i++) {
    // O(1)
}
```

??? note "เฉลย"
    อย่าลืมว่าเราไม่นำค่าคงที่มาคิด ดังนั้น คำตอบต้องเป็นแค่ $\mathcal{O}(1)$

```cpp
for (int i = 1; i <= n; i++) {
    for (int j = i; j <= n; j++) {
        // O(1)
    }
}
```

??? note "เฉลย"
    จะมีการทำงานทั้งหมด $n + (n-1) + (n-2) + \dots + 1 = \frac{n(n+1)}{2}$ ครั้ง ซึ่งเทียบได้กับ $\mathcal{O}(n^2)$

<!-- ## Complexity ที่พบบ่อย

| รูปแบบ | ตัวอย่าง | Complexity |
|--------|----------|------------|
| คำนวณสูตรคณิต | ตอบค่าโดยตรง | $\mathcal{O}(1)$ |
| Binary Search | หาตำแหน่งในอาร์เรย์เรียง | $\mathcal{O}(\log n)$ |
| เช็คจำนวนเฉพาะ | ตรวจหารากสูงสุด | $\mathcal{O}(\sqrt{n})$ |
| อ่าน input n ตัว | scanning | $\mathcal{O}(n)$ |
| Sorting (ทั่วไป) |  qsort ใน C / std::sort ใน C++ | $\mathcal{O}(n \log n)$ |
| ทุก permutation | next_permutation | $\mathcal{O}(n!)$ | -->

## ตารางประเมินความเป็นไปได้

โดยทั่วไป (ภายใต้ time limit ประมาณ 1 วินาที ในภาษา C++) จะรองรับได้ประมาณนี้:

| ขนาด $n$ | Complexities ที่ยังพอเป็นไปได้ |
|--------------------|----------------------------------|
| $\le 10$ | $\mathcal{O}(n!)$, $\mathcal{O}(n^7)$, $\mathcal{O}(n^6)$ |
| $\le 20$ | $\mathcal{O}(2^n\times n)$, $\mathcal{O}(n^5)$ |
| $\le 80$ | $\mathcal{O}(n^4)$ |
| $\le 400$ | $\mathcal{O}(n^3)$ |
| $\le 7.5 \times 10^3$ | $\mathcal{O}(n^2)$ |
| $\le 7 \times 10^4$ | $\mathcal{O}(n \sqrt n)$ |
| $\le 5 \times 10^5$ | $\mathcal{O}(n \log n)$ |
| $\le 5 \times 10^6$ | $\mathcal{O}(n)$ |
| $\le 10^{18}$ | $\mathcal{O}(\log^2 n)$, $\mathcal{O}(\log n)$, $\mathcal{O}(1)$ |

!!! info "อ้างอิงจาก"
    [USACO Guide](https://usaco.guide/bronze/time-comp)

## Constant Factor คืออะไร

แม้สองอัลกอริทึมจะอยู่ในคลาสเดียวกัน (เช่น $\mathcal{O}(n)$) ตัวคูณข้างหน้าก็ต่างกันได้ เช่น ทำ 1 การบวก เร็วกว่าทำ 1 ล้านการบวก แม้ทั้งคู่เป็น $\mathcal{O}(1)$ เพราะมี Constant Factor ที่ไม่เท่ากัน
