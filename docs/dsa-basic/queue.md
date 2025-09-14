---
title: Queue
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่อยู่หน้าสุดออกมา เหมือนกับการต่อคิวเพื่อเข้าร้านอาหาร คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Queue**

## Queue

**Queue** ใน C++ จะถูก include อยู่ใน library `<queue>` ซึ่ง Queue มีการทำงานแบบ "First In First Out" (FIFO) นั่นคือ เราจะนำข้อมูลใหม่มาใส่ตรงท้ายแถว แล้วเวลาจะนำข้อมูลออก จะนำออกมาทางด้านหน้าแถว ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ [Time Complexity](/dsa-basic/complexity) เพียง $O(1)$

## Operations
- Initialization
    ```cpp title="การ Implement ใน C++"
    // ประกาศ
    struct node {
        int data;
        node* next;
    };
    
    struct queue {
        node* front;
        node* back;
    };

    void init(queue &q) {
        q.front = q.back = nullptr;
    }

    int main() {
        queue q;
        init(q);
    }
    ```
- `push()`: ใช้ในการเพิ่มข้อมูลเข้า Queue (ใส่ท้ายแถว)
    ```cpp title="การ Implement ใน C++"
    // เพิ่มข้อมูลเข้า Queue
    void push(queue &q, int val) {
        node* newNode = new node();
        newNode->data = val;
        newNode->next = nullptr;
        if (q.back == nullptr) { // คิวว่าง
            q.front = q.back = newNode;
        } 
        else {
            q.back->next = newNode;
            q.back = newNode;
        }
    }
    ```
- `pop()`: ใช้ในการนำข้อมูลออกจาก Queue (ดึงหน้าสุด)
    ```cpp title="การ Implement ใน C++"
    // นำข้อมูลออกจาก Queue
    void pop(queue &q) {
        node* temp = q.front;
        q.front = q.front->next;
        if (q.front == nullptr) q.back = nullptr;
        delete temp;
    }
    ```
- `front()`: ใช้ในการเรียกค่าตัวหน้าสุดของ Queue
    ```cpp title="การ Implement ใน C++"
    // เรียกค่าตัวหน้าสุดของ Queue
    int front(queue &q) {
        return q.front->data;
    }
    ```
- ตัวอย่างการใช้งาน
    ```cpp title="ตัวอย่างการใช้งาน Queue"
    #include <iostream>
    using namespace std;

    // ประกาศ
    struct node {
        int data;
        node* next;
    };
    
    struct queue {
        node* front;
        node* back;
    };

    void init(queue &q) {
        q.front = q.back = nullptr;
    }

    // เพิ่มข้อมูลเข้า Queue
    void push(queue &q, int val) {
        node* newNode = new node();
        newNode->data = val;
        newNode->next = nullptr;
        if (q.back == nullptr) { // คิวว่าง
            q.front = q.back = newNode;
        } 
        else {
            q.back->next = newNode;
            q.back = newNode;
        }
    }

    // นำข้อมูลออกจาก Queue
    void pop(queue &q) {
        node* temp = q.front;
        q.front = q.front->next;
        if (q.front == nullptr) q.back = nullptr;
        delete temp;
    }

    // เรียกค่าตัวหน้าสุดของ Queue
    int front(queue &q) {
        return q.front->data;
    }

    int main() {
        queue q;
        init(q);

        push(q, 10);
        push(q, 20);
        push(q, 30);

        cout << "Front: " << front(q) << endl;
        pop(q);
        cout << "Front after pop: " << front(q) << endl;
    }
    ```
## โจทย์

!problems [prog-0003, prog-0004, prog-0010, prog-0016, prog-0020, prog-0021, prog-0025, prog-0030, prog-0033, prog-0035, prog-0043]
