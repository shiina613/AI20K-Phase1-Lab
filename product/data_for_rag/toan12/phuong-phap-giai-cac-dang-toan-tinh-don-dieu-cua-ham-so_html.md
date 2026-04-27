# Phương pháp giải các dạng toán tính đơn điệu của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
Bài viết trình bày tóm tắt lý thuyết sách giáo khoa và phương pháp giải các dạng toán tính đơn điệu của hàm số trong chương trình Giải tích 12 chương 1.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## I. NHẮC LẠI:

Giả sử $K$ là một khoảng (một đoạn hoặc nửa khoảng) và $f$ là một hàm số xác định trên $K.$

+ $f$ đồng biến trên $K$ $\Leftrightarrow \forall {x_1},{x_2} \in K$: ${x_1} < {x_2} \Rightarrow f\left( {{x_1}} \right) < f\left( {{x_2}} \right).$

+ $f$ nghịch biến trên $K$ $\Leftrightarrow \forall {x_1},{x_2} \in K$: ${x_1} < {x_2} \Rightarrow f\left( {{x_1}} \right) > f\left( {{x_2}} \right).$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## II. ỨNG DỤNG CỦA ĐẠO HÀM ĐỂ XÉT TÍNH ĐƠN ĐIỆU:
1. Điều kiện cần:
Định lí 1: Giả sử hàm số $f$ có đạo hàm trên khoảng $K.$

a) Nếu hàm số $f$ đồng biến trên khoảng $K$ thì $f'(x) \ge 0$ với mọi $x \in K.$

b) Nếu hàm số $f$ nghịch biến trên khoảng $K$ thì $f'(x) \le 0$ với mọi $x \in K.$

2. Điều kiện đủ:

Định lí 2: (điều kiện đủ để hàm số đơn điệu trên một khoảng).

Giả sử hàm số $f$ có đạo hàm trên khoảng $K.$

a) Nếu $f'(x) > 0$ với mọi $x \in K$ thì hàm số $f$ đồng biến trên khoảng $K.$

b) Nếu $f'(x) < 0$ với mọi $x \in K$ thì hàm số $f$ nghịch biến trên khoảng $K.$

c) Nếu $f'(x) = 0$ với mọi $x \in K$ thì hàm số $f$ không đổi trên khoảng $K.$

Chú ý:

Khoảng $K$ trong định lí trên có thể được thay bởi một đoạn hay nửa khoảng. Khi đó ta phải bổ sung thêm giả thiết “Hàm số liên tục $f$ trên đoạn hay nửa khoảng đó”. Tức là ta có:

+ Nếu hàm số $f$ liên tục trên đoạn $[a,b]$ và có đạo hàm $f'(x) > 0$ trên khoảng $(a,b)$ thì hàm số $f$ đồng biến trên $[a,b].$

+ Nếu hàm số $f$ liên tục trên đoạn $[a,b]$ và có đạo hàm $f'(x) < 0$ trên khoảng $(a,b)$ thì hàm số $f$ nghịch biến trên $[a,b].$

3. Mở rộng:

Trong trường hợp phương trình $y’ = 0$ có hữu hạn nghiệm, thì ta có định lí mở rộng sau:

Định lí 3:

+ $f$ tăng trên $K$ $\Leftrightarrow f'(x) \ge 0$, $\forall x \in K.$

+ $f$ giảm trên $K$ $\Leftrightarrow f'(x) \le 0$, $\forall x \in K.$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Dạng 1: Tìm khoảng tăng, giảm của hàm số $y = f(x).$

1. PHƯƠNG PHÁP:

+ Tìm miền xác định.

+ Tìm $y’.$

+ Tìm các điểm mà tại đó hàm số có đạo hàm bằng $0$ hay tại đó hàm số không có đạo hàm.

+ Xét dấu $y’$ bằng bảng biến thiên.

+ Dựa vào định lí trên để kết luận về tính tăng, giảm của hàm số.

2. CÁC VÍ DỤ:

<!-- chunk:4 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 1: Xét chiều biến thiên của các hàm số sau:

a) $y = {x^3} – 6{x^2} + 9x + 1.$

b) $y = {x^4} – 8{x^2} + 3.$

a) Tập xác định: $D = R.$

$y’ = 3{x^2} – 12x + 9.$

$y’ = 0 \Leftrightarrow 3{x^2} – 12x + 9 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 3}
\end{array}} \right. .
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-1.png" alt="">

Vậy hàm số tăng trên $( – \infty ;1)$, $(3; + \infty )$, hàm số giảm trong $(1;3).$

b) Tập xác định: $D = R.$

$y’ = 4{x^3} – 16x.$

