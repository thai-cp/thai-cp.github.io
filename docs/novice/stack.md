---
title: Stack 
author: Nagorn Phongphasura
level:
---

ลองนึกสถานการณ์ขึ้นมาว่า คุณต้องการโครงสร้างข้อมูลหนึ่ง ที่สามารถเก็บข้อมูลเข้าไป แล้วดึงตัวที่เก็บล่าสุดออกมา เหมือนกับการวางจานซ้อนทับกันกองหนึ่ง คุณสามารถแก้ไขปัญหานี้ได้ด้วยการใช้สิ่งที่เรียกว่า **Stack**

## Stack

**Stack** ใน C++ จะถูก include อยู่ใน library `<stack>` ซึ่ง Stack มีการทำงานแบบ "Last In First Out" (LIFO) นั่นคือ ช่องที่เรานำข้อมูลมาใส่ จะเป็นช่องเดียวกันกับทางที่เราดึงข้อมูลออกมา ซึ่งทั้งการเพิ่มข้อมูล การเอาข้อมูลออก และการเรียกข้อมูลตัวแรก จะใช้ Time Complexity เพียง $O(1)$

### Operations

- Initialization

    ```cpp
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

    ```cpp
    // นำค่าใหม่ใส่ใน Stack
    void push(node* &stack, int val) {
        node* newNode = new node();
        newNode->data = val;
        newNode->next = stack;
        stack = newNode;
    }
    ```

- `pop()`: ใช้ในการนำข้อมูลออกจาก Stack

    ```cpp
    // pop ตัวบนสุดทิ้ง
    void pop(node* &stack) {
        if (stack == nullptr) return;
        node* temp = stack;
        stack = stack->next;
        delete temp;
    }
    ```

- `top()`: ใช้ในการเรียกค่าตัวบนของ Stack

    ```cpp
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

    ```cpp
    // ตรวจสอบว่า Stack ว่างหรือไม่
    bool empty(node* stack) {
        return stack == nullptr;
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

## STL

C++ มี Stack ที่มีการทำงานเหมือนกันกับที่เราเขียนข้างต้น แต่สามารถใช้งานได้ง่ายกว่ามาก โดยสามารถ include จาก library `<stack>` ได้เลย

### Operations

- Initialization

    ```cpp
    #include <stack>
    
    int main() {
        stack<int> st;
    }
    ```

- `push()`: ใช้ในการเพิ่มข้อมูลเข้า Stack

    ```cpp
    st.push(10);
    st.push(20);
    st.push(30);
    ```

- `pop()`: ใช้ในการนำข้อมูลออกจาก Stack

    ```cpp
    st.pop(); // นำข้อมูลตัวบนสุดออก
    ```

- `top()`: ใช้ในการเรียกค่าตัวบนของ Stack

    ```cpp
    int topValue = st.top(); // เรียกค่าตัวบนสุด
    ```

- `empty()`: ใช้ในการตรวจสอบว่า Stack ว่างหรือไม่

    ```cpp
    if (st.empty()) {
        cout << "Stack is empty!" << endl;
    }
    ```

- `size()`: ใช้ในการเช็คจำนวนข้อมูลใน Stack

    ```cpp
    int stackSize = st.size();
    ```

- ตัวอย่างการใช้งาน

    ```cpp
    #include <iostream>
    #include <stack>

    using namespace std;

    int main() {
        stack<int> st;

        st.push(10);
        st.push(20);
        st.push(30);

        cout << "Stack top: " << st.top() << endl;
        
        st.pop();
        
        cout << "Stack top after pop: " << st.top() << endl;
        cout << "Stack size: " << st.size() << endl;
        
        if (!st.empty()) {
            cout << "Stack is not empty!" << endl;
        }

        return 0;
    }
    ```

## โจทย์

!unfinished
