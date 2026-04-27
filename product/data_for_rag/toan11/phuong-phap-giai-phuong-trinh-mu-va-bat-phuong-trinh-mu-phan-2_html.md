# Phương pháp giải phương trình mũ và bất phương trình mũ (Phần 2)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
Bài viết phân dạng và hướng dẫn phương pháp giải các dạng toán phương trình mũ và bất phương trình mũ trong chương trình Giải tích 12 chương 2, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu lũy thừa – mũ – logarit được đăng tải trên TOANMATH.com.

**XEM LẠI PHẦN 1**: Phương pháp giải phương trình mũ và bất phương trình mũ (Phần 1)

<!-- chunk:1 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Dạng 5. Sử dụng tính đơn điệu của hàm số
Phương pháp:

Chuyển phương trình đã cho về dạng $f\left( x \right) = k.$

Nhẩm $1$ nghiệm $x = {x_0}$, ta chứng minh $x = {x_0}$ là nghiệm duy nhất.

Tính chất 1: Nếu hàm số $y = f\left( x \right)$ luôn đồng biến (hoặc luôn nghịch biến) trên $\left( {a;b} \right)$ thì số nghiệm của phương trình: $f\left( x \right) = k$ (trên $\left( {a;b} \right)$) không nhiều hơn một và $f\left( u \right) = f\left( v \right) \Leftrightarrow u = v$ $\forall u,v \in \left( {a;b} \right).$
Tính chất 2: Nếu hàm số $y = f\left( x \right)$ liên tục và luôn đồng biến (hoặc luôn nghịch biến); hàm số $y = g\left( x \right)$ liên tục và luôn nghịch biến (hoặc luôn đồng biến) trên $D$ thì số nghiệm trên $D$ của phương trình: $f\left( x \right) = g\left( x \right)$ không nhiều hơn một.

Tính chất 3: Nếu hàm số $y = f\left( x \right)$ luôn đồng biến (hoặc luôn nghịch biến) trên $D$ thì $f\left( u \right) > f\left( v \right) \Leftrightarrow u > v$ $(u < v)$ $\forall u,v \in D$.

Tính chất 4: Cho hàm số $y = f\left( x \right)$ liên tục trên $\left[ {a;b} \right]$ và có đạo hàm trên khoảng $\left( {a;b} \right).$ Nếu $f\left( a \right) = f\left( b \right)$ thì phương trình $f’\left( x \right) = 0$ có ít nhất một nghiệm thuộc khoảng $\left( {a;b} \right).$

Hệ quả 1: Nếu phương trình $f\left( x \right) = 0$ có $m$ nghiệm thì phương trình $f’\left( x \right) = 0$ có $m – 1$ nghiệm.

Hệ quả 2: Cho hàm số $y = f\left( x \right)$ có đạo hàm đến cấp $k$ liên tục trên $\left( {a;b} \right).$ Nếu phương trình ${f^{\left( k \right)}}\left( x \right) = 0$ có đúng $m$ nghiệm thì phương trình ${f^{\left( {k – 1} \right)}}\left( x \right) = 0$ có nhiều nhất là $m + 1$ nghiệm.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 10. Giải các phương trình:

1. ${\left( {\sqrt {15} } \right)^x} + 1 = {4^x}.$

2. ${4^x} + {5^x} = 9.$

3. $x + \sqrt {{x^2} + 1} = {5^x}.$

1. Phương trình đã cho $\Leftrightarrow {\left( {\frac{{\sqrt {15} }}{4}} \right)^x} + {\left( {\frac{1}{4}} \right)^x} = 1$ $(*).$

Ta thấy vế trái của $(*)$ là một hàm số nghịch biến và $x = 2$ là một nghiệm của phương trình, nên $x = 2$ là nghiệm duy nhất của $(*).$

Vậy, phương trình cho có nghiệm $x = 2.$

2. Nhận xét $x = 1$ là nghiệm của phương trình đã cho vì ${4^1} + {5^1} = 9.$

Ta chứng minh phương trình cho có nghiệm duy nhất là $x = 1.$

Thật vậy, xét hàm số $f\left( x \right) = {4^x} + {5^x}$ xác định trên $R.$

