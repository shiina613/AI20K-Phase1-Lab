# Cách giải phương trình logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán phương trình logarit thường gặp trong chương trình Giải tích lớp 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## A. TÓM TẮT SÁCH GIÁO KHOA

1. Định nghĩa:

Phương trình logarit là phương trình có chứa ẩn số dưới dấu logarit.

2. Phương trình logarit cơ bản:
${\log _a}x = m$ (với $0 < a \ne 1$) $\Leftrightarrow x = {a^m}.$

<!-- chunk:2 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Vấn đề 1: Đưa các logarit về cùng cơ số.

1. PHƯƠNG PHÁP:
Với $0 < a \ne 1$ thì:

${\log _a}\alpha = {\log _a}\beta$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\alpha = \beta }\\
{\alpha > 0({\rm{\:hay\:}}\beta > 0)}
\end{array}} \right..
$$

${\log _a}f(x) = m \Leftrightarrow f(x) = {a^m}.$

2. CÁC VÍ DỤ:

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 1: Giải các phương trình sau:

a) ${\log _3}x + {\log _3}(x + 2) = 1.$

b) ${\log _2}\left( {{2^x} – 3} \right) + x = 2.$

a) ${\log _3}x + {\log _3}(x + 2) = 1$ $(1).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x > 0}\\
{x + 2 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow x > 0.$

$(1) \Leftrightarrow {\log _3}x(x + 2) = {\log _3}3$ $\Leftrightarrow x(x + 2) = 3$ $\Leftrightarrow {x^2} + 2x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 3\:{\rm{(loại)}}}\\
{x = 1\:{\rm{(nhận)}}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

b) ${\log _2}\left( {{2^x} – 3} \right) + x = 2$ $\Leftrightarrow {\log _2}\left( {{2^x} – 3} \right) = 2 – x$ $\Leftrightarrow {2^x} – 3 = {2^{2 – x}}$ $\Leftrightarrow {2^x} – 3 = \frac{4}{{{2^x}}}$ $\Leftrightarrow {\left( {{2^x}} \right)^2} – {3.2^x} – 4 = 0$ $(1).$

Đặt $t = {2^x}$, điều kiện $t>0.$

$(1)$ trở thành ${t^2} – 3t – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1\:{\rm{(loại)}}}\\
{t = 4\:{\rm{(nhận)}}}
\end{array}} \right.
$$
 $\Leftrightarrow {2^x} = 4$ $\Leftrightarrow x = 2.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 2: Giải các phương trình sau:

a) ${\log _2}\frac{1}{x} = {\log _{\frac{1}{2}}}\left( {{x^2} – x – 3} \right).$

b) ${\log _4}(x + 12).{\log _x}2 = 1.$

a) ${\log _2}\frac{1}{x} = {\log _{\frac{1}{2}}}\left( {{x^2} – x – 3} \right).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x > 0}\\
{{x^2} – x – 3 > 0}
\end{array}} \right.
$$
. Ta có:

${\log _2}\frac{1}{x} = {\log _{\frac{1}{2}}}\left( {{x^2} – x – 3} \right)$ $\Leftrightarrow {\log _2}{x^{ – 1}} = {\log _{{2^{ – 1}}}}\left( {{x^2} – x – 3} \right)$ $\Leftrightarrow – {\log _2}x = – {\log _2}\left( {{x^2} – x – 3} \right)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 0}\\
{{x^2} – x – 3 = x}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 0}\\
{{x^2} – 2x – 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 0}\\
{x = – 1{\rm{\:hoặc\:}}x = 3}
\end{array}} \right.
$$
 $\Leftrightarrow x = 3$ (thỏa mãn điều kiện).

Vậy phương trình đã cho có nghiệm là $x = 3.$

b) ${\log _4}(x + 12).{\log _x}2 = 1$ $(1).$

Điều kiện: $0 < x \ne 1.$

