# Hàm số mũ và hàm số logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
Bài viết trình bày lý thuyết và hướng dẫn phương pháp giải một số dạng toán thường gặp về hàm số mũ và hàm số logarit trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## I. Định nghĩa

Cho $0 < a \ne 1.$

Hàm số dạng $y = {a^x}$ được gọi là hàm số mũ theo cơ số $a.$

Hàm số dạng $y = {\log _a}x$ được gọi là hàm số logarit theo cơ số $a.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## II. Một số giới hạn liên quan đến hàm số mũ và hàm số logarit

1. Hàm số mũ và hàm số logarit liên tục tại mọi điểm mà hàm số xác định, nghĩa là ta có:

$\forall {x_0} \in R$, $\mathop {\lim }\limits_{x \to {x_0}} {a^x} = {a^{{x_0}}}.$

$\forall {x_0} \in (0; + \infty )$, $\mathop {\lim }\limits_{x \to {x_0}} {\log _a}x = {\log _a}{x_0}.$

2. Ta có $\mathop {\lim }\limits_{t \to + \infty } {\left( {1 + \frac{1}{t}} \right)^t} = e$, $\mathop {\lim }\limits_{t \to – \infty } {\left( {1 + \frac{1}{t}} \right)^t} = e.$

3. Bằng cách viết $\frac{1}{t} = x$, ta được: $\mathop {\lim }\limits_{x \to 0} {(1 + x)^{\frac{1}{x}}} = e.$

4. Định lý: $\mathop {\lim }\limits_{x \to 0} \frac{{{e^x} – 1}}{x} = 1$ và $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (1 + x)}}{x} = 1.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## III. Đạo hàm của hàm số mũ

Định lý: Cho $0 < a \ne 1.$

Hàm số $y = {a^x}$ có đạo hàm tại mọi $x \in R$ và $\left( {{a^x}} \right)’ = {a^x}.\ln a.$

Đặc biệt: $\left( {{e^x}} \right)’ = {e^x}.$

Nếu $u = u(x)$ là hàm số có đạo hàm trên khoảng $K$ thì hàm số $y = {a^{u(x)}}$ có đạo hàm trên $K$ và: $\left( {{a^{u(x)}}} \right)’ = u'(x).{a^{u(x)}}.\ln a.$

Đặc biệt: $\left( {{e^{u(x)}}} \right)’ = u'(x).{e^{u(x)}}.$

<!-- chunk:4 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## IV. Đạo hàm của hàm số logarit

1. Định lý: Cho $0 < a \ne 1$ và $u = u(x)$ là hàm số nhận giá trị dương và có đạo hàm trên khoảng $K.$ Ta có:

a) $\left( {{{\log }_a}x} \right)’ = \frac{1}{{x\ln a}}.$ Nói riêng, ta có: $(\ln x)’ = \frac{1}{x}.$

b) $\left( {{{\log }_a}u(x)} \right)’ = \frac{{u'(x)}}{{u(x)\ln a}}.$ Đặc biệt: $(\ln u(x))’ = \frac{{u'(x)}}{{u(x)}}.$

2. Hệ quả: 

a) $(\ln |x|)’ = \frac{1}{x}$ $(x \ne 0).$

