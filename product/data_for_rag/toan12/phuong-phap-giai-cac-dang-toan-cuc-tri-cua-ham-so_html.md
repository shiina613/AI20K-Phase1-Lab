# Phương pháp giải các dạng toán cực trị của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
Bài viết trình bày tóm tắt lý thuyết sách giáo khoa và hướng dẫn phương pháp giải các dạng toán cực trị của hàm số trong chương trình Giải tích 12 chương 1.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## I. KHÁI NIỆM CỰC TRỊ CỦA HÀM SỐ

Định nghĩa: Giả sử hàm số $f$ xác định trên tập hợp $D$ $(D \subset R)$ và ${x_0} \in D.$

a) ${x_0}$ được gọi là điểm cực đại của hàm số $f$ nếu tồn tại khoảng $(a;b)$ có chứa điểm ${x_0}$ sao cho $(a;b) \subset D$ và $f(x) < f\left( {{x_0}} \right)$ với mọi $x \in (a;b)\backslash \left\{ {{x_0}} \right\}.$

Khi đó $f\left( {{x_0}} \right)$ được gọi là giá trị cực đại của hàm số $f.$

b) ${x_0}$ được gọi là điểm cực tiểu của hàm số $f$ nếu tồn tại khoảng $(a;b)$ có chứa điểm ${x_0}$ sao cho $(a;b) \subset D$ và $f(x) > f\left( {{x_0}} \right)$ với mọi $x \in (a;b)\backslash \{ {x_0}\} .$

Khi đó $f\left( {{x_0}} \right)$ được gọi là giá trị cực tiểu của hàm số $f.$

Điểm cực đại và điểm cực tiểu được gọi chung là điểm cực trị.

Giá trị cực đại và giá trị cực tiểu được gọi chung là giá trị cực trị.

Nếu ${x_0}$ là một điểm cực trị của hàm số $f$ thì ta nói hàm số $f$ đạt cực trị tại ${x_0}.$

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-1.png" alt="">

Chú ý:

a) Giá trị cực đại (cực tiểu) $f\left( {{x_0}} \right)$ của hàm số $f$ nói chung không phải là GTLN (GTNN) của hàm số $f$ trên tập xác định $D.$

b) Một hàm số $f$ có thể đạt cực trị tại nhiều điểm trên tập xác định $D$ và các cực trị nói chung là khác nhau. Hàm số $f$ cũng có thể không có cực trị trên một tập hợp cho trước.

c) Nếu ${x_0}$ là một điểm cực trị của hàm số $f$ thì điểm $M\left( {{x_0};f\left( {{x_0}} \right)} \right)$ được gọi là điểm cực trị của đồ thị hàm số $f.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## II. ĐIỀU KIỆN CẦN ĐỂ HÀM SỐ ĐẠT CỰC TRỊ

Định lý 1:

Cho hàm số $f$ đạt cực trị tại ${x_0}$.

Khi đó: Nếu $f$ có đạo hàm tại điểm ${x_0}$ thì $f’\left( {{x_0}} \right) = 0.$

Chú ý:

Từ định lí trên ta suy ra: Hàm số chỉ có thể đạt cực trị tại các điểm ${x_0} \in D$ mà tại ${x_0}$ hàm số có đạo hàm bằng $0$ hoặc hàm số không có đạo hàm.

Chiều ngược lại của định lí 1 có thể không đúng.

Chẳng hạn:

+ Có những hàm số có đạo hàm bằng $0$ tại ${x_0}$ nhưng tại ${x_0}$ hàm số không đạt cực trị.

+ Có những hàm số $f$ đạt cực trị tại một điểm mà tại điểm đó hàm số không có đạo hàm.

<!-- chunk:3 level:1 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## III. ĐIỀU KIỆN ĐỦ ĐỂ HÀM SỐ ĐẠT CỰC TRỊ

Định lý 2:

Cho hàm số $f$ liên tục trên khoảng $(a;b)$ chứa điểm ${x_0}$ và có đạo hàm trên các khoảng $\left( {a;{x_0}} \right)$ và $\left( {{x_0};b} \right).$ Khi đó:

a) Nếu $f'(x) < 0$ với mọi $x \in \left( {a;{x_0}} \right)$ và $f'(x) > 0$ với mọi $x \in \left( {{x_0};b} \right)$ thì hàm số $f$ đạt cực tiểu tại điểm ${x_0}.$

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-2.png" alt="">

b) Nếu $f'(x) > 0$ với mọi $x \in \left( {a;{x_0}} \right)$ và $f'(x) < 0$ với mọi $x \in \left( {{x_0};b} \right)$ thì hàm số $f$ đạt cực đại tại điểm ${x_0}.$

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-3.png" alt="">

Từ định lí 2 ta có quy tắc tìm cực trị sau:

Quy tắc 1:

1) Tìm $f'(x).$

