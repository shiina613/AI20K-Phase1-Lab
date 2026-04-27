# Tìm giới hạn của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp tìm giới hạn của hàm số thông qua các bước giải cụ thể và các ví dụ minh họa có lời giải chi tiết.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Bài toán 1: Tìm $\mathop {\lim }\limits_{x \to {x_0}} f(x)$ biết $f(x)$ xác định tại ${x_0}.$

Phương pháp:

+ Nếu $f(x)$ là hàm số cho bởi một công thức thì giá trị giới hạn bằng $f({x_0}).$

+ Nếu $f(x)$ cho bởi nhiều công thức, khi đó ta sử dụng điều kiện để hàm số có giới hạn (giới hạn trái bằng giới hạn phải).

<!-- chunk:2 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 1. Tìm các giới hạn sau:

1. $\mathop {\lim }\limits_{x \to 0} \frac{{\sin 2x + 3\cos x + x}}{{2x + {{\cos }^2}3x}}.$

2. $\mathop {\lim }\limits_{x \to 2} \frac{{\sqrt {{x^2} + 3} – 2x}}{{\sqrt[3]{{x + 6}} + 2x – 1}}.$

1. Ta có: $\mathop {\lim }\limits_{x \to 0} \frac{{\sin 2x + 3\cos x + x}}{{2x + {{\cos }^2}3x}}$ $= \frac{{\sin 0 + 3\cos 0 + 0}}{{2.0 + {{\cos }^2}0}}$ $= 3.$

2. Ta có: $\mathop {\lim }\limits_{x \to 2} \frac{{\sqrt {{x^2} + 3} – 2x}}{{\sqrt[3]{{x + 6}} + 2x – 1}}$ $= \frac{{\sqrt {{2^2} + 3} – 2.2}}{{\sqrt[3]{{2 + 6}} + 2.2 – 1}}$ $= \frac{{\sqrt 7 – 4}}{5}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 2. Xét xem các hàm số sau có giới hạn tại các điểm chỉ ra hay không? Nếu có hay tìm giới hạn đó?