b) $(\ln |u(x)|)’ = \frac{{u'(x)}}{{u(x)}}.$

<!-- chunk:5 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## V. Sự biến thiên và đồ thị của hàm số mũ
Tập xác định: $D= R.$

Tập giá trị: $f(D) = (0; + \infty ).$

Đạo hàm: $y’ = {a^x}.\ln a.$

Do đó:

+ Khi $a>1$ thì $y’ > 0$ nên hàm số $y = {a^x}$ đồng biến trên $R.$

+ Khi $0<a< 1$ thì $y'< 0$ nên hàm số $y = {a^x}$ nghịch biến trên $R.$

Giới hạn và tiệm cận:

+ Khi $a>1$ ta có $\mathop {\lim }\limits_{x \to + \infty } {a^x} = + \infty$, $\mathop {\lim }\limits_{x \to – \infty } {a^x} = 0$ nên đồ thị hàm số $y = {a^x}$ nhận $y = 0$ làm tiệm cận ngang khi $x \to – \infty .$

+ Khi $0 < a < 1$ ta có $\mathop {\lim }\limits_{x \to – \infty } {a^x} = + \infty$, $\mathop {\lim }\limits_{x \to + \infty } {a^x} = 0$ nên đồ thị hàm số $y = {a^x}$ nhận $y = 0$ làm tiệm cận ngang khi $x \to + \infty .$

Bảng biến thiên:

+ Với $a > 1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-1.png" alt="">

+ Với $0 <a<1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-2.png" alt="">

Đồ thị hàm số luôn cắt trục tung tại điểm $M(0;1)$ (vì ${a^0} = 1$) và nằm ở phía trên trục hoành (vì ${a^x} > 0$ với mọi $x$).

+ Với $a > 1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-3.png" alt="">

+ Với $0<a<1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-4.png" alt="">

<!-- chunk:6 level:1 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## VI. Sự biến thiên và đồ thị của hàm số $y = {\log _a}x$
Tập xác định: $D = (0; + \infty ).$

Tập giá trị: $f(D) = R.$

Đạo hàm: $y’ = \frac{1}{{x.\ln a}}.$

+ Khi $a>1$ thì $y’> 0$ nên $y = {\log _a}x$ đồng biến trên $(0; + \infty ).$

+ Khi $0<a< 1$ thì $y'< 0$ nên $y = {\log _a}x$ nghịch biến trên $(0; + \infty ).$

Giới hạn và tiệm cận:

+ Khi $a> 1:$ $\mathop {\lim }\limits_{x \to {0^ + }} {\log _a}x = – \infty$, $\mathop {\lim }\limits_{x \to + \infty } {\log _a}x = + \infty$ $\Rightarrow x = 0$ là tiệm cận đứng của đồ thị khi $x \to {0^ + }.$

+ Khi $0<a< 1:$ $\mathop {\lim }\limits_{x \to {0^ + }} {\log _a}x = + \infty$, $\mathop {\lim }\limits_{x \to + \infty } {\log _a}x = – \infty$ $\Rightarrow x = 0$ là tiệm cận đứng của đồ thị khi $x \to {0^ + }.$

Bảng biến thiên:

+ Với $a > 1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-5.png" alt="">

+ Với $0<a<1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-6.png" alt="">

Đồ thị hàm số luôn cắt trục hoành tại điểm $M(1;0)$ (vì ${\log _a}1 = 0$) và nằm ở bên phải trục tung (vì ${\log _a}x$ chỉ xác định khi $x > 0$).

+ Với $a>1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-7.png" alt="">

+ Với $0<a<1:$

<img link="data_for_rag/toan11/images/ham-so-mu-va-ham-so-logarit-8.png" alt="">

Nhận xét: Đồ thị $(G)$ của hàm số $y = {a^x}$ và đồ thị $(G’)$ của hàm số $y = {\log _a}x$ đối xứng với nhau qua đường phân giác của góc phần tư thứ nhất: $y = x.$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Vấn đề 1: Tìm giới hạn của hàm số mũ.

1. PHƯƠNG PHÁP:

Sử dụng các công thức giới hạn:

+ $\forall {x_0} \in R$, $\mathop {\lim }\limits_{x \to {x_0}} {a^x} = {a^{{x_0}}}$ (với $0 < a \ne 1$).

+ Khi gặp giới hạn dạng ${1^\infty }$ ta biến đổi để áp dụng:

$\mathop {\lim }\limits_{x \to 0} {(1 + x)^{\frac{1}{x}}} = e$ hay $\mathop {\lim }\limits_{x \to \pm \infty } {\left( {1 + \frac{1}{x}} \right)^x} = e.$

+ Khi gặp giới hạn dạng $\frac{0}{0}$ ta biến đổi để áp dụng $\mathop {\lim }\limits_{x \to 0} \frac{{{e^x} – 1}}{x} = 1.$

2. CÁC VÍ DỤ:

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 1: Tìm các giới hạn sau:

a) $\mathop {\lim }\limits_{x \to + \infty } {e^{\frac{{2x + 1}}{{x + 1}}}}.$

b) $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt[3]{{{e^x}}} – 1}}{{2x}}.$

