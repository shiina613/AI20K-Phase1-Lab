# Phương pháp tính tích phân hàm số phân thức hữu tỉ

<!-- chunk:0 level:0 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
Bài viết hướng dẫn phương pháp tính tích phân hàm số phân thức hữu tỉ, đây là dạng tích phân được bắt gặp thường xuyên trong chương trình Giải tích 12 chương 3 (nguyên hàm – tích phân và ứng dụng).

1. Phương pháp tính tích phân hàm số phân thức hữu tỉ
Bài toán tổng quát: Tính tích phân $I = \int_\alpha ^\beta {\frac{{P(x)}}{{Q(x)}}} dx$ với $P(x)$ và $Q(x)$ là các đa thức.

Trường hợp 1: Nếu bậc của tử số $P(x)$ $<$ bậc của mẫu số $Q(x)$: Xem xét mẫu số, ta có các dạng phổ biến sau:

<!-- chunk:1 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Dạng 2: $I = \int_\alpha ^\beta {\frac{A}{{a{x^2} + bx + c}}}$, dựa vào biệt thức $\Delta = {b^2} – 4ac$ của mẫu số, ta chia thành các trường hợp:

+ Nếu $\Delta > 0$, ta có: $I = \int_\alpha ^\beta {\frac{A}{{a\left( {x – {x_1}} \right)\left( {x – {x_2}} \right)}}} dx$ $= \frac{A}{{a\left( {{x_2} – {x_1}} \right)}}\int_a^\beta {\left( {\frac{1}{{x – {x_2}}} – \frac{1}{{x – {x_1}}}} \right)}$.

+ Nếu $\Delta = 0$, ta có: $I = \int_\alpha ^\beta {\frac{{Adx}}{{a{{\left( {x – {x_0}} \right)}^2}}}}$ $= – \left. {\frac{A}{{a\left( {x – {x_0}} \right)}}} \right|_\alpha ^\beta .$

+ Nếu $\Delta < 0$, ta có: $I = \frac{A}{a}\int_\alpha ^\beta {\frac{{dx}}{{{{\left( {x + {x_o}} \right)}^2} + {k^2}}}}$, sử dụng phương pháp đổi biến tích phân $x + {x_0} = k\tan t$, $t \in \left( { – \frac{\pi }{2};\frac{\pi }{2}} \right)$, ta được: $I = \frac{A}{{ka}}\int_\alpha ^\beta d t$ $= \frac{A}{{ka}}\left. t \right|_\alpha ^\beta .$

<!-- chunk:2 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Dạng 3: $I = \int_\alpha ^\beta {\frac{{Ax + B}}{{a{x^2} + bx + c}}} dx$, dựa vào biệt thức $\Delta = {b^2} – 4ac$ của mẫu số, ta chia thành các trường hợp:

+ Nếu $\Delta > 0$, ta có: $I = \int_\alpha ^\beta {\frac{{C\left( {x – {x_1}} \right) + D\left( {x – {x_2}} \right)}}{{a\left( {x – {x_1}} \right)\left( {x – {x_2}} \right)}}} dx$ $= \frac{1}{a}\int_\alpha ^\beta {\left( {\frac{C}{{x – {x_2}}} + \frac{D}{{x – {x_1}}}} \right)} dx$.

+ Nếu $\Delta = 0$, ta có: $I = \int_\alpha ^\beta {\frac{{Ax + B}}{{a{{\left( {x – {x_0}} \right)}^2}}}} dx$ $= \frac{1}{a}\int_a^\beta {\frac{{A\left( {x – {x_0}} \right) + C}}{{a{{\left( {x – {x_0}} \right)}^2}}}} dx$ $= \frac{1}{a}\int_\alpha ^\beta {\left( {\frac{A}{{x – {x_0}}} + \frac{C}{{{{\left( {x – {x_0}} \right)}^2}}}} \right)} dx$.

+ Nếu $\Delta < 0$, ta có: $I = \int_\alpha ^\beta {\frac{{k{{\left( {a{x^2} + bx + c} \right)}^\prime } + h}}{{a{x^2} + bx + c}}} dx$ $= k\int_\alpha ^\beta {\frac{{d\left( {a{x^2} + bx + c} \right)}}{{a{x^2} + bx + c}}}$ $+ h\int_\alpha ^\beta {\frac{{dx}}{{a{x^2} + bx + c}}} .$

<!-- chunk:3 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Dạng 4: Nếu $Q(x)$ có bậc lớn hơn $2$, ta thực hiện giảm bậc bằng cách đổi biến, tách ghép, nhân, chia … để đưa bài toán về các dạng 1, dạng 2, dạng 3.

Trường hợp 2: Nếu bậc của tử số $P(x)$ $≥$ bậc của mẫu số $Q(x)$, ta sử dụng phép chia đa thức: $I = \int_\alpha ^\beta {\frac{{P(x)}}{{Q(x)}}}$ $= \int_\alpha ^\beta {\left[ {H(x) + \frac{{R(x)}}{{Q(x)}}} \right]} dx$ $= \int_\alpha ^\beta H (x)dx + \int_\alpha ^\beta {\frac{{R(x)}}{{Q(x)}}} dx$ $= {I_1} + {I_2}$, trong đó $I_1$ là tích phân cơ bản, $I_2$ là tích phân hàm số phân thức hữu tỉ có bậc tử số nhỏ hơn bậc mẫu số.