$y’ = 0 \Leftrightarrow 4x\left( {{x^2} – 4} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-2.png" alt="">

Vậy hàm số tăng trong $( – 2;0)$, $(2; + \infty )$, giảm trong $( – \infty ; – 2)$, $(0;2).$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 2: Tìm khoảng tăng, giảm của các hàm số sau:

a) $y = \frac{{2x – 3}}{{x – 2}}.$

b) $y = \frac{{{x^2} – 4x + 4}}{{x – 1}}.$

a) Tập xác định: $D = R\backslash \{ 2\} .$

$y’ = \frac{{ – 1}}{{{{(x – 2)}^2}}} < 0$ với mọi $x \in D.$

Vậy hàm số luôn giảm trên từng khoảng xác định.

b) Tập xác định: $D = R\backslash \{ 1\} .$

$y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}}.$

$y’ = 0 \Leftrightarrow {x^2} – 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-3.png" alt="">

Vậy:

Hàm số tăng trong $( – \infty ;0)$ và $(2; + \infty ).$

Hàm số giảm trong $(0;1)$ và $(1;2).$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 3: Xét chiều biến thiên của các hàm số sau:

a) $y = x + \sqrt {4 – {x^2}} .$

b) $y = 2x – \sqrt {{x^2} – 4x – 5} .$

a) $y = x + \sqrt {4 – {x^2}} .$

Tập xác định: $D = [ – 2;2].$

$y’ = 1 – \frac{x}{{\sqrt {4 – {x^2}} }}$ $= \frac{{\sqrt {4 – {x^2}} – x}}{{\sqrt {4 – {x^2}} }}$, $\forall x \in ( – 2;2).$

$y’ = 0$ $\Leftrightarrow \sqrt {4 – {x^2}} = x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{4 – {x^2} = {x^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \sqrt 2 .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-4.png" alt="">

Vậy:

Hàm số tăng trong khoảng $( – 2;\sqrt 2 ).$

Hàm số giảm trong khoảng $(\sqrt 2 ;2).$

b) $y = 2x – \sqrt {{x^2} – 4x – 5} .$

Tập xác định: $D = ( – \infty ; – 1] \cup [5; + \infty ).$

$y’ = 2 – \frac{{x – 2}}{{\sqrt {{x^2} – 4x – 5} }}$ $= \frac{{2\sqrt {{x^2} – 4x – 5} – x + 2}}{{\sqrt {{x^2} – 4x – 5} }}$, $\forall x \in ( – \infty ; – 1) \cup (5; + \infty ).$

$y’ = 0 \Leftrightarrow 2\sqrt {{x^2} – 4x – 5} = x – 2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 2 \ge 0}\\
{4\left( {{x^2} – 4x – 5} \right) = {{(x – 2)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 2}\\
{3{x^2} – 12x – 24 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = 2 + 2\sqrt 3 .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-5.png" alt="">

Vậy:

Hàm số tăng trong khoảng $( – \infty ; – 1)$, $(2 + 2\sqrt 3 ; + \infty ).$

Hàm số giảm trong khoảng $(5;2 + 2\sqrt 3 ).$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 4: Tìm khoảng tăng, giảm của các hàm số sau:

a) $y = – {x^2} + 6|x – 2|.$

b) $y = \left| {{x^2} + 4x – 5} \right|.$

a) Tập xác định: $D = R.$

Ta có: 
$$
y = \left\{ {\begin{array}{l}
{ – {x^2} + 6x – 12{\rm{\: khi \:}}x \ge 2}\\
{ – {x^2} – 6x + 12{\rm{\: khi \:}}x < 2}
\end{array}} \right..
$$

Do đó: 
$$
y’ = \left\{ {\begin{array}{l}
{ – 2x + 6{\rm{\:khi\:}}x > 2}\\
{ – 2x – 6{\rm{\:khi\:}}x < 2}
\end{array}} \right. .
$$

$y’ = 0 \Leftrightarrow x = \pm 3.$

Tại $x = 2$ hàm số không có đạo hàm.

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-6.png" alt="">

Vậy:

Hàm số tăng trong $( – \infty ; – 3)$ và $(2;3).$

Hàm số giảm trong $( – 3;2)$ và $(3; + \infty ).$

b) Tập xác định: $D = R.$

Ta có:

$$
y = \left\{ {\begin{array}{l}
{{x^2} + 4x – 5{\rm{\: khi \:}}x \le – 5{\rm{\: hay \:}}x \ge 1}\\
{ – {x^2} – 4x + 5{\rm{\: khi \:}} – 5 < x < 1}
\end{array}} \right. .
$$

Do đó: 
$$
y’ = \left\{ {\begin{array}{c}
{2x + 4{\rm{\: khi \:}}x < – 5{\rm{\: hay \:}}x > 1}\\
{ – 2x – 4{\rm{\: khi \:}} – 5 < x < 1}
\end{array}} \right..
$$

$y’ = 0 \Leftrightarrow x = – 2.$

Tại $x = -5$ hay $x = 1$ hàm số không có đạo hàm.

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-7.png" alt="">

Vậy:

Hàm số đồng biến trong $( – 5; – 2)$ và $(1; + \infty ).$

Hàm số nghịch biến trong $( – \infty ; – 5)$ và $(-2;1).$

## Bài tập
## Bài tập 1. Tìm các khoảng tăng, giảm của các hàm số sau:

a) $y = {x^2} + 2mx + m – 1.$

b) $y = – {x^3} + 6{x^2} – 12x + 8.$

c) $y = – \frac{1}{4}{x^4} – {x^3} + \frac{1}{2}{x^2} + 3x.$

