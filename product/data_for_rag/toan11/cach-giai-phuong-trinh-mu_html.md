# Cách giải phương trình mũ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán phương trình mũ thường gặp trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## A. TÓM TẮT SÁCH GIÁO KHOA

1. Định nghĩa:

Phương trình mũ là phương trình có chứa ẩn ở số mũ của lũy thừa.

2. Phương trình mũ cơ bản:
${a^x} = m$ với $0 < a \ne 1.$

+ Nếu $m \le 0$ thì phương trình vô nghiệm.

+ Nếu $m > 0$ thì: ${a^x} = m \Leftrightarrow x = {\log _a}m.$

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Vấn đề 1: Đưa về cùng một cơ số.

1. PHƯƠNG PHÁP:

Sử dụng các quy tắc biến đổi lũy thừa để đưa phương trình đã cho về phương trình mà hai vế là hai lũy thừa có cùng cơ số. Áp dụng kết quả:

Với $0 < a \ne 1$ thì ${a^\alpha } = {a^\beta } \Leftrightarrow \alpha = \beta .$

Ta sẽ đưa phương trình đã cho về phương trình không còn ẩn ở mũ.

2. CÁC VÍ DỤ:

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 1: Giải các phương trình sau:

a) ${2^{2x – 1}} + {4^{x + 1}} = 72.$

b) ${9^{{x^2} + 3}} = {27^{2x + 2}}.$

c) ${5^{{2^{\frac{1}{x}}}}} = 625.$

d) ${4^{ – 2{x^2}}} = {64^{x – 9}}.$

a) ${2^{2x – 1}} + {4^{x + 1}} = 72$ $\Leftrightarrow \frac{{{4^x}}}{2} + {4^x}.4 = 72$ $\Leftrightarrow {9.4^x} = 144.$

b) ${9^{{x^2} + 3}} = {27^{2x + 2}}$ $\Leftrightarrow {\left( {{3^2}} \right)^{{x^2} + 3}} = {\left( {{3^3}} \right)^{2x + 2}}$ $\Leftrightarrow {3^{2{x^2} + 6}} = {3^{6x + 6}}$ $\Leftrightarrow 2{x^2} + 6 = 6x + 6$ $\Leftrightarrow {x^2} – 3x = 0 \Leftrightarrow x = 0$ hay $x = 3.$

c) ${5^{{2^{\frac{1}{x}}}}} = 625$ $\Leftrightarrow {5^{{2^{\frac{1}{x}}}}} = {5^4}$ $\Leftrightarrow {2^{\frac{1}{x}}} = 4 = {2^2}$ $\Leftrightarrow \frac{1}{x} = 2$ $\Leftrightarrow x = \frac{1}{2}.$

d) ${4^{ – 2{x^2}}} = {64^{x – 9}}$ $\Leftrightarrow {4^{ – 2{x^2}}} = {4^{3(x – 9)}}$ $\Leftrightarrow – 2{x^2} = 3x – 27$ $\Leftrightarrow 2{x^2} + 3x – 27 = 0$ $\Leftrightarrow x = 3$ hay $x = – \frac{9}{2}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 2: Giải phương trình sau: ${3^x} – {3^{x – 1}} + {3^{x – 2}} = {2^x} + {2^{x – 1}} + {2^{x – 2}}.$

${3^x} – {3^{x – 1}} + {3^{x – 2}} = {2^x} + {2^{x – 1}} + {2^{x – 2}}$ $\Leftrightarrow {3^x} – \frac{{{3^x}}}{3} + \frac{{{3^x}}}{9} = {2^x} + \frac{{{2^x}}}{2} + \frac{{{2^x}}}{4}$ $\Leftrightarrow \frac{7}{9}{3^x} = \frac{7}{4}{2^x}$ $\Leftrightarrow {\left( {\frac{2}{3}} \right)^x} = {\left( {\frac{2}{3}} \right)^2}$ $\Leftrightarrow x = 2.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 3: Giải các phương trình sau:

a. ${(7 + 4\sqrt 3 )^{{x^2} – x – 5}} = {(7 – 4\sqrt 3 )^{2x + 3}}.$

b. ${(3 – 2\sqrt 2 )^{{x^2} – 4x}} = {(3 + 2\sqrt 2 )^{6 – x}}.$