Chú ý: Đối với những bài toán phức tạp, để đưa về các dạng 1, 2, 3 ta phải thực hiện biến đổi phân số ban đầu thành tổng các phân số và tìm các hệ số bằng phương pháp đồng nhất thức. Một số trường hợp thường gặp:

• $\frac{1}{{(ax + b)(cx + d)}}$ $= \frac{1}{{ad – bc}}\left( {\frac{a}{{ax + b}} – \frac{c}{{cx + d}}} \right).$

• $\frac{{mx + n}}{{(ax + b)(cx + d)}}$ $= \frac{A}{{ax + b}} + \frac{B}{{cx + d}}.$

• $\frac{{mx + n}}{{{{(ax + b)}^2}}}$ $= \frac{A}{{ax + b}} + \frac{B}{{{{(ax + b)}^2}}}.$

• $\frac{{mx + n}}{{{{(ax + b)}^2}(cx + d)}}$ $= \frac{A}{{{{(ax + b)}^2}}} + \frac{B}{{cx + d}} + \frac{C}{{ax + b}}.$

• $\frac{1}{{(x – m)\left( {a{x^2} + bx + c} \right)}}$ $= \frac{A}{{x – m}} + \frac{{Bx + C}}{{a{x^2} + bx + c}}$, với $\Delta = {b^2} – 4ac < 0.$

• $\frac{1}{{{{(x – a)}^2}{{(x – b)}^2}}}$ $= \frac{A}{{x – a}} + \frac{B}{{{{(x – a)}^2}}}$ $+ \frac{C}{{x – b}} + \frac{D}{{{{(x – b)}^2}}}.$

• $\frac{{P(x)}}{{{{\left( {x – {x_o}} \right)}^n}}}$ $= \frac{A}{{x – {x_o}}} + \frac{B}{{{{\left( {x – {x_o}} \right)}^2}}}$ $+ \ldots + \frac{C}{{{{\left( {x – {x_o}} \right)}^n}}}.$

• $\frac{{P(x)}}{{\left( {x – {x_1}} \right)\left( {x – {x_2}} \right)\left( {x – {x_3}} \right)…}}$ $= \frac{A}{{x – {x_1}}} + \frac{B}{{x – {x_2}}}$ $+ \frac{C}{{x – {x_3}}} + \cdots .$

2. Một số bài toán minh họa

<!-- chunk:4 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 1: Tính các tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_1^2 {\frac{{{x^3}}}{{2x + 3}}} dx.$

b) $I = \int_{\sqrt 5 }^3 {\frac{{{x^2} – 5}}{{x + 1}}} dx.$

c) $\int_0^{\frac{1}{2}} {\frac{{{x^3}}}{{{x^2} – 1}}} dx.$

a) Ta có: $\frac{{{x^3}}}{{2x + 3}}$ $= \frac{1}{2} \cdot \frac{{\left( {2{x^3} + 3{x^2}} \right) – \frac{3}{2}\left( {2{x^2} + 3x} \right) + \frac{9}{4}(2x + 3) – \frac{{27}}{4}}}{{2x + 3}}$ $= \frac{{{x^2}}}{2} – \frac{3}{4}x + \frac{9}{8} – \frac{{27}}{{8(2x + 3)}}.$

Suy ra: $\int_1^2 {\frac{{{x^3}}}{{2x + 3}}} dx$ $= \int_1^2 {\left( {\frac{{{x^2}}}{2} – \frac{3}{4}x + \frac{9}{8} – \frac{{27}}{{8(2x + 3)}}} \right)} dx$ $= \left. {\left( {\frac{1}{3}{x^3} – \frac{3}{8}{x^2} + \frac{9}{8}x – \frac{{27}}{{16}}\ln |2x + 3|} \right)} \right|_1^2$ $= – \frac{{13}}{6} – \frac{{27}}{{16}}\ln 35.$

b) Ta có: $\frac{{{x^2} – 5}}{{x + 1}}$ $= \frac{{{x^2} – 1 – 4}}{{x + 1}}$ $= x – 1 – \frac{4}{{x + 1}}.$

Suy ra: $\int_{\sqrt 5 }^3 {\frac{{{x^2} – 5}}{{x + 1}}} dx$ $= \int_{\sqrt 5 }^3 {\left( {x – 1 – \frac{4}{{x + 1}}} \right)} dx$ $= \left. {\left( {\frac{1}{2}{x^2} – x – 4\ln |x + 1|} \right)} \right|_{\sqrt 5 }^3$ $= \sqrt 5 – 1 + 4\ln \left( {\frac{{\sqrt 5 + 1}}{4}} \right).$

c) Ta có: $\frac{{{x^3}}}{{{x^2} – 1}}$ $= \frac{{x\left( {{x^2} – 1} \right) + x}}{{{x^2} – 1}}$ $= x + \frac{x}{{{x^2} – 1}}.$