d) $y = \frac{1}{3}{x^3} + \frac{1}{2}(2m + 2){x^2} + \left( {{m^2} + 2m} \right)x.$

## Bài tập 2. Tìm các khoảng đơn điệu của các hàm số sau:

a) $y = \frac{{3x + 1}}{{x + 2}}.$

b) $y = \frac{{{{(x – 2)}^2}}}{{1 – x}}.$

c) $y = \frac{{{x^2} – x}}{{{x^2} – x – 2}}.$

d) $y = \frac{{{x^3}}}{{9 – {x^2}}}.$

e) $y = \frac{x}{{{x^2} + 1}}.$

f) $y = \frac{{{x^2} + 2x + 2}}{{{x^2} – 2x + 2}}.$

## Bài tập 3. Tìm các khoảng đơn điệu của các hàm số sau:

a) $y = \sqrt {{x^2} – 4x + 3} .$

b) $y = \frac{{x + 1}}{{\sqrt {{x^2} – x + 1} }}.$

c) $y = \frac{{{x^2}}}{{\sqrt {{x^2} – 1} }}.$

d) $y = \sqrt {2x – {x^2}} .$

## Bài tập 4. Tìm khoảng tăng, giảm của các hàm số:

a) $y = |x – 1| + \frac{{{x^2} + x + 2}}{{x + 1}}.$

b) $y = {x^2} – 2x + 4|x – 2| + 3.$

## Bài tập 5. Chứng minh các hàm số:

a) $y = \left( {{m^2} + 1} \right){x^3} + {x^2} + 2x – 10$ luôn tăng trên miền xác định.

b) $y = \frac{{2x – 3}}{{3x – 6}}$ luôn giảm trên các khoảng xác định.

c) $y = \frac{{{x^2} – x – 4}}{{1 – x}}$ luôn giảm trên các khoảng xác định.

d) $y = \frac{{(m – 2)x – 2{m^2} + 2m – 4}}{{x – m}}$ luôn tăng trên các khoảng xác định.

e) $f(x) = {x^3} + x – \cos x – 4$ luôn tăng trên các khoảng xác định.

<!-- chunk:8 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Dạng 2: Chứng minh hàm số tăng (giảm) trên đoạn hay nửa khoảng.

1. PHƯƠNG PHÁP:

Để chứng minh hàm số tăng (giảm) trên $[a;b]$ (hay $[a;b)$ hay $(a;b]$) ta thực hiện các bước sau:

+ Bước 1: Chứng minh trong $(a;b)$ hàm số tăng (giảm).

+ Bước 2: Chứng minh hàm số liên tục trên đoạn hay nửa khoảng đã cho.

Kết luận: Hàm số tăng (giảm) trên đoạn hay nửa khoảng đã cho.

2. CÁC VÍ DỤ:

<!-- chunk:9 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 1: Chứng minh rằng hàm số $f(x) = \frac{1}{{\sqrt 3 }}x + \sqrt {16 – {x^2}}$ nghịch biến trên $[2;4].$

Ta có:

$f(x)$ là hàm số liên tục trên $[2;4]$ $(1).$

$f'(x) = \frac{1}{{\sqrt 3 }} – \frac{x}{{\sqrt {16 – {x^2}} }}$ $= \frac{{\sqrt {16 – {x^2}} – \sqrt 3 x}}{{\sqrt 3 \sqrt {16 – {x^2}} }}.$

$f'(x) = 0$ $\Leftrightarrow \sqrt {16 – {x^2}} = \sqrt 3 x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{16 – {x^2} = 3{x^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 2.$

Với $x \in (2;4)$ thì $\sqrt {16 – {x^2}} – \sqrt 3 x < 0$ nên $f'(x) < 0$, do đó hàm số nghịch biến trong $(2;4)$ $(2).$