$(1) \Leftrightarrow \frac{1}{2}{\log _2}(x + 12) = {\log _2}x$ $\Leftrightarrow {\log _2}(x + 12) = {\log _2}{x^2}$ $\Leftrightarrow x + 12 = {x^2}$ $\Leftrightarrow {x^2} – x – 12 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 4\:{\rm{(nhận)}}}\\
{x = – 3\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 4.$

Vậy phương trình đã cho có nghiệm là $x = 4.$

## Bài tập
## Bài tập 1. Giải các phương trình sau:

a. $\log (\sqrt {x + 1} + 1) – 3\log \sqrt[3]{{x – 40}} = 0.$

b. $2 – \log (x – 9) – \log (2x – 1) = 0.$

c. ${\log _2}\left( {{x^2} + 3x + 2} \right) + {\log _2}\left( {{x^2} – 7x + 12} \right)$ $– {\log _2}3 – 3 = 0.$

d. ${3^{{{\log }_4}x + \frac{1}{2}}} + {3^{{{\log }_4}x – \frac{1}{2}}} = 4\sqrt x .$

## Bài tập 2. Giải các phương trình sau:

a. ${\log _2}[x(x – 1)] = 1.$

b. ${\log _2}x + {\log _2}(x – 1) = 1.$

c. ${\log _2}(3 – x) + {\log _2}(1 – x) = 3.$

d. ${\log _2}x + {\log _4}x = {\log _{\frac{1}{2}}}\sqrt 3 .$

## Bài tập 3. Giải các phương trình sau:

a. ${\log _3}\left( {{3^x} + 8} \right) = 2 + x.$

b. ${\log _2}\left( {9 – {2^x}} \right) = {10^{\lg (3 – x)}}.$

c. ${\log _{\sqrt 3 }}x.{\log _3}x.{\log _9}x = 8.$

d. ${\log _4}\left( {{{\log }_2}x} \right) + {\log _2}\left( {{{\log }_4}x} \right) = 2.$

## Bài tập 4. Giải phương trình: ${\log _2}\left( {{4^x} + {{15.2}^x} + 27} \right) + 2{\log _2}\frac{1}{{{{4.2}^x} – 3}} = 0.$

## Bài tập 5. Giải các phương trình sau:

a. ${\log _4}{(x + 1)^2} + 2 = {\log _{\sqrt 2 }}\sqrt {4 – x} + {\log _8}{(x + 4)^3}.$

b. ${\log _9}{\left( {{x^2} – 5x + 6} \right)^2} = \frac{1}{2}{\log _{\sqrt 3 }}\frac{{x – 1}}{2} + {\log _3}\left| {x – 3} \right|.$

c. $(x – 1){\log _5}3 + {\log _5}\left( {{3^{x + 1}} + 3} \right) = {\log _5}\left( {{{11.3}^x} – 9} \right).$

d. ${\log _5}x + {\log _3}x = {\log _5}3.{\log _9}225.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Vấn đề 2: Phương pháp đặt ẩn số phụ.

1. PHƯƠNG PHÁP:

Tìm một ${\log _a}f(x)$ chung trong phương trình, đặt bằng $t.$ Đưa phương trình đã cho về phương trình theo $t.$ Giải phương trình tìm $t$, thay $t$ vào cách đặt để tìm $x.$

Chú ý: Nếu đặt $t = {\log _a}x$ thì ${\log _{\frac{1}{a}}}x = – t$, ${\log _{{a^2}}}x = \frac{1}{2}t$, $\log _a^2x = {t^2}$ ….

2. CÁC VÍ DỤ:

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 1: Giải các phương trình sau:

a) $\log _2^2{x^2} – 4{\log _2}{x^3} + 8 = 0.$

b) $\frac{6}{{{{\log }_2}16x}} + \frac{4}{{{{\log }_2}\left( {{x^2}} \right)}} = 2.$

a) $\log _2^2{x^2} – 4{\log _2}{x^3} + 8 = 0$ $(1).$

Điều kiện: $x>0.$

$(1) \Leftrightarrow {\left( {2{{\log }_2}x} \right)^2} – 12{\log _2}x + 8 = 0.$

Đặt $t = {\log _2}x$, ta được:

$(1) \Leftrightarrow 4{t^2} – 12t + 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{{\log }_2}x = 1}\\
{{{\log }_2}x = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2}\\
{x = 4}
\end{array}} \right..
$$

So sánh điều kiện ta được nghiệm của phương trình là $x = 2$ hay $x = 4.$

b) $\frac{6}{{{{\log }_2}16x}} + \frac{4}{{{{\log }_2}\left( {{x^2}} \right)}} = 2$ $(1).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{0 < {x^2} \ne 1}\\
{0 < 16x \ne 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{0 < x \ne 1}\\
{x \ne \frac{1}{{16}}}
\end{array}} \right..
$$