Suy ra: $\int_0^{\frac{1}{2}} {\frac{{{x^3}}}{{{x^2} – 1}}} dx$ $= \int_0^{\frac{1}{2}} {\left( {x + \frac{x}{{{x^2} – 1}}} \right)} dx$ $= \int_1^{\frac{1}{2}} x dx + \int_0^{\frac{1}{2}} {\frac{{xdx}}{{{x^2} – 1}}}$ $= \left. {\frac{{{x^2}}}{2}} \right|_0^{\frac{1}{2}} + \frac{1}{2}\ln \left. {\left| {{x^2} – 1} \right|} \right|_0^{\frac{1}{2}}$ $= \frac{1}{8} + \frac{1}{2}\ln \frac{3}{4}.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 2: Tính tích phân hàm số phân thức hữu tỉ: $I = \int_0^1 {\frac{{4x + 11}}{{{x^2} + 5x + 6}}} dx.$

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $f(x) = \frac{{4x + 11}}{{{x^2} + 5x + 6}}$ $= \frac{{4x + 11}}{{(x + 2)(x + 3)}}$ $= \frac{A}{{x + 2}} + \frac{B}{{x + 3}}$ $= \frac{{A(x + 3) + B(x + 2)}}{{(x + 2)(x + 3)}}.$

Thay $x = – 2$ vào hai tử số: $3 = A$ và thay $x = -3$ vào hai tử số: $-1 = -B$ suy ra $B = 1.$

Do đó: $f(x) = \frac{3}{{x + 2}} + \frac{1}{{x + 3}}.$

Vậy: $\int_0^1 {\frac{{4x + 11}}{{{x^2} + 5x + 6}}} dx$ $= \int_0^1 {\left( {\frac{3}{{x + 2}} + \frac{1}{{x + 3}}} \right)} dx$ $= 3\ln |x + 2| + \ln \left. {|x + 3|} \right|_0^1$ $= 2\ln 3 – \ln 2.$

Cách 2: (Nhảy tầng lầu)

Ta có: $f(x) = \frac{{2(2x + 5) + 1}}{{{x^2} + 5x + 6}}$ $= 2.\frac{{2x + 5}}{{{x^2} + 5x + 6}}$ $+ \frac{1}{{(x + 2)(x + 3)}}$ $= 2.\frac{{2x + 5}}{{{x^2} + 5x + 6}}$ $+ \frac{1}{{x + 2}} – \frac{1}{{x + 3}}.$

Suy ra: $I = \int_0^1 f (x)dx$ $= \int_0^1 {\left( {2.\frac{{2x + 5}}{{{x^2} + 5x + 6}} + \frac{1}{{x + 2}} – \frac{1}{{x + 3}}} \right)} dx$ $= \left. {\left( {2\ln \left| {{x^2} + 5x + 6} \right| + \ln \left| {\frac{{x + 2}}{{x + 3}}} \right|} \right)} \right|_0^1$ $= 2\ln 3 – \ln 2.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 3: Tính các tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_0^3 {\frac{{{x^3}}}{{{x^2} + 2x + 1}}} dx.$

b) $I = \int_0^1 {\frac{{4x}}{{4{x^2} – 4x + 1}}} dx.$

a)

Cách 1: Thực hiện cách chia đa thức ${x^3}$ cho đa thức ${x^2} + 2x + 1$, ta được:

$\frac{{{x^3}}}{{{x^2} + 2x + 1}}$ $= x – 2 + \frac{{3x + 2}}{{{x^2} + 2x + 1}}.$

$I = \int_0^3 {\frac{{{x^3}}}{{{x^2} + 2x + 1}}} dx$ $= \int_0^3 {(x – 2)} dx$ $+ \int_0^3 {\frac{{3x + 3 – 1}}{{{x^2} + 2x + 1}}} dx$ $= \left. {\left( {\frac{{{x^2}}}{2} – 2x} \right)} \right|_0^3$ $+ \frac{3}{2}\int_0^3 {\frac{{d\left( {{x^2} + 2x + 1} \right)}}{{{x^2} + 2x + 1}}}$ $– \int_0^3 {\frac{{dx}}{{{{(x + 1)}^2}}}}$ $= – \frac{3}{2} + \frac{3}{2}\ln \left. {{{(x + 1)}^2}} \right|_0^3$ $+ \left. {\frac{1}{{x + 1}}} \right|_0^3$ $= – \frac{3}{2} + \frac{3}{2}\ln 16 + \frac{1}{4} – 1$ $= – \frac{9}{4} + 6\ln 2.$

Cách 2: Ta có: $\int_0^3 {\frac{{{x^3}}}{{{x^2} + 2x + 1}}} dx$ $= \int_0^3 {\frac{{{x^3}}}{{{{(x + 1)}^2}}}} dx.$

Đặt $t = x + 1$, suy ra: $dx = dt$, $x = t – 1.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 1}\\
{x = 3 \Rightarrow t = 4}
\end{array}} \right.
$$