Từ $(1)$ và $(2)$ suy ra $f$ là hàm số nghịch biến trên đoạn $[2;4].$

## Bài tập

## Bài tập 1. Chứng minh rằng hàm số $y = f(x) = x\sqrt {8 – {x^2}}$ đồng biến trên $[ – 2;2].$

## Bài tập 2. Chứng minh hàm số $y = \sqrt {x – 1} + \sqrt {7 – x}$ nghịch biến trên đoạn $[4;7].$

## Bài tập 3. Chứng minh hàm số $y = {x^2} + 2\sqrt 5 \sqrt {9 – {x^2}}$ đồng biến trên $[ – 3; – 2]$ và nghịch biến trong $[2;3].$

<!-- chunk:10 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Dạng 3: Định giá trị tham số để hàm số đơn điệu trên tập hợp $X$ cho trước.

1. PHƯƠNG PHÁP:

Bước 1: Tìm $y’.$

Bước 2: Đặt điều kiện cho bài toán:

+ Hàm số tăng trên $D$ $\Leftrightarrow y’ \ge 0$ $\forall x \in D.$

+ Hàm số giảm trên $D$ $\Leftrightarrow y’ \le 0$ $\forall x \in D.$

Chú ý: Trong điều kiện trên dấu bằng xảy ra khi phương trình $y’ = 0$ có hữu hạn nghiệm, nếu phương trình $y’ = 0$ có vô hạn nghiệm thì trong điều kiện sẽ không có dấu bằng.

Trong thực hành ta thường sử dụng:

Nếu biểu thức $g(x)$ quyết định dấu của $y’$ không chứa $x$ thì trong điều kiện trên không có dấu bằng.

Bước 3: Từ điều kiện trên sử dụng các kiến thức về dấu nhị thức, tam thức suy ra giá trị tham số cần tìm.

Chú ý 1: Cho $f(x) = a{x^2} + bx + c$ $(a \ne 0)$ ta có:

+ $f(x) \ge 0$, $\forall x \in R$ $\Leftrightarrow \Delta \le 0$ và $a > 0.$

+ $f(x) \le 0$, $\forall x \in R$ $\Leftrightarrow \Delta \le 0$  và $a < 0.$

Chú ý 2: Đối với hàm số lượng giác ta cần nhớ:

+ $|a\sin x| \le |a|$, $\forall x \in R.$

+ $|a\sin x + b\cos x| \le \sqrt {{a^2} + {b^2}}$, $\forall x \in R.$

2. CÁC VÍ DỤ:

<!-- chunk:11 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 1: Tìm $m$ để hàm số $y = {x^3} + (m – 3){x^2} + (2m + 3)x + m – 4$ luôn tăng trên $R.$

Tập xác định: $D = R.$

$y’ = 3{x^2} + 2(m – 3)x + 2m – 1.$

Hàm số luôn tăng trên $R \Leftrightarrow y’ \ge 0$ với mọi $x \in R.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a > 0}\\
{\Delta ‘ \le 0}
\end{array}} \right.
$$
 $\Leftrightarrow {(m – 3)^2} – 3(2m + 3) \le 0$ $\Leftrightarrow {m^2} – 12m \le 0$ $\Leftrightarrow 0 \le m \le 12.$

Vậy $m$ thỏa mãn yêu cầu bài toán $\Leftrightarrow 0 \le m \le 12.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 2: Tìm $m$ để các hàm số sau tăng trên từng khoảng xác định của nó:

a) $y = \frac{{mx + 7m – 8}}{{x – m}}.$

b) $y = \frac{{2{x^2} + x + 3m – 5}}{{x – 1}}.$

a) Tập xác định: $D = R\backslash \{ m\} .$

$y’ = \frac{{ – {m^2} – 7m + 8}}{{{{(x – m)}^2}}}.$

Dấu $y’$ là dấu của biểu thức $– {m^2} – 7m + 8.$

Hàm số tăng trên từng khoảng xác định $\Leftrightarrow y’ > 0$ với mọi $x \in D$ $\Leftrightarrow – {m^2} – 7m + 8 > 0$ $\Leftrightarrow – 8 < m < 1.$

Vậy $m$ thỏa mãn yêu cầu bài toán $\Leftrightarrow – 8 < m < 1.$

b) Tập xác định: $D = R\backslash \{ 1\} .$

$y’ = \frac{{2{x^2} – 4x – 3m + 4}}{{{{(x – 1)}^2}}}.$

Dấu của $y’$ chính là dấu của $g(x) = 2{x^2} – 4x – 3m + 4.$

