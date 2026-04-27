# Phương pháp giải phương trình mũ và bất phương trình mũ (Phần 1)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
Bài viết phân dạng và hướng dẫn phương pháp giải các dạng toán phương trình mũ và bất phương trình mũ trong chương trình Giải tích 12 chương 2, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu lũy thừa – mũ – logarit được đăng tải trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## A. KIẾN THỨC CẦN GHI NHỚ

1. ${a^{f\left( x \right)}} = {a^{g\left( x \right)}}$ $\Leftrightarrow f\left( x \right) = g\left( x \right).$

2. ${a^{f\left( x \right)}} = b = {a^{{{\log }_a}b}}$ $\Leftrightarrow f\left( x \right) = {\log _a}b.$

3. ${a^{f\left( x \right)}} = {b^{g\left( x \right)}}$ $\Leftrightarrow f\left( x \right) = g\left( x \right){\log _a}b.$

4. ${a^{f\left( x \right)}} > {a^{g\left( x \right)}}$ $(1).$

+ Nếu $a > 1$ thì $\left( 1 \right) \Leftrightarrow f\left( x \right) > g\left( x \right).$

+ Nếu $0 < a < 1$ thì $\left( 1 \right) \Leftrightarrow f\left( x \right) < g\left( x \right).$

Hay 
$$
\left( 1 \right) \Leftrightarrow \left\{ \begin{array}{l}
a > 0\\
\left( {a – 1} \right)\left( {f\left( x \right) – g\left( x \right)} \right) > 0
\end{array} \right.
$$

<!-- chunk:2 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Dạng 1. Biến đổi, quy về cùng cơ số
Phương pháp: Ta sử dụng phép biến đổi tương đương sau:

${a^{f\left( x \right)}} = {a^{g\left( x \right)}} \Leftrightarrow a = 1$ hoặc 
$$
\left\{ \begin{array}{l}
0 < a \ne 1\\
f\left( x \right) = g\left( x \right)
\end{array} \right.
$$

Logarit hóa và đưa về cùng cơ số:

+ Dạng 1: Phương trình: 
$$
{a^{f\left( x \right)}} = b \Leftrightarrow \left\{ \begin{array}{l}
0 < a \ne 1,b > 0\\
f\left( x \right) = {\log _a}b
\end{array} \right.
$$

+ Dạng 2: Phương trình:

${a^{f\left( x \right)}} = {b^{g\left( x \right)}}$ $\Leftrightarrow {\log _a}{a^{f\left( x \right)}} = {\log _a}{b^{f\left( x \right)}}$ $\Leftrightarrow f\left( x \right) = g\left( x \right).{\log _a}b$ hoặc ${a^{f\left( x \right)}} = {b^{g\left( x \right)}}$ $⇔ {\log _b}{a^{f\left( x \right)}} = {\log _b}{b^{g\left( x \right)}}$ $\Leftrightarrow f\left( x \right).{\log _b}a = g\left( x \right).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 1. Giải các phương trình:

1. ${2^{{x^2} – x + 8}} = {4^{1 – 3x}}.$

2. ${5^{x + 1}} – {5^x} = {2^{x + 1}} + {2^{x + 3}}.$

1. ${2^{{x^2} – x + 8}} = {4^{1 – 3x}}$ $\Leftrightarrow {2^{{x^2} – x + 8}} = {2^{2\left( {1 – 3x} \right)}}$ $\Leftrightarrow {x^2} – x + 8 = 2\left( {1 – 3x} \right)$ $\Leftrightarrow {x^2} + 5x + 6 = 0$ $\Leftrightarrow x = – 2, x = – 3.$

Vậy, phương trình cho có nghiệm $x = – 2, x = – 3.$

2. ${5^{x + 1}} – {5^x} = {2^{x + 1}} + {2^{x + 3}}$ $\Leftrightarrow {5.5^x} – {5^x} = {2.2^x} + {2^3}{.2^x}$

$\Leftrightarrow {4.5^x} = {10.2^x}$ $\Leftrightarrow {\left( {\frac{5}{2}} \right)^x} = \frac{{10}}{4} = \frac{5}{2}$ $\Leftrightarrow x = 1.$

Vậy, phương trình cho có nghiệm $x = 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 2.Giải các phương trình:

1. ${8^{\frac{x}{{x + 2}}}} = {36.3^{2 – x}}.$

2. $\sqrt {{2^x}.\sqrt[3]{{{4^x}}}.\sqrt[{3{\rm{x}}}]{{0.125}}} = 4\sqrt[3]{2}.$

1. Điều kiện: $x \ne – 2.$

Phương trình đã cho $\Leftrightarrow {2^{\frac{{3x}}{{x + 2}}}} = {2^2}{.3^{4 – x}}$ $\Leftrightarrow {2^{\frac{{x – 4}}{{x + 2}}}} = {3^{4 – x}}$ $\Leftrightarrow \frac{{x – 4}}{{x + 2}}{\log _3}2 = 4 – x$

$\Leftrightarrow \left( {x – 4} \right)\left( {x + 2 + {{\log }_3}2} \right) = 0$ $\Leftrightarrow x = 4$ hoặc $x = – 2 – {\log _3}2.$

Vậy, phương trình cho có nghiệm: $x = 4$ hoặc $x = – 2 – {\log _3}2.$

2. Điều kiện: 
$$
\left\{ \begin{array}{l}
x \ge \frac{1}{3}\\
3x \in N
\end{array} \right.
$$

Vì các cơ số của các lũy thừa đều viết được dưới dạng lũy thừa cơ số $2$ nên ta biến đổi hai vế của phương trình về lũy thừa cơ số $2$ và so sánh hai số mũ.

Phương trình $\Leftrightarrow \sqrt {{2^x}{{.2}^{2.\frac{x}{3}}}.{{\left( {\frac{1}{8}} \right)}^{\frac{1}{{{\rm{3x}}}}}}}$ $= {2^2}{.2^{\frac{1}{3}}}$ $\Leftrightarrow {2^{\frac{x}{2}}}{.2^{\frac{x}{3}}}{2^{\frac{{ – 1}}{{{\rm{2x}}}}}} = {2^{\frac{7}{3}}}$

$\Leftrightarrow {2^{\frac{x}{2} + \frac{x}{3} – \frac{1}{{2x}}}} = {2^{\frac{7}{3}}}$ $\Leftrightarrow \frac{x}{2} + \frac{x}{3} – \frac{1}{{2x}} = \frac{7}{3}$ $\Leftrightarrow 5{x^2} – 14x – 3 = 0$ $\Leftrightarrow x = – \frac{1}{5}$ hoặc $x = 3.$

Kết hợp với điều kiện ta có $x = 3$ là nghiệm của phương trình.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 3. Giải phương trình: ${4^{{x^2} – 3x + 2}} + {4^{2{x^2} + 6x + 5}}$ $= {4^{3{x^2} + 3x + 7}} + 1.$

Phương trình đã cho $\Leftrightarrow {4^{{x^2} – 3x + 2}} + {4^{2{x^2} + 6x + 5}}$ $= {4^{{x^2} – 3x + 2}}{.4^{2{x^2} + 6x + 5}} + 1$

$\Leftrightarrow {4^{{x^2} – 3x + 2}} – 1 + {4^{2{x^2} + 6x + 5}}$ $– {4^{{x^2} – 3x + 2}}{.4^{2{x^2} + 6x + 5}} = 0$

$\Leftrightarrow \left( {{4^{{x^2} – 3x + 2}} – 1} \right)\left( {{4^{2{x^2} + 6x + 5}} – 1} \right) = 0.$

${4^{{x^2} – 3x + 2}} = 1$ $\Rightarrow {x^2} – 3x + 2 = 0$ $\Leftrightarrow x = 1$ hoặc $x = 2.$

${4^{2{x^2} + 6x + 5}} = 1$ $\Rightarrow 2{x^2} + 6x + 5 = 0$, phương trình này vô nghiệm.

Vậy, phương trình cho có $2$ nghiệm: $x = 1$, $x = 2.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Dạng 2. Đặt ẩn phụ
Phương pháp: $f\left[ {{a^{g\left( x \right)}}} \right] = 0$ $\left( {0 < a \ne 1} \right)$ 
$$
\Leftrightarrow {\rm{ }}\left\{ \begin{array}{l}
t = {a^{g\left( x \right)}} > 0\\
f\left( t \right) = 0
\end{array} \right.
$$

+ Dạng 1: Ta có dạng tổng quát của bài toán trên là: $F\left( {{a^{f\left( x \right)}}} \right) = 0.$ Với dạng này ta đặt $t = {a^{f\left( x \right)}}$, $t > 0$ và chuyển về phương trình $F\left( t \right) = 0$, giải tìm nghiệm dương $t$ của phương trình, từ đó ta tìm được $x.$ Ta thường gặp dạng: $m.{a^{2f\left( x \right)}} + n.{a^{f\left( x \right)}} + p = 0.$ Với bất phương trình ta cũng làm tương tự.

+ Dạng 2: $m.{a^{f\left( x \right)}} + n.{b^{f\left( x \right)}} + p = 0$, trong đó $a.b = 1.$

Đặt $t = {a^{f\left( x \right)}}$, $t > 0$ $\Rightarrow {b^{f\left( x \right)}} = \frac{1}{t}.$

+ Dạng 3: $m.{a^{2f\left( x \right)}} + n.{\left( {a.b} \right)^{f\left( x \right)}} + p.{b^{2f\left( x \right)}} = 0$. Chia $2$ vế phương trình cho ${b^{2f\left( x \right)}}$ và đặt $t = {\left( {\frac{a}{b}} \right)^{f\left( x \right)}}$, $t > 0$. Ta có phương trình: $m{t^2} + nt + p = 0.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 4. Giải các phương trình:

1. ${2.16^x} – {15.4^x} – 8 = 0.$

2. ${2^{3x}} – {6.2^x} – \frac{1}{{{2^{3(x – 1)}}}} + \frac{{12}}{{{2^x}}} = 1.$

1. Đặt $t = {4^x}, t > 0$ ta có phương trình $2{t^2} – 15t – 8 = 0$ $\Leftrightarrow t = 8, t = – \frac{1}{2}$ (loại).

Với $t = 8$ $\Leftrightarrow {2^x} = {2^3} \Leftrightarrow x = 3.$

Vậy, phương trình cho có nghiệm $x = 3.$

2. Đặt $t = {2^x}, t > 0$ ta có: ${t^3} – 6t – \frac{8}{{{t^3}}} + \frac{{12}}{t} = 1$ $\Leftrightarrow \left( {{t^3} – \frac{8}{{{t^3}}}} \right) – 6\left( {t – \frac{2}{t}} \right) – 1 = 0.$

Đặt $y = t – \frac{2}{t}$ $\Rightarrow {t^3} – \frac{8}{{{t^3}}}$ $= \left( {t – \frac{2}{t}} \right)\left( {{t^2} + \frac{4}{{{t^2}}} + 2} \right)$ $= \left( {t – \frac{2}{t}} \right)\left[ {{{(t – \frac{2}{t})}^2} + 6} \right]$ $= y({y^2} + 6).$

Nên ta có phương trình: ${y^3} – 1 = 0 \Leftrightarrow y = 1$ $\Leftrightarrow t – \frac{2}{t} = 1$

$\Leftrightarrow {t^2} – t – 2 = 0$ $\Leftrightarrow t = 2 \Leftrightarrow x = 1.$

Vậy, phương trình cho có nghiệm $x = 1.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 5. Giải các phương trình:

1. ${3.8^x} + {4.12^x} – {18^x} – {2.27^x} = 0.$

2. ${9^{ – {x^2} + 2x + 1}} – {34.15^{2x – {x^2}}}$ $+ {25^{2x – {x^2} + 1}} = 0.$

1. Phương trình đã cho $\Leftrightarrow 3{\left( {\frac{2}{3}} \right)^{3x}} + 4.{\left( {\frac{2}{3}} \right)^{2x}} – {\left( {\frac{2}{3}} \right)^x} – 2 = 0.$

Đặt $t = {\left( {\frac{2}{3}} \right)^x}, t > 0$ ta được: $3{t^3} + 4{t^2} – t – 2 = 0$ $\Leftrightarrow (t + 1)(3{t^2} + t – 2) = 0$ $\Leftrightarrow t = \frac{2}{3} \Leftrightarrow x = 1.$

Vậy, phương trình cho có nghiệm $x = 1.$

2. Phương trình $\Leftrightarrow {9.9^{2x – {x^2}}} – {34.15^{2x – {x^2}}} + {25.25^{2x – {x^2}}} = 0$

$\Leftrightarrow 9{\left( {\frac{3}{5}} \right)^{2(2x – {x^2})}} – 34{\left( {\frac{3}{5}} \right)^{2x – {x^2}}} + 25 = 0.$

Đặt $t = {\left( {\frac{3}{5}} \right)^{2{\rm{x}} – {x^2}}}, t > 0.$

Ta có phương trình: $9{t^2} – 34t + 25 = 0$ $\Leftrightarrow t = 1$ hoặc $t = \frac{{25}}{9}.$

+ Với $t = 1 \Leftrightarrow {\left( {\frac{3}{5}} \right)^{2x – {x^2}}} = 1$ $\Leftrightarrow 2x – {x^2} = 0$ $\Leftrightarrow x = 0; x = 2.$

+ Với $t = \frac{{25}}{9} \Leftrightarrow {\left( {\frac{3}{5}} \right)^{2x – {x^2}}} = {\left( {\frac{3}{5}} \right)^{ – 2}}$ $\Leftrightarrow {x^2} – 2x – 2 = 0$ $\Leftrightarrow x = 1 \pm \sqrt 3 .$

Vậy phương trình đã cho có các nghiệm $x = 0; x = 2; x = 1 \pm \sqrt 3 .$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 6. Giải các phương trình:

1. ${2^{2{x^2} + 1}} – {9.2^{{x^2} + x}} + {2^{2x + 2}} = 0.$

2. $\frac{8}{{{2^{x – 1}} + 1}} + \frac{{{2^x}}}{{{2^x} + 2}} = \frac{{18}}{{{2^{x – 1}} + {2^{1 – x}} + 2}}.$

1. Chia cả $2$ vế phương trình cho ${2^{2x + 2}} \ne 0$ ta được:

${2^{2{x^2} – 2x – 1}} – {9.2^{{x^2} – 2x – 2}} + 1 = 0$ $\Leftrightarrow \frac{1}{2}{.2^{2{x^2} – 2x}} – \frac{9}{4}{.2^{{x^2} – x}} + 1 = 0$

$\Leftrightarrow {2.2^{2{x^2} – 2x}} – {9.2^{{x^2} – x}} + 4 = 0.$

Đặt $t = {2^{{x^2} – x}}, t > 0.$ Khi đó phương trình cho viết lại:

$2{t^2} – 9t + 4 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = 4\\
t = \frac{1}{2}
\end{array} \right.
$$
 
$$
\Rightarrow \left[ \begin{array}{l}
{2^{{x^2} – x}} = {2^2}\\
{2^{{x^2} – x}} = {2^{ – 1}}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – x = 2\\
{x^2} – x = – 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 1\\
x = 2
\end{array} \right.
$$

Vậy phương trình có $2$ nghiệm $x = – 1, x = 2.$

Chú ý: Để ý bài toán cho không có tham số nên ta sử dụng điều kiện cho ẩn phụ chỉ là $t > 0$ và nếu $t = \frac{1}{2}$ vô nghiệm. Nếu bài toán có chứa tham số thì điều kiện đúng của: ${x^2} – x = {\left( {x – \frac{1}{2}} \right)^2} – \frac{1}{4} \ge – \frac{1}{4}$ $\Leftrightarrow {2^{{x^2} – x}} \ge {2^{\frac{1}{4}}} \Leftrightarrow t \ge \frac{1}{{\sqrt[4]{2}}}.$

2. Phương trình cho viết lại: $\frac{8}{{{2^{x – 1}} + 1}} + \frac{1}{{{2^{1 – x}} + 1}} = \frac{{18}}{{{2^{x – 1}} + {2^{1 – x}} + 2}}$ $(*).$

Đặt: $u = {2^{x – 1}} + 1$, $v = {2^{1 – x}} + 1$ $\left( {u,v > 1} \right).$

Phương trình $(*)$ trở thành: 
$$
\left\{ \begin{array}{l}
\frac{8}{u} + \frac{1}{v} = \frac{{18}}{{u + v}}\\
u + v = uv
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
u + 8v = 18\\
u + v = uv
\end{array} \right.
$$
 $\Leftrightarrow u = v = 2$ hoặc $u = 9; v = \frac{9}{8}.$

+ Với $u = v = 2$, ta được 
$$
\left\{ \begin{array}{l}
{2^{x – 1}} + 1 = 2\\
{2^{1 – x}} + 1 = 2
\end{array} \right. \Leftrightarrow x = 1.
$$

+ Với $u = 9; v = \frac{9}{8}$, ta được 
$$
\left\{ \begin{array}{l}
{2^{x – 1}} + 1 = 9\\
{2^{1 – x}} + 1 = \frac{9}{8}
\end{array} \right. \Leftrightarrow x = 4.
$$

Vậy, phương trình đã cho có nghiệm $x = 1, x = 4.$

[ads]

<!-- chunk:10 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Dạng 3. Logarit hóa
Phương pháp:

+ Dạng 1: ${a^{g\left( x \right)}} = f\left( x \right)$ $\left( {0 < a \ne 1} \right)$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
f\left( x \right) > 0\\
g\left( x \right) = {\log _a}f\left( x \right)
\end{array} \right.
$$

+ Dạng 2: ${a^{f\left( x \right)}} = {b^{g\left( x \right)}}$ $\left( {0 < a, b \ne 1} \right)$ $\Leftrightarrow {\log _a}{a^{f\left( x \right)}} = {\log _a}{b^{g\left( x \right)}}$ $\Leftrightarrow f\left( x \right) = g\left( x \right).{\log _a}b.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 7. Giải các phương trình:

1. ${({x^2} + 1)^{\left| {{x^2} – 5x + 4} \right|}} = {({x^2} + 1)^{x + 4}}.$

2. ${5^x}{.8^{\frac{{x – 1}}{x}}} = 500.$

1. Phương trình 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + 1 = 1\\
\left| {{x^2} – 5x + 4} \right| = x + 4
\end{array} \right.
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
x = 0\\
\left\{ \begin{array}{l}
x \ge – 4\\
{({x^2} – 5x + 4)^2} – {(x + 4)^2} = 0
\end{array} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 0\\
\left\{ \begin{array}{l}
x \ge – 4\\
({x^2} – 4x + 8)({x^2} – 6x) = 0
\end{array} \right.
\end{array} \right.
$$
 $\Leftrightarrow x = 0, x = 6$ là nghiệm của phương trình đã cho.

Chú ý: Lấy logarit $2$ vế, bài toán cho lời giải đẹp.

2.

Cách 1: ${5^x}{.8^{\frac{{x – 1}}{8}}} = 500$ $\Leftrightarrow {5^x}{.2^{3\frac{{x – 1}}{x}}} = {5^3}{.2^2}$ $\Leftrightarrow {5^{x – 3}}{.2^{\frac{{x – 3}}{x}}} = 1.$

Lấy logarit cơ số $2$ vế, ta được: ${\log _2}\left( {{5^{x – 3}}{{.2}^{\frac{{x – 3}}{x}}}} \right) = 0$ $\Leftrightarrow {\log _2}\left( {{5^{x – 3}}} \right) + {\log _2}\left( {{2^{\frac{{x – 3}}{x}}}} \right) = 0$

$\Leftrightarrow \left( {x – 3} \right).{\log _2}5 + \frac{{x – 3}}{x}{\log _2}2 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 3\\
x = – \frac{1}{{{{\log }_2}5}} = – {\log _5}2
\end{array} \right.
$$

Vậy phương trình có $2$ nghiệm phân biệt: $x = 3, x = – {\log _5}2.$

Cách 2: Phương trình đã cho $\Leftrightarrow {5^x}{.2^{\frac{{3\left( {x – 1} \right)}}{x}}} = {5^3}{.2^2}$ $\Leftrightarrow {5^{x – 3}} = {2^{\frac{{3 – x}}{x}}}$ $\Leftrightarrow {5^{x – 3}} = {\left( {{2^{ – \frac{1}{x}}}} \right)^{x – 3}}$

$\Leftrightarrow {5^{x – 3}} = {\left( {\frac{1}{{{2^{\frac{1}{x}}}}}} \right)^{x – 3}}$ $\Leftrightarrow {\left( {{{5.2}^{\frac{1}{x}}}} \right)^{x – 3}} = 1$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x – 3 = 0\\
{5.2^{\frac{1}{x}}} = 1
\end{array} \right. \Leftrightarrow \left[ \begin{array}{l}
x = 3\\
x = – {\log _5}2
\end{array} \right.
$$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 8. Giải các phương trình:

1. ${x^6}{.5^{ – {{\log }_x}5}} = {5^{ – 5}}.$

2. ${49.2^{{x^2}}} = {16.7^x}.$

3. ${8^x}{.5^{{x^2} – 1}} = {2^{ – 3}}.$

1. Điều kiện: $0 < x \ne 1.$

Lấy logarit cơ số $5$ cả hai vế phương trình cho ta được:

${\log _5}\left( {{x^6}{{.5}^{ – {{\log }_x}5}}} \right) = {\log _5}{5^{ – 5}}$ hay $6{\log _5}x – {\log _x}5 = – 5$

$\Leftrightarrow 6{\left( {{{\log }_5}x} \right)^2} + 5{\log _5}x – 1 = 0$ $(*).$

Đặt $t = {\log _5}x$, phương trình $(*)$ trở thành $6{t^2} + 5t – 1 = 0$, phương trình này có hai nghiệm $t = – 1$ hoặc $t = \frac{1}{6}.$

+ Với $t = – 1$ tức ${\log _5}x = – 1$ $\Leftrightarrow x = {5^{ – 1}} = \frac{1}{5}.$

+ Với $t = \frac{1}{6}$ tức ${\log _5}x = \frac{1}{6}$ $\Leftrightarrow x = {5^{\frac{1}{5}}} = \sqrt[6]{5}.$

Vậy, phương trình cho có $2$ nghiệm: $x \in \left\{ {\sqrt[6]{5};\frac{1}{5}} \right\}.$

2. Phương trình cho tương đương ${2^{{x^2} – 4}} = {7^{x – 2}}$ $(*).$

Lấy logarit cơ số $2$ hai vế phương trình $(*)$ ta được: ${\log _2}{2^{{x^2} – 4}} = {\log _2}{7^{x – 2}}$

$\Leftrightarrow {x^2} – 4 = \left( {x – 2} \right){\log _2}7$ $\Leftrightarrow \left( {x – 2} \right)\left( {x + 2 – {{\log }_2}7} \right) = 0$

$\Leftrightarrow x = 2$ hoặc $x = {\log _2}7 – 2.$

Vậy, phương trình đã cho có nghiệm $x = {\log _2}7 – 2$, $x = 2.$

3. Lấy logarit hai vế với cơ số $8$, ta được:

${\log _8}{8^x}{.5^{{x^2} – 1}} = {\log _8}\frac{1}{8}$ $\Leftrightarrow {\log _8}{8^x} + {\log _8}{5^{{x^2} – 1}} = {\log _8}{8^{ – 1}}$

$\Leftrightarrow x + \left( {{x^2} – 1} \right){\log _8}5 = – 1$ $\Leftrightarrow x + 1 + \left( {{x^2} – 1} \right){\log _8}5 = 0$

$\Leftrightarrow \left( {x + 1} \right) + \left( {x + 1} \right)\left( {x – 1} \right){\log _8}5 = 0$ $\Leftrightarrow \left( {x + 1} \right)\left[ {1 + \left( {x – 1} \right){{\log }_8}5} \right] = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
x + 1 = 0\\
1 + \left( {x – 1} \right){\log _8}5 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 1\\
x.{\log _8}5 = {\log _8}5 – 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 1\\
x = 1 – {\log _5}8
\end{array} \right.
$$

Vậy phương trình có nghiệm: $x = – 1, x = 1 – {\log _5}8.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-1.html -->
## Ví dụ 9. Giải các phương trình:

1. ${3.4^x} + (3x – 10){2^x} + 3 – x = 0.$

2. ${9^x} – 2\left( {x + 5} \right){.3^x} + 9\left( {2x + 1} \right) = 0.$

1. Đặt $t = {2^x}, t > 0$, ta có phương trình:

$3{t^2} + (3x – 10)t + 3 – x = 0$ $(1).$

Ta xem $(1)$ là phương trình bậc hai ẩn $t$ và $x$ là tham số.

Phương trình này có: $\Delta = {(3x – 10)^2} – 12(3 – x) = {(3x – 8)^2}$

$\Rightarrow (1) \Leftrightarrow t = \frac{1}{3}$ hoặc $t = – x + 3.$

+ Với $t = \frac{1}{3} \Leftrightarrow {2^x} = \frac{1}{3} \Leftrightarrow x = – {\log _2}3.$

+ Với $t = – x + 3$ $\Leftrightarrow {2^x} + x = 3 \Leftrightarrow x = 1$ (Do $VT$ là một hàm đồng biến).

Vậy phương trình đã cho có hai nghiệm: $x = – {\log _2}3; x = 1.$

2. Đặt $t = {3^x},$ $t > 0.$

Phương trình cho trở thành: ${t^2} – 2\left( {x + 5} \right)t + 9\left( {2x + 1} \right) = 0$ $(*)$, phương trình này có biệt số $\Delta’ = {\left( {x + 5} \right)^2} – 9\left( {2x + 1} \right) = {\left( {x – 4} \right)^2}.$

Vì $\Delta’ \ge 0$ nên phương trình $(*)$ có $2$ nghiệm: $t = 9$ hoặc $t = 2x + 1.$

+ Với $t = 9$ tức ${3^x} = 9 ⇔ x = 2.$

+ Với $t = 2x + 1$ tức ${3^x} = 2x + 1$ $⇔x = 0$ hoặc $x = 1$ (Phương trình ${3^x} = 2x + 1$ có thể giải bằng phương pháp xét tính đơn điệu của hàm số $f(x) = 3^x – 2x – 1$ sẽ được đề cập ở dạng 5).

Vậy, phương trình cho có $3$ nghiệm: $x = 0$, $x = 1$, $x = 2.$

**XEM TIẾP PHẦN 2**: Phương pháp giải phương trình mũ và bất phương trình mũ (Phần 2)