a) $\mathop {\lim }\limits_{x \to + \infty } {e^{\frac{{2x + 1}}{{x + 1}}}} = {e^{\mathop {\lim }\limits_{x \to + \infty } \frac{{2x + 1}}{{x + 1}}}} = {e^2}.$

b) $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt[3]{{{e^x}}} – 1}}{{2x}} = \mathop {\lim }\limits_{x \to 0} \frac{{{e^{\frac{x}{3}}} – 1}}{{2x}}$ $= \mathop {\lim }\limits_{x \to 0} \left( {\frac{1}{6}.\frac{{{e^{\frac{x}{3}}} – 1}}{{\frac{x}{3}}}} \right) = \frac{1}{6}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 2: Tìm giới hạn:

a) $\mathop {\lim }\limits_{x \to 0} {(\cos 2x)^{\frac{1}{{{x^2}}}}}.$

b) $\mathop {\lim }\limits_{x \to + \infty } {\left( {\frac{{x + 3}}{{x + 1}}} \right)^{4x + 3}}.$

a) $\mathop {\lim }\limits_{x \to 0} {(\cos 2x)^{\frac{1}{{{x^2}}}}}$ $= \mathop {\lim }\limits_{x \to 0} {\left( {1 – 2{{\sin }^2}x} \right)^{\frac{1}{{{x^2}}}}}$ $= \mathop {\lim }\limits_{x \to 0} {\left( {1 – 2{{\sin }^2}x} \right)^{\frac{1}{{ – 2{{\sin }^2}x}}.\frac{{ – 2{{\sin }^2}x}}{{{x^2}}}}}$ $= \mathop {\lim }\limits_{x \to 0} {\left[ {{{\left( {1 – 2{{\sin }^2}x} \right)}^{\frac{1}{{ – 2{{\sin }^2}x}}}}} \right]^{ – 2{{\left( {\frac{{\sin x}}{x}} \right)}^2}}} = {e^{ – 2}}.$

b) $\mathop {\lim }\limits_{x \to + \infty } {\left( {\frac{{x + 3}}{{x + 1}}} \right)^{4x + 3}}$ $= \mathop {\lim }\limits_{x \to + \infty } {\left[ {{{\left( {1 + \frac{2}{{x + 1}}} \right)}^{\frac{{x + 1}}{2}}}} \right]^{\frac{{2(4x + 3)}}{{x + 1}}}} = {e^8}.$

## Bài tập
## Bài tập 1. Tìm các giới hạn sau:

a. $\mathop {\lim }\limits_{x \to 0} \frac{{{e^2} – {e^{5x + 2}}}}{x}.$

b. $\mathop {\lim }\limits_{x \to 0} \frac{{{e^{2x}} – {e^{7x}}}}{x}.$

c. $\mathop {\lim }\limits_{x \to 0} \frac{{{e^{2x}} + {e^{\sin 3x}} – 2}}{x}.$

## Bài tập 2. Tìm giới hạn:

a. $\mathop {\lim }\limits_{x \to + \infty } \left( {x.{e^{\frac{1}{x}}} – x} \right).$

b. $\mathop {\lim }\limits_{x \to + \infty } {\left( {\frac{{x – 1}}{{x + 2}}} \right)^{3x + 1}}.$

c. $\mathop {\lim }\limits_{x \to 0} {(1 + 4\sin 3x)^{\frac{1}{{2x}}}}.$

<!-- chunk:10 level:2 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Vấn đề 2: Tìm giới hạn của hàm số logarit.

1. PHƯƠNG PHÁP:

Sử dụng các công thức giới hạn:

+ $\forall {x_0} \in {R^ + }$, $\mathop {\lim }\limits_{x \to {x_0}} {\log _a}x = {\log _a}{x_0}$ (với $0 < a \ne 1$).

+ $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (1 + x)}}{x} = 1$ (dùng khi giới hạn có dạng $\frac{0}{0}$ và có chứa logarit).

2. CÁC VÍ DỤ:
Ví dụ: Tìm các giới hạn sau:

a. $\mathop {\lim }\limits_{x \to 8} {\log _2}x.$

b. $\mathop {\lim }\limits_{x \to 0} \log \left| {\frac{{\sin 10x}}{x}} \right|.$

c. $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (1 + \sin 2x)}}{x}.$

a) $\mathop {\lim }\limits_{x \to 8} {\log _2}x = {\log _2}8 = 3.$

b) $\mathop {\lim }\limits_{x \to 0} \log \left| {10.\frac{{\sin 10x}}{{10x}}} \right| = \log 10 = 1.$

c) $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (1 + \sin x)}}{x}$ $= \mathop {\lim }\limits_{x \to 0} \left[ {\frac{{\ln (1 + \sin 2x)}}{{\sin 2x}}.2.\frac{{\sin 2x}}{{2x}}} \right] = 2.$

## Bài tập
## Bài tập 1. Tìm các giới hạn sau:

a. $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (1 + 3x)}}{x}.$

b. $\mathop {\lim }\limits_{x \to 0} \frac{{\ln \left( {1 + {x^2}} \right)}}{x}.$

c. $\mathop {\lim }\limits_{x \to 0} \frac{{\ln (3x + 1) – \ln (2x + 1)}}{x}.$

## Bài tập 2. Tìm các giới hạn sau:

a. $\mathop {\lim }\limits_{x \to 0} \frac{{x\left[ {{e^{\sin 4x}} – \ln e(1 + 3x)} \right]}}{{\ln (\cos 2x)}}.$

b. $\mathop {\lim }\limits_{x \to + \infty } \sin \frac{2}{{x + 1}}\ln \left( {\frac{{x + 5}}{{x + 1}}} \right).$

<!-- chunk:11 level:2 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Vấn đề 3: Tìm đạo hàm của hàm số mũ.
1. PHƯƠNG PHÁP:
Sử dụng các công thức tính đạo hàm:

$\left( {{a^x}} \right)’ = {a^x}.\ln a.$

$\left( {{e^x}} \right)’ = {e^x}.$

$\left[ {{a^{u(x)}}} \right]’ = u'(x).{a^{u(x)}}.\ln a.$

$\left[ {{e^{u(x)}}} \right]’ = u'(x).{e^{u(x)}}.$

2. CÁC VÍ DỤ:

<!-- chunk:12 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 1: Tìm đạo hàm của các hàm số sau:

a. $y = \left( {{x^2} + 1} \right){e^{4x}}.$

b. $y = {e^{\sqrt x \sin \sqrt x }}.$

a. $y = \left( {{x^2} + 1} \right){e^{4x}}.$

$\Rightarrow y’ = \left( {{x^2} + 1} \right)'{e^{4x}} + \left( {{x^2} + 1} \right)\left( {{e^{4x}}} \right)’$ $= 2x{e^{4x}} + \left( {{x^2} + 1} \right)4{e^{4x}}$ $= 2{e^{4x}}\left( {2{x^2} + x + 2} \right).$

b. $y = {e^{\sqrt x \sin x}}.$

$\Rightarrow y’ = \left( {\sqrt x .\sin \sqrt x } \right)'{e^{\sqrt x \sin \sqrt x }}$ $= \left( {\frac{1}{{2\sqrt x }}.\sin \sqrt x + \sqrt x \cos \sqrt x .\frac{1}{{2\sqrt x }}} \right){e^{\sqrt x \sin \sqrt x }}$ $= \frac{1}{{2\sqrt x }}{e^{\sqrt x \sin \sqrt x }}\left( {\sin \sqrt x + \sqrt x \cos \sqrt x } \right).$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 2: Cho hàm số $y = {e^{\sqrt x }} + {e^{ – \sqrt x }}.$ Chứng minh: $4xy” + 2y’ – y = 0.$