1. 
$$
f(x) = \left\{ \begin{array}{l}
\frac{{{x^2} + 3x + 1}}{{{x^2} + 2}} \quad {\rm{ khi }} \: x < 1\\
\frac{{3x + 2}}{3} \quad {\rm{ khi }} \: x \ge 1
\end{array} \right.
$$
 khi $x \to 1.$

2. 
$$
f(x) = \left\{ \begin{array}{l}
2{x^2} + 3x + 1\quad {\rm{khi}} \: x \ge 0\\
– {x^2} + 3x + 2\quad {\rm{khi}} \: x < 0
\end{array} \right.
$$
 khi $x \to 0.$

1. Ta có:

$\mathop {\lim }\limits_{x \to {1^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{3x + 2}}{3}$ $= \frac{5}{3}.$

$\mathop {\lim }\limits_{x \to {1^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {1^ – }} \frac{{{x^2} + 3x + 1}}{{{x^2} + 2}} = \frac{5}{3}.$

$\Rightarrow \mathop {\lim }\limits_{x \to {1^ + }} f(x) = \mathop {\lim }\limits_{x \to {1^ – }} f(x) = \frac{5}{3}.$

Vậy $\mathop {\lim }\limits_{x \to 1} f(x) = \frac{5}{3}.$

2. Ta có:

$\mathop {\lim }\limits_{x \to {0^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ + }} (2{x^2} + 3x + 1) = 1.$

$\mathop {\lim }\limits_{x \to {0^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ – }} ( – {x^2} + 3x + 2) = 2.$

$\Rightarrow \mathop {\lim }\limits_{x \to {0^ + }} f(x) \ne \mathop {\lim }\limits_{x \to {0^ – }} f(x).$

Vậy hàm số $f(x)$ không có giới hạn khi $x \to 0.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 3. Tìm $m$ để các hàm số:

1. 
$$
f(x) = \left\{ \begin{array}{l}
\frac{{{x^2} + mx + 2m + 1}}{{x + 1}} \quad {\rm{khi}} \: x \ge 0\\
\frac{{2x + 3m – 1}}{{\sqrt {1 – x} + 2}} \quad {\rm{khi}} \: x < 0
\end{array} \right.
$$
 có giới hạn khi $x \to 0.$

2. 
$$
f(x) = \left\{ \begin{array}{l}
\frac{{{x^2} + x – 2}}{{\sqrt {1 – x} }} + mx + 1 \quad {\rm{khi}} \: x < 1\\
3mx + 2m – 1 \quad {\rm{khi}} \: x \ge 1
\end{array} \right.
$$
 có giới hạn khi $x \to 1.$

1. Ta có:

$\mathop {\lim }\limits_{x \to {0^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ + }} \frac{{{x^2} + mx + 2m + 1}}{{x + 1}}$ $= 2m + 1.$

$\mathop {\lim }\limits_{x \to {0^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ – }} \frac{{2x + 3m – 1}}{{\sqrt {1 – x} + 2}}$ $= \frac{{3m – 1}}{3}.$

Hàm số có giới hạn khi $x \to 0$ khi và chỉ khi $\mathop {\lim }\limits_{x \to {0^ + }} f(x) = \mathop {\lim }\limits_{x \to {0^ – }} f(x)$ $\Leftrightarrow 2m + 1 = \frac{{3m – 1}}{3}$ $\Leftrightarrow m = – \frac{4}{3}.$

2. Ta có:

$\mathop {\lim }\limits_{x \to {1^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {1^ + }} (3mx + 2m – 1)$ $= 5m – 1.$

$\mathop {\lim }\limits_{x \to {1^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {1^ – }} \left( {\frac{{{x^2} + x – 2}}{{\sqrt {1 – x} }} + mx + 1} \right)$ $= \mathop {\lim }\limits_{x \to {1^ – }} \left( { – (x + 2)\sqrt {1 – x} + mx + 1} \right)$ $= m + 1.$

Hàm số có giới hạn khi $x \to 1$ khi và chỉ khi $\mathop {\lim }\limits_{x \to {1^ + }} f(x) = \mathop {\lim }\limits_{x \to {1^ – }} f(x)$ $\Leftrightarrow 5m – 1 = m + 1$ $\Leftrightarrow m = \frac{1}{2}.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Bài toán 2: Tìm $\mathop {\lim }\limits_{x \to {x_0}} \frac{{f(x)}}{{g(x)}}$ trong đó $f({x_0}) = g({x_0}) = 0$ (dạng vô định $\frac{0}{0}$).

Để khử dạng vô định $\frac{0}{0}$ ta sử dụng định lí Bơzu (Bézout) cho đa thức: Nếu đa thức $f(x)$ có nghiệm $x = {x_0}$ thì ta có: $f(x) = (x – {x_0}){f_1}(x).$

+ Nếu $f(x)$ và $g(x)$ là các đa thức thì ta phân tích $f(x) = (x – {x_0}){f_1}(x)$ và $g(x) = (x – {x_0}){g_1}(x).$ Khi đó $\mathop {\lim }\limits_{x \to {x_0}} \frac{{f(x)}}{{g(x)}}$ $= \mathop {\lim }\limits_{x \to {x_0}} \frac{{{f_1}(x)}}{{{g_1}(x)}}$, nếu giới hạn này có dạng $\frac{0}{0}$ thì ta tiếp tục quá trình như trên.

Chú ý: Nếu tam thức bậc hai $a{x^2} + b{\rm{x + c}}$ có hai nghiệm ${x_1},{x_2}$ thì ta luôn có sự phân tích: $a{x^2} + bx + c$ $= a(x – {x_1})(x – {x_2}).$

+ Nếu $f(x)$ và $g(x)$ là các hàm chứa căn thức thì ta nhân lượng liên hợp để chuyển về các đa thức, rồi phân tích các đa thức như trên.

Các lượng liên hợp:

$(\sqrt a – \sqrt b )(\sqrt a + \sqrt b )$ $= a – b.$

$(\sqrt[3]{a} \pm \sqrt[3]{b})(\sqrt[3]{{{a^2}}} \mp \sqrt[3]{{ab}} + \sqrt[3]{{{b^2}}})$ $= a – b.$

$(\sqrt[n]{a} – \sqrt[n]{b})(\sqrt[n]{{{a^{n – 1}}}} + \sqrt[n]{{{a^{n – 2}}b}} + … + \sqrt[n]{{{b^{n – 1}}}})$ $= a – b.$

+ Nếu $f(x)$ và $g(x)$ là các hàm chứa căn thức không đồng bậc ta sử dụng phương pháp tách, chẳng hạn:

Nếu $\sqrt[n]{{u(x)}},\sqrt[m]{{v(x)}} \to c$ thì ta phân tích: $\sqrt[n]{{u(x)}} – \sqrt[m]{{v(x)}}$ $= (\sqrt[n]{{u(x)}} – c) – (\sqrt[m]{{v(x)}} – c).$

Trong nhiều trường hợp việc phân tích như trên không đi đến kết quả ta phải phân tích như sau: $\sqrt[n]{{u(x)}} – \sqrt[m]{{v(x)}}$ $= (\sqrt[n]{{u(x)}} – m(x))$ $– (\sqrt[m]{{v(x)}} – m(x))$, trong đó $m(x) \to c.$

+ Một đẳng thức cần lưu ý: ${a^n} – {b^n}$ $= (a – b)({a^{n – 1}} + {a^{n – 2}}b + … + a{b^{n – 2}} + {b^{n – 1}}).$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 4. Tìm các giới hạn sau:

1. $A = \mathop {\lim }\limits_{x \to 1} \frac{{{x^n} – 1}}{{x – 1}}.$

2. $B = \mathop {\lim }\limits_{x \to 1} \frac{{{x^5} – 5{x^3} + 2{x^2} + 6x – 4}}{{{x^3} – {x^2} – x + 1}}.$

1. Ta có: ${x^n} – 1$ $= (x – 1)$ $({x^{n – 1}} + {x^{n – 2}} + … + x + 1).$

Suy ra: $\frac{{{x^n} – 1}}{{x – 1}}$ $= {x^{n – 1}} + {x^{n – 2}} + … + x + 1.$

Do đó: $A = \mathop {\lim }\limits_{x \to 1} \left( {{x^{n – 1}} + {x^{n – 2}} + … + x + 1} \right)$ $= n.$

2. Ta có:

${x^5} – 5{x^3} + 2{x^2} + 6x – 4$ $= {(x – 1)^2}(x + 2)({x^2} – 2).$

${x^3} – {x^2} – x + 1$ $= {(x – 1)^2}(x + 1).$

Do đó: $B = \mathop {\lim }\limits_{x \to 1} \frac{{(x + 2)({x^2} – 2)}}{{x + 1}}$ $= – \frac{3}{2}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 5. Tìm các giới hạn sau:

1. $C = \mathop {\lim }\limits_{x \to 0} \frac{{{{(1 + mx)}^n} – {{(1 + nx)}^m}}}{{{x^2}}}.$

2. $D = \mathop {\lim }\limits_{x \to 0} \frac{{{{(1 + 2x)}^2}{{(1 + 3x)}^3} – 1}}{x}.$

1. Ta có:

${(1 + mx)^n}$ $= 1 + mnx$ $+ \frac{{{m^2}n(n – 1){x^2}}}{2}$ $+ {m^3}{x^3}A$, với $A = C_n^3 + mxC_n^4$ $+ … + {\left( {mx} \right)^{n – 3}}C_n^n.$

${\left( {1 + nx} \right)^m}$ $= 1 + mnx$ $+ \frac{{{n^2}m(m – 1){x^2}}}{2}$ $+ {n^3}{x^3}B$, với $B = C_m^3 + nxC_m^4$ $+ … + {\left( {nx} \right)^{m – 3}}C_m^m.$

Do đó: $C = \mathop {\lim }\limits_{x \to 0} [\frac{{{m^2}n(n – 1) – {n^2}m(m – 1)}}{2}$ $+ x\left( {{m^3}A – {n^3}B} \right)]$ $= \frac{{{m^2}n(n – 1) – {n^2}m(m – 1)}}{2}$ $= \frac{{mn(n – m)}}{2}.$

Ta có: $\frac{{{{\left( {1 + 2x} \right)}^2}{{\left( {1 + 3x} \right)}^3} – 1}}{x}$ $= \frac{{\left( {1 + 2{x^2}} \right)\left[ {{{\left( {1 + 3x} \right)}^3} – 1} \right]}}{x}$ $+ \frac{{{{(1 + 2x)}^2} – 1}}{x}$ $= {\left( {1 + 2x} \right)^2}$ $\left( {9 + 27x + 27{x^2}} \right)$ $– (4 + 4x).$

Suy ra: $D = \mathop {\lim }\limits_{x \to 0} [{\left( {1 + 2x} \right)^2}$ $\left( {9 + 27x + 27{x^2}} \right)$ $– (4 + 4x)]$ $= 5.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 6. Tìm các giới hạn sau:

1. $A = \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt {2x – 1} – x}}{{{x^2} – 1}}.$

2. $B = \mathop {\lim }\limits_{x \to 2} \frac{{\sqrt[3]{{3x + 2}} – x}}{{\sqrt {3x – 2} – 2}}.$

1. Ta có: $A =$ $\mathop {\lim }\limits_{x \to 1} \frac{{2x – 1 – {x^2}}}{{(x – 1)(x + 1)(\sqrt {2x – 1} + x)}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{ – (x – 1)}}{{(x + 1)(\sqrt {2x – 1} + x)}}$ $= 0.$

2. Ta có: $B =$ $\mathop {\lim }\limits_{x \to 2} \frac{{(3x + 2 – {x^3})(\sqrt {3x – 2} + 2)}}{{3(x – 2)(\sqrt[3]{{{{(3x + 2)}^2}}} + 2\sqrt[3]{{3x + 2}} + 4)}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{ – ({x^2} + 2x + 1)(\sqrt {3x – 2} + 2)}}{{3(\sqrt[3]{{{{(3x + 2)}^2}}} + 2\sqrt[3]{{3x + 2}} + 4)}}$ $= – 1.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 7. Tìm các giới hạn sau:

1. $C = \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{2x – 1}} – 1}}{{x – 1}}.$

2. $D =$ $\mathop {\lim }\limits_{x \to 1} \frac{{\sqrt {2x – 1} .\sqrt[3]{{3x – 2}}.\sqrt[4]{{4x – 3}} – 1}}{{x – 1}}.$

1. Đặt $t = x – 1$ ta có: $C = \mathop {\lim }\limits_{t \to 0} \frac{{\sqrt[3]{{2t + 1}} – 1}}{t} = \frac{2}{3}.$

2. Ta có: $\sqrt {2x – 1} .\sqrt[3]{{3x – 2}}.\sqrt[4]{{4x – 3}} – 1$ $= \sqrt {2x – 1} .\sqrt[3]{{3x – 2}}\left( {\sqrt[4]{{4x – 3}} – 1} \right)$ $+ \sqrt {2x – 1} \left( {\sqrt[3]{{3x – 2}} – 1} \right)$ $+ \sqrt {2x – 1} – 1.$

Mà: $\mathop {\lim }\limits_{x \to 1} \frac{{\sqrt {2x – 1} – 1}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{3x – 2}} – 1}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[4]{{4x – 3}} – 1}}{{x – 1}} = 1.$