Do đó: $\int_0^3 {\frac{{{x^3}}}{{{{(x + 1)}^2}}}} dx$ $= \int_1^4 {\frac{{{{(t – 1)}^3}}}{{{t^2}}}} dt$ $= \int_1^4 {\left( {t – 3 + \frac{3}{t} – \frac{1}{{{t^2}}}} \right)} dt$ $= \left. {\left( {\frac{1}{2}{t^2} – 3t + 3\ln |t| + \frac{1}{t}} \right)} \right|_1^4$ $= – \frac{9}{4} + 6\ln 2.$

b) Ta có: $\frac{{4x}}{{4{x^2} – 4x + 1}}$ $= \frac{{4x}}{{{{(2x – 1)}^2}}}.$

Đặt $t = 2x – 1$ suy ra: $dt = 2dx$ $\to dx = \frac{1}{2}dt.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = – 1}\\
{x = 1 \Rightarrow t = 1}
\end{array}} \right.
$$

Do đó: $\int_0^1 {\frac{{4x}}{{4{x^2} – 4x + 1}}} dx$ $= \int_0^1 {\frac{{4x}}{{{{(2x – 1)}^2}}}} dx$ $= \int_{ – 1}^1 {\frac{{4.\frac{1}{2}(t + 1)}}{{{t^2}}}} \frac{1}{2}dt$ $= \int_{ – 1}^1 {\left( {\frac{1}{t} + \frac{1}{{{t^2}}}} \right)} dt$ $= \left. {\left( {\ln |t| – \frac{1}{t}} \right)} \right|_{ – 1}^1$ $= – 2.$

[ads]

<!-- chunk:7 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 4: Tính các tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_0^2 {\frac{x}{{{x^2} + 4x + 5}}} dx.$

b) $I = \int_0^2 {\frac{{{x^3} + 2{x^2} + 4x + 9}}{{{x^2} + 4}}} dx.$

a) Ta có: $\int_0^2 {\frac{x}{{{x^2} + 4x + 5}}} dx$ $= \int_0^2 {\frac{x}{{{{(x + 2)}^2} + 1}}} dx.$

Đặt $x + 2 = \tan t$, suy ra: $dx = \frac{1}{{{{\cos }^2}t}}dt$.

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow \tan t = 2}\\
{x = 2 \Rightarrow \tan t = 4}
\end{array}} \right.
$$

Do đó: $\int_0^2 {\frac{x}{{{{(x + 2)}^2} + 1}}} dx$ $= \int_{{t_1}}^{{t_2}} {\frac{{\tan t – 2}}{{1 + {{\tan }^2}t}}} \frac{{dt}}{{{{\cos }^2}t}}$ $= \int_{{t_1}}^{{t_2}} {\left( {\frac{{\sin t}}{{\cos t}} – 2} \right)} dt$ $= \left. {( – \ln |\cos t| – 2t)} \right|_{{t_1}}^{{t_2}}.$

Từ $\tan t = 2$ $\Rightarrow 1 + {\tan ^2}t = 5$ $\Leftrightarrow {\cos ^2}t = \frac{1}{5}$ $\Rightarrow \cos {t_1} = \frac{1}{{\sqrt 5 }}$ và $\tan t = 4$ $\Rightarrow 1 + {\tan ^2}t = 17$ $\Leftrightarrow {\cos ^2}t = \frac{1}{{17}}$ $\Rightarrow \cos {t_2} = \frac{1}{{\sqrt {17} }}.$

Vậy $\left. {( – \ln |\cos t| – 2t)} \right|_{{t_1}}^{{t_2}}$ $= 2(\arctan 4 – \arctan 2) – \frac{1}{2}\ln \frac{5}{{17}}.$

b) Ta có: $\frac{{{x^3} + 2{x^2} + 4x + 9}}{{{x^2} + 4}}$ $= \frac{{{x^3} + 4x + 2{x^2} + 8 + 1}}{{{x^2} + 4}}$ $= x + 2 + \frac{1}{{{x^2} + 4}}.$

Do đó: $\int_0^2 {\frac{{{x^3} + 2{x^2} + 4x + 9}}{{{x^2} + 4}}} dx$ $= \int_0^2 {\left( {x + 2 + \frac{1}{{{x^2} + 4}}} \right)} dx$ $= \left. {\left( {\frac{1}{2}{x^2} + 2x} \right)} \right|_0^2$ $+ \int_0^2 {\frac{{dx}}{{{x^2} + 4}}}$ $= 6 + J.$

Tính tích phân: $J = \int_0^2 {\frac{1}{{{x^2} + 4}}} dx.$

Đặt $x = 2\tan t$ suy ra: $dx = \frac{2}{{{{\cos }^2}t}}dt.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 0}\\
{x = 2 \Rightarrow t = \frac{\pi }{4}}
\end{array}} \right.
$$

Ta có: $t \in \left[ {0;\frac{\pi }{4}} \right]$ $\to \cos t > 0.$