Ta có: $y’ = \left( {\sqrt x } \right)'{e^{\sqrt x }} + \left( { – \sqrt x } \right)'{e^{ – \sqrt x }}$ $= \frac{{{e^{\sqrt x }}}}{{2\sqrt x }} – \frac{{{e^{ – \sqrt x }}}}{{2\sqrt x }} = \frac{{{e^{\sqrt x }} – {e^{ – \sqrt x }}}}{{2\sqrt x }}.$

$y” = \frac{{\left( {{e^{\sqrt x }} – {e^{ – \sqrt x }}} \right).2\sqrt x – \left( {{e^{\sqrt x }} – {e^{ – \sqrt x }}} \right)\left( {2\sqrt x } \right)’}}{{4x}}$ $= \frac{{\left( {\frac{1}{{2\sqrt x }}{e^{\sqrt x }} + \frac{1}{{2\sqrt x }}{e^{ – \sqrt x }}} \right).2\sqrt x – \left( {{e^{\sqrt x }} – {e^{ – \sqrt x }}} \right)\left( {2\frac{1}{{2\sqrt x }}} \right)}}{{4x}}$ $= \frac{{\left( {{e^{\sqrt x }} + {e^{ – \sqrt x }}} \right).2\sqrt x – \left( {{e^{\sqrt x }} – {e^{ – \sqrt x }}} \right)(2)}}{{8x\sqrt x }}$ $= \frac{{2\sqrt x .y – 2.2\sqrt x .y’}}{{8x\sqrt x }}$ $= \frac{{y – 2y’}}{{4x}}.$

Suy ra $4xy” = y – 2y’$ hay $4xy” + 2y’ – y = 0.$

## Bài tập
## Bài tập 1. Tìm đạo hàm của các hàm số sau:

a. $y = (x – 1){e^{2x}}.$

b. $y = {x^2}\sqrt {{e^{4x}} + 1} .$

c. $y = \frac{1}{2}\left( {{e^{2x}} – {e^{ – 2x}}} \right).$

d. $y = (x + 1){e^{{x^2}}} + \left( {{x^2} + 1} \right){e^{x + 1}}.$

e. $y = \frac{{{e^x} – {e^{ – x}}}}{{{e^x} + {e^{ – x}}}}.$

f. $y = {2^x} – \sqrt {{e^x}} .$

## Bài tập 2. Tìm đạo hàm cấp $n$ $\left( {n \in {N^*}} \right)$ của các hàm số sau:

a. $y = {a^x}.$

b. $y = {e^{kx}}.$

## Bài tập 3. Cho hàm số $y = x{e^{ – \frac{1}{x}}}.$ Chứng minh rằng: ${x^3}y” – xy’ + y = 0.$

## Bài tập 4. Cho hàm số $y = {e^{4x}} + 2{e^{ – x}}.$ Chứng minh rằng: $y”’ – 13y’ – 12y = 0.$

## Bài tập 5. Cho hàm số $y = {e^{ – x}}.\sin x$ Chứng minh rằng: $y” + 2y’ + 2y = 0.$

<!-- chunk:14 level:2 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Vấn đề 4: Tìm đạo hàm hàm số logarit.

1. PHƯƠNG PHÁP:

Sử dụng các công thức tính đạo hàm:

$(\ln |x|)’ = \frac{1}{x}.$

$(\ln |u|)’ = \frac{{u’}}{u}.$

$\left( {{{\log }_a}|x|} \right)’ = \frac{1}{{x\ln a}}.$

$\left( {{{\log }_a}|u|} \right)’ = \frac{{u’}}{{u\ln a}}.$

2. CÁC VÍ DỤ:

<!-- chunk:15 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 1: Tìm đạo hàm của hàm số sau: $y = \ln \left( {x + \sqrt {{x^2} + 1} } \right).$