Hàm số tăng trên từng khoảng xác định $\Leftrightarrow y’ \ge 0$ với mọi $x \in D$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a > 0}\\
{\Delta ‘ \le 0}
\end{array}} \right.
$$
 $\Leftrightarrow 4 – 2( – 3m + 4) \le 0$ $\Leftrightarrow 6m – 4 \le 0$ $\Leftrightarrow m \le \frac{2}{3}.$

Vậy $m$ thỏa mãn yêu cầu bài toán $\Leftrightarrow m \le \frac{2}{3}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 3: Định $m$ để hàm số $y = \frac{{{x^2} – 3mx + 4m – 12}}{{x – 2}}$ đồng biến trên $( – \infty ;0).$

Tập xác định: $D = R\backslash \{ 2\} .$

$y’ = \frac{{{x^2} – 4x + 2m + 12}}{{{{(x – 2)}^2}}}.$

Dấu của $y’$ là dấu của $g(x) = {x^2} – 4x + 2m + 12.$

Hàm số đồng biến trên $( – \infty ;0)$ $\Leftrightarrow y’ \ge 0$, $\forall x \in ( – \infty ;0).$

Cách 1:

Trường hợp 1: $\Delta ‘ \le 0$ $\Leftrightarrow – 2m – 8 \le 0$ $\Leftrightarrow m \ge – 4.$

Khi đó do $a = 1 > 0$ nên $y’ \ge 0$, $\forall x \in D.$

$\Rightarrow$ Hàm số đồng biến trên từng khoảng xác định.

$\Rightarrow$ Hàm số đồng biển trên $( – \infty ;0).$

Vậy $m \ge – 4$ thỏa yêu cầu bài toán.

Trường hợp 2: $\Delta ‘ > 0 \Leftrightarrow m < – 4.$

Khi đó $y’ = 0$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ $\left( {{x_1} < {x_2}} \right).$

Yêu cầu bài toán $\Leftrightarrow 0 \le {x_1} < {x_2}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ > 0}\\
{S > 0}\\
{P \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < – 4}\\
{4 > 0}\\
{2m + 12 \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow – 6 \le m < – 4.$

Kết luận: $m$ thỏa yêu cầu bài toán 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > – 4}\\
{ – 6 \le m < – 4}
\end{array}} \right.
$$
 $\Leftrightarrow m \ge – 6.$

Cách 2: $y’ \ge 0$ $\forall x \in ( – \infty ;0)$ $\Leftrightarrow {x^2} – 4x + 2m + 12 \ge 0$, $\forall x < 0$ $\Leftrightarrow 2m \ge – {x^2} + 4x – 12 = h(x)$ $(*).$

Ta có: $h'(x) = – 2x + 4.$

$h'(x) = 0 \Leftrightarrow x = 2.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/cac-dang-toan-tinh-don-dieu-cua-ham-so-8.png" alt="">

Dựa vào bảng biến thiên của $h(x)$ ta có:

$(*) \Leftrightarrow 2m \ge h(x)$, $\forall x \in ( – \infty ;0)$ $\Leftrightarrow 2m \ge – 12 \Leftrightarrow m \ge – 6.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 4: Tìm $m$ để hàm số $y = m\sin x + (m – 3)\cos x – 3x$ luôn giảm trên $[0;4\pi ].$

Tập xác định: $D = R.$

$y’ = m\cos x – (m – 3)\sin x – 3.$

Ta có: $|m\cos x – (m – 3)\sin x|$ $\le \sqrt {{m^2} + {{(m – 3)}^2}}$, $\forall x \in [0;4\pi ].$

$\Rightarrow m\cos x – (m – 3)\sin x$ $\le \sqrt {{m^2} + {{(m – 3)}^2}}$, $\forall x \in [0;4\pi ].$

$\Rightarrow y’ \le \sqrt {{m^2} + {{(m – 3)}^2}} – 3$, $\forall x \in [0;4\pi ].$

Phương trình $y’ = 0$ nếu có nghiệm thì có hữu hạn nghiệm thuộc $(0;4\pi ).$

Hàm số đã cho liên tục trên $[0;4\pi ].$

Do đó: Hàm số nghịch biến trên $[0;4\pi ]$ $\Leftrightarrow y’ \le 0$, $\forall x \in [0;4\pi ]$ $\Leftrightarrow \sqrt {{m^2} + {{(m – 3)}^2}} – 3 \le 0$ $\Leftrightarrow 2{m^2} – 6m \le 0$ $\Leftrightarrow 0 \le m \le 3.$

Vậy $m$ thỏa YCBT $\Leftrightarrow 0 \le m \le 3.$

## Bài tập
## Bài tập 1. Định $m$ để hàm số:

a) $y = \frac{1}{3}{x^3} + m{x^2} + (4m – 3)x + 3$ đồng biến trên $R.$