Khi đó: $J = \int_0^2 {\frac{1}{{{x^2} + 4}}} dx$ $= \frac{1}{4}\int_0^{\frac{\pi }{4}} {\frac{1}{{1 + {{\tan }^2}t}}} \frac{2}{{{{\cos }^2}t}}dt$ $= \frac{1}{2}\int_0^{\frac{\pi }{4}} d t$ $= \frac{1}{2}\left. t \right|_0^{\frac{\pi }{4}} = \frac{\pi }{8}.$

Vậy $I = 6 + \frac{\pi }{8}.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 5: Tính các tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_0^1 {\frac{x}{{{{(x + 1)}^3}}}} dx.$

b) $I = \int_{ – 1}^0 {\frac{{{x^4}}}{{{{(x – 1)}^3}}}} dx.$

a)

Cách 1:

Đặt $x + 1 = t$, suy ra: $x = t – 1.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 0 \Rightarrow t = 1}\\
{x = 1 \Rightarrow t = 2}
\end{array}} \right.
$$

Do đó: $\int_0^1 {\frac{x}{{{{(x + 1)}^3}}}} dx$ $= \int_1^2 {\frac{{t – 1}}{{{t^3}}}} dt$ $= \int_1^2 {\left( {\frac{1}{{{t^2}}} – \frac{1}{{{t^3}}}} \right)} dt$ $= \left. {\left( { – \frac{1}{t} + \frac{1}{2}\frac{1}{{{t^2}}}} \right)} \right|_1^2$ $= \frac{1}{8}.$

Cách 2:

Ta có: $\frac{x}{{{{(x + 1)}^3}}}$ $= \frac{{(x + 1) – 1}}{{{{(x + 1)}^3}}}$ $= \frac{1}{{{{(x + 1)}^2}}} – \frac{1}{{{{(x + 1)}^3}}}.$

Do đó: $\int_0^1 {\frac{x}{{{{(x + 1)}^3}}}} dx$ $= \int_0^1 {\left[ {\frac{1}{{{{(x + 1)}^2}}} – \frac{1}{{{{(x + 1)}^3}}}} \right]} dx$ $= \left. {\left[ { – \frac{1}{{x + 1}} + \frac{1}{2}\frac{1}{{{{(x + 1)}^2}}}} \right]} \right|_0^1$ $= \frac{1}{8}.$

b) Đặt $x – 1 = t$, suy ra: $x = t + 1.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = – 1 \Rightarrow t = – 2}\\
{x = 0 \Rightarrow t = – 1}
\end{array}} \right.
$$

Do đó: $\int_{ – 1}^0 {\frac{{{x^4}}}{{{{(x – 1)}^3}}}} dx$ $= \int_{ – 2}^{ – 1} {\frac{{{{(t + 1)}^4}}}{{{t^3}}}} dt$ $= \int_{ – 2}^{ – 1} {\frac{{{t^4} + 4{t^3} + 6{t^2} + 4t + 1}}{{{t^3}}}} dt$ $= \int_{ – 2}^{ – 1} {\left( {t + 4 + \frac{6}{t} + \frac{4}{{{t^2}}} + \frac{1}{{{t^3}}}} \right)} dt$ $= \left. {\left( {\frac{1}{2}{t^2} + 4t + 6\ln |t| – \frac{4}{t} – \frac{1}{2}\frac{1}{{{t^2}}}} \right)} \right|_{ – 2}^1$ $= \frac{{33}}{8} – 6\ln 2.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 6: Tính các tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_2^3 {\frac{1}{{(x – 1){{(x + 1)}^3}}}} dx.$

b) $I = \int_2^3 {\frac{{{x^2}}}{{{{(x – 1)}^2}(x + 2)}}} dx.$

a)

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $\frac{1}{{(x – 1){{(x + 1)}^2}}}$ $= \frac{A}{{x – 1}} + \frac{B}{{(x + 1)}} + \frac{C}{{{{(x + 1)}^2}}}$ $= \frac{{A{{(x + 1)}^2} + B(x – 1)(x + 1) + C(x – 1)}}{{(x – 1){{(x + 1)}^2}}}$ $(1).$

