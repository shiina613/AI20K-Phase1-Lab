# Cách giải bất phương trình logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán bất phương trình logarit thường gặp trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## A. TÓM TẮT SÁCH GIÁO KHOA

Định nghĩa: Bất phương trình logarit cơ bản là bất phương trình có một trong các dạng: ${\log _a}x > m$, ${\log _a}x \ge m$, ${\log _a}x < m$, ${\log _a}x \le m$ với $0 < a \ne 1.$

## B. PHƯƠNG PHÁP GIẢI TOÁN

**Phương pháp chung**: Dùng tính chất đồng biến, nghịch biến của hàm mũ (mũ hóa).

**Chú ý**: Có thể tìm tập xác định của bất phương trình trước khi giải.

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Vấn đề 1: Bất phương trình logarit dạng cơ bản.

1. PHƯƠNG PHÁP:

Với bất phương trình ${\log _a}x > m$ $(1).$

$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x > {a^m}{\rm{\:nếu\:}}a > 1}\\
{0 < x < {a^m}{\rm{\:nếu\:}}0 < a < 1}
\end{array}} \right..
$$

2. CÁC VÍ DỤ:

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Ví dụ 1: Giải các bất phương trình sau:

a) ${\log _2}\left( {{x^2} – 2x} \right) > 3.$

b) ${\log _{\frac{1}{3}}}\left( {{x^2} – 6x} \right) > – 3.$

a) ${\log _2}\left( {{x^2} – 2x} \right) > 3$ $\Leftrightarrow {x^2} – 2x > {2^3}$ $\Leftrightarrow {x^2} – 2x – 8 > 0$ $\Leftrightarrow x < – 2$ hoặc $x > 4.$

b) ${\log _{\frac{1}{3}}}\left( {{x^2} – 6x} \right) > – 3$ $\Leftrightarrow 0 < {x^2} – 6x < {\left( {\frac{1}{3}} \right)^{ – 3}}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} – 6x > 0}\\
{{x^2} – 6x – 27 < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x < 0{\rm{\:hoặc\:}}x > 6}\\
{ – 3 < x < 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – 3 < x < 0}\\
{6 < x < 9}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Ví dụ 2: Giải bất phương trình sau: ${\log _3}\frac{{{x^2} + 4x}}{{2x – 3}} < 1.$

${\log _3}\frac{{{x^2} + 4x}}{{2x – 3}} < 1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{{x^2} + 4x}}{{2x – 3}} > 0}\\
{\frac{{{x^2} + 4x}}{{2x – 3}} < 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{{x^2} + 4x}}{{2x – 3}} > 0}\\
{\frac{{{x^2} – 2x + 9}}{{2x – 3}} < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2x – 3 < 0}\\
{{x^2} + 4x < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x < \frac{3}{2}}\\
{ – 4 < x < 0}
\end{array}} \right.
$$
 $\Leftrightarrow – 4 < x < 0.$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) ${\log _8}(4 – 2x) \ge 2.$

b) ${\log _2}\left( {2 – x – \sqrt {{x^2} – 1} } \right) < 1.$

c) ${\log _{\sqrt 5 }}\left( {{6^{x + 1}} – {{36}^x}} \right) \le 2.$

## Bài tập 2. Giải bất phương trình sau: ${\log _{\frac{2}{3}}}{\log _3}|x – 3| \ge 0.$

## Bài tập 3. Giải bất phương trình sau: ${\log _2}x\left( {{{\log }_3}x – 1} \right) + 1 – {\log _3}x > 0.$

## Bài tập 4. Giải bất phương trình: ${\log _{0,7}}\left[ {{{\log }_6}\left( {\frac{{{x^2} + x}}{{x + 4}}} \right)} \right] < 0$ (TSĐH – khối B – 2008).

## Bài tập 5. Giải bất phương trình: ${\log _{\frac{1}{2}}}\left( {\frac{{{x^2} – 3x + 2}}{x}} \right) \ge 0$ (TSĐH – khối D – 2008).

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Vấn đề 2: Đưa logarit về cùng một cơ số.

