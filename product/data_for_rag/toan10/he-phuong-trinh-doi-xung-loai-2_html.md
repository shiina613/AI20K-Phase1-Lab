# Hệ phương trình đối xứng loại 2

<!-- chunk:0 level:0 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
Bài viết hướng dẫn nhận dạng và cách giải hệ phương trình đối xứng loại 2 cùng các bài toán có liên quan đến hệ phương trình đối xứng loại 2.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## I. LÝ THUYẾT CẦN NẮM
1. Định nghĩa: Hệ phương trình đối xứng loại 2 là hệ phương trình có dạng: 
$$
\left\{ \begin{array}{l}
f\left( {x;y} \right) = a\\
f\left( {y;x} \right) = a
\end{array} \right.
$$
 $(*).$

2. Cách giải hệ phương trình đối xứng loại 2:

Trừ hai phương trình của hệ cho nhau ta được: $f\left( {x;y} \right) – f\left( {y;x} \right) = 0$ $\Leftrightarrow \left( {x – y} \right)g\left( {x;y} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = y\\
g\left( {x;y} \right) = 0
\end{array} \right.
$$

3. Chú ý:

+ Nếu hệ phương trình $(*)$ có nghiệm $\left( {{x}_{0}};{{y}_{0}} \right)$ thì $\left( {{y}_{0}};{{x}_{0}} \right)$ cũng là nghiệm của hệ phương trình $(*)$. Từ đó suy ra, nếu hệ phương trình $(*)$ có nghiệm duy nhất thì điều kiện cần là ${{x}_{0}}={{y}_{0}}.$

+ $f\left( {x;y} \right) + f\left( {y;x} \right) = 2a$ là một phương trình đối xứng.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 1. Giải các hệ phương trình sau:

1. 
$$
\left\{ \begin{array}{l}
{x^2} = 3x + 2y\\
{y^2} = 3y + 2x
\end{array} \right.
$$

2. 
$$
\left\{ \begin{array}{l}
{x^3} + 1 = 2y\\
{y^3} + 1 = 2x
\end{array} \right.
$$

1. Trừ vế với vế hai phương trình của hệ, ta được:

${x^2} – {y^2} = x – y$ $\Leftrightarrow \left( {x – y} \right)\left( {x + y – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = y\\
x = 1 – y
\end{array} \right.
$$

+ Với $x = y \Rightarrow {x^2} = 3x$ $\Leftrightarrow x = 0,x = 3.$

+ Với $x = 1 – y$ $\Rightarrow {y^2} = 3y + 2\left( {1 – y} \right)$ $\Leftrightarrow {y^2} – y – 2 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
y = – 1 \Rightarrow x = 2\\
y = 2 \Rightarrow x = – 1
\end{array} \right.
$$

Vậy hệ phương trình đã cho có nghiệm: $\left( {x;y} \right) = \left( {0;0} \right),\left( {3;3} \right)$, $\left( { – 1;2} \right),\left( {2; – 1} \right).$

2. Trừ hai phương trình của hệ, ta được:

${x^3} – {y^3} = 2\left( {y – x} \right)$ $\Leftrightarrow \left( {x – y} \right)\left( {{x^2} + xy + {y^2} + 2} \right) = 0$ $\Leftrightarrow x = y$ (do ${x^2} + xy + {y^2} + 2 > 0$, $\forall x,y$).

Thay vào hệ phương trình, ta được:

${x^3} + 1 = 2x$ $\Leftrightarrow \left( {x – 1} \right)\left( {{x^2} + x – 1} \right) = 0$ $\Leftrightarrow x = 1$, $x = \frac{{ – 1 \pm \sqrt 5 }}{2}.$

Vậy hệ phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = y = 1\\
x = y = \frac{{ – 1 \pm \sqrt 5 }}{2}
\end{array} \right.
$$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 2. Giải các hệ phương trình sau:

1. 
$$
\left\{ \begin{array}{l}
\frac{3}{{{x^2}}} = 2x + y\\
\frac{3}{{{y^2}}} = 2y + x
\end{array} \right.
$$

2. 
$$
\left\{ \begin{array}{l}
\sqrt {x + 9} + \sqrt {y – 7} = 8\\
\sqrt {y + 9} + \sqrt {x – 7} = 8
\end{array} \right.
$$

1. Điều kiện: $x,y \ne 0.$

Hệ phương trình 
$$
\Leftrightarrow \left\{ \begin{array}{l}
2{x^3} + {x^2}y = 3\\
2{y^3} + {y^2}x = 3
\end{array} \right.
$$
 $\Rightarrow 2\left( {{x^3} – {y^3}} \right) + xy\left( {x – y} \right) = 0$ $\Leftrightarrow \left( {x – y} \right)\left( {2{x^2} + 3xy + 2{y^2}} \right) = 0$ $\Leftrightarrow x = y$ (do $2{x^2} + 3xy + 2{y^2}$ $= 2{\left( {x + \frac{3}{4}y} \right)^2} + \frac{7}{8}{y^2} > 0$).

Thay vào hệ phương trình, ta được: $3{x^3} = 3$ $\Leftrightarrow x = 1 = y.$

Vậy hệ phương trình đã cho có nghiệm $x=y=1.$

2. Điều kiện: $x,y \ge 7.$

Trừ hai phương trình của hệ, ta được:

$\sqrt {x + 9} + \sqrt {y – 7}$ $= \sqrt {y + 9} + \sqrt {x – 7}$ $\Leftrightarrow \sqrt {\left( {x + 9} \right)\left( {y – 7} \right)}$ $= \sqrt {\left( {y + 9} \right)\left( {x – 7} \right)}$ $\Leftrightarrow x = y.$

Thay vào hệ phương trình, ta được:

$\sqrt {x + 9} + \sqrt {x – 7} = 8$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\sqrt {x + 9} + \sqrt {x – 7} = 8\\
\sqrt {x + 9} – \sqrt {x – 7} = 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\sqrt {x + 9} = 5\\
\sqrt {x – 7} = 3
\end{array} \right.
$$
 $\Leftrightarrow x = 16.$

Vậy hệ phương trình đã cho có nghiệm: $x=y=16.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 3. Giải các hệ phương trình sau:

1. 
$$
\left\{ \begin{array}{l}
\sqrt x + \sqrt {2 – y} = 2\\
\sqrt y + \sqrt {2 – x} = 2
\end{array} \right.
$$

2. 
$$
\left\{ \begin{array}{l}
\sqrt {5x + 1} + \sqrt {12 – y} = 7\\
\sqrt {5y + 1} + \sqrt {12 – x} = 7
\end{array} \right.
$$

1. Điều kiện: $0 \le x,y \le 2.$

Trừ hai phương trình của hệ, ta được:

$\sqrt x – \sqrt {2 – x}$ $= \sqrt y – \sqrt {2 – y}$ $\left( * \right).$

Do hàm số $f\left( t \right) = \sqrt t + \sqrt {2 – t}$ là một hàm liên tục và đồng biến trên $(0;2).$

Nên $\left( * \right) \Leftrightarrow f(x) = f(y)$ $\Leftrightarrow x = y.$

Thay vào hệ phương trình, ta có:

$\sqrt x + \sqrt {2 – x} = 2$ $\Leftrightarrow \sqrt {x\left( {2 – x} \right)} = 1$ $\Leftrightarrow x = 1.$

Vậy hệ phương trình đã cho có nghiệm: $x=y=1.$

2. Điều kiện: 
$$
\left\{ \begin{array}{l}
– \frac{1}{5} \le x \le 12\\
– \frac{1}{5} \le y \le 12
\end{array} \right.
$$

Trừ hai phương trình của hệ, ta được:

$\sqrt {5x + 1} – \sqrt {12 – x}$ $= \sqrt {5y + 1} – \sqrt {12 – y}$ $(*).$

Xét hàm số: $f\left( t \right) = \sqrt {5t + 1} – \sqrt {12 – t}$, $t \in \left[ { – \frac{1}{5};12} \right]$, ta có:

$f’\left( x \right) = \frac{5}{{2\sqrt {5t + 1} }} + \frac{1}{{2\sqrt {12 – t} }} > 0$, $\forall t \in \left( { – \frac{1}{5};12} \right).$

Suy ra: $\left( * \right) \Leftrightarrow f\left( x \right) = f\left( y \right)$ $\Leftrightarrow x = y.$

Thay $x=y$ vào hệ phương trình, ta được:

$\sqrt {5x + 1} + \sqrt {12 – x} = 7$ $\Leftrightarrow 4x + 13$ $+ 2\sqrt {\left( {5x + 1} \right)\left( {12 – x} \right)} = 49$ $\Leftrightarrow \sqrt { – 5{x^2} + 59x + 12} = 18 – 2x$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \le 9\\
9{x^2} – 131x + 312 = 0
\end{array} \right.
$$
 $\Leftrightarrow x = 3.$

Vậy hệ phương trình đã cho có nghiệm $x=y=3.$

[ads]

<!-- chunk:5 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 4. Giải các hệ phương trình sau:

1. 
$$
\left\{ \begin{array}{l}
{x^3} = 2x + y\\
{y^3} = 2y + x
\end{array} \right.
$$

2. 
$$
\left\{ \begin{array}{l}
\left( {x – 1} \right)\left( {{y^2} + 6} \right) = y\left( {{x^2} + 1} \right)\\
\left( {y – 1} \right)\left( {{x^2} + 6} \right) = x\left( {{y^2} + 1} \right)
\end{array} \right.
$$

1. Trừ hai phương trình của hệ, ta được:

${x^3} – {y^3} = x – y$ $\Leftrightarrow \left( {x – y} \right)\left( {{x^2} + xy + {y^2} – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = y\\
{x^2} + xy + {y^2} – 1 = 0
\end{array} \right.
$$

+ Với $x=y$, thay vào hệ phương trình, ta được: ${x^3} = 3x$ $\Leftrightarrow x = 0$, $x = \pm \sqrt 3 .$

+ Với ${x^2} + xy + {y^2} = 1$ $\left( 1 \right)$, cộng hai phương trình của hệ phương trình, ta có: ${x^3} + {y^3} – 3\left( {x + y} \right) = 0$ $\left( 2 \right).$

Từ $(1)$ và $(2)$, ta có hệ phương trình: 
$$
\left\{ \begin{array}{l}
{x^2} + xy + {y^2} – 1 = 0\\
{x^3} + {y^3} – 3\left( {x + y} \right) = 0
\end{array} \right.
$$

Đặt $S=x+y$, $P=xy$, ta có: 
$$
\left\{ \begin{array}{l}
{S^2} – P – 1 = 0\\
{S^3} – 3SP – 3S = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
P = {S^2} – 1\\
{S^3} – 3S\left( {{S^2} – 1} \right) – 3S = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
S = 0\\
P = – 1
\end{array} \right.
$$

$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 1\\
y = – 1
\end{array} \right.
$$
 hoặc 
$$
\left\{ \begin{array}{l}
x = – 1\\
y = 1
\end{array} \right.
$$

Vậy hệ phương trình đã cho có các nghiệm: 
$$
\left\{ \begin{array}{l}
x = 0\\
y = 0
\end{array} \right.
$$
, 
$$
\left\{ \begin{array}{l}
x = – 1\\
y = 1
\end{array} \right.
$$
, 
$$
\left\{ \begin{array}{l}
x = 1\\
y = – 1
\end{array} \right.
$$
, 
$$
\left\{ \begin{array}{l}
x = \sqrt 3 \\
y = \sqrt 3
\end{array} \right.
$$
, 
$$
\left\{ \begin{array}{l}
x = – \sqrt 3 \\
y = – \sqrt 3
\end{array} \right.
$$

2. Hệ phương trình 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x{y^2} + 6x – {y^2} – 6 = y{x^2} + y\\
y{x^2} + 6y – {x^2} – 6 = x{y^2} + x
\end{array} \right.
$$

Trừ vế theo vế hai phương trình của hệ, ta được:

$2xy\left( {y – x} \right) + 7\left( {x – y} \right)$ $+ \left( {x – y} \right)\left( {x + y} \right) = 0$ $\Leftrightarrow \left( {x – y} \right)\left( {x + y – 2xy + 7} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = y\\
x + y – 2xy + 7 = 0
\end{array} \right.
$$

+ Với $x=y$, thay vào hệ phương trình, ta được: ${x^2} – 5x + 6 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = y = 2\\
x = y = 3
\end{array} \right.
$$

+ Với $x+y-2xy+7=0$ $(1)$, cộng hai phương trình của hệ đã cho, ta được: ${x^2} + {y^2} – 5x – 5y + 12 = 0$ $\left( 2 \right).$

Từ $(1)$ và $(2)$ ta có hệ phương trình: 
$$
\left\{ \begin{array}{l}
x + y – 2xy + 7 = 0\\
{x^2} + {y^2} – 5x – 5y + 12 = 0
\end{array} \right.
$$

Đặt $S=x+y$, $P=xy$, ta có hệ phương trình:

$$
\left\{ \begin{array}{l}
S – 2P + 7 = 0\\
{S^2} – 5S – 2P + 12 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
P = \frac{{S + 7}}{2}\\
{S^2} – 6S + 5 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
S = 1\\
P = 4
\end{array} \right.
$$
 hoặc 
$$
\left\{ \begin{array}{l}
S = 5\\
P = 6
\end{array} \right.
$$

+ Với 
$$
\left\{ \begin{array}{l}
S = 1\\
P = 4
\end{array} \right.
$$
, ta thấy hệ vô nghiệm.

+ Với 
$$
\left\{ \begin{array}{l}
S = 5\\
P = 6
\end{array} \right.
$$
, ta có: 
$$
\left\{ \begin{array}{l}
x = 2\\
y = 3
\end{array} \right.
$$
 hoặc 
$$
\left\{ \begin{array}{l}
x = 3\\
y = 2
\end{array} \right.
$$

Vậy nghiệm của hệ phương trình đã cho là: $\left( {x;y} \right) = \left( {2;2} \right),\left( {3;3} \right)$, $\left( {2;3} \right),\left( {3;2} \right).$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 5. Tìm $m$ để hệ phương trình sau có nghiệm:
$$
\left\{ \begin{array}{l}
2x + \sqrt {y – 1} = m\\
2y + \sqrt {x – 1} = m
\end{array} \right.
$$

Điều kiện: $x,y \ge 1$. Đặt $a = \sqrt {x – 1}$, $b = \sqrt {y – 1}$ $\Rightarrow a,b \ge 0$, ta có:

$$
\left\{ \begin{array}{l}
2{a^2} + b = m – 2\\
2{b^2} + a = m – 2
\end{array} \right.
$$
 $\Rightarrow 2\left( {a – b} \right)\left( {a + b} \right)$ $+ b – a = 0$ $\Leftrightarrow \left( {a – b} \right)\left( {2a + 2b – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
a = b\\
a = \frac{{1 – 2b}}{2}
\end{array} \right.
$$

+ Với $a = b$ $\Rightarrow 2{a^2} + a = m – 2$ $\Rightarrow$ Phương trình có nghiệm $a \ge 0$ $\Leftrightarrow m – 2 \ge 0$ $\Leftrightarrow m \ge 2.$

+ Với $a = \frac{{1 – 2b}}{2}$ 
$$
\Rightarrow \left\{ \begin{array}{l}
0 \le b \le \frac{1}{2}\\
4{b^2} – 2b = 2m – 5
\end{array} \right.
$$
, hệ phương trình có nghiệm $\Leftrightarrow – \frac{1}{4} \le 2m – 5 \le 0$ $\Leftrightarrow \frac{{19}}{8} \le m \le \frac{5}{2}.$

Vậy hệ phương trình đã cho có nghiệm khi và chỉ khi $m \ge 2.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 6. Tìm $m$ để các hệ phương trình sau có nghiệm duy nhất:

1. 
$$
\left\{ \begin{array}{l}
x = {y^2} – y + m\\
y = {x^2} – x + m
\end{array} \right.
$$

2. 
$$
\left\{ \begin{array}{l}
3{x^2} = {y^3} – 2{y^2} + my\\
3{y^2} = {x^3} – 2{x^2} + mx
\end{array} \right.
$$

1. Điều kiện cần: Giả sử hệ có nghiệm $\left( {{x}_{0}};{{y}_{0}} \right)$ thì $\left( {{y}_{0}};{{x}_{0}} \right)$ cũng là nghiệm của hệ nên để hệ có nghiệm duy nhất thì trước hết ${{x}_{0}}={{y}_{0}}.$

Thay vào hệ ta được: $x_0^2 – 2{x_0} + m = 0$, phương trình này có nghiệm duy nhất $\Leftrightarrow \Delta’ = 1 – m = 0$ $\Leftrightarrow m = 1.$

Điều kiện đủ: Với $m = 1$ hệ trở thành:

$$
\left\{ \begin{array}{l}
x = {y^2} – y + 1\\
y = {x^2} – x + 1
\end{array} \right.
$$
 $\Rightarrow {x^2} + {y^2} – 2x – 2y + 2 = 0$ $\Leftrightarrow {\left( {x – 1} \right)^2} + {\left( {y – 1} \right)^2} = 0$ $\Leftrightarrow x = y = 1$ (thử lại ta thấy thỏa mãn hệ).

Vậy hệ phương trình đã cho có nghiệm duy nhất khi và chỉ khi $m = 1.$

2. Điều kiện cần: Giả sử hệ có nghiệm $\left( {{x}_{0}};{{y}_{0}} \right)$ thì $\left( {{y}_{0}};{{x}_{0}} \right)$ cũng là nghiệm của hệ nên để hệ có nghiệm duy nhất thì trước hết ${{x}_{0}}={{y}_{0}}.$

Thay vào hệ ta được: $x_0^3 – 5x_0^2 + m{x_0} = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x_0} = 0\\
x_0^2 – 5{x_0} + m = 0\left( * \right)
\end{array} \right.
$$

Để hệ phương trình có nghiệm duy nhất thì $(*)$ phải vô nghiệm hoặc có nghiệm kép $x = 0.$

$$
\Leftrightarrow \left[ \begin{array}{l}
\Delta = 25 – 4m < 0\\
\left\{ \begin{array}{l}
\Delta = 25 – 4m = 0\\
5 = 0
\end{array} \right.
\end{array} \right.
$$
 $\Leftrightarrow m > \frac{{25}}{4}.$

Điều kiện đủ: Với $m > \frac{{25}}{4}$, ta có:

$$
\left[ \begin{array}{l}
3{x^2} = y\left( {{y^2} – 2y + m} \right) = y\left[ {{{\left( {y – 1} \right)}^2} + m – 1} \right]\\
3{y^2} = x\left( {{x^2} – 2x + m} \right) = x\left[ {{{\left( {x – 1} \right)}^2} + m – 1} \right]
\end{array} \right.
$$
 $\Rightarrow x,y \ge 0.$

Cộng hai phương trình của hệ với nhau, ta được:

$x\left( {{x^2} – 5x + m} \right)$ $+ y\left( {{y^2} – 5y + m} \right) = 0$ $\Leftrightarrow x\left[ {{{\left( {x – \frac{5}{2}} \right)}^2} + m – \frac{{25}}{4}} \right]$ $+ y\left[ {{{\left( {y – \frac{5}{2}} \right)}^2} + m – \frac{{25}}{4}} \right] = 0$ $\Leftrightarrow x = y = 0.$

Vậy hệ phương trình đã cho có nghiệm duy nhất khi và chỉ khi $m > \frac{{25}}{4}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/07/he-phuong-trinh-doi-xung-loai-2.html -->
## Ví dụ 7. Chứng minh rằng hệ phương trình
$$
\left\{ \begin{array}{l}
2{x^2} = y + \frac{{{a^2}}}{y}\\
2{y^2} = x + \frac{{{a^2}}}{x}
\end{array} \right.
$$
 có nghiệm duy nhất với mọi $a \ne 0.$

Điều kiện: $x \ne 0.$

Từ hai phương trình của hệ $\Rightarrow x,y > 0.$

Hệ phương trình 
$$
\Leftrightarrow \left\{ \begin{array}{l}
2{x^2}y = {y^2} + {a^2}\\
2{y^2}x = {x^2} + {a^2}
\end{array} \right.
$$
 $\Rightarrow 2xy\left( {x – y} \right) = {y^2} – {x^2}$ $\Leftrightarrow \left( {x – y} \right)\left( {2xy + x + y} \right) = 0$ $\Leftrightarrow x = y$ (do $x,y > 0$ $\Rightarrow 2xy + x + y > 0$).

Thay vào hệ phương trình, ta được: ${a^2} = 2{x^3} – {x^2} = f\left( x \right)$ $(*).$

Xét hàm số: $f\left( x \right) = 2{x^3} – {x^2}$ với $x>0.$

Ta có: $f’\left( x \right) = 2x\left( {3x – 1} \right)$ $\Rightarrow f’\left( x \right) = 0$ $\Leftrightarrow x = \frac{1}{3}.$

Mà $f\left( 0 \right) = 0$, $f\left( {\frac{1}{3}} \right) = – \frac{1}{{27}}$ và ${a^2} > 0$ nên phương trình $(*)$ chỉ có duy nhất một nghiệm.

Vậy hệ đã cho luôn có nghiệm duy nhất với mọi $a \ne 0.$