Nên ta có: $D = 1 + 1 + 1 = 3.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 8. Tìm các giới hạn sau:

1. $A = \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{7x + 1}} – \sqrt {5x – 1} }}{{x – 1}}.$

2. $B = \mathop {\lim }\limits_{x \to 7} \frac{{\sqrt {x + 2} – \sqrt[3]{{x + 20}}}}{{\sqrt[4]{{x + 9}} – 2}}.$

1. Ta có: $A =$ $\mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{7x + 1}} – 2 – (\sqrt {5x – 1} – 2)}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{7x + 1}} – 2}}{{x – 1}}$ $– \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt {5x – 1} – 2}}{{x – 1}}$ $= I – J.$

$I =$ $\mathop {\lim }\limits_{x \to 1} \frac{{7(x – 1)}}{{(x – 1)(\sqrt[3]{{{{(7x – 1)}^2}}} + 2\sqrt[3]{{7x – 1}} + 4)}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{7}{{\sqrt[3]{{{{(7x – 1)}^2}}} + 2\sqrt[3]{{7x – 1}} + 4}}$ $= \frac{7}{{12}}.$

$J = \mathop {\lim }\limits_{x \to 1} \frac{{5(x – 1)}}{{(x – 1)(\sqrt {5x – 1} + 1)}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{5}{{\sqrt {5x – 1} + 1}} = \frac{5}{3}.$

Vậy $A = – \frac{2}{3}.$

2. Ta có: $B = \mathop {\lim }\limits_{x \to 7} \frac{{\sqrt {x + 2} – \sqrt[3]{{x + 20}}}}{{\sqrt[4]{{x + 9}} – 2}}$ $= \mathop {\lim }\limits_{x \to 7} \frac{{\frac{{\sqrt {x + 2} – 3}}{{x – 7}} – \frac{{\sqrt[3]{{x + 20}} – 3}}{{x – 7}}}}{{\frac{{\sqrt[4]{{x + 9}} – 2}}{{x – 7}}}}.$

Mà:

$\mathop {\lim }\limits_{x \to 7} \frac{{\sqrt {x + 2} – 3}}{{x – 7}}$ $= \mathop {\lim }\limits_{x \to 7} \frac{1}{{\sqrt {x + 2} + 3}}$ $= \frac{1}{6}.$

$\mathop {\lim }\limits_{x \to 7} \frac{{\sqrt[3]{{x + 20}} – 3}}{{x – 7}}$ $= \mathop {\lim }\limits_{x \to 7} \frac{1}{{{{(\sqrt[3]{{x + 20}})}^2} + 3\sqrt[3]{{x + 20}} + 9}}$ $= \frac{1}{{27}}.$

$\mathop {\lim }\limits_{x \to 7} \frac{{\sqrt[4]{{x + 9}} – 2}}{{x – 7}}$ $= \mathop {\lim }\limits_{x \to 7} \frac{1}{{{{(\sqrt[4]{{x + 9}})}^3} + 2{{(\sqrt[4]{{x + 9}})}^2} + 4\sqrt[4]{{x + 9}} + 8}}$ $= \frac{1}{{32}}.$

Vậy $B = \frac{{\frac{1}{6} – \frac{1}{{27}}}}{{\frac{1}{{32}}}} = \frac{{112}}{{27}}.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Bài toán 3: Tìm $\mathop {\lim }\limits_{x \to \pm \infty } \frac{{f(x)}}{{g(x)}}$, trong đó $f(x),g(x) \to \infty$ (dạng vô định $\frac{\infty }{\infty }$).

Phương pháp: Ta cần tìm cách đưa về các giới hạn:

$\mathop {\lim }\limits_{x \to \pm \infty } {x^{2k}} = + \infty .$

$\mathop {\lim }\limits_{x \to + \infty } {x^{2k + 1}} = + \infty .$

$\mathop {\lim }\limits_{x \to – \infty } {x^{2k + 1}} = – \infty .$

$\mathop {\lim }\limits_{x \to \pm \infty } \frac{k}{{{x^n}}} = 0\left( {n > 0;k \ne 0} \right).$

$\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right) = \pm \infty$ $\Leftrightarrow \mathop {\lim }\limits_{x \to {x_0}} \frac{k}{{f\left( x \right)}} = 0\left( {k \ne 0} \right).$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 9. Tìm các giới hạn sau:

1. $A = \mathop {\lim }\limits_{x \to + \infty } \frac{{{{(4x + 1)}^3}{{(2x + 1)}^4}}}{{{{(3 + 2x)}^7}}}.$

2. $B = \mathop {\lim }\limits_{x \to – \infty } \frac{{\sqrt {4{x^2} – 3x + 4} + 3x}}{{\sqrt {{x^2} + x + 1} – x}}.$

1. Ta có: $A =$ $\mathop {\lim }\limits_{x \to + \infty } \frac{{{{\left( {4 + \frac{1}{x}} \right)}^3}{{\left( {2 + \frac{1}{x}} \right)}^4}}}{{{{\left( {\frac{3}{x} + 2} \right)}^7}}}$ $= 8.$

2. Ta có: $B =$ $\mathop {\lim }\limits_{x \to – \infty } \frac{{ – \sqrt {4 – \frac{3}{x} + \frac{4}{{{x^2}}}} + 3}}{{ – \sqrt {1 + \frac{1}{x} + \frac{1}{{{x^2}}}} – 1}}$ $= \frac{1}{2}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 10. Tìm các giới hạn sau:

1. $A =$ $\mathop {\lim }\limits_{x \to + \infty } \frac{{\sqrt {2{x^2} + 1} – \sqrt {{x^2} + 1} }}{{2x + 2}}.$

2. $B =$ $\mathop {\lim }\limits_{x \to – \infty } \frac{{\sqrt {3{x^2} – 2} + \sqrt {x + 1} }}{{\sqrt {{x^2} + 1} – 1}}.$

1. Ta có: $A =$ $\mathop {\lim }\limits_{x \to + \infty } \frac{{\left| x \right|\sqrt {2 + \frac{1}{{{x^2}}}} – \left| x \right|\sqrt {1 + \frac{1}{{{x^2}}}} }}{{x(2 + \frac{2}{x})}}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{\sqrt {2 + \frac{1}{{{x^2}}}} – \sqrt {1 + \frac{1}{{{x^2}}}} }}{{2 + \frac{2}{x}}}$ $= \frac{{\sqrt 2 – 1}}{2}.$