2) Tìm các điểm ${x_i}$ $(i = 1,2, \ldots )$ mà tại đó $f’\left( {{x_i}} \right) = 0$ hoặc tại đó hàm số $f$ liên tục nhưng không có đạo hàm.

3) Lập bảng biến thiên. Từ đó suy ra cực trị của hàm số.

Định lý 3:

Cho hàm số $f$ có đạo hàm cấp một trên khoảng $(a;b)$ chứa điểm ${x_0}$, $f’\left( {{x_0}} \right) = 0$ và $f$ có đạo hàm cấp hai khác $0$ tại điểm ${x_0}.$

a) Nếu $f”\left( {{x_0}} \right) < 0$ thì hàm số $f$ đạt cực đại tại điểm ${x_0}.$

b) Nếu $f”\left( {{x_0}} \right) > 0$ thì hàm số $f$ đạt cực tiểu tại điểm ${x_0}.$

Từ định lý 3 ta có quy tắc 2 để tìm cực trị sau:

Quy tắc 2:

1) Tìm $f'(x).$

2) Tìm các nghiệm ${x_i}$ $(i = 1,2, \ldots )$ của phương trình $f'(x) = 0.$

3) Tìm $f”(x)$ và tính $f”({x_i}).$

+ Nếu $f”\left( {{x_i}} \right) < 0$ thì hàm số $f$ đạt cực đại tại ${x_i}.$

+ Nếu $f”\left( {{x_i}} \right) > 0$ thì hàm số $f$ đạt cực tiểu tại ${x_i}.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Vấn đề 1: Tìm cực trị của hàm số theo quy tắc 1.

1. PHƯƠNG PHÁP:

1) Tìm tập xác định, tính $f'(x).$

2) Giải phương trình $y’ = 0$, tìm các nghiệm ${x_i}$ $(i = 1,2, \ldots ).$ Tìm các điểm tại đó hàm số $f$ liên tục nhưng không có đạo hàm.

3) Lập bảng biến thiên. Từ đó suy ra cực trị của hàm số.

2. CÁC VÍ DỤ:

<!-- chunk:5 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 1: Tìm các điểm cực trị của các hàm số sau:

a) $y = 2{x^3} – 3{x^2} – 72x + 8.$

b) $y = \frac{{{x^2} – 2x + 9}}{{x – 2}}.$

c) $y = 2x – \left| {{x^2} – 1} \right|.$

a) $y = 2{x^3} – 3{x^2} – 72x + 8.$

Tập xác định: $D = R.$

$y’ = 6{x^2} – 6x – 72 = 6\left( {{x^2} – x – 12} \right).$

$y’ = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 3 \Rightarrow y = 143\\
x = 4 \Rightarrow y = – 200
\end{array} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-4.png" alt="">

Vậy:

Hàm số đạt cực đại tại $x = – 3$, ${y_{CĐ}} = 143.$

Hàm số đạt cực tiểu tại $x = 2$, ${y_{CT}} = – 200.$

b) $y = \frac{{{x^2} – 2x + 9}}{{x – 2}}.$

Tập xác định: $D = R\backslash \{ 2\} .$

$y’ = \frac{{{x^2} – 4x – 5}}{{{{(x – 2)}^2}}}.$

$y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1 \Rightarrow y = – 4}\\
{x = 5 \Rightarrow y = 8}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-5.png" alt="">

Vậy hàm số đạt cực đại tại $x = – 1$, ${y_{CĐ}} = – 4$ và đạt cực tiểu tại $x = 5$, ${y_{CT}} = 8.$

c) $y = 2x + \left| {{x^2} – 4} \right|$ 
$$
= \left\{ {\begin{array}{l}
{{x^2} + 2x – 4{\rm{\: khi \:}}x \le – 2{\rm{\: hay \:}}x \ge 2}\\
{ – {x^2} + 2x + 4{\rm{\: khi \:}} – 2 < x < 2}
\end{array}} \right. .
$$

Tập xác định: $D = R.$

$$
y’ = \left\{ {\begin{array}{l}
{2x + 2{\rm{\:khi \:}}x < – 2{\rm{\: hay \:}}x > 2}\\
{ – 2x + 2{\rm{\: khi \:}} – 2 < x < 2}
\end{array}.} \right.
$$

$y’ = 0 \Leftrightarrow x = 1 \Rightarrow y = 5.$

Tại $x = \pm 2$ hàm số không có đạo hàm.

Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-6.png" alt="">

Vậy:

Hàm số đạt cực đại tại $x = 0$, ${y_{CĐ}} = 5.$

Hàm số đạt cực tiểu tại $x = – 2$, ${y_{CT}} = – 4$ và tại $x = 2$, ${y_{CT}} = 4.$

## Bài tập
## Bài tập 1. Tìm cực trị của các hàm số sau:

a) $f(x) = \frac{1}{3}{x^3} – 2{x^2} + 3x – 1.$

b) $f(x) = \frac{1}{3}{x^3} – {x^2} + 3x – 2.$

