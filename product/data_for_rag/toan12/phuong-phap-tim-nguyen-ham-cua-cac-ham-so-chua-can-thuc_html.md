# Phương pháp tìm nguyên hàm của các hàm số chứa căn thức

<!-- chunk:0 level:0 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
Bài viết trình bày các dạng toán thường gặp và phương pháp tìm nguyên hàm của các hàm số chứa căn thức (hàm số vô tỉ), đây là dạng toán rất phổ biến trong chương trình Giải tích 12 chương 3.

Để tìm nguyên hàm của các hàm số chứa căn thức (hàm số vô tỉ) ta cần linh hoạt lựa chọn một trong các phương pháp cơ bản sau:

1. Phương pháp tam thức bậc hai.

2. Phương pháp phân tích.

3. Phương pháp đổi biến.

4. Phương pháp nguyên hàm từng phần.

5. Sử dụng các phương pháp khác nhau.

Sau đây chúng ta cùng đi xem xét từng dạng.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng toán 1: Tìm nguyên hàm các hàm số chứa căn thức (hàm số vô tỉ) dựa trên tam thức bậc hai.

Trên cơ sở đưa tam thức bậc hai về dạng chính tắc và dùng các công thức sau:

1. $\int {\frac{{xdx}}{{\sqrt {{x^2} \pm a} }}} = \sqrt {{x^2} \pm a} + C.$

2. $\int {\frac{{dx}}{{\sqrt {{x^2} \pm a} }}} = \ln \left| {x + \sqrt {{x^2} \pm a} } \right| + C.$

3. $\int {\sqrt {{x^2} \pm a} } dx$ $= \frac{x}{2}\sqrt {{x^2} \pm a}$ $\pm \frac{a}{2}\ln \left| {x + \sqrt {{x^2} \pm a} } \right|$ $+ C.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 1: Tìm nguyên hàm các hàm số chứa căn thức sau:

a) $\int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}} .$

b) $\int {\frac{{(2x + 1)dx}}{{\sqrt {2{x^2} + 2x} }}} .$

a) Ta có thể lựa chọn các cách trình bày sau:

Cách 1: Ta biến đổi: $\int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\frac{{d\left( {{x^2} + 1} \right)}}{{2\sqrt {{x^2} + 1} }}}$ $= \sqrt {{x^2} + 1} + C.$

Cách 2: Đặt $u = {x^2} + 1$, suy ra: $du = 2xdx$ $\Leftrightarrow xdx = \frac{1}{2}du.$

Từ đó: $\int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\frac{{du}}{{2\sqrt u }}}$ $= \sqrt u + C$ $= \sqrt {{x^2} + 1} + C.$

Cách 3: Đặt $u = \sqrt {{x^2} + 1}$, suy ra: ${u^2} = {x^2} + 1$ $\Rightarrow 2udu = 2xdx$ $\Leftrightarrow xdx = udu.$

Từ đó: $\int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}} = \int {\frac{{udu}}{u}}$ $= \int {du} = u + C$ $= \sqrt {{x^2} + 1} + C.$

b) Ta có thể lựa chọn các cách trình bày sau:

Cách 1: Ta biến đổi: $\int {\frac{{(2x + 1)dx}}{{\sqrt {2{x^2} + 2x} }}}$ $= \int {\frac{{d\left( {2{x^2} + 2x} \right)}}{{2\sqrt {2{x^2} + 2x} }}}$ $= \sqrt {2{x^2} + 2x} + C.$

Cách 2: Đặt $u = 2{x^2} + 2x$, suy ra: $du = (4x + 2)dx$ $= 2(2x + 1)dx$ $\Leftrightarrow (2x + 1)dx = \frac{1}{2}du.$

Từ đó: $\int {\frac{{(2x + 1)dx}}{{\sqrt {2{x^2} + 2x} }}}$ $= \int {\frac{{du}}{{2\sqrt u }}}$ $= \sqrt u + C$ $= \sqrt {2{x^2} + 2x} + C.$

Cách 3: Đặt: $u = \sqrt {2{x^2} + 2x}$, suy ra: ${u^2} = 2{x^2} + 2x$ $\Rightarrow 2udu = (4x + 2)dx$ $= 2(2x + 1)dx$ $\Leftrightarrow (2x + 1)dx = udu.$

Từ đó: $\int {\frac{{(2x + 1)dx}}{{\sqrt {2{x^2} + 2x} }}}$ $= \int {\frac{{udu}}{u}}$ $= \int d u = u + C$ $= \sqrt {2{x^2} + 2x} + C.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 2: Tìm nguyên hàm các hàm số chứa căn thức sau:

a) $f(x) = \frac{1}{{\sqrt {{x^2} – a} }}.$

b) $f(x) = \frac{1}{{\sqrt {{x^2} – x – 1} }}.$

a) Đặt $t = x + \sqrt {{x^2} – a}$, suy ra: $dt = \left( {1 + \frac{x}{{\sqrt {{x^2} – a} }}} \right)dx$ $= \frac{{\sqrt {{x^2} – a} + x}}{{\sqrt {{x^2} – a} }}dx$ $= \frac{{tdx}}{{\sqrt {{x^2} – a} }}$ $\Leftrightarrow \frac{{dx}}{{\sqrt {{x^2} – a} }} = \frac{{dt}}{t}.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{dx}}{{\sqrt {{x^2} – a} }}}$ $= \int {\frac{{dt}}{t}}$ $= \ln |t| + C$ $= \ln \left| {x + \sqrt {{x^2} – a} } \right| + C.$

b) Ta có thể lựa chọn các cách trình bày sau:

Cách 1: Ta có: $\int f (x)dx$ $= \int {\frac{{dx}}{{\sqrt {{x^2} – x – 1} }}}$ $= \int {\frac{{dx}}{{\sqrt {{{\left( {x – \frac{1}{2}} \right)}^2} – \frac{5}{4}} }}} .$

Đặt $t = x – \frac{1}{2}$ $\Rightarrow dt = dx.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{dt}}{{\sqrt {{t^2} – \frac{5}{4}} }}}$ $= \ln \left| {t + \sqrt {{t^2} – \frac{5}{4}} } \right| + C$ $= \ln \left| {x – \frac{1}{2} + \sqrt {{x^2} – x – 1} } \right| + C.$

Cách 2: Ta có: $\int f (x)dx$ $= \int {\frac{{dx}}{{\sqrt {{x^2} – x – 1} }}}$ $= \int {\frac{{dx}}{{\sqrt {{{\left( {x – \frac{1}{2}} \right)}^2} – \frac{5}{4}} }}} .$

Đặt $t = x – \frac{1}{2} + \sqrt {{x^2} – x – 1}$, suy ra: $dt = \left( {1 + \frac{{2x – 1}}{{2\sqrt {{x^2} – x – 1} }}} \right)dx$ $= \left( {1 + \frac{{x – \frac{1}{2}}}{{\sqrt {{x^2} – x – 1} }}} \right)dx$ $= \frac{{\left( {\sqrt {{x^2} – x – 1} + x – \frac{1}{2}} \right)dx}}{{\sqrt {{x^2} – x – 1} }}$ $\Leftrightarrow \frac{{dx}}{{\sqrt {{x^2} – x – 1} }} = \frac{{dt}}{t}.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{dx}}{{\sqrt {{x^2} – x – 1} }}}$ $= \int {\frac{{dt}}{t}}$ $= \ln |t| + C$ $= \ln \left| {x – \frac{1}{2} + \sqrt {{x^2} – x – 1} } \right| + C.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 3: Biết rằng $\int {\frac{{dx}}{{\sqrt {{x^2} + 3} }}}$ $= \ln \left( {x + \sqrt {{x^2} + 3} } \right) + C.$ Tìm nguyên hàm: $I = \int {\sqrt {{x^2} + 3} } dx.$