1. PHƯƠNG PHÁP:

Với $0 < a \ne 1$, ta có:

+ ${\log _a}f(x) > {\log _a}g(x)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) > g(x) > 0{\rm{\:nếu\:}}a{\rm{ }} > 1}\\
{0 < f(x) < g(x){\rm{\:nếu\:}}0 < a < 1}
\end{array}} \right..
$$

+ ${\log _a}f(x) ≥ {\log _a}g(x)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{f(x) ≥ g(x) > 0{\rm{\:nếu\:}}a{\rm{ }} > 1}\\
{0 < f(x) ≤ g(x){\rm{\:nếu\:}}0 < a < 1}
\end{array}} \right..
$$

2. CÁC VÍ DỤ:

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Ví dụ 1: Giải các bất phương trình:

a) ${\log _{0,5}}(5x + 10) < {\log _{0,5}}\left( {{x^2} + 6x + 8} \right).$

b) ${\log _2}(x – 3) + {\log _2}(x – 2) \le 1.$

a) ${\log _{0,5}}(5x + 10) < {\log _{0,5}}\left( {{x^2} + 6x + 8} \right)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^2} + 6x + 8 > 0}\\
{5x + 10 > {x^2} + 6x + 8}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x < – 4 \vee x > – 2}\\
{{x^2} + x – 2 < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x < – 4 \vee x > – 2}\\
{ – 2 < x < 1}
\end{array}} \right.
$$
 $\Leftrightarrow – 2 < x < 1.$

b) ${\log _2}(x – 3) + {\log _2}(x – 2) \le 1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 3 > 0}\\
{x – 2 > 0}\\
{{{\log }_2}(x – 3)(x – 2) \le {{\log }_2}2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 3}\\
{{x^2} – 5x + 6 \le 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 3}\\
{1 \le x \le 4}
\end{array}} \right.
$$
 $\Leftrightarrow 3 < x \le 4.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Ví dụ 2: Giải bất phương trình: ${\log _x}\left( {3 – \sqrt {1 – 2x + {x^2}} } \right) > 1.$

Ta có: ${\log _x}\left( {3 – \sqrt {1 – 2x + {x^2}} } \right) > 1$ $\Leftrightarrow {\log _x}(3 – |1 – x|) > 1$ $(1).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{1 \ne x > 0}\\
{3 – |1 – x| > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{0 < x \ne 1}\\
{ – 2 < x < 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{0 < x < 4}\\
{x \ne 1}
\end{array}} \right..
$$

$$
(1) \Leftrightarrow \left\{ {\begin{array}{l}
{x > 1}\\
{3 – |1 – x| > x}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{0 < x < 1}\\
{3 – |1 – x| < x}
\end{array}} \right.
$$
 $\Leftrightarrow 1 < x < 2$ (thỏa điều kiện).

Vậy nghiệm của bất phương trình là: $1 < x < 2.$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) ${\log _{\frac{1}{3}}}(x + 1) \le {\log _3}(2 – x).$

b) ${\log _{\frac{1}{7}}}\frac{{{x^2} + 6x + 9}}{{2(x + 1)}} < – {\log _7}(x + 1).$

c) ${\log _2}\left( {{9^{x – 1}} + 7} \right) > {\log _2}\left( {{3^{x – 1}} + 1} \right) + 2.$

## Bài tập 2. Giải các bất phương trình sau:

a) ${\log _x}\left( {5{x^2} – 8x + 3} \right) > 2.$

b) ${\log _x}\frac{{4x + 5}}{{6 – 5x}} < – 1.$

## Bài tập 3. Giải các bất phương trình sau:

a) $\frac{1}{2}{\log _{\frac{1}{2}}}x + {\log _{\frac{1}{4}}}(x – 1) + \frac{1}{2}{\log _2}6 \le 0.$

b) $\log \left( {{x^2} – 3x + 6} \right) > 2(\log x + \log 2).$