c) $y = \frac{2}{3}{x^3} + \frac{5}{2}{x^2} + 2x + 1.$

d) $y = 4 – 2{x^2} – {x^4}.$

e) $f(x) = {x^4} – 4{x^2} – 5.$

f) $f(x) = \frac{{{x^5}}}{5} – \frac{{{x^3}}}{3} + 2.$

## Bài tập 2. Tìm cực trị của các hàm số sau:

a) $y = \frac{{{x^2} – 3x + 6}}{{x – 1}}.$

b) $f(x) = x + 3 + \frac{4}{x}.$

c) $y = \frac{{{x^2} – x + 1}}{{{x^2} + x + 1}}.$

d) $y = \frac{{{x^2}}}{{{x^3} + 1}}.$

## Bài tập 3. Tìm cực trị của hàm số sau:

a) $f(x) = |x|(x + 4).$

b) $y = \left| {{x^2} – 6x + 5} \right| + 2x.$

c) $y = {x^2} + 3x + \sqrt {{x^2} – 6x + 9} .$

## Bài tập 4. Tìm cực trị của hàm số sau:

a) $y = x\sqrt {4 – {x^2}} .$

b) $y = x + \sqrt {{x^2} + 1} .$

c) $y = \sqrt {{x^2} – 4x + 12} .$

d) $y = \sqrt {5 – 4x – {x^2}} .$

<!-- chunk:6 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Vấn đề 2: Tìm cực trị của hàm số theo quy tắc 2.

1. PHƯƠNG PHÁP:
1) Tìm $f'(x).$

2) Tìm các nghiệm ${x_i}$ $(i = 1,2, \ldots )$ của phương trình $f'(x) = 0.$

3) Tìm $f”(x)$ và tính $f”\left( {{x_i}} \right).$

+ Nếu $f”\left( {{x_i}} \right) < 0$ thì hàm số $f$ đạt cực đại tại ${x_i}.$

+ Nếu $f”\left( {{x_i}} \right) > 0$ thì hàm số $f$ đạt cực tiểu tại ${x_i}.$

2. CÁC VÍ DỤ:

<!-- chunk:7 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 1: Tìm các điểm cực trị của các hàm số $y = {x^4} – 8{x^2} – 6.$

Tập xác định: $D = R.$

$y’ = 4{x^3} – 16x.$

$y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \Rightarrow y = – 6}\\
{x = \pm 2 \Rightarrow y = – 22}
\end{array}} \right..
$$

$y” = 12{x^2} – 16.$

Ta có:

$y”(0) = – 16 < 0$ $\Rightarrow$ Tại $x = 0$ hàm số đạt cực đại và ${y_{CĐ}} = 3.$

$y”( \pm 2) = 32 > 0$ $\Rightarrow$ Tại $x = \pm 2$ hàm số đạt cực tiểu và ${y_{CT}} = – 22.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 2: Tìm các điểm cực trị của các hàm số $y = \sin 2x + \cos 2x + \sqrt 2 .$

Tập xác định: $D = R.$

$y’ = 2\cos 2x – 2\sin 2x.$

$y’ = 0 \Leftrightarrow \sin 2x = \cos 2x$ $\Leftrightarrow x = \frac{\pi }{8} + \frac{{k\pi }}{2}.$

$y” = – 4\sin 2x – 4\cos 2x.$

Ta có:

$y”\left( {\frac{\pi }{8} + \frac{{k\pi }}{2}} \right)$ $= – 4\sin \left( {\frac{\pi }{4} + k\pi } \right) – 4\cos \left( {\frac{\pi }{4} + k\pi } \right)$ 
$$
= \left\{ \begin{array}{l}
– 4\sqrt 2 {\rm{\:khi\:}}k = 2m\\
4\sqrt 2 {\rm{\:khi\:}}k = 2m – 1
\end{array} \right..
$$

Suy ra:

+ Tại $x = \frac{\pi }{8} + m\pi$ hàm số đạt cực đại và ${y_{CĐ}} = 2\sqrt 2 .$

+ Tại $x = – \frac{{7\pi }}{8} + m\pi$ hàm số đạt cực tiểu và ${y_{CT}} = 0.$

## Bài tập

## Bài tập 1. Tìm cực trị của các hàm số sau:

a) $y = x – \sin 2x + 2.$

b) $y = 3 – 2\cos x – \cos 2x.$

## Bài tập 2. Tìm cực trị của các hàm số sau:

a) $y = \sin 2x + \cos 2x + \sqrt 2 .$

b) $y = {\sin ^2}x – \sqrt 3 \cos x.$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Vấn đề 3: Điều kiện để hàm số đạt cực trị.

1. PHƯƠNG PHÁP:

1) Tìm tập xác định $D$ và tính $f'(x).$

2) Hàm số đạt cực trị tại ${x_0} \in D$ $\Leftrightarrow f'(x)$ đổi dấu khi qua ${x_0}.$

2. CÁC VÍ DỤ:

Ví dụ: Định giá trị của $m$ để hàm số sau có cực trị:

a) $y = \frac{{{x^2} – 2x + 3m – 2}}{{x – m}}.$

b) $y = {x^3} – 3m{x^2} – 3\left( {{m^2} – 8} \right)x + m.$

a) $y = \frac{{{x^2} – 2x + 3m – 2}}{{x – m}}.$

Tập xác định: $D = R\backslash \{ m{\rm{\} }}.$

$y’ = \frac{{{x^2} – 2mx – m + 2}}{{{{(x – m)}^2}}}.$

$y’ = 0$ $\Leftrightarrow g(x) = {x^2} – 2mx – m + 2 = 0$ $(x \ne m)$ $(1).$

Hàm số có cực trị $\Leftrightarrow y’$ đổi dấu trên $D.$

$\Leftrightarrow (1)$ có $2$ nghiệm phân biệt khác $m.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ > 0}\\
{g(m) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + m – 2 > 0}\\
{ – {m^2} – m + 2 \ne 0}
\end{array}} \right. .
$$

$\Leftrightarrow m < – 1$ hay $m > 2.$

Vậy $m$ thỏa yêu cầu bài toán $\Leftrightarrow m < – 1$ hay $m > 2.$

b) $y = {x^3} – 3m{x^2} – 3\left( {{m^2} – 8} \right)x + m.$

Tập xác định: $D = R.$

$y’ = 3{x^2} – 6mx – 3{m^2} + 24.$

$y’ = 0$ $\Leftrightarrow 3{x^2} – 6mx – 3{m^2} + 24 = 0$ $(2).$

Hàm số có cực trị $\Leftrightarrow y’$ đổi dấu trên $D.$

$\Leftrightarrow (2)$ có $2$ nghiệm phân biệt.

$\Leftrightarrow \Delta ‘ = {(3m)^2} + 9{m^2} – 72 > 0.$

$\Leftrightarrow {m^2} – 4 > 0.$

$\Leftrightarrow m < – 2$ hay $m > 2.$

## Bài tập

## Bài tập 1. Chứng minh rằng hàm số $y = \frac{{{x^2} – m(m + 1)x + {m^3} + 1}}{{x – m}}$ luôn có cực đại và cực tiểu.

## Bài tập 2. Định $m$ để hàm số có cực đại, cực tiểu:

a) $y = {x^3} + 3{x^2} + mx – 10.$

b) $y = {x^3} – 3{x^2} + 3mx + 3m + 4.$

c) $y = \frac{{{x^2} – mx + 3}}{{x – 1}}.$

d) $y = \frac{{{x^2} – (m + 1)x + 2m – 1}}{{x – m}}.$

## Bài tập 3. Định $m$ để hàm số $y = – 2x + m\sqrt {{x^2} + 1}$:

a) Có cực trị.

b) Có cực đại.

<!-- chunk:10 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Vấn đề 4: Định giá trị tham số để hàm số đạt cực trị tại ${x_0}$ cho trước.
1. PHƯƠNG PHÁP:

1) Tìm tập xác định $D$ và tính $f'(x).$

2) Điều kiện cần: Hàm số có cực trị tại ${x_0}$ $\Rightarrow y’\left( {{x_0}} \right) = 0$ $\Rightarrow$ giá trị của tham số.

3) Thay giá trị tham số vừa tìm được vào $y’$ thử lại.

Chú ý:

+ Khi thử lại ta có thể dùng một trong hai cách: Dùng Quy tắc 1 hay Quy tắc 2.

+ Khi phương trình $y’ = 0$ có thể xác định được nghiệm cụ thể thì ta lập bảng biến thiên và dựa vào bảng biến thiên để suy ra yêu cầu bài toán.

2. CÁC VÍ DỤ:

<!-- chunk:11 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 1: Định $m$ để hàm số $y = \frac{{{x^2} – mx + 1}}{{x – m}}$ đạt cực đại tại $x = 10.$

Tập xác định: $D = R\backslash \{ m\} .$

$y’ = \frac{{{x^2} – 2mx + {m^2} – 1}}{{{{(x – m)}^2}}}.$

$y’ = 0$ $\Leftrightarrow {x^2} – 2mx + {m^2} – 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = m – 1}\\
{x = m + 1}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so-7.png" alt="">

Dựa vào bảng biến thiên ta có:

Hàm số đạt cực đại tại $x = 10$ $\Leftrightarrow m – 1 = 10 \Leftrightarrow m = 11.$

