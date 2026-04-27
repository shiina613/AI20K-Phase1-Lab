# Hàm số liên tục trên một tập hợp

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán thường gặp trong chủ đề hàm số liên tục trên một tập hợp. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu chuyên đề giới hạn xuất bản trên TOANMATH.com.

1. Kiến thức cần nắm:

• Giả sử hàm số $f$ xác định trên tập hợp $J$, trong đó $J$ là một khoảng hoặc hợp của nhiều khoảng. Ta nói rằng hàm số $f$ liên tục trên $J$ nếu nó liên tục tại mọi điểm thuộc tập hợp $J$.

• Hàm số $f$ xác định trên đoạn $[a;b]$ được gọi là liên tục trên đoạn $[a; b]$ nếu nó liên tục trên khoảng $(a;b)$ và $\mathop {\lim }\limits_{x \to {a^ + }} f\left( x \right) = f\left( a \right)$, $\mathop {\lim }\limits_{x \to {b^ – }} f\left( x \right) = f\left( b \right).$

• Tính liên tục của hàm số trên các nửa khoảng $[a;b)$, $(a;b]$, $[a;+∞)$ và $(-∞;b]$ được định nghĩa tương tự như tính liên tục của hàm số trên một đoạn.

• Hàm số đa thức liên tục trên toàn bộ tập số thực $R.$

• Hàm số phân thức hữu tỉ (thương của hai đa thức), các hàm số lượng giác, hàm số lũy thừa, hàm số mũ và hàm số logarit liên tục trên tập xác định của chúng.

2. Các dạng toán và ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
## Ví dụ 1: Chứng minh các hàm số sau liên tục trên $R.$

a) $f\left( x \right) = {x^4} – {x^2} + 2.$

b) $f\left( x \right) = {x^2}\sin x – 2{\cos ^2}x + 3.$

c) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{2{x^3} + x + 3}}{{{x^3} + 1}}\:khi\:x \ne – 1\\
\frac{7}{3}\:khi\:x = – 1
\end{array} \right.{\rm{ }}
$$

d) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^2} – 4x + 3}}{{x – 1}}\:khi\:x > 1\\
– \sqrt {5 – x} \:khi\:x \le 1
\end{array} \right.
$$

a) Tập xác định: $D = R.$

$\forall {x_0} \in R$, ta có: $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {x_0}} \left( {{x^4} – {x^2} + 2} \right)$ $= x_0^4 – x_0^2 + 2$ $= f\left( {{x_0}} \right).$ Suy ra hàm số liên tục trên $R.$

b) Tập xác định: $D = R.$

$\forall {x_0} \in R$, ta có: $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {x_0}} \left( {{x^2}.\sin x – 2{{\cos }^2}x + 3} \right)$ $= x_0^2\sin {x_0} – 2{\cos ^2}{x_0} + 3$ $= f\left( {{x_0}} \right).$ Suy ra hàm số liên tục trên $R.$

c) Tập xác định của $f(x)$ là: $D = R.$

Nếu $x \ne – 1$ thì $f\left( x \right) = \frac{{2{x^3} + x + 3}}{{{x^3} + 1}}$ là hàm số phân thức hữu tỉ, nên liên tục trên các khoảng $\left( { – \infty ; – 1} \right)$ và $\left( { – 1; + \infty } \right)$ $(1).$

Bây giờ ta xét tính liên tục của $f(x)$ tại ${x_0} = – 1.$

Ta có:

$f({x_0}) = f( – 1) = \frac{7}{3}.$

$\mathop {\lim }\limits_{x \to – 1} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – 1} \frac{{2{x^3} + x + 3}}{{{x^3} + 1}}$ $= \mathop {\lim }\limits_{x \to – 1} \frac{{\left( {x + 1} \right)\left( {2{x^2} – 2x + 3} \right)}}{{\left( {x + 1} \right)\left( {{x^2} – x + 1} \right)}}$ $= \mathop {\lim }\limits_{x \to – 1} \frac{{2{x^2} – 2x + 3}}{{{x^2} – x + 1}}$ $= \frac{7}{3}.$

