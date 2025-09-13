---
title: กุลีแห่งท่าเรือ (Labor at the Deck)
source: TOI
fsource: การแข่งขันคอมพิวเตอร์โอลิมปิกระดับชาติ
link: https://programming.in.th/tasks/toi11_labor
difficulty: Normal
tags: [Binary search]
author: 
prereq: ["[Binary search](../dsa-basic/binary-search.md)"]
extsol: https://programming.in.th/tasks/toi11_labor/solution
---

!problem_info TOI11-labor

??? note "เฉลย"
    === "C"
        ```c
        #include <stdio.h>
        #include <stdbool.h>

        int t[1000005];
        long long n;
        int m;

        bool check(long long x) {
            long long ans = 0;
            for (int i = 0; i < m; i++) {
                ans += (x / t[i]);
                if (ans >= n)
                    return true;
            }
            return false;
        }

        int main() {
            scanf("%d %lld", &m, &n);
            long long mn_element = 1000000;
            for (int i = 0; i < m; i++) {
                scanf("%d", &t[i]);
                if (t[i] < mn_element)
                    mn_element = t[i];
            }
            long long l = 1, r = mn_element * n;
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

        int t[1000005];
        long long n;
        int m;

        bool check(long long x) {
            long long ans = 0;
            for (int i = 0; i < m; i++) {
                ans += (x / t[i]);
                if (ans >= n)
                    return true;
            }
            return false;
        }

        int main() {
            ios::sync_with_stdio(false);
            cin.tie(nullptr);
            cin >> m >> n;
            long long mn_element = 1000000;
            for (int i = 0; i < m; i++) {
                cin >> t[i];
                if(t[i] < mn_element)
                    mn_element = t[i];
            }
            long long l = 1, r = mn_element * n;
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