2. Ta có: $B =$ $\mathop {\lim }\limits_{x \to – \infty } \frac{{\left| x \right|\sqrt {3 – \frac{2}{{{x^2}}}} + \left| x \right|\sqrt {\frac{1}{x} + \frac{1}{{{x^2}}}} }}{{\left| x \right|\left( {\sqrt {1 + \frac{1}{{{x^2}}}} – \frac{1}{{\left| x \right|}}} \right)}}$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{ – \sqrt {3 – \frac{2}{{{x^2}}}} – \sqrt {\frac{1}{x} + \frac{1}{{{x^2}}}} }}{{ – \left( {\sqrt {1 + \frac{1}{{{x^2}}}} – \frac{1}{{\left| x \right|}}} \right)}}$ $= \sqrt 3 .$

<!-- chunk:14 level:2 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Bài toán 4: Dạng vô định $\infty – \infty$ và $0.\infty .$

Phương pháp: Những dạng vô định này ta tìm cách biến đổi đưa về dạng $\frac{\infty }{\infty }.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 11. Tìm các giới hạn sau: $A =$ $\mathop {\lim }\limits_{x \to – \infty } (\sqrt[3]{{{x^3} – 3{x^2}}} + \sqrt {{x^2} – 2x} ).$

Ta có: $\sqrt[3]{{{x^3} – 3{x^2}}} + \sqrt {{x^2} – 2x}$ $= (\sqrt[3]{{{x^3} – 3{x^2}}} – x)$ $+ (\sqrt {{x^2} – 2x} + x)$ $= \frac{{ – 3{x^2}}}{{\sqrt[3]{{{{({x^3} – 3{x^2})}^2}}} + x\sqrt[3]{{{x^3} – 3{x^2}}} + {x^2}}}$ $+ \frac{{ – 2x}}{{\sqrt {{x^2} – 2x} – x}}.$