Vì $\mathop {\lim }\limits_{x \to – 1} f\left( x \right) = f\left( { – 1} \right)$ suy ra hàm số liên tục tại ${x_0} = – 1$ $(2).$

Từ $(1)$ và $(2)$ suy ra hàm số $f(x)$ liên tục trên $R.$

d) Tập xác định của $f(x)$ là $D = R.$

Với mọi ${x_0} \in \left( {1; + \infty } \right)$, ta có: $\mathop {\lim }\limits_{x \to {x_0}} f(x)$ $= \mathop {\lim }\limits_{x \to {x_0}} \frac{{{x^2} – 4x + 3}}{{x – 1}}$ $= \frac{{x_0^2 – 4{x_0} + 3}}{{{x_0} – 1}}$ $= f({x_0}).$ Suy ra hàm số $f(x)$ liên tục trên khoảng $\left( {1; + \infty } \right)$ $(1).$

Với mọi ${x_0} \in \left( { – \infty ;1} \right)$, ta có: $\mathop {\lim }\limits_{x \to {x_0}} f(x)$ $= \mathop {\lim }\limits_{x \to {x_0}} \left( { – \sqrt {5 – x} } \right)$ $= – \sqrt {5 – {x_0}}$ $= f({x_0}).$ Suy ra hàm số $f(x)$ liên tục trên khoảng $\left( { – \infty ;1} \right)$ $(2).$

Ta xét tính liên tục của $f(x)$ tại ${x_0} = 1.$

Ta có:

$\mathop {\lim }\limits_{x \to {1^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{{x^2} – 4x + 3}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{{\left( {x – 1} \right)\left( {x – 3} \right)}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} (x – 3)$ $= – 2.$

$\mathop {\lim }\limits_{x \to {1^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {1^ – }} \left( { – \sqrt {5 – x} } \right)$ $= – 2.$

$f\left( 1 \right) = – \sqrt {5 – 1} = -2.$

Vì $\mathop {\lim }\limits_{x \to {1^ + }} f\left( x \right) = \mathop {\lim }\limits_{x \to {1^ – }} f\left( x \right) = f\left( 1 \right)$ suy ra hàm số liên tục tại ${x_0} = 1.$

Từ $(1)$, $(2)$ và $(3)$ suy ra $f(x)$ liên tục trên $R.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
## Ví dụ 2: Tìm $m$ để các hàm số sau liên tục trên $R.$

a) 
$$
f(x) = \left\{ \begin{array}{l}
\frac{{\sqrt[3]{{x – 2}} + 2x – 1}}{{x – 1}}\:khi\:x \ne 1\\
3m – 2\:khi\:x = 1
\end{array} \right.
$$

b) 
$$
f(x) = \left\{ \begin{array}{l}
\frac{{\sqrt {x + 1} – 1}}{x}\:khi\:x > 0\\
2{x^2} + 3m + 1\:khi\:x \le 0
\end{array} \right.
$$

c) 
$$
f(x) = \left\{ \begin{array}{l}
\sqrt {2x – 4} + 3\:khi\:x \ge 2\\
\frac{{x + 1}}{{{x^2} – 2mx + 3m + 2}}\:khi\:x < 2
\end{array} \right.
$$

a) Với $x \ne 1$ ta có $f(x) = \frac{{\sqrt[3]{{x – 2}} + 2x – 1}}{{x – 1}}$ nên hàm số liên tục trên khoảng $R\backslash \left\{ 1 \right\}.$

Do đó hàm số liên tục trên $R$ khi và chỉ khi hàm số liên tục tại $x = 1.$

Ta có:

$f(1) = 3m – 2.$

$\mathop {\lim }\limits_{x \to 1} f(x)$ $= \mathop {\lim }\limits_{x \to 1} \frac{{\sqrt[3]{{x – 2}} + 2x – 1}}{{x – 1}}$ $= \mathop {\lim }\limits_{x \to 1} \left[ {1 + \frac{{{x^3} + x – 2}}{{(x – 1)\left( {{x^2} – x\sqrt[3]{{x – 2}} + \sqrt[3]{{{{(x – 2)}^2}}}} \right)}}} \right]$ $= \mathop {\lim }\limits_{x \to 1} \left[ {1 + \frac{{{x^2} + x + 2}}{{{x^2} – x\sqrt[3]{{x – 2}} + \sqrt[3]{{{{(x – 2)}^2}}}}}} \right]$ $= 2.$

Nên hàm số liên tục tại $x = 1$ khi và chỉ khi $3m – 2 = 2$ $m = \frac{4}{3}.$

Vậy $m = \frac{4}{3}$ là giá trị cần tìm.

b)

• Với $x > 0$, ta có: $f(x) = \frac{{\sqrt {x + 1} – 1}}{x}$ nên hàm số liên tục trên $\left( {0; + \infty } \right).$

• Với $x < 0$ ta có $f(x) = 2{x^2} + 3m + 1$ nên hàm số liên tục trên $( – \infty ;0).$

Do đó hàm số liên tục trên $R$ khi và chỉ khi hàm số liên tục tại $x = 0.$

Ta có:

$f(0) = 3m + 1.$

$\mathop {\lim }\limits_{x \to {0^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ + }} \frac{{\sqrt {x + 1} – 1}}{x}$ $= \mathop {\lim }\limits_{x \to {0^ + }} \frac{1}{{\sqrt {x + 1} + 1}}$ $= \frac{1}{2}.$

$\mathop {\lim }\limits_{x \to {0^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {0^ – }} \left( {2{x^2} + 3m + 1} \right)$ $= 3m + 1.$

Do đó hàm số liên tục tại $x = 0$ khi và chỉ khi $3m + 1 = \frac{1}{2}$ $\Leftrightarrow m = – \frac{1}{6}.$

Vậy với $m = – \frac{1}{6}$ thì hàm số liên tục trên $R.$

c) Với $x > 2$ ta có hàm số liên tục.

Để hàm số liên tục trên $R$ thì hàm số phải liên tục trên khoảng $\left( { – \infty ;2} \right)$ và liên tục tại $x = 2.$

• Hàm số liên tục trên $\left( { – \infty ;2} \right)$ khi và chỉ khi tam thức $g(x) = {x^2} – 2mx + 3m + 2 \ne 0$, $\forall x \le 2.$

+ Trường hợp 1: 
$$
\left\{ \begin{array}{l}
\Delta’ = {m^2} – 3m – 2 \le 0\\
g(2) = – m + 6 \ne 0
\end{array} \right.
$$
 $\Leftrightarrow \frac{{3 – \sqrt {17} }}{2} \le m \le \frac{{3 + \sqrt {17} }}{2}.$

+ Trường hợp 2: 
$$
\left\{ \begin{array}{l}
\Delta’ = {m^2} – 3m – 2 > 0\\
{x_1} = m – \sqrt {\Delta’} > 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{m^2} – 3m – 2 > 0\\
m > 2\\
\Delta’ < {(m – 2)^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m > \frac{{3 + \sqrt {17} }}{2}\\
m < 6
\end{array} \right.
$$
 $\Leftrightarrow \frac{{3 + \sqrt {17} }}{2} < m < 6.$

Nên $\frac{{3 – \sqrt {17} }}{2} \le m < 6$ $(*)$ thì $g(x) \ne 0$, $\forall x \le 2.$

• Ta có:

$\mathop {\lim }\limits_{x \to {2^ + }} f(x)$ $= \mathop {\lim }\limits_{x \to {2^ + }} \left( {\sqrt {2x – 4} + 3} \right) = 3.$

$\mathop {\lim }\limits_{x \to {2^ – }} f(x)$ $= \mathop {\lim }\limits_{x \to {2^ – }} \frac{{x + 1}}{{{x^2} – 2mx + 3m + 2}}$ $= \frac{3}{{6 – m}}.$

Hàm số liên tục tại $x = 2$ $\Leftrightarrow \frac{3}{{6 – m}} = 3$ $\Leftrightarrow m = 5$ (thỏa $(*)$).

Vậy $m = 5$ là giá trị cần tìm.

[ads]

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
## Ví dụ 3: Cho hàm số
$$
f\left( x \right) = \left\{ \begin{array}{l}
1\:khi\:x \le 3\\
ax + b\:khi\:3 < x < 5\\
7\:khi\:x \ge 5
\end{array} \right. .
$$
 Xác định $a$, $b$ để hàm số liên tục trên $R.$

Tập xác định của hàm số $f(x)$ là $D=R.$

Ta có: hàm số liên tục trên khoảng $\left( { – \infty ;3} \right)$, $\left( {3;5} \right)$, $\left( {5; + \infty } \right)$ (vì $f(x)$ là hàm đa thức).

Do đó hàm số liên tục trên $R$ khi và chỉ khi hàm số liên tục tại các điểm $x = 3$ và $x = 5.$

• Tại $x = 3:$

Ta có:

$\mathop {\lim }\limits_{x \to {3^ – }} f\left( x \right) = \mathop {\lim }\limits_{x \to {3^ – }} 1 = 1.$

$\mathop {\lim }\limits_{x \to {3^ + }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {3^ + }} \left( {ax + b} \right)$ $= 3a + b.$

$f\left( 3 \right) = 1.$

Do đó hàm liên tục tại $x = 3$ khi và chỉ khi: $\mathop {\lim }\limits_{x \to {3^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {3^ + }} f\left( x \right)$ $= f\left( 3 \right)$ $\Leftrightarrow 3a + b = 1$ $\left( 1 \right).$

• Tại $x = 5:$

Ta có:

$\mathop {\lim }\limits_{x \to {5^ – }} f\left( x \right) = 5a + b.$

$\mathop {\lim }\limits_{x \to {5^ + }} f\left( x \right) = 7 = f\left( 5 \right).$

Do đó hàm số liên tục tại $x = 5$ khi và chỉ khi: $\mathop {\lim }\limits_{x \to {5^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {5^ + }} f\left( x \right)$ $= f\left( 5 \right)$ $\Leftrightarrow 5a + b = 7$ $\left( 2 \right).$

Từ $\left( 1 \right)$ và $\left( 2 \right)$ suy ra hàm số liên tục trên $R$ khi và chỉ khi: 
$$
\left\{ \begin{array}{l}
3a + b = 1\\
5a + b = 7
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = 3\\
b = – 8
\end{array} \right.
$$

Vậy với $a = 3$, $b = – 8$ thì hàm số liên tục trên $R.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
## Ví dụ 4: Xét xem các hàm số sau có liên tục với $\forall x \in R$ không? Nếu không, hãy chỉ ra các điểm gián đoạn.

a) $f\left( x \right) = 2{x^4} – 4{x^3} + 2x – 1.$

b) $f\left( x \right) = \frac{{3{x^2} – 4x + 5}}{{{x^2} – 3x + 2}}.$

c) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{2x + 1}}{{2{x^2} + 3x + 1}}\:khi\:x \ne – \frac{1}{2}\\
2\:khi\:x = – \frac{1}{2}
\end{array} \right.
$$

d) 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{2{x^3} + 6{x^2} + x + 3}}{{x + 3}}\:khi\:x \ne – 3\\
19\:khi\:x = – 3
\end{array} \right.
$$

a) Hàm số $f\left( x \right) = 2{x^4} – 4{x^3} + 2x – 1$ liên tục với mọi $x \in R$ vì $f\left( x \right)$ là hàm đa thức.

b) Hàm số $f\left( x \right) = \frac{{3{x^2} – 4x + 5}}{{{x^2} – 3x + 2}}$ liên tục với mọi $x \in R\backslash \left\{ {1;2} \right\}$, gián đoạn tại các điểm $x = 1$, $x = 2$ vì $f\left( x \right)$ không xác định tại $x = 1$ và $x = 2.$

