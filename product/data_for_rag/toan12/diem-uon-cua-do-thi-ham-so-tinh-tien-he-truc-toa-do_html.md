# Điểm uốn của đồ thị hàm số - Tịnh tiến hệ trục tọa độ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
Bài viết trình bày lý thuyết và một số dạng toán cơ bản về các chủ đề: điểm uốn của đồ thị hàm số, tịnh tiến hệ trục tọa độ trong chương trình Giải tích 12.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## I. KHÁI NIỆM ĐIỂM UỐN CỦA ĐỒ THỊ

Điểm $U\left( {{x_0};f\left( {{x_0}} \right)} \right)$ được gọi là điểm uốn của đồ thị hàm số $f(x)$ nếu tồn tại một khoảng $(a;b)$ chứa điểm ${x_0}$ sao cho trên một trong hai khoảng $\left( {a;{x_0}} \right)$ và $\left( {{x_0};b} \right)$ tiếp tuyến của đồ thị tại điểm $U$ nằm phía trên đồ thị và trên khoảng kia tiếp tuyến nằm phía dưới đồ thị.

<img link="data_for_rag/toan12/images/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do-1.png" alt="">

Định lý: Nếu hàm số $y = f(x)$ có đạo hàm cấp hai trên một khoảng chứa điểm ${x_0}$, $f”\left( {{x_0}} \right) = 0$ và $f”(x)$ đổi dấu khi $x$ qua điểm ${x_0}$ thì điểm $U\left( {{x_0};f\left( {{x_0}} \right)} \right)$ là một điểm uốn của đồ thị hàm số $y = f(x).$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## II. TỊNH TIẾN HỆ TỌA ĐỘ

1. Công thức chuyển hệ tọa độ

Giả sử $I$ là một điểm của mặt phẳng và $\left( {{x_0};{y_0}} \right)$ là tọa độ của điểm $I$ đối với hệ tọa độ $Oxy.$

Gọi $IXY$ là hệ tọa độ mới có gốc là điểm $I$ và hai trục là $IX$, $IY$ theo thứ tự có cùng các vectơ đơn vị $\overrightarrow i$, $\overrightarrow j$ với hai trục $Ox$, $Oy.$

Giả sử $M$ là một điểm bất kỳ của mặt phẳng.

$(x;y)$ là tọa độ của điểm $M$ đối với hệ tọa độ $Oxy.$

$(X;Y)$ là tọa độ của điểm $M$ đối với hệ tọa độ $IXY.$

Khi đó ta có công thức chuyển hệ tọa độ trong phép tịnh tiến theo $\overrightarrow {OI}$ là:

$$
\left\{ {\begin{array}{l}
{x = X + {x_0}}\\
{y = Y + {y_0}}
\end{array}} \right.
$$

2. Phương pháp tìm phương trình của đường cong đối với hệ tọa độ mới

Trong hệ trục tọa độ $Oxy$, cho hàm số $y = f(x)$ có đồ thị là $(C).$

Tịnh tiến hệ trục $Oxy$ về hệ trục $IXY$ theo vectơ $\overrightarrow {OI}$, công thức chuyển hệ trục là: 
$$
\left\{ {\begin{array}{l}
{x = X + {x_I}}\\
{y = Y + {y_I}}
\end{array}} \right. .
$$

Thay $x$, $y$ vào phương trình của $(C)$ ta thu được phương trình $Y = F(X).$

Suy ra trong hệ trục $IXY$, $(C)$ có phương trình là $Y = F(X).$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Vấn đề 1: Tìm điểm uốn của đồ thị $(C)$ của hàm số $y = f(x).$

1. PHƯƠNG PHÁP

Tìm tập xác định.

Tìm $y’$ và $y”.$

Xét dấu $y”$ và kết luận theo định lí trên.

2. CÁC VÍ DỤ

Ví dụ: Tìm điểm uốn của đồ thị các hàm số:

a) $y = {x^3} – 3{x^2} + 3.$

b) $y = 3{x^5} – 5{x^4} + 3x + 1.$

a) Tập xác định: $D = R.$

$y’ = 3{x^2} – 6x.$

$y” = 6x – 6.$

$y” = 0$ $\Leftrightarrow x = 1 \Rightarrow y = 1.$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do-2.png" alt="">

Vậy đồ thị có một điểm uốn là $U(1;1).$

b) Tập xác định: $D = R.$

$y’ = 15{x^4} – 20{x^3} + 3.$

$y” = 60{x^3} – 60{x^2} = 60{x^2}(x – 1).$

$$
y” = 0 \Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \Rightarrow y = 1}\\
{x = 1 \Rightarrow y = 2}
\end{array}} \right..
$$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do-3.png" alt="">

Vậy đồ thị có một điểm uốn là $U(1;2).$