Vậy $m$ thỏa bài toán $\Leftrightarrow m = 11.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 2: Định $a$ để hàm số $y = 2x – a\sin x + \frac{1}{3}\sin 3x$ đạt cực tiểu tại $x = \frac{\pi }{3}.$

Tập xác định: $D = R.$

$y’ = 2 – a\cos x + \cos 3x.$

Hàm số đạt cực trị tại $x = \frac{\pi }{3}$ $\Rightarrow y’\left( {\frac{\pi }{3}} \right) = 0.$

$\Leftrightarrow 2 – a\cos \frac{\pi }{3} + \cos 3 \cdot \frac{\pi }{3} = 0$ $\Leftrightarrow 2 – \frac{a}{2} – 1 = 0$ $\Leftrightarrow a = 2.$

Đảo lại: Với $a = 2$ ta có $y’ = 2 – 2\cos x + \cos 3x$ $\Rightarrow y” = 2\sin x – 3\sin 3x.$

Ta có: $y”\left( {\frac{\pi }{3}} \right) = 2\sin \frac{\pi }{3} – 3\sin \pi = \sqrt 3 > 0$ $\Rightarrow$ Tại $x = \frac{\pi }{3}$ hàm số đạt cực tiểu.

Vậy: Hàm số đạt cực tiểu tại $x = \frac{\pi }{3}$ $\Leftrightarrow a = 2.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 3: Định $m$ để hàm số $y = {x^3} – (m + 1){x^2} + (3m – 4)x + 5$ đạt cực đại tại $x = 1.$

Tập xác định: $D = R.$

$y’ = 3{x^2} – 2(m + 1)x + 3m – 4.$

Hàm số đạt cực đại tại $x = 1 \Rightarrow y'(1) = 0.$

$\Leftrightarrow 3 – 2(m + 1) + 3m – 4 = 0$ $\Leftrightarrow m = 3.$

Khi $m = 3$ thì $y’ = 3{x^2} – 8x + 5$ $\Rightarrow y” = 6x – 8.$

Ta có: $y”(1) = – 2 < 0$ $\Rightarrow$ Tại $x = 1$ hàm số đạt cực đại.

Vậy $m = 3$ thỏa yêu cầu bài toán.

<!-- chunk:14 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 4: Cho hàm số $y = \frac{1}{3}{x^3} – (m – 1){x^2} + \left( {{m^2} + 6m} \right)x + 4.$ Định $m$ để hàm số đạt cực trị tại ${x_1}$, ${x_2}$ sao cho ${x_1} < {x_2} < 1.$

Tập xác định: $D = R.$

$y’ = {x^2} – 2(m – 1)x + {m^2} + 6m.$

$y’ = 0$ $\Leftrightarrow {x^2} – 2(m – 1)x + {m^2} + 6m = 0$ $(1).$

Đặt $t = x – 1 \Leftrightarrow x = t + 1.$

$(1)$ trở thành ${(t + 1)^2} – 2(m – 1)(t + 1) + {m^2} + 6m = 0.$

$\Leftrightarrow {t^2} + 2t + 1 – 2(m – 1)t – 2m + 2 + {m^2} + 6m = 0.$

$\Leftrightarrow {t^2} – 2(m – 2)t + {m^2} + 4m + 3 = 0$ $(2).$

YCBT $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ sao cho ${x_1} < {x_2} < 1.$

$\Leftrightarrow (2)$ có $2$ nghiệm ${t_1}$, ${t_2}$ sao cho ${t_1} < {t_2} < 0.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ > 0}\\
{S < 0}\\
{P > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 8m + 1 > 0}\\
{2(m – 2) < 0}\\
{{m^2} + 4m + 3 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < \frac{1}{8}}\\
{m < 2}\\
{m < – 3{\rm{\:hay\:}}m > – 1}
\end{array}} \right.
$$
 $\Leftrightarrow m < – 3$ hay $– 1 < m < \frac{1}{8}.$

Chú ý:

Khi cần so sánh nghiệm của một phương trình bậc hai với $\alpha$, ta đặt $t = x – \alpha .$

## Bài tập
## Bài tập 1. Tìm $a$, $b$, $c$, $d$ của hàm số $f(x) = a{x^3} + b{x^2} + cx + d$ sao cho $f(x)$ đạt cực tiểu tại $x = 0$, $f(0) = 0$ và đạt cực đại tại $x = 1$, $f(1) = 1.$

## Bài tập 2. Cho hàm số $y = \frac{{{x^2} – ax + 2b}}{{{x^2} – 2x + 1}}.$ Tìm $a$, $b$ để hàm số có giá trị cực trị bằng $\frac{5}{4}$ khi $x = -3.$

## Bài tập 3. Xác định các hệ số $a$, $b$, $c$ sao cho hàm số $f(x) = {x^3} + a{x^2} + bx + c$ đạt cực trị bằng $0$ tại điểm $x = -2$ và đồ thị của hàm số qua điểm $A(1;0).$