$\Rightarrow A =$ $\mathop {\lim }\limits_{x \to – \infty } \frac{{ – 3}}{{\sqrt[3]{{{{(1 – \frac{3}{x})}^2}}} + \sqrt[3]{{1 – \frac{3}{x}}} + 1}}$ $+ \mathop {\lim }\limits_{x \to – \infty } \frac{{ – 2}}{{ – \sqrt {1 – \frac{2}{x}} – 1}}$ $= 0.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 12. Tìm các giới hạn sau: $B =$ $\mathop {\lim }\limits_{x \to + \infty } x(\sqrt {{x^2} + 2x} – 2\sqrt {{x^2} + x} + x).$

Ta có: $\sqrt {{x^2} + 2x} – 2\sqrt {{x^2} + x} + x$ $= \frac{{2{x^2} + 2x + 2x\sqrt {{x^2} + 2x} – 4{x^2} – 4x}}{{\sqrt {{x^2} + 2x} + 2\sqrt {{x^2} + x} + x}}$ $= 2x\frac{{\sqrt {{x^2} + 2x} – x – 1}}{{\sqrt {{x^2} + 2x} + 2\sqrt {{x^2} + x} + x}}$ $= \frac{{ – 2x}}{{(\sqrt {{x^2} + 2x} + 2\sqrt {{x^2} + x} + x)(\sqrt {{x^2} + 2x} + x + 1)}}.$

