# Xác định cấp số và các yếu tố của cấp số

<!-- chunk:0 level:0 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán xác định cấp số và các yếu tố của cấp số, giúp học sinh học tốt chương trình Đại số và Giải tích 11 chương 3: Dãy số, cấp số cộng và cấp số nhân (CSC và CSN).

<!-- chunk:1 level:1 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## I. PHƯƠNG PHÁP

+ Dãy số $\left( {{u_n}} \right)$ là một cấp số cộng $\Leftrightarrow {u_{n + 1}} – {u_n} = d$ không phụ thuộc vào $n$ và $d$ là công sai.

+ Dãy số $\left( {{u_n}} \right)$ là một cấp số nhân $\Leftrightarrow \frac{{{u_{n + 1}}}}{{{u_n}}} = q$ không phụ thuộc vào $n$ và $q$ là công bội.

+ Ba số $a$, $b$, $c$ theo thứ tự đó lập thành cấp số cộng $\Leftrightarrow a + c = 2b.$

+ Ba số $a$, $b$, $c$ theo thứ tự đó lập thành cấp số nhân $\Leftrightarrow ac = {b^2}.$

+ Để xác định một cấp số cộng, ta cần xác định số hạng đầu và công sai. Do đó, ta thường biểu diễn giả thiết của bài toán qua ${u_1}$ và $d.$

+ Để xác định một cấp số nhân, ta cần xác định số hạng đầu và công bội. Do đó, ta thường biểu diễn giả thiết của bài toán qua ${u_1}$ và $q.$

<!-- chunk:2 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 1. Tìm bốn số hạng liên tiếp của một cấp số cộng biết tổng của chúng bằng $20$ và tổng các bình phương của chúng bằng $120.$

Lời giải:

Giả sử bốn số hạng đó là $a – 3x$; $a – x$; $a + x$; $a + 3x$ với công sai là $d = 2x.$

Khi đó, ta có:

$$
\left\{ {\begin{array}{l}
{(a – 3x) + (a – x) + (a + x) + (a + 3x) = 20}\\
{{{(a – 3x)}^2} + {{(a – x)}^2} + {{(a + x)}^2} + {{(a + 3x)}^2} = 120}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{c}
{4a = 20}\\
{4{a^2} + 20{x^2} = 120}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 5}\\
{x = \pm 1}
\end{array}} \right..
$$

Vậy bốn số cần tìm là $2$; $4$; $6$; $8.$

Chú ý:

+ Cách gọi các số hạng của cấp số cộng như trên giúp ta giải quyết bài toán gọn hơn.

+ Nếu số hạng cấp số cộng là lẻ thì gọi công sai $d = x$, là chẵn thì gọi công sai $d = 2x$ rồi viết các số hạng cấp số dưới dạng đối xứng.

+ Nếu cấp số cộng $\left( {{a_n}} \right)$ thỏa mãn: 
$$
\left\{ {\begin{array}{l}
{{a_1} + {a_2} + \ldots + {a_n} = p}\\
{a_1^2 + a_2^2 + \ldots + a_n^2 = {s^2}}
\end{array}} \right.
$$
 thì:

${a_1} = \frac{1}{n}\left[ {p – \frac{{n(n – 1)}}{2}d} \right]$ và $d = \pm \sqrt {\frac{{12\left( {n{s^2} – {p^2}} \right)}}{{{n^2}\left( {{n^2} – 1} \right)}}} .$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 2. Cho CSC $\left( {{u_n}} \right)$ thỏa mãn:
$$
\left\{ {\begin{array}{c}
{{u_2} – {u_3} + {u_5} = 10}\\
{{u_4} + {u_6} = 26}
\end{array}} \right..
$$

1. Xác định công sai và công thức tổng quát của cấp số.

2. Tính $S = {u_1} + {u_4} + {u_7} + \ldots + {u_{2011}}.$

Lời giải:

Gọi $d$ là công sai của cấp số cộng, ta có:

$$
\left\{ {\begin{array}{l}
{\left( {{u_1} + d} \right) – \left( {{u_1} + 2d} \right) + \left( {{u_1} + 4d} \right) = 10}\\
{\left( {{u_1} + 3d} \right) + \left( {{u_1} + 5d} \right) = 26}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} + 3d = 10}\\
{{u_1} + 4d = 13}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} = 1}\\
{d = 3}
\end{array}} \right..
$$

