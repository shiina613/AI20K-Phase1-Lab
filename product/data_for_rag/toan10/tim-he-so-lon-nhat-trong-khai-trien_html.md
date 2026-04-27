# Tìm hệ số lớn nhất trong khai triển

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/tim-he-so-lon-nhat-trong-khai-trien.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm hệ số lớn nhất trong khai triển nhị thức Newton (Niu-tơn), đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và Xác suất.

1. PHƯƠNG PHÁP GIẢI TOÁN

+ Áp dụng khai triển ${(a + b)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} {a^{n – k}}{b^k}.$

+ Xác định số hạng tổng quát $C_n^k{a^{n – k}}{b^k}$, suy ra hệ số tổng quát là một dãy số theo ${a_k}.$

+ Xét tính tăng giảm của ${a_k}$ từ đó tìm $k$ tương ứng.

+ Suy ra hệ số lớn nhất trong khai triển.

## Bài tập

## Bài 1: Cho khai triển: ${(1 + 2x)^n}$ $= {a_0} + {a_1}x + \ldots + {a_n}{x^n}$, trong đó $n \in {N^*}$ và các hệ số ${a_0}$, ${a_1}$, …, ${a_n}$ thỏa mãn ${a_0} + \frac{{{a_1}}}{2} + \ldots + \frac{{{a_n}}}{{{2^n}}} = 4096.$ Tìm số lớn nhất trong các số ${a_0}$, ${a_1}$, …, ${a_n}.$

Lời giải:

Ta có: ${(1 + 2x)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} {2^k}{x^k}.$

Chọn $x = \frac{1}{2}$, ta được: $\sum\limits_{k = 0}^n {C_n^k} = {2^n}.$

Suy ra: ${a_0} + \frac{{{a_1}}}{2} + \ldots + \frac{{{a_n}}}{{{2^n}}}$ $= \sum\limits_{k = 0}^n {C_n^k}$ $\Leftrightarrow {2^n} = 4096$ $\Leftrightarrow n = 12.$

Xét số tổng quát trong khai triển là: ${a_k} = C_{12}^k{2^k}.$

Xét dãy số ${a_k} = C_{12}^k{.2^k}$, ta có: ${a_{k + 1}} = C_{12}^{k + 1}{.2^{k + 1}}.$

Xét ${a_k} – {a_{k + 1}} > 0$ $\Leftrightarrow C_{12}^k{.2^k} – C_{12}^{k + 1}{.2^{k + 1}} > 0.$

$\Leftrightarrow \frac{{12!{2^k}}}{{k!(12 – k)!}} – \frac{{12!{2^{k + 1}}}}{{(k + 1)!(11 – k)!}} > 0$ $\Leftrightarrow \frac{{12!{2^k}}}{{k!(11 – k)!}}\left( {\frac{1}{{12 – k}} – \frac{2}{{k + 1}}} \right) > 0.$

$\Leftrightarrow \frac{1}{{12 – k}} – \frac{2}{{k + 1}} > 0$ $\Leftrightarrow 3k – 23 > 0$ $\Leftrightarrow k > \frac{{23}}{3} \approx 7,7.$

Do đó ${a_8} > {a_9} > \ldots > {a_{12}}.$

Tương tự: ${a_k} – {a_{k + 1}} < 0$ $\Leftrightarrow k < \frac{{23}}{3}.$

Do đó ${a_8} > {a_7} > \ldots > {a_0}.$

Vậy $\max \left( {{a_0},{a_1}, \ldots ,{a_n}} \right) = {a_8}$ $= C_{12}^8{2^8} = 126720.$

## Bài 2: Tìm $k \in \{ 0;1;2; \ldots ;2005\}$ sao cho $C_{2005}^k$ đạt giá trị lớn nhất.

Lời giải:

Ta có: $C_{2005}^k$ lớn nhất 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{C_{2005}^k \ge C_{2005}^{k + 1}}\\
{C_{2005}^k \ge C_{2005}^{k – 1}}
\end{array}} \right.
$$
 $(\forall k \in \{ 0;1;2; \ldots ;2005\} ).$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{2005!}}{{k!(2005 – k)!}} \ge \frac{{2005!}}{{(k + 1)!(2004 – k)!}}}\\
{\frac{{2005!}}{{k!(2005 – k)!}} \ge \frac{{2005!}}{{(k – 1)!(2006 – k)!}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{1}{{2005 – k}} \ge \frac{1}{{k + 1}}}\\
{\frac{1}{k} \ge \frac{1}{{2006 – k}}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{k + 1 \ge 2005 – k}\\
{2006 – k \ge k}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{k \ge 1002}\\
{k \le 1003}
\end{array}} \right.
$$
 $\Leftrightarrow 1002 \le k \le 1003.$

Vậy $C_{2005}^k$ đạt giá trị lớn nhất khi và chỉ khi 
$$
\left[ {\begin{array}{l}
{k = 1002}\\
{k = 1003}
\end{array}} \right..
$$

## Bài 3: Tìm hệ số lớn nhất trong khai triển nhị thức Newton của ${\left( {\frac{1}{3} + \frac{2}{3}x} \right)^{15}}.$

Lời giải:

Ta có: ${\left( {\frac{1}{3} + \frac{2}{3}x} \right)^{15}}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {\left( {\frac{1}{3}} \right)^{15 – k}}\left( {\frac{2}{3}} \right){x^k}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} \frac{{{2^k}}}{{{3^{15}}}}{x^k}.$

Gọi ${a_k}$ là hệ số của ${x^k}$ trong khai triển, với $k = \overline {0..15} .$

Xét dãy số ${a_k} = \frac{1}{{{3^{15}}}}C_{15}^k{2^k}.$

Ta có: ${a_{k + 1}} = \frac{1}{{{3^{15}}}}C_{15}^{k + 1}{.2^{k + 1}}.$

Suy ra: ${a_k} < {a_{k + 1}}$ $\Leftrightarrow \frac{1}{{{3^{15}}}}C_{15}^k{.2^k} < \frac{1}{{{3^{15}}}}C_{15}^{k + 1}{.2^{k + 1}}$ $\Leftrightarrow \frac{{15!}}{{k!(15 – k)!}} < \frac{{15!}}{{(k + 1)!(14 – k)!}}.2.$

$\Leftrightarrow \frac{1}{{15 – k}} < \frac{2}{{k + 1}}$ $\Leftrightarrow k + 1 < 30 – 2k$ $\Leftrightarrow k < \frac{{29}}{3}.$

Vậy ${a_0} < {a_1} < {a_2} < \ldots < {a_{10}}.$

Ngược lại: ${a_k} > {a_{k + 1}}$ $\Leftrightarrow k > \frac{{29}}{3}.$

Suy ra: ${a_{10}} > {a_{11}} > {a_{12}} > \ldots > {a_{15}}.$

Vậy hệ số lớn nhất trong khai triển trên là: ${a_{10}} = \frac{{{2^{10}}}}{{{3^{15}}}}C_{15}^{10} = 3003.\frac{{{2^{10}}}}{{{3^{15}}}}.$

## Bài 4: Trong khai triển của ${\left( {\frac{1}{3} + \frac{2}{3}x} \right)^{10}}$ thành đa thức ${a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{10}}{x^{10}}$ $\left( {{a_k} \in R} \right).$ Tìm hệ số ${a_k}$ lớn nhất $(0 \le k \le 10).$

Lời giải:

Ta có: ${a_{k – 1}} \le {a_k}$ $\Leftrightarrow C_{10}^{k – 1}{.2^{k – 1}} \le C_{10}^k{.2^k}$ $\Leftrightarrow \frac{1}{{(k – 1)!(11 – k)!}} \le \frac{2}{{k!(10 – k)!}}.$

$\Leftrightarrow k \le 2(11 – k)$ $\Leftrightarrow k \le \frac{{22}}{3}.$

Vậy hệ số ${a_7}$ là lớn nhất: ${a_7} = \frac{1}{{{3^{10}}}}.C_{10}^7{.2^7}.$

## Bài 5: Cho $n$ là số nguyên dương cố định. Chứng minh rằng $C_n^k$ lớn nhất nếu $k$ là một số tự nhiên lớn nhất không vượt quá $\frac{{n + 1}}{2}.$

Lời giải:

Ta có: $C_n^k = \frac{{n!}}{{k!(n – k)!}}$ và $C_n^{k – 1} = \frac{{n!}}{{(k – 1)!(n – k + 1)!}}$ $\Rightarrow \frac{{C_n^k}}{{C_n^{k – 1}}} = \frac{{n – k + 1}}{k}.$

Do đó: $C_n^k > C_n^{k – 1}$ $\Leftrightarrow \frac{{n – k + 1}}{k} > 1$ $\Leftrightarrow k < \frac{{n + 1}}{2}.$

Suy ra $C_n^k$ lớn nhất nếu $k$ là số tự nhiên lớn nhất không vượt quá $\frac{{n + 1}}{2}.$

## Bài 6: Khai triển đa thức $P(x) = {(1 + 2x)^{12}}$ thành dạng $P(x) = {a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_{12}}{x^{12}}.$ Hãy tìm $\max \left( {{a_1},{a_2},{a_3}, \ldots ,{a_{12}}} \right).$

Lời giải:

Ta có: $P(x) = {(1 + 2x)^{12}}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} .{(2x)^k}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {.2^k}.{x^k}.$

Do đó: ${a_k} = C_{12}^k{.2^k}.$