Ta có: $y’ = \frac{{\left( {x + \sqrt {{x^2} + 1} } \right)}}{{x + \sqrt {{x^2} + 1} }}$ $= \frac{{1 + \frac{x}{{\sqrt {{x^2} + 1} }}}}{{x + \sqrt {{x^2} + 1} }}$ $= \frac{1}{{\sqrt {{x^2} + 1} }}.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 2: Chứng minh rằng: Nếu $y = (x + 1)\ln (x + 2)$ thì $(x + 1)y’ – (x + 2)y” = x + y – 1.$

Ta có: $y’ = \ln (x + 2) + \frac{{x + 1}}{{x + 2}}.$

$y” = \frac{1}{{x + 2}} + \frac{1}{{{{(x + 2)}^2}}} = \frac{{x + 3}}{{{{(x + 2)}^2}}}.$

Do đó:

$(x + 1)y’$ $= (x + 1)\ln (x + 2) + \frac{{{x^2} + 2x + 1}}{{x + 2}}$ $= y + x + \frac{1}{{x + 2}}.$

$(x + 2)y” = \frac{{x + 3}}{{x + 2}} = 1 + \frac{1}{{x + 2}}.$

Suy ra: $(x + 1)y’ – (x + 2)y” = x + y – 1.$

## Bài tập

## Bài tập 1. Tìm đạo hàm của các hàm số sau:

a. $y = (3x – 2){\ln ^2}(3x – 2).$

b. $y = \sqrt {{x^2} + 1} \ln {x^2}.$

c. $y = x\ln \frac{1}{{1 + x}}.$

d. $y = \frac{{\ln \left( {{x^2} + 1} \right)}}{x}.$

## Bài tập 2. Tìm đạo hàm cấp $n$ của các hàm số sau:

a. $y = \ln x.$

b. $y = x\ln x$ $(n \ge 2).$

## Bài tập 3. Cho hàm số $y = \sin (\ln x) + \cos (\ln x).$ Chứng minh rằng: ${x^2}y” + xy’ + y = 0.$

## Bài tập 4. Cho $y = \ln \frac{1}{{1 + x}}.$ Chứng minh: $xy’ + 1 = {e^y}.$

## Bài tập 5. Cho $y = \frac{1}{{1 + x + \ln x}}.$ Chứng minh: $xy’ = y(y\ln x – 1).$

<!-- chunk:17 level:2 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Vấn đề 5: Tìm tập xác định, chứng minh bất đẳng thức, tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số mũ và hàm số logarit.

1. PHƯƠNG PHÁP:
a) Cần chú ý: ${\log _a}b$ xác định $\Leftrightarrow 0 < a \ne 1$ và $b > 0.$

b) Hàm số mũ $y = {a^x}$ với $0 < a < 1.$

+ Tăng trên $R$ nếu $a > 1.$

+ Giảm trên $R$ nếu $0<a< 1.$

c) Hàm số logarit $y = {\log _a}x$ với $0<a< 1.$

+ Tăng trên $(0; + \infty )$ nếu $a> 1.$

+ Giảm trên $(0; + \infty )$ nếu $0 < a < 1.$

2. CÁC VÍ DỤ:

<!-- chunk:18 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 1: Chứng minh rằng: ${e^x} > 1 + x + \frac{{{x^2}}}{2}$ với mọi $x > 0.$

Xét hàm số: $f(x) = {e^x} – 1 – x – \frac{{{x^2}}}{2}$ trên $[0; + \infty ).$

Ta có:

+ $f$ liên tục trên $[0; + \infty ).$

+ $y'(x) = {e^x} – 1 – x$, $y”(x) = {e^x} – 1.$

Vì $x > 0$ $\Rightarrow {e^x} > 1$ $\Rightarrow f”(x) > 0$ $\Rightarrow f'(x)$ là hàm đồng biến trên $[0; + \infty ).$

Suy ra $f'(x) > f'(0)$ với $x > 0.$

$\Rightarrow f'(x) > 0$ với $x > 0 \Rightarrow f(x)$ đồng biến trên $[0; + \infty ).$