1. Ta có công sai $d = 3$ và số hạng tổng quát: ${u_n} = {u_1} + (n – 1)d = 3n – 2.$

2. Ta có các số hạng ${u_1}$, ${u_4}$, ${u_7}$, …, ${u_{2011}}$ lập thành một cấp số cộng gồm $670$ số hạng với công sai $d’ = 3d$ nên ta có: $S = \frac{{670}}{2}\left( {2{u_1} + 669d’} \right)$ $= 673015.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 3. Cho cấp số cộng $\left( {{u_n}} \right)$ thỏa mãn:
$$
\left\{ {\begin{array}{l}
{{u_5} + 3{u_3} – {u_2} = – 21}\\
{3{u_7} – 2{u_4} = – 34}
\end{array}} \right..
$$

1. Tính số hạng thứ $100$ của cấp số.

2. Tính tổng $15$ số hạng đầu của cấp số.

3. Tính $S = {u_4} + {u_5} + \ldots + {u_{30}}.$

Lời giải:

Từ giả thiết bài toán, ta có: 
$$
\left\{ {\begin{array}{l}
{{u_1} + 4d + 3\left( {{u_1} + 2d} \right) – \left( {{u_1} + d} \right) = – 21}\\
{3\left( {{u_1} + 6d} \right) – 2\left( {{u_1} + 3d} \right) = – 34}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} + 3d = – 7}\\
{{u_1} + 12d = – 34}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} = 2}\\
{d = – 3}
\end{array}} \right..
$$

1. Số hạng thứ $100$ của cấp số: ${u_{100}} = {u_1} + 99d = – 295.$

2. Tổng của $15$ số hạng đầu: ${S_{15}} = \frac{{15}}{2}\left[ {2{u_1} + 14d} \right] = – 285.$

3. Ta có: $S = {u_4} + {u_5} + \ldots + {u_{30}}$ $= \frac{{27}}{2}\left[ {2{u_4} + 26d} \right]$ $= 27\left( {{u_1} + 16d} \right) = – 1242.$

Chú ý: Ta có thể tính $S$ theo cách sau:

$S = {S_{30}} – {S_3}$ $= 15\left( {2{u_1} + 29d} \right) – \frac{3}{2}\left( {2{u_1} + 2d} \right)$ $= – 1242.$

<!-- chunk:5 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 4. Cho cấp số cộng $\left( {{u_n}} \right)$ thỏa mãn:
$$
\left\{ {\begin{array}{c}
{{u_2} – {u_3} + {u_5} = 10}\\
{{u_4} + {u_6} = 26}
\end{array}} \right..
$$

1. Xác định cấp số cộng.

2. Tính tổng $S = {u_5} + {u_7} + \ldots + {u_{2011}}.$

Lời giải:

1. Ta có: 
$$
\left\{ {\begin{array}{l}
{{u_1} + d – \left( {{u_1} + 2d} \right) + {u_1} + 4d = 10}\\
{{u_1} + 3d + {u_1} + 5d = 26}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} + 3d = 10}\\
{{u_1} + 4d = 13}
\end{array}} \right..
$$

$\Leftrightarrow {u_1} = 1$, $d = 3$; ${u_5} = {u_1} + 4d = 1 + 12 = 13.$

