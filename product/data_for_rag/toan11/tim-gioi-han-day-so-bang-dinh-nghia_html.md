# Tìm giới hạn dãy số bằng định nghĩa

<!-- chunk:0 level:0 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
Bài viết hướng dẫn phương pháp tìm giới hạn dãy số bằng định nghĩa, giúp học sinh học tốt chương trình Đại số và Giải tích 11 chương 4: giới hạn.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
## I. PHƯƠNG PHÁP

+ Để chứng minh $\lim {u_n} = 0$ ta chứng minh với mọi số $a >0$ nhỏ tùy ý, luôn tồn tại một số ${n_a}$ sao cho $\left| {{u_n}} \right| < a$, $\forall n > {n_a}.$

+ Để chứng minh $\lim {u_n} = l$ ta chứng minh $\lim \left( {{u_n} – l} \right) = 0.$

+ Để chứng minh $\lim {u_n} = + \infty$ ta chứng minh với mọi số $M > 0$ lớn tùy ý, luôn tồn tại số tự nhiên ${n_M}$ sao cho ${u_n} > M$, $\forall n > {n_M}.$

+ Để chứng minh $\lim {u_n} = – \infty$ ta chứng minh $\lim \left( { – {u_n}} \right) = + \infty .$

+ Một dãy số nếu có giới hạn thì giới hạn đó là duy nhất.

<!-- chunk:2 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
## Ví dụ 1. Chứng minh rằng:

1. $\lim \frac{{n + 2}}{{n + 1}} = 1.$

2. $\lim \frac{{{n^2} – 1}}{{2{n^2} + 1}} = \frac{1}{2}.$

3. $\lim \frac{{1 – 2n}}{{\sqrt {{n^2} + 1} }} = – 2.$

Lời giải:

1. Với $a > 0$ nhỏ tùy ý, ta chọn ${n_a} > \frac{1}{a} – 1$, ta có: $\left| {\frac{{n + 2}}{{n + 1}} – 1} \right| = \frac{1}{{n + 1}}$ $< \frac{1}{{{n_a} + 1}} < a$ với $\forall n > {n_a}.$

Suy ra $\lim \left| {\frac{{n + 2}}{{n + 1}} – 1} \right| = 0$ $\Rightarrow \lim \frac{{n + 2}}{{n + 1}} = 1.$

2. Với $a > 0$ nhỏ tùy ý, ta chọn ${n_a} > \sqrt {\frac{3}{a} – 1}$, ta có:

$\left| {\frac{{{n^2} – 1}}{{2{n^2} + 1}} – \frac{1}{2}} \right| = \frac{3}{{{n^2} + 1}}$ $< \frac{3}{{n_a^2 + 1}} < a$ với $\forall n > {n_a}.$

Suy ra $\lim \left| {\frac{{{n^2} – 1}}{{2{n^2} + 1}} – \frac{1}{2}} \right| = 0$ $\Rightarrow \lim \frac{{{n^2} – 1}}{{2{n^2} + 1}} = \frac{1}{2}.$

3. Với $a > 0$ nhỏ tùy ý, ta chọn ${n_a} > \sqrt {\frac{9}{{{a^2}}} – 1}$, ta có:

$\left| {\frac{{1 – 2n}}{{\sqrt {{n^2} + 1} }} + 2} \right|$ $= \left| {\frac{{1 – 2n + 2\sqrt {{n^2} + 1} }}{{\sqrt {{n^2} + 1} }}} \right|$ $< \left| {\frac{{1 – 2n + 2(n + 1)}}{{\sqrt {{n^2} + 1} }}} \right|$ $= \frac{3}{{\sqrt {{n^2} + 1} }}$ $< \frac{3}{{\sqrt {n_a^2 + 1} }} < a$ với $\forall n > {n_a}.$

Suy ra $\lim \left| {\frac{{1 – 2n}}{{\sqrt {{n^2} + 1} }} + 2} \right| = 0$ $\Rightarrow \lim \frac{{1 – 2n}}{{\sqrt {{n^2} + 1} }} = – 2.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
## Ví dụ 2. Chứng minh rằng dãy số $\left( {{u_n}} \right)$: ${u_n} = {( – 1)^n}$ không có giới hạn.

Lời giải:

Ta có: ${u_{2n}} = 1$ $\Rightarrow \lim {u_{2n}} = 1$; ${u_{2n + 1}} = – 1$ $\Rightarrow \lim {u_{2n + 1}} = – 1.$

Vì giới hạn của dãy số nếu có là duy nhất nên ta suy ra dãy $\left( {{u_n}} \right)$ không có giới hạn.

<!-- chunk:4 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
## Ví dụ 3. Chứng minh các giới hạn sau:

1. $\lim \frac{{{n^2} + 1}}{n} = + \infty .$

2. $\lim \frac{{2 – n}}{{\sqrt n }} = – \infty .$

Lời giải:

1. Với mọi số thực dương $M$ lớn tùy ý, ta có:

$\left| {\frac{{{n^2} + 1}}{n}} \right| > M$ $\Leftrightarrow {n^2} – Mn + 1 > 0$ $\Leftrightarrow n > \frac{{M + \sqrt {{M^2} – 4} }}{2}.$

Ta chọn ${n_0} = \left[ {\frac{{M + \sqrt {{M^2} – 4} }}{2}} \right]$ thì ta có: $\frac{{{n^2} + 1}}{n} > M$, $\forall n > {n_0}.$

Do đó: $\lim \frac{{{n^2} + 1}}{n} = + \infty .$

2. Với mọi $M > 0$ lớn tùy ý, ta có:

$\frac{{n – 2}}{{\sqrt n }} > M$ $\Leftrightarrow n – M\sqrt n – 2 > 0$ $\Leftrightarrow n > {\left( {\frac{{M + \sqrt {{M^2} + 8} }}{2}} \right)^2}.$

Ta chọn ${n_0} = \left[ {{{\left( {\frac{{M + \sqrt {{M^2} + 8} }}{2}} \right)}^2}} \right]$ thì ta có: $\frac{{n – 2}}{{\sqrt n }} > M$, $\forall n > {n_0}.$

Do đó: $\lim \frac{{2 – n}}{{\sqrt n }} = – \infty .$

<!-- chunk:5 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-day-so-bang-dinh-nghia.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Chứng minh rằng:

## Bài tập 1. $\lim \frac{1}{{{n^k}}} = 0$ $\left( {k \in {N^*}} \right).$

## Bài tập 2. $\lim \frac{{1 – {n^2}}}{n} = – \infty .$

Lời giải:

1. Với $a > 0$ nhỏ tùy ý, ta chọn: ${n_a} > \sqrt[k]{{\frac{1}{a}}}$, ta có: $\frac{1}{{{n^k}}} < \frac{1}{{n_a^k}} < a$, $\forall n > {n_a}$ nên có $\lim \frac{1}{{{n^k}}} = 0.$

2. Với mọi số dương $M$ lớn tùy ý ta chọn ${n_M}$ thỏa mãn $\frac{{n_M^2 – 1}}{{{n_M}}} > M$ $\Leftrightarrow {n_M} > \frac{{M + \sqrt {{M^2} + 4} }}{2}.$

Ta có: $\frac{{{n^2} – 1}}{n} > M$, $\forall n > {n_M}$ $\Rightarrow \lim \frac{{{n^2} – 1}}{n} = + \infty .$

Vậy $\lim \frac{{1 – {n^2}}}{n} = – \infty .$

## Bài 2. Chứng minh các giới hạn sau:

## Bài tập 1. $\lim \frac{{\cos n + \sin n}}{{{n^2} + 1}} = 0.$

## Bài tập 2. $\lim \frac{{\sqrt {n + 1} }}{{n + 2}} = 0.$

## Bài tập 3. $\lim \frac{{3{n^3} + n}}{{{n^2}}} = + \infty .$

Lời giải:

1. Ta có $\frac{{|\cos n + \sin n|}}{{{n^2}}} < \frac{2}{{{n^2}}}$ mà $\lim \frac{1}{{{n^2}}} = 0$ $\Rightarrow \lim \frac{{\cos n + \sin n}}{{{n^2} + 1}} = 0.$

2. Với mọi số thực $a>0$ nhỏ tùy ý, ta chọn ${n_a} = \left[ {\frac{1}{{{a^2}}} – 1} \right] + 1.$

Ta có: $\frac{{\sqrt {n + 1} }}{{n + 2}} < \frac{1}{{\sqrt {n + 1} }} < a$, $\forall n > {n_a}$ $\Rightarrow \lim \frac{{\sqrt {n + 1} }}{{n + 2}} = 0.$

3. Với mọi $M > 0$ lớn tùy ý, ta chọn ${n_M} = \left[ {\frac{M}{3}} \right] + 1.$

Ta có: $\frac{{3{n^3} + n}}{{{n^2}}} = 3n + \frac{1}{n} > M$, $\forall n > {n_M}.$ Vậy $\lim \frac{{3{n^3} + n}}{{{n^2}}} = + \infty .$

## Bài 3. Dùng định nghĩa tìm các giới hạn sau:

## Bài tập 1. $A = \lim \frac{{2n + 1}}{{n – 2}}.$

## Bài tập 2. $B = \lim \frac{{2n + 3}}{{{n^2} + 1}}.$

Lời giải:

1. Với số thực $a>0$ nhỏ tùy ý, ta chọn ${n_a} > \frac{5}{a} + 2 > 2.$

Ta có: $\left| {\frac{{2n + 1}}{{n – 2}} – 2} \right| = \frac{5}{{|n – 2|}}$ $< \frac{5}{{{n_a} – 2}} < a$, $\forall n > {n_a}.$

Vậy $A=2.$

