# Phương pháp giải phương trình logarit và bất phương trình logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
Bài viết phân dạng và hướng dẫn phương pháp giải các dạng toán phương trình logarit và bất phương trình logarit trong chương trình Giải tích 12 chương 2, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu lũy thừa – mũ – logarit được đăng tải trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## A. KIẾN THỨC CẦN GHI NHỚ

1. ${\log _a}f\left( x \right) = {\log _a}g\left( x \right)$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
f\left( x \right) = g\left( x \right)\\
f\left( x \right) \ge 0{\rm{ }}\left( {g\left( x \right) \ge 0} \right)
\end{array} \right.
$$

2. ${\log _a}f\left( x \right) = b \Leftrightarrow f\left( x \right) = {a^b}.$

3. ${\log _a}f\left( x \right) > {\log _a}g\left( x \right)$ $(*).$

+ Nếu $a > 1$ thì 
$$
\left( * \right) \Leftrightarrow \left\{ \begin{array}{l}
f\left( x \right) > g\left( x \right)\\
g\left( x \right) > 0
\end{array} \right.
$$

+ Nếu $0 < a < 1$ thì 
$$
\left( * \right) \Leftrightarrow \left\{ \begin{array}{l}
f\left( x \right) < g\left( x \right)\\
f\left( x \right) > 0
\end{array} \right.
$$

Chú ý: ${\log _a}f\left( x \right)$ có nghĩa 
$$
\Leftrightarrow \left\{ \begin{array}{l}
f\left( x \right) > 0\\
0 < a \ne 1
\end{array} \right.
$$

<!-- chunk:2 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Dạng 1. Biến đổi, quy về cùng cơ số
Phương pháp:

${\log _a}f\left( x \right) = {\log _a}g\left( x \right)$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
0 < a \ne 1\\
f\left( x \right) = g\left( x \right) > 0
\end{array} \right.
$$

Phương trình logarit cơ bản: ${\log _a}x = b$, $\left( {0 < a \ne 1} \right).$

* ${\log _a}x = b \Leftrightarrow x = {a^b}$, $\left( {0 < a \ne 1} \right)$.

* $\lg x = b \Leftrightarrow x = {10^b}$, $\ln x = b \Leftrightarrow x = {e^b}$.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 1. Giải các phương trình:

1. ${\log _{25}}{\left( {4x + 5} \right)^2} + {\log _5}x = {\log _3}27.$

2. ${\log _2}x + {\log _3}x + {\log _4}x = {\log _{20}}x.$

1. Điều kiện: $x > 0.$

Phương trình đã cho trở thành: ${\log _5}\left( {4x + 5} \right) + {\log _5}x = 3$ $\Leftrightarrow {\log _5}(4{x^2} + 5x) = 3$ $\Leftrightarrow 4{x^2} + 5x = 125$ $\Leftrightarrow x = 5$ hoặc $x = \frac{{25}}{4}.$

Vậy, phương trình đã cho có nghiệm $x = 5$ hoặc $x = \frac{{25}}{4}.$

2. Điều kiện $x > 0.$ Bài toán áp dụng công thức đổi cơ số ${\log _a}x = \frac{{{{\log }_b}x}}{{{{\log }_b}a}}.$

Phương trình đã cho $\Leftrightarrow {\log _2}x + \frac{{{{\log }_2}x}}{{{{\log }_2}3}} + \frac{{{{\log }_2}x}}{{{{\log }_2}4}} = \frac{{{{\log }_2}x}}{{{{\log }_2}20}}$

$\Leftrightarrow {\log _2}x\left( {1 + \frac{1}{{{{\log }_2}3}} + \frac{1}{{{{\log }_2}4}} – \frac{1}{{{{\log }_2}20}}} \right) = 0$ $\Leftrightarrow {\log _2}x = 0 \Leftrightarrow x = 1.$

Vậy, phương trình đã cho có nghiệm $x = 1.$

Chú ý: Ngoài ra bài toán trên ta có thể dùng công thức ${\log _a}x = \frac{{\ln x}}{{\ln a}}$ sẽ giải quyết nhanh gọn và đẹp hơn.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 2. Giải phương trình: ${\log _3}{\left( {x – 2} \right)^2} + {\log _{\sqrt 3 }}\frac{x}{{{x^2} – 3x + 3}} = 0.$

Điều kiện: $0 < x \ne 2.$

Phương trình đã cho viết lại ${\log _3}{\left( {x – 2} \right)^2} + {\log _3}{\left( {\frac{x}{{{x^2} – 3x + 3}}} \right)^2} = 0$

$\Leftrightarrow {\log _3}\left[ {{{\left( {x – 2} \right)}^2}.{{\left( {\frac{x}{{{x^2} – 3x + 3}}} \right)}^2}} \right] = 0$

$\Leftrightarrow {\left( {x – 2} \right)^2}.{\left( {\frac{x}{{{x^2} – 3x + 3}}} \right)^2} = 1.$

Giải phương trình này ta được $x = 1, x = \frac{3}{2}, x = 3.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 3. Giải phương trình: ${\log _2}\left( {8 – {x^2}} \right)$ $+ {\log _{\frac{1}{2}}}\left( {\sqrt {1 + x} + \sqrt {1 – x} } \right) – 2 = 0.$

Với $x \in \left[ { – 1;1} \right]$ phương trình đã cho viết lại: ${\log _2}\left( {8 – {x^2}} \right)$ $= 2 + {\log _2}\left( {\sqrt {1 + x} + \sqrt {1 – x} } \right)$

$\Leftrightarrow 8 – {x^2} = 4\left( {\sqrt {1 + x} + \sqrt {1 – x} } \right)$ $(*).$

Đặt $t = \sqrt {1 + x} + \sqrt {1 – x}$, phương trình $(*)$ trở thành: ${\left( {{\rm{t}} – {\rm{2}}} \right)^{\rm{2}}}\left( {{{\rm{t}}^{\rm{2}}} + {\rm{4t}} + {\rm{8}}} \right) = 0$, phương trình này có nghiệm $t = 2$ hay $\sqrt {1 + x} + \sqrt {1 – x} = 2$. Bình phương $2$ vế và rút gọn ta được $x = 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 4. Giải phương trình: $\lg \sqrt {1 + x} + 3\lg \sqrt {1 – x} – 2 = \lg \sqrt {1 – {x^2}} .$

Điều kiện: 
$$
\left\{ \begin{array}{l}
1 + x > 0\\
1 – x > 0\\
1 – {x^2} > 0
\end{array} \right.
$$
 $\Leftrightarrow – 1 < x < 1.$

Để ý: $\lg \sqrt {1 – {x^2}} = \lg \sqrt {1 + x} \sqrt {1 – x}$ $= \lg \sqrt {1 + x} + \lg \sqrt {1 – x} .$

Phương trình đã cho $\Leftrightarrow \lg \sqrt {1 + x} + 3\lg \sqrt {1 – x} – 2$ $= \lg \sqrt {1 + x} + \lg \sqrt {1 – x}$

$\Leftrightarrow \lg \sqrt {1 – x} = 1$ $\Leftrightarrow \sqrt {1 – x} = 10$ $\Leftrightarrow 1 – x = 100 \Leftrightarrow x = – 99.$

Kết hợp với điều kiện suy ra phương trình vô nghiệm.

<!-- chunk:7 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Dạng 2. Đặt ẩn phụ
Phương pháp: $f\left[ {{{\log }_a}g\left( x \right)} \right] = 0$ $\left( {0 < a \ne 1} \right)$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
t = {\log _a}g\left( x \right)\\
f\left( t \right) = 0
\end{array} \right.
$$

Ta chú ý công thức đổi cơ số: ${\log _b}x = \frac{{{{\log }_a}x}}{{{{\log }_a}b}}$ $\Rightarrow {\log _a}b = \frac{1}{{{{\log }_b}a}}$ $\forall a, b, x > 0; a, b \ne 1.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 5. Giải các phương trình:

1. ${\log _2}x + \sqrt {10{{\log }_2}x + 6} = 9.$

2. $\sqrt {{{\log }_9}x + 1} + \sqrt {{{\log }_3}x + 3} = 5.$

3. ${4^{{{\log }_2}2{\rm{x}}}} – {x^{{{\log }_2}6}} = {2.3^{{{\log }_2}4{x^2}}}.$

1. Điều kiện: $x > 0$ và $10{\log _2}x + 6 \ge 0.$

Đặt $t = {\log _2}x$, phương trình đã cho đưa về dạng: $\sqrt {10t + 6} = 9 – t$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
9 – t \ge 0\\
10t + 6 = {\left( {9 – t} \right)^2}
\end{array} \right.
$$
 từ đây ta tìm được $t = 3$ tức $x = 8.$

Vậy, phương trình cho có nghiệm $x = 8.$

2. Điều kiện: $x > 0$ và ${\log _3}x + 3 \ge 0,$ ${\log _9}x + 1 \ge 0.$

Đặt $t = {\log _3}x$, phương trình đã cho về dạng $\sqrt {\frac{1}{2}t + 1} + \sqrt {t + 3} = 5$ $(1).$

Với điều kiện $t \ge – 2$, bình phương hai vế của $(1)$ và rút gọn ta được: $\sqrt {\frac{1}{2}{t^2} + \frac{5}{2}t + 3} = 21 – \frac{3}{2}t$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
– 2 \le t \le 14\\
{t^2} – 292t + 1716 = 0
\end{array} \right.
$$
 $⇒t = 6$ tức $x = 64.$

Vậy, phương trình cho có nghiệm $x = 64.$

3. Điều kiện: $x > 0.$

Phương trình đã cho $\Leftrightarrow {4^{1 + {{\log }_2}x}} – {6^{{{\log }_2}x}} = {2.3^{2 + 2{{\log }_2}x}}$ $\Leftrightarrow {4.4^{{{\log }_2}x}} – {6^{{{\log }_2}x}} – {18.9^{{{\log }_2}x}} = 0$ $\Leftrightarrow 4.{\left( {\frac{2}{3}} \right)^{{{\log }_2}x}} – {\left( {\frac{2}{3}} \right)^{{{\log }_2}x}} – 18 = 0.$

Đặt $t = {\left( {\frac{2}{3}} \right)^{{{\log }_2}x}}, t > 0$, ta có: $4{t^2} – t – 18 = 0 \Leftrightarrow t = \frac{9}{4}$ $\Leftrightarrow {\left( {\frac{2}{3}} \right)^{{{\log }_2}x}} = \frac{9}{4} = {\left( {\frac{2}{3}} \right)^{ – 2}}$ $\Leftrightarrow {\log _2}x = – 2 \Leftrightarrow x = \frac{1}{4}.$

Vậy, phương trình đã cho có nghiệm $x = \frac{1}{4}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 6. Giải phương trình: ${\log _2}x{\left( {x – 1} \right)^2}$ $+ {\log _2}x.{\log _2}\left( {{x^2} – x} \right) – 2 = 0.$

Điều kiện: $x > 1.$

Biến đổi phương trình về dạng:

${\log _2}\frac{{{{\left( {{x^2} – x} \right)}^2}}}{x}$ $+ {\log _2}x.{\log _2}\left( {{x^2} – x} \right) – 2 = 0$

$\Leftrightarrow 2{\log _2}\left( {{x^2} – x} \right) – {\log _2}x$ $+ {\log _2}x.{\log _2}\left( {{x^2} – x} \right) – 2 = 0$ $(*).$

Đặt $u = {\log _2}\left( {{x^2} – x} \right)$ và $v = {\log _2}x.$ Đưa phương trình $(*)$ về phương trình:

$\left( {u – 1} \right)\left( {v + 2} \right) = 0$

$\Leftrightarrow u = 1$ hoặc $v = – 2.$

+ Với $u = 1$ thì ${\log _2}\left( {{x^2} – x} \right) = 1$ $\Leftrightarrow {x^2} – x = 2 \Leftrightarrow x = 2.$

+ Với $v = – 2$ thì ${\log _2}x = – 2 \Leftrightarrow x = \frac{1}{4}$ (không thỏa mãn điều kiện).

Vậy, phương trình đã cho có nghiệm $x = 2.$

<!-- chunk:10 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Dạng 3. Biến đổi phương trình về dạng tích
Phương pháp: $f\left( x \right).g\left( x \right) = 0{\rm{ }}$ $\Leftrightarrow f\left( x \right) = 0$ hoặc $g\left( x \right) = 0.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 7. Giải phương trình: ${\log _3}x + {\log _4}x = {\log _5}x.$

Dễ thấy: ${\log _4}x = {\log _4}3.{\log _3}x$, ${\log _5}x = {\log _5}3.{\log _3}x.$

Với $x > 0$. Phương trình được viết dưới dạng:

${\log _3}x + {\log _4}3.{\log _3}x = {\log _5}3.{\log _3}x$ $\Leftrightarrow {\log _3}x = 0 \Leftrightarrow x = 1.$

Vậy, phương trình đã cho có nghiệm $x = 1.$

Ví dụ 8.  Giải các phương trình:

1. ${\log _{5x}}\frac{5}{x} + \log _5^2x = 1.$

2. ${\log _{{x^2}}}16 + {\log _{2x}}64 = 3{\rm{ }}.$

1. Điều kiện: $0 < x \ne \frac{1}{5}.$

Phương trình đã cho $\Leftrightarrow \frac{{{{\log }_5}\frac{5}{x}}}{{{{\log }_5}5x}} + \log _5^2x = 1$ $\Leftrightarrow \frac{{1 – {{\log }_5}x}}{{1 + {{\log }_5}x}} + \log _5^2x = 1$

$\Leftrightarrow {\log _5}x(\log _5^2x + {\log _5}x – 2) = 0$ $\Leftrightarrow {\log _5}x\left( {{{\log }_5}x – 1} \right)\left( {{{\log }_5}x + 2} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
{\log _5}x = 0\\
{\log _5}x = 1\\
{\log _5}x = – 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 1\\
x = 5\\
x = {5^{ – 2}}
\end{array} \right.
$$

Vậy phương trình có ba nghiệm: $x = 1; x = 5; x = \frac{1}{{25}}.$

2. Điều kiện: $0 < x \ne 1, x \ne \frac{1}{2}.$

Phương trình đã cho $\Leftrightarrow \frac{{{{\log }_2}16}}{{{{\log }_2}{x^2}}} + \frac{{{{\log }_2}64}}{{{{\log }_2}2x}} = 3$ $\Leftrightarrow \frac{2}{{{{\log }_2}x}} + \frac{6}{{1 + {{\log }_2}x}} = 3$

$\Leftrightarrow 3\log _2^2x – 5{\log _2}x – 2 = 0$ $\Leftrightarrow \left( {{{\log }_2}x – 2} \right)\left( {3{{\log }_2}x + 1} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
{\log _2}x = 2\\
{\log _2}x = – \frac{1}{3}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 4\\
x = \frac{1}{{\sqrt[3]{2}}}
\end{array} \right.
$$

Vậy phương trình đã cho có hai nghiệm: $x = 4; x = \frac{1}{{\sqrt[3]{2}}}.$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Dạng 4. Phương pháp đồ thị
Phương pháp:

Giải phương trình: ${\log _a}x = f\left( x \right)$ $\left( {0 < a \ne 1} \right)$ $(*).$

$(*)$ là phương trình hoành độ giao điểm của $2$ đồ thị $y = {\log _a}x$ $\left( {0 < a \ne 1} \right)$ và $y = f\left( x \right)$. Khi đó ta thực hiện 2 bước:

+ Bước 1: Vẽ đồ thị các hàm số: $y = {\log _a}x$ $\left( {0 < a \ne 1} \right)$ và $y = f\left( x \right).$

+ Bước 2: Kết luận nghiệm của phương trình đã cho là số giao điểm của  đồ thị.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 9. Giải phương trình: ${\log _3}\left[ {{{\left( {x + 1} \right)}^3} + 3{{\left( {x + 1} \right)}^2} + 3x + 4} \right]$ $= 2{\log _2}\left( {x + 1} \right).$

Điều kiện: $x > – 1.$

Phương trình đã cho tương đương ${\log _3}{\left( {x + 2} \right)^3} = 2{\log _2}\left( {x + 1} \right)$ hay $3{\log _3}\left( {x + 2} \right) = 2{\log _2}\left( {x + 1} \right).$

Đặt $3{\log _3}\left( {x + 2} \right) = 2{\log _2}\left( {x + 1} \right) = 6t$ suy ra 
$$
\left\{ {\begin{array}{c}
{x + 2 = {3^{2t}}}\\
{x + 1 = {2^{3t}}}
\end{array}} \right. \Rightarrow {9^t} – {8^t} = 1
$$
, tức ${\left( {\frac{1}{9}} \right)^t} + {\left( {\frac{8}{9}} \right)^t} = 1$ $(*).$

Xét hàm $f\left( t \right){\rm{ }} = {\left( {\frac{1}{9}} \right)^t} + {\left( {\frac{8}{9}} \right)^t}$, ta thấy hàm $f\left( t \right)$ nghịch biến, lại có $f\left( 1 \right) = 1$ nên $t = 1$ là nghiệm duy nhất của $(*).$

Vậy, phương trình đã cho có nghiệm duy nhất $x = 7.$

Ví dụ 10. Giải phương trình: ${\log _2}\left( {x + {3^{{{\log }_6}x}}} \right) = {\log _6}x.$

Đặt $t = {\log _6}x \Rightarrow x = {6^t}.$ Phương trình đã cho trở thành: ${6^t} + {3^t} = {2^t}$, chia cả $2$ vế cho ${2^t}.$

Xét hàm số $f\left( t \right) = {3^t} + {\left( {\frac{3}{2}} \right)^t} – 1$, vì $3 > \frac{3}{2} > 1$ nên $f\left( t \right)$ tăng và $f\left( { – 1} \right) = 0$, do đó $f\left( t \right) = 0$ xảy ra khi $t = – 1$ tức $x = \frac{1}{6}.$

Vậy, phương trình đã cho có nghiệm $x = \frac{1}{6}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 11. Giải phương trình: $\left( {3x – 5} \right)\log _3^2x$ $+ \left( {9x – 19} \right){\log _3}x – 12 = 0.$

Điều kiện: $x > 0.$

Đặt $t = {\log _3}x,$ phương trình trở thành: $\left( {3x – 5} \right){t^2} + \left( {9x – 19} \right)t – 12 = 0.$

Khi $x = \frac{5}{3}$, phương trình vô nghiệm.

Khi $x \ne \frac{5}{3}$, ta có: $\Delta = {\left( {9x – 11} \right)^2}$, khi đó phương trình có $2$ nghiệm $t = – 3$ hoặc $t = \frac{4}{{3x – 5}}.$

+ Với $t = – 3$ tức ${\log _3}x = – 3$ $\Leftrightarrow x = {3^{ – 3}} = \frac{1}{{27}}.$

+ Với $t = \frac{4}{{3x – 5}}$ tức ${\log _3}x = \frac{4}{{3x – 5}}$. Xét hàm số: $f\left( x \right) = {\log _3}x – \frac{4}{{3x – 5}}$ với $0 < x \ne \frac{5}{3}.$

Ta có: $f’\left( x \right) = \frac{1}{{x\ln 3}} + \frac{{12}}{{{{\left( {3x – 5} \right)}^2}}} > 0$, với mọi $0 < x \ne \frac{5}{3}.$

$\mathop {\lim }\limits_{x \to + \infty } f\left( x \right) = + \infty$, $\mathop {\lim }\limits_{x \to {{\left( {\frac{5}{3}} \right)}^ – }} f\left( x \right) = + \infty$, $\mathop {\lim }\limits_{x \to {{\left( {\frac{5}{3}} \right)}^ + }} f\left( x \right) = – \infty .$

Lập bảng biến thiên, dễ thấy phương trình $f\left( x \right) = 0$ luôn có $2$ nghiệm phân biệt, hơn nữa $f\left( 3 \right) = f\left( {\frac{1}{3}} \right) = 0$ nên phương trình $f\left( x \right) = 0$ luôn có $2$ nghiệm $x = \frac{1}{3}$ hoặc $x = 3.$

Vậy, phương trình có $3$ nghiệm: $x \in \left\{ {\frac{1}{{27}};\frac{1}{3};3} \right\}.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-logarit-va-bat-phuong-trinh-logarit.html -->
## Ví dụ 12. Giải bất phương trình:

1. ${\log _2}\left( {\sqrt {3x + 1} + 6} \right) – 1$ $\ge {\log _2}\left( {7 – \sqrt {10 – x} } \right).$

2. ${\log _2}\frac{{5 – 12x}}{{12x – 8}} + {\log _{\frac{1}{2}}}x \le 0.$

1. Điều kiện: 
$$
\left\{ \begin{array}{l}
3x + 1 \ge 0\\
10 – x \ge 0\\
7 – \sqrt {10 – x} > 0
\end{array} \right.
$$
 $\Leftrightarrow – \frac{1}{3} \le x \le 10.$

Bất phương trình tương đương với ${\log _2}\frac{{\sqrt {3x + 1} + 6}}{2}$ $\ge {\log _2}\left( {7 – \sqrt {10 – x} } \right)$

$\Leftrightarrow \sqrt {3x + 1} + 6 \ge 2\left( {7 – \sqrt {10 – x} } \right)$

$\Leftrightarrow \sqrt {3x + 1} + 2\sqrt {10 – x} \ge 8$

$\Leftrightarrow {\rm{49}}{{\rm{x}}^{\rm{2}}}–{\rm{ 418x }} + {\rm{ 369 }} \le {\rm{ }}0$

$\Leftrightarrow {\rm{1 }} \le {\rm{ x }} \le \frac{{369}}{{49}}$ (thoả điều kiện).

Vậy, bất phương trình đã cho có nghiệm ${\rm{1 }} \le {\rm{ x }} \le \frac{{369}}{{49}}.$

2. Bất phương trình đã cho tương đương với 
$$
\left\{ \begin{array}{l}
\frac{{5 – 12x}}{{12x – 8}} \le x\\
\frac{{5 – 12x}}{{12x – 8}} > 0
\end{array} \right.
$$

$$
\Leftrightarrow \left\{ \begin{array}{l}
\frac{{ – 12{x^2} – 4x + 5}}{{12x – 8}} \le 0\\
\frac{{5 – 12x}}{{12x – 8}} > 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\left[ \begin{array}{l}
– \frac{5}{6} \le x \le \frac{1}{2}\\
x > \frac{2}{3}
\end{array} \right.\\
\frac{5}{{12}} < x < \frac{2}{3}
\end{array} \right.
$$
 $\Leftrightarrow \frac{5}{{12}} < x \le \frac{1}{2}.$

Vậy, bất phương trình đã cho có nghiệm $\frac{5}{{12}} < x \le \frac{1}{2}.$