2. Ta có ${u_5}$, ${u_7}$, …, ${u_{2011}}$ lập thành CSC với công sai $d = 6$ và có $1003$ số hạng nên $S = \frac{{1003}}{2}\left( {2{u_5} + 1002.6} \right)$ $= 3028057.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 5. Cho một cấp số cộng $\left( {{u_n}} \right)$ có ${u_1} = 1$ và tổng $100$ số hạng đầu bằng $24850.$ Tính $S = \frac{1}{{{u_1}{u_2}}} + \frac{1}{{{u_2}{u_3}}} + \ldots + \frac{1}{{{u_{49}}{u_{50}}}}.$

Lời giải:

Gọi $d$ là công sai của cấp số đã cho.

Ta có: ${S_{100}} = 50\left( {2{u_1} + 99d} \right) = 24850$ $\Rightarrow d = \frac{{497 – 2{u_1}}}{{99}} = 5.$

$\Rightarrow 5S = \frac{5}{{{u_1}{u_2}}} + \frac{5}{{{u_2}{u_3}}} + \ldots + \frac{5}{{{u_{49}}{u_{50}}}}$ $= \frac{{{u_2} – {u_1}}}{{{u_1}{u_2}}} + \frac{{{u_3} – {u_2}}}{{{u_2}{u_3}}} + \ldots + \frac{{{u_{50}} – {u_{49}}}}{{{u_{49}}{u_{50}}}}.$

$= \frac{1}{{{u_1}}} – \frac{1}{{{u_2}}}$ $+ \frac{1}{{{u_2}}} – \frac{1}{{{u_3}}}$ $+ \ldots + \frac{1}{{{u_{48}}}} – \frac{1}{{{u_{49}}}}$ $+ \frac{1}{{{u_{49}}}} – \frac{1}{{{u_{50}}}}.$

$= \frac{1}{{{u_1}}} – \frac{1}{{{u_{50}}}}$ $= \frac{1}{{{u_1}}} – \frac{1}{{{u_1} + 49d}} = \frac{{245}}{{246}}$ $\Rightarrow S = \frac{{49}}{{246}}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 6. Cho cấp số nhân $\left( {{u_n}} \right)$ có các số hạng khác không, tìm ${u_1}$ biết:

$$
\left\{ {\begin{array}{l}
{{u_1} + {u_2} + {u_3} + {u_4} = 15}\\
{u_1^2 + u_2^2 + u_3^2 + u_4^2 = 85}
\end{array}} \right..
$$

Lời giải:

Ta có: 
$$
\left\{ {\begin{array}{l}
{{u_1}\left( {1 + q + {q^2} + {q^3}} \right) = 15}\\
{u_1^2\left( {1 + {q^2} + {q^4} + {q^6}} \right) = 85}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1}\frac{{{q^4} – 1}}{{q – 1}} = 15}\\
{u_1^2\frac{{{q^8} – 1}}{{{q^2} – 1}} = 85}
\end{array}} \right..
$$

$\Rightarrow {\left( {\frac{{{q^4} – 1}}{{q – 1}}} \right)^2}\left( {\frac{{{q^2} – 1}}{{{q^8} – 1}}} \right) = \frac{{45}}{{17}}$ $\Leftrightarrow \frac{{\left( {{q^4} – 1} \right)(q + 1)}}{{(q – 1)\left( {{q^4} + 1} \right)}} = \frac{{45}}{{17}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{q = 2}\\
{q = \frac{1}{2}}
\end{array}} \right..
$$

Từ đó ta tìm được ${u_1} = 1$ hoặc ${u_1} = 8.$