## Bài tập

Tìm điểm uốn của các đồ thị hàm số:

a) $y = {x^3} – 6{x^2} – 3x + 5.$

b) $y = 2{x^4} – 12{x^2} + 5.$

c) $y = – {x^4} – 3{x^2} + 4.$

d) $y = 3{x^5} – 5{x^4} – 4x + 5.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Vấn đề 2: Chứng minh đồ thị có 3 điểm uốn thẳng hàng.

1. PHƯƠNG PHÁP

Tìm $y”$ và chứng tỏ phương trình $y” = 0$ có $3$ nghiệm (đơn) phân biệt.

Suy ra đồ thị có $3$ điểm uốn $A$, $B$ và $C.$

Chứng minh $\overrightarrow {AB}$ và $\overrightarrow {AC}$ cùng phương, suy ra $A$, $B$, $C$ thẳng hàng.

Chú ý nếu phương trình $y” = 0$ không xác định được nghiệm cụ thể thì ta chứng minh $A$, $B$, $C$ thẳng hàng như sau:

Tọa độ $A$, $B$, $C$ thỏa hệ: 
$$
\left\{ {\begin{array}{l}
{y” = 0}\\
{y = f(x)}
\end{array}} \right..
$$

Từ hệ trên ta suy ra $x$, $y$ thỏa phương trình $y = ax + b.$ Từ đó suy ra $A$, $B$, $C$ cùng thuộc đường thẳng có phương trình $y = ax + b.$

2. CÁC VÍ DỤ
Ví dụ: Chứng minh rằng đồ thị hàm số sau có $3$ điểm uốn thẳng hàng: $y = \frac{{2x – 3}}{{{x^2} – 3x + 3}}.$

Tập xác định: $D = R.$

$y’ = \frac{{ – 2{x^2} + 6x – 3}}{{{{\left( {{x^2} – 3x + 3} \right)}^2}}}.$

$y” = \frac{{(4x – 6)\left( {{x^2} – 3x} \right)}}{{{{\left( {{x^2} – 3x + 3} \right)}^3}}}.$

$y” = 0$ $\Leftrightarrow (2x – 3)\left( {{x^2} – 3x} \right) = 0$ $\Leftrightarrow x = 0$ hoặc $x = 3$ hoặc $x = \frac{3}{2}.$

Vậy đồ thị hàm số có ba điểm uốn là $A(0; -1)$, $B(3; 1)$ và $C\left( {\frac{3}{2};0} \right).$

Để chứng minh ba điểm uốn thẳng hàng ta sử dụng một số cách sau:

Cách 1: $M(x;y)$ là điểm uốn, suy ra $x$, $y$ thỏa hệ: 
$$
\left\{ {\begin{array}{l}
{y = \frac{{2x – 3}}{{{x^2} – 3x + 3}}}\\
{(2x – 3)\left( {{x^2} – 3x} \right) = 0}
\end{array}} \right..
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{y = \frac{{2x – 3 + a(2x – 3)\left( {{x^2} – 3x} \right)}}{{{x^2} – 3x + 3}} = \alpha x + \beta }\\
{(2x – 3)\left( {{x^2} – 3x} \right) = 0}
\end{array}} \right. .
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{y = \frac{{2x – 3 + a(2x – 3)\left( {{x^2} – 3x} \right)}}{{{x^2} – 3x + 3}} = \alpha x + \beta }\\
{x = 0\:{\rm{hay}}\:x = 3\:{\rm{hay}}\:x = \frac{3}{2}}
\end{array}} \right. .
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\beta = – 1}\\
{3\alpha = 2}\\
{2a – 1 = \alpha + \beta }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\alpha = \frac{2}{3}}\\
{\beta = – 1}\\
{a = \frac{1}{3}}
\end{array}} \right..
$$

$\Rightarrow y = \frac{2}{3}x – 1$ là phương trình đường thẳng qua ba điểm uốn của đồ thị.

Cách 2: Gọi $A$, $B$, $C$ là ba điểm uốn của đồ thị hàm số.

Giả sử $A$, $B$, $C$ thuộc đường thẳng $y = ax + b.$ Ta có hoành độ $A$, $B$, $C$ thỏa phương trình:

$\frac{{2x – 3}}{{{x^2} – 3x + 3}} = ax + b$ $\Leftrightarrow (ax + b)\left( {{x^2} – 3x + 3} \right) = 2x – 3$ $\Leftrightarrow a{x^3} + (b – 3a){x^2}$ $+ (3a – 3b – 2)x + 3b + 3 = 0$ $(1).$

Ta có: $y” = 0$ $\Leftrightarrow 2{x^3} – 9{x^2} + 9x = 0$ $(2).$