c) Hàm số 
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{2x + 1}}{{2{x^2} + 3x + 1}}\:khi\:x \ne – \frac{1}{2}\\
2\:khi\:x = – \frac{1}{2}
\end{array} \right.
$$

• Với $x \in R\backslash \left\{ { – 1; – \frac{1}{2}} \right\}$, $f\left( x \right)$ là hàm phân thức hữu tỉ nên liên tục.

• Với $x = – \frac{1}{2}$, ta có: $\mathop {\lim }\limits_{x \to – \frac{1}{2}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – \frac{1}{2}} \frac{1}{{x + 1}}$ $= 2 = f\left( { – \frac{1}{2}} \right).$ Do đó hàm số liên tục tại $x = – \frac{1}{2}.$

• Hàm số gián đoạn tại $x = – 1$ vì nó không xác định tại $x = – 1.$

d) Với $x \ne – 3$, $f\left( x \right)$ là hàm phân thức hữu tỉ nên liên tục.

Tại $x = – 3$, ta có:

$f\left( { – 3} \right) = 19.$

$\mathop {\lim }\limits_{x \to – 3} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – 3} \frac{{\left( {x + 3} \right)\left( {2{x^2} + 1} \right)}}{{x + 3}}$ $= \mathop {\lim }\limits_{x \to – 3} \left( {2{x^2} + 1} \right)$ $= 19 = f\left( { – 3} \right).$