## Bài tập 4. Định $m$ để hàm số $y = {x^3} – (m – 3){x^2} + (4m – 1)x – m$ đạt cực trị tại ${x_1}$, ${x_2}$ sao cho ${x_1} < – 2 < {x_2}.$

## Bài tập 5. Định $m$ để hàm số $y = \frac{{{x^2} + (m + 1)x + 2m + 1}}{{x + 1}}$ đạt cực trị tại ${x_1}$, ${x_2}$ sao cho ${x_1} < {x_2} < 2.$

## Bài tập 6. Định $m$ để hàm số $y = \frac{{m{x^2} – 2x + m}}{{{x^2} – x}}$:

a) Đạt cực đại, cực tiểu tại các điểm có hoành độ dương.

b) Chỉ có một cực trị.

## Bài tập 7. Tìm $m$ để đồ thị hàm số $y = \frac{{{x^3}}}{3} + m{x^2} + (m + 6)x + 2$ có hai điểm cực trị ở về hai phía đối với trục $Oy.$

## Bài tập 8. Tìm $m$ để hàm số $y = {x^3} + 3m{x^2} + 3\left( {{m^2} – 1} \right)x + {m^2} – 3m$ đạt cực đại, cực tiểu tại ${x_1}$, ${x_2}$ thỏa $x_1^2 + x_2^2 = 10.$

<!-- chunk:15 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Vấn đề 5: Giá trị cực trị của hàm số bậc ba và hàm số dạng phân thức.

1. PHƯƠNG PHÁP: 

a) Cho hàm số bậc ba: $y = f(x) = a{x^3} + b{x^2} + cx + d$ đạt cực trị tại ${x_0}.$

Khi đó: Lấy $y$ chia cho $y’$ ta được thương là $T(x)$ và dư là $D(x) = \alpha x + \beta .$

Ta viết được $y = f(x) = y’.T(x) + D(x).$

Ta có: Tọa độ điểm cực trị của hàm số thỏa hệ:

$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y = y’.T(x) + D(x)}
\end{array}} \right.
$$
 $\Rightarrow y = D(x) = \alpha x + \beta .$

Do đó ta có $y\left( {{x_0}} \right) = \alpha {x_0} + \beta .$

b) Cho hàm số $y = f(x) = \frac{{u(x)}}{{v(x)}}$ đạt cực trị tại ${x_0}.$

Ta có: Tọa độ điểm cực trị của hàm số thỏa hệ:

$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y = \frac{{u(x)}}{{v(x)}}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{u'(x)v(x) = u(x)v'(x)}\\
{y = \frac{{u(x)}}{{v(x)}}}
\end{array}} \right.
$$
 $\Rightarrow y = \frac{{u(x)}}{{v(x)}} = \frac{{u'(x)}}{{v'(x)}}.$

Do đó ta có $y\left( {{x_0}} \right) = \frac{{u’\left( {{x_0}} \right)}}{{v’\left( {{x_0}} \right)}}.$

2. VÍ DỤ:

<!-- chunk:16 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 1: Định $m$ để hàm số $y = \frac{{2{x^2} + (m + 2)x – 4 – m}}{{2x – m}}$ có cực đại, cực tiểu sao cho:

a) Hai giá trị cực trị cùng dấu.

b) Hai điểm cực trị cùng với điểm $A(1;1)$ tạo thành một tam giác vuông tại $A.$

Tập xác định: $D = R\backslash \left\{ {\frac{m}{2}} \right\}.$

$y’ = \frac{{4{x^2} – 4mx – {m^2} + 8}}{{{{(2x – m)}^2}}}.$

$y’ = 0$ $\Leftrightarrow g(x) = 4{x^2} – 4mx – {m^2} + 8 = 0$ $(x \ne m).$

