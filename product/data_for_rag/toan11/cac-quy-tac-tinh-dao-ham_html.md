# Các quy tắc tính đạo hàm

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
Bài viết trình bày các quy tắc tính đạo hàm, giúp việc tính đạo hàm của một hàm số phức tạp trở nên dễ dàng hơn bằng cách quy về tính đạo hàm của các hàm số đơn giản.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## I. Kiến thức cần nắm:

1. Quy tắc tính đạo hàm:
a. Đạo hàm của tổng, hiệu, tích, thương các hàm số:

• $({u_1} \pm {u_2} \pm … \pm {u_n})’$ $= {u_1}’ \pm {u_2}’ \pm … \pm {u_n}’.$

• $(k.u(x))’ = k.u'(x).$

• $(uv)’ = u’v + uv’.$

• $(uvw)’ = u’vw + uv’w + uvw’.$

• $({u^n}(x))’ = n{u^{n – 1}}(x).u'(x).$

• $\left( {\frac{c}{{u(x)}}} \right)’ = – \frac{{c.u'(x)}}{{{u^2}(x)}}.$

• ${\left( {\frac{{u(x)}}{{v(x)}}} \right)}’$ $= \frac{{u'(x)v(x) – v'(x)u(x)}}{{{v^2}(x)}}.$

b. Đạo hàm của hàm số hợp: Cho hàm số $y = f(u(x)) = f(u)$ với $u = u(x).$ Khi đó: $y{‘_x} = y{‘_u}.u{‘_x}.$

2. Bảng công thức đạo hàm các hàm sơ cấp cơ bản:

**Đạo hàm** | 
**Hàm hợp** | 

\[(c)’ = 0\] | 
 | 

\[(x)’ = 1\] | 
 | 

\[({x^\alpha })’ = \alpha {x^{\alpha – 1}}\] | 
\[\left( {{u^\alpha }} \right)’ = \alpha {u^{\alpha – 1}}.u’\] | 

\[\left( {\sqrt x } \right)’ = \frac{1}{{2\sqrt x }}\] | 
\[\left( {\sqrt u } \right)’ = \frac{{u’}}{{2\sqrt u }}\] | 

\[\left( {\sqrt[n]{x}} \right)’ = \frac{1}{{n\sqrt[n]{{{x^{n – 1}}}}}}\] | 
\[\left( {\sqrt[n]{u}} \right)’ = \frac{{u’}}{{n\sqrt[n]{{{u^{n – 1}}}}}}\] | 

\[(\sin x)’ = \cos x\] | 
\[(\sin u)’ = u’.\cos u\] | 

\[(\cos x)’ = – \sin x\] | 
\[(\cos u)’ = – u’\sin u\] | 

\[(\tan x)’ = \frac{1}{{{{\cos }^2}x}}\] | 
\[\left( {\tan u} \right)’ = \frac{{u’}}{{{{\cos }^2}u}}\] | 

\[(\cot x)’ = – \frac{1}{{{{\sin }^2}x}}\] | 
\[\left( {\cot u} \right)’ = – \frac{{u’}}{{{{\sin }^2}u}}\] |

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 1. Tính đạo hàm các hàm số sau:

a. $y = {x^3} – 3{x^2} + 2x + 1.$

b. $y = – {x^3} + 3x + 1.$

c. $y = \frac{{{x^4}}}{4} – {x^2} + 1.$

d. $y = – 2{x^4} + \frac{3}{2}{x^2} + 1.$

e. $y = \frac{{2x + 1}}{{x – 3}}.$

f. $y = \frac{{{x^2} – 2x + 2}}{{x + 1}}.$

a. $y’ = {\left( {{x^3} – 3{x^2} + 2x + 1} \right)’}$ $= 3{x^2} – 6x + 2.$

b. $y’ = {\left( { – {x^3} + 3x + 1} \right)’}$ $= – 3{x^2} + 3.$

c. $y’ = {\left( {\frac{{{x^4}}}{4} – {x^2} + 1} \right)’}$ $= {x^3} – 2x.$

d. $y’ = {\left( { – 2{x^4} + \frac{3}{2}{x^2} + 1} \right)’}$ $= – 8{x^3} + 3x.$

e. $y’ =$ $\frac{{(2x + 1)'(x – 3) – (x – 3)'(2x + 1)}}{{{{(x – 3)}^2}}}$ $= \frac{{ – 7}}{{{{(x – 3)}^2}}}.$

f. $y’ =$ $\frac{{({x^2} – 2x + 2)'(x + 1) – ({x^2} – 2x + 2)(x + 1)’}}{{{{(x + 1)}^2}}}$ $= \frac{{(2x – 2)(x + 1) – ({x^2} – 2x + 2)}}{{{{(x + 1)}^2}}}$ $= \frac{{{x^2} + 2x – 4}}{{{{\left( {x + 1} \right)}^2}}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 2. Tính đạo hàm các hàm số sau:

a. $y = {\left( {{x^7} + x} \right)^2}.$

b. $y = \left( {{x^2} + 1} \right)\left( {5 – 3{x^2}} \right).$

c. $y = {x^2}\left( {2x + 1} \right)\left( {5x – 3} \right).$

d. $y = {\left( {4x + \frac{5}{{{x^2}}}} \right)^3}.$

e. $y = {(x + 2)^3}{(x + 3)^2}.$

a. $y’ = 2({x^7} + x)({x^7} + x)’$ $= 2({x^7} + x)(7{x^6} + 1).$

b. Ta có: $y = \left( {{x^2} + 1} \right)\left( {5 – 3{x^2}} \right)$ $= – 3{x^4} + 2{x^2} + 5$ $\Rightarrow y’ = – 12{x^3} + 4x.$

c. Ta có: $y = {x^2}\left( {2x + 1} \right)\left( {5x – 3} \right)$ $= 10{x^4} – {x^3} – 3{x^2}$ $\Rightarrow y’ = 40{x^3} – 3{x^2} – 6x.$

d. $y’ = 3{\left( {4x + \frac{5}{{{x^2}}}} \right)^2}\left( {4x + \frac{5}{{{x^2}}}} \right)’$ $= 3{\left( {4x + \frac{5}{{{x^2}}}} \right)^2}\left( {4 – \frac{{10}}{{{x^3}}}} \right).$

e. $y’ = 3{({x^2} + 5x + 6)^2} + 2(x + 3){(x + 2)^3}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 3. Giải bất phương trình $f'(x) \ge 0$, biết:

a. $f(x) = x\sqrt {4 – {x^2}} .$

b. $f(x) = x – 2\sqrt {{x^2} + 12} .$

c. $f(x) = \sqrt[4]{{{x^2} + 1}} – \sqrt x .$

a. Tập xác định: $D = \left[ { – 2;2} \right].$

Ta có: $f'(x) = \sqrt {4 – {x^2}} – \frac{{{x^2}}}{{\sqrt {4 – {x^2}} }}$ $= \frac{{4 – 2{x^2}}}{{\sqrt {4 – {x^2}} }}.$

Do đó: $f'(x) \ge 0$ $\Leftrightarrow 4 – 2{x^2} \ge 0$ $\Leftrightarrow – \sqrt 2 \le x \le \sqrt 2 .$

b. Tập xác định: $D = R.$

Ta có: $f'(x) = 1 – \frac{{2x}}{{\sqrt {{x^2} + 12} }}$ $= \frac{{\sqrt {{x^2} + 12} – 2x}}{{\sqrt {{x^2} + 12} }}.$

Suy ra: $f'(x) \ge 0$ $\Leftrightarrow \sqrt {{x^2} + 12} \ge 2x$ $(1).$

• Với $x < 0$ thì $(1)$ luôn đúng.

• Với $x \ge 0$ thì 
$$
(1) \Leftrightarrow \left\{ \begin{array}{l}
x \ge 0\\
{x^2} + 12 \ge 4{x^2}
\end{array} \right.
$$
 $\Leftrightarrow 0 \le x \le 2.$

Vậy bất phương trình $f'(x) \ge 0$ có nghiệm khi và chỉ khi $x \le 2.$

c. Tập xác định: $D = \left[ {0; + \infty } \right).$

Ta có: $f'(x) = \frac{x}{{2\sqrt[4]{{{{({x^2} + 1)}^3}}}}} – \frac{1}{{2\sqrt x }}.$

$f'(x) \ge 0$ $\Leftrightarrow x\sqrt x \ge \sqrt[4]{{{{({x^2} + 1)}^3}}}$ $\Leftrightarrow {x^6} \ge {({x^2} + 1)^3}$ $\Leftrightarrow {x^2} \ge {x^2} + 1$, bất phương trình này vô nghiệm.

[ads]

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 4. Tính đạo hàm các hàm số sau:

a. $y = \sqrt {2{x^2} + 3x + 1} .$

b. $y = \sqrt[5]{{\sqrt {2{x^2} + 1} + 3x + 2}}.$

c. $y = \sqrt {2{{\sin }^2}(2x – 1) + \cos \sqrt x } .$

d. $y = \tan ({\sin ^2}3x) + \sqrt {{{\cot }^2}(1 – 2{x^3}) + 3} .$

e. $y = \sqrt[3]{{\sin (\tan x) + \cos (\cot x)}}.$

a. $y’ = \frac{{(2{x^2} + 3x + 1)’}}{{2\sqrt {2{x^2} + 3x + 1} }}$ $= \frac{{4x + 3}}{{2\sqrt {2{x^2} + 3x + 1} }}.$

b. $y’ = \frac{1}{{5.\sqrt[5]{{{{(\sqrt {2{x^2} + 1} + 3x + 2)}^4}}}}}$$(\sqrt {2{x^2} + 1} + 3x + 2)’$ $= \frac{1}{{5.\sqrt[5]{{{{(\sqrt {2{x^2} + 1} + 3x + 2)}^4}}}}}$$(\frac{{2x}}{{\sqrt {2{x^2} + 1} }} + 3).$

c. $y’ = \frac{{(2{{\sin }^2}(2x – 1) + \cos \sqrt x )’}}{{2\sqrt {2{{\sin }^2}(2x – 1) + \cos \sqrt x } }}$ $= \frac{{2\sin (4x – 2) – \frac{1}{{2\sqrt x }}\sin \sqrt x }}{{2\sqrt {2{{\sin }^2}(2x – 1) + \cos \sqrt x } }}$ $= \frac{{4\sqrt x \sin (4x – 2) – \sin \sqrt x }}{{4\sqrt {2x{{\sin }^2}(2x – 1) + x\cos \sqrt x } }}.$

d. $y’ = [1 + {\tan ^2}({\sin ^2}3x)]({\sin ^2}3x)’$ $+ \frac{{[{{\cot }^2}(1 – 2{x^3}) + 3]’}}{{2\sqrt {{{\cot }^2}(1 – 2{x^3}) + 3} }}$ $= 3 [1 + {\tan ^2}({\sin ^2}3x)]\sin 6x$ $+ \frac{{6{x^2}{\rm{[}}1 + {{\cot }^2}(1 – 2{x^3}){\rm{]}}\cot (1 – 2{x^3})}}{{\sqrt {{{\cot }^2}(1 – 2{x^3}) + 3} }}.$

e. $y’ = \frac{{[\sin (\tan x) + \cos (\cot x)]’}}{{3\sqrt {{{[\sin (\tan x) + \cos (\cot x)]}^2}} }}$ $= \frac{{(1 + {{\tan }^2}x)\cos (\tan x) + (1 + {{\cot }^2}x)\sin (\cot x)}}{{3\sqrt {{{[\sin (\tan x) + \cos (\cot x)]}^2}} }}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 5. Tính đạo hàm các hàm số sau:

a. 
$$
f(x) = \left\{ \begin{array}{l}
{x^2} – 3x + 1\:khi\:x > 1\\
2x + 2\:khi\:x \le 1{\rm{ }}
\end{array} \right.
$$

b. 
$$
f(x) = \left\{ \begin{array}{l}
{x^2}\cos \frac{1}{{2x}}\:khi\:x \ne 0\\
0\:khi\:x = 0
\end{array} \right.
$$

a.

• Với $x > 1$ $\Rightarrow f(x) = {x^2} – 3x + 1$ $\Rightarrow f'(x) = 2x – 3.$

• Với $x < 1$ $\Rightarrow f(x) = 2x + 2$ $\Rightarrow f'(x) = 2.$

• Với $x = 1$, ta có: $\mathop {\lim }\limits_{x \to {1^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {1^ + }} \left( {{x^2} – 3x + 1} \right)$ $= – 1 \ne f(1)$ $\Rightarrow$ hàm số không liên tục tại $x = 1$, suy ra hàm số không có đạo hàm tại $x = 1.$

Vậy 
$$
f'(x) = \left\{ \begin{array}{l}
2x – 3\:khi\:x > 1\\
2\:khi\:x < 1
\end{array} \right.
$$

b.

• Với $x \ne 0$ $\Rightarrow f(x) = {x^2}\cos \frac{1}{{2x}}$ $\Rightarrow f'(x) = 2x\cos \frac{1}{{2x}} – \frac{1}{2}\cos \frac{1}{{2x}}.$

• Với $x = 0$, ta có: $\mathop {\lim }\limits_{x \to 0} \frac{{f(x) – f(0)}}{x}$ $= \mathop {\lim }\limits_{x \to 0} x\cos \frac{1}{{2x}} = 0$ $\Rightarrow f'(0) = 0.$

Vậy 
$$
f'(x) = \left\{ \begin{array}{l}
\left( {2x – \frac{1}{2}} \right)\cos \frac{1}{{2x}}\:khi\:x \ne 0\\
0\:khi\:x = 0
\end{array} \right.
$$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 6. Chứng minh rằng các hàm số sau đây có đạo hàm không phụ thuộc $x.$

a. $y = {\sin ^6}x + {\cos ^6}x + 3{\sin ^2}x{\cos ^2}x.$

b. $y = {\cos ^2}\left( {\frac{\pi }{3} – x} \right) + {\cos ^2}\left( {\frac{\pi }{3} + x} \right)$ $+ {\cos ^2}\left( {\frac{{2\pi }}{3} – x} \right) + {\cos ^2}\left( {\frac{{2\pi }}{3} + x} \right)$ $– 2{\sin ^2}x.$

a. Ta có: $y = {\sin ^6}x + {\cos ^6}x + 3{\sin ^2}x{\cos ^2}x$ $= {\left( {{{\sin }^2}x} \right)^3} + {\left( {{{\cos }^2}x} \right)^3}$ $+ 3{\sin ^2}x{\cos ^2}x\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $= {\left( {{{\sin }^2}x + {{\cos }^2}x} \right)^3} = 1.$ Suy ra: $y’ = 0.$

b. Ta có: $y = 2 + \frac{1}{2}{\rm{[}}\cos \left( {\frac{{2\pi }}{3} – 2x} \right) + \cos \left( {\frac{{2\pi }}{3} + 2x} \right)$ $+ \cos \left( {\frac{{4\pi }}{3} – 2x} \right) + \cos \left( {\frac{{4\pi }}{3} + 2x} \right)]$ $– 2{\sin ^2}x$ $= \frac{3}{2} + \frac{1}{2}( – \cos 2x – \cos 2x) – 2{\sin ^2}x = 1.$ Suy ra: $y’ = 0.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 7. Tìm $a,b$ để hàm số
$$
f(x) = \left\{ \begin{array}{l}
{x^2} – x + 1{\rm{ }}\:khi\:x \le 1\\
– {x^2} + ax + b\:khi\:x > 1
\end{array} \right.
$$
 có đạo hàm trên $R.$

Với $x \ne 1$ thì hàm số luôn có đạo hàm.

Do đó hàm số có đạo hàm trên $R$ khi và chỉ khi hàm số có đạo hàm tại $x = 1.$

Ta có: $\mathop {\lim }\limits_{x \to {1^ – }} f(x) = 1$, $\mathop {\lim }\limits_{x \to {1^ + }} f(x) = a + b – 1.$

Hàm số liên tục trên $R$ $\Leftrightarrow a + b – 1 = 1$ $\Leftrightarrow a + b = 2.$

Khi đó:

$\mathop {\lim }\limits_{x \to {1^ – }} \frac{{f(x) – f(1)}}{{x – 1}} = 1.$

$\mathop {\lim }\limits_{x \to {1^ + }} \frac{{f(x) – f(1)}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{ – {x^2} + ax + 1 – a}}{{x – 1}}$ $= a – 2.$

Nên hàm số có đạo hàm trên $R$ thì: 
$$
\left\{ \begin{array}{l}
a + b = 2\\
a – 2 = 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = 3\\
b = – 1
\end{array} \right.
$$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-dao-ham.html -->
## Ví dụ 8. Tìm $m$ để các hàm số:

a. $y = (m – 1){x^3} – 3(m + 2){x^2}$ $– 6(m + 2)x + 1$ có $y’ \ge 0$, $\forall x \in R.$

b. $y = \frac{{m{x^3}}}{3} – m{x^2} + (3m – 1)x + 1$ có $y’ \le 0$, $\forall x \in R.$

a. Ta có: $y’ = 3\left[ {(m – 1){x^2} – 2(m + 2)x – 2(m + 2)} \right].$

Do đó: $y’ \ge 0$ $\Leftrightarrow (m – 1){x^2} – 2(m + 2)x – 2(m + 2) \ge 0$ $(1).$

• Với $m = 1$ thì $\left( 1 \right) \Leftrightarrow – 6x – 6 \ge 0 \Leftrightarrow x \le – 1.$

• Với $m \ne 1$ thì $(1)$ đúng với mọi $x \in R$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = m – 1 > 0\\
\Delta ‘ \le 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m > 1\\
(m + 1)(4 – m) \le 0
\end{array} \right.
$$
 $\Leftrightarrow m \ge 4.$

Vậy $m \ge 4.$

b. Ta có: $y’ = m{x^2} – 2mx + 3m – 1.$

Nên $y’ \le 0$ $\Leftrightarrow m{x^2} – 2mx + 3m – 1 \le 0$ $(2).$

• Với $m = 0$ thì $(2)$ trở thành: $– 1 \le 0$ (luôn đúng).

• Với $m \ne 0$ khi đó $(2)$ đúng với mọi $x \in R$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = m < 0\\
\Delta’ \le 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m < 0\\
m(1 – 2m) \le 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m < 0\\
1 – 2m \ge 0
\end{array} \right.
$$
 $\Leftrightarrow m < 0.$

Vậy $m \le 0.$