Sử dụng phương pháp nguyên hàm từng phần bằng cách đặt:

$$
\left\{ {\begin{array}{l}
{u = \sqrt {{x^2} + 3} }\\
{dv = dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{x}{{\sqrt {{x^2} + 3} }}dx}\\
{v = x}
\end{array}} \right.
$$

Khi đó: $I = x\sqrt {{x^2} + 3} – \int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + 3} }}}$ $= x\sqrt {{x^2} + 3} – \int {\frac{{\left( {{x^2} + 3 – 3} \right)dx}}{{\sqrt {{x^2} + 3} }}}$ $= x\sqrt {{x^2} + 3}$ $– \int {\sqrt {{x^2} + 3} } dx$ $+ \int {\frac{{3dx}}{{\sqrt {{x^2} + 3} }}} .$

$\Leftrightarrow 2I = x\sqrt {{x^2} + 3}$ $+ 3\ln \left( {x + \sqrt {{x^2} + 3} } \right) + C.$

$\Leftrightarrow I = \frac{1}{2}x\sqrt {{x^2} + 3}$ $+ \frac{3}{2}\ln \left( {x + \sqrt {{x^2} + 3} } \right) + C.$

Chú ý: Với các em học sinh đã kinh nghiệm trong việc tính nguyên hàm có thể trình bày theo cách sau:

$\sqrt {{x^2} + 3}$ $= \frac{1}{2} \cdot \frac{{2{x^2} + 6}}{{\sqrt {{x^2} + 3} }}$ $= \frac{1}{2} \cdot \left( {\sqrt {{x^2} + 3} + \frac{{{x^2}}}{{\sqrt {{x^2} + 3} }}} \right)$ $+ \frac{3}{2} \cdot \frac{1}{{\sqrt {{x^2} + 3} }}$ $= \frac{1}{2} \cdot {\left( {x\sqrt {{x^2} + 3} } \right)^\prime } + \frac{3}{2} \cdot \frac{1}{{\sqrt {{x^2} + 3} }}.$

Khi đó: $I = \frac{1}{2}\int {{{\left( {x\sqrt {{x^2} + 3} } \right)}^\prime }} dx$ $+ \frac{3}{2}\int {\frac{{dx}}{{\sqrt {{x^2} + 3} }}}$ $= \frac{1}{2}x\sqrt {{x^2} + 3}$ $+ \frac{3}{2}\ln \left( {x + \sqrt {{x^2} + 3} } \right) + C.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 4: Tìm nguyên hàm của hàm số $f(x) = \frac{{{x^2}}}{{\sqrt {{x^2} + 1} }}.$

Ta có: $\int f (x)dx$ $= \int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\frac{{\left[ {\left( {{x^2} + 1} \right) – 1} \right]dx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\left( {\sqrt {{x^2} + 1} – \frac{1}{{\sqrt {{x^2} + 1} }}} \right)dx}$ $= \int {\sqrt {{x^2} + 1} } dx$ $– \int {\frac{{dx}}{{\sqrt {{x^2} + 1} }}}$ $= \frac{x}{2}\sqrt {{x^2} + 1}$ $+ \frac{1}{2}\ln \left| {x + \sqrt {{x^2} + 1} } \right|$ $– \ln \left| {x + \sqrt {{x^2} + 1} } \right| + C$ $= \frac{x}{2}\sqrt {{x^2} + 1}$ $– \frac{1}{2}\ln \left| {x + \sqrt {{x^2} + 1} } \right| + C.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 2: Tìm nguyên hàm của hàm số $f(x) = \sqrt {\frac{{x – a}}{{x + a}}}$, với $a > 0.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Vì điều kiện: $\frac{{x – a}}{{x + a}} \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge a}\\
{x < – a}
\end{array}} \right.
$$
 nên ta xét hai trường hợp:

Trường hợp 1: Với $x \ge a$ thì:

$\int f (x)dx$ $= \int {\sqrt {\frac{{x – a}}{{x + a}}} } dx$ $= \int {\frac{{(x – a)dx}}{{\sqrt {{x^2} – {a^2}} }}}$ $= \int {\frac{{2xdx}}{{2\sqrt {{x^2} – {a^2}} }}} – a\int {\frac{{dx}}{{\sqrt {{x^2} – {a^2}} }}}$ $= \sqrt {{x^2} – {a^2}}$ $– \ln \left| {x + \sqrt {{x^2} – {a^2}} } \right| + C.$

Trường hợp 2: Với $x < – a$ thì:

$\int f (x)dx$ $= \int {\sqrt {\frac{{x – a}}{{x + a}}} } dx$ $= – \int {\frac{{(x – a)dx}}{{\sqrt {{x^2} – {a^2}} }}}$ $= – \int {\frac{{2xdx}}{{2\sqrt {{x^2} – {a^2}} }}}$ $+ a\int {\frac{{dx}}{{\sqrt {{x^2} – {a^2}} }}}$ $= – \sqrt {{x^2} – {a^2}}$ $+ \ln \left| {x + \sqrt {{x^2} – {a^2}} } \right| + C.$

Cách 2: Đặt: $t = \sqrt {\frac{{x – a}}{{x + a}}}$ $\Rightarrow {t^2} = \frac{{x – a}}{{x + a}}$ $\Rightarrow x = \frac{{a\left( {1 + {t^2}} \right)}}{{1 – {t^2}}}$ $\Rightarrow dx = \frac{{4atdt}}{{{{\left( {1 – {t^2}} \right)}^2}}}.$

Khi đó: $\int f (x)dx$ $= \int {\sqrt {\frac{{x – a}}{{x + a}}} } dx$ $= \int {\frac{{4a{t^2}dt}}{{{{\left( {1 – {t^2}} \right)}^2}}}}$ $= 4a\int {\frac{{\left[ {\left( {{t^2} – 1} \right) + 1} \right]dt}}{{{{\left( {{t^2} – 1} \right)}^2}}}}$ $= 4a\left[ {\underbrace {\int {\frac{{dt}}{{{t^2} – 1}}} }_{{I_1}} + \underbrace {\int {\frac{{dt}}{{{{\left( {{t^2} – 1} \right)}^2}}}} }_{{1_2}}} \right].$

Các nguyên hàm $I_1$ và $I_2$ chúng ta đã biết cách giải.

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \sqrt {\frac{{x – 1}}{{x + 1}}} .$

Vì điều kiện $\frac{{x – 1}}{{x + 1}} \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge 1}\\
{x < – 1}
\end{array}} \right.
$$
, ta xét hai trường hợp:

Trường hợp 1: Với $x \ge 1$ thì:

$\int f (x)dx$ $= \int {\sqrt {\frac{{x – 1}}{{x + 1}}} } dx$ $= \int {\frac{{(x – 1)dx}}{{\sqrt {{x^2} – 1} }}}$ $= \int {\frac{{2xdx}}{{2\sqrt {{x^2} – 1} }}} – \int {\frac{{dx}}{{\sqrt {{x^2} – 1} }}}$ $= \sqrt {{x^2} – 1}$ $– \ln \left| {x + \sqrt {{x^2} – 1} } \right| + C.$

Trường hợp 2: Với $x < – 1$ thì:

$\int f (x)dx$ $= \int {\sqrt {\frac{{x – 1}}{{x + 1}}} } dx$ $= – \int {\frac{{(x – 1)dx}}{{\sqrt {{x^2} – 1} }}}$ $= – \int {\frac{{2xdx}}{{2\sqrt {{x^2} – 1} }}} + \int {\frac{{dx}}{{\sqrt {{x^2} – 1} }}}$ $= – \sqrt {{x^2} – 1}$ $+ \ln \left| {x + \sqrt {{x^2} – 1} } \right| + C.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 3: Tìm nguyên hàm của hàm số $f(x) = \frac{{dx}}{{\sqrt {ax + b} + \sqrt {ax + c} }}$, với $a \ne 0$ và $b – c \ne 0.$

Khử tính vô tỉ ở mẫu số bằng cách trục căn thức, ta được:

$I = \frac{1}{{b – c}}\int {(\sqrt {ax + b} + \sqrt {ax + c} )} dx$ $= \frac{1}{{a(b – c)}}\left[ {\int {{{(ax + b)}^{1/2}}} d(ax + b) + \int {{{(ax + c)}^{1/2}}} d(ax + c)} \right]$ $= \frac{2}{{3a(b – c)}}\left[ {\sqrt {{{(ax + b)}^3}} + \sqrt {{{(ax + c)}^3}} } \right] + C.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 1: Tìm nguyên hàm của hàm số: $f(x) = \tan x + \frac{1}{{\sqrt {2x + 1} + \sqrt {2x – 1} }}.$

Ta có: $\int f (x)dx$ $= \int {\left( {\tan x + \frac{1}{{\sqrt {2x + 1} + \sqrt {2x – 1} }}} \right)} dx$ $= \int {\frac{{\sin xdx}}{{\cos x}}}$ $+ \int {\frac{{\sqrt {2x + 1} – \sqrt {2x – 1} }}{2}} dx$ $= – \ln |\cos x|$ $+ \frac{1}{3}\left[ {{{(2x + 1)}^{3/2}} – {{(2x – 1)}^{3/2}}} \right] + C.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Ví dụ 2: Tìm nguyên hàm của hàm số: $f(x) = \frac{{2x}}{{x + \sqrt {{x^2} – 1} }}.$

Ta có thể lựa chọn một trong hai cách giải sau:

Cách 1: (Sử dụng phương pháp biến đổi): Ta có:

$\int f (x)dx$ $= \int {\frac{{2x}}{{x + \sqrt {{x^2} – 1} }}} dx$ $= \int {\frac{{2x\left( {x – \sqrt {{x^2} – 1} } \right)}}{{{x^2} – {x^2} + 1}}} dx$ $= \int 2 {x^2}dx – \int 2 x\sqrt {{x^2} – 1} dx$ $= \frac{2}{3}{x^3} – \int {\sqrt {{x^2} – 1} } d\left( {{x^2} – 1} \right) + C$ $= \frac{2}{3}{x^3} – \frac{2}{3}\sqrt {{{\left( {{x^2} – 1} \right)}^3}} + C.$

Cách 2: (Sử dụng phương pháp đổi biến số): Đặt $t = x + \sqrt {{x^2} – 1}$ ta có:

$t – x = \sqrt {{x^2} – 1}$ $\Rightarrow x = \frac{{{t^2} + 1}}{{2t}}$ $\Rightarrow dx = \frac{{{t^2} – 1}}{{2{t^2}}}dt.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{2xdx}}{{x + \sqrt {{x^2} – 1} }}}$ $= \int {\frac{{2 \cdot \frac{{{t^2} + 1}}{{2t}} \cdot \frac{{{t^2} – 1}}{{2{t^2}}}dt}}{t}}$ $= \int {\frac{{\left( {{t^4} – 1} \right)dt}}{{2{t^4}}}}$ $= \frac{1}{2}\int {\left( {1 – \frac{1}{{{t^4}}}} \right)} dt$ $= \frac{1}{2}\left( {t + \frac{1}{{3{t^3}}}} \right) + C$ $= \frac{1}{2}\left( {x + \sqrt {{x^2} – 1} } \right)$ $+ \frac{1}{{6{{\left( {x + \sqrt {{x^2} – 1} } \right)}^3}}} + C.$

<!-- chunk:10 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 4: Tìm nguyên hàm của hàm số chứa căn thức (hàm số vô tỉ) bằng cách sử dụng các đồng nhất thức.
Ví dụ: Tìm nguyên hàm của hàm số: $f(x) = \frac{x}{{\sqrt[{10}]{{x + 1}}}}.$

Sử dụng đồng nhất thức $x = x + 1 – 1$, ta được: $f(x) = \frac{{x + 1 – 1}}{{\sqrt[{10}]{{x + 1}}}}$ $= {(x + 1)^{9/10}} – {(x + 1)^{ – 1/10}}.$

Do đó: $\int f (x)dx$ $= \int {\left[ {{{(x + 1)}^{9/10}} – {{(x + 1)}^{ – 1/10}}} \right]} dx$ $= \frac{{10}}{{19}}{(x + 1)^{19/10}}$ $– \frac{{10}}{9}{(x + 1)^{9/10}} + C.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 5: Tìm nguyên hàm của hàm số: $f(x) = \frac{{v(x)dx}}{{\sqrt {{u^2}(x) \pm \alpha } }}.$

Ta thực hiện theo các bước sau:

Bước 1: Phân tích: $\frac{{v(x)}}{{\sqrt {{u^2}(x) + \alpha } }}$ $= \frac{{a\left[ {{u^2}(x) + \alpha } \right]}}{{\sqrt {{u^2}(x) + \alpha } }}$ $+ \frac{{bu(x)}}{{\sqrt {{u^2}(x) + \alpha } }}$ $+ \frac{c}{{\sqrt {{u^2}(x) + \alpha } }}.$

Sử dụng phương pháp hằng số bất định ta xác định được $a,b,c.$

Bước 2: Áp dụng các công thức:

1. $\int {\frac{{xdx}}{{\sqrt {{x^2} \pm a} }}}$ $= \sqrt {{x^2} \pm a} + C.$

2. $\int {\frac{{dx}}{{\sqrt {{x^2} \pm a} }}}$ $= \ln \left| {x + \sqrt {{x^2} \pm a} } \right| + C.$

3. $\int {\sqrt {{x^2} \pm a} } dx$ $= \frac{x}{2}\sqrt {{x^2} \pm a}$ $\pm \frac{a}{2}\ln \left| {x + \sqrt {{x^2} \pm a} } \right| + C.$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \frac{{2{x^2} + 1}}{{\sqrt {{x^2} + 2x} }}.$