Do đó hàm số liên tục tại $x = – 3.$

Vậy hàm số liên tục với mọi $x \in R.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/ham-so-lien-tuc-tren-mot-tap-hop.html -->
## Ví dụ 5: Cho hàm số
$$
f\left( x \right) = \left\{ \begin{array}{l}
\frac{{{x^3} + 8}}{{{x^2} – 4}}\:khi\:x > – 2\\
– 3\:khi\:x = – 2\\
\sqrt {3 + x} – 5\:khi\: – 3 \le x < – 2
\end{array} \right. .
$$
 Tìm các khoảng, nửa khoảng mà trên đó hàm số $f(x)$ liên tục.

Vì ${x^2} – 4 \ne 0$ với mọi $x > – 2$ nên hàm số $f\left( x \right) = \frac{{{x^3} + 8}}{{{x^2} – 4}}$ xác định trên khoảng $\left( { – 2; + \infty } \right).$

Ta có: $\forall {x_0} \in \left( { – 2; + \infty } \right)$ thì $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {x_0}} \frac{{{x^3} + 8}}{{{x^2} – 4}}$ $= \frac{{x_0^3 + 8}}{{x_0^2 – 4}}$ $= f\left( {{x_0}} \right)$ nên hàm số $f(x)$ liên tục trên khoảng $\left( { – 2; + \infty } \right).$

Với mọi $x \in \left[ { – 3; – 2} \right)$ thì $3 + x \ge 0$, do đó hàm số $f\left( x \right) = \sqrt {3 + x} – 5$ xác định trên nửa khoảng $\left[ { – 3; – 2} \right).$

$\forall {x_0} \in \left[ { – 3; – 2} \right)$, ta có: $\mathop {\lim }\limits_{x \to {x_0}} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to {x_0}} \left( {\sqrt {3 + x} – 5} \right)$ $= \sqrt {3 + {x_0}} – 5$ $= f\left( {{x_0}} \right)$ nên hàm số $f(x)$ liên tục trên nửa khoảng $\left[ { – 3; – 2} \right).$

Tại ${x_0} = – 2$, ta có: $f\left( { – 2} \right) = – 3.$ Và $\mathop {\lim }\limits_{x \to – {2^ – }} f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – {2^ – }} \left( {\sqrt {3 + x} – 5} \right)$ $= – 4 \ne f\left( { – 2} \right)$ nên hàm số $f(x)$ không liên tục tại $x = – 2.$

Kết luận hàm số $f(x)$ liên tục trên $\left( { – 2; + \infty } \right)$ và trên $\left[ { – 3; – 2} \right).$