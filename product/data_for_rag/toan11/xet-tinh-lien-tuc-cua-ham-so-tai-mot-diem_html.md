# Xét tính liên tục của hàm số tại một điểm

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
Bài viết hướng dẫn phương pháp xét tính liên tục của hàm số tại một điểm, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu giới hạn xuất bản trên TOANMATH.com.

Phương pháp: Để xét tính liên tục của hàm số $y = f(x)$ tại điểm $x = x_0$, ta thực hiện theo các bước sau:

• Cách 1:

+ Tính $f\left( {{x_0}} \right).$

+ Tìm $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right).$

+ Nếu $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right) = f\left( {{x_0}} \right)$ thì hàm số $f(x)$ liên tục tại $x_0 .$

• Cách 2:

+ Tìm $\mathop {\lim }\limits_{x \to x_0^ – } f\left( x \right).$

+ Tìm  $\mathop {\lim }\limits_{x \to x_0^ + } f\left( x \right).$

+ Nếu $\mathop {\lim }\limits_{x \to x_0^ + } f\left( x \right) = \mathop {\lim }\limits_{x \to x_0^ – } f\left( x \right) = f\left( {{x_0}} \right)$ thì hàm số $f(x)$ liên tục tại ${x_0}.$

Ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
## Ví dụ 1. Xét tính liên tục của các hàm số sau tại điểm $x = – 2.$

a) $f\left( x \right) = \frac{{{x^2} – 4}}{{x + 2}}.$

b) 
$$
g\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^2} – 4}}{{x + 2}}\:với\:x \ne – 2\\
– 4\:với\:x = – 2
\end{array} \right.
$$

a) Vì $f\left( { – 2} \right)$ không xác định, suy ra hàm số không liên tục tại $x = – 2.$

b) Ta có: $\mathop {\lim }\limits_{x \to – 2} g\left( x \right)$ $= \mathop {\lim }\limits_{x \to – 2} \frac{{\left( {x + 2} \right)\left( {x – 2} \right)}}{{x + 2}}$ $= \mathop {\lim }\limits_{x \to – 2} \left( {x – 2} \right)$ $= – 4 = f\left( { – 2} \right).$

Do đó hàm số liên tục tại $x = – 2.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
## Ví dụ 2. Cho hàm số:
$$
y = f\left( x \right) = \left\{ \begin{array}{l}
\frac{{3 – \sqrt {{x^2} + 5} }}{{{x^2} – 4}} \: với \:x \ne \pm 2\\
– \frac{1}{6}\:với\:x = 2
\end{array} \right.
$$

a) Tính $\mathop {\lim }\limits_{x \to 2} f\left( x \right).$

b) Xét tính liên tục của hàm số $f\left( x \right)$ tại $x = 2$; $x = – 2.$

a) Ta có $\mathop {\lim }\limits_{x \to 2} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 2} \frac{{3 – \sqrt {{x^2} + 5} }}{{{x^2} – 4}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{9 – {x^2} – 5}}{{\left( {{x^2} – 4} \right)\left( {3 + \sqrt {{x^2} + 5} } \right)}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{ – 1}}{{3 + \sqrt {{x^2} + 5} }}$ $= – \frac{1}{6}.$

b) Từ câu a suy ra $\mathop {\lim }\limits_{x \to 2} f\left( x \right) = f\left( 2 \right).$ Vậy hàm số đã cho liên tục tại $x = 2.$ Hàm số đã cho không xác định tại $x = – 2.$ do đó hàm số không liên tục tại $x = – 2.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
## Ví dụ 3. Xét tính liên tục tại giá trị ${x_0}$ của các hàm số sau:

a) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^2} – 3x + 2}}{{x – 2}}\:với\:x \ne 2\\
1\:với\:x = 2
\end{array} \right.
$$
 tại ${x_0} = 2$ và tại ${x_0} = 4.$

b) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{\sqrt {x + 3} – 2}}{{x – 1}}\:với\:x \ne 1\\
\frac{1}{4}\:với\:x = 1
\end{array} \right.
$$
 tại ${x_0} = 1.$

c) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{1 – \sqrt {\cos x} }}{{{x^2}}}\:với\:x \ne 0\\
\frac{1}{4}\:với\:x = 0
\end{array} \right.
$$
 tại ${x_0} = 0$ và tại ${x_0} = \frac{\pi }{3}.$

d) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{2 – 7x + 5{x^2} – {x^3}}}{{{x^2} – 3x + 2}}\:với\:x \ne 2\\
1\:với\:x = 2
\end{array} \right.
$$
 tại ${x_0} = 2$ và tại ${x_0} = 5.$

e) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{x – 5}}{{\sqrt {2x – 1} – 3}}\:với\:x > 5\\
{\left( {x – 5} \right)^2} + 3\:với\:x \le 5
\end{array} \right.
$$
 tại ${x_0} = 5$, tại ${x_0} = 6$ và tại ${x_0} = 4.$

f) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{\sqrt {2x + 3} – 1}}{{x + 1}}\:với\:x > – 1\\
\frac{{\sqrt {3 – x} }}{2}\:với\:x \le – 1
\end{array} \right.
$$
 tại ${x_0} = – 1.$

g) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^2} – 3x + 2}}{{{x^2} – 1}}\:với\:x > 1\\
\frac{1}{2}\:với\:x = 1\\
x – \frac{3}{2}\:với\:x < 1
\end{array} \right.
$$
 tại ${x_0} = 1.$

[ads]

a)

• Xét tính liên tục của hàm số tại ${x_0} = 2:$

Ta có:

$f\left( {{x_0}} \right) = f\left( 2 \right) = 1.$

$\mathop {\lim }\limits_{x \to 2} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 2} \frac{{{x^2} – 3x + 2}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{\left( {x – 2} \right)\left( {x – 1} \right)}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to 2} (x – 1) = 1.$

Vì $\mathop {\lim }\limits_{x \to 2} f\left( x \right) = f\left( 2 \right)$ suy ra hàm số liên tục tại ${x_0} = 2.$

• Xét tính liên tục của hàm số tại ${x_0} = 4:$

Ta có: $\mathop {\lim }\limits_{x \to 4} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 4} \frac{{{x^2} – 3x + 2}}{{x – 2}}$ $= \frac{{{4^2} – 3.4 + 2}}{{4 – 2}}$ $= 3 = f\left( 4 \right)$, suy ra hàm số $f(x)$ liên tục tại ${x_0} = 4.$

b) Ta có:

$f\left( {{x_0}} \right) = f\left( 1 \right) = \frac{1}{4}.$

$\mathop {\lim }\limits_{x \to 1} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt {x + 3} – 2}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{x + 3 – 4}}{{\left( {\sqrt {x + 3} + 2} \right)\left( {x – 1} \right)}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{{x – 1}}{{\left( {\sqrt {x + 3} + 2} \right)\left( {x – 1} \right)}}$ $= \mathop {\lim }\limits_{x \to 1} \frac{1}{{\sqrt {x + 3} + 2}}$ $= \frac{1}{4}.$

Vì $\mathop {\lim }\limits_{x \to 1} f\left( x \right) = f\left( 1 \right)$ suy ra hàm số liên tục tại $x = 1.$

c)

• Xét tính liên tục của hàm số tại ${x_0} = 0:$

Ta có:

$f\left( {{x_0}} \right) = f\left( 0 \right) = \frac{1}{4}.$

$\mathop {\lim }\limits_{x \to 0} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 0} \frac{{1 – \sqrt {\cos x} }}{{{x^2}}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{1 – \cos x}}{{{x^2}\left( {1 + \sqrt {\cos x} } \right)}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{2{{\sin }^2}\frac{x}{2}}}{{{x^2}\left( {1 + \sqrt {\cos x} } \right)}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{1}{2}{\left( {\frac{{\sin \frac{x}{2}}}{{\frac{x}{2}}}} \right)^2}\frac{1}{{1 + \sqrt {\cos x} }}$ $= \frac{1}{4}.$

Vì $\mathop {\lim }\limits_{x \to 0} f\left( x \right) = f\left( 0 \right)$ suy ra hàm số liên tục tại ${x_0} = 0.$

• Xét tính liên tục của hàm số tại ${x_0} = \frac{\pi }{3}:$

Ta có: $\mathop {\lim }\limits_{x \to \frac{\pi }{3}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to \frac{\pi }{3}} \frac{{1 – \sqrt {\cos x} }}{{{x^2}}}$ $= \frac{{1 – \sqrt {\cos \frac{\pi }{3}} }}{{{{\left( {\frac{\pi }{3}} \right)}^2}}}$ $= f\left( {\frac{\pi }{3}} \right)$, suy ra hàm số $f(x)$ liên tục tại ${x_0} = \frac{\pi }{3}.$

d)

