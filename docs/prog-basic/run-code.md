---
title: วิธีการรันโปรแกรม
author: Pakin Olanraktham
level:
---

## การรันโค้ดภายในเครื่อง (Running Code Locally)

!resources [(Download VS Code, https://code.visualstudio.com/Download, VS Code), (C/C++ for VS Code, https://code.visualstudio.com/docs/languages/cpp, VS Code)]

ในการรันโปรแกรม เราจะต้องใช้ "Code Editor" หรือ "IDE" โดยที่นิยม ของภาษา C/C++ ได้แก่

1. Visual Studio Code (แนะนำ)
2. Code::Blocks (ไม่แนะนำ เนื่องจาก Crash ง่ายและบ่อย)

## การลงโปรแกรม Visual Studio Code และการ Set Up

### Windows

**การติดตั้ง VS Code**

1. ไปที่ [Visual Studio Code](https://code.visualstudio.com/download)
2. ดาวน์โหลดเวอร์ชันสำหรับ Windows
3. เปิดไฟล์ '.exe' ที่ได้มา
4. ทำตามขั้นตอนการติดตั้งจนเสร็จ

**การติดตั้ง Compiler**

!resources [(GCC with MinGW, https://code.visualstudio.com/docs/cpp/config-mingw, VS Code)]

1. ดาวน์โหลด [MinGW-w64](https://github.com/msys2/msys2-installer/releases/download/2024-12-08/msys2-x86_64-20241208.exe)
2. รัน Installer ของ MinGW และทำตามขั้นตอน เมื่อเสร็จสิ้น ให้ช่อง "Run MSYS2 now" ถูกเลือกอยู่ด้วย แล้วจึงกด "Finish"
3. ใน Terminal (ที่พึ่งเปิดขึ้นมาของ MSYS2) ให้รัน

```shell
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-gcc
```

4. กด Enter เมื่อถามว่า `Enter a selection (default=all)` แล้วจึงกด Y หากถามว่าจะทำต่อหรือไม่ จนเสร็จสิ้น
5. เปิด Settings แล้วค้นหาว่า "Edit environment variables for your account"
6. ใน "User variables" ให้เลือก "Path" แล้วกด "Edit"
7. เลือก "New" และเพิ่มที่อยู่ของ MinGW-w64 (หากตั้งค่าเป็น default ให้เลือก `C:\msys64\ucrt64\bin`)
8. กด "OK" และ "OK" อีกรอบใน "Environment Variables"
9. Restart คอมพิวเตอร์ และ VS Code
10. ตรวจสอบว่าลงสำเร็จหรือไม่ โดยพิมพ์คำสั่งต่อไปนี้ลงใน Command Prompt

```bash
gcc --version
g++ --version
gdb --version
```

หากติดตั้งสำเร็จ จะได้ version ของ GCC, g++, GDB

### Linux (Ubuntu)

**การติดตั้ง VS Code**

1. ไปที่ [Visual Studio Code](https://code.visualstudio.com/download)
2. ดาวน์โหลดเวอร์ชันสำหรับ Linux (เลือก .deb)
3. รัน `sudo apt install ./path/to/file.deb` โดยแก้ `path/to/file.deb` เป็นชื่อไฟล์ที่ดาวน์โหลดมา

**การติดตั้ง Compiler**

1. รัน `sudo apt-get update && sudo apt-get install build-essential gdb`

### MacOS

**การติดตั้ง VS Code**

1. ดาวน์โหลด VS Code for macOS
2. แตกไฟล์ .zip
3. ลาก Visual Studio Code.app ไปที่โฟลเดอร์ Applications

**การติดตั้ง Compiler**

1. รัน `xcode-select --install`

## การ Set Up และ ติดตั้ง Extension สำหรับ VS Code

<div style="margin: 1em 0;">
    <video controls muted loop style="width:100%; border:1px solid #ccc; border-radius:6px;">
        <source src="../../assets/vscode.mp4" type="video/mp4" />
    เบราว์เซอร์ของคุณไม่รองรับการเล่นวิดีโอนี้
    </video>
</div>

1. เปิดโปรแกรม VS Code
2. เปิด Setting แล้วเลือก "Auto Save" ให้เป็น "After Delay"
3. ดาวน์โหลด Extension "C/C++ Extension Pack"
4. ดาวน์โหลด Extension "Code Runner"
5. เปิด Setting ของ Extension "Code Runner"
6. เลื่อนหา "Run In Terminal" แล้วกดเครื่องหมายถูก
7. จากนั้นเลื่อนหา "Excutor Map" และกดตรง "Edit in settings.json"
8. แก้ตรง "c" ให้ เป็น `"c": "cd $dir && gcc -std=c11 -O2 -pipe -static -s $fileName -o $fileNameWithoutExt -lm && $dir$fileNameWithoutExt",`
9. แก้ตรง "cpp" ให้เป็น `"cpp": "cd $dir && g++ -std=c++17 -O2 -pipe -static -s $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",`

## การสร้างไฟล์

1. ตรงแถบ Menu ด้านซ้าย ให้เลือก "Explorer" แล้วกด "Open Folder"
2. เลือก Folder ที่ต้องการที่จะเก็บโค้ดต่างๆ
3. ตรงแถบด้านซ้าย ให้กด New File แล้วสร้างไฟล์ที่มีนามสกุล ".cpp" เช่น "hello.cpp"
4. กดไปที่ไฟล์นั้น จะมี Code Editor ขึ้นมาทางด้านขวา ซึ่งสามารถพิมพ์โค้ดได้เลย
5. หากต้องการจะรันโค้ด จะมีปุ่มรัน อยู่ทางมุมขวาบนของหน้าจอ ที่เป็นรูปสามเหลี่ยม ให้กด Drop Down แล้วเลือก "Run Code"

!!! note "เพิ่มเติม"
    - ในกรณีที่ไม่มี Code Runner (เครื่องของศูนย์อาจจะไม่ได้ติดตั้งมา) ให้กด "Run C/C++ File" แทน จากนั้น ด่านล่างให้เลือก Terminal
    - หากต้องการ Debug File (หา Error ของโค้ด) ให้กด "Debug C/C++ File" จากนั้น ด่านล่างให้เลือก Terminal

## การรันโค้ด Online

เว็บไซต์ที่แนะนำ เช่น

- [USACO ide](https://ide.usaco.guide/)
- [GDB online Debugger](http://onlinegdb.com/)