<!-- chunk:8 level:3 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## Ví dụ 7. Cho cấp số nhân $\left( {{u_n}} \right)$ thỏa mãn:
$$
\left\{ {\begin{array}{l}
{{u_4} = \frac{2}{{27}}}\\
{{u_3} = 243{u_8}}
\end{array}} \right..
$$

1. Viết năm số hạng đầu của cấp số.

2. Tính tổng $10$ số hạng đầu của cấp số.

3. Số $\frac{2}{{6561}}$ là số hạng thứ bao nhiêu của cấp số?

Lời giải:

Gọi $q$ là công bội của cấp số. Theo giả thiết ta có:

$$
\left\{ {\begin{array}{l}
{{u_1}{q^3} = \frac{2}{{27}}}\\
{{u_1}{q^2} = 243{u_1}{q^7}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1}{q^3} = \frac{2}{{27}}}\\
{{q^5} = \frac{1}{{243}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{q = \frac{1}{3}}\\
{{u_1} = 2}
\end{array}} \right..
$$

1. Năm số hạng đầu của cấp số là: ${u_1} = 2$, ${u_2} = \frac{2}{3}$, ${u_3} = \frac{2}{9}$, ${u_4} = \frac{2}{{27}}$, ${u_5} = \frac{2}{{81}}.$

2. Tổng $10$ số hạng đầu của cấp số:

${S_{10}} = {u_1}\frac{{{q^{10}} – 1}}{{q – 1}}$ $= 2.\frac{{{{\left( {\frac{1}{3}} \right)}^{10}} – 1}}{{\frac{1}{3} – 1}}$ $= 3\left[ {1 – {{\left( {\frac{1}{3}} \right)}^{10}}} \right]$ $= \frac{{59048}}{{19683}}.$

3. Ta có: ${u_n} = \frac{2}{{{3^{n – 1}}}}$ $\Rightarrow {u_n} = \frac{2}{{6561}}$ $\Leftrightarrow {3^{n – 1}} = 6561$ $= {3^8}$ $\Rightarrow n = 9.$

Vậy $\frac{2}{{6561}}$ là số hạng thứ $9$ của cấp số.

<!-- chunk:9 level:1 source:https://toanmath.com/2020/04/xac-dinh-cap-so-va-cac-yeu-to-cua-cap-so.html -->
## II. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Dãy số $\left( {{u_n}} \right)$ có phải là cấp số cộng không? Nếu phải hãy xác định số công sai? Biết:

## Bài tập 1. ${u_n} = 2n + 3.$

## Bài tập 2. ${u_n} = \frac{2}{n}.$

Lời giải:

1. Ta có: ${u_{n + 1}} – {u_n}$ $= 2(n + 1) + 3 – (2n + 3) = 2$ là hằng số.

Suy ra dãy $\left( {{u_n}} \right)$ là cấp số cộng với công sai $d = 2.$

2. Ta có: ${u_{n + 1}} – {u_n}$ $= \frac{2}{{n + 1}} – \frac{2}{n}$ $= \frac{{ – 2}}{{n(n + 1)}}$ phụ thuộc vào $n.$

Vậy dãy $\left( {{u_n}} \right)$ không phải là cấp số cộng.

## Bài 2. Dãy số $\left( {{u_n}} \right)$ có phải là cấp số nhân không? Nếu phải hãy xác định số công bội? Biết:

## Bài tập 1. ${u_n} = 2n.$

## Bài tập 2. ${u_n} = {4.3^n}.$

## Bài tập 3. ${u_n} = \frac{2}{n}.$

Lời giải:

1. Ta có: $\frac{{{u_{n + 1}}}}{{{u_n}}} = \frac{{n + 1}}{n}$ phụ thuộc vào $n$ suy ra dãy $\left( {{u_n}} \right)$ không phải là cấp số nhân.

2. Ta có: $\frac{{{u_{n + 1}}}}{{{u_n}}} = \frac{{{{4.3}^{n + 1}}}}{{{{4.3}^n}}} = 3$ không phụ thuộc vào $n$ suy ra dãy $\left( {{u_n}} \right)$ là một cấp số nhân với công bội $q = 3.$

3. Ta có: $\frac{{{u_{n + 1}}}}{{{u_n}}} = \frac{2}{{n + 1}}:\frac{2}{n} = \frac{n}{{n + 1}}$ phụ thuộc vào $n.$

Suy ra dãy $\left( {{u_n}} \right)$ không phải là cấp số nhân.

## Bài 3. Xét xem các dãy số sau có phải là cấp số cộng hay không? Nếu phải hãy xác định công sai.

## Bài tập 1. ${u_n} = 4 – 5n.$

## Bài tập 2. ${u_n} = \frac{{2n + 3}}{5}.$

## Bài tập 3. ${u_n} = \frac{{n + 1}}{n}.$

Lời giải:

1. Ta có: ${u_{n + 1}} – {u_n} = – 5.$

Dãy $\left( {{u_n}} \right)$ là cấp số cộng có công sai $d = -5.$

2. Ta có: ${u_{n + 1}} – {u_n} = \frac{2}{5}.$ Dãy $\left( {{u_n}} \right)$ là cấp số cộng có công sai $d = \frac{2}{5}.$

3. Ta có: ${u_{n + 1}} – {u_n} = – \frac{1}{{n(n + 1)}}$ $\Rightarrow \left( {{u_n}} \right)$ không là cấp số cộng.

## Bài 4. Tam giác $ABC$ có ba góc $A$, $B$, $C$ theo thứ tự đó lập thành cấp số cộng và $C = 5A.$ Xác định số đo các góc $A$, $B$, $C.$

Lời giải:

Từ giả thiết bài toán ta có hệ phương trình:

$$
\left\{ {\begin{array}{l}
{A + B + C = {{180}^0}}\\
{A + C = 2B}\\
{C = 5A}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{C = 5A}\\
{B = 3A}\\
{9A = {{180}^0}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{A = {{20}^0}}\\
{B = {{60}^0}}\\
{C = {{100}^0}}
\end{array}} \right..
$$

## Bài 5. Cho dãy số $\left( {{u_n}} \right)$ với ${u_n} = {3^{\frac{n}{2} + 1}}.$

## Bài tập 1. Chứng minh dãy số $\left( {{u_n}} \right)$ là cấp số nhân.

## Bài tập 2. Tính tổng $S = {u_2} + {u_4} + {u_6} + \ldots + {u_{20}}.$

## Bài tập 3. Số $19683$ là số hạng thứ mấy của dãy số.

Lời giải:

1. Ta có: $\frac{{{u_{n + 1}}}}{{{u_n}}} = \frac{{{3^{\frac{{n + 1}}{2} + 1}}}}{{{3^{\frac{n}{2} + 1}}}} = \sqrt 3$, $\forall n \in {N^*}$ $\Rightarrow$ Dãy số là cấp số nhân với ${u_1} = 3\sqrt 3$; $q = \sqrt 3 .$

2. Ta có ${u_2}$, ${u_4}$, ${u_6}$, …, ${u_{20}}$ lập thành cấp số nhân số hạng đầu ${u_2} = 9$; $q = 3$ và có $10$ số hạng nên: $S = {u_2}.\frac{{1 – {3^{10}}}}{{1 – 3}}$ $= 9.\frac{{{3^{10}} – 1}}{2}$ $= \frac{9}{2}\left( {{3^{10}} – 1} \right).$

3. Ta có: ${u_n} = 19683$ $\Leftrightarrow {3^{\frac{n}{2} + 1}} = {3^9}$ $\Leftrightarrow \frac{n}{2} + 1 = 9$ $\Leftrightarrow n = 16.$

Vậy số $19683$ là số hạng thứ $16$ của cấp số.

## Bài 6.

## Bài tập 1. Cho cấp số nhân có $7$ số hạng, số hạng thứ tư bằng $6$ và số hạng thứ bảy gấp $243$ lần số hạng thứ hai. Hãy tìm số hạng còn lại của CSN đó.

## Bài tập 2. Tìm ba số hạng liên tiếp của một cấp số cộng biết tổng của chúng bằng $– 9$ và tổng các bình phương của chúng bằng $29.$

Lời giải:

## Bài tập 1. Gọi CSN đó là $\left( {{u_n}} \right)$, $n = \overline {1,7} .$ Theo đề bài ta có:

$$
\left\{ {\begin{array}{c}
{{u_4} = 6}\\
{{u_7} = 243{u_2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{{u_1}{q^3} = 6}\\
{{u_1}{q^6} = 243{u_1}q}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} = \frac{2}{9}}\\
{q = 3}
\end{array}} \right..
$$

Do đó các số hạng còn lại của cấp số nhân là:

${u_1} = \frac{2}{9}$; ${u_2} = \frac{2}{3}$; ${u_3} = 2$; ${u_5} = 18$; ${u_6} = 54$; ${u_7} = 162.$

## Bài tập 2. Gọi ba số hạng của CSC là $a – 2x$; $a$; $a + 2x$ với $d = 2x.$

Ta có: 
$$
\left\{ {\begin{array}{l}
{a – 2x + a + a + 2x = – 9}\\
{{{(a – 2x)}^2} + {a^2} + {{(a + 2x)}^2} = 29}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = – 3}\\
{x = \pm \frac{1}{2}}
\end{array}} \right..
$$

## Bài 7.

## Bài tập 1. Cho cấp số cộng $\left( {{u_n}} \right)$ thỏa mãn
$$
\left\{ {\begin{array}{l}
{{u_7} – {u_3} = 8}\\
{{u_2}{u_7} = 75}
\end{array}} \right..
$$
 Tìm ${u_1}$, $d$?

## Bài tập 2. Cho cấp số cộng $\left( {{u_n}} \right)$ có công sai $d > 0$;
$$
\left\{ {\begin{array}{l}
{{u_{31}} + {u_{34}} = 11}\\
{u_{31}^2 + u_{34}^2 = 101}
\end{array}} \right..
$$
 Hãy tìm số hạng tổng quát của cấp số cộng đó.

## Bài tập 3. Gọi ${S_1}$; ${S_2}$; ${S_3}$ là tổng ${n_1}$; ${n_2}$; ${n_3}$ số hạng đầu của một cấp số cộng. Chứng minh rằng $\frac{{{S_1}}}{{{n_1}}}\left( {{n_2} – {n_3}} \right)$ $+ \frac{{{S_2}}}{{{n_2}}}\left( {{n_3} – {n_1}} \right)$ $+ \frac{{{S_3}}}{{{n_3}}}\left( {{n_1} – {n_2}} \right) = 0.$

Lời giải:

1. Ta có: 
$$
\left\{ {\begin{array}{l}
{{u_1} + 6d – {u_1} – 2d = 8}\\
{\left( {{u_1} + d} \right)\left( {{u_1} + 6d} \right) = 75}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{d = 2}\\
{{u_1} = 3,{u_1} = – 17}
\end{array}} \right..
$$

2. Ta có: 
$$
\left\{ {\begin{array}{l}
{2{u_1} + 63d = 11}\\
{{{\left( {{u_1} + 30d} \right)}^2} + {{\left( {{u_1} + 33d} \right)}^2} = 101}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1} = – 89}\\
{d = 3}
\end{array}} \right..
$$

Vậy ${u_n} = 3(n – 1) – 89$ $= 3n – 92.$

## Bài tập 3. Thay công thức ${S_1} = \frac{{{n_1}}}{2}\left( {2{u_1} + \left( {{n_1} – 1} \right)d} \right)$; ${S_2} = \frac{{{n_2}}}{2}\left( {2{u_2} + \left( {{n_2} – 1} \right)d} \right)$; ${S_3} = \frac{{{n_3}}}{2}\left( {2{u_3} + \left( {{n_3} – 1} \right)d} \right).$

Ta có điều phải chứng minh.

## Bài 8. Cho cấp số nhân $\left( {{u_n}} \right)$ thỏa mãn:
$$
\left\{ {\begin{array}{l}
{{u_1} + {u_2} + {u_3} + {u_4} + {u_5} = 11}\\
{{u_1} + {u_5} = \frac{{82}}{{11}}}
\end{array}} \right..
$$

## Bài tập 1. Tìm công bội và số hạng tổng quát của cấp số.

## Bài tập 2. Tính tổng ${S_{2011}}.$

## Bài tập 3. Trên khoảng $\left( {\frac{1}{2};1} \right)$ có bao nhiêu số hạng của cấp số.

Lời giải:

## Bài tập 1. Gọi $q$ là công bội của cấp số. Khi đó ta có:

$$
\left\{ {\begin{array}{l}
{{u_2} + {u_3} + {u_4} = \frac{{39}}{{11}}}\\
{{u_1} + {u_5} = \frac{{82}}{{11}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{u_1}\left( {q + {q^2} + {q^3}} \right) = \frac{{39}}{{11}}}\\
{{u_1}\left( {1 + {q^4}} \right) = \frac{{82}}{{11}}}
\end{array}} \right..
$$

Suy ra: $\frac{{{q^4} + 1}}{{{q^3} + {q^2} + q}} = \frac{{82}}{{39}}$ $\Leftrightarrow 39{q^4} – 82{q^3} – 82{q^2} – 82q + 39 = 0.$

$\Leftrightarrow (3q – 1)(q – 3)\left( {13{q^2} + 16q + 13} \right) = 0$ $\Leftrightarrow q = \frac{1}{3}$ hoặc $q = 3.$

+ Với $q = \frac{1}{3}$ $\Rightarrow {u_1} = \frac{{81}}{{11}}$ $\Rightarrow {u_n} = \frac{{81}}{{11}}.\frac{1}{{{3^{n – 1}}}}$

+ Với $q = 3$ $\Rightarrow {u_1} = \frac{1}{{11}}$ $\Rightarrow {u_n} = \frac{{{3^{n – 1}}}}{{11}}.$

2. Ta có: ${S_{2011}} = {u_1}\frac{{{q^{2011}} – 1}}{{q – 1}}.$

+ Với $q = \frac{1}{3}$ $\Rightarrow {S_{2011}} = \frac{{243}}{{22}}\left( {1 – \frac{1}{{{3^{2011}}}}} \right).$

+ Với $q = 3$ $\Rightarrow {S_{2011}} = \frac{1}{{22}}\left( {{3^{2011}} – 1} \right).$

3. Với $q = 3$ ta có: ${u_n} = \frac{{{3^{n – 1}}}}{{11}} \in \left( {\frac{1}{2};1} \right)$ $\Leftrightarrow n = 3$ nên có một số hạng của dãy.

Với $q = \frac{1}{3}$ ta có: ${u_n} = \frac{1}{{{{11.3}^{n – 5}}}} \in \left( {\frac{1}{2};1} \right)$ $\Leftrightarrow n = 3$ nên có một số hạng của dãy.

## Bài 9. Cho dãy số $\left( {{x_n}} \right)$: ${x_n} = \frac{1}{n}$, $n = 1,2,3 \ldots .$ Chứng minh rằng luôn tồn tại một cấp số cộng gồm $2011$ số hạng mà mỗi số hạng đều thuộc dãy số trên.

Lời giải: Xét dãy số $\left( {{u_n}} \right):{u_k} = \frac{k}{{2011!}}$, $k = \overline {1,2011} .$

Ta có: ${u_{k + 1}} = \frac{{k + 1}}{{2011!}}$ $= \frac{k}{{2011!}} + \frac{1}{{2011!}}$ $= {u_k} + \frac{1}{{2011!}}.$

Nên dãy $\left( {{u_n}} \right)$ là cấp số cộng có $2011$ số hạng.

Hơn nữa ${u_k} = \frac{1}{{1.2 \ldots (k – 1)(k + 1) \ldots 2011}}$ $= {x_{1.2 \ldots (k – 1)(k + 1) \ldots 2011}}.$

Từ đó ta có điều phải chứng minh.