# Tính tích phân bằng phương pháp tích phân từng phần

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan.html -->
Bài viết hướng dẫn các bước tính tích phân bằng phương pháp tích phân từng phần, đồng thời nêu ra một số dạng toán thường gặp và kinh nghiệm đặt biến số thích hợp khi thực hiện tích phân từng phần.

Phương pháp tích phân từng phần:

Nếu $u(x)$ và $v(x)$ là các hàm số có đạo hàm liên tục trên $\left[ {a;b} \right]$ thì:

$\int\limits_a^b {u(x)v'(x)dx}$ 
$$
= \left( {u(x)v(x)} \right)\left| \begin{array}{l}
b\\
a
\end{array} \right. – \int\limits_a^b {v(x)u'(x)dx} .
$$

Hay: 
$$
\int\limits_a^b {udv = uv\left| \begin{array}{l}
b\\
a
\end{array} \right. – \int\limits_a^b {vdu} } .
$$

Áp dụng công thức trên ta có quy tắc tính $\int\limits_a^b {f(x)dx}$ bằng phương pháp tích phân từng phần như sau:

+ Bước 1: Viết $f(x)dx$ dưới dạng $udv = uv’dx$ bằng cách chọn một phần thích hợp của $f(x)$ làm $u(x)$ và phần còn lại $dv = v'(x)dx.$

+ Bước 2: Tính $du = u’dx$ và $v = \int {dv} = \int {v'(x)dx} .$

+ Bước 3: Tính $\int\limits_a^b {vdu} = \int\limits_a^b {vu’dx}$ và 
$$
uv\left| \begin{array}{l}
b\\
a
\end{array} \right. .
$$

+ Bước 4: Áp dụng công thức 
$$
\int\limits_a^b {f(x)dx} = \int\limits_a^b {udv = uv\left| \begin{array}{l}
b\\
a
\end{array} \right. – \int\limits_a^b {vdu} } .
$$

Cách đặt $u$ và $dv$ trong phương pháp tích phân từng phần

Điều quan trọng khi sử dụng công thức tích phân từng phần là làm thế nào để chọn $u$ và $dv = v’dx$ thích hợp trong biểu thức dưới dấu tích phân $f(x)dx$. Nói chung nên chọn $u$ là phần của $f(x)$ mà khi lấy đạo hàm thì đơn giản, chọn $dv = v’dx$ là phần của $f(x)dx$ là vi phân một hàm số đã biết hoặc có nguyên hàm dễ tìm.

<img link="data_for_rag/toan12/images/tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan-1.png" alt="tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan-1">

+ Nếu tính tích phân $\int\limits_\alpha ^\beta {P(x)Q(x)dx}$ mà $P(x)$ là đa thức chứa $x$ và $Q(x)$ là một trong những hàm số: ${e^{ax}}$, $\sin ax$, $\cos ax$ thì ta thường đặt:

$$
\left\{ \begin{array}{l}
u = P(x)\\
dv = Q(x)dx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = P'(x)dx\\
v = \int {Q(x)dx}
\end{array} \right.
$$

+ Nếu tính tích phân $\int\limits_\alpha ^\beta {P(x)Q(x)dx}$ mà $P(x)$ là đa thức của $x$ và $Q(x)$ là hàm số $ln(ax)$ thì ta đặt: 
$$
\left\{ \begin{array}{l}
u = Q(x)\\
dv = P(x)dx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = Q’\left( x \right)dx\\
v = \int {P(x)dx}
\end{array} \right.
$$

+ Nếu tính tích phân $J = \int\limits_\alpha ^\beta {{e^{ax}}\sin bxdx}$ thì ta đặt 
$$
\left\{ \begin{array}{l}
u = {e^{ax}}\\
dv = \sin bxdx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = a{e^{ax}}dx\\
v = – \frac{1}{b}\cos bx
\end{array} \right.
$$

Tương tự với tích phân $I = \int\limits_\alpha ^\beta {{e^{ax}}\cos bxdx}$, ta đặt 
$$
\left\{ \begin{array}{l}
u = {e^{ax}}\\
dv = \cos bxdx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = a{e^{ax}}dx\\
v = \frac{1}{b}\sin bx
\end{array} \right.
$$

Trong trường hợp này, ta phải tính tích phân từng phần hai lần sau đó trở thành tích phân ban đầu. Từ đó suy ra kết quả tích phân cần tính.

[ads]

Ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan.html -->
## Ví dụ 1: Tính các tích phân sau:

a. $\int\limits_1^2 {\frac{{\ln x}}{{{x^5}}}dx} .$

b. $\int\limits_0^{\frac{\pi }{2}} {x\cos xdx} .$

c. $\int\limits_0^1 {x{e^x}dx} .$

d. $\int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx} .$

a. Đặt 
$$
\left\{ \begin{array}{l}
u = \ln x\\
dv = \frac{1}{{{x^5}}}dx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = \frac{{dx}}{x}\\
v = – \frac{1}{{4{x^4}}}
\end{array} \right.
$$

Do đó: $\int\limits_1^2 {\frac{{\ln x}}{{{x^5}}}dx}$ $= \left. { – \frac{{\ln x}}{{4{x^4}}}} \right|_1^2 + \frac{1}{4}\int\limits_1^2 {\frac{{dx}}{{{x^5}}}}$ $= – \frac{{\ln 2}}{{64}} + \left. {\frac{1}{4}\left( { – \frac{1}{{4{x^4}}}} \right)} \right|_1^2$ $= \frac{{15 – 4\ln 2}}{{256}}.$

b. Đặt 
$$
\left\{ \begin{array}{l}
u = x\\
dv = \cos xdx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = dx\\
v = \sin x
\end{array} \right.
$$

Do đó: $\int\limits_0^{\frac{\pi }{2}} {x\cos xdx}$ 
$$
= \left( {x\sin x} \right)\left| \begin{array}{l}
\frac{\pi }{2}\\
0
\end{array} \right. – \int\limits_0^{\frac{\pi }{2}} {\sin xdx}
$$
 
$$
= \frac{\pi }{2} + \cos x\left| \begin{array}{l}
\frac{\pi }{2}\\
0
\end{array} \right. = \frac{\pi }{2} – 1.
$$

c. Đặt 
$$
\left\{ \begin{array}{l}
u = x\\
dv = {e^x}dx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = dx\\
v = {e^x}
\end{array} \right.
$$

Do đó: $\int\limits_0^1 {x{e^x}dx}$ 
$$
= x{e^x}\left| \begin{array}{l}
1\\
0
\end{array} \right. – \int\limits_0^1 {{e^x}dx}
$$
 
$$
= e – {e^x}\left| \begin{array}{l}
1\\
0
\end{array} \right.
$$
 $= e – \left( {e – 1} \right) = 1.$

d. Đặt 
$$
\left\{ \begin{array}{l}
u = {e^x}\\
dv = \cos xdx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = {e^x}dx\\
v = \sin x
\end{array} \right.
$$
 $\Rightarrow \int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx}$ 
$$
= {e^x}\sin x\left| \begin{array}{l}
\frac{\pi }{2}\\
0
\end{array} \right. – \int\limits_0^{\frac{\pi }{2}} {{e^x}\sin xdx} .
$$

Đặt 
$$
\left\{ \begin{array}{l}
{u_1} = {e^x}\\
d{v_1} = \sin xdx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
d{u_1} = {e^x}dx\\
{v_1} = – \cos x
\end{array} \right.
$$

$\Rightarrow \int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx}$ 
$$
= {e^{\frac{\pi }{2}}} + {e^x}\cos x\left| \begin{array}{l}
\frac{\pi }{2}\\
0
\end{array} \right. – \int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx}
$$

$\Leftrightarrow 2\int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx}$ $= {e^{\frac{\pi }{2}}} – 1$ $\Leftrightarrow \int\limits_0^{\frac{\pi }{2}} {{e^x}\cos xdx} = \frac{{{e^{\frac{\pi }{2}}} – 1}}{2}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan.html -->
## Ví dụ 2: Tính các tích phân sau:

a. $I = \int\limits_1^3 {\frac{{3 + \ln x}}{{{{(x + 1)}^2}}}dx} .$

b. $J = \int\limits_{ – 1}^0 {(2{x^2} + x + 1)\ln (x + 2)dx} .$

a. Đặt 
$$
\left\{ \begin{array}{l}
u = 3 + \ln x\\
dv = \frac{{dx}}{{{{(x + 1)}^2}}}
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = \frac{{dx}}{x}\\
v = \frac{{ – 1}}{{x + 1}}
\end{array} \right.
$$

$I = – \left. {\frac{{3 + \ln x}}{{x + 1}}{\rm{ }}} \right|_1^3 + \int\limits_1^3 {\frac{{dx}}{{x(x + 1)}}}$ $= – \frac{{3 + \ln 3}}{4} + \frac{3}{2} + \left. {\ln \left| {\frac{x}{{x + 1}}} \right|} \right|_1^3$ $= \frac{{3 – \ln 3}}{4} + \ln \frac{3}{2}.$

b. Đặt 
$$
\left\{ \begin{array}{l}
u = \ln (x + 2)\\
dv = (2{x^2} + x + 1)dx
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
du = \frac{1}{{x + 2}}dx\\
v = \frac{2}{3}{x^3} + \frac{1}{2}{x^2} + x
\end{array} \right.
$$

$J = (\frac{2}{3}{x^3} + \frac{1}{2}{x^2} + x)\ln (x + 2)\left| {_{ – 1}^0} \right.$ $– \frac{1}{6}\int\limits_{ – 1}^0 {\frac{{4{x^3} + 3{x^2} + 6x}}{{x + 2}}dx}$

$= – \frac{1}{6}\int\limits_{ – 1}^0 {(4{x^2} – 5x + 16 – \frac{{32}}{{x + 2}})dx}$ $= – \frac{1}{6}\left. {\left[ {\frac{4}{3}{x^3} – \frac{5}{2}{x^2} + 16x – 32\ln (x + 2)} \right]} \right|_{ – 1}^0$

$= \frac{{16}}{3}\ln 2 – \frac{{119}}{{36}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/tinh-tich-phan-bang-phuong-phap-tich-phan-tung-phan.html -->
## Ví dụ 3: Tính tích phân sau: $I = \int\limits_0^{e – 1} {x\ln (x + 1)dx} .$

Đặt 
$$
\left\{ \begin{array}{l}
u = \ln (x + 1)\\
dv = xdx
\end{array} \right.
$$
 ta có 
$$
\left\{ \begin{array}{l}
du = \frac{1}{{x + 1}}dx\\
v = \frac{{{x^2} – 1}}{2}
\end{array} \right.
$$

Suy ra: $I = \int\limits_0^{e – 1} {x\ln (x + 1)dx}$ $= \left. {\left[ {\ln (x + 1)\frac{{{x^2} – 1}}{2}} \right]} \right|_0^{e – 1}$ $– \frac{1}{2}\int\limits_0^{e – 1} {(x – 1)dx}$ $= \frac{{{e^2} – 2e}}{2} – \frac{1}{2}\left( {\frac{{{x^2}}}{2} – x} \right)\left| {_0^{e – 1}} \right.$ $= \frac{{{e^2} – 3}}{4}.$

Chú ý: Trong ví dụ này, ta chọn $v = \frac{{{x^2} – 1}}{2}$ thay vì $v = \frac{{{x^2}}}{2}$ để việc tính tích phân $\int\limits_0^{e – 1} {vdu}$ dễ dàng hơn, như vậy bạn đọc có thể chọn $v$ một cách khéo léo để lời giải được ngắn gọn.