a. ${(7 + 4\sqrt 3 )^{{x^2} – x – 5}} = {(7 – 4\sqrt 3 )^{2x + 3}}$ $\Leftrightarrow {(7 + 4\sqrt 3 )^{{x^2} – x – 5}} = {(7 + 4\sqrt 3 )^{ – 2x – 3}}$ $\Leftrightarrow {x^2} – x – 5 = – 2x – 3$ $\Leftrightarrow {x^2} + x – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 2}
\end{array}} \right..
$$

b. ${(3 – 2\sqrt 2 )^{{x^2} – 4x}} = {(3 + 2\sqrt 2 )^{6 – x}}$ $\Leftrightarrow {(3 – 2\sqrt 2 )^{{x^2} – 4x}} = {(3 – 2\sqrt 2 )^{x – 6}}$ $\Leftrightarrow {x^2} – 4x = x – 6$ $\Leftrightarrow {x^2} – 5x + 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2}\\
{x = 3}
\end{array}} \right..
$$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 4: Giải phương trình sau:

a) ${5^{x – 2}} = {10^x}{.2^{ – x}}{.5^{x + 3}}.$

b) ${2^{\frac{{\sqrt {16x} + 20}}{{\sqrt x (\sqrt x – 1)}}}} = 4.$

a) ${5^{x – 2}} = {10^x}{.2^{ – x}}{.5^{x + 3}}$ $\Leftrightarrow {5^{x – 2}} = {5^x}{2^x}{.2^{ – x}}{.5^{x + 3}}$ $\Leftrightarrow {5^{x – 2}} = {5^{2x + 3}}$ $\Leftrightarrow x – 2 = 2x + 3$ $\Leftrightarrow x = – 5.$

b) Ta có: ${2^{\frac{{\sqrt {16x} + 20}}{{\sqrt x (\sqrt x – 1)}}}} = {2^2}$ $(x > 0,x \ne 1).$

$\Leftrightarrow \frac{{4(\sqrt x + 5)}}{{\sqrt x (\sqrt x – 1)}} = 2$ $\Leftrightarrow 4(\sqrt x + 5) = 2\sqrt x (\sqrt x – 1)$ $\Leftrightarrow {x^2} – 3\sqrt x – 10 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sqrt x = 5}\\
{\sqrt x = – 2{\rm{\:(loại)\:}}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 25.$

## Bài tập

## Bài tập 1. Giải các phương trình sau:

a. ${5^{x + 1}} – {5^x} = {2.2^x} + {2^{x + 3}}.$

b. ${2^{x + 1}} + {9.2^x} – {2^{x + 2}} = 56.$

## Bài tập 2. Giải các phương trình sau:

a. ${2^{\frac{{\sqrt x + 5}}{{\sqrt x (5\sqrt x + 1)}}}} – {2^{2\sqrt x – 1}} = 0.$

b. ${5^{2|2x – 3|}} – {5^{6x – 8}} = 0.$

c. ${(2 + \sqrt 3 )^{2x}} = 2 – \sqrt 3 .$

d. ${2^{{x^2} – 3x + 2}} = 4.$

## Bài tập 3. Giải các phương trình sau:

a. ${2^{{x^2} – 6x – \frac{5}{2}}} = 16\sqrt 2 .$

b. ${3^{x – 1}} = {18^{2x}}{.2^{ – 2}}{.3^{x + 1}}.$

c. ${5^x}{.8^{\frac{{x – 1}}{3}}} = 500.$

d. ${2^{x + 3}}{.3^{x – 2}}{.5^{x + 1}} = 4000.$

e. ${4.9^{x – 1}} = 3\sqrt {{2^{2x + 1}}} .$

f. ${16^{\frac{{x + 10}}{{x – 10}}}} = {0,125.8^{\frac{{x + 5}}{{x – 15}}}}.$

## Bài tập 4. Giải các phương trình sau:

a. ${32^{\frac{{x + 5}}{{x – 7}}}} = {0,25.128^{\frac{{x + 17}}{{x – 3}}}}.$

b. ${5^{x – 1}} = {10^x}{.2^{ – x}}{.5^{x + 1}}.$

c. ${4^x} – {3^{x – 0,5}} = {3^{x + 0,5}} – {2^{2x – 1}}.$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Vấn đề 2: Phương pháp đặt ẩn số phụ.

1. PHƯƠNG PHÁP:

Tìm một lũy thừa chung, đặt làm ẩn phụ $t$ để đưa phương trình về phương trình đơn giản hơn.

Khi đặt ẩn phụ cần lưu ý:

1. Nếu đặt $t = {a^x}$, điều kiện $t>0$ thì:

${a^{2x}} = {\left( {{a^2}} \right)^x} = {\left( {{a^x}} \right)^2} = {t^2}.$

${a^{3x}} = {t^3}.$

${a^{ – x}} = \frac{1}{t}.$

……

## Bài tập 2. Lưu ý các kết quả sau:

$\sqrt 2 – 1 = {(\sqrt 2 + 1)^{ – 1}}.$

$2 – \sqrt 3 = {(2 + \sqrt 3 )^{ – 1}}.$

$4 – \sqrt {15} = {(4 + \sqrt {15} )^{ – 1}}.$

$\sqrt {7 – \sqrt {48} } = {\left( {\sqrt {7 + \sqrt {48} } } \right)^{ – 1}}.$

## Bài tập 3. Gặp phương trình dạng $\alpha .{a^{2f(x)}} + \beta .{a^{f(x) + g(x)}} + \gamma .{a^{2g(x)}} = 0$ ta chia hai vế cho ${a^{2g(x)}}$ và đặt $t = {a^{f(x) – g(x)}}.$

## Bài tập 4. Gặp phương trình dạng $\alpha .{a^{2f(x)}} + \beta .{(ab)^{f(x)}} + \gamma .{b^{2f(x)}} = 0$ ta chia hai vế cho ${a^{2f(x)}}$ và đặt $t = {\left( {\frac{a}{b}} \right)^{f(x)}}.$

2. CÁC VÍ DỤ:

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 1: Giải phương trình sau: ${e^{4x}} + 2 = 3.{e^{2x}}$ $(1).$

Đặt ${e^{2x}} = t$ với $t > 0.$

$(1) \Leftrightarrow {t^2} – 3t + 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \frac{1}{2}\ln 2}
\end{array}} \right..
$$