Thay hai nghiệm mẫu số vào hai tử số: 
$$
\left\{ {\begin{array}{l}
{1 = 4A}\\
{1 = – 2C}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{A = \frac{1}{4}}\\
{C = – \frac{1}{2}}
\end{array}} \right.
$$

$(1) \Leftrightarrow \frac{{(A + B){x^2} + (2A + C)x + A – B – C}}{{(x – 1){{(x + 1)}^2}}}$ $\Rightarrow A – B – C = 1$ $\Leftrightarrow B = A – C – 1$ $= \frac{1}{4} + \frac{1}{2} – 1 = – \frac{1}{4}.$

Do đó: $\int_2^3 {\frac{1}{{(x – 1){{(x + 1)}^2}}}} dx$ $= \int_2^3 {\left( {\frac{1}{4}\frac{1}{{x – 1}} + \frac{1}{4}\frac{1}{{(x + 1)}} – \frac{1}{2}\frac{1}{{{{(x + 1)}^2}}}} \right)} dx$ $= \left. {\left[ {\frac{1}{4}\ln (x – 1)(x + 1) + \frac{1}{2} \cdot \frac{1}{{(x + 1)}}} \right]} \right|_2^3$ $= \frac{1}{4}\ln 8 = \frac{3}{4}\ln 2.$

Cách 2: (Phương pháp đổi biến)

Đặt: $t = x + 1$, suy ra $x = t – 1.$

Đổi cận: 
$$
\left\{ {\begin{array}{l}
{x = 2 \Rightarrow t = 3}\\
{x = 3 \Rightarrow t = 4}
\end{array}} \right.
$$

Khi đó: $I = \int_2^3 {\frac{1}{{(x – 1){{(x + 1)}^2}}}} dx$ $= \int_3^4 {\frac{{dt}}{{{t^2}(t – 2)}}}$ $= \frac{1}{2}\int_3^4 {\frac{{t – (t – 2)}}{{{t^2}(t – 2)}}} dt$ $= \frac{1}{2}\left( {\int_2^4 {\frac{1}{{t(t – 2)}}} dt – \int_3^4 {\frac{1}{t}} dt} \right)$ $\Leftrightarrow I = \frac{1}{2}\left( {\frac{1}{2}\int_2^4 {\left( {\frac{1}{{t – 2}} – \frac{1}{t}} \right)} dt – \int_3^4 {\frac{1}{t}} dt} \right)$ $= \left. {\left( {\frac{1}{4}\ln \left| {\frac{{t – 2}}{t}} \right| – \frac{1}{2}\ln |t|} \right)} \right|_3^4$ $= \frac{3}{4}\ln 2.$

b) Đặt $t = x – 1$, suy ra $x = t + 1$, $dx = dt.$

Đổi cận 
$$
\left\{ {\begin{array}{l}
{x = 2 \Rightarrow t = 1}\\
{x = 3 \Rightarrow t = 2}
\end{array}} \right.
$$

Do đó: $\int_2^3 {\frac{{{x^2}}}{{{{(x – 1)}^2}(x + 2)}}} dx$ $= \int_1^2 {\frac{{{{(t + 1)}^2}}}{{{t^2}(t + 3)}}} dt$ $= \int_1^2 {\frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}} dt.$

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $\frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}$ $= \frac{{At + B}}{{{t^2}}} + \frac{C}{{t + 3}}$ $= \frac{{(At + B)(t + 3) + C{t^2}}}{{{t^2}(t + 3)}}$ $= \frac{{(A + C){t^2} + (3A + B)t + 3B}}{{{t^2}(t + 3)}}.$

Đồng nhất hệ số hai tử số: 
$$
\left\{ {\begin{array}{l}
{A + C = 1}\\
{3A + B = 2}\\
{3B = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{B = \frac{1}{3}}\\
{A = \frac{5}{9}}\\
{C = \frac{4}{9}}
\end{array}} \right.
$$
 $\Rightarrow \frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}$ $= \frac{1}{9}\frac{{t + 3}}{{{t^2}}} + \frac{4}{9}\frac{1}{{t + 3}}.$

Do đó: $\int_1^2 {\frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}} dt$ $= \int_1^2 {\left( {\frac{1}{9}\left( {\frac{1}{t} + \frac{3}{{{t^2}}}} \right) + \frac{4}{9}\left( {\frac{1}{{t + 3}}} \right)} \right)} dt$ $= \left. {\left( {\frac{1}{9}\left( {\ln |t| – \frac{3}{t}} \right) + \frac{4}{9}\ln |t + 3|} \right)} \right|_1^2$ $= \frac{{17}}{6} + \frac{4}{9}\ln 5 – \frac{7}{9}\ln 2.$

Cách 2:

Ta có: $\frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}$ $= \frac{1}{3}\left( {\frac{{3{t^2} + 6t + 3}}{{{t^3} + 3{t^2}}}} \right)$ $= \frac{1}{3}\left[ {\frac{{3{t^2} + 6t}}{{{t^3} + 3{t^2}}} + \frac{3}{{{t^2}(t + 3)}}} \right]$ $= \frac{1}{3}\left[ {\left( {\frac{{3{t^2} + 6t}}{{{t^3} + 3{t^2}}}} \right) + \frac{1}{9}\left( {\frac{{{t^2} – \left( {{t^2} – 9} \right)}}{{{t^2}(t + 3)}}} \right)} \right]$ $= \frac{1}{3}\left( {\frac{{3{t^2} + 6t}}{{{t^3} + 3{t^2}}}} \right)$ $+ \frac{1}{9}\frac{1}{{t + 3}} – \frac{1}{9}\frac{{t – 3}}{{{t^2}}}$ $= \frac{1}{3}\left[ {\left( {\frac{{3{t^2} + 6t}}{{{t^3} + 3{t^2}}}} \right) + \frac{1}{9}\frac{1}{{t + 3}} – \frac{1}{9}\left( {\frac{1}{t} – \frac{3}{{{t^2}}}} \right)} \right].$