• Xét tính liên tục của hàm số tại ${x_0} = 2:$

Ta có:

$f\left( x \right) = f\left( 2 \right) = 1.$

$\mathop {\lim }\limits_{x \to 2} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 2} \frac{{2 – 7x + 5{x^2} – {x^3}}}{{{x^2} – 3x + 2}}$ $= \frac{{\left( {x – 2} \right)\left( { – {x^2} + 3x – 1} \right)}}{{\left( {x – 2} \right)\left( {x – 1} \right)}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{ – {x^2} + 3x – 1}}{{x – 1}}$ $= 1.$

Vì $\mathop {\lim }\limits_{x \to 2} f\left( x \right) = f\left( 2 \right)$ suy ra hàm số liên tục tại ${x_0} = 2.$

• Xét tính liên tục của hàm số tại ${x_0} = 5:$

Ta có: $\mathop {\lim }\limits_{x \to 5} f\left( x \right)$ $= \frac{{2 – 7.5 + {{5.5}^2} – {5^3}}}{{{5^2} – 3.5 + 2}}$ $= f\left( 5 \right)$, suy ra hàm số $f(x)$ liên tục tại ${x_0} = 5.$

e)

• Xét tính liên tục của hàm số tại ${x_0} = 5:$

Ta có:

$\mathop {\lim }\limits_{x \to {5^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {5^ + }} \frac{{x – 5}}{{\sqrt {2x – 1} – 3}}$ $= \mathop {\lim }\limits_{x \to {5^ + }} \frac{{\left( {x – 5} \right)\left( {\sqrt {2x – 1} + 3} \right)}}{{2x – 1 – 9}}$ $= \mathop {\lim }\limits_{x \to {5^ + }} \frac{{\left( {x – 5} \right)\left( {\sqrt {2x – 1} + 3} \right)}}{{2x – 10}}$ $= \mathop {\lim }\limits_{x \to {5^ + }} \frac{{\left( {x – 5} \right)\left( {\sqrt {2x – 1} + 3} \right)}}{{2\left( {x – 5} \right)}}$ $= \mathop {\lim }\limits_{x \to {5^ + }} \frac{{\left( {\sqrt {2x – 1} + 3} \right)}}{2}$ $= \frac{{\sqrt {2.5 – 1} + 3}}{2}$ $= 3.$

$\mathop {\lim }\limits_{x \to {5^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {5^ – }} \left[ {{{\left( {x – 5} \right)}^2} + 3} \right]$ $= 0 + 3 = 3$ $= f\left( 5 \right).$

Vì $\mathop {\lim }\limits_{x \to {5^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {5^ – }} f\left( x \right)$ $= f\left( 5 \right)$, suy ra hàm số liên tục tại ${x_0} = 5.$

• Xét tính liên tục của hàm số tại ${x_0} = 6.$

Ta có: $\mathop {\lim }\limits_{x \to 6} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 6} \frac{{x – 5}}{{\sqrt {2x – 1} – 3}}$ $= \frac{{6 – 5}}{{\sqrt {2.6 – 1} – 3}}$ $= \frac{1}{{\sqrt {11} – 3}}$ $= f\left( 6 \right).$

Vậy hàm số $f(x)$ liên tục tại ${x_0} = 6.$

• Xét tính liên tục của hàm số tại ${x_0} = 4.$

Ta có: $\mathop {\lim }\limits_{x \to 4} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 4} \left[ {{{\left( {x – 5} \right)}^2} + 3} \right]$ $= {\left( {4 – 5} \right)^2} + 3$ $= 4 = f\left( 4 \right)$, suy ra hàm số $f(x)$ liên tục tại ${x_0} = 4.$

f) Ta có:

$\mathop {\lim }\limits_{x \to – {1^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – {1^ + }} \frac{{\sqrt {2x + 3} – 1}}{{x + 1}}$ $= \mathop {\lim }\limits_{x \to – {1^ + }} \frac{{2x + 3 – 1}}{{\left( {\sqrt {2x + 3} + 1} \right)\left( {x + 1} \right)}}$ $= \mathop {\lim }\limits_{x \to – {1^ + }} \frac{{2\left( {x + 1} \right)}}{{\left( {\sqrt {2x + 3} + 1} \right)\left( {x + 1} \right)}}$ $= \mathop {\lim }\limits_{x \to – {1^ + }} \frac{2}{{\sqrt {2x + 3} + 1}}$ $= \frac{2}{{\sqrt {2.\left( { – 1} \right) + 3} + 1}}$ $= 1.$

$\mathop {\lim }\limits_{x \to – {1^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – {1^ – }} \frac{{\sqrt {3 – x} }}{2}$ $= \frac{{\sqrt {3 – \left( { – 1} \right)} }}{2}$ $= 1.$

$f\left( { – 1} \right) = \frac{{\sqrt {3 – ( – 1)} }}{2} = 1.$

Vì $\mathop {\lim }\limits_{x \to – {1^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – {1^ – }} f\left( x \right)$ $= f\left( { – 1} \right)$, suy ra hàm số liên tục tại ${x_0} = – 1.$

g) Ta có:

$f\left( {{x_0}} \right) = f\left( 1 \right) = \frac{1}{2}.$

$\mathop {\lim }\limits_{x \to {1^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{{x^2} – 3x + 2}}{{{x^2} – 1}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{\left( {x – 1} \right)\left( {x – 2} \right)}}{{\left( {x – 1} \right)\left( {x + 1} \right)}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{x – 2}}{{x + 1}}$ $= \frac{{1 – 2}}{{1 + 1}}$ $= – \frac{1}{2}.$

$\mathop {\lim }\limits_{x \to {1^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {1^ – }} \left( {x – \frac{3}{2}} \right)$ $= 1 – \frac{3}{2}$ $= – \frac{1}{2}.$

Vì $f\left( 1 \right) \ne \mathop {\lim }\limits_{x \to – 1} f\left( x \right)$, suy ra hàm số không liên tục tại ${x_0} = 1.$

Ví dụ 4. Cho hàm số 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^2} – 3x + 2}}{{x – 2}}\:với\:x \ne 2\\
a\:với\:x = 2
\end{array} \right.
$$
. Với giá trị nào của $a$ thì hàm số đã cho liên tục tại điểm $x = 2?$

Ta có: $\mathop {\lim }\limits_{x \to 2} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 2} \frac{{{x^2} – 3x + 2}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{{\left( {x – 1} \right)\left( {x – 2} \right)}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to 2} \left( {x – 1} \right)$ $= 1.$

Hàm số liên tục tại $x = 2$ khi và chỉ khi $\mathop {\lim }\limits_{x \to 2} f\left( x \right) = f\left( 2 \right)$ $\Leftrightarrow a = 1.$

Vậy hàm số đã cho liên tục tại $x = 2$ khi $a = 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
## Ví dụ 5. Cho hàm số
$$
y = f\left( x \right) = \left\{ \begin{array}{l}
\frac{{\left| {2{x^2} – 7x + 6} \right|}}{{x – 2}}\:khi \:x < 2\\
{\rm{a + }}\frac{{1 – x}}{{2 + x}}\:khi\:x \ge 2
\end{array} \right. .
$$
 Xác định $a$ để hàm số $f(x)$ liên tục tại ${x_0} = 2.$

Ta có:

$\mathop {\lim }\limits_{x \to {2^ – }} f\left( x \right)$ $= \frac{{\left| {2{x^2} – 7x + 6} \right|}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to {2^ – }} \frac{{\left| {\left( {x – 2} \right)\left( {2x – 3} \right)} \right|}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to {2^ – }} \frac{{\left( {2 – x} \right)\left( {2x – 3} \right)}}{{x – 2}}$ $= \mathop {\lim }\limits_{x \to {2^ – }} \left( {3 – 2x} \right)$ $= – 1.$

$\mathop {\lim }\limits_{x \to {2^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {2^ + }} \left( {{\rm{a + }}\frac{{1 – x}}{{2 + x}}} \right)$ $= a – \frac{1}{4} = f\left( 2 \right).$

Hàm số liên tục tại ${x_0} = 2$ $\Leftrightarrow \mathop {\lim }\limits_{x \to {2^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {2^ + }} f\left( x \right)$ $= f\left( 2 \right)$ $\Leftrightarrow a – \frac{1}{4}$ $= – 1$ $\Leftrightarrow a = – \frac{3}{4}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/xet-tinh-lien-tuc-cua-ham-so-tai-mot-diem.html -->
## Ví dụ 6. Cho các hàm số $f(x)$ sau đây. Có thể định nghĩa $f\left( 0 \right)$ để hàm số $f\left( x \right)$ trở thành hàm liên tục tại $x = 0$ được không?

a) $f\left( x \right) = \frac{{7{x^2} – 5x}}{{12x}}$ với $x \ne 0.$

b) $f\left( x \right) = \frac{{3x}}{{\sqrt {x + 4} – 2}}$ với $x \ne 0.$

c) $f\left( x \right) = \frac{3}{{2x}}$ với $x \ne 0.$

d) $f\left( x \right) = \frac{{\sqrt {x + 2} – \sqrt {2 – x} }}{{3x}}$ với $x \ne 0.$

