---
title: Stack 
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่เก็บล่าสุดออกมา เหมือนกับการวางจานซ้อนทับกันกองหนึ่ง คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Stack**

## Stack

**Stack** ใน C++ จะถูก include อยู่ใน library `<stack>` ซึ่ง Stack มีการทำงานแบบ "Last In First Out" (LIFO) นั่นคือ ช่องที่เรานำข้อมูลมาใส่ จะเป็นช่องเดียวกันกับทางที่เราดึงข้อมูลออกมา ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ Time Complexity เพียง $O(1)$

## Operations

- Initialization

    ```cpp title="การ Implement ใน C++"
    // ประกาศ
    struct node {
        int data;
        node* next;
    };
    
    int main() {
        node* stack = nullptr;
    }
    ```

- `push()`: ใช้ในการเพิ่มข้อมูลเข้า Stack

    ```cpp title="การ Implement ใน C++"
    // นำค่าใหม่ใส่ใน Stack
    void push(node* &stack, int val) {
        node* newNode = new node();
        newNode->data = val;
        newNode->next = stack;
        stack = newNode;
    }
    ```

- `pop()`: ใช้ในการนำข้อมูลออกจาก Stack

    ```cpp title="การ Implement ใน C++"
    // pop ตัวบนสุดทิ้ง
    void pop(node* &stack) {
        if (stack == nullptr) return;
        node* temp = stack;
        stack = stack->next;
        delete temp;
    }
    ```

- `top()`: ใช้ในการเรียกค่าตัวบนของ Stack

    ```cpp title="การ Implement ใน C++"
    // เรียกค่าบนสุดใน Stack
    int top(node* stack) {
        if (stack == nullptr) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return stack->data;
    }
    ```

- `empty()`: ใช้ในการตรวจสอบว่า Stack ว่างหรือไม่

    ```cpp title="การ Implement ใน C++"
    // ตรวจสอบว่า Stack ว่างหรือไม่
    bool empty(node* stack) {
        return stack == nullptr;
    }
    ```

- ตัวอย่างการใช้งาน

    ```cpp title="ตัวอย่างการใช้งาน Stack"
    #include <iostream>

    using namespace std;

    // ประกาศ
    struct node {
        int data;
        node* next;
    };

    // นำค่าใหม่ใส่ใน Stack
    void push(node* &stack, int val) {
        node* newNode = new node();
        newNode->data = val;
        newNode->next = stack;
        stack = newNode;
    }

    // pop ตัวบนสุดทิ้ง
    void pop(node* &stack) {
        if (stack == nullptr) return;
        node* temp = stack;
        stack = stack->next;
        delete temp;
    }

    // เรียกค่าตัวบนสุดใน Stack
    int top(node* stack) {
        if (stack == nullptr) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return stack->data;
    }

    // ตรวจสอบว่า Stack ว่างหรือไม่
    bool empty(node* stack) {
        return stack == nullptr;
    }

    int main() {
        node* stack = nullptr;

        push(stack, 10);
        push(stack, 20);
        push(stack, 30);

        cout << "Stack top: " << top(stack) << endl;
        cout << "Popped: " << pop(stack) << endl;
        cout << "Stack top after pop: " << top(stack) << endl;
    }
    ```

## โจทย์

!unfinished