$\Rightarrow f(x) > f(0)$ với mọi $x > 0.$

$\Rightarrow {e^x} – x – \frac{{{x^2}}}{2} – 1 > 0$, $\forall x > 0$ $\Rightarrow {e^x} > \frac{{{x^2}}}{2} + x + 1$, $\forall x > 0.$

<!-- chunk:19 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 2: Tìm giá trị lớn nhất, giá trị nhỏ nhất của hàm số $y = f(x) = {4^x}$ trên đoạn $[2;4].$

Do hàm số $f(x) = {4^x}$ là hàm số mũ với cơ số lớn hơn $1$ nên hàm số luôn đồng biến.

Do đó ta có: $f(2) \le f(x) \le f(4)$ với mọi $x \in [2;4].$

Vì vậy: $\mathop {\max }\limits_{x \in \left[ {2;4} \right]} f(x) = f(4) = 256$ và $\mathop {\min }\limits_{{ _{x \in [2;4]}}} f(x) = f(2) = 16.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 3: Tìm tập xác định của các hàm số:

a) $y = {\log _2}\frac{3}{{10 – x}}.$

b) $y = {\log _{5 – x}}{x^2}.$

c) $y = {\log _3}\frac{{x + 1}}{{\sqrt {{x^2} – x – 2} }}.$

d) $y = \frac{1}{{{{\log }_2}x – 1}}.$

a) $y = {\log _2}\frac{3}{{10 – x}}.$

Hàm số xác định $\Leftrightarrow \frac{3}{{10 – x}} > 0 \Leftrightarrow x < 10.$

Vậy tập xác định của hàm số là $D = ( – \infty ;10).$

b) $y = {\log _{5 – x}}{x^2}.$

Hàm số xác định 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{0 < 5 – x \ne 1}\\
{{x^2} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{4 \ne x < 5}\\
{x \ne 0}
\end{array}} \right..
$$

Vậy tập xác định của hàm số là $D = ( – \infty ;5)\backslash \{ 0;4\} .$

c) $y = {\log _3}\frac{{x + 1}}{{\sqrt {{x^2} – x – 2} }}.$

Hàm số xác định $\Leftrightarrow \frac{{x + 1}}{{\sqrt {{x^2} – x – 2} }} > 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x + 1 > 0}\\
{{x^2} – x – 2 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow x > 2.$

Vậy tập xác định của hàm số là $D = (2; + \infty ).$

d) $y = \frac{1}{{{{\log }_2}x – 1}}.$

Hàm số xác định 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 0}\\
{{{\log }_2}x – 1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x > 0}\\
{x \ne 2}
\end{array}} \right..
$$

Vậy tập xác định của hàm số là $D = (0; + \infty )\backslash \{ 2\} .$

<!-- chunk:21 level:3 source:https://toanmath.com/2019/08/ham-so-mu-va-ham-so-logarit.html -->
## Ví dụ 4: Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x) = (x – 1)\ln x$ trên $\left[ {\frac{1}{e};{e^2}} \right].$

Tập xác định: $D = (0; + \infty )$, $X = \left[ {\frac{1}{e};{e^2}} \right].$

$f'(x) = \ln x + (x – 1)\frac{1}{x}$ $= \frac{{x\ln x + x – 1}}{x}.$

$f'(x) = 0 \Leftrightarrow g(x) = x\ln x + x – 1 = 0$ $(*).$

Ta có:

$g(1) = 0.$

$g'(x) = \ln x + 2.$

Với $x \in \left( {{e^{ – 1}};{e^2}} \right)$ thì $– 1 < \ln x < 2$ nên $g(x) > 0$ với mọi $x \in \left( {{e^{ – 1}};{e^2}} \right).$

Do đó $(*)$ có nghiệm duy nhất là $x = 1.$

Ta có:

$f\left( {{e^2}} \right) = 2\left( {{e^2} – 1} \right).$

$f\left( {{e^{ – 1}}} \right) = – \left( {{e^{ – 1}} – 1} \right).$