Vậy nghiệm của phương trình $(1)$ là: $x = 0$ hay $x = \frac{1}{2}\ln 2.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 2: Giải phương trình sau: ${\left( {\sqrt {2 + \sqrt 3 } } \right)^x} + {\left( {\sqrt {2 – \sqrt 3 } } \right)^x} = 4$ $(2).$

Đặt ${\left( {\sqrt {2 + \sqrt 3 } } \right)^x} = t$ $\left( {t > 0} \right)$ $\Rightarrow {\left( {\sqrt {2 – \sqrt 3 } } \right)^x} = \frac{1}{t}.$

Phương trình $(2)$ trở thành: $t + \frac{1}{t} – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t_1} = 2 + \sqrt 3 }\\
{{t_2} = 2 – \sqrt 3 }
\end{array}} \right.
$$
 $\Leftrightarrow x = \pm 2.$

Vậy phương trình có hai nghiệm là $x = 2$ và $x = -2.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 3: Giải phương trình sau: ${3.8^x} + {4.12^x} = {18^x} + {2.27^x}$ $(3).$

Chia hai vế cho ${27^x}$ ta có:

$(3) \Leftrightarrow 3.{\left( {\frac{2}{3}} \right)^{3x}} + 4.{\left( {\frac{2}{3}} \right)^{2x}}$ $= {\left( {\frac{2}{3}} \right)^x} + 2.$

Đặt $t = {\left( {\frac{2}{3}} \right)^x}$, $t > 0.$

Phương trình $(3)$ trở thành $3{t^3} + 4{t^2} – t – 2 = 0.$

$\Leftrightarrow t = \frac{2}{3}$ $\Leftrightarrow {\left( {\frac{2}{3}} \right)^x} = \frac{2}{3}$ $\Leftrightarrow x = 1.$

Vậy nghiệm của phương trình là $x = 1.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 4: Giải phương trình sau: $\frac{{{{49}^x}}}{{{{10}^{2x}}}} = 6.{(0,7)^x} + 7$ $(4).$

$(4) \Leftrightarrow \frac{{{7^{2x}}}}{{{{100}^x}}} – 6.{(0,7)^x} – 7 = 0$ $\Leftrightarrow {(0,7)^{2x}} – 6.{(0,7)^x} + 7 = 0.$

Đặt $t = {(0,7)^x}$, $t > 0.$

Phương trình trên trở thành:

${t^2} – 6t – 7 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1{\rm{\:(loại)\:}}}\\
{t = 7 \Leftrightarrow {{(0,7)}^x} = 7}
\end{array}} \right.
$$
 $\Leftrightarrow x = {\log _{0,7}}7.$