Vì $(1)$ và $(2)$ cùng có ba nghiệm là ${x_A}$, ${x_B}$ và ${x_C}$ nên ta có (các hệ số tương ứng tỉ lệ):

$a:(b – 3a):(3a – 3b – 2):(3b + 3)$ $= 2:( – 9):9:0.$

$\Rightarrow b = – 1$ và $\frac{a}{2} = \frac{{b – 3a}}{{ – 9}} = \frac{{3a – 3b – 2}}{9}$ $\Rightarrow b = – 1$, $a = \frac{2}{3}.$

$\Rightarrow y = \frac{2}{3}x – 1$ là phương trình đường thẳng qua ba điểm uốn của đồ thị.

Cách 3: Ta có đồ thị hàm số có ba điểm uốn là $A(0;-1)$, $B(3;1)$ và $C\left( {\frac{3}{2};0} \right).$

Do đó: $\overrightarrow {AB} = (3;2)$, $\overrightarrow {AC} = \left( {\frac{3}{2};1} \right).$ $\overrightarrow {AB} = 2\overrightarrow {AC}$ $\Rightarrow A$, $B$, $C$ thẳng hàng.

## Bài tập
## Bài tập 1. Chứng minh rằng đồ thị các hàm số sau có $3$ điểm uốn thẳng hàng:

a) $y = \frac{{2x + 1}}{{{x^2} + x + 1}}.$

b) $y = \frac{{x + 1}}{{{x^2} + 1}}.$

c) $y = \frac{{{x^2} – x + 2}}{{{x^2} – 2x + 2}}.$

## Bài tập 2. Chứng minh rằng các điểm uốn của đường cong $(C):y = x.\sin x$ nằm trên đường cong $(E):{y^2}\left( {4 + {x^2}} \right) = 4{x^2}.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Vấn đề 3: Tìm điều kiện của tham số để đồ thị có điểm uốn thỏa mãn điều kiện cho trước.

1. PHƯƠNG PHÁP

Tìm $y’$, $y”.$

Tìm điểm uốn của đồ thị hàm số.

Đặt điều kiện để điểm uốn thỏa mãn điều kiện cho trước, từ đó suy ra giá trị của tham số.

2. CÁC VÍ DỤ

<!-- chunk:6 level:3 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Ví dụ 1: Tìm giá trị của tham số để đồ thị hàm số $y = a{x^3} + b{x^2} – 3x + 2$ có điểm uốn là $I(1;3).$

Tập xác định: $D = R.$

$y’ = 3a{x^2} + 2bx – 3.$

$y” = 6ax + 2b.$

$I$ là điểm uốn của đồ thị hàm số 
$$
\Rightarrow \left\{ {\begin{array}{l}
{y”(1) = 0}\\
{y(1) = 3}
\end{array}} \right..
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{6a + 2b = 0}\\
{a + b – 3 + 2 = 3}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{a = – 2}\\
{b = 6}
\end{array}} \right..
$$

Khi đó $y = – 2{x^3} + 6{x^2} – 3x + 2$, $y” = – 12x + 12.$

Ta có: $y” = 0$ $\Leftrightarrow x = 1 \Rightarrow y = 3.$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do-4.png" alt="">

Vậy đồ thị nhận $U(1;3)$ làm điểm uốn.

Suy ra $a = -2$ và $b=3$ thỏa yêu cầu bài toán.

<!-- chunk:7 level:3 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Ví dụ 2: Tìm $m$ để đồ thị $(C)$ của hàm số $y = f(x) = – \frac{{{x^3}}}{m} + 3m{x^2} – 2$ có điểm uốn nằm trên đường parabol $(P):y = 2{x^2} – 2.$

Ta chỉ xét $m \ne 0.$

$f'(x) = – \frac{3}{m}{x^2} + 6mx.$

$f”(x) = – \frac{{6x}}{m} + 6m$, $f”(x) = 0 \Leftrightarrow x = {m^2}.$

Với $m \ne 0$, $(C)$ có điểm uốn $U\left( {{m^2};2{m^5} – 1} \right).$

Ta có: $U \in (P)$ $\Leftrightarrow 2{m^5} – 1 = 2{m^4} – 1$ $\Leftrightarrow {m^4}(m – 1) = 0$ $\Leftrightarrow m = 1$ (do $m \ne 0$).

Vậy: Đồ thị $(C)$ của hàm số đã cho có điểm uốn nằm trên $(P)$ $\Leftrightarrow m = 1.$

## Bài tập

## Bài tập 1. Tìm $m$ để đồ thị hàm số $y = {x^3} – 3{x^2} + 3mx + 3m + 4$ có điểm uốn nằm trên đường thẳng $(d):y = 5x + 9.$

## Bài tập 2. Tìm $a$ để đồ thị hàm số $y = {x^4} – (a – 1){x^2} + 3.$

a) Có hai điểm uốn.

b) Không có điểm uốn.

## Bài tập 3. Cho hàm số $y = {x^3} – 3{x^2} – 9x + 6.$ Chứng minh rằng trong tất cả các tiếp tuyến với đồ thị hàm số, tiếp tuyến tại điểm uốn có hệ số góc nhỏ nhất.

## Bài tập 4. Tìm $a$, $b$ để đồ thị hàm số:

a) $y = {x^3} – a{x^2} + x + b$ nhận điểm $I(1; 4)$ làm điểm uốn.

b) $y = a{x^3} + b{x^2}$ nhận điểm $I(1; 8)$ là điểm uốn.

c) $y = a{x^3} + b{x^2} + x + 1$ nhận điểm $I(1;-2)$ là điểm uốn.

d) $y = {x^3} – 3{x^2} + 3mx + 3m + 4$ nhận điểm $I(1,2)$ làm điểm uốn.

<!-- chunk:8 level:2 source:https://toanmath.com/2019/05/diem-uon-cua-do-thi-ham-so-tinh-tien-he-truc-toa-do.html -->
## Vấn đề 4: Công thức chuyển hệ trục tọa độ và áp dụng.
1. PHƯƠNG PHÁP

Công thức chuyển hệ trục $Oxy$ về hệ trục $IXY$ theo vectơ $\overrightarrow {OI}$ là:

$$
\left\{ {\begin{array}{l}
{x = X + {x_0}}\\
{y = Y + {y_0}}
\end{array}} \right..
$$

Phương trình của đường $(C): y = f(x)$ đối với hệ tọa độ mới $IXY:$

$Y = f\left( {X + {x_0}} \right) – {y_0}.$

Chú ý:

+ Đồ thị hàm số lẻ nhận gốc tọa độ làm tâm đối xứng.

+ Đồ thị hàm số chẵn nhận trục tung làm trục đối xứng.

2. CÁC VÍ DỤ 

Ví dụ: Cho hàm số $y = {x^3} – 3{x^2} + 4$ có đồ thị là $(C).$

a) Tìm điểm uốn $I$ của đồ thị hàm số.

b) Viết công thức chuyển hệ trục trong phép tịnh tiến theo $\overrightarrow {OI}$ và tìm phương trình của $(C)$ đối với hệ tọa độ $IXY.$

c) Từ đó suy ra rằng $I$ là tâm đối xứng của $(C).$

a) Tập xác định: $D = R.$

$y’ = 3{x^2} – 6x.$

$y” = 6x – 6.$

$y” = 0 \Leftrightarrow x = 1 \Rightarrow y = 2.$

Ta có $y”$ đổi dấu khi qua $x = 1$ nên đồ thị có điểm uốn là $I(1;2).$

b) Công thức chuyển hệ tọa độ trong phép tịnh tiến theo $\overrightarrow {OI}$ là:

$$
\left\{ {\begin{array}{l}
{x = X + {x_I} = X + 1}\\
{y = Y + {y_I} = Y + 2}
\end{array}} \right..
$$

Phương trình của $(C)$ đối với hệ tọa độ $IXY$ là:

$Y = f\left( {X + {x_I}} \right) – {y_I}$ $= f(X + 1) – 2.$

$\Leftrightarrow Y = {(X + 1)^3} – 3{(X + 1)^2} + 4 – 2.$

$\Leftrightarrow Y = {X^3} – 3X = F(X).$

c) Hàm số $Y = F(X) = {X^3} – 3X$ có:

Tập xác định là ${D_F} = R$ nên $X \in {D_F} \Rightarrow – X \in {D_F}.$

$F( – X) = – {X^3} + 3X$ $= – F(X)$ $\forall X \in {D_F}.$

Vậy $F(X)$ là hàm số lẻ.

Suy ra đồ thị $(C)$ nhận $I$ là tâm đối xứng.

## Bài tập
## Bài tập 1. Cho đường cong $(C):y = 3 – \frac{1}{{x – 2}}$ và điểm $I(2; 3).$ Viết công thức chuyển hệ tọa độ trong phép tịnh tiến theo $\overrightarrow {OI}$ và viết phương trình của đường cong $(C)$ đối với hệ tọa độ $IXY.$ Từ đó suy ra $I$ là tâm đối xứng của đường cong $(C).$

## Bài tập 2. Chứng minh đồ thị:

a) Hàm số $y = \frac{{5x – 2}}{{x – 1}}$ nhận điểm $I(1;5)$ làm tâm đối xứng.

b) Hàm số $y = {x^4} – 4{x^3} – {x^2} + 10x + 5$ có trục đối xứng vuông góc với $Ox.$

c) Hàm số $y = {(x – 2a)^2}{(x + 2)^2}$ có trục đối xứng vuông góc trục $Ox.$