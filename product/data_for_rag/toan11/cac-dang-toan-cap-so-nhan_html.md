# Các dạng toán cấp số nhân

<!-- chunk:0 level:0 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
Bài viết phân dạng và hướng dẫn phương pháp giải các dạng toán cấp số nhân thông qua các ví dụ minh họa có lời giải chi tiết.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Dạng toán 1. Chứng minh tính chất của một cấp số nhân.

Phương pháp: Với bài toán: Cho ba số $a, b, c$ lập thành cấp số nhân, chứng minh tính chất $K$, ta thực hiện theo các bước sau:

+ Bước 1. Từ giả thiết $a, b, c$ lập thành một cấp số nhân, ta được: $ac = {b^2}.$

+ Bước 2. Chứng minh tính chất $K.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 1. Cho ba số $a, b, c$ lập thành một cấp số nhân. Chứng minh rằng: $\left( {{a^2} + {b^2}} \right)\left( {{b^2} + {c^2}} \right)$ $= {\left( {ab + bc} \right)^2}.$

Từ giả thiết $a, b, c$ lập thành một cấp số nhân, ta được: $ac = {b^2}.$

Khi đó: $\left( {{a^2} + {b^2}} \right)\left( {{b^2} + {c^2}} \right)$ $= {a^2}{b^2} + {a^2}{c^2} + {b^4} + {b^2}{c^2}$ $= {a^2}{b^2} + ac{b^2} + ac{b^2} + {b^2}{c^2}$ $= {a^2}{b^2} + 2a{b^2}c + {b^2}{c^2}$ $= {\left( {ab + bc} \right)^2}.$

Vậy: $\left( {{a^2} + {b^2}} \right)\left( {{b^2} + {c^2}} \right)$ $= {\left( {ab + bc} \right)^2}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 2. Cho $\left( {{a_n}} \right)$ là một cấp số nhân. Chứng minh rằng: ${a_1}{a_n} = {a_k}{a_{n – k + 1}}$ với $k = 1, 2,…, n.$

Ta có:

$VT = {a_1}{a_n}$ $= {a_1}{a_1}{q^{n – 1}} = a_1^2{q^{n – 1}}.$

$VP = {a_k}{a_{n – k + 1}}$ $= {a_1}{q^{k – 1}}{a_1}{q^{n – k}} = a_1^2{q^{n – 1}}.$

Suy ra $VT = VP$, hay ${a_1}{a_n} = {a_k}{a_{n – k + 1}}$ với $k = 1, 2,…, n.$

<!-- chunk:4 level:2 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Dạng toán 2. Chứng minh bộ số lập thành một cấp số nhân.

Phương pháp: Để chứng minh ba số $a, b, c$ lập thành cấp số nhân, ta chứng minh: $ac = {b^2}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 3. Cho ba số $\frac{2}{{b – a}}$, $\frac{1}{b}$, $\frac{2}{{b – c}}$ lập thành một cấp số cộng. Chứng minh rằng ba số $a, b, c$ lập thành một cấp số nhân.

Từ giả thiết ba số $\frac{2}{{b – a}}$, $\frac{1}{b}$, $\frac{2}{{b – c}}$ lập thành một cấp số cộng, ta được: $\frac{2}{{b – a}} + \frac{2}{{b – c}} = \frac{2}{b}$ $\Leftrightarrow b(b – c + b – a)$ $= (b – a)(b – c)$ $\Leftrightarrow {b^2} = ac.$

Vậy: ba số $a, b, c$ lập thành một cấp số nhân.

<!-- chunk:6 level:2 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Dạng toán 3. Tìm điều kiện của tham số để bộ số lập thành một cấp số nhân.

Phương pháp:

+ Để ba số $a, b, c$ lập thành cấp số nhân, điều kiện là: $ac = {b^2}$, bài toán được chuyển về việc giải phương trình.

