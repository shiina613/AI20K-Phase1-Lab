# Tìm điều kiện tham số m để hàm số đơn điệu trên R hoặc trên khoảng con của R

<!-- chunk:0 level:0 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
Ta xét dạng toán tìm điều kiện của tham số $m$ để hàm số đơn điệu trên $R$ hoặc trên khoảng con của $R.$

Lý thuyết:

Cho hàm số $y = f\left( {x,m} \right)$ với $m$ là tham số xác định trên một khoảng $I.$

a. Hàm số đồng biến trên $I$ $\Leftrightarrow y’ \ge 0, \forall x \in I$ và $y’ = 0$ chỉ xảy ra tại hữu hạn điểm.

b. Hàm số nghịch biến trên $I$ $\Leftrightarrow y’ \le 0, \forall x \in I$ và $y’ = 0$ chỉ xảy ra tại hữu hạn điểm.

Chú ý: Để xét dấu của $y’$ ta thường sử dụng phương pháp hàm số hay định lý về dấu của tam thức bậc hai như sau:

Cho tam thức bậc hai: $g\left( x \right) = a{x^2} + bx + c, \left( {a \ne 0} \right).$

a. Nếu $\Delta < 0$ thì $g(x)$ luôn cùng dấu với $a.$

b. Nếu $\Delta = 0$ thì $g(x)$ luôn cùng dấu với $a$ (trừ $x = – \frac{b}{{2a}}$).

c. Nếu $\Delta > 0$ thì phương trình $g\left( x \right) = 0$ luôn có hai nghiệm phân biệt, khi đó dấu của $g(x)$ trong khoảng hai nghiệm thì khác dấu với hệ số $a$, ngoài khoảng hai nghiệm thì cùng dấu với hệ số $a.$

Các bước cơ bản để giải bài toán tìm giá trị của tham số để hàm số đơn điệu trên một khoảng xác định:

+ Bước 1: Tìm miền xác định.

+ Bước 2: Tìm đạo hàm.

+ Bước 3: Áp dụng lý thuyết vửa nhắc ở trên.

Ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 1: Tìm tham số $m$ để hàm số $y = \frac{1}{3}{x^3} + (m + 1){x^2} – (m + 1)x + 1$ đồng biến trên tập xác định.

Phân tích: Khi xét hàm số bậc ba:

1. Luôn đồng biến hoặc nghịch biến ($y’ = 0$ vô nghiệm hoặc có nghiệm kép), đồng biến khi $a > 0$ và ngược lại.

2. Có $2$ khoảng đồng biến, một khoảng nghịch biến ($y’ = 0$ có hai nghiệm phân biệt và có hệ số $a > 0$) và ngược lại.

Lời giải:

Xét hàm số $y = \frac{1}{3}{x^3} + (m + 1){x^2} – (m + 1)x + 1$ có $y’ = {x^2} + 2\left( {m + 1} \right)x – \left( {m + 1} \right).$

Do hệ số $a = \frac{1}{3} > 0$ nên để hàm số đã cho đồng biến trên tập xác định thì phương trình $y’ = 0$ vô nghiệm hoặc có nghiệm kép.

$\Leftrightarrow \Delta’ \le 0 \Leftrightarrow {\left( {m + 1} \right)^2} + \left( {m + 1} \right) \le 0$ $\Leftrightarrow – 1 \le m + 1 \le 0$ $\Leftrightarrow – 2 \le m \le – 1.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 2: Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = 2{\sin ^3}x – 3{\sin ^2}x + m\sin x$ đồng biến trên $\left( {0;\frac{\pi }{2}} \right)$.

Phân tích:

Ta có thể biết được $\left( {0;1} \right)$ nằm ngoài khoảng hai nghiệm thì hàm số đồng biến bởi $y’$ là một tam thức bậc hai có hệ số $a = 6 > 0$, do vậy dựa trên cách xét dấu tam thức bậc hai đã học ở lớp 10 thì:

1. Nếu $\Delta < 0$ thì dấu của tam thức cùng dấu với hệ số $a$, tức là lớn hơn $0$, tức là luôn đồng biến.

2. Nếu phương trình $y’ = 0$ có hai nghiệm phân biệt ${x_1}; {x_2}$ thì trong khoảng hai nghiệm hàm số sẽ khác dấu với hệ số $a$, và ngoài khoảng hai nghiệm thì hám số sẽ cùng dấu với hệ số $a.$

Lời giải:

Do hàm số $t = \sin x$ đồng biến trên $\left( {0;\frac{\pi }{2}} \right)$ nên đặt $t = \sin x$; $t \in \left( {0;1} \right)$.

Để hàm số đồng biến trên $\left( {0;\frac{\pi }{2}} \right)$ thì hàm số $y = f\left( t \right)$ phải đồng biến trên $\left( {0;1} \right)$ $\Leftrightarrow$ phương trình $y’ = 0$ hoặc là vô nghiệm, có nghiệm kép $(1)$; hoặc là có $2$ nghiệm ${x_1} < {x_2}$ thỏa mãn 
$$
\left[ \begin{array}{l}
{x_1} < {x_2} < 0 < 1\\
0 < 1 < {x_1} < {x_2}
\end{array} \right.\left( 2 \right).
$$

Trường hợp $(1)$: Phương trình $y’ = 0$ vô nghiệm hoặc có nghiệm kép $\Leftrightarrow \Delta’ \le 0 \Leftrightarrow 9 – 6m \le 0$ $\Leftrightarrow m \ge \frac{3}{2}.$

Trường hợp $(2)$: Thỏa mãn 
$$
\Leftrightarrow \left[ \begin{array}{l}
\left\{ \begin{array}{l}
\Delta’ > 0\\
{x_1}.{x_2} > 0\\
{x_1} + {x_2} < 0
\end{array} \right.\\
\left\{ \begin{array}{l}
\Delta’ > 0\\
\left( {{x_1} – 1} \right)\left( {{x_2} – 1} \right) > 0\\
\frac{{{x_1} + {x_2}}}{2} > 1
\end{array} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
\left\{ \begin{array}{l}
m < \frac{3}{2}\\
\frac{m}{6} > 0\\
1 < 0
\end{array} \right.\\
\left\{ \begin{array}{l}
m < \frac{3}{2}\\
\frac{m}{6} – 1 + 1 > 0\\
\frac{1}{2} > 1
\end{array} \right.
\end{array} \right.
$$
 (loại).

<!-- chunk:3 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 3: Trong tất cả các giá trị của tham số $m$ để hàm số $y = \frac{1}{3}{x^3} + m{x^2} – mx – m$ đồng biến trên $R$, giá trị nhỏ nhất của $m$ là?

Phân tích: Đây là hàm bậc ba, ta xét $y’ \ge 0, \forall x \in R$, dấu bằng xảy ra tại hữu hạn điểm để tìm giá trị nhỏ nhất của $m.$

Lời giải: Ta có $y’ = {x^2} + 2mx – m$. Để hàm số đã cho luôn đồng biến trên $R$ thì $\Delta’ \le 0$ với mọi $m$ $\Leftrightarrow {m^2} + m \le 0$ $\Leftrightarrow – 1 \le m \le 0$. Vậy giá trị nhỏ nhất của $m$ thỏa mãn là $m = -1$.

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 4: Điều kiện cần và đủ để hàm số $y = \frac{{mx + 5}}{{x + 1}}$ đồng biến trên từng khoảng xác định là?

Phân tích: Hàm số bậc nhất trên bậc nhất có dạng $y = \frac{{ax + b}}{{cx + d}}$ có đạo hàm $y’ = \frac{{ad – bc}}{{{{\left( {cx + d} \right)}^2}}}$ luôn đơn điệu trên từng khoảng xác định (chứ không phải trên tập xác định).

Đồng biến trên từng khoảng xác định khi $ad – bc > 0$, nghịch biến trên từng khoảng xác định khi $ad – bc < 0.$

Lời giải: Ta có $y’ = \frac{{m – 5}}{{{{\left( {x + 1} \right)}^2}}}$. Để hàm số đã cho luôn đồng biến trên từng khoảng xác định thì $m – 5 > 0 \Leftrightarrow m > 5.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 5: Cho hàm số $y = \frac{{mx + 2 – 2m}}{{x + m}} (1)$ ($m$ là tham số). Tìm $m$ để hàm số $(1)$ đồng biến trên từng khoảng xác định.

Phân tích: Một bài toán về hàm phân thức bậc nhất trên bậc nhất nhưng có tham số ở mẫu. Nếu bài toán hỏi “Tìm $m$ để hàm số $(1)$ nghịch biến (hoặc đồng biến) trên một khoảng $\left( {a;b} \right)$ nhất định thì bài toán phải thêm điều kiện, tuy nhiên ở đây ta có thể giải đơn giản như sau:

Lời giải: Điều kiện $x \ne – m.$

Ta có $y’ = \frac{{{m^2} + 2m – 2}}{{{{\left( {x + m} \right)}^2}}}$. Để hàm số đã cho đồng biến trên từng khoảng xác định thì:

${m^2} + 2m – 2 > 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
m > – 1 + \sqrt 3 \\
m < – 1 – \sqrt 3
\end{array} \right.
$$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 6: Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = \frac{{x + 2 – 2m}}{{x + m}}$ đồng biến trên $\left( { – 1;2} \right)$.

Phân tích: Hàm số đơn điệu trên khoảng nào thì phải xác định trên khoảng đó. Do vậy ở đây cần có điều kiện cho $– m \notin \left( { – 1;2} \right)$.

Lời giải: Để hàm số đã cho đồng biến trên $\left( { – 1;2} \right)$ thì $y’ > 0$ với mọi $x \in \left( { – 1;2} \right).$

$$
\Leftrightarrow \left\{ \begin{array}{l}
m – \left( {2 – 2m} \right) > 0\\
– m \notin \left( { – 1;2} \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
3m – 2 > 0\\
\left[ \begin{array}{l}
m \ge 1\\
m \le – 2
\end{array} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m > \frac{2}{3}\\
\left[ \begin{array}{l}
m \ge 1\\
m \le – 2
\end{array} \right.
\end{array} \right. \Leftrightarrow m \ge 1.
$$

Chú ý: Phải có điều kiện $-m$ nằm ngoài khoảng $\left( { – 1;2} \right)$ bởi nếu $-m$ nằm trong khoảng $\left( { – 1;2} \right)$ thì hàm số bị gián đoạn trên $\left( { – 1;2} \right)$. Tức là không thể đồng biến trên $\left( { – 1;2} \right)$ được.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 7: Cho hàm số $y = \frac{{mx + 2m – 3}}{{x – m}}$ ($m$ là tham số). Tìm tất cả các giá trị của $m$ sao cho hàm số nghịch biến trên khoảng $(2; + \infty )$.

Lời giải:

Tập xác định $D = R\backslash \left\{ m \right\}.$

Ta có: $y’ = \frac{{ – {m^2} – 2m + 3}}{{{{\left( {x – m} \right)}^2}}}.$

Hàm số $y = \frac{{mx + 2m – 3}}{{x – m}}$ nghịch biến trên khoảng $(2; + \infty )$ khi và chỉ khi:

$$
\left\{ \begin{array}{l}
y’ < 0\\
m \notin \left( {2; + \infty } \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
– {m^2} – 2m + 3 < 0\\
m \le 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\left[ \begin{array}{l}
m > 1\\
m < – 3
\end{array} \right.\\
m \le 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
1 < m \le 2\\
m < – 3
\end{array} \right.
$$

Phân tích: Ở đây nhiều đọc giả không xét điều kiện để hàm số luôn xác định trên $(2; + \infty )$ là sai.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/02/tim-dieu-kien-tham-so-m-de-ham-so-don-dieu-tren-r-hoac-tren-khoang-con-cua-r.html -->
## Ví dụ 8: Cho hàm số $y = x – \sqrt {{x^2} – x + a}$. Tìm tham số thực $a$ để hàm số luôn nghịch biến trên $R.$

Phân tích: Ở đây để hàm số nghịch biến trên $R$ thì phải xác định trên $R.$ Do vậy ta phải tìm điều kiện để căn thức luôn xác định với mọi số thực $x.$

Lời giải:

Để hàm số xác định với mọi $x \in R \Leftrightarrow {x^2} – x + a \ge 0$, $\forall x \in R$ $\Leftrightarrow \Delta \le 0 \Leftrightarrow 1 – 4a \le 0$ $\Leftrightarrow a \ge \frac{1}{4}$.

Với $a \ge \frac{1}{4}$ thì:

Tính đạo hàm $y’ = 1 – \frac{{2x – 1}}{{2\sqrt {{x^2} – x + a} }}.$

Hàm số đã cho luôn nghịch biến trên $R$ $\Leftrightarrow y’ \le 0,\forall x \in R.$ Dấu bằng xảy ra tại hữu hạn điểm

$\Leftrightarrow 1 – \frac{{2x – 1}}{{2\sqrt {{x^2} – x + a} }} \le 0$ $\Leftrightarrow \frac{{2x – 1}}{{2\sqrt {{x^2} – x + a} }} \ge 1$ $\Leftrightarrow 2x – 1 \ge 2\sqrt {{x^2} – x + a}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \ge \frac{1}{2}\\
1 \ge 4a
\end{array} \right. \Leftrightarrow \left\{ \begin{array}{l}
x \ge \frac{1}{2}\\
a \le \frac{1}{4}
\end{array} \right.
$$

Kết hợp với điều kiện để hàm số xác định với mọi số thực $x$ thì ta thấy không có giá trị nào của $a$ thỏa mãn.

Kết quả: Sau bài toán trên ta thấy, với các bài toán hàm căn thức thì nếu đề bài yêu cầu tìm điều kiện của tham số để hàm số đơn điệu trên $R$ hoặc trên khoảng $I$ nào đó, thì ta cần tìm điều kiện để hàm số luôn xác định trên $R$ hoặc trên khoảng $I$ đó.