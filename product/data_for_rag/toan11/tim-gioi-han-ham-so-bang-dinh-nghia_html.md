# Tìm giới hạn hàm số bằng định nghĩa

<!-- chunk:0 level:0 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
Bài viết hướng dẫn phương pháp tìm giới hạn hàm số bằng định nghĩa, giúp học sinh học tốt chương trình Đại số và Giải tích 11.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
## I. PHƯƠNG PHÁP

Sử dụng định nghĩa chuyển giới hạn của hàm số về giới hạn của dãy số.

<!-- chunk:2 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
## Ví dụ 1. Tìm giới hạn các hàm số sau bằng định nghĩa:

1. $A = \mathop {\lim }\limits_{x \to 1} \left( {3{x^2} + x + 1} \right).$

2. $B = \mathop {\lim }\limits_{x \to 1} \frac{{{x^3} – 1}}{{x – 1}}.$

3. $C = \mathop {\lim }\limits_{x \to 2} \frac{{\sqrt {x + 2} – 2}}{{x – 2}}.$

4. $D = \mathop {\lim }\limits_{x \to + \infty } \frac{{3x + 2}}{{x – 1}}.$

Lời giải:

1. Với mọi dãy $\left( {{x_n}} \right)$ mà $\lim {x_n} = 1$ ta có: $A = \lim \left( {3x_n^2 + {x_n} + 1} \right)$ $= 3 + 1 + 1 = 5.$

2. Với mọi dãy $\left( {{x_n}} \right)$ mà $\lim {x_n} = 1$ và ${x_n} \ne 1$, $\forall n$ ta có:

$B = \lim \frac{{\left( {{x_n} – 1} \right)\left( {x_n^2 + {x_n} + 1} \right)}}{{{x_n} – 1}}$ $= \lim \left( {x_n^2 + {x_n} + 1} \right) = 3.$

3. Với mọi dãy $\left( {{x_n}} \right)$ mà $\lim {x_n} = 2$ và ${x_n} \ne 2$, $\forall n$ ta có:

$B = \lim \frac{{\sqrt {{x_n} + 2} – 2}}{{{x_n} – 2}}$ $= \lim \frac{{\left( {{x_n} – 2} \right)}}{{\left( {{x_n} – 2} \right)(\sqrt {{x_n} + 2} + 2)}}$ $= \lim \frac{1}{{\sqrt {{x_n} + 2} + 2}}$ $= \frac{1}{4}.$

4. Với mọi dãy $\left( {{x_n}} \right)$ mà $\lim {x_n} = + \infty$ ta có:

$D = \lim \frac{{3{x_n} + 2}}{{{x_n} – 1}}$ $= \lim \frac{{3 + \frac{2}{{{x_n}}}}}{{1 – \frac{1}{{{x_n}}}}} = 3.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
## Ví dụ 2. Chứng minh rằng hàm số sau không có giới hạn:

1. $f(x) = \sin \frac{1}{{\sqrt x }}$ khi $x \to 0.$

2. $f(x) = {\cos ^5}2x$ khi $x \to – \infty .$

Lời giải:

1. Xét hai dãy $\left( {{x_n}} \right):$ ${x_n} = \frac{1}{{{{\left( {\frac{\pi }{2} + n2\pi } \right)}^2}}}$, $\left( {{y_n}} \right):$ ${y_n} = \frac{1}{{{{(n\pi )}^2}}}.$

Ta có: $\lim {x_n} = \lim {y_n} = 0$ và $\lim f\left( {{x_n}} \right) = 1$; $\lim f\left( {{y_n}} \right) = 0.$

Nên hàm số không có giới hạn khi $x \to 0.$

2. Tương tự ý 1 xét hai dãy: ${x_n} = n\pi$; ${y_n} = \frac{\pi }{4} + n\pi .$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
## Ví dụ 3. Chứng minh rằng nếu $\mathop {\lim }\limits_{x \to {x_0}} |f(x)| = 0$ thì $\mathop {\lim }\limits_{x \to {x_0}} f(x) = 0.$

Lời giải:

Với mọi dãy $\left( {{x_n}} \right):$ $\lim {x_n} = {x_0}$ ta có: $\lim \left| {f\left( {{x_n}} \right)} \right| = 0$ $\Rightarrow \lim f\left( {{x_n}} \right) = 0.$

$\Rightarrow \mathop {\lim }\limits_{x \to {x_0}} f(x) = 0.$

<!-- chunk:5 level:1 source:https://toanmath.com/2020/05/tim-gioi-han-ham-so-bang-dinh-nghia.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Tìm giới hạn các hàm số sau bằng định nghĩa:

## Bài tập 1. $\mathop {\lim }\limits_{x \to 1} \frac{{x + 1}}{{x – 2}}.$

## Bài tập 2. $\mathop {\lim }\limits_{x \to 1} \frac{{3x + 2}}{{2x – 1}}.$

## Bài tập 3. $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {x + 4} – 2}}{{2x}}.$

## Bài tập 4. $\mathop {\lim }\limits_{x \to {1^ + }} \frac{{4x – 3}}{{x – 1}}.$

Lời giải:

1. Với mọi dãy $\left( {{x_n}} \right):$ $\lim {x_n} = 1$ ta có: $\lim \frac{{{x_n} + 1}}{{{x_n} – 2}} = – 2.$

Vậy $\mathop {\lim }\limits_{x \to 1} \frac{{x + 1}}{{x – 2}} = – 2.$

2. Với mọi dãy $\left( {{x_n}} \right):$ $\lim {x_n} = 1$ ta có:

$\mathop {\lim }\limits_{x \to 1} \frac{{3x + 2}}{{2x – 1}}$ $= \lim \frac{{3{x_n} + 2}}{{2{x_n} – 1}}$ $= \frac{{3.1 + 2}}{{2.1 – 1}} = 5.$

3. Với mọi dãy $\left( {{x_n}} \right):$ $\lim {x_n} = 0$ ta có:

$\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {x + 4} – 2}}{{2x}}$ $= \lim \frac{{\sqrt {{x_n} + 4} – 2}}{{2{x_n}}}$ $= \lim \frac{{{x_n}}}{{2{x_n}(\sqrt {{x_n} + 4} + 2)}}$ $= \lim \frac{1}{{2(\sqrt {{x_n} + 4} + 2)}} = \frac{1}{8}.$

4. Với mọi dãy $\left( {{x_n}} \right):$ ${x_n} > 1$, $\forall n$ và $\lim {x_n} = 1$ ta có: $\mathop {\lim }\limits_{x \to {1^ + }} \frac{{4x – 3}}{{x – 1}}$ $= \lim \frac{{4{x_n} – 3}}{{{x_n} – 1}} = + \infty .$

## Bài 2. Chứng minh rằng các hàm số sau không có giới hạn:

## Bài tập 1. $f(x) = \sin \frac{1}{x}$ khi $x \to 0.$

## Bài tập 2. $f(x) = \cos x$ khi $x \to + \infty .$

Lời giải:

## Bài tập 1. Xét hai dãy số ${x_n} = \frac{1}{{\pi + 2n\pi }}$; ${y_n} = \frac{1}{{\frac{\pi }{2} + 2n\pi }}$ $\Rightarrow \lim {x_n} = \lim {y_n} = 0.$

Mà: $\lim f\left( {{x_n}} \right) = \lim [\sin (\pi + 2n\pi )] = 0.$

$\lim f\left( {{y_n}} \right) = \lim \left[ {\sin \left( {\frac{\pi }{2} + 2n\pi } \right)} \right] = 1.$

Suy ra $\lim f\left( {{x_n}} \right) \ne \lim f\left( {{y_n}} \right).$

Vậy hàm số $f$ không có giới hạn khi $x \to 0.$

## Bài tập 2. Xét hai dãy ${x_n} = 2n\pi$; ${y_n} = \frac{\pi }{2} + n\pi$ $\Rightarrow \lim {x_n} = \lim {y_n} = + \infty .$

Mà: $\lim f\left( {{x_n}} \right) = \lim [\cos (2n\pi )] = 1.$

$\lim f\left( {{y_n}} \right) = \lim \left[ {\cos \left( {\frac{\pi }{2} + n\pi } \right)} \right] = 0.$

Suy ra $\lim f\left( {{x_n}} \right) \ne \lim f\left( {{y_n}} \right).$

Vậy hàm số $f$ không có giới hạn khi $x \to + \infty .$

## Bài 3. Chứng minh rằng các hàm số sau không có giới hạn:

$f(x) = \cos \frac{1}{{{x^2}}}$ khi $x \to 0.$

Lời giải:

Xét hai dãy $\left( {{x_n}} \right)$; $\left( {{y_n}} \right)$ xác định bởi ${x_n} = \sqrt {\frac{1}{{2n\pi }}}$; ${y_n} = \sqrt {\frac{1}{{\frac{\pi }{2} + n\pi }}} .$

Ta có: $\lim {x_n} = \lim {y_n} = 0.$

Nhưng: $\lim f\left( {{x_n}} \right) = 1$; $\lim f\left( {{y_n}} \right) = 0$ nên hàm số $f$ không có giới hạn khi $x \to 0.$