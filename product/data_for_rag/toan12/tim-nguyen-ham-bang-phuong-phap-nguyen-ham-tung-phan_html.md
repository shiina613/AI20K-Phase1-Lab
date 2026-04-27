# Tìm nguyên hàm bằng phương pháp nguyên hàm từng phần

<!-- chunk:0 level:0 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
Bài viết hướng dẫn các bước tìm nguyên hàm bằng phương pháp nguyên hàm từng phần, đồng thời nêu ra một số dạng toán thường gặp và kinh nghiệm đặt biến số thích hợp khi thực hiện nguyên hàm từng phần.

Lý do sử dụng phương pháp nguyên hàm từng phần: Đôi khi ta gặp phải những nguyên hàm mà không thể sử dụng hai phương phương pháp: phân tích và đối biến số để tìm nguyên hàm trực tiếp được, vì thế ta phải thông qua việc tìm nguyên hàm bằng một hàm số khác (mà có thể sử dụng hai phương pháp đã biết để tìm nguyên hàm).

CÔNG THỨC: $\int {udv = uv – \int {vdu} } .$

CÁC DẠNG TOÁN THƯỜNG GẶP

<!-- chunk:1 level:2 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Bài toán 1: Sử dụng công thức nguyên hàm từng phần để tính $I = \int {f(x)dx}$
Ta thực hiện theo các bước sau:

+ Bước 1: Ta biến đổi nguyên hàm ban đầu về dạng: $I = \int {f(x)dx = \int {{f_1}(x).{f_2}(x)dx} } .$