Ta có: $(1) \Leftrightarrow \frac{6}{{{{\log }_2}16 + {{\log }_2}x}} + \frac{4}{{2{{\log }_2}x}} = 2$ $\Leftrightarrow \frac{6}{{{{\log }_2}x + 4}} + \frac{2}{{{{\log }_2}x}} = 2$ $(2).$

Đặt $t = {\log _2}x.$

Phương trình $(2)$ trở thành:

$\frac{6}{{t + 4}} + \frac{2}{t} = 2$ $\Leftrightarrow 6t + 2t + 8 = 2t(t + 4)$ $\Leftrightarrow 2{t^2} – 8 = 0$ $\Leftrightarrow t = \pm 2.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{{{\log }_2}x = 2}\\
{{{\log }_2}x = – 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 4}\\
{x = \frac{1}{4}}
\end{array}} \right..
$$

Vậy phương trình đã cho có nghiệm là $x = 4$ và $x = \frac{1}{4}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 2: Giải phương trình sau: $\log _3^2x + \sqrt {\log _3^2x + 1} – 5 = 0.$

Ta có: $\log _3^2x + \sqrt {\log _3^2x + 1} – 5 = 0$ $(1).$

Đặt $t = \sqrt {\log _3^2x + 1} .$ Điều kiện: $t \ge 1.$

Phương trình $(1)$ trở thành:

${t^2} + t – 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2\:{\rm{(nhận)}}}\\
{t = – 3\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow t = 2.$

$\Leftrightarrow \log _3^2x = 3$ $\Leftrightarrow {\log _3}x = \pm 3$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = {3^{\sqrt 3 }}}\\
{x = {3^{ – \sqrt 3 }}}
\end{array}} \right..
$$

Vậy nghiệm của phương trình là $x = {3^{\sqrt 3 }}$, $x = {3^{ – \sqrt 3 }}.$

## Bài tập

## Bài tập 1. Giải các phương trình sau:

a. ${\log ^2}x = 3 + \log {x^2}.$

b. ${2.9^{{{\log }_2}x – 1}} = {6^{{{\log }_2}x}} – {x^2}.$

c. ${\log _3}(2x + 1) – 2{\log _{2x + 1}}3 – 1 = 0.$

d. ${\log ^2}\left( {{x^3}} \right) – 20\log \sqrt x + 1 = 0.$

## Bài tập 2. Giải các phương trình sau:

a. ${\log _5}\left( {{5^x} – 1} \right)\left[ {\frac{1}{2}{{\log }_5}5\left( {{5^x} – 1} \right)} \right] – 1 = 0.$

b. ${\log _{27}}\left( {{x^{{{\log }_{27}}x}}} \right) – 3{\log _{27}}x + 2 = 0.$

c. $3\sqrt {{{\log }_2}x} – {\log _2}8x + 1 = 0.$

d. $5\sqrt {{{\log }_2}( – x)} = {\log _2}\sqrt {{x^2}} .$

## Bài tập 3. Giải các phương trình sau:

a. ${\log _{9x}}27 – {\log _{3x}}3 + {\log _9}243 = 0.$

b. $\frac{{{{\log }_2}x}}{{{{\log }_4}2x}} = \frac{{{{\log }_8}4x}}{{{{\log }_{16}}8x}}.$

c. ${\log _3}\left( {{3^x} – 1} \right).{\log _3}\left( {{3^{x + 1}} – 3} \right) = 12.$

d. ${\log _{x – 1}}4 = 1 + {\log _2}(x – 1).$

## Bài tập 4. Giải các phương trình sau:

a. $\frac{6}{{{{\log }_2}x + 1}} + \frac{2}{{{{\log }_2}x}} – 3 = 0.$

b. $\frac{1}{{{{\log }_2}\frac{{16}}{x}}} + \frac{2}{{{{\log }_2}4x}} = 1.$

## Bài tập 5. Cho phương trình: $\log _3^2x + \sqrt {\log _3^2x + 1} – 2m – 1 = 0$ $(1)$ ($m$ là tham số).

a. Giải phương trình $(1)$ khi $m = 2.$

b. Định $m$ để $(1)$ có ít nhất một nghiệm thuộc đoạn $\left[ {1;{3^{\sqrt 3 }}} \right].$

(Đề thi TSĐH – khối A – 2002).

## Bài tập 6. Giải các phương trình sau:

a. ${\log _3}\left( {\log _{0,5}^2x – 3{{\log }_{0,5}}x + 5} \right) = 2.$

