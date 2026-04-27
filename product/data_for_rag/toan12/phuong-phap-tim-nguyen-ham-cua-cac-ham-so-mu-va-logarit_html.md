# Phương pháp tìm nguyên hàm của các hàm số mũ và logarit

<!-- chunk:0 level:0 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
Bài viết hướng dẫn giải bài toán tìm nguyên hàm của các hàm số mũ và logarit bằng cách sử dụng các phương pháp: dựa vào nguyên hàm cơ bản, phân tích, đổi biến và nguyên hàm từng phần … trong mỗi phương pháp sẽ có các ví dụ minh họa cụ thể với lời giải chi tiết.

Để xác định nguyên hàm của các hàm số mũ và logarit ta cần linh hoạt lựa chọn một trong các phương pháp cơ bản sau:

1. Sử dụng các dạng nguyên hàm cơ bản.

2. Phương pháp phân tích.

3. Phương pháp đổi biến.

4. Phương pháp nguyên hàm từng phần.

**Dạng toán 1: Tìm nguyên hàm của hàm số mũ và logarit dựa trên các dạng nguyên hàm cơ bản.**

Bằng các phép biến đổi đại số, ta biến đổi biểu thức dưới dấu tích phân về các dạng nguyên hàm cơ bản đã biết.

<!-- chunk:1 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 1: Tìm nguyên hàm của các hàm số sau:

a) $f(x) = \frac{1}{{{e^x} – {e^{ – x}}}}.$

b) $\frac{{{2^{2x}}{3^x}}}{{{{16}^x} – {9^x}}}.$

a) Ta có: $\int f (x)dx$ $= \int {\frac{{d\left( {{e^x}} \right)}}{{{e^{2x}} – 1}}}$ $= \frac{1}{2}\ln \left| {\frac{{{e^x} – 1}}{{{e^x} + 1}}} \right| + C.$

b) Chia tử số và mẫu số của biểu thức dưới dấu tích phân cho ${4^x}$, ta được:

$\int f (x)dx$ $= \int {\frac{{{{\left( {\frac{4}{3}} \right)}^x}}}{{{{\left( {\frac{4}{3}} \right)}^{2x}} – 1}}} dx$ $= \frac{1}{{\ln \frac{4}{3}}}\int {\frac{{d\left[ {{{\left( {\frac{4}{3}} \right)}^x}} \right]}}{{{{\left( {\frac{4}{3}} \right)}^{2x}} – 1}}} dx$ $= \frac{1}{{\ln \frac{4}{3}}}.\frac{1}{2}\ln \left| {\frac{{{{\left( {\frac{4}{3}} \right)}^x} – 1}}{{{{\left( {\frac{4}{3}} \right)}^x} + 1}}} \right| + C$ $= \frac{1}{{2(\ln 4 – \ln 3)}}\ln \left| {\frac{{{4^x} – {3^x}}}{{{4^x} + {3^x}}}} \right| + C.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 2: Tìm nguyên hàm của các hàm số sau:

a) $f(x) = \frac{1}{{1 + {8^x}}}.$

b) $f(x) = \frac{{\ln (ex)}}{{3 + x\ln x}}.$

a) Ta có: $\int f (x)dx$ $= \int {\frac{1}{{1 + {8^x}}}} dx$ $= \int {\left( {1 – \frac{{{8^x}}}{{1 + {8^x}}}} \right)} dx$ $= x – \frac{{\ln \left( {1 + {8^x}} \right)}}{{\ln 8}} + C.$

b) Ta có: $\int f (x)dx$ $= \int {\frac{{1 + \ln x}}{{3 + x\ln x}}} dx$ $= \int {\frac{{d(x\ln x)}}{{3 + x\ln x}}}$ $= \int {\frac{{d(3 + x\ln x)}}{{3 + x\ln x}}}$ $= \ln |3 + x\ln x| + C.$

**Dạng toán 2: Tìm nguyên hàm của hàm số mũ và logarit bằng phương pháp phân tích.