Vậy: $\int_1^2 {\frac{{{t^2} + 2t + 1}}{{{t^2}(t + 3)}}} dt$ $= \int_1^2 {\left( {\frac{1}{3}\left( {\frac{{3{t^2} + 6t}}{{{t^3} + 3{t^2}}}} \right) + \frac{1}{9}\left( {\frac{1}{{t + 3}} – \frac{1}{t} + \frac{3}{{{t^2}}}} \right)} \right)} dt$ $\left. { = \left[ {\frac{1}{3}\ln \left| {{t^3} + 3{t^2}} \right| + \frac{1}{{27}}\left( {\ln \left| {\frac{{t + 3}}{t}} \right| – \frac{3}{t}} \right)} \right]} \right|_1^2.$

Do đó: $I = \frac{{17}}{6} + \frac{4}{9}\ln 5 – \frac{7}{9}\ln 2.$

<!-- chunk:10 level:2 source:https://toanmath.com/2018/11/phuong-phap-tinh-tich-phan-ham-so-phan-thuc-huu-ti.html -->
## Bài toán 7: Tính tích phân hàm số phân thức hữu tỉ sau:

a) $I = \int_2^3 {\frac{1}{{x\left( {{x^2} – 1} \right)}}} dx.$

b) $I = \int_3^4 {\frac{{x + 1}}{{x\left( {{x^2} – 4} \right)}}} dx.$

c) $\int_2^3 {\frac{{{x^2}}}{{\left( {{x^2} – 1} \right)(x + 2)}}} dx.$

a)

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $f(x) = \frac{1}{{x\left( {{x^2} – 1} \right)}}$ $= \frac{1}{{x(x – 1)(x + 1)}}$ $= \frac{A}{x} + \frac{B}{{x – 1}} + \frac{C}{{x + 1}}$ $= \frac{{A\left( {{x^2} – 1} \right) + Bx(x + 1) + Cx(x – 1)}}{{x(x – 1)(x + 1)}}.$

Đồng nhất hệ số hai tử số bằng cách thay các nghiệm: $x = 0$, $x = 1$ và $x = -1$ vào hai tử ta có:

$$
\left\{ {\begin{array}{l}
{x = 0 \to 1 = – A}\\
{x = – 1 \to 1 = 2C}\\
{x = 1 \to 1 = 2B}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{A = – 1}\\
{B = \frac{1}{2}}\\
{C = \frac{1}{2}}
\end{array}} \right.
$$
 $\Rightarrow f(x) = – \frac{1}{x}$ $+ \frac{1}{2}\left( {\frac{1}{{x – 1}}} \right) + \frac{1}{2}\left( {\frac{1}{{x + 1}}} \right).$

Vậy $\int_2^3 {\frac{1}{{x\left( {{x^2} – 1} \right)}}} dx$ $= \int_2^3 {\left( {\frac{1}{2}\left( {\frac{1}{{x – 1}} + \frac{1}{{x + 1}}} \right) – \frac{1}{x}} \right)} dx$ $= \left. {\left[ {\frac{1}{2}(\ln (x – 1)(x + 1)) – \ln |x|} \right]} \right|_2^3$ $= \frac{5}{2}\ln 2 – \frac{3}{2}\ln 3.$

Cách 2: (Phương pháp nhảy lầu)

Ta có: $\frac{1}{{x\left( {{x^2} – 1} \right)}}$ $= \frac{{{x^2} – \left( {{x^2} – 1} \right)}}{{x\left( {{x^2} – 1} \right)}}$ $= \frac{x}{{{x^2} – 1}} – \frac{1}{x}$ $= \frac{1}{2}\frac{{2x}}{{{x^2} – 1}} – \frac{1}{x}.$

Do đó: $\int_2^3 {\frac{1}{{x\left( {{x^2} – 1} \right)}}} dx$ $= \frac{1}{2}\int_2^3 {\frac{{2xdx}}{{{x^2} – 1}}} – \int_2^3 {\frac{1}{x}} dx$ $= \left. {\left( {\frac{1}{2}\ln \left( {{x^2} – 1} \right) – \ln x} \right)} \right|_2^3$ $= \frac{5}{2}\ln 2 – \frac{3}{2}\ln 3.$

b)

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $\frac{{x + 1}}{{x\left( {{x^2} – 4} \right)}}$ $= \frac{{x + 1}}{{x(x – 2)(x + 2)}}$ $= \frac{A}{x} + \frac{B}{{x – 2}} + \frac{C}{{x + 2}}$ $= \frac{{A\left( {{x^2} – 4} \right) + Bx(x + 2) + Cx (x – 2)}}{{x\left( {{x^2} – 4} \right)}}.$

Thay các nghiệm của mẫu số vào hai tử số:

Khi $x = 0$, ta có: $1 = – 4A$, suy ra: $A = – \frac{1}{4}.$

Khi $x = – 2$, ta có: $– 1 = 8C$, suy ra: $C = – \frac{1}{8}.$

Khi $x = 2$, ta có: $3 = 8B$, suy ra: $B = \frac{3}{8}.$