Xét dãy số ${a_k} = C_{12}^k{.2^k}$, $k = \overline {1..12} .$

Ta có: ${a_{k + 1}} = C_{12}^{k + 1}{.2^{k + 1}}.$

Suy ra ${a_k} < {a_{k + 1}}$ $\Leftrightarrow C_{12}^k{.2^k} < C_{12}^{k + 1}{.2^{k + 1}}$ $\Leftrightarrow \frac{{12!}}{{k!(12 – k)!}}{.2^k} < \frac{{12!}}{{(k + 1)!(11 – k)!}}{.2^{k + 1}}.$

$\Leftrightarrow \frac{{12!}}{{k!(12 – k).(11 – k)!}}{.2^k}$ $< \frac{{12!}}{{(k + 1).k!(11 – k)!}}{.2.2^k}$ $\Leftrightarrow \frac{1}{{12 – k}} < \frac{2}{{k + 1}}$ $\Leftrightarrow k < \frac{{23}}{3}.$

Suy ra: ${a_0} < {a_1} < {a_2} < \ldots < {a_8}.$

Ngược lại: ${a_k} > {a_{k + 1}}$ $\Leftrightarrow k > \frac{{23}}{3}$ suy ra: ${a_8} > {a_9} > {a_{10}} > {a_{11}} > {a_{12}}.$

Vậy với mọi $k = \overline {1..12}$, ${a_k} \le {a_8}.$

Vậy $\max \left( {{a_1},{a_2},{a_3}, \ldots ,{a_{12}}} \right) = {a_8}$ $= C_{12}^8{.2^8} = 126720.$

## Bài 7: Tìm hệ số lớn nhất trong khai triển: ${(3 + 2x)^8}.$

Lời giải:

Ta có: ${(3 + 2x)^8}$ $= \sum\limits_{k = 0}^8 {C_8^k} {3^{8 – k}}{2^k}{x^k}.$

Hệ số tổng quát trong khai triển là: ${a_k} = C_8^k{3^{8 – k}}{2^k}.$

Xét dãy số ${a_k} = C_8^k{3^{8 – k}}{2^k}$, $k = \overline {0..8} .$

Ta có: ${a_{k + 1}} = C_8^{k + 1}{3^{7 – k}}{2^{k + 1}}.$

Xét ${a_k} – {a_{k + 1}} > 0$ $\Leftrightarrow C_8^k{3^{8 – k}}{2^k} – C_8^{k + 1}{3^{7 – k}}{2^{k + 1}} > 0.$

$\Leftrightarrow {3^{7 – k}}{2^k}\left( {3C_8^k – 2C_8^{k + 1}} \right) > 0$ $\Leftrightarrow 3.\frac{{8!}}{{k!(8 – k)!}} – 2.\frac{{8!}}{{(k + 1)!(7 – k)!}} > 0.$

$\Leftrightarrow \frac{{8!}}{{k!(7 – k)!}}\left( {\frac{3}{{8 – k}} – \frac{2}{{k + 1}}} \right) > 0$ $\Leftrightarrow \frac{{3k – 3 – 16 + 2k}}{{(8 – k)(k + 1)}} > 0$ $\Leftrightarrow k > \frac{{19}}{5}.$

Suy ra: ${a_4} > {a_5} > {a_6} > {a_7} > {a_8}.$

Ngược lại: ${a_k} – {a_{k + 1}} < 0$ $\Leftrightarrow k < \frac{{19}}{5}.$

Suy ra: ${a_4} > {a_3} > {a_2} > {a_1} > {a_0}.$

Vậy hệ số lớn nhất trong khai triển là: ${a_4} = C_8^4{3^4}{2^4} = 90720.$

## Bài 8: Tìm hệ số lớn nhất trong khai triển của ${(2 + 3x)^{2n}}$, trong đó $n$ là số nguyên dương thỏa mãn: $C_{2n + 1}^1 + C_{2n + 1}^3$ $+ C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1}$ $= 1024.$

Lời giải:

Xét khai triển: ${(1 + x)^{2n + 1}}$ $= C_{2n + 1}^0 + C_{2n + 1}^1x$ $+ C_{2n + 1}^2{x^2} + C_{2n + 1}^3{x^3}$ $+ \ldots + C_{2n + 1}^{2n + 1}{x^{2n + 1}}.$

Chọn $x= 1$, ta được: $C_{2n + 1}^0 + C_{2n + 1}^1$ $+ C_{2n + 1}^2 + C_{2n + 1}^3$ $+ \ldots + C_{2n + 1}^{2n + 1} = {2^{2n + 1}}$ $(*).$

Chọn $x = – 1$, ta được: $C_{2n + 1}^0 – C_{2n + 1}^1$ $+ C_{2n + 1}^2 – C_{2n + 1}^3$ $+ \ldots – C_{2n + 1}^{2n + 1} = 0.$

