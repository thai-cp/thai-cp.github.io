---
title: Factory Machines
source: CSES
fsource: CSES Problem Set
link: https://cses.fi/problemset/task/1620
difficulty: Normal
tags: [Sorting and Searching]
author:
prereq: ["[Binary search](../algorithm-basic/binary-search.md)"]
---

!problem_info CSES-Factory-Machines

??? note "เฉลย"
    === "C"
        ```c
        #include <stdbool.h>
        #include <stdio.h>

        int n, t;
        int machine[200005];

        bool check(long long mid) {
            long long ans = 0;
            for (int i = 0; i < n; i++) {
                ans += mid / machine[i];
                if (ans >= t)
                    return true;
            }
            return false;
        }

        int main() {
            scanf("%d %d", &n, &t);
            long long mn_element = 1000000000;
            for (int i = 0; i < n; i++) {
                scanf("%d", &machine[i]);
                if (machine[i] < mn_element)
                    mn_element = machine[i];
            }
            long long l = 1, r = mn_element * t;
            while (l < r) {
                long long mid = (l + r) / 2;
                if (check(mid)) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            printf("%lld", l);
        }
        ```
    === "C++"
        ```cpp
        #include <iostream>
        using namespace std;

        int n, t;
        int machine[200005];

        bool check(long long mid) {
            long long ans = 0;
            for (int i = 0; i < n; i++) {
                ans += mid / machine[i];
                if (ans >= t)
                    return true;
            }
            return false;
        }

        int main() {
            cin >> n >> t;
            long long mn_element = 1000000000;
            for (int i = 0; i < n; i++) {
                cin >> machine[i];
                if (machine[i] < mn_element)
                    mn_element = machine[i];
            }
            long long l = 1, r = mn_element * t;
            while (l < r) {
                long long mid = (l + r) / 2;
                if (check(mid)) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            cout << l;
        }
        ```