+ Bước 2: Đặt 
$$
\left\{ \begin{array}{l}
u = {f_1}(x)\\
dv = {f_2}(x)dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = {f’_1}(x)dx\\
v = \int {{f_2}(x)dx}
\end{array} \right.
$$

+ Bước 3: Khi đó: $\int {u.dv = u.v – \int {v.du} } .$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 1: Tìm nguyên hàm: $I = \int {\frac{{x.\ln \left( {x + \sqrt {{x^2} + 1} } \right)}}{{\sqrt {{x^2} + 1} }}} dx.$

Viết lại: $I = \int {\ln \left( {x + \sqrt {{x^2} + 1} } \right).\frac{{xdx}}{{\sqrt {{x^2} + 1} }}} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = \ln \left( {x + \sqrt {{x^2} + 1} } \right)\\
dv = \frac{{xdx}}{{\sqrt {{x^2} + 1} }}
\end{array} \right.
$$
 $\to$ 
$$
\left\{ \begin{array}{l}
du = \frac{{\frac{{1 + x}}{{\sqrt {{x^2} + 1} }}}}{{x + \sqrt {{x^2} + 1} }} = \frac{{dx}}{{\sqrt {{x^2} + 1} }}\\
v = \sqrt {{x^2} + 1}
\end{array} \right.
$$

Khi đó: $I = \int {u.dv}$ $= {\sqrt {{x^2} + 1} \ln \left( {x + \sqrt {{x^2} + 1} } \right) – \int {dx} }$

${ = \sqrt {{x^2} + 1} \ln \left( {x + \sqrt {{x^2} + 1} } \right) – x + C}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 2: Tìm nguyên hàm $I = \int {\frac{{\ln \left( {c{\rm{osx}}} \right)}}{{c{\rm{o}}{{\rm{s}}^{\rm{2}}}x}}dx} .$

Ta viết lại: $I = \int {\ln \left( {c{\rm{osx}}} \right).\frac{{dx}}{{c{\rm{o}}{{\rm{s}}^{\rm{2}}}x}}} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = \ln \left( {c{\rm{osx}}} \right)\\
dv = \frac{{dx}}{{c{\rm{o}}{{\rm{s}}^{\rm{2}}}x}}
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = – \frac{{{\mathop{\rm s}\nolimits} {\rm{inx}}}}{{{\rm{cosx}}}} = – {\mathop{\rm t}\nolimits} {\rm{anx}}\\
{\rm{v = }}\int {\frac{{dx}}{{c{\rm{o}}{{\rm{s}}^{\rm{2}}}x}} = {\mathop{\rm t}\nolimits} {\rm{anx}}}
\end{array} \right.
$$

$\Rightarrow I = \int {u.dv }$ $= {\mathop{\rm t}\nolimits} {\rm{anx}}{\rm{.ln}}\left( {{\rm{cosx}}} \right) + \int {{{\tan }^2}xdx} .$

Khi đó: $I = {\mathop{\rm t}\nolimits} {\rm{anx}}{\rm{.ln}}\left( {{\rm{cosx}}} \right) + \int {\left( {\frac{1}{{c{\rm{o}}{{\rm{s}}^{\rm{2}}}x}} – 1} \right)dx}$ ${ = {\mathop{\rm t}\nolimits} {\rm{anx}}{\rm{.ln}}\left( {{\rm{cosx}}} \right) + {\mathop{\rm t}\nolimits} {\rm{anx – x + C}}}.$

<!-- chunk:4 level:2 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Bài toán 2: Tìm nguyên hàm dạng
$$
\left[ \begin{array}{l}
I = \int {P(x)\sin axdx} \\
I = \int {P(x)c{\rm{osaxdx}}}
\end{array} \right.
$$
 với $P(x)$ là một đa thức
Ta lựa chọn một trong hai cách sau:

* Cách 1: Sử dụng nguyên hàm từng phần, thực hiện theo các bước sau:

+ Bước 1: Đặt: 
$$
\left\{ \begin{array}{l}
u = P(x)\\
dv = \left[ \begin{array}{l}
{\mathop{\rm s}\nolimits} {\rm{inaxdx}}\\
{\rm{cosaxdx}}
\end{array} \right.
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = P'(x)dx\\
v = \left[ \begin{array}{l}
\frac{{ – 1}}{a}c{\rm{osax}}\\
\frac{{\rm{1}}}{{\rm{a}}}\sin ax
\end{array} \right.
\end{array} \right.
$$

+ Bước 2: Thay vào công thức nguyên hàm từng phần.

+ Bước 3: Tiếp tục thủ tục như trên ta sẽ khử được bậc của đa thức.

* Cách 2: Sử dụng phương pháp hệ số bất định, thực hiện theo các bước sau:

+ Bước 1: Ta có: $I = \int {P(x)c{\rm{osaxdx}}}$ ${{\rm{ = A(x)sinax + B(x)cosax + C}}}$ $(1)$, trong đó $A(x)$ và $B(x)$ là các đa thức cùng bậc với $P(x).$

+ Bước 2: Lấy đạo hàm hai vế của $(1)$: $P(x)c{\rm{osax}}$ ${\rm{ = A'(x)cosax – A(x)a}}{\rm{.sinax}}$ ${\rm{ + B'(x)sinax + aB(x)cosax}}.$

+ Bước 3: Sử dụng phương pháp hệ số bất định ta xác định được $A(x)$ và $B(x).$

Nhận xét: Nếu bậc của đa thức lớn hơn $3$ thì cách 1 tỏ ra cồng kềnh, vì khi đó ta thực hiện số lần nguyên hàm từng phần bằng với số bậc của đa thức, cho nên ta đi đến nhận định như sau:

+ Nếu bậc của đa thức nhỏ hơn hoặc bằng $2$: Ta sử dụng cách 1.

+ Nếu bậc của đa thức lớn hơn hoặc bằng $3$: Ta sử dụng cách 2.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 3: Tìm nguyên hàm $\int {x{{\sin }^2}xdx} .$

Ta có: $I = \int {x\left( {\frac{{1 – c{\rm{os2x}}}}{2}} \right)dx}$ ${ = \frac{1}{2}\int {xdx} – \frac{1}{2}\int {x\cos 2xdx} }$ ${ = \frac{1}{4}{x^2} – \frac{1}{2}J}$ $(1).$

Tính: $J = \int {x\cos 2xdx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = x\\
dv = c{\rm{os2xdx}}
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = dx\\
v = \frac{1}{2}\sin 2x
\end{array} \right.
$$
 $\Rightarrow J = \frac{x}{2}\sin 2x – \frac{1}{2}\int {\sin 2xdx}$ ${ = \frac{x}{2}\sin 2x + \frac{1}{4}c{\rm{os2x + C}}}.$

Thay vào $(1)$: $I = \frac{1}{4}{x^2} – \frac{1}{2}\left( {\frac{x}{2}\sin 2x + \frac{1}{4}c{\rm{os2x}}} \right)$ $= \frac{1}{4}\left( {{x^2} – x\sin 2x – \frac{1}{2}c{\rm{os2x}}} \right) + C.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 4: Tìm nguyên hàm $I = \int {\left( {{x^3} – {x^2} + 2x – 3} \right){\mathop{\rm s}\nolimits} {\rm{inx}}dx} .$

Theo nhận xét trên, ta sử dụng phương pháp hệ số bất định. Ta có:

$I = \int {\left( {{x^3} – {x^2} + 2x – 3} \right){\mathop{\rm s}\nolimits} {\rm{inx}}dx}$ $= \left( {{a_1}{x^3} + {b_1}{x^2} + {c_1}x + {d_1}} \right)c{\rm{osx}}$ ${\rm{ + }}\left( {{a_2}{x^3} + {b_2}{x^2} + {c_2}x + {d_2}} \right){\mathop{\rm s}\nolimits} {\rm{inx}}$ $(1).$

Lấy đạo hàm hai vế của $(1)$:

$\Leftrightarrow \left( {{x^3} – {x^2} + 2x – 3} \right){\mathop{\rm s}\nolimits} {\rm{inx}}$ ${\rm{ = [}}{{\rm{a}}_{\rm{2}}}{x^3} + \left( {3{a_1} + {b_2}} \right){x^2}$ $+ \left( {2{b_1} + {c_2}} \right)x + {c_1} + {d_2}{\rm{]cosx}}$

$– [{{\rm{a}}_{\rm{1}}}{x^3} – \left( {3{a_2} – {b_1}} \right){x^2}$ $– \left( {2{b_2} – {c_1}} \right)x + {c_2} – {d_1}]\sin x$ $(2).$

Đồng nhất thức ta được: 
$$
\left\{ \begin{array}{l}
{a_2} = 0\\
3{a_1} + {b_2} = 0\\
2{b_1} + {c_2} = 0\\
{c_1} + {d_2} = 0
\end{array} \right.
$$
 và 
$$
\left\{ \begin{array}{l}
– {a_1} = 1\\
3{a_2} – {b_1} = – 1\\
2{b_2} – {c_1} = 2\\
– {c_2} + {d_1} = – 3
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
{a_1} = – 1;{a_2} = 0\\
{b_1} = 1;{b_2} = 3\\
{c_1} = 4;{c_2} = – 2\\
{d_1} = 1;{d_2} = – 4
\end{array} \right.
$$

Khi đó: $I = \left( { – {x^3} + {x^2} + 4x + 1} \right)c{\rm{osx}}$ ${\rm{ + }}\left( {{\rm{3}}{{\rm{x}}^{\rm{2}}} – 2x + 4} \right){\mathop{\rm s}\nolimits} {\rm{inx + C}}.$

Ngoài ra ta có thể bài toán trên bằng cách lấy nguyên hàm từng phần ba lần.

[ads]

<!-- chunk:7 level:2 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Bài toán 3: Tìm nguyên hàm dạng
$$
\left[ \begin{array}{l}
I = \int {{e^{{\rm{ax}}}}\sin bxdx} \\
I = \int {{e^{{\rm{ax}}}}c{\rm{osbxdx}}}
\end{array} \right.
$$
 với $a, b ≠ 0$
Sử dụng phương pháp nguyên hàm từng phần, theo các bước sau:

+ Bước 1: Đặt 
$$
\left[ \begin{array}{l}
\left\{ \begin{array}{l}
u = c{\rm{osbx}}\\
{\rm{dv = }}{{\rm{e}}^{{\rm{ax}}}}dx
\end{array} \right.\\
\left\{ \begin{array}{l}
u = \sin bx\\
dv = {e^{{\rm{ax}}}}dx
\end{array} \right.
\end{array} \right.
$$
 
$$
\Rightarrow \left[ \begin{array}{l}
\left\{ \begin{array}{l}
du = – b\sin {\rm{bxdx}}\\
{\rm{v = }}\frac{{\rm{1}}}{{\rm{a}}}{{\rm{e}}^{{\rm{ax}}}}
\end{array} \right.\\
\left\{ \begin{array}{l}
du = b\cos {\rm{b}}xdx\\
v = \frac{1}{a}{e^{{\rm{ax}}}}
\end{array} \right.
\end{array} \right.
$$

+ Bước 2: Thay vào công thức nguyên hàm từng phần.

Chú ý: Riêng đối với dạng nguyên hàm này bao giờ cũng phải lấy nguyên hàm từng phần hai lần.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 5: Tìm nguyên hàm $I = \int {{e^{2x}}{{\sin }^2}xdx} .$

Ta có: $I = \int {{e^{2x}}{{\sin }^2}xdx}$ $= \int {{e^{2x}}\left( {\frac{{1 – c{\rm{os2x}}}}{2}} \right)dx}$ ${ = \frac{1}{2}\int {{e^{2x}}dx – \frac{1}{2}\int {{e^{2x}}c{\rm{os2xdx}}} } }$ ${ = \frac{1}{4}{e^{2x}} – \frac{1}{2}J}$ $(1).$

Tìm nguyên hàm: $J = \int {{e^{2x}}c{\rm{os2xdx}}} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = c{\rm{os2x}}\\
{\rm{dv = }}{{\rm{e}}^{{\rm{2x}}}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = – 2\sin 2xdx\\
v = \frac{1}{2}{e^{2x}}
\end{array} \right.
$$
 $\Rightarrow J = \frac{1}{2}{e^{2x}}c{\rm{os2x + }}\int {{e^{2x}}\sin 2xdx}$ $= \frac{1}{2}{e^{2x}}c{\rm{os2x + K}}$ $(2).$

Tìm nguyên hàm: $K = \int {{e^{2x}}\sin 2xdx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
{u_1} = \sin 2x\\
d{v_1} = {e^{2x}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
d{u_1} = 2\cos 2xdx\\
{v_1} = \frac{1}{2}{e^{2x}}
\end{array} \right.
$$
 $\Rightarrow K = \frac{1}{2}{e^{2x}}\sin 2x – \int {{e^{2x}}c{\rm{os2xdx}}}$ $= \frac{1}{2}{e^{2x}}\sin 2x – J$ $(3).$

Từ $(2)$ và $(3)$ ta có hệ: 
$$
\left\{ \begin{array}{l}
J – K = \frac{1}{2}{e^{2x}}c{\rm{os2x}}\\
J + K = \frac{1}{2}{e^{2x}}\sin {\rm{2x}}
\end{array} \right.
$$
 $\leftrightarrow J = \frac{1}{4}{e^{2x}}\left( {\sin 2x + c{\rm{os2x}}} \right).$

Thay vào $(1)$ ta được: $I = \frac{1}{4}{e^{2x}} – \frac{1}{2}.\frac{1}{4}{e^{2x}}\left( {\sin 2x + c{\rm{os2x}}} \right)$ $= \frac{1}{4}{e^{2x}}\left( {1 – \frac{1}{2}\left( {\sin 2x + c{\rm{os2x}}} \right)} \right) + C.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Bài toán 4: Tìm nguyên hàm dạng $I = \int {P(x){e^{{\rm{ax}}}}dx}$
Sử dụng phương pháp nguyên hàm từng phần.Ta tiến hành theo các bước sau:

+ Bước 1: Đặt 
$$
\left\{ \begin{array}{l}
u = P(x)\\
dv = {e^{{\rm{ax}}}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = P'(x)dx\\
v = \frac{1}{a}{e^{{\rm{ax}}}}
\end{array} \right.
$$

+ Bước 2: Khi đó: $I = \frac{1}{a}{e^{{\rm{ax}}}}P(x) – \frac{1}{a}\int {P'(x){e^{{\rm{ax}}}}dx}$.

+ Bước 3: Tiếp tục thủ tục như trên ta sẽ khử được đa thức.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 6: Tìm nguyên hàm: $I = \int {x{e^{3x}}dx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = x\\
dv = {e^{3x}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = dx\\
v = \frac{1}{3}{e^{3x}}
\end{array} \right.
$$
 $\Rightarrow I = \frac{1}{3}x{e^{3x}} – \frac{1}{3}\int {{e^{3x}}dx }$ $= \frac{1}{3}x{e^{3x}} – \frac{1}{9}{e^{3x}} + C.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 7: Tìm nguyên hàm: $I = \int {{x^2}{e^{2x}}dx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = {x^2}\\
dv = {e^{2x}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = 2xdx\\
v = \frac{1}{2}{e^{2x}}
\end{array} \right.
$$
 $\Rightarrow I = \frac{1}{2}{x^2}{e^{2x}} – \int {x.{e^{2x}}dx\quad }$ ${ = \frac{1}{2}{x^2}{e^{2x}} – J}$ $(1).$

Tìm nguyên hàm $J = \int {x{e^{2x}}dx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
{u_1} = x\\
d{v_1} = {e^{2x}}dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
d{u_1} = dx\\
{v_1} = \frac{1}{2}{e^{2x}}
\end{array} \right.
$$
 $\Rightarrow J = \frac{1}{2}x{e^{2x}} – \frac{1}{2}\int {{e^{2x}}dx}$ $= \frac{1}{2}x{e^{2x}} – \frac{1}{4}{e^{2x}}.$

Thay vào $(1)$ ta được: $I = \frac{1}{2}{x^2}{e^{2x}} – \left( {\frac{1}{2}x{e^{2x}} – \frac{1}{4}{e^{2x}}} \right) + C$ $= \frac{1}{4}{e^{2x}}\left( {2{x^2} – 2x + 1} \right) + C.$

Chú ý: Qua hai ví dụ 6 và 7 ta thấy số lần lấy nguyên hàm từng phần bằng với số bậc của đa thức $P(x).$ Nghĩa là: số bậc của $P(x)$ càng cao thì số lần lấy nguyên hàm từng phần càng nhiều.

<!-- chunk:12 level:2 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Bài toán 5: Tìm nguyên hàm dạng $I = \int {P(x)\ln xdx}$
Ta lấy nguyên hàm từng phần, theo các bước sau:

+ Bước 1: Đặt: 
$$
\left\{ \begin{array}{l}
u = \ln x\\
dv = P(x)dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = \frac{{dx}}{x}\\
v = \int {P(x)dx}
\end{array} \right.
$$

+ Bước 2: Thay vào công thức nguyên hàm từng phần, ta được một nguyên hàm quen thuộc mà có thể tính được bằng hai phương pháp đã biết: phân tích và đổi biến số.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/05/tim-nguyen-ham-bang-phuong-phap-nguyen-ham-tung-phan.html -->
## Ví dụ 8: Tìm nguyên hàm: $I = \int {\left( {{x^2} – 2x} \right)\ln xdx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = \ln x\\
dv = \left( {{x^2} – 2x} \right)dx
\end{array} \right.
$$
 
$$
\to \left\{ \begin{array}{l}
du = \frac{{dx}}{x}\\
v = \frac{1}{3}{x^3} – {x^2}
\end{array} \right.
$$

Suy ra:

$I = \left( {\frac{1}{3}{x^3} – {x^2}} \right)\ln x$ $– \int {\left( {\frac{1}{3}{x^3} – {x^2}} \right)\frac{{dx}}{x} }$ $= \left( {\frac{1}{3}{x^3} – {x^2}} \right)\ln x$ $– \left[ {\frac{1}{3}\int {{x^2}dx} – \int {xdx} } \right].$

$I = \left( {\frac{1}{3}{x^3} – {x^2}} \right)\ln x$ $– \frac{1}{9}{x^3} + \frac{1}{2}{x^2} + C.$