Ta có: $\frac{{2{x^2} + 1}}{{\sqrt {{x^2} + 2x} }}$ $= \frac{{2{x^2} + 1}}{{\sqrt {{{(x + 1)}^2} – 1} }}$ $= \frac{{a\left[ {{{(x + 1)}^2} – 1} \right]}}{{\sqrt {{{(x + 1)}^2} – 1} }}$ $+ \frac{{b(x + 1)}}{{\sqrt {{{(x + 1)}^2} – 1} }}$ $+ \frac{c}{{\sqrt {{{(x + 1)}^2} – 1} }}$ $= \frac{{a{x^2} + (2a + b)x + b + c}}{{\sqrt {{x^2} + 2x} }}.$

Đồng nhất đẳng thức, ta được:

$$
\left\{ {\begin{array}{l}
{a = 2}\\
{2a + b = 0}\\
{b + c = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 2}\\
{b = – 4}\\
{c = 5}
\end{array}} \right.
$$

Khi đó: $\frac{{2{x^2} + 1}}{{\sqrt {{x^2} + 2x} }}$ $= 2\sqrt {{{(x + 1)}^2} – 1}$ $– \frac{{4(x + 1)}}{{\sqrt {{{(x + 1)}^2} – 1} }}$ $+ \frac{5}{{\sqrt {{{(x + 1)}^2} – 1} }}.$

Do đó: $\int f (x)dx$ $= \int {\left[ {2\sqrt {{{(x + 1)}^2} – 1} – \frac{{4(x + 1)}}{{\sqrt {{{(x + 1)}^2} – 1} }} + \frac{5}{{\sqrt {{{(x + 1)}^2} – 1} }}} \right]} dx$ $= (x + 1)\sqrt {{x^2} + 2x}$ $– \ln \left| {x + 1 + \sqrt {{x^2} + 2x} } \right|$ $– 4\sqrt {{x^2} + 2x}$ $+ 5\ln \left| {x + 1 + \sqrt {{x^2} + 2x} } \right| + C$ $= (x + 1)\sqrt {{x^2} + 2x}$ $+ 4\ln \left| {x + 1 + \sqrt {{x^2} + 2x} } \right|$ $– 4\sqrt {{x^2} + 2x} + C.$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 6: (Phương pháp đổi biến) Tìm nguyên hàm của hàm số: $f(x) = \frac{1}{{\sqrt {(x + a)(x + b)} }}.$

Ta xét hai trường hợp:

Trường hợp 1: Với: 
$$
\left\{ {\begin{array}{l}
{x + a > 0}\\
{x + b > 0}
\end{array}} \right.
$$

Đặt $t = \sqrt {x + a} + \sqrt {x + b}$, suy ra: $dt = \left( {\frac{1}{{2\sqrt {x + a} }} + \frac{1}{{2\sqrt {x + b} }}} \right)dx$ $= \frac{{(\sqrt {x + a} + \sqrt {x + b} )dx}}{{2\sqrt {(x + a)(x + b)} }}.$

$\Leftrightarrow \frac{{dx}}{{\sqrt {(x + a)(x + b)} }} = \frac{{2dt}}{t}.$

Khi đó: $\int f (x)dx$ $= 2\int {\frac{{dt}}{t}}$ $= 2\ln |t| + C$ $= 2\ln |\sqrt {x + a} + \sqrt {x + b} | + C.$

Trường hợp 2: Với: 
$$
\left\{ {\begin{array}{l}
{x + a < 0}\\
{x + b < 0}
\end{array}} \right.
$$

Đặt $t = \sqrt { – (x + a)} + \sqrt { – (x + b)}$, suy ra: $dt = \left[ { – \frac{1}{{2\sqrt { – (x + a)} }} – \frac{1}{{2\sqrt { – (x + b)} }}} \right]dx$ $= – \frac{{[\sqrt { – (x + a)} + \sqrt { – (x + b)} ]dx}}{{2\sqrt {(x + a)(x + b)} }}.$

$\Leftrightarrow \frac{{dx}}{{\sqrt {(x + a)(x + b)} }} = – \frac{{2dt}}{t}.$

Khi đó: $\int f (x)dx$ $= – 2\int {\frac{{dt}}{t}}$ $= – 2\ln |t| + C$ $= – 2\ln |\sqrt { – (x + a)} + \sqrt { – (x + b)} | + C.$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \frac{1}{{\sqrt {{x^2} – 5x + 6} }}.$

Biến đổi $I$ về dạng: $\int f (x)dx$ $= \int {\frac{{dx}}{{\sqrt {(x – 2)(x – 3)} }}} .$

Ta xét hai trường hợp:

Trường hợp 1: Với: 
$$
\left\{ {\begin{array}{l}
{x – 2 > 0}\\
{x – 3 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow x > 3.$

Đặt $t = \sqrt {x – 2} + \sqrt {x – 3}$, suy ra: $dt = \left( {\frac{1}{{2\sqrt {x – 2} }} + \frac{1}{{2\sqrt {x – 3} }}} \right)dx$ $= \frac{{(\sqrt {x – 2} + \sqrt {x – 3} )dx}}{{2\sqrt {(x – 2)(x – 3)} }}.$

$\Leftrightarrow \frac{{dx}}{{\sqrt {(x – 2)(x – 3)} }} = \frac{{2dt}}{t}.$

Khi đó: $\int f (x)dx$ $= 2\int {\frac{{dt}}{t}}$ $= 2\ln |t| + C$ $= 2\ln |\sqrt {x – 2} + \sqrt {x – 3} | + C.$

Trường hợp 2: Với 
$$
\left\{ {\begin{array}{l}
{x – 2 < 0}\\
{x – 3 < 0}
\end{array}} \right.
$$
 $\Leftrightarrow x < 2.$

Đặt $t = \sqrt {2 – x} + \sqrt {3 – x}$, suy ra: $dt = \left[ { – \frac{1}{{2\sqrt {2 – x} }} – \frac{1}{{2\sqrt {3 – x} }}} \right]dx$ $= – \frac{{[\sqrt {2 – x} + \sqrt {3 – x} ]dx}}{{2\sqrt {(x – 2)(x – 3)} }}.$

$\Leftrightarrow \frac{{dx}}{{\sqrt {(x – 2)(x – 3)} }} = – \frac{{2dt}}{t}.$

Khi đó: $\int f (x)dx$ $= – 2\int {\frac{{dt}}{t}}$ $= – 2\ln |t| + C$ $= – 2\ln |\sqrt {2 – x} + \sqrt {3 – x} | + C.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 7: (Phương pháp đổi biến): Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt {{a^2} – {x^2}} } \right)dx$ với $a > 0.$

Ta thực hiện theo các bước sau:

Bước 1: Đặt 
$$
\left[ {\begin{array}{l}
{x = |a|\sin t\:{\rm{với}}\: – \frac{\pi }{2} \le t \le \frac{\pi }{2}}\\
{x = |a|\cos t\:{\rm{với}}\:0 \le t \le \pi }
\end{array}} \right.
$$
 (hoặc có thể $t = x + \sqrt {{a^2} – {x^2}}$).

Bước 2: Bài toán được chuyển về $I = \int S (\sin t,\cos t)dt.$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \frac{{{x^3}}}{{\sqrt {1 – {x^2}} }}.$

Ta có thể trình bày theo hai cách sau:

Cách 1: Đặt $x = \sin t$, $– \frac{\pi }{2} < t < \frac{\pi }{2}$, suy ra: $dx = \cos tdt$ và $\frac{{{x^3}dx}}{{\sqrt {1 – {x^2}} }}$ $= \frac{{{{\sin }^3}t\cos tdt}}{{\cos t}}$ $= {\sin ^3}tdt$ $= \frac{1}{4}(3\sin t – \sin 3t)dt.$

Khi đó: $\int f (x)dx$ $= \frac{1}{4}\int {(3\sin t – \sin 3t)} dt$ $= – \frac{3}{4}\cos t + \frac{1}{{12}}\cos 3t + C$ $= – \frac{3}{4}\cos t + \frac{1}{{12}}\left( {4{{\cos }^3}t – 3\cos t} \right) + C$ $= \frac{1}{3}{\cos ^3}t – \cos t + C$ $= \left( {\frac{1}{3}{{\cos }^2}t – 1} \right)\cos t + C$ $= \left[ {\frac{1}{3}\left( {1 – {{\sin }^2}t} \right) – 1} \right]\cos t + C$ $= \left[ {\frac{1}{3}\left( {1 – {x^2}} \right) – 1} \right]\sqrt {1 – {x^2}} + C$ $= – \frac{1}{3}\left( {{x^2} + 2} \right)\sqrt {1 – {x^2}} + C.$

Chú ý: Trong các giải trên ta có: $– \frac{\pi }{2} < t < \frac{\pi }{2}$ $\Rightarrow \cos t > 0$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\sqrt {{{\cos }^2}t} = \cos t}\\
{\cos t = \sqrt {1 – {{\sin }^2}t} = \sqrt {1 – {x^2}} }
\end{array}} \right.
$$

Cách 2: Đặt $t = \sqrt {1 – {x^2}}$, suy ra: ${x^2} = 1 – {t^2}$, từ đó: $2xdx = – 2tdt$ và $\frac{{{x^3}dx}}{{\sqrt {1 – {x^2}} }}$ $= \frac{{{x^2}xdx}}{{\sqrt {1 – {x^2}} }}$ $= \frac{{\left( {1 – {t^2}} \right)( – tdt)}}{t}$ $= \left( {{t^2} – 1} \right)dt.$

Khi đó: $\int f (x)dx$ $= \int {\left( {{t^2} – 1} \right)} dt$ $= \frac{1}{3}{t^3} – t + C$ $= \frac{1}{3}\left( {{t^2} – 3} \right)t + C$ $= – \frac{1}{3}\left( {{x^2} + 2} \right)\sqrt {1 – {x^2}} + C.$

<!-- chunk:14 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 8: (Phương pháp đổi biến) Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt {{a^2} + {x^2}} } \right)dx$, với $a > 0.$

Ta thực hiện theo các bước sau:

Bước 1: Đặt 
$$
\left[ {\begin{array}{l}
{x = |a|\tan t\:{\rm{với}}\: – \frac{\pi }{2} < t < \frac{\pi }{2}}\\
{x = |a|\cot t\:{\rm{với}}\:0 < t < \pi }
\end{array}} \right.
$$
 (hoặc có thể $t = x + \sqrt {{a^2} + {x^2}}$).

Bước 2: Bài toán được chuyển về $I = \int S (\sin t,\cos t)dt.$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \sqrt {1 + {x^2}} .$

Ta có thể trình bày theo hai cách sau:

Cách 1: Đặt $x = \tan t$, $– \frac{\pi }{2} < t < \frac{\pi }{2}$, suy ra: $dx = \frac{{dt}}{{{{\cos }^2}t}}$ và $\sqrt {1 + {x^2}} dx = \frac{{dt}}{{{{\cos }^3}t}}.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{dt}}{{{{\cos }^3}t}}}$ $= \int {\frac{{\cos tdt}}{{{{\cos }^4}t}}}$ $= \int {\frac{{\cos tdt}}{{{{\left( {1 – {{\sin }^2}t} \right)}^2}}}} .$

Đặt $u = \sin t$, suy ra: $du = \cos tdt$ và $\frac{{{\rm{ }}\cos tdt{\rm{ }}}}{{{{\left( {1 – {{\sin }^2}t} \right)}^2}}}$ $= \frac{{du}}{{{{(u + 1)}^2}{{(u – 1)}^2}}}.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{du}}{{{{(u + 1)}^2}{{(u – 1)}^2}}}}$ $= \frac{1}{4}\left[ {\ln \left| {\frac{{u + 1}}{{u – 1}}} \right| – \frac{{2u}}{{(u + 1)(u – 1)}}} \right] + C$ $= \frac{1}{4}\left[ {\ln \left| {\frac{{\sin t + 1}}{{\sin t – 1}}} \right| – \frac{{2\sin t}}{{(\sin t + 1)(\sin t – 1)}}} \right] + C$ $= \frac{1}{4}\left[ {\ln \left| {\frac{{\frac{x}{{\sqrt {1 + {x^2}} }} + 1}}{{\frac{x}{{\sqrt {1 + {x^2}} }} – 1}}} \right| – \frac{{2\frac{x}{{\sqrt {1 + {x^2}} }}}}{{\left( {\frac{x}{{\sqrt {1 + {x^2}} }} + 1} \right)\left( {\frac{x}{{\sqrt {1 + {x^2}} }} – 1} \right)}}} \right] + C$ $= \frac{1}{4}\left( {\ln \left| {\frac{{x + \sqrt {1 + {x^2}} }}{{x – \sqrt {1 + {x^2}} }}} \right| + 2x\sqrt {1 + {x^2}} } \right) + C$ $= \frac{1}{4}\left( {2\ln \left| {x + \sqrt {1 + {x^2}} } \right| + 2x\sqrt {1 + {x^2}} } \right) + C$ $= \frac{1}{2}\left( {\ln \left| {x + \sqrt {1 + {x^2}} } \right| + x\sqrt {1 + {x^2}} } \right) + C.$