** Chúng ta đã được làm quen với phương pháp phân tích để tính các xác định nguyên hàm nói chung. Bây giờ đi xem xét chi tiết hơn về việc sử dụng phương pháp này để xác định nguyên hàm của các hàm số mũ và logarit. Cần hiểu rằng thực chất nó là một dạng của phương pháp hệ số bất định, nhưng ở đây ta sử dụng các đồng nhất thức quen thuộc.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 1: Tìm nguyên hàm của hàm số $f(x) = \frac{1}{{1 – {e^x}}}.$

Sử dụng đồng nhất thức: $1 = \left( {1 – {e^x}} \right) + {e^x}$, ta được:

$\frac{1}{{1 – {e^x}}}$ $= \frac{{\left( {1 – {e^x}} \right) + {e^x}}}{{1 – {e^x}}}$ $= 1 + \frac{{{e^x}}}{{1 – {e^x}}}.$

Suy ra: $\int f (x)dx$ $= \int {\left( {1 + \frac{{{e^x}}}{{1 – {e^x}}}} \right)} dx$ $= \int d x – \int {\frac{{d\left( {1 – {e^x}} \right)}}{{1 – {e^x}}}}$ $= x – \ln \left| {1 – {e^x}} \right| + C.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 2: Tìm nguyên hàm của hàm số $f(x) = {e^x}\sqrt {{e^{2x}} – 2{e^x} + 2} .$

Ta có: $\int f (x)dx$ $= \int {{e^x}} \sqrt {{{\left( {{e^x} – 1} \right)}^2} + 1} dx$ $= \int {\sqrt {{{\left( {{e^x} – 1} \right)}^2} + 1} } d\left( {{e^x} – 1} \right)$ $= \frac{{{e^x} – 1}}{2}\sqrt {{{\left( {{e^x} – 1} \right)}^2} + 1}$ $+ \frac{1}{2}\ln \left| {\left( {{e^x} – 1} \right) + \sqrt {{{\left( {{e^x} – 1} \right)}^2} + 1} } \right| + C$ $= \frac{{{e^x} – 1}}{2}\sqrt {{e^{2x}} – 2{e^x} + 2}$ $+ \frac{1}{2}\ln \left| {{e^x} – 1 + \sqrt {{e^{2x}} – 2{e^x} + 2} } \right| + C.$

Chú ý: Nếu các em học sinh thấy khó hình dùng một cách cặn kẽ cách biến đổi để đưa về dạng cơ bản trong bài toán trên thì thực hiện theo hai bước sau:

Bước 1: Thực hiện phép đổi biến $t = {e^x}$, suy ra:

$dt = {e^x}dx.$

${e^x}\sqrt {{e^{2x}} – 2{e^x} + 2} dx$ $= \sqrt {{t^2} – 2t + 2} dt$ $= \sqrt {{{(t – 1)}^2} + 1} dt.$

Khi đó: $\int f (x)dx = \int {\sqrt {{{(t – 1)}^2} + 1} } dt.$

Bước 2: Thực hiện phép đổi biến $u = t – 1$, suy ra:

$du = dt.$

$\sqrt {{{(t – 1)}^2} + 1} dt = \sqrt {{u^2} + 1} du.$

Khi đó: $\int f (x)dx$ $= \int {\sqrt {{u^2} + 1} } du$ $= \frac{u}{2}\sqrt {{u^2} + 1}$ $+ \frac{1}{2}\ln \left| {u + \sqrt {{u^2} + 1} } \right| + C$ $= \frac{{t – 1}}{2}\sqrt {{{(t – 1)}^2} + 1}$ $+ \frac{1}{2}\ln \left| {t – 1 + \sqrt {{{(t – 1)}^2} + 1} } \right| + C$ $= \frac{{{e^x} – 1}}{2}\sqrt {{e^{2x}} – 2{e^x} + 2}$ $+ \frac{1}{2}\ln \left| {{e^x} – 1 + \sqrt {{e^{2x}} – 2{e^x} + 2} } \right| + C.$

[ads]

<!-- chunk:5 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Dạng toán 3: Tìm nguyên hàm của hàm số mũ và logarit bằng phương pháp đổi biến.