c) $\frac{1}{{{{\log }_{\frac{1}{2}}}(2x – 1)}} + \frac{1}{{{{\log }_2}\sqrt {{x^2} – 3x + 2} }} > 0.$

## Bài tập 4. Giải bất phương trình: $2{\log _3}(4x – 3) + {\log _{\frac{1}{3}}}(2x + 3) \le 2$ (TSĐH – khối A – 2007).

## Bài tập 5. Giải các bất phương trình sau:

a) ${\log _{\frac{1}{5}}}\left( {{x^2} – 6x + 18} \right) + 2{\log _5}(x – 4) < 0.$

b) ${\log _3}\left[ {{{\log }_{\frac{1}{2}}}\left( {{x^2} – 1} \right)} \right] < 1.$

## Bài tập 6. Giải bất phương trình: ${\log _x}\left( {{{\log }_3}\left( {{9^x} – 72} \right)} \right) \le 1$ (TSĐH – khối B – 2002).

<!-- chunk:8 level:2 source:https://toanmath.com/2019/08/cach-giai-bat-phuong-trinh-logarit.html -->
## Vấn đề 3: Phương pháp đặt ẩn số phụ.

1. PHƯƠNG PHÁP:

Nếu đặt $t = {\log _a}x$ thì ${\log _{\frac{1}{a}}}x = – t$, ${\log _{{a^2}}}x = \frac{1}{2}t$, $\log _a^2x = {t^2}$ ….

2. CÁC VÍ DỤ:

Ví dụ: Giải bất phương trình: ${\log _2}\left( {{2^x} – 1} \right) \cdot {\log _2}\left( {{2^{x + 1}} – 2} \right) < 2.$

Ta có: ${\log _2}\left( {{2^x} – 1} \right).{\log _2}\left( {{2^{x + 1}} – 2} \right) < 2$ $\Leftrightarrow {\log _2}\left( {{2^x} – 1} \right).\left[ {{{\log }_2}\left( {{2^x} – 1} \right) + {{\log }_2}2} \right] < 2$ $(1).$

Đặt $t = {\log _2}\left( {{2^x} – 1} \right).$

$(1)$ trở thành: $t(t + 1) < 2$ $\Leftrightarrow {t^2} + t – 2 < 0$ $\Leftrightarrow – 2 < t < 1$ $\Leftrightarrow – 2 < {\log _2}\left( {{2^x} – 1} \right) < 1$ $\Leftrightarrow {2^{ – 2}} < {2^x} – 1 < {2^1}$ $\Leftrightarrow \frac{1}{4} + 1 < {2^x} < 2$ $\Leftrightarrow \frac{5}{4} < {2^x} < 2$ $\Leftrightarrow {\log _2}\frac{5}{4} < x < {\log _2}2$ $\Leftrightarrow {\log _2}5 – 2 < x < 1.$

## Bài tập

## Bài tập 1. Giải các bất phương trình sau:

a) $2{\log _5}x – {\log _x}125 < 1.$

b) ${\log _x}2.{\log _{\frac{x}{{16}}}}2 > \frac{1}{{{{\log }_2}x – 6}}.$

## Bài tập 2. Giải các bất phương trình sau:

a) ${3^{\log x + 2}} – {3^{\log {x^2} + 5}} + 2 < 0.$

b) ${6^{\log _6^2x}} + {x^{{{\log }_6}x}} \le 12.$

## Bài tập 3. Giải các bất phương trình sau:

a) $\sqrt {\log _3^2x – 4{{\log }_3}x + 9} \ge 2{\log _3}x – 3.$

b) ${\log _2}\left( {{2^x} – 1} \right).{\log _2}\left( {{2^{x + 1}} – 2} \right) < 2.$

## Bài tập 4. Giải bất phương trình: ${\log _5}\left( {{4^x} + 144} \right) – 4{\log _5}2 < 1 + {\log _5}\left( {{2^{x – 2}} + 1} \right)$ (Đề thi TSĐH – khối B – 2006).