Cách 2: Đặt $t = x + \sqrt {1 + {x^2}}$, suy ra: $t – x = \sqrt {1 + {x^2}}$ $\Rightarrow {(t – x)^2} = 1 + {x^2}$ $\Rightarrow x = \frac{{{t^2} – 1}}{{2t}}.$

$\Rightarrow \sqrt {1 + {x^2}}$ $= t – \frac{{{t^2} – 1}}{{2t}}$ $= \frac{{{t^2} + 1}}{{2t}}.$

$\Rightarrow dt = \left( {1 + \frac{x}{{\sqrt {1 + {x^2}} }}} \right)dx$ $= \frac{{x + \sqrt {1 + {x^2}} }}{{\sqrt {1 + {x^2}} }}dx$ $= \frac{{2{t^2}}}{{{t^2} + 1}}dx$ $\Leftrightarrow dx = \frac{{{t^2} + 1}}{{2{t^2}}}dt$, $\sqrt {1 + {x^2}} dx$ $= \frac{{{t^2} + 1}}{{2t}} \cdot \frac{{{t^2} + 1}}{{2{t^2}}}dt$ $= \frac{1}{4}\frac{{{{\left( {{t^2} + 1} \right)}^2}}}{{{t^3}}}dt$ $= \frac{1}{4}\left( {t + \frac{2}{t} + \frac{1}{{{t^3}}}} \right)dt.$