2. Với số thực $a > 0$ nhỏ tùy ý, ta chọn ${n_a}$ thỏa mãn: $\frac{{2{n_a} + 3}}{{n_a^2 + 1}} < a$ $\Leftrightarrow {n_a} > \frac{{1 + \sqrt {{a^2} – 4a + 13} }}{a}.$

Ta có: $\frac{{2n + 3}}{{{n^2} + 1}} < a$, $\forall n > {n_a}$ $\Rightarrow B = 0.$

## Bài 4. Chứng minh các giới hạn sau:

## Bài tập 1. $\lim \frac{{{a^n}}}{{n!}} = 0.$

## Bài tập 2. $\lim \sqrt[n]{a} = 1$ với $a >0.$

Lời giải:

## Bài tập 1. Gọi $m$ là số tự nhiên thỏa mãn: $m + 1 > |a|.$ Khi đó với mọi $n > m + 1.$

Ta có: $0 < \left| {\frac{{{a^n}}}{{n!}}} \right|$ $= \left| {\frac{a}{1}.\frac{a}{2} \ldots \frac{a}{m}} \right|.\left| {\frac{a}{{m + 1}} \ldots \frac{a}{n}} \right|$ $< \frac{{|a{|^m}}}{{m!}}.{\left( {\frac{{|a|}}{{m + 1}}} \right)^{n – m}}.$

Mà $\lim {\left( {\frac{{|a|}}{{m + 1}}} \right)^{n – m}} = 0.$

Từ đó suy ra: $\lim \frac{{{a^n}}}{{n!}} = 0.$

2. Nếu $a =1$ thì ta có điều phải chứng minh.

Giả sử $a >1.$ Khi đó: $a = {[1 + (\sqrt[n]{a} – 1)]^n} > n(\sqrt[n]{a} – 1).$

Suy ra: $0 < \sqrt[n]{a} – 1 < \frac{a}{n} \to 0$ nên $\lim \sqrt[n]{a} = 1.$

Với $0 < a < 1$ thì $\frac{1}{a} > 1$ $\Rightarrow \lim \sqrt[n]{{\frac{1}{a}}} = 1$ $\Rightarrow \lim \sqrt[n]{a} = 1.$

Tóm lại ta luôn có: $\lim \sqrt[n]{a} = 1$ với $a > 0.$

## Bài 5. Dãy số $\left( {{x_n}} \right)$ thỏa mãn điều kiện $1 < {x_1} < 2$ và ${x_{n + 1}} = 1 + {x_n} – \frac{1}{2}x_n^2$, $\forall n \in {N^*}.$ Chứng minh rằng dãy số đã cho hội tụ. Tìm $\lim {x_n}.$

Lời giải:

Ta sẽ chứng minh bằng quy nạp bất đẳng thức sau: $\left| {{x_n} – \sqrt 2 } \right| < \frac{1}{{{2^n}}}$, $\forall n \ge 3.$

Thật vậy ta kiểm tra được ngay bất đẳng thức đúng với $n= 3.$

Giả sử bất đẳng thức đúng với $n \ge 3$, tức là $\left| {{x_n} – \sqrt 2 } \right| < \frac{1}{{{2^n}}}.$

Khi đó ta có: $\left| {{x_{n + 1}} – \sqrt 2 } \right|$ $= \frac{1}{2}\left| {{x_n} – \sqrt 2 } \right|\left| {2 – \sqrt 2 – {x_n}} \right|$ $\le \frac{1}{2}\left| {{x_n} – \sqrt 2 } \right|\left( {\left| {\sqrt 2 – {x_n}} \right| + \left| {2 – 2\sqrt 2 } \right|} \right).$

$< \frac{1}{2}\left| {{x_n} – \sqrt 2 } \right|$ $< \frac{1}{2}\frac{1}{{{2^n}}} = \frac{1}{{{2^{n + 1}}}}.$

Do đó bất đẳng thức đúng đến $n+1.$

Mặt khác do $\lim \frac{1}{{{2^n}}} = 0$ nên từ bất đẳng thức trên và nguyên lý kẹp ta có $\lim \left( {{x_n} – \sqrt 2 } \right) = 0$ $\Rightarrow \lim {x_n} = \sqrt 2 .$

Chú ý: Ta có kết quả sau:

Cho hàm số $f:R \to R$ thỏa: $|f(x) – f(y)| \le q.|x – y|$ với mọi $x,y \in R$ và $q \in (0;1).$ Khi đó dãy số $\left( {{u_n}} \right)$ được xác định bởi ${u_0} = c$; ${u_n} = f\left( {{u_{n – 1}}} \right)$, $\forall n = 2,3, \ldots$ có giới hạn hữu hạn là nghiệm của phương trình $f(x) = x.$

Sử dụng kết quả trên ta có nghiệm của phương trình $f(x) = x$ có nghiệm là $\sqrt 2$ nên ta mới đi chứng minh $\lim {x_n} = \sqrt 2 .$