Vậy nghiệm của phương trình là $x = {\log _{0,7}}7.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 5: Giải phương trình sau: ${5^3} – {5^{x – 1}} – {5^{3 – x}} = 99$ $(5).$

Ta có: $(5) \Leftrightarrow {5^{x – 1}} + {5^{3 – x}} – 26 = 0$ $\Leftrightarrow \frac{{{5^x}}}{5} + \frac{{125}}{{{5^x}}} = 26.$

Đặt $t = {5^x}$, điều kiện $t>0.$

Phương trình trở thành:

${t^2} – 130t + 625 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t_1} = 125}\\
{{t_2} = 5}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 3}
\end{array}} \right..
$$

Vậy nghiệm của phương trình là $x = 1$ và $x = 3.$

## Bài tập

## Bài tập 1. Giải các phương trình sau:

a) ${3^{x + 1}} + {18.3^{ – x}} = 29.$

b) ${4.9^x} + {12^x} = {3.16^x}.$

c) ${3.5^{2x + 1}} – {34.15^x} + {135.9^{x – 1}} = 0.$

d) ${5.6^{\frac{x}{2}}} – {4.3^x} + {9.2^x} = 0.$

## Bài tập 2. Giải phương trình sau: ${\left( {\sqrt {7 – \sqrt {48} } } \right)^x} + {\left( {\sqrt {7 + \sqrt {48} } } \right)^x} = \sqrt {7 + \sqrt {35721} } .$

## Bài tập 3. Giải các phương trình sau:

a. ${9^x} – {4.3^x} – 45 = 0.$

b. ${3^{2x + 5}} = {3^{x + 2}} + 2.$

c. ${9^{{x^2} + 1}} + {3^{{x^2} + 1}} – 6 = 0.$

d. ${4^{x – \sqrt {{x^2} – 5} }} – {12.2^{x – 1 – \sqrt {{x^2} – 5} }} + 8 = 0.$

e. ${5.4^x} – {7.10^x} + {2.25^x} = 0.$

f. ${3^{2{x^2} + 6x – 9}} + {4.15^{{x^2} + 3x – 5}} = {3.5^{2{x^2} + 6x – 9}}.$

## Bài tập 4. Giải các phương trình sau:

a) ${2^{3x + 1}} – {125^x} – {50^x} = 0.$

b) ${8^x} – {2.4^x} – {2^x} + 2 = 0.$

c) ${7^{\frac{2}{x} + 2}} – {74.35^{\frac{1}{x}}} – {25^{\frac{1}{x} + 1}} = 0.$

d) ${2^{x(1 – x) + 2}} – {2^{x(x – 1)}} + 3 = 0.$

e) ${4^{x + \sqrt {{x^2} – 2} }} – {5.2^{x – 1 + \sqrt {{x^2} – 2} }} – 6 = 0.$

f) ${3^{4x + 8}} – {4.3^{2x + 5}} + 28 = 2{\log _2}\sqrt 2 .$

## Bài tập 5. Giải các phương trình sau:

a) ${3^{2{{\sin }^2}x}} + {3^{2{{\cos }^2}x}} = 10.$

b) ${4^{{{\sin }^2}x}} + {2^{{{\cos }^2}x}} – \sqrt 2 (\sqrt 2 + 1) = 0.$

c) ${2^{{{\sin }^2}x}} + {4.2^{{{\cos }^2}x}} = 6.$

d) ${4^{3 + 2\cos 2x}} – {7.4^{1 + \cos 2x}} = {4^{\frac{1}{2}}}.$

## Bài tập 6. Giải các phương trình sau:

a) ${2^{{x^2} – x}} – {2^{2 + x – {x^2}}} = 3$ (Khối D – 2003).

b) ${3.8^x} + {4.12^x} – {18^x} – {2.27^x} = 0$ (Khối A – 2006).

c) ${(\sqrt 2 – 1)^x} + {(\sqrt 2 + 1)^x} – 2\sqrt 2 = 0$ (Khối B – 2007).

d) ${2^{{x^2} + x}} – {4.2^{{x^2} – x}} – {2^{2x}} + 4 = 0$ (Khối D – 2006).

<!-- chunk:13 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Vấn đề 3: Phương pháp lôgarit hóa.

1. PHƯƠNG PHÁP:

Với phương trình không cùng cơ số dạng: ${a^{f(x)}} = {b^{g(x)}}$ ($a$, $b$ dương, khác $1$ và nguyên tố cùng nhau), lấy lôgarit cơ số $a$ (hoặc $b$) cho hai vế, ta có:

${a^{f(x)}} = {b^{g(x)}}$ $\Leftrightarrow {\log _a}\left[ {{a^{f(x)}}} \right] = {\log _a}\left[ {{b^{g(x)}}} \right]$ $\Leftrightarrow f(x) = g(x).{\log _a}b.$

2. CÁC VÍ DỤ:

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 1: Giải phương trình sau: ${50.2^{{x^2} – 2}} = {5^{x + 1}}$ $(1).$

Ta có:

$(1) \Leftrightarrow {\log _2}\left( {{{50.2}^{{x^2} – 2}}} \right) = {\log _2}{5^{x + 1}}.$

$\Leftrightarrow {\log _2}50 + {\log _2}{2^{{x^2} – 2}} = (x + 1){\log _2}5.$

$\Leftrightarrow {\log _2}{5^2}.2 + {x^2} – 2 – x{\log _2}5 – {\log _2}5 = 0.$

$\Leftrightarrow {x^2} – x{\log _2}5 – 1 + {\log _2}5 = 0.$

$\Leftrightarrow x = 1$ hay $x = {\log _2}5 – 1.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 2: Giải phương trình sau: ${3^{x – 1}}{.5^{3\frac{{^{x – 1}}}{x}}} = {15^{{x^2} – 7}}$ $(2).$

$(2) \Leftrightarrow {\log _5}\left( {{2^{x – 1}}{{.5}^{3\frac{{x + 1}}{x}}}} \right) = {\log _5}\left( {{{10}^{x – 1}}{{.5}^{{x^2} – 7}}} \right).$

$\Leftrightarrow (x – 1){\log _5}2 + 3.\frac{{x + 1}}{x}$ $= (x – 1){\log _5}10 + {x^2} – 7.$

$\Leftrightarrow \left( {{x^2} – x} \right){\log _5}2 + 3x + 3$ $= \left( {{x^2} – x} \right){\log _5}10 + {x^3} – 7x.$

$\Leftrightarrow \left( {{x^2} – x} \right)\left( {{{\log }_5}10 – {{\log }_5}2} \right) + {x^3} – 10x – 3 = 0.$

$\Leftrightarrow {x^2} – x + {x^3} – 10x – 3 = 0$ $\Leftrightarrow {x^3} + {x^2} – 11x – 3 = 0.$

$\Leftrightarrow (x – 3)\left( {{x^2} + 4x + 1} \right) = 0$ $\Leftrightarrow x = 3$ hay $x = – 2 \pm \sqrt 3 .$

Vậy phương trình có $3$ nghiệm là: $x = 3$ hay $x = – 2 \pm \sqrt 3 .$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 3: Giải phương trình sau: ${5^x}{.8^{\frac{{x – 1}}{x}}} – 500 = 0.$

Ta có: ${5^x}{.8^{\frac{{x – 1}}{x}}} – 500 = 0$ $\Leftrightarrow {5^x}{.2^{\frac{{3(x – 1)}}{x}}} = {5^3}{.2^2}$ $\Leftrightarrow {2^{\left( {\frac{{3(x – 1)}}{x} – 2} \right)}} = {5^{(3 – x)}}$ $\Leftrightarrow \left( {\frac{{3(x – 1)}}{x} – 2} \right) = (3 – x){\log _2}5$ $\Leftrightarrow {x^2}.{\log _2}5 + \left( {1 – 3{{\log }_2}5} \right)x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = {{\log }_5}\frac{1}{2} = – {{\log }_5}2}\\
{x = 3}
\end{array}.} \right.
$$