Khi đó: $\int f (x)dx$ $= \frac{1}{4}\int {\left( {t + \frac{2}{t} + \frac{1}{{{t^3}}}} \right)} dt$ $= \frac{1}{4}\left( {\frac{1}{2}{t^2} + 2\ln |t| – \frac{1}{{2{t^2}}}} \right) + C$ $= \frac{1}{8}\left[ {\left( {{t^2} – \frac{1}{{{t^2}}}} \right) + 4\ln |t|} \right] + C$ $= \frac{1}{8}\left[ {4x\sqrt {1 + {x^2}} + 4\ln \left| {x + \sqrt {1 + {x^2}} } \right|} \right] + C$ $= \frac{1}{2}\left( {\ln \left| {x + \sqrt {1 + {x^2}} } \right| + x\sqrt {1 + {x^2}} } \right) + C.$

Cách 3: (Sử dụng phương pháp tích phân từng phần).

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt {{x^2} + 1} }\\
{dv = dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{{xdx}}{{\sqrt {{x^2} + 1} }}}\\
{v = x}
\end{array}} \right.
$$

Khi đó: $I = \int f (x)dx$ $= x\sqrt {{x^2} + 1} – \int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + 1} }}} .$

Trong đó: $\int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\frac{{\left[ {\left( {{x^2} + 1} \right) – 1} \right]dx}}{{\sqrt {{x^2} + 1} }}}$ $= \int {\sqrt {{x^2} + 1} } dx – \int {\frac{{dx}}{{\sqrt {{x^2} + 1} }}}$ $= I – \ln \left| {x + \sqrt {{x^2} + 1} } \right| + C.$

Vậy: $I = x\sqrt {{x^2} + 1}$ $– \left( {I – a\ln \left| {x + \sqrt {{x^2} + 1} } \right| + C} \right).$

$\Leftrightarrow 2I = x\sqrt {{x^2} + 1} + \ln \left| {x + \sqrt {{x^2} + 1} } \right| + C.$

$\Leftrightarrow I = \frac{x}{2}\sqrt {{x^2} + 1} + \frac{1}{2}\ln \left| {x + \sqrt {{x^2} + 1} } \right| + C.$

Chú ý:

1. Trong cách giải thứ nhất sở dĩ ta có: $\sqrt {1 + {x^2}} = \frac{1}{{\cos t}}$ và $\sin t = \frac{x}{{\sqrt {1 + {x^2}} }}$ là bởi $– \frac{\pi }{2} < t < \frac{\pi }{2}$ $\Rightarrow \cos t > 0$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\sqrt {{{\cos }^2}t} = \cos t}\\
{\sin t = \tan t.\cos t = \frac{x}{{\sqrt {1 + {x^2}} }}}
\end{array}} \right.
$$

2. Cả ba phương pháp trên (tốt nhất là phương pháp 2) được áp dụng để tìm các nguyên hàm:

$\int {\sqrt {{x^2} + a} } dx$ $= \frac{a}{2}\ln \left| {x + \sqrt {{x^2} + a} } \right|$ $+ \frac{x}{2}\sqrt {{x^2} + a} + C.$

$\int {\frac{{dx}}{{\sqrt {{x^2} + a} }}}$ $= \ln \left| {x + \sqrt {{x^2} + a} } \right| + C.$

3. Với nguyên hàm $\int {\frac{{dx}}{{\sqrt {{{\left( {{a^2} + {x^2}} \right)}^{2k + 1}}} }}}$, với $k \in Z$ tốt nhất là sử dụng phương pháp 1.

4. Với nguyên hàm $I = \int {\sqrt {(x + a)(x + b)} } dx$ ta có thể thực hiện như sau:

Đặt $t = x + \frac{{a + b}}{2}$ và $A = – \frac{{{{(b – a)}^2}}}{4}$, suy ra: $dt = dx$ và $\sqrt {(x + a)(x + b)} dx$ $= \sqrt {{t^2} + A} dt.$

Khi đó: $I = \int {\sqrt {{t^2} + A} } dt$ $= \frac{A}{2}\ln \left| {t + \sqrt {{t^2} + A} } \right|$ $+ \frac{t}{2}\sqrt {{t^2} + A} + C$ $= – \frac{{{{(b – a)}^2}}}{8}\ln \left| {x + \frac{{a + b}}{2} + \sqrt {(x + a)(x + b)} } \right|$ $+ \frac{{2x + a + b}}{4}\sqrt {(x + a)(x + b)} + C.$

<!-- chunk:15 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 9: (Phương pháp đổi biến): Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt {{x^2} – {a^2}} } \right)dx$, với $a > 0.$

Ta thực hiện theo các bước sau:

Bước 1: Đặt 
$$
\left[ {\begin{array}{l}
{x = \frac{{|a|}}{{\sin t}}\:{\rm{với}}\:t \in \left[ { – \frac{\pi }{2},\frac{\pi }{2}} \right]\backslash \{ 0\} }\\
{x = \frac{{|a|}}{{\cos t}}\:{\rm{với}}\:t \in [0,\pi ]\backslash \left\{ {\frac{\pi }{2}} \right\}}
\end{array}} \right.
$$
 (hoặc có thể $t = \sqrt {{x^2} – {a^2}} .$

Bước 2: Bài toán được chuyển về $I = \int S (\sin t,\cos t)dt.$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \frac{x}{{2{x^2} – 1 + 3\sqrt {{x^2} – 1} }}.$

Ta có thể trình bày theo hai cách sau:

Cách 1: Đặt $t = \sqrt {{x^2} – 1}$ thì ${t^2} = {x^2} – 1$, suy ra: $2tdt = 2xdx$ và $\frac{{xdx}}{{2{x^2} – 1 + 3\sqrt {{x^2} – 1} }}$ $= \frac{{xdx}}{{2\left( {{x^2} – 1} \right) + 3\sqrt {{x^2} – 1} + 1}}$ $= \frac{{{\rm{ }}tdt{\rm{ }}}}{{2{t^2} + 3t + 1}}.$

Khi đó: $\int f (x)dx = \int {\frac{{tdt}}{{2{t^2} + 3t + 1}}} .$

Ta có: $\frac{1}{{2{t^2} + 3t + 1}}$ $= \frac{t}{{(2t + 1)(t + 1)}}$ $= \frac{a}{{2t + 1}} + \frac{b}{{t + 1}}$ $= \frac{{(a + 2b)t + a + b}}{{(2t + 1)(t + 1)}}.$

Đồng nhất đẳng thức, ta được: 
$$
\left\{ {\begin{array}{l}
{a + 2b = 1}\\
{a + b = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = – 1}\\
{b = 1}
\end{array}} \right.
$$

Khi đó: $\frac{t}{{2{t^2} + 3t + 1}}$ $= – \frac{1}{{2t + 1}} + \frac{1}{{t + 1}}.$

Do đó: $\int f (x)dx$ $= \int {\left( { – \frac{1}{{2t + 1}} + \frac{1}{{t + 1}}} \right)} dt$ $= – \frac{1}{2}\ln |2t + 1| + \ln |t + 1| + C$ $= \frac{1}{2}\ln \frac{{{{(t + 1)}^2}}}{{|2t + 1|}} + C$ $= \frac{1}{2}\ln \frac{{{{\left( {\sqrt {{x^2} – 1} + 1} \right)}^2}}}{{2\sqrt {{x^2} – 1} + 1}} + C.$

Cách 2: Vì điều kiện $|x| > 1$, ta xét hai trường hợp:

Trường hợp 1: Với $x > 1$ thì đặt $x = \frac{1}{{\cos t}}$, $t \in \left[ {0;\frac{\pi }{2}} \right)$ suy ra $dx = \frac{{\sin tdt}}{{{{\cos }^2}t}}.$

Khi đó: $I = \int f (x)dx$ $= \int {\frac{{xdx}}{{2{x^2} – 1 + 3\sqrt {{x^2} – 1} }}}$ $= \int {\frac{{\frac{1}{{\cos t}} \cdot \frac{{\sin t}}{{{{\cos }^2}t}}dt}}{{\frac{2}{{{{\cos }^2}t}} – 1 + 3\tan t}}}$ $= \int {\frac{{\left( {1 + {{\tan }^2}t} \right)\tan tdt}}{{2\left( {1 + {{\tan }^2}t} \right) – 1 + 3\tan t}}}$ $= \int {\frac{{\left( {1 + {{\tan }^2}t} \right)\tan tdt}}{{2{{\tan }^2}t + 3\tan t + 1}}} .$

Đặt $u = \tan t$ suy ra: $du = \frac{{dt}}{{{{\cos }^2}t}} = \left( {1 + {{\tan }^2}t} \right)dt.$

Khi đó: $I = \int {\frac{{udu}}{{2{u^2} + 3u + 1}}}$ $= \int {\left( { – \frac{1}{{2u + 1}} + \frac{1}{{u + 1}}} \right)} du$ $= – \frac{1}{2}\ln |2u + 1| + \ln |u + 1| + C$ $= \frac{1}{2}\ln \frac{{{{(u + 1)}^2}}}{{|2u + 1|}} + C$ $= \frac{1}{2}\ln \frac{{{{(\tan t + 1)}^2}}}{{|2\tan t + 1|}} + C$ $= \frac{1}{2}\ln \frac{{{{\left( {\sqrt {{x^2} – 1} + 1} \right)}^2}}}{{2\sqrt {{x^2} – 1} + 1}} + C.$

Trường hợp 2: Với $x < – 1$: Bạn đọc tự giải.

<!-- chunk:16 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 10: (Phương pháp đổi biến) Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt {(x – a)(b – x)} } \right)dx.$

Ta thực hiện theo các bước sau:

Bước 1: Đặt $x = a + (b – a){\sin ^2}t.$

Bước 2: Bài toán được chuyển về $I = \int S (\sin t,\cos t)dt.$

Ví dụ: Tìm nguyên hàm của hàm số: $f(x) = \frac{1}{{\sqrt {{{[(x – a)(b – x)]}^3}} }}$ với $a < b.$

Đặt $x = a + (b – a){\sin ^2}t$, với $0 \le t \le \frac{\pi }{2}$ suy ra: $dx = 2(b – a) \sin t \cos tdt$ $= (b – a)\sin 2tdt$, $\frac{{dx}}{{\sqrt {{{[(x – a)(b – x)]}^3}} }}$ $= \frac{{(b – a)\sin 2tdt}}{{\sqrt {{{\left[ {(b – a){{\sin }^2}t(b – a){{\cos }^2}t} \right]}^3}} }}$ $= \frac{{(b – a)\sin 2tdt}}{{{{(b – a)}^3}{{\sin }^3}2t}}$ $= \frac{1}{{{{(b – a)}^2}}} \cdot \frac{{dt}}{{{{\sin }^2}2t}}.$

Khi đó: $\int f (x)dx$ $= \frac{1}{{{{(b – a)}^2}}}\int {\frac{{dt}}{{{{\sin }^2}2t}}}$ $= – \frac{{\cot 2t}}{{2{{(b – a)}^2}}} + C$ $= – \frac{{a + b – 2x}}{{2\sqrt {(x – a)(b – x)} }} + C.$

<!-- chunk:17 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 11: (Phương pháp đổi biến): Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt {a{x^2} + bx + c} } \right)dx.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: (Đưa $I$ về các dạng nguyên hàm cơ bản đã biết): Ta xét các trường hợp sau:

Trường hợp 1: Nếu $a > 0$ và $\Delta < 0$ thì ta thực hiện theo các bước:

Bước 1: Ta có: $a{x^2} + bx + c$ $= – \frac{\Delta }{{4a}}\left[ {1 + {{\left( {\frac{{2ax + b}}{{\sqrt { – \Delta } }}} \right)}^2}} \right].$

Bước 2: Thực hiện phép đổi biến: $t = \frac{{2ax + b}}{{\sqrt { – \Delta } }}.$

Bước 3: Bài toán được chuyển về $I = \int S \left( {t,\sqrt {1 + {t^2}} } \right)dt.$

Trường hợp 2: Nếu $a < 0$ và $\Delta > 0$ thì ta thực hiện theo các bước:

Bước 1: Ta có: $a{x^2} + bx + c$ $= – \frac{\Delta }{{4a}}\left[ {1 – {{\left( {\frac{{2ax + b}}{{\sqrt \Delta }}} \right)}^2}} \right].$

Bước 2: Thực hiện phép đổi biến: $t = \frac{{2ax + b}}{{\sqrt \Delta }}.$

Bước 3: Bài toán được chuyển về $I = \int S \left( {t,\sqrt {1 – {t^2}} } \right)dt.$

Trường hợp 3: Nếu $a > 0$ và $\Delta > 0$ thì ta thực hiện theo các bước:

Bước 1: Ta có: $a{x^2} + bx + c$ $= \frac{\Delta }{{4a}}\left[ {{{\left( {\frac{{2ax + b}}{{\sqrt \Delta }}} \right)}^2} – 1} \right].$

Bước 2: Thực hiện phép biến đổi: $t = \frac{{2ax + b}}{{\sqrt \Delta }}.$

Bước 3: Bài toán được chuyển về $I = \int S \left( {t,\sqrt {{t^2} – 1} } \right)dt.$

Cách 2: (Sử dụng phép thế Euler): Ta xét các trường hợp sau:

1. Nếu $a > 0$, đặt $\sqrt {a{x^2} + bx + c} = t – x\sqrt a$ hoặc $t + x\sqrt a .$

2. Nếu $c > 0$, đặt $\sqrt {a{x^2} + bx + c} = tx + \sqrt c$ hoặc $tx – \sqrt c .$

3. Nếu tam thức $a{x^2} + bx + c$ có biệt số $\Delta > 0$ thì: $a{x^2} + bx + c$ $= a\left( {x – {x_1}} \right)\left( {x – {x_2}} \right).$ Khi đó đặt $\sqrt {a{x^2} + bx + c} = t\left( {x – {x_1}} \right).$

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \sqrt {{x^2} + 2x + 2} .$

Sử dụng phép đổi biến $t = x + 1$ suy ra $dt = dx.$

Khi đó: $I = \int {\sqrt {{t^2} + 1} } dt.$ Tích phân này chúng ta biết biết cách xác định.

<!-- chunk:18 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 12: Tìm nguyên hàm của hàm số: $f(x) = \frac{{dx}}{{(\lambda x + \mu )\sqrt {a{x^2} + bx + c} }}.$

Ta thực hiện theo các bước sau:

Bước 1: Đặt $t = \frac{1}{{\lambda x + \mu }}.$

Bước 2: Bài toán được chuyển về $I = \int {\frac{{dt}}{{\sqrt {\alpha {t^2} + \beta t + \gamma } }}} .$