Hàm số có cực đại, cực tiểu $\Leftrightarrow$ $y’$ đổi dấu hai lần trên $D.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{\Delta _g} > 0}\\
{g(m) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{8{m^2} – 32 > 0}\\
{ – 8{m^2} + 32 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m < – 2$ hay $m > 2.$

Khi đó: Tọa độ điểm cực trị thỏa hệ:

$$
\left\{ {\begin{array}{l}
{y = \frac{{u(x)}}{{v(x)}}}\\
{y’ = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{u'(x)v(x) = u(x)v'(x)}\\
{y = \frac{{u(x)}}{{v(x)}}}
\end{array}} \right..
$$

$\Rightarrow y = \frac{{u(x)}}{{v(x)}} = \frac{{u'(x)}}{{v'(x)}}$ $= \frac{{4x + m + 2}}{2}.$

Do đó: ${y_{CĐ}} = \frac{{4{x_{CT}} + m + 2}}{2}$, ${y_{CT}} = \frac{{4{x_{CĐ}} + m + 2}}{2}.$

${x_{CĐ}}.{x_{CT}} = \frac{{ – {m^2} + 8}}{4}$ và ${x_{CĐ}} + {x_{CT}} = m.$

a) ${y_{CĐ}}$ và ${y_{CT}}$ cùng dấu $\Leftrightarrow {y_{CĐ}}.{y_{CT}} > 0.$

$\Leftrightarrow \frac{1}{4}\left[ {16{x_{CĐ}}{x_{CT}} + 4(m + 2)\left( {{x_{CĐ}} + {x_{CT}}} \right) + {{(m + 2)}^2}} \right] > 0.$

$\Leftrightarrow 16.\frac{{ – {m^2} + 8}}{4} + 4(m + 2)m + {(m + 2)^2} > 0.$

$\Leftrightarrow {m^2} + 12m + 36 > 0.$

$\Leftrightarrow m \ne – 6.$

Vậy $m$ thỏa yêu cầu bài toán $\Leftrightarrow m < – 2$ hay $m > 2$ và $m \ne – 6.$

b) Ta có hai điểm cực trị là $M\left( {{x_{CĐ}};{y_{CĐ}}} \right)$ và $N\left( {{x_{CT}};{y_{CT}}} \right).$

Suy ra: 
$$
\overrightarrow {AM} = \left( {\begin{array}{c}
{{x_{CĐ}} – 1;\frac{{4{x_{CĐ}} + m}}{2})}
\end{array}} \right)
$$
 và $\overrightarrow {AN} = \left( {{x_{CT}} – 1;\frac{{4{x_{CT}} + m}}{2}} \right).$

Do đó $\Delta AMN$ vuông tại $A$ $\Leftrightarrow \overrightarrow {AM} .\overrightarrow {AN} = 0.$

$\Leftrightarrow \left( {{x_{CĐ}} – 1} \right)\left( {{x_{CT}} – 1} \right)$ $+ \frac{{\left( {4{x_{CĐ}} + m} \right)\left( {4{x_{CT}} + m} \right)}}{4} = 0.$

$\Leftrightarrow 20{x_{CĐ}}{x_{CT}} + (4m – 4)\left( {{x_{CĐ}} + {x_{CT}}} \right) + {m^2} + 4 = 0.$

$\Leftrightarrow 5\left( { – {m^2} + 8} \right) + (4m – 4)m + {m^2} + 4 = 0.$

$\Leftrightarrow – 4m + 44 = 0$ $\Leftrightarrow m = 11$ (thỏa điều kiện $m < -2$ hay $m > 2$).

Vậy $m$ thỏa bài toán $\Leftrightarrow m = 11.$

Chú ý: Khi gặp các bài toán đòi hỏi đến tọa độ các điểm cực trị ta thường biến đổi để đưa về áp dụng định lí Viet đối với phương trình bậc hai.

<!-- chunk:17 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-cuc-tri-cua-ham-so.html -->
## Ví dụ 2: Cho hàm số $y = {x^3} – 3{x^2} + 3(4m – 3)x + 3.$ Định $m$ để hàm số có cực đại, cực tiểu và khoảng cách giữa hai tiếp tuyến của đồ thị tại hai điểm cực trị bằng $32.$

Tập xác định: $D = R.$

$y’ = 3{x^2} – 6x + 3(4m – 3).$

$y’ = 0$ $\Leftrightarrow 3{x^2} – 6x + 3(4m – 3) = 0$ $\Leftrightarrow {x^2} – 2x + 4m – 3 = 0$ $(1).$

Hàm số có cực đại, cực tiểu $\Leftrightarrow (1)$ có $2$ nghiệm phân biệt ${x_1}$, ${x_2}.$

$\Leftrightarrow \Delta ‘ = 1 – 4m + 3 > 0$ $\Leftrightarrow 4m – 4 < 0 \Leftrightarrow m < 1.$

Chia y cho $y’$ ta viết được:

$y = \frac{{x – 1}}{3}y’ + (8m – 8)x + 4m.$

Tọa độ điểm cực trị của đồ thị thỏa hệ:

$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y = \frac{{x – 1}}{3}y’ + (8m – 8)x + 4m}
\end{array}} \right..
$$

$\Rightarrow y = (8m – 8)x + 4m.$