Từ $(*)$ suy ra: $2\left( {C_{2n + 1}^1 + C_{2n + 1}^3 + C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1}} \right)$ $= {2^{2n + 1}}.$

$\Leftrightarrow C_{2n + 1}^1 + C_{2n + 1}^3 + C_{2n + 1}^5 + \ldots + C_{2n + 1}^{2n + 1} = {2^{2n}}.$

Theo giả thiết ta có: ${2^{2n}} = 1024 = {2^{10}}$ $\Leftrightarrow n = 5.$

Từ đó suy ra: ${(2 + 3x)^{2n}}$ $= {(2 + 3x)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {2^{10 – k}}{(3x)^k}$ $= \sum\limits_{k = 0}^{10} {{3^k}} .C_{10}^k{2^{10 – k}}{x^k}.$

Xét dãy số ${a_k} = {3^k}.C_{10}^k{2^{10 – k}}$, $k = \overline {0..10} .$

Ta có: ${a_{k + 1}} = {3^{k + 1}}.C_{10}^{k + 1}{2^{9 – k}}.$

Ta có: ${a_k} > {a_{k + 1}}$ $\Leftrightarrow {a_k} – {a_{k + 1}} > 0$ $\Leftrightarrow {3^k}.C_{10}^k{2^{10 – k}} – {3^{k + 1}}.C_{10}^{k + 1}{2^{9 – k}} > 0.$

$\Leftrightarrow {3^k}{2^{9 – k}}\left( {2C_{10}^k – 3C_{10}^{k + 1}} \right) > 0$ $\Leftrightarrow 2.\frac{{10!}}{{k!(10 – k)!}} – 3.\frac{{10!}}{{(k + 1)!(9 – k)!}} > 0.$

$\Leftrightarrow \frac{{10!}}{{k!(9 – k)!}}\left( {\frac{2}{{10 – k}} – \frac{3}{{k + 1}}} \right) > 0$ $\Leftrightarrow \frac{{10!}}{{k!(9 – k)!}}\left( {\frac{{5k – 28}}{{(10 – k)(k + 1)}}} \right) > 0$ $\Leftrightarrow k > \frac{{28}}{5}.$

Suy ra: ${a_6} > {a_7} > \ldots > {a_{10}}.$

Ngược lại: ${a_k} < {a_{k + 1}}$ $\Leftrightarrow k < \frac{{28}}{5}.$

Suy ra: ${a_6} > {a_7} > … > {a_{10}}.$

Ngược lại: ${a_k} < {a_{k + 1}}$ $\Leftrightarrow k < \frac{{28}}{5}.$

Suy ra: ${a_6} > {a_5} > … > {a_0}.$

Vậy hệ số lớn nhất trong khai triển là: ${a_6} = {3^6}.C_{16}^6{2^4} = 2449440.$

## Bài 9: Tìm hệ số có giá trị lớn nhất của khai triển: ${(1 + x)^n}$, biết rằng tổng các hệ số bằng $4096.$

Lời giải:

Xét khai triển ${(1 + x)^n} = \sum\limits_{k = 0}^n {C_n^k} {x^k}.$

Chọn $x = 1$, ta được: $\sum\limits_{k = 0}^n {C_n^k} = {2^n}.$

Theo giả thiết ta có: ${2^n} = 4096$ $\Leftrightarrow n = 12.$

Suy ra: ${(1 + x)^n}$ $= {(1 + x)^{12}}$ $= \sum\limits_{k = 0}^{12} {C_{12}^k} {x^k}.$

Xét dãy số ${a_k} = C_{12}^k.$

Ta có: ${a_k} \ge {a_{k + 1}}$ $\Leftrightarrow C_{12}^k \ge C_{12}^{k + 1}$ $\Leftrightarrow \frac{{12!}}{{k!(12 – k)!}} \ge \frac{{12!}}{{(k + 1)!(11 – k)!}}.$

$\Leftrightarrow \frac{{12!}}{{k!(12 – k)(11 – k)!}} \ge \frac{{12!}}{{(k + 1)k!(11 – k)!}}$ $\Leftrightarrow \frac{1}{{(12 – k)}} \ge \frac{1}{{(k + 1)}}$ $\Leftrightarrow k \ge \frac{{13}}{2}.$

Suy ra: ${a_7} \ge {a_8} \ge \ldots \ge {a_{12}}.$

Ngược lại: ${a_k} \le {a_{k + 1}}$ $\Leftrightarrow k \le \frac{{13}}{2}.$

Suy ra: ${a_7} \ge {a_6} \ge \ldots \ge {a_0}.$

Vậy hệ số lớn nhất trong khai triển là: ${a_7} = C_{12}^7 = 792.$