b) $y = \left( {\frac{{1 – m}}{3}} \right){x^3} – 2(1 – m){x^2} + 2(m – 2)x + 5$ nghịch biến trên $R.$

c) $y = \frac{{mx – {m^2} – 1}}{{x + 2}}$ luôn tăng trên từng khoảng xác định.

d) $y = \frac{{m{x^2} – 2x + 1}}{{x + 1}}$ luôn giảm trên từng khoảng xác định.

## Bài tập 2. Định $m$ để hàm số:

a) $y = {x^2} – 2(m – 4)x + m + 3$ đồng biến trên khoảng $(2; + \infty ).$

b) $y = \frac{1}{3}{x^3} – 2m{x^2} – 4mx – 2$ đồng biến trên $( – \infty ;0).$

c) $y = \frac{1}{3}{x^3} – (m + 1){x^2} + 4x – 10$ nghịch biến trên đúng một khoảng có độ dài bằng $2.$

d) $y = \frac{{mx – 8}}{{x – m – 2}}$ nghịch biến trên $(1; + \infty ).$

e) $y = \frac{{{x^2} – 2mx + {m^2} + 1}}{{x – m}}$ đồng biến trên $(2; + \infty ).$

## Bài tập 3. Định $m$ để hàm số:

a) $y = x + (m + 1)\sin x$ tăng trên $[0;2\pi ].$

b) $y = m\sin x + 2\cos x + (m + 2)x$ tăng trên $(0;10\pi ).$

<!-- chunk:15 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Dạng 4: Chứng minh bất đẳng thức $F(x) \ge 0$ với mọi $x \in K.$

1. PHƯƠNG PHÁP:

Chứng minh hàm số $F(x)$ liên tục và đơn điệu trên $K.$

Áp dụng định nghĩa sự đơn điệu suy ra bất đẳng thức cần chứng minh.

2. VÍ DỤ:

Chứng minh các bất đẳng thức sau:

a) $\sin x < x$ với mọi $x > 0.$

b) $\cos x > 1 – \frac{{{x^2}}}{2}$ với mọi $x \ne 0.$

a) Cách 1:

Với mỗi $x > 0$, xét hàm số $f(t) = t – \sin t$ trên $[0;a]$ với $a > x.$

Ta có:

$f(t)$ liên tục trên $[0;a].$

$f'(t) = 1 – \cos t \ge 0$, $\forall t \in (0;a).$

Phương trình $f(t) = 0$ có hữu hạn nghiệm $t \in (0;a).$

Vậy $f(t)$ đồng biến trên $[0;a].$

Do đó $f(x) > f(0)$ (vì $x > 0$) $\Rightarrow x – \sin x > 0$ hay $\sin x < x.$

Vậy ta luôn có $\sin x < x$ với mọi $x > 0.$

Cách 2:

Khi $x \ge \pi$ thì $\sin x \le 1 < \pi \le x$ nên $\sin x < x$ với mọi $x \ge \pi$ $(1).$

Khi $x \in [0;\pi )$, xét hàm số $f(x) = x – \sin x$ trên $[0;\pi )$ ta có:

+ $f$ liên tục trên $[0;\pi ).$

+ $f'(x) = 1 – \cos x > 0$, $\forall x \in (0;\pi ).$

Vậy $f$ đồng biến trên $[0;\pi ).$

Do đó: $\forall x \in (0;\pi )$ thì $f(x) > f(0)$ hay $x – \sin x > 0$ hay $\sin x < x$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\sin x < x$ với mọi $x > 0.$

b) Ta có: $\cos x > 1 – \frac{{{x^2}}}{2}$ $\Leftrightarrow \frac{{{x^2}}}{2} + \cos x – 1 > 0$ $(*).$

Xét hàm số $f(x) = \frac{{{x^2}}}{2} + \cos x – 1.$

Trường hợp 1: $x > 0.$

Ta có:

+ $f'(x) = x – \sin x > 0$, $\forall x \in (0; + \infty )$ (do câu a).

+ $f$ liên tục trên $[0; + \infty ).$

Do đó: $f$ đồng biến trên $[0; + \infty ).$

Suy ra với $x > 0$ thì $f(x) > f(0)$ $\Rightarrow \frac{{{x^2}}}{2} + \cos x – 1 > 0$ $\Rightarrow (*)$ đúng với mọi $x>0.$

Trường hợp 2: $x < 0.$

Đặt $t = -x$ thì $t > 0.$

Áp dụng kết quả của trường hợp 1, ta có:

$\frac{{{t^2}}}{2} + \cos t – 1 > 0$ $\Rightarrow \frac{{{{( – x)}^2}}}{2} + \cos ( – x) – 1 > 0$ $\Rightarrow \frac{{{x^2}}}{2} – \cos x – 1 > 0.$