Phương pháp đổi biến được sử dụng cho các hàm số mũ và logarit với mục đích chủ đạo để chuyển biểu thức dưới dấu tích phân về các dạng hữu tỉ hoặc vô tỉ, tuy nhiên trong nhiều trường hợp cần tiếp thu những kinh nghiệm nhỏ đã được trình bày bằng các chú ý.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 1: Tìm nguyên hàm của hàm số $f(x) = \frac{1}{{\sqrt {1 + {e^{2x}}} }}.$

Ta có thể lựa chọn các cách trình bày sau:

Cách 1: Ta có:

$\frac{{dx}}{{\sqrt {1 + {e^{2x}}} }}$ $= \frac{{dx}}{{{e^x}\sqrt {{e^{ – 2x}} + 1} }}$ $= \frac{{{e^{ – x}}dx}}{{\sqrt {{e^{ – 2x}} + 1} }}$ $= – \frac{{d\left( {{e^{ – x}}} \right)}}{{\sqrt {{e^{ – 2x}} + 1} }}.$

Khi đó:

$\int f (x)dx$ $= – \int {\frac{{d\left( {{e^{ – x}}} \right)}}{{\sqrt {{e^{ – 2x}} + 1} }}}$ $= – \ln \left( {{e^{ – x}} + \sqrt {{e^{ – 2x}} + 1} } \right) + C.$

Cách 2: Đặt $t = \sqrt {1 + {e^{2x}}}$, suy ra:

${t^2} = 1 + {e^{2x}}$ $\Rightarrow 2tdt = 2{e^{2x}}dx$ $\Leftrightarrow dx = \frac{{tdt}}{{{t^2} – 1}}.$

Khi đó:

$\int {f(x)} dx$ $= \int {\frac{{tdt}}{{t\left( {{t^2} – 1} \right)}}}$ $= \int {\frac{{dt}}{{{t^2} – 1}}}$ $= \frac{1}{2}\ln \left| {\frac{{t – 1}}{{t + 1}}} \right| + C$ $= \frac{1}{2}\ln \left| {\frac{{\sqrt {1 + {e^{2x}}} – 1}}{{\sqrt {1 + {e^{2x}}} + 1}}} \right| + C.$

Cách 3: Đặt $t = {e^x}$, suy ra $dt = {e^x}dx.$

Khi đó:

$\int {f(x)} dx$ $= \int {\frac{{dt}}{{t\sqrt {1 + {t^2}} }}}$ $= \int {\frac{{dt}}{{{t^2}\sqrt {\frac{1}{{{t^2}}} + 1} }}}$ $= – \int {\frac{{d\left( {\frac{1}{t}} \right)}}{{\sqrt {\frac{1}{{{t^2}}} + 1} }}}$ $= – \ln \left| {\frac{1}{t} + \sqrt {\frac{1}{{{t^2}}} + 1} } \right| + C$ $= – \ln \left( {{e^{ – x}} + \sqrt {{e^{ – 2x}} + 1} } \right) + C.$

Cách 4: Đặt $t = {e^{ – x}}$, suy ra:

$dt = – {e^{ – x}}dx$ $\Leftrightarrow – dt = \frac{{dx}}{{{e^x}}}.$

Khi đó:

$\int {f(x)} dx$ $= \int {\frac{{dx}}{{\sqrt {1 + {e^{2x}}} }}}$ $= \int {\frac{{dx}}{{\sqrt {{e^{2x}}\left( {{e^{ – 2x}} + 1} \right)} }}}$ $= \int {\frac{{dx}}{{{e^x}\sqrt {{e^{ – 2x}} + 1} }}}$ $= \int {\frac{{ – dt}}{{\sqrt {{t^2} + 1} }}}$ $= – \int {\frac{{dt}}{{\sqrt {{t^2} + 1} }}}$ $= – \ln \left| {t + \sqrt {{t^2} + 1} } \right| + C$ $= – \ln \left| {{e^{ – x}} + \sqrt {{e^{ – 2x}} + 1} } \right| + C.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 2: Tìm nguyên hàm của hàm số: $f(x) = \frac{1}{{{e^x} – 4{e^{ – x}}}}.$

Đặt ${e^x} = t$, suy ra ${e^x}dx = dt.$