$f(1) = 0.$

Do đó:

$\mathop {\max }\limits_x f(x) = f\left( {{e^2}} \right) = 2\left( {{e^2} – 1} \right).$

$\mathop {\min }\limits_x f(x) = f\left( 1 \right) = 0.$

## Bài tập
1.

a. Chứng minh rằng hàm số $y = \frac{{{2^x} – {2^{ – x}}}}{3}$ đồng biến trên $R.$

b. Chứng minh rằng hàm số $y = {\log _{\frac{1}{2}}}x – {\log _{\frac{1}{2}}}(x + 1)$ đồng biến trên $R.$

## Bài tập 2. Tìm giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

a. $f(x) = {3^x} + {2^x}$ trên $[ – 1;1].$

b. $f(x) = {5^{\left| {{x^2} – 2x} \right|}}$ trên $[ – 1;2].$

## Bài tập 3. Cho ${a^\alpha } + {b^\alpha } = {c^\alpha }$ $(a > 0,b > 0,\alpha > 0).$

a. Chứng minh: ${a^m} + {b^m} < {c^m}$ nếu $m > \alpha .$

b. Chứng minh: ${a^m} + {b^m} > {c^m}$ nếu $m < \alpha .$

4. Với điều kiện nào của $a$ thì:

a. ${a^\pi } > \sqrt[3]{{{a^{10}}}}.$

b. ${a^{ – 0.02}} < {a^{\sqrt 3 }}.$

c. ${(a – 1)^{\frac{3}{4}}} > {(a – 1)^{t + \sqrt t + 1}}$ $(t > 0).$

## Bài tập 5. Cho hàm số $f(x) = \frac{{{4^x}}}{{{4^x} + 2}}.$ Tính tổng sau:

$S = f\left( {\frac{1}{{2012}}} \right) + f\left( {\frac{2}{{2012}}} \right)$ $+ f\left( {\frac{3}{{2012}}} \right) + \ldots + f\left( {\frac{{2011}}{{2012}}} \right).$

## Bài tập 6. Tìm tập xác định của các hàm số sau:

a. $y = {\log _3}\left( {{x^2} + 2x} \right).$

b. $y = {\log _{0,7}}\frac{{{x^2} – 9}}{{x + 5}}.$

c. $y = \frac{2}{{{{\log }_4}x – 3}}.$

d. $y = {\log _3}{(2 – x)^2}.$

## Bài tập 7. Tìm giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

a. $y = \ln {x^2}$ $\left( { – e \le x \le – \frac{1}{e}} \right).$

b. $y = \left| {\ln x} \right|.$

c. $y = {\log _2}x – \frac{2}{x}$ $\left( {x \ge \frac{{\sqrt 2 }}{2}} \right).$

d. $y = \frac{{\ln (2x – 3)}}{{2x – 3}}.$

## Bài tập 8. Xét sự biến thiên của các hàm số sau:

a) $y = \sqrt {{x^2} + 1} .\ln {x^2}.$

b) $y = x\ln \left( {\frac{1}{{x + 1}}} \right).$

## Bài tập 9. Chứng minh rằng hàm số $f(x) = \frac{{\ln \left( {{x^2} + 1} \right)}}{x}$ đồng biến trong các khoảng $( – 1;0)$, $(0;1).$

## Bài tập 10. Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số: $y = \frac{{{{\ln }^2}x}}{x}$ trên đoạn $\left[ {1;{e^3}} \right].$

## Bài tập 11. Chứng minh: $x > \ln (1 + x) > x – \frac{{{x^2}}}{2}$ với mọi $x > 0.$

## Bài tập 12. Cho $0 < x < 1$, $0 < y < 1$ và $x < y.$ Chứng minh rằng: $\frac{1}{{y – x}}\left( {\ln \frac{y}{{1 – y}} – \ln \frac{x}{{1 – x}}} \right) > 4.$

## Bài tập 13. Tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số $f(x) = \ln x – \frac{{x + 1}}{x}\ln (x + 1)$ trên $[1;e].$