$\Rightarrow (*)$ đúng với mọi $x < 0.$

Vậy $(*)$ đúng với mọi $x \ne 0.$

## Bài tập

## Bài tập 1. Chứng minh rằng:

$\sin x > x – \frac{{{x^3}}}{6}$ với mọi $x > 0$ và $\sin x < x – \frac{{{x^3}}}{6}$ với mọi $x < 0.$

## Bài tập 2. Chứng minh:

a) $3x < 2\sin x + \tan x$, $\forall x \in \left( {0,\frac{\pi }{2}} \right).$

b) $2\sin x + \sin 2x \le \frac{{3\sqrt 3 }}{2}$, $\forall x \in \left[ {\frac{\pi }{3};\frac{\pi }{2}} \right).$

## Bài tập 3. Cho $a \le 6$, $b \le – 8$, $c \le 3$ và $x \ge 1.$ Chứng minh rằng ${x^4} – a{x^2} – bx \ge c.$

## Bài tập 4. Chứng minh rằng với mọi $x \in \left[ {0;\frac{\pi }{4}} \right]$ ta có $\tan x \le \frac{{4x}}{\pi }.$

## Bài tập 5. Chứng minh rằng với mọi $x \in \left( {0;\frac{\pi }{2}} \right)$ ta có $\tan x > x + \frac{{{x^3}}}{3}.$

<!-- chunk:16 level:2 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Dạng 5: Dùng tính đơn điệu của hàm số để giải phương trình – hệ phương trình.

1. PHƯƠNG PHÁP:

a) Để chứng minh phương trình $F(x) = 0$ có nghiệm duy nhất ta thực hiện:

Bước 1: Chỉ ra một nghiệm của phương trình hay dùng tính chất hàm số liên tục để chứng minh phương trình có nghiệm.

Bước 2: Chứng minh $F(x)$ là hàm số liên tục và luôn tăng hay luôn giảm, suy ra phương trình $F(x) = 0$ nếu có nghiệm thì nghiệm đó là duy nhất.

Kết luận: Phương trình $F(x) = 0$ có nghiệm duy nhất.

b) Nếu hàm số $f(x)$ liên tục và tăng (hay giảm) trên $X$ thì với $u,v \in X$ ta có $f(u) = f(v) \Leftrightarrow u = v.$

2. VÍ DỤ:

<!-- chunk:17 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 1: Giải phương trình $9\left( {\sqrt {4x + 1} – \sqrt {3x – 2} } \right) = x + 3$ $(1).$

Điều kiện: $x \ge \frac{2}{3}.$

$(1) \Leftrightarrow \frac{{9[(4x + 1) – (3x – 2)]}}{{\sqrt {4x + 1} + \sqrt {3x – 2} }} = x + 3$ $\Leftrightarrow \sqrt {4x + 1} + \sqrt {3x – 2} – 9 = 0$ $(2).$

Xét hàm số $f(x) = \sqrt {4x + 1} + \sqrt {3x – 2} – 9.$

Ta có: $f'(x) = \frac{4}{{2\sqrt {4x + 1} }} + \frac{3}{{2\sqrt {3x – 2} }} > 0$ với mọi $x > \frac{2}{3}.$

$\Rightarrow f(x)$ tăng và liên tục trên $\left[ {\frac{2}{3}; + \infty } \right).$

$\Rightarrow (2)$ nếu có nghiệm thì nghiệm đó là duy nhất.

Mặt khác $f(6) = 0$ nên $x = 6$ là một nghiệm của $(2).$

Vậy $(2)$ có nghiệm duy nhất là $x = 6.$

Do đó $(1)$ có một nghiệm là $x = 6.$

<!-- chunk:18 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 2: Giải phương trình $8{x^3} – 4x – 2 = \sqrt[3]{{6x + 2}}$ $(1).$

$(1) \Leftrightarrow {(2x)^3} + 2x = 6x + 2 + \sqrt[3]{{6x + 2}}.$

Đặt $u = 2x$ và $v = \sqrt[3]{{6x + 2}}$, ta được $(1) \Leftrightarrow {u^3} + u = {v^3} + v$ $(2).$

Xét $f(t) = {t^3} + t$, ta có $f'(t) = 3{t^2} + 1 > 0$, $\forall t \in R.$

Do đó $(2) \Leftrightarrow f(u) = f(v)$ $\Leftrightarrow u = v \Leftrightarrow 2x = \sqrt[3]{{6x + 2}}$ $\Leftrightarrow 8{x^3} – 6x – 2 = 0$ $\Leftrightarrow (x – 1)\left( {8{x^2} + 8x + 2} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – \frac{1}{2}}
\end{array}} \right..
$$

Vậy phương trình đã cho có hai nghiệm.

<!-- chunk:19 level:3 source:https://toanmath.com/2019/04/phuong-phap-giai-cac-dang-toan-tinh-don-dieu-cua-ham-so.html -->
## Ví dụ 3: Giải hệ phương trình:

$$
\left\{ {\begin{array}{l}
{\sqrt {x + \sqrt {{x^2} – x + 1} } – \sqrt {y + \sqrt {{y^2} – y + 1} } = (y – x)(xy + 2)}\\
{{x^2} + {y^2} = 2}
\end{array}} \right. .
$$

Xét hàm số $f(t) = \sqrt {t + \sqrt {{t^2} – t + 1} } .$

Tập xác định: $D = R.$

$f'(t) = \frac{{1 + \frac{{2t – 1}}{{2\sqrt {{t^2} – t + 1} }}}}{{2\sqrt {t + \sqrt {{t^2} – t + 1} } }}$ $= \frac{{2\sqrt {{t^2} – t + 1} + 2t – 1}}{{4\sqrt {t + \sqrt {{t^2} – t + 1} } .\sqrt {{t^2} – t + 1} }} .$

Vì $2\sqrt {{t^2} – t + 1} + 2t – 1$ $= \sqrt {{{(2t – 1)}^2} + 3} + 2t – 1$ $> |2t – 1| + 2t – 1 \ge 0$ nên ta có $f(t) > 0$, $\forall t \in R.$

Suy ra $f(t)$ tăng trên $R.$

Mặt khác ta có: $2 = {x^2} + {y^2} \ge 2|xy|$ nên $|xy| \le 1$ $\Rightarrow 2 + xy > 1 + xy \ge 0.$

Do đó ta có:

+ $x > y$ thì $f(x) > f(y)$ và $y – x < 0$ $\Rightarrow$ vế trái $(1)$ $> 0 >$ vế phải $(1).$

$\Rightarrow$ Hệ không có nghiệm $(x; y)$ thỏa $x > y.$

+ $x < y$ thì $f(x) < f(y)$ và $y – x > 0$ $\Rightarrow$ vế trái $(1)$ $< 0 <$ vế phải $(1).$

$\Rightarrow$ Hệ không có nghiệm $(x;y)$ thỏa $x < y.$

Vậy nếu $(x;y)$ là nghiệm của hệ thì $x = y.$

Khi đó $(2)$ $\Leftrightarrow 2{x^2} = 2 \Leftrightarrow x = \pm 1.$

Vậy hệ đã cho có hai nghiệm là $(1;1)$, $(-1;-1).$

## Bài tập
## Bài tập 1. Giải các phương trình:

a) $\sqrt {2x + 3} + 3\sqrt {4x + 13} = 18.$

b) $\sqrt {x + 1} + \sqrt {2x + 3} + \sqrt {3x + 7} + \sqrt {4x + 24} = 15.$

c) $\sqrt {x – 1} = – {x^3} + 3{x^2} – 4x + 5.$

## Bài tập 2. Giải các hệ phương trình sau:

a) 
$$
\left\{ {\begin{array}{l}
{x – y = \cos x – \cos y}\\
{\cos x + \cos y = 1}
\end{array}} \right.
$$
 $\left( {x \in ( – \pi ;2\pi )} \right).$

b) 
$$
\left\{ {\begin{array}{l}
{\tan x – \tan y = y – x}\\
{2{x^2} + 6{y^2} = {\pi ^2}}
\end{array}} \right.
$$
 $\left( {x \in \left( { – \frac{\pi }{2};\frac{\pi }{2}} \right)} \right).$

c) 
$$
\left\{ {\begin{array}{l}
{\sqrt {x + 6} + \sqrt {y – 9} = 5}\\
{\sqrt {x – 9} + \sqrt {y + 6} = 5}
\end{array}} \right. .
$$

## Bài tập 3. Chứng minh phương trình ${x^5} – {x^2} – 2x – 1 = 0$ có nghiệm duy nhất.

## Bài tập 4. Chứng minh các phương trình sau có nghiệm duy nhất:

a) $6x + 3\cos x + 2\sin x = 0.$

b) $2x = 2a + \sin (x + a).$

c) ${x^5} – 5{x^4} + 2{x^3} – 2{x^2} + 5x + 1 = 0.$

d) ${x^2}\sqrt {x – 2} + x = 11\sqrt {30 – x} .$

## Bài tập 5. Chứng minh rằng với mọi $m \in ( – 1;1)$ thì phương trình ${\sin ^2}x + \cos x = m$ có nghiệm duy nhất thuộc đoạn $[0;\pi ].$