Khi đó: $\int f (x)dx$ $= \int {\frac{{dx}}{{{e^x} – 4{e^{ – x}}}}}$ $= \int {\frac{{{e^x}dx}}{{{e^{2x}} – 4}}}$ $= \int {\frac{{dt}}{{{t^2} – 4}}}$ $= \ln \left| {\frac{{t – 2}}{{t + 2}}} \right| + C$ $= \ln \left| {\frac{{{e^x} – 2}}{{{e^x} + 2}}} \right| + C.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Dạng toán 4: Tìm nguyên hàm của hàm số mũ và logarit bằng phương pháp lấy nguyên hàm từng phần.
Chúng ta đã được biết trong phần xác định nguyên hàng bằng phương pháp nguyên hàm từng phần, đối với các dạng nguyên hàm:

<!-- chunk:9 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Dạng 1: Tính: $\int {{e^{ax}}} \cos (bx)$ hoặc $\int {{e^{ax}}} \sin (bx)$ với $a,b \ne 0.$

Khi đó ta đặt: 
$$
\left\{ {\begin{array}{l}
{u = \cos (bx)}\\
{dv = {e^{ax}}dx}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{u = \sin (bx)}\\
{dv = {e^{ax}}dx}
\end{array}} \right.
$$

Ngoài ra cũng có thể sử dụng phương pháp hằng số bất định.

<!-- chunk:10 level:2 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Dạng 2: Tính: $\int P (x){e^{\alpha x}}dx$ với $\alpha \in {R^*}.$

Khi đó ta đặt: 
$$
\left\{ {\begin{array}{l}
{u = P(x)}\\
{dv = {e^{\alpha x}}dx}
\end{array}} \right.
$$

Ngoài ra cũng có thể sử dụng phương pháp hằng số bất định.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 1: Tìm nguyên hàm $I = \int x \ln \frac{{1 – x}}{{1 + x}}dx.$

Đặt 
$$
\left\{ {\begin{array}{l}
{u = \ln \frac{{1 – x}}{{1 + x}}}\\
{dv = xdx}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{du = \frac{{ – 1}}{{1 – {x^2}}}dx}\\
{v = \frac{1}{2}{x^2}}
\end{array}} \right.
$$

Khi đó: $I = \frac{1}{2}{x^2}\ln \frac{{1 – x}}{{1 + x}}$ $+ \int {\frac{{{x^2}}}{{2\left( {1 – {x^2}} \right)}}} dx$ $= \frac{1}{2}{x^2}\ln \frac{{1 – x}}{{1 + x}}$ $+ \int {\left( {\frac{1}{{2\left( {1 – {x^2}} \right)}} – \frac{1}{2}} \right)} dx + C$ $= \frac{1}{2}{x^2}\ln \frac{{1 – x}}{{1 + x}}$ $+ \frac{1}{4}\ln \left| {\frac{{1 + x}}{{1 – x}}} \right| – \frac{1}{2}x + C.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/11/phuong-phap-tim-nguyen-ham-cua-cac-ham-so-mu-va-logarit.html -->
## Ví dụ 2: Tìm nguyên hàm của hàm số $f(x) = \left( {{{\tan }^2}x + \tan x + 1} \right){e^x}.$

Ta có: $\int f (x)dx$ $= \int {\left( {{{\tan }^2}x + \tan x + 1} \right)} {e^x}$ $= \int {\left( {{{\tan }^2}x + 1} \right)} {e^x} + \int {{e^x}} \tan xdx$ $(1).$

Xét tích phân $J = \int {{e^x}} \tan xdx$, đặt:

$$
\left\{ {\begin{array}{l}
{u = \tan x}\\
{dv = {e^x}dx}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{du = \frac{{dx}}{{{{\cos }^2}x}} = \left( {1 + {{\tan }^2}x} \right)dx}\\
{v = {e^x}}
\end{array}} \right.
$$

Khi đó: $J = {e^x}\tan x – \int {\left( {{{\tan }^2}x + 1} \right)} {e^x}$ $(2).$

Thay $(2)$ vào $(1)$ ta được: $\int f (x)dx = {e^x}\tan x + C.$