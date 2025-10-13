---
title: Queue
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่อยู่หน้าสุดออกมา เหมือนกับการต่อคิวเพื่อเข้าร้านอาหาร คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Queue**

## Queue

**Queue** ใน C++ จะถูก include อยู่ใน library `<queue>` ซึ่ง Queue มีการทำงานแบบ "First In First Out" (FIFO) นั่นคือ เราจะนำข้อมูลใหม่มาใส่ตรงท้ายแถว แล้วเวลาจะนำข้อมูลออก จะนำออกมาทางด้านหน้าแถว ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ Time Complexity เพียง $O(1)$

### Operations

- Initialization

    ```cpp
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

    ```cpp
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

    ```cpp
    // นำข้อมูลออกจาก Queue
    void pop(queue &q) {
        if (stack == nullptr) return;
        node* temp = q.front;
        q.front = q.front->next;
        if (q.front == nullptr) q.back = nullptr;
        delete temp;
    }
    ```

- `front()`: ใช้ในการเรียกค่าตัวหน้าสุดของ Queue

    ```cpp
    // เรียกค่าตัวหน้าสุดของ Queue
    int front(queue &q) {
        return q.front->data;
    }
    ```

- `empty()`: ใช้ในการตรวจสอบว่า Queue ว่างหรือไม่

    ```cpp
    // ตรวจสอบว่า Queue ว่างหรือไม่
    bool empty(queue &q) {
        return q.front == nullptr;
    }
    ```

- ตัวอย่างการใช้งาน

    ```cpp
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
        if (q.front == nullptr) return;
        node* temp = q.front;
        q.front = q.front->next;
        if (q.front == nullptr) q.back = nullptr;
        delete temp;
    }

    // เรียกค่าตัวหน้าสุดของ Queue
    int front(queue &q) {
        return q.front->data;
    }

    // ตรวจสอบว่า Queue ว่างหรือไม่
    bool empty(queue &q) {
        return q.front == nullptr;
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

## STL

C++ มี Queue ที่มีการทำงานเหมือนกันกับที่เราเขียนข้างต้น แต่สามารถใช้งานได้ง่ายกว่ามาก โดยสามารถ include จาก library `<queue>` ได้เลย

### Operations

- Initialization

    ```cpp
    #include <queue>
    
    int main() {
        queue<int> q;
    }
    ```

- `push()`: ใช้ในการเพิ่มข้อมูลเข้า Queue (ใส่ท้ายแถว)

    ```cpp
    q.push(10);
    q.push(20);
    q.push(30);
    ```

- `pop()`: ใช้ในการนำข้อมูลออกจาก Queue (ดึงหน้าสุด)

    ```cpp
    q.pop(); // นำข้อมูลตัวหน้าสุดออก
    ```

- `front()`: ใช้ในการเรียกค่าตัวหน้าสุดของ Queue

    ```cpp
    int frontValue = q.front(); // เรียกค่าตัวหน้าสุด
    ```

- `back()`: ใช้ในการเรียกค่าตัวท้ายสุดของ Queue

    ```cpp
    int backValue = q.back(); // เรียกค่าตัวท้ายสุด
    ```

- `empty()`: ใช้ในการตรวจสอบว่า Queue ว่างหรือไม่

    ```cpp
    if (q.empty()) {
        cout << "Queue is empty!" << endl;
    }
    ```

- `size()`: ใช้ในการเช็คจำนวนข้อมูลใน Queue

    ```cpp
    int queueSize = q.size();
    ```

- ตัวอย่างการใช้งาน

    ```cpp
    #include <iostream>
    #include <queue>

    using namespace std;

    int main() {
        queue<int> q;

        q.push(10);
        q.push(20);
        q.push(30);

        cout << "Front: " << q.front() << endl;
        cout << "Back: " << q.back() << endl;
        
        q.pop();
        
        cout << "Front after pop: " << q.front() << endl;
        cout << "Queue size: " << q.size() << endl;
        
        if (!q.empty()) {
            cout << "Queue is not empty!" << endl;
        }

        return 0;
    }
    ```

## โจทย์

!unfinished