Chú ý: Phương pháp trên có thể được áp dụng cho dạng tổng quát hơn là: $I = \int {\frac{{(Ax + B)dx}}{{{{(\lambda x + \mu )}^n}\sqrt {a{x^2} + bx + c} }}} .$

Ví dụ: Tìm nguyên hàm của hàm số: $f(x) = \frac{1}{{(x + 1)\sqrt {{x^2} + 2x + 2} }}.$

Đặt $t = \frac{1}{{x + 1}}$ thì $x = \frac{1}{t} – 1$ suy ra: $dx = – \frac{1}{{{t^2}}}dt$, $\frac{{dx}}{{(x + 1)\sqrt {{x^2} + 2x + 2} }}$ $= \frac{{t\left( { – \frac{1}{{{t^2}}}} \right)dt}}{{\sqrt {\frac{1}{{{t^2}}} + 1} }}$ $= – \frac{{dt}}{{t\sqrt {\frac{1}{{{t^2}}} + 1} }}$ 
$$
= \left\{ {\begin{array}{l}
{ – \frac{{dt}}{{\sqrt {1 + {t^2}} }}\:{\rm{khi}}\:t > 0}\\
{\frac{{dt}}{{\sqrt {1 + {t^2}} }}\:{\rm{khi}}\:t < 0}
\end{array}} \right.
$$

Khi đó ta xét hai trường hợp:

Trường hợp 1: Với $t>0$, ta được: $\int f (x)dx$ $= \ln \left| {\frac{{1 – \sqrt {{x^2} + 2x + 2} }}{{x + 1}}} \right| + C.$

Trường hợp 2: Với $t < 0$. ta được: $\int f (x)dx$ $= \ln \left| {\frac{{1 – \sqrt {{x^2} + 2x + 2} }}{{x + 1}}} \right| + C.$

Tóm lại với $t \ne 0 \Leftrightarrow x \ne – 1$ ta luôn có: $\int f (x)dx$ $= \ln \left| {\frac{{1 – \sqrt {{x^2} + 2x + 2} }}{{x + 1}}} \right| + C.$

<!-- chunk:19 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 13: (Phương pháp đổi biến): Tìm nguyên hàm của hàm số: $I = \int R \left( {x,\sqrt[n]{{\frac{{ax + b}}{{cx + d}}}}} \right)dx$ với $ad – bc \ne 0.$
Ta thực hiện theo các bước sau:

Bước 1: Đặt $t = \sqrt[n]{{\frac{{ax + b}}{{cx + d}}}}$ $\Rightarrow {t^n} = \frac{{ax + b}}{{cx + d}}$ $\Leftrightarrow x = \frac{{b – d{t^n}}}{{c{t^n} – a}}.$

Bước 2: Bài toán được chuyển về: $I = \int S (t)dt.$

<!-- chunk:20 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 14: Tìm nguyên hàm của hàm số $f(x) = \frac{{P(x)}}{{Q(x)}} \cdot \frac{{dx}}{y}$, trong đó $y = \sqrt {a{x^2} + bx + c} .$

Ta thực hiện theo các bước sau:

Bước 1: Phân tích hàm hữu tỉ $\frac{{P(x)}}{{Q(x)}}$ thành các phân số tối giản.

Bước 2: Lựa chọn các phương pháp phù hợp cho mỗi tích phân mới.

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \frac{{6{x^3} + 8x + 1}}{{\left( {3{x^2} + 4} \right)\sqrt {{x^2} + 1} }}.$

Ta có: $\frac{{6{x^3} + 8x + 1}}{{3{x^2} + 4}}$ $= 2x + \frac{1}{{3{x^2} + 4}}.$

Do đó: $I = \int f (x)dx$ $= \int {\left( {2x + \frac{1}{{3{x^2} + 4}}} \right)} \frac{1}{{\sqrt {{x^2} + 1} }}dx$ $= \underbrace {\int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}} }_{{I_1}}$ $+ \underbrace {\int {\frac{{dx}}{{\left( {3{x^2} + 4} \right)\sqrt {{x^2} + 1} }}} }_{{I_2}}.$

Trong đó: ${I_1} = \int {\frac{{xdx}}{{\sqrt {{x^2} + 1} }}}$ $= \sqrt {x_.^2 + 1} + C.$

Với $I_2$ ta thực hiện phép đổi biến $t = \frac{x}{{\sqrt {{x^2} + 1} }}$ thì ${x^2} = \frac{{{t^2}}}{{1 – {t^2}}}$ suy ra: $dt = \frac{{dx}}{{\left( {{x^2} + 1} \right)\sqrt {{x^2} + 1} }}.$

Khi đó: ${I_2} = \int {\frac{{dx}}{{\left( {3{x^2} + 4} \right)\sqrt {{x^2} + 1} }}}$ $= \int {\frac{{\left( {{x^2} + 1} \right)\sqrt {{x^2} + 1} dt}}{{\left( {3{x^2} + 4} \right)\sqrt {{x^2} + 1} }}}$ $= \smallint \frac{{\left( {\frac{{{t^2}}}{{1 – {t^2}}} + 1} \right)dt}}{{\frac{{3{t^2}}}{{1 – {t^2}}} + 4}}$ $= \int {\frac{{dt}}{{4 – {t^2}}}}$ $= – \frac{1}{4}\ln \left| {\frac{{t – 2}}{{t + 2}}} \right| + C$ $= \frac{1}{4}\ln \left| {\frac{{t + 2}}{{t – 2}}} \right| + C$ $= \frac{1}{4}\ln \left| {\frac{{x + 2\sqrt {{x^2} + 1} }}{{x – 2\sqrt {{x^2} + 1} }}} \right| + C.$

Vậy: $I = \sqrt {{x^2} + 1}$ $+ \frac{1}{4}\ln \left| {\frac{{x + 2\sqrt {{x^2} + 1} }}{{x – 2\sqrt {{x^2} + 1} }}} \right| + C.$

<!-- chunk:21 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-chua-can-thuc.html -->
## Dạng 15: Phương pháp nguyên hàm từng phần.

Ví dụ: Tìm nguyên hàm của hàm số $f(x) = \sqrt {{x^2} + a} .$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \sqrt {{x^2} + a} }\\
{dv = dx}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{du = \frac{{xdx}}{{\sqrt {{x^2} + a} }}}\\
{v = x}
\end{array}} \right.
$$

Khi đó: $I = \int f (x)dx$ $= x\sqrt {{x^2} + a} – \underbrace {\int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + a} }}} }_J.$

Biến đổi $J$ như sau: $J = \int {\frac{{{x^2}dx}}{{\sqrt {{x^2} + a} }}}$ $= \int {\frac{{\left[ {\left( {{x^2} + a} \right) – a} \right]dx}}{{\sqrt {{x^2} + a} }}}$ $= \int {\sqrt {{x^2} + a} } dx – a\int {\frac{{dx}}{{\sqrt {{x^2} + a} }}}$ $= I – a\ln \left| {x + \sqrt {{x^2} + a} } \right| + C.$

Vậy: $I = x\sqrt {{x^2} + a}$ $– \left( {I – a\ln \left| {x + \sqrt {{x^2} + a} } \right| + C} \right)$ $\Leftrightarrow I = \frac{x}{2}\sqrt {{x^2} + a}$ $+ \frac{a}{2}\ln \left| {x + \sqrt {{x^2} + a} } \right| + C.$