$$
\Rightarrow \left\{ {\begin{array}{l}
{{y_1} = (8m – 8){x_1} + 4m}\\
{{y_2} = (8m – 8){x_2} + 4m}
\end{array}} \right..
$$

Vì tại điểm cực trị ta có $y’ = 0$ nên:

Tiếp tuyến của đồ thị tại $A\left( {{x_1};{y_1}} \right)$ là ${d_A}:y = {y_1}.$

Tiếp tuyến của đồ thị tại $B\left( {{x_2};{y_2}} \right)$ là ${d_B}:y = {y_2}.$

Suy ra $d = d\left( {{d_A};{d_B}} \right) = \left| {{y_1} – {y_2}} \right|$ $= \left| {(8m – 8)\left( {{x_1} – {x_2}} \right)} \right|.$

Do đó: YCBT $\Leftrightarrow {d^2} = {32^2}.$

$\Leftrightarrow {(8m – 8)^2}\left[ {{{\left( {{x_1} + {x_2}} \right)}^2} – 4{x_1}{x_2}} \right] = {32^2}.$

$\Leftrightarrow {(8m – 8)^2}\left[ {{{(2)}^2} – 4(4m – 3)} \right] = {32^2}.$

$\Leftrightarrow {(m – 1)^2}[16 – 16m] = 16.$

$\Leftrightarrow {(m – 1)^2}(1 – m) = 1.$

$\Leftrightarrow {(m – 1)^3} = – 1.$

$\Leftrightarrow m – 1 = – 1 \Leftrightarrow m = 0.$

Vậy $m$ thỏa yêu cầu bài toán $\Leftrightarrow m = 0.$

## Bài tập
## Bài tập 1. Cho hàm số $y = \frac{{{x^2} – 2mx + m + 1}}{{x – 1}} = \frac{{u(x)}}{{v(x)}}.$

a) Tìm $m$ để hàm số đạt cực đại, cực tiểu tại các điểm có hoành độ dương.

b) Giả sử ${x_0}$ là hoành độ cực trị. Chứng minh rằng: $y\left( {{x_0}} \right) = \frac{{u’\left( {{x_0}} \right)}}{{v’\left( {{x_0}} \right)}}.$

c) Khi hàm số có cực đại và cực tiểu. Tìm $m$ để ${y_{CD}}$ và ${y_{CT}}$ cùng dấu.

## Bài tập 2. Cho hàm số $y = \frac{{m{x^3}}}{3} – m{x^2} + x – 1.$

a) Tìm $m$ để hàm số có cực đại, cực tiểu.

b) Giả sử ${x_0}$ là hoành độ cực trị, $R(x)$ là biểu thức dư khi chia $y$ cho $y’.$ Chứng minh rằng: $f\left( {{x_0}} \right) = R\left( {{x_0}} \right).$

c) Khi hàm số có cực đại và cực tiểu. Tìm $m$ để ${y_{CĐ}}$ và ${y_{CT}}$ cùng dấu.

## Bài tập 3. Cho hàm số $y = \frac{{ – {x^2} + 3x + m}}{{x – 4}}.$ Định $m$ để hàm số có cực đại và cực tiểu thoả điều kiện: $\left| {{y_{CĐ}} – {y_{CT}}} \right| = 4.$

## Bài tập 4. Định $m$ để các hàm số sau có cực đại và cực tiểu. Viết phương trình đường thẳng đi qua hai điểm cực trị đó.

a) $y = \frac{{{x^2} – 2x + m + 2}}{{x + m – 1}}.$

b) $y = – {x^3} + 3m{x^2} + 3\left( {1 – {m^2}} \right)x + {m^3} – {m^2}.$

## Bài tập 5. Cho hàm số $y = \frac{{{x^2} + (m + 1)x + m + 1}}{{x + 1}}$ $\left( {{C_m}} \right).$ Chứng minh rằng: Với $m$ bất kỳ, $\left( {{C_m}} \right)$ luôn có điểm cực đại, điểm cực tiểu và khoảng cách giữa hai điểm đó bằng $\sqrt {20} .$

## Bài tập 6. Cho hàm số $y = x + \left| {{x^2} – 2x + m} \right|.$

a) Tùy theo $m$ hãy lập bảng biến thiên của hàm số.

b) Định $m$ để hàm số có cực đại và ${y_{CĐ}} < 3.$

## Bài tập 7. Tìm $m$ để đồ thị hàm số $y = \frac{{{x^2} + 2{m^2}x + m}}{{x + 1}}$ có hai điểm cực trị ở về hai phía đối với trục $Ox.$

## Bài tập 8. Tìm $m$ để đồ thị hàm số $y = 2{x^3} – 3(2m + 1){x^2} + 6m(m + 1)x + 1$ có hai điểm cực trị đối xứng nhau qua đường thẳng $(d):y = x + 4.$

## Bài tập 9. Cho $y = \frac{{{x^2} + 2mx + 2}}{{x + 1}}.$ Tìm $m$ để đồ thị hàm số có điểm cực đại, cực tiểu và khoảng cách từ hai điểm đó đến đường thẳng $x + y + 1 = 0$ bằng nhau.

## Bài tập 10. Tìm $m$ để đồ thị hàm số $y = \frac{{{x^2} + 2(m + 1)x + {m^2} + 4m}}{{x + 2}}$ có hai điểm cực trị và các điểm cực trị này cùng với gốc tọa độ $O$ tạo thành tam giác vuông tại $O.$