Vì $f’\left( x \right) = {4^x}\ln 4 + {5^x}\ln 5 > 0$ với mọi $x$ thuộc $R$ nên $f\left( x \right)$ đồng biến trên $R$.

Do đó:

+ Với $x > 1$ thì $f\left( x \right) > f\left( 1 \right)$ hay ${4^x} + {5^x} > 9$, nên phương trình cho không thể có nghiệm $x > 1.$

+ Với $x < 1$ thì $f\left( x \right) < f\left( 1 \right)$ hay ${4^x} + {5^x} < 9$, nên phương trình cho không thể có nghiệm $x < 1.$

Vậy phương trình cho có nghiệm duy nhất $x = 1$.

3. Phương trình cho $\Leftrightarrow \ln \left( {x + \sqrt {{x^2} + 1} } \right) – x\ln 5 = 0.$

Xét hàm số $f(x) = \ln \left( {x + \sqrt {{x^2} + 1} } \right) – x\ln 5$ có $f'(x) = \frac{1}{{\sqrt {{x^2} + 1} }} – \ln 5 < 0$ $\Rightarrow f(x)$ là hàm nghịch biến.

Hơn nữa $f(0) = 0$ $\Rightarrow x = 0$ là nghiệm duy nhất của phương trình đã cho.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 11. Giải các phương trình:

1. ${3^{2{x^3} – x + 2}} – {3^{{x^3} + 2x}} + {x^3} – 3x + 2 = 0.$

2. ${2^{x – 1}} – {2^{{x^2} – x}} = {\left( {x – 1} \right)^2}.$

1. Phương trình đã cho $⇔{3^{2{x^3} – x + 2}} + 2{x^3} – x + 2$ $= {3^{{x^3} + 2x}} + {x^3} + 2x$, có dạng $f\left( {2{x^3} – x + 2} \right) = f\left( {{x^3} + 2x} \right)$. Xét hàm số $f\left( t \right) = {3^t} + t$, $t \in R$ ta có: $f’\left( t \right) = {3^t}\ln 3 + 1 > 0$, $\forall t \in R$ nên $f\left( t \right)$ đồng biến trên $R.$ Phương trình đã cho tương đương $2{x^3} – x + 2 = {x^3} + 2x$, phương trình này có nghiệm $x = – 2,$ $x = 1.$

Vậy, phương trình đã cho có nghiệm: $x = – 2,$ $x = 1.$

2. Đặt $u = x – 1,$ $v = {x^2} – x,$ phương trình đã cho viết về dạng: ${2^u} + u = {2^v} + v.$

Hàm số $f\left( t \right) = {2^t} + t$ luôn đồng biến trên $R$, do đó $f\left( u \right) = f\left( v \right)$ xảy ra khi $u = v$ tức $x = 1$ thỏa bài toán.
Vậy, phương trình đã cho có nghiệm: $x = 1.$

<!-- chunk:4 level:2 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Dạng 6. Phương pháp lượng giác hóa
Phương pháp:

Chọn thích hợp để đặt ${a^x} = \sin t$ hoặc ${a^x} = \cos t$ $\left( {0 < a \ne 1} \right).$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 12. Giải phương trình: $\sqrt {1 + \sqrt {1 – {2^{2x}}} } = \left( {1 + 2\sqrt {1 – {2^{2x}}} } \right){.2^x}.$

Điều kiện: $1 – {2^{2x}} \ge 0$ $\Leftrightarrow {2^{2x}} \le 1 \Leftrightarrow x \le 0.$

Với $x \le 0 \Rightarrow 0 < {2^x} \le 1$, đặt ${2^x} = \sin t;$ $t \in \left( {0;\frac{\pi }{2}} \right).$

Phương trình đã cho trở thành: $\sqrt {1 + \sqrt {1 – {{\sin }^2}t} }$ $= \sin t\left( {1 + 2\sqrt {1 – {{\sin }^2}t} } \right)$

$\Leftrightarrow \sqrt {1 + \cos t} = \left( {1 + 2\cos t} \right)\sin t$ $\Leftrightarrow \sqrt 2 \cos \frac{t}{2} = \sin t + \sin 2t$