$\Rightarrow B =$ $\mathop {\lim }\limits_{x \to + \infty } \frac{{ – 2{x^2}}}{{(\sqrt {{x^2} + 2x} + 2\sqrt {{x^2} + x} + x)(\sqrt {{x^2} + 2x} + x + 1)}}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{ – 2}}{{(\sqrt {1 + \frac{2}{x}} + 2\sqrt {1 + \frac{1}{x}} + 1)(\sqrt {1 + \frac{2}{x}} + 1 + \frac{1}{x})}}$ $= – \frac{1}{4}.$

<!-- chunk:17 level:2 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Bài toán 5: Dạng vô định các hàm lượng giác.

Phương pháp: Ta sử dụng các công thức lượng giác biến đổi về các dạng sau:

+ $\mathop {\lim }\limits_{x \to 0} \frac{{\sin x}}{x}$ $= \mathop {\lim }\limits_{x \to 0} \frac{x}{{\sin x}}$ $= 1$, từ đó suy ra $\mathop {\lim }\limits_{x \to 0} \frac{{\tan x}}{x}$ $= \mathop {\lim }\limits_{x \to 0} \frac{x}{{\tan x}}$ $= 1.$

+ Nếu $\mathop {\lim }\limits_{x \to {x_0}} u(x) = 0$ $\Rightarrow \mathop {\lim }\limits_{x \to {x_0}} \frac{{\sin u(x)}}{{u(x)}} = 1$ và $\mathop {\lim }\limits_{x \to {x_0}} \frac{{\tan u(x)}}{{u(x)}} = 1.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 13. Tìm các giới hạn sau:

1. $A =$ $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {\cos x} – \sqrt[3]{{\cos x}}}}{{{{\sin }^2}x}}.$

2. $B =$ $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {1 + 2x} – \sqrt[3]{{1 + 3x}}}}{{1 – \sqrt {\cos 2x} }}.$

1. Ta có: $A =$ $\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {\cos x} – 1}}{{{x^2}}}\frac{{{x^2}}}{{{{\sin }^2}x}}$ $+ \mathop {\lim }\limits_{x \to 0} \frac{{1 – \sqrt[3]{{\cos x}}}}{{{x^2}}}.\frac{{{x^2}}}{{{{\sin }^2}x}}.$

Mà:

$\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {\cos x} – 1}}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{\cos x – 1}}{{{x^2}}}.\frac{1}{{\sqrt {\cos x} + 1}}$ $= – \frac{1}{4}.$

$\mathop {\lim }\limits_{x \to 0} \frac{{1 – \sqrt[3]{{\cos x}}}}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{1 – \cos x}}{{{x^2}}}.\frac{1}{{\sqrt[3]{{{{\cos }^2}x}} + \sqrt[3]{{\cos x}} + 1}}$ $= \frac{1}{6}.$

Do đó: $A = – \frac{1}{4} + \frac{1}{6} = – \frac{1}{{12}}.$