Vậy nghiệm của phương trình là: 
$$
\left[ {\begin{array}{l}
{x = – {{\log }_5}2}\\
{x = 3}
\end{array}} \right..
$$

## Bài tập

## Bài tập 1. Giải các phương trình sau:

a. ${2^{x – 3}} = {5^{{x^2} – 5x + 6}}.$

b. ${3^x}{.2^{{x^2}}} = 144.$

c. ${3^{x – 1}}{.2^{{x^2}}} = {8.4^{x – 2}}.$

## Bài tập 2. Giải các phương trình sau:

a. ${2^{{x^3} – 1}}{.5^x} = 3200.$

b. ${3^{2x + 4}} = {4^{{x^2} – 1}}.$

c. ${6^x} + {6^{x + 1}} = {2^{{x^2}}} + {2^{{x^2} + 2}} + {2^{{x^2} + 4}}.$

d. ${7^{\log x}} – {5^{\log x + {{\log }_5}(x – 1) – 1}} = {5^{\log x – 1}} – {3.7^{\log x – 1}}.$

## Bài tập 3. Giải các phương trình sau:

a. ${3^{{4^x}}} = {4^{{3^x}}}.$

b. ${3^{2 – {{\log }_3}x}} = 81x.$

c. ${3^x}{.8^{\frac{x}{{x + 1}}}} = 36.$

d. ${x^6}{.5^{ – {{\log }_x}5}} = {5^{ – 5}}.$

<!-- chunk:17 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Vấn đề 4: Phương pháp dùng tính đơn điệu của hàm số.

1. PHƯƠNG PHÁP:

Hướng 1: Biến đổi hai vế của phương trình sao cho một vế là một hàm số đồng biến (hoặc là hàm hằng) và một vế là một hàm số nghịch biến (hoặc là hàm hằng).

+ Bước 1: Nhẩm và chứng minh ${x_0}$ là nghiệm.

+ Bước 2: Chứng minh ${x_0}$ là nghiệm duy nhất (bằng cách chứng minh $x \ne {x_0}$ không là nghiệm).

Hướng 2: Đưa phương trình về dạng $f(u) = f(v)$ mà $f$ là hàm số tăng hay giảm.

Khi đó ta có: $f(u) = f(v) \Leftrightarrow u = v.$

2. CÁC VÍ DỤ:

<!-- chunk:18 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 1: Giải phương trình: ${2^x} + 3x – 5 = 0$ $(1).$

Xét hàm số $f(x) = {2^x} + 3x – 5$, ta có:

$f(1) = 0$ nên $x = 1$ là một nghiệm của phương trình.

$f'(x) = {2^x}\ln 2 + 3 > 0$, $\forall x$ nên $f$ đồng biến trên $R.$

Suy ra $(1)$ có nhiều nhất là một nghiệm.

Vậy phương trình $(1)$ có một nghiệm duy nhất $x = 1.$

<!-- chunk:19 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 2: Giải phương trình: ${3^x} + {4^x} = {5^x}.$

Chia hai vế phương trình cho ${5^x}$ ta có: ${\left( {\frac{3}{5}} \right)^x} + {\left( {\frac{4}{5}} \right)^x} – 1 = 0$ $(*).$

Xét hàm số $f(x) = {\left( {\frac{3}{5}} \right)^x} + {\left( {\frac{4}{5}} \right)^x} – 1$, ta có:

$f(2) = 0 \Rightarrow x = 2$ là một nghiệm của phương trình $(*).$

$f'(x) = {\left( {\frac{3}{5}} \right)^x}\ln \frac{3}{5} + {\left( {\frac{4}{5}} \right)^x}\ln \frac{4}{5} < 0$ $\Rightarrow f$ nghịch biến trên $R.$

Suy ra $(*)$ có nhiều nhất là một nghiệm.

Vậy phương trình có một nghiệm duy nhất là $x = 2.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Ví dụ 3: Giải phương trình: ${3^{2x}} + 2x\left( {{3^x} + 1} \right) – {4.3^x} – 5 = 0.$

${3^{2x}} + 2x\left( {{3^x} + 1} \right) – {4.3^x} – 5 = 0$ $\Leftrightarrow {3^{2x}} + 2x\left( {{3^x} + 1} \right) – {4.3^x} – 5 = 0$ $\Leftrightarrow {9^x} – 1 + 2x\left( {{3^x} + 1} \right) – 4\left( {{3^x} + 1} \right) = 0$ $\Leftrightarrow \left( {{3^x} + 1} \right)\left( {{3^x} + 2x – 5} \right) = 0$ $\Leftrightarrow {3^x} + 2x – 5 = 0$ $(*).$

Xét $f(x) = {3^x} + 2x – 5$, ta có:

$f(1) = 0 \Rightarrow x = 1$ là một nghiệm của phương trình $(*).$

$f'(x) = {3^x}\ln 3 + 3 > 0$, $\forall x \in R.$

$\Rightarrow f(x) = {3^x} + 2x – 5$ đồng biến trên $R.$

Suy ra phương trình $(*)$ có nhiều nhất một nghiệm.

Vậy phương trình đã cho có một nghiệm duy nhất là $x = 1.$

## Bài tập

## Bài tập 1. Giải phương trình: ${(\sqrt 3 – \sqrt 2 )^x} + {(\sqrt 3 + \sqrt 2 )^x} = {(\sqrt {10} )^x}.$

## Bài tập 2. Giải phương trình: ${13^x} – {11^x} – {4^x} = {(4\sqrt 2 )^x}.$

## Bài tập 3. Giải các phương trình sau:

a) ${2^x} + {3^x} + {5^x} = 10.$