b. ${\log _2}\left( {{{4.3}^x} – 6} \right) – {\log _2}\left( {{9^x} – 6} \right) = 1.$

## Bài tập 7. Giải phương trình: ${\log _{2x – 1}}\left( {2{x^2} + x – 1} \right) + {\log _{x + 1}}{(2x – 1)^2} = 4$ (Đề thi TSĐH – khối A – 2008).

<!-- chunk:8 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Vấn đề 3: Phương pháp dùng tính đơn điệu của hàm số.

1. PHƯƠNG PHÁP:
a) Biến đổi hai vế của phương trình sao cho hai vế là hai hàm số không cùng chiều biến thiên.

+ Bước 1: Nhẩm và chứng minh ${x_0}$ là nghiệm.

+ Bước 2: Chứng minh ${x_0}$ là nghiệm duy nhất (bằng cách chứng minh $x \ne {x_0}$ không là nghiệm).

b) Một số phương trình ta sử dụng phương pháp đánh giá hai vế, phương pháp đối lập … để giải.

c) Một số phương trình biến đổi được về dạng $f(u) = f(v)$ thì ta áp dụng: Nếu $f(t)$ là hàm số tăng (hay giảm) thì $f(u) = f(v) \Leftrightarrow u = v.$

2. CÁC VÍ DỤ:

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 1: Giải phương trình: ${2^x} = 2 – {\log _3}x$ $(1).$

Điều kiện $x>0.$

$(1) \Leftrightarrow f(x) = {2^x} + {\log _3}x – 2 = 0.$

Ta có:

$f(1) = 0$ nên $x =1$ là một nghiệm của phương trình $(1).$

$f'(x) = {2^x}\ln 2 + \frac{1}{{x\ln 3}} > 0$, $\forall x > 0$ nên hàm số $f$ đồng biến trên $(0; + \infty ).$

Suy ra $(1)$ có không quá một nghiệm.

Vậy phương trình có một nghiệm duy nhất $x = 1.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 2: Giải phương trình: $11 – x = {\log _3}x$ $(2).$

Điều kiện $x > 0.$

Ta có: $x = 9$ là một nghiệm của phương trình $(2).$

Ta chứng minh $x = 9$ là nghiệm duy nhất của phương trình.

Ta có:

$f(x) = 11 – x$ $\Rightarrow f'(x) = – 1 > 0$ nên $f$ nghịch biến trên $(0; + \infty ).$

$g(x) = {\log _3}x$ $\Rightarrow g'(x) = \frac{1}{{x\ln 3}} > 0$, $\forall x > 0$ nên $g$ đồng biến trên $(0; + \infty ).$

Do đó:

+ $x>9:$ 
$$
\left\{ {\begin{array}{l}
{VT < 2}\\
{VP > 2}
\end{array}} \right.
$$
 suy ra phương trình $(2)$ không có nghiệm thỏa mãn $x >9.$

+ $0<x<1:$ 
$$
\left\{ {\begin{array}{l}
{VT > 2}\\
{VP < 2}
\end{array}} \right.
$$
 suy ra phương trình $(2)$ không có nghiệm thỏa mãn $x <9.$

Vậy phương trình $(2)$ có một nghiệm duy nhất $x = 9.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Ví dụ 3: Giải phương trình: ${\log _3}\left( {{x^2} + x + 1} \right) = x(2 – x) + {\log _3}x$ $(3).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x > 0}\\
{{x^2} + x + 1 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow x > 0.$

Cách 1: (Dùng phương pháp đánh giá hai vế).

Ta có: $(3) \Leftrightarrow {\log _3}\frac{{\left( {{x^2} + x + 1} \right)}}{x} = 2x – {x^2}$ $(4).$

Ta có:

+ Khi $x > 0$ $\Rightarrow \frac{{{x^2} + x + 1}}{x} = x + \frac{1}{x} + 1 \ge 3$ $\Rightarrow VT(4) \ge {\log _3}3$ $\Rightarrow VT(4) \ge 1.$

Mặt khác ta có: $VP(4) = 2x – {x^2}$ $= 1 – {(x – 1)^2} \le 1.$

Do đó 
$$
(3) \Leftrightarrow \left\{ {\begin{array}{l}
{{{\log }_3}\frac{{\left( {{x^2} + x + 1} \right)}}{x} = 1}\\
{2x – {x^2} = 1}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

Vậy phương trình đã cho có nghiệm $x = 1.$

Cách 2: (Dùng phương pháp hàm số).

Ta có: $(3) \Leftrightarrow {\log _3}\left( {{x^2} + x + 1} \right) + \left( {{x^2} + x + 1} \right)$ $= {\log _3}(3x) + 3x$ $(*).$

Xét hàm số $f(t) = {\log _3}t + t$ với $t > 0.$

Ta có: $f'(t) = \frac{1}{{t\ln 3}} + 1 > 0$ với mọi $t>0.$

Suy ra $f(t)$ là hàm số đồng biến trên $(0; + \infty ).$

Do đó: $(*) \Leftrightarrow f\left( {{x^2} + x + 1} \right) = f(3x)$ $\Leftrightarrow {x^2} + x + 1 = 3x$ $\Leftrightarrow {(x – 1)^2} = 0$ $\Leftrightarrow x = 1.$

Vậy phương trình đã cho có nghiệm duy nhất là $x = 1.$

## Bài tập

## Bài tập 1. Giải các phương trình sau:

a. $x – {2^{{{\log }_5}(x + 3)}} = 0.$

b. ${\log _2}(\sqrt x + 1) – {\log _3}x = 0.$

## Bài tập 2. Giải các phương trình sau:

a. ${\log _2}\left( {x + {3^{{{\log }_6}x}}} \right) – {\log _6}x = 0.$

b. ${\log _7}x = {\log _3}(\sqrt x + 2).$

## Bài tập 3. Giải phương trình: ${\log _3}\left( {\frac{{{x^2} + x + 3}}{{2{x^2} + 4x + 5}}} \right) = {x^2} + 3x + 2.$

## Bài tập 4. Giải phương trình: $2{\log _6}(\sqrt[4]{x} + \sqrt[8]{x}) = {\log _4}\sqrt x .$

## Bài tập 5. Giải phương trình: $(x + 2)\log _3^2(x + 1) + 4(x + 1){\log _3}(x + 1) – 16 = 0.$

## Bài tập 6. Giải phương trình: ${\log _x}(x + 1) = \lg 1,5.$

<!-- chunk:12 level:2 source:https://toanmath.com/2019/08/cach-giai-phuong-trinh-logarit.html -->
## Vấn đề 4: Phương trình tích.

1. PHƯƠNG PHÁP:

Biến đổi phương trình đã cho về phương trình tích.

Ta có: 
$$
A.B = 0 \Leftrightarrow \left[ {\begin{array}{l}
{A = 0}\\
{B = 0}
\end{array}} \right..
$$
 Ở đây các phương trình $A = 0$, $B = 0$ là những phương trình đơn giản hơn.

2. VÍ DỤ:

Ví dụ: Giải phương trình: $2\log _9^2x = {\log _3}x.{\log _3}(\sqrt {2x + 1} – 1)$ $(1).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x > 0}\\
{\sqrt {2x + 1} – 1 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow x > 0.$

$(1) \Leftrightarrow 2{\left( {\frac{1}{2}{{\log }_3}x} \right)^2}$ $= {\log _3}x.{\log _3}(\sqrt {2x + 1} – 1)$ $\Leftrightarrow \log _3^2x – 2{\log _3}x{\log _3}(\sqrt {2x + 1} – 1) = 0$ $\Leftrightarrow {\log _3}x\left[ {{{\log }_3}x – 2{{\log }_3}(\sqrt {2x + 1} – 1)} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{{\log }_3}x = 0}\\
{{{\log }_3}x = {{\log }_3}{{(\sqrt {2x + 1} – 1)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2x – 2\sqrt {2x + 1} }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{\sqrt {8x + 4} = x}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{{x^2} – 8x – 4 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 4 + 2\sqrt 5 }
\end{array}} \right..
$$

Vậy phương trình có hai nghiệm là $x = 1$ hay $x = 4 + 2\sqrt 5 .$

## Bài tập

## Bài tập 1. Giải phương trình ${\log _2}x + 2{\log _7}x = 2 + {\log _2}x.{\log _7}x.$

## Bài tập 2. Giải phương trình $2x + {\log _2}\left( {{x^2} – 4x + 4} \right)$ $= 2 – (x + 1){\log _{\frac{1}{2}}}(2 – x).$

## Bài tập 3. Giải phương trình: $\frac{1}{{x – 1}}\log _2^2x + {\log _2}x + 2 = \frac{4}{{x – 1}}.$