2. Ta có: $B =$ $\mathop {\lim }\limits_{x \to 0} \frac{{\frac{{\sqrt {1 + 2x} – \sqrt[3]{{1 + 3x}}}}{{{x^2}}}}}{{\frac{{1 – \sqrt {\cos 2x} }}{{{x^2}}}}}.$

Mà:

$\mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {1 + 2x} – \sqrt[3]{{1 + 3x}}}}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{\sqrt {1 + 2x} – (1 + x)}}{{{x^2}}}$ $+ \mathop {\lim }\limits_{x \to 0} \frac{{(x + 1) – \sqrt[3]{{1 + 3x}}}}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{ – 1}}{{\sqrt {1 + 2x} + x + 1}}$ $+ \mathop {\lim }\limits_{x \to 0} \frac{{x + 3}}{{{{(x + 1)}^2} + (x + 1)\sqrt[3]{{1 + 3x}} + \sqrt[3]{{{{\left( {1 + 3x} \right)}^2}}}}}$ $= – \frac{1}{2} + 1 = \frac{1}{2}.$

$\mathop {\lim }\limits_{x \to 0} \frac{{1 – \sqrt {\cos 2x} }}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{1 – \cos 2x}}{{{x^2}}}.\frac{1}{{1 + \sqrt {\cos 2x} }}$ $= 1.$

Vậy $B = \frac{1}{2}.$

<!-- chunk:19 level:3 source:https://toanmath.com/2018/07/tim-gioi-han-cua-ham-so.html -->
## Ví dụ 14. Tìm các giới hạn sau:

1. $A = \mathop {\lim }\limits_{x \to 0} {x^3}\sin \frac{1}{{{x^2}}}.$

2. $B =$ $\mathop {\lim }\limits_{x \to + \infty } \left( {2\sin x + {{\cos }^3}x} \right)\left( {\sqrt {x + 1} – \sqrt x } \right).$

1. Ta có: $0 \le \left| {{x^3}\sin \frac{1}{{{x^2}}}} \right| \le {x^3}.$

Mà $\mathop {\lim }\limits_{x \to 0} {x^3} = 0$ $\Rightarrow \mathop {\lim }\limits_{x \to 0} \left| {{x^3}\sin \frac{1}{{{x^2}}}} \right| = 0$ $\Rightarrow \mathop {\lim }\limits_{x \to 0} {x^3}\sin \frac{1}{{{x^2}}} = 0.$

Vậy $A = 0.$

2. Ta có: $B = \mathop {\lim }\limits_{x \to + \infty } \frac{{2\sin x + {{\cos }^3}x}}{{\sqrt {x + 1} + \sqrt x }}.$

Mà $0 \le \left| {\frac{{2\sin x + {{\cos }^2}x}}{{\sqrt {x + 1} + \sqrt x }}} \right|$ $\le \frac{3}{{\sqrt {x + 1} + \sqrt x }} \to 0$ khi $x \to + \infty .$

Do đó: $B = 0.$