a) Ta có: $\mathop {\lim }\limits_{x \to 0} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 0} \frac{{x\left( {7x – 5} \right)}}{{12x}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{7x – 5}}{{12}}$ $= – \frac{5}{{12}}.$

Hàm số liên tục tại $x = 0$ khi và chỉ khi $\mathop {\lim }\limits_{x \to 0} f\left( x \right) = f\left( 0 \right).$

Vậy nếu bổ sung $f\left( 0 \right) = – \frac{5}{{12}}$ thì hàm số liên tục tại $x = 0.$

b) Ta có: $\mathop {\lim }\limits_{x \to 0} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 0} \frac{{3x}}{{\sqrt {x + 4} – 2}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{{3x\left( {\sqrt {x + 4} + 2} \right)}}{{x + 4 – 4}}$ $= \mathop {\lim }\limits_{x \to 0} 3\left( {\sqrt {x + 4} + 2} \right)$ $= 12.$

Hàm số liên tục tại $x = 0$ khi và chỉ khi $\mathop {\lim }\limits_{x \to 0} f\left( x \right) = f\left( 0 \right).$

Vậy nếu bổ sung $f\left( 0 \right) = 12$ thì hàm số liên tục tại $x = 0.$

c) Ta có $\mathop {\lim }\limits_{x \to {0^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {0^ + }} \frac{3}{{2x}} = + \infty .$

Hàm số không có giới hạn hữu hạn tại $x = 0$, do đó hàm không thể liên tục tại $x = 0.$

d) Ta có $\mathop {\lim }\limits_{x \to 0} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to 0} \frac{{x + 2 – 2 + x}}{{3x\left( {\sqrt {x + 2} + \sqrt {2 – x} } \right)}}$ $= \mathop {\lim }\limits_{x \to 0} \frac{2}{{3\left( {\sqrt {x + 2} + \sqrt {2 – x} } \right)}}$ $= \frac{2}{{6\sqrt 2 }}$ $= \frac{1}{{3\sqrt 2 }}.$

Hàm số liên tục tại $x = 0$ khi và chỉ khi $\mathop {\lim }\limits_{x \to 0} f\left( x \right) = f\left( 0 \right).$

Vậy nếu bổ sung $f\left( 0 \right) = \frac{1}{{3\sqrt 2 }}$ thì hàm số liên tục tại $x = 0.$