$\Leftrightarrow \sqrt 2 \cos \frac{t}{2} = 2\sin \frac{{3t}}{2}\cos \frac{t}{2}$ $\Leftrightarrow \sqrt 2 \cos \frac{t}{2}\left( {1 – \sqrt 2 \sin \frac{{3t}}{2}} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\cos \frac{t}{2} = 0\\
\sin \frac{{3t}}{2} = \frac{{\sqrt 2 }}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = \frac{\pi }{6}\\
t = \frac{\pi }{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{2^x} = \frac{1}{2}\\
{2^x} = 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 1\\
x = 0
\end{array} \right.
$$

Vậy, phương trình cho có $2$ nghiệm $x = – 1$ hoặc $x = 0.$

[ads]

<!-- chunk:6 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 13. Tìm $m$ để phương trình ${9^{1 + \sqrt {1 – {x^2}} }} – \left( {m + 2} \right){3^{1 + \sqrt {1 – {x^2}} }}$ $+ 2m + 1 = 0$ có nghiệm thực.

Điều kiện: $– 1 \le x \le 1.$

Đặt $t = {3^{1 + \sqrt {1 – {x^2}} }}$, với $– 1 \le x \le 1 \Rightarrow t \in \left[ {3;9} \right].$

Phương trình đã cho trở thành: ${t^2} – \left( {m + 2} \right)t + 2m + 1 = 0$, với $t \in \left[ {3;9} \right]$, tương đương với $m = \frac{{{t^2} – 2t + 1}}{{t – 2}}.$

Xét hàm số: $f\left( t \right) = \frac{{{t^2} – 2t + 1}}{{t – 2}}$ với $t \in \left[ {3;9} \right].$

Ta có: $f’\left( t \right) = \frac{{{t^2} – 4t + 3}}{{{{\left( {t – 2} \right)}^2}}} > 0$ với mọi $t \in \left( {3;9} \right)$, do đó hàm số $f\left( t \right)$ đồng biến trên đoạn $\left[ {3;9} \right]$ và $f\left( 3 \right) \le f\left( t \right) \le f\left( 9 \right)$ suy ra $4 \le m \le \frac{{64}}{7}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 14. Giải các bất phương trình:

1. ${\left( {\sqrt {10} + 3} \right)^{\frac{{x – 3}}{{x – 1}}}} < {\left( {\sqrt {10} – 3} \right)^{\frac{{x + 1}}{{x + 3}}}}.$

2. ${\left( {{x^2} + \frac{1}{2}} \right)^{2{x^2} + x + 1}} \le {\left( {{x^2} + \frac{1}{2}} \right)^{1 – x}}.$

1. Ta có $(\sqrt {10} + 3)(\sqrt {10} – 3) = 1$ $\Rightarrow \sqrt {10} – 3 = {\left( {\sqrt {10} + 3} \right)^{ – 1}}.$

Bất phương trình đã cho $\Leftrightarrow {\left( {\sqrt {10} + 3} \right)^{\frac{{x – 3}}{{x – 1}}}} < {\left( {\sqrt {10} + 3} \right)^{ – \frac{{x + 1}}{{x + 3}}}}$

$\Leftrightarrow \frac{{x – 3}}{{x – 1}} < – \frac{{x + 1}}{{x + 3}}$ $\Leftrightarrow \frac{{2{x^2} – 10}}{{(x – 1)(x + 3)}} < 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
– 3 < x < – \sqrt 5 \\
1 < x < \sqrt 5
\end{array} \right.
$$

2. Vì ${x^2} + \frac{1}{2} > 0$ nên ta có các trường hợp sau:

* ${x^2} + \frac{1}{2} = 1 \Leftrightarrow x = \pm \frac{1}{{\sqrt 2 }}.$

* 
$$
\left\{ \begin{array}{l}
{x^2} + \frac{1}{2} > 1\\
2{x^2} + x + 1 \ge 1 – x
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\left| x \right| > \frac{1}{{\sqrt 2 }}\\
2{x^2} + 2x \ge 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x \le – 1\\
x > \frac{1}{{\sqrt 2 }}
\end{array} \right.
$$

* 
$$
\left\{ \begin{array}{l}
{x^2} + \frac{1}{2} < 1\\
2{x^2} + x + 1 \le 1 – x
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\left| x \right| < \frac{1}{{\sqrt 2 }}\\
2{x^2} + 2x \le 0
\end{array} \right.
$$
 $\Leftrightarrow – \frac{1}{{\sqrt 2 }} < x \le 0.$

Vậy nghiệm của bất phương trình là: $x \in ( – \infty ; – 1]$ $\cup \left[ { – \frac{1}{{\sqrt 2 }};0} \right] \cup \left[ {\frac{1}{{\sqrt 2 }}; + \infty } \right).$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 15. Giải bất phương trình: ${9^{\sqrt {{x^2} – 2x} – x}} – {7.3^{\sqrt {{x^2} – 2x} – x – 1}} \le 2.$

Bất phương trình đã cho $\Leftrightarrow {3.9^{\sqrt {{x^2} – 2x} – x}} – {7.3^{\sqrt {{x^2} – 2x} – x}} \le 6.$

Đặt $t = {3^{\sqrt {{x^2} – 2{\rm{x}}} – x}}, t > 0$, ta có bất phương trình:

$3{t^2} – 7t – 6 \le 0 \Leftrightarrow t \le 3$ $\Leftrightarrow \sqrt {{x^2} – 2x} – x \le 1$ $\Leftrightarrow \sqrt {{x^2} – 2x} \le x + 1$

$$
\Leftrightarrow \left\{ \begin{array}{l}
{x^2} – 2x \ge 0\\
x + 1 \ge 0\\
{x^2} – 2x \le {(x + 1)^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \le 0{\rm{ }} \vee {\rm{ }}x \ge 2\\
x \ge – 1\\
x \ge – \frac{1}{4}
\end{array} \right.
$$
 $\Leftrightarrow – \frac{1}{4} \le x \le 0$ hoặc $x \ge 2.$

Vậy, bất phương trình cho có nghiệm là $– \frac{1}{4} \le x \le 0$ hoặc $x \ge 2.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/05/phuong-phap-giai-phuong-trinh-mu-va-bat-phuong-trinh-mu-phan-2.html -->
## Ví dụ 16. Giải các bất phương trình:

1. ${\rm{ }}{(7 + 4\sqrt 3 )^x} – 3{(2 – \sqrt 3 )^x} + 2 \le 0.$

2. ${2.3^{\sqrt x + \sqrt[4]{x}}} + {9^{\sqrt[4]{x} + \frac{1}{2}}} \ge {9^{\sqrt x }}.$

1. Ta có: $7 + 4\sqrt 3 = {(2 + \sqrt 3 )^2}$ và $(2 – \sqrt 3 )(2 + \sqrt 3 ) = 1$ nên đặt $t = {(2 + \sqrt 3 )^x}, t > 0$ ta có  bất phương trình:

${t^2} – \frac{3}{t} + 2 \le 0$ $\Leftrightarrow {t^3} + 2t – 3 \le 0$ $\Leftrightarrow (t – 1)({t^2} + t + 3) \le 0$ $\Leftrightarrow t \le 1$

$\Leftrightarrow {(2 + \sqrt 3 )^x} \le 1 \Leftrightarrow x \le 0.$

Vậy, bất phương trình cho có nghiệm là $x \le 0.$

2. Chia hai vế bất phương trình cho ${9^{\sqrt x }}$ ta được: ${2.3^{\sqrt[4]{{\rm{x}}} – \sqrt x }} + {3.9^{\sqrt[4]{{\rm{x}}} – \sqrt x }} \ge 1.$

Đặt $t = {3^{\sqrt[{\rm{4}}]{{\rm{x}}} – \sqrt x }}, t > 0$ ta có bất phương trình: $3{t^2} + 2t – 1 \ge 0$

$\Leftrightarrow t \ge \frac{1}{3} \Leftrightarrow {3^{\sqrt[4]{{\rm{x}}} – \sqrt x }} \ge {3^{ – 1}}$ $\Leftrightarrow \sqrt[4]{{\rm{x}}} – \sqrt x \ge – 1$ $\Leftrightarrow \sqrt x – \sqrt[4]{{\rm{x}}} – 1 \le 0$ $\Leftrightarrow \sqrt[4]{{\rm{x}}} \le \frac{{1 + \sqrt 5 }}{2}$ $\Leftrightarrow 0 \le x \le \frac{{7 + 3\sqrt 5 }}{2}.$

Vậy, bất phương trình đã cho có nghiệm là $0 \le x \le \frac{{7 + 3\sqrt 5 }}{2}.$