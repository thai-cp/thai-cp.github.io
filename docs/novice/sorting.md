---
title: Sorting Algorithms
author: Pasit Sangprachathanarak
level: 
---

!resources [(Introduction to Sorting, https://usaco.guide/bronze/intro-sorting, USACO), (Sorting (ใช้อ้างอิงบทเรียนนี้), https://usaco.guide/CPH.pdf#page=35, CPH)]

## Sorting Algorithms คืออะไร

Sorting Algorithms หรืออัลกอริทึมการเรียงลำดับข้อมูล
เป็นอัลกอริทึมที่ใช้เรียงลำดับข้อมูลจากมากไปน้อยหรือน้อยไปมากโดยอัลกอริทึมการเรียงลำ
ดับข้อมูลที่ดีคสรทำงานในเวลา [$\mathcal{O}(n\log n)$](complexity.md)

## Bubble Sort

การเรียงลำดับข้อมูบแบบ Bubble Sort จะวนซ้ำผ่านแต่ละค่าในอาร์เรย์ เมื่อใดก็ตามที่ค่าสองค่าที่เรียงต่อกันไม่อยู่ในลำดับที่ถูกต้อง  อัลกอริทึมจะสลับค่าเหล่านั้น สังเกตได้ว่าถ้าเกิดวนผ่าน 1 รอบ ค่าด้านขวาของอาร์เรย์จะมีค่ามากสุดเสมอ
เมื่อทำซ้ำ $n$ รอบ จะได้ว่า อาร์เรย์จะเรียงจากน้อยไปมาก

### รูปแบบการใช้งาน

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

!unfinished
