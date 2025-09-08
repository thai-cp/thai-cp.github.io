---
title: วิธีการรันโปรแกรม
author: Pakin Olanraktham
---

## การรันโค้ดภายในเครื่อง (Running Code Locally)

!resource [(Download VS Code, https://code.visualstudio.com/Download), (C/C++ for VS Code, https://code.visualstudio.com/docs/languages/cpp)]

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
5. เปิด VS Code
6. ดาวน์โหลด Extension "C/C++ extension for VS Code"

**การติดตั้ง Compiler**

!resource [(GCC with MinGW, https://code.visualstudio.com/docs/cpp/config-mingw)]

1. ดาวน์โหลด [MinGW-w64](https://github.com/msys2/msys2-installer/releases/download/2024-12-08/msys2-x86_64-20241208.exe)
2. รัน Installer ของ MinGW และทำตามขั้นตอน เมื่อเสร็จสิ้น ให้ช่อง "Run MSYS2 now" ถูกเลือกอยู่ด้วย แล้วจึงกด "Finish"
3. ใน Terminal (ที่พึ่งเปิดขึ้นมาของ MSYS2) ให้รัน
```shell
pacman -S --needed base-devel mingw-w64-ucrt-x86_64-toolchain
```
4. กด Enter เมื่อถามว่า `Enter a selection (default=all)` แล้วจึงกด Y หากถามว่าจะทำต่อหรือไม่ จนเสร็จสิ้น
5. เปิด Settings แล้วค้นหาว่า "Edit environment variables for your account"
6. ใน "User variables" ให้เลือก "Path" แล้วกด "Edit"
7. เลือก "New" และเพิ่มที่อยู่ของ MinGW-w64 (หากตั้งค่าเป็น default ให้เลือก `C:\msys64\ucrt64\bin`)
8. กด "OK" และ "OK" อีกรอบใน "Environment Variables"
9. ตรวจสอบว่าลงสำเร็จหรือไม่ โดยพิมพ์คำสั่งต่อไปนี้ลงใน Command Prompt
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
5. เปิด VS Code
6. ดาวน์โหลด Extension "C/C++ extension for VS Code"

**การติดตั้ง Compiler**

1. รัน `sudo apt-get update && sudo apt-get install build-essential gbd`

### MacOS

**การติดตั้ง VS Code**

1. ดาวน์โหลด VS Code for macOS
2. แตกไฟล์ .zip
3. ลาก Visual Studio Code.app ไปที่โฟลเดอร์ Applications
4. เปิดใช้งาน VS Code
5. ดาวน์โหลด Extension "C/C++ extension for VS Code"

**การติดตั้ง Compiler**

1. รัน `xcode-select --install`

## การติดตั้ง Extension สำหรับ VS Code

1. ดาวน์โหลด Extension "Code Runner"
2. เปิด Setting ของ Extension
3. เลื่อนหา Excutor Map และกดตรง "Edit in settings.json"
4. แก้ตรง "c" ให้ เป็น `"c": "cd $dir && gcc -std=c11 -O2 -pipe -static -s $fileName -o $fileNameWithoutExt -lm && $dir$fileNameWithoutExt",`
5. แก้ตรง "cpp" ให้เป็น `"cpp": "cd $dir && g++ -std=c++17 -O2 -pipe -static -s $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",`