Do đó: $f(x) = – \frac{1}{4}\left( {\frac{1}{x}} \right)$ $– \frac{1}{8}\left( {\frac{1}{{x – 2}}} \right) + \frac{3}{8}\left( {\frac{1}{{x + 2}}} \right).$

Vậy $\int_3^4 {\frac{{x + 1}}{{x\left( {{x^2} – 4} \right)}}} dx$ $= – \frac{1}{4}\int_2^3 {\frac{1}{x}} dx$ $– \frac{1}{8}\int_2^3 {\frac{1}{{x – 2}}} dx$ $+ \frac{3}{8}\int_2^3 {\frac{1}{{x + 2}}} dx$ $= \left. {\left( { – \frac{1}{4}\ln |x| – \frac{1}{8}\ln |x – 2| + \frac{3}{8}\ln |x + 2|} \right)} \right|_2^3$ $= \frac{5}{8}\ln 3 – \frac{3}{8}\ln 5 – \frac{1}{4}\ln 2.$

Cách 2: (Phương pháp nhảy lầu)

Ta có: $\frac{{x + 1}}{{x\left( {{x^2} – 4} \right)}}$ $= \frac{1}{{\left( {{x^2} – 4} \right)}} + \frac{1}{{x\left( {{x^2} – 4} \right)}}$ $= \frac{1}{4}\left( {\frac{1}{{x – 2}} – \frac{1}{{x + 2}}} \right)$ $+ \frac{1}{4}\left( {\frac{{{x^2} – \left( {{x^2} – 4} \right)}}{{x\left( {{x^2} – 4} \right)}}} \right)$ $= \frac{1}{4}\left( {\frac{1}{{x – 2}} – \frac{1}{{x + 2}} + \frac{1}{2}\frac{{2x}}{{{x^2} – 4}} – \frac{1}{x}} \right).$

Do đó: $\int_3^4 {\frac{{x + 1}}{{x\left( {{x^2} – 4} \right)}}}$ $= \frac{1}{4}\int_3^4 {\left( {\frac{1}{{x – 2}} – \frac{1}{{x + 2}} + \frac{1}{2}\frac{{2x}}{{{x^2} – 4}} – \frac{1}{x}} \right)} dx$ $= \left. {\left[ {\frac{1}{4}\ln \left| {\frac{{x – 2}}{{x + 2}}} \right| + \frac{1}{2}\ln \left( {{x^2} – 4} \right) – \ln |x|} \right]} \right|_3^4.$

c)

Cách 1: (Phương pháp đồng nhất thức)

Ta có: $\frac{{{x^2}}}{{\left( {{x^2} – 1} \right)(x + 2)}}$ $= \frac{{{x^2}}}{{(x – 1)(x + 1)(x + 2)}}$ $= \frac{A}{{x – 1}} + \frac{B}{{x + 1}} + \frac{C}{{x + 2}}$ $= \frac{{A(x + 1)(x + 2) + B(x – 1)(x + 2) + C\left( {{x^2} – 1} \right)}}{{\left( {{x^2} – 1} \right)(x + 2)}}.$

Thay lần lượt các nghiệm mẫu số vào hai tử số:

Thay: $x = 1$, ta có: $1 = 2A$, suy ra: $A = \frac{1}{2}.$

Thay: $x = – 1$, ta có: $1 = – 2B$, suy ra: $B = – \frac{1}{2}.$

Thay: $x = – 2$, ta có: $4 = – 5C$, suy ra: $C = – \frac{5}{4}.$

Do đó: $I = \int_2^3 {\frac{{{x^2}}}{{\left( {{x^2} – 1} \right)(x + 2)}}} dx$ $= \int_2^3 {\left( {\frac{1}{2}\frac{1}{{x – 1}} – \frac{1}{2}\frac{1}{{x + 1}} – \frac{5}{4}\frac{1}{{x + 2}}} \right)} dx$ $= \left. {\left[ {\frac{1}{2}\ln \left| {\frac{{x – 1}}{{x + 1}}} \right| – \frac{5}{4}\ln |x + 2|} \right]} \right|_2^3$ $= \frac{1}{2}\ln \frac{3}{2}.$

Cách 2: (Nhảy tầng lầu)

$\frac{{{x^2}}}{{\left( {{x^2} – 1} \right)(x + 2)}}$ $= \frac{{{x^2} – 1 + 1}}{{\left( {{x^2} – 1} \right)(x + 2)}}$ $= \frac{1}{{x + 2}} + \frac{1}{{(x – 1)(x + 1)(x + 2)}}$ $= \frac{1}{{x + 2}} + \frac{1}{2}\frac{{x(x + 1) – (x – 1)(x + 2)}}{{(x – 1)(x + 1)(x + 2)}}$ $= \frac{1}{{x + 2}} + \frac{1}{2}\left[ {\frac{x}{{(x – 1)(x + 2)}} – \frac{1}{{x + 1}}} \right]$ $= \frac{1}{{x + 2}} + \frac{1}{2}\left[ {1 + \frac{1}{3}\left( {\frac{1}{{x – 1}} – \frac{1}{{x + 2}}} \right) – \frac{1}{{x + 1}}} \right].$

Từ đó suy ra kết quả.