b) ${3.25^{x – 2}} + (3x – 10){5^{x – 2}} + 3 – x = 0.$

## Bài tập 4. Giải các phương trình sau:

a) ${2^x} = 3 – x.$

b) ${\left( {\frac{1}{3}} \right)^x} = x + 4.$

c) ${\left( {\sin \frac{\pi }{5}} \right)^x} + {\left( {\cos \frac{\pi }{5}} \right)^x} = 1.$

## Bài tập 5. Giải phương trình ${2^{{x^2} + 5x}} + \log x = {2^{x + 5}}.$

## Bài tập 6. Giải phương trình sau: $x – {2^{{{\log }_5}(x + 3)}} = 0.$

## Bài tập 7. Giải phương trình: ${3.2^{2x}} + 6 – 2x = 3 – x – (3x – 10){.2^x}.$

<!-- chunk:21 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-mu.html -->
## Vấn đề 5: Đưa về phương trình tích.

1. PHƯƠNG PHÁP:

Biến đổi phương trình đã cho thành phương trình tích: $A.B = 0.$

Từ đó ta đưa việc giải phương trình đã cho về giải các phương trình $A = 0$; $B = 0$ đơn giản hơn.

2. CÁC VÍ DỤ:

Ví dụ: Giải phương trình: ${x^2}{.2^{x – 1}} – {2^{x + 1}} – {x^2}{.2^{|x – 7| + 4}} + {2^{|x – 7| + 6}} = 0$ $(1).$

Biến đổi bằng cách đặt thừa số chung, ta có:

${2^{x – 1}}\left( {{x^2} – 4} \right) – {2^{|x – 7| + 4}}\left( {{x^2} – 4} \right) = 0$ $\Leftrightarrow \left( {{x^2} – 4} \right)\left( {{2^{x – 1}} – {2^{|x – 7| + 4}}} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} – 4 = 0\:\left( 1 \right)}\\
{{2^{x – 1}} = {2^{|x – 7| + 4}}\:\left( 2 \right)}
\end{array}} \right..
$$

$(1) \Leftrightarrow x = \pm 2.$

$(2) \Leftrightarrow x – 1 = |x – 7| + 4$ $\Leftrightarrow |x – 7| = x – 5$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 5 \ge 0}\\
{x – 7 = x – 5}\\
{x – 7 = – (x – 5)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 5}\\
{x = 6}
\end{array} \Leftrightarrow x = 6} \right..
$$

Vậy phương trình đã cho có $3$ nghiệm là $x = -2$, $x = 2$, $x = 6.$

## Bài tập

## Bài tập 1. Giải phương trình: ${3^{2x}} + 2x\left( {{3^x} + 1} \right) – {4.3^x} = 5.$

## Bài tập 2. Giải phương trình: ${x^2}\left( {{2^{x – 1}} + {2^{2 – x}}} \right) + 3 = 3{x^2} + {2^{2 – x}} + {2^{x – 1}}.$

## Bài tập 3. Giải phương trình: ${x^2}.\left( {{2^{x + 1}} – {2^{|x – 3| + 4}}} \right) + {2^{|x – 3| + 2}} – {2^{x – 1}} = 0.$

## Bài tập 4. Giải phương trình: ${4^{2x + \sqrt {x + 2} }} + {2^{{x^3}}} = {4^{2 + \sqrt {x + 2} }} + {2^{{x^3} + 4x – 4}}$ (khối D – 2010).

## Bài tập 5. Giải phương trình: ${4^{{x^2} – 3x + 2}} + {4^{{x^2} + 6x + 5}} = {4^{2{x^2} + 3x + 7}} + 1.$

## Bài tập 6. Giải phương trình: ${2^{{x^2} + x}} – {4.2^{{x^2} – x}} – {2^{2x}} + 4 = 0$ (khối D – 2006).