+ Để bốn số $a, b, c, d$ lập thành cấp số nhân, điều kiện là: 
$$
\left\{ \begin{array}{l}
ac = {b^2}\\
bd = {c^2}
\end{array} \right.
$$
, bài toán được chuyển về việc giải hệ phương trình.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 4. Tìm $x$ để ba số $x – 2$, $x – 4$, $x + 2$ lập thành một cấp số nhân.

Để ba số $x – 2$, $x – 4$, $x + 2$ lập thành một cấp số nhân, điều kiện là: ${(x – 4)^2} = (x – 2)\left( {x + 2} \right)$ $\Leftrightarrow 8x = 20$ $\Leftrightarrow x = \frac{5}{2}.$

Vậy: $x = \frac{5}{2}$ thoả mãn yêu cầu bài toán.

Bài toán: Tìm điều kiện của tham số sao cho phương trình bậc ba: $a{x^3} + b{x^2} + cx + d = 0$ $(*)$, (với $a \ne 0$) có $3$ nghiệm ${x_1},{\rm{ }}{x_2},{\rm{ }}{x_3}$ lập thành cấp số nhân.

Điều kiện cần: Giả sử phương trình có ba nghiệm phân biệt lập thành cấp số nhân, khi đó: ${x_1}{x_3} = x_2^2.$

Áp dụng định lý Viet đối với phương trình bậc ba, ta có:

${x_1} + {x_2} + {x_3} = – \frac{b}{a}.$

${x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1} = \frac{c}{a}$ $\Leftrightarrow {x_1}{x_2} + {x_2}{x_3} + x_2^2 = \frac{c}{a}$ $\Leftrightarrow {x_2}\left( {{x_1} + {x_2} + {x_3}} \right) = \frac{c}{a}$ $\Leftrightarrow {x_2} = – \frac{c}{b}.$

Với ${x_2} = – \frac{c}{b}$ thay vào $(*)$ ta được:

$a{\left( { – \frac{c}{b}} \right)^3} + b{\left( { – \frac{c}{b}} \right)^2}$ $+ c\left( { – \frac{c}{b}} \right) + d = 0$ $\Leftrightarrow a{c^3} = {b^3}d.$

Đây chính là điều kiện cần để phương trình $(*)$ có $3$ nghiệm lập thành cấp số nhân.

Điều kiện đủ: Từ $a{c^3} = {b^3}d$ suy ra phương trình $(*)$ có nghiệm ${x_2} = – \frac{c}{b}.$ Khi đó:

${x_2}\left( {{x_1} + {x_2} + {x_3}} \right)$ $= \left( { – \frac{c}{b}} \right)\left( { – \frac{b}{a}} \right)$ $= \frac{c}{a}$ $= {x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1}$ $\Leftrightarrow {x_1}{x_3} = x_2^2$ $\Leftrightarrow {x_1},{\rm{ }}{x_2},{\rm{ }}{x_3}$ lập thành cấp số nhân.

Vậy, điều kiện cần và đủ để $(*)$ có $3$ nghiệm lập thành cấp số nhân là: $a{c^3} = {b^3}d.$

Với bài toán chỉ chứa một tham số, trong điều kiện đủ ta có thể khẳng định bằng việc chỉ ra nghiệm cụ thể của phương trình. Hãy nhớ điều này rất quan trọng bởi khi đó ta còn phải khẳng định phương trình đã cho có $3$ nghiệm phân biệt.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 5. Xác định $m$ để phương trình: ${x^3} + 2{x^2} + \left( {m + 1} \right)x$ $+ 2\left( {m + 1} \right) = 0$ $(1)$ có ba nghiệm phân biệt lập thành cấp số nhân.

Điều kiện cần: Giả sử phương trình $(1)$ có ba nghiệm phân biệt lập thành cấp số nhân, khi đó: ${x_1}{x_3} = x_2^2.$

Ta có:

${x_1} + {x_2} + {x_3} = – 2.$

${x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1} = m + 1$ $\Leftrightarrow {x_1}{x_2} + {x_2}{x_3} + x_2^2 = m + 1$ $\Leftrightarrow {x_2}\left( {{x_1} + {x_2} + {x_3}} \right) = m + 1$ $\Leftrightarrow {x_2} = – \frac{{m + 1}}{2}.$

Với ${x_2} = – \frac{{m + 1}}{2}$ thay vào $(1)$ ta được:

${\left( { – \frac{{m + 1}}{2}} \right)^3} + 2{\left( { – \frac{{m + 1}}{2}} \right)^2}$ $+ \left( {m + 1} \right)\left( { – \frac{{m + 1}}{2}} \right)$ $+ 2\left( {m + 1} \right) = 0$ $\Leftrightarrow \left( {m + 1} \right)({m^2} + 2m – 15) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
m = – 1\\
m = 3\\
m = – 4
\end{array} \right.
$$

Đó chính là điều kiện cần để $(1)$ có $3$ nghiệm lập thành cấp số nhân.

Điều kiện đủ:

+ Với $m = -1$, ta được: $(1)$ $\Leftrightarrow {x^3} + 2{x^2} = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 0\\
x = – 2
\end{array} \right.
$$
 không thoả mãn.

+ Với $m = 3$, ta được: $(1)$ $\Leftrightarrow {x^3} + 2{x^2} + 4x + 8 = 0$ $\Leftrightarrow x = – 2$ không thoả mãn.

+ Với $m = -5$, ta được: $(1)$ $\Leftrightarrow {x^3} + 2{x^2} – 4x – 8 = 0$ $\Leftrightarrow x = 0$ không thoả mãn.

Vậy: không tồn tại giá trị $m$ thoả mãn yêu câu bài toán.

<!-- chunk:9 level:2 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Dạng toán 4. Tìm các phần tử của một cấp số nhân $\left( {{u_n}} \right).$

Phương pháp: Thông thường bài toán được chuyển về xác định ${u_1}$ và công bội $q.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 6. Tìm số hạng đầu ${u_1}$ và công bội $q$ của các cấp số nhân $\left( {{u_n}} \right)$ biết:
$$
\left\{ \begin{array}{l}
{u_4} – {u_2} = 72\\
{u_5} – {u_3} = 144
\end{array} \right.
$$

Ta biến đổi: 
$$
\left\{ \begin{array}{l}
{u_1}{q^3} – {u_1}q = 72\\
{u_1}{q^4} – {u_1}{q^2} = 144
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{u_1}q({q^2} – 1) = 72\\
{u_1}{q^2}({q^2} – 1) = 144
\end{array} \right.
$$
 $\Rightarrow q = \frac{{144}}{{72}} = 2$ $\Rightarrow {u_1} = 12.$

Vậy: cấp số nhân $\left( {{u_n}} \right)$ có ${u_1} = 12$ và $q = 2.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 7. Cho cấp số nhân $\left( {{u_n}} \right)$ thoả mãn ${u_4} – {u_2} = 72$ và ${u_5} – {u_3} = 144.$

a. Tìm số hạng đầu tiên và công bội của cấp số nhân $\left( {{u_n}} \right).$

b. Tính tổng số của $10$ số hạng đầu tiên của cấp số nhân $\left( {{u_n}} \right).$

c. Tính tổng $S’ = {u_3} + {u_6} + \ldots + {u_{12}}.$

a. Gọi $q$ là công bội của cấp số nhân $\left( {{u_n}} \right)$, ta có:

$$
\left\{ \begin{array}{l}
{u_4} – {u_2} = 72\\
{u_5} – {u_3} = 144
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{u_1}{q^3} – {u_1}q = 72\\
{u_1}{q^4} – {u_1}{q^2} = 144
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{u_1}({q^3} – q) = 72\\
{u_1}({q^4} – {q^2}) = 144
\end{array} \right.
$$

$\Rightarrow \frac{{{q^3} – q}}{{{q^4} – {q^2}}} = \frac{1}{2}$ $\Leftrightarrow q = 2$ $\Rightarrow {u_1} = 12.$

Vậy: cấp số nhân $\left( {{u_n}} \right)$ có ${u_1} = 12$ và $q = 2.$

b. Ta có: ${S_{20}} = {u_1} + {u_2} + \ldots + {u_{10}}$ $= {u_1}\frac{{{q^{10}} – 1}}{{q – 1}}$ $= 12\frac{{{2^{10}} – 1}}{{2 – 1}}$ $= 12276.$

c. Ta có: $S’ = {u_3} + {u_6} + \ldots + {u_{12}}$ $= {u_3}\frac{{{q^{10}} – 1}}{{q – 1}}$ $= {12.2^2}\frac{{{2^{10}} – 1}}{{2 – 1}}$ $= 49104.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 8. Cho ba số $a, b, c$ lập thành một cấp số nhân. Chứng minh rằng: $\left( {a + b + c} \right)(a – b + c)$ $= {a^2} + {b^2} + {c^2}.$

Áp dụng: Tìm ba số liên tiếp của một cấp số nhân biết tổng của chúng bằng $21$ và tổng bình phương của chúng bằng $189.$

Từ giả thiết ba số $a, b, c$ lập thành một cấp số nhân, ta được: $ac = {b^2}.$

Khi đó: $\left( {a + b + c} \right)\left( {a – b + c} \right)$ $= {\left( {a + c} \right)^2} – {b^2}$ $= {a^2} + 2ac + {c^2} – {b^2}$ $= {a^2} + 2{b^2} + {c^2} – {b^2}$ $= {a^2} + {b^2} + {c^2}.$

Áp dụng: Với ba số $a, b, c$ lập thành một cấp số nhân, biết rằng $a + b + c = 21$ và ${a^2} + {b^2} + {c^2} = 189$, suy ra:

$a – b + c = \frac{{189}}{{21}} = 9$ 
$$
\Rightarrow \left\{ \begin{array}{l}
b = 6\\
a + c = 15
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
b = 6\\
a + c = 15\\
{a^2} + {c^2} = 153
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = 3\\
b = 6\\
c = 12
\end{array} \right.
$$

Vậy, ba số cần tìm là $3, 6, 12.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 9. Biết rằng ba số $x, y, z$ lập thành một cấp số nhân và ba số $x, 2y, 3z$ lập thành một cấp số cộng. Tìm công bội của cấp số nhân.

Gọi $q$ là công bội của cấp số nhân.

Các số $x, 2y, 3z$ lập thành một cấp số cộng, suy ra: $x + 3z = 4y$ $\Leftrightarrow x + 3x{q^2} = 4xq$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 0 \left( {loại} \right)\\
3{q^2} – 4q + 1 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
q = 1\\
q = \frac{1}{3}
\end{array} \right.
$$

Vậy: cấp số nhân có công bội $q = 1$ hoặc $q = \frac{1}{3}.$

<!-- chunk:14 level:2 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Dạng toán 5. Tính tổng cấp số nhân.

Phương pháp: Nếu $\left( {{u_n}} \right)$ là một cấp số nhân với công bội $q \ne 1$ thì tổng $n$ số hạng đầu tiên của cấp số nhân $\left( {{u_n}} \right)$ được tính theo công thức: ${S_n} = \frac{{{u_1}(1 – {q^n})}}{{1 – q}}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 10. Tính các tổng sau:

a. $S = 2 + 6 + 18 + \ldots + 13122.$

b. $S = 1 + 2.2 + {3.2^2} + \ldots + {100.2^{99}}.$

a. Xét cấp số nhân $\left( {{u_n}} \right)$ có ${u_1} = 2$ và công bội $q = 3$, ta có:

$13122 = {u_n}$ $= {u_1}{q^{n – 1}} = {2.3^{n – 1}}$ $\Leftrightarrow n = 9.$

Suy ra: $S = {S_9} = {u_1}\frac{{{q^9} – 1}}{{q – 1}}$ $= 2\frac{{{3^9} – 1}}{{3 – 1}} = 19682.$

b. Ta có:

$S = \left( {2 – 1} \right)S = 2S – S$

$= 1.2 + {2.2^2} + {3.2^3} + … + {100.2^{100}}$ $– 1 – 2.2 – {3.2^2} – … – {100.2^{99}}$

$= {100.2^{100}} – 1$ $+ \left( {1.2 – 2.2} \right) + \left( {{{2.2}^2} – {{3.2}^2}} \right)$ $+ … + \left( {{{99.2}^{99}} – {{100.2}^{99}}} \right)$

$= {100.2^{100}} – 1 – 2 – {2^2} – … – {2^{99}}$ $= {100.2^{100}} – \left( {1 + 2 + {2^2} + … + {2^{99}}} \right)$

Xét cấp số nhân $\left( {{u_n}} \right)$ có ${u_1} = 1$, công bội $q = 2.$

Ta có: $1 + 2 + {2^2} + … + {2^{99}}$ $= \frac{{1\left( {1 – {2^{100}}} \right)}}{{1 – 2}}$ $= {2^{100}} – 1.$

Suy ra: $S = {100.2^{100}} – \left( {{2^{100}} – 1} \right)$ $= {99.2^{100}} + 1.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/07/cac-dang-toan-cap-so-nhan.html -->
## Ví dụ 11. Tính tổng $S = 1 + 11 + 111$ $+ \ldots + \underbrace {11…1}_{n chữ số}.$

Xét hai dãy số:

+ Cấp số nhân $\left( {{u_n}} \right)$ có ${u_1} = 1$ và công bội $q = 10.$

+ Dãy số $\left( {{s_n}} \right) = \left\{ {1,11,111, \ldots ,\underbrace {11…1}_{n chữ số}} \right\}.$

Suy ra ${s_n}$ là tổng $n$ số hạng đầu của cấp số nhân $\left( {{u_n}} \right)$, tức là: ${s_n} = \frac{{{{10}^n} – 1}}{{10 – 1}}$ $= \frac{1}{9}\left( {{{10}^n} – 1} \right).$

Khi đó, ta nhận được: $S = {s_1} + {s_2} + \ldots + {s_n}$ $= \sum\limits_{k = 1}^n {{s_k}} = \sum\limits_{k = 1}^n {\frac{1}{9}\left( {{{10}^k} – 1} \right)}$ $= \frac{1}{9}\sum\limits_{k = 1}^n {{{10}^k} – \frac{n}{9}}$ $= \frac{1}{9}.10.\frac{{{{10}^n} – 1}}{{10 – 1}} – \frac{n}{9}$ $= \frac{1}{{81}}\left( {{{10}^{n + 1}} – 10 – 9n} \right).$

* *