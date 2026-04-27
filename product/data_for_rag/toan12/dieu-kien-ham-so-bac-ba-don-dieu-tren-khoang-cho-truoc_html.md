# Điều kiện hàm số bậc ba đơn điệu trên khoảng cho trước

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/dieu-kien-ham-so-bac-ba-don-dieu-tren-khoang-cho-truoc.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm điều kiện hàm số bậc ba đơn điệu trên khoảng cho trước trong chương trình Giải tích 12.

1. PHƯƠNG PHÁP GIẢI TOÁN

Cho hàm số bậc ba $y = a{x^3} + b{x^2} + cx + d$ $(a \ne 0).$ Khi đó:

+ Tập xác định: $D = R.$

+ Đạo hàm: $y’ = 3a{x^2} + 2bx + c.$

a) Hàm số bậc ba đồng biến, nghịch biến trên $R.$

+ Hàm số đồng biến trên $R$ $\Leftrightarrow y’ \ge 0$, $\forall x \in R$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{b^2} – 3ac \le 0}\\
{a > 0}
\end{array}} \right..
$$

+ Hàm số nghịch biến trên $R$ $\Leftrightarrow y’ \le 0$, $\forall x \in R$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{b^2} – 3ac \le 0}\\
{a < 0}
\end{array}} \right..
$$

b) Hàm số bậc ba đồng biến, nghịch biến trên khoảng $(a;b)$ cho trước.

+ Hàm số đồng biến trên $(a;b)$ $\Leftrightarrow y’ \ge 0$, $\forall x \in (a;b).$

+ Hàm số nghịch biến trên $(a;b)$ $\Leftrightarrow y’ \le 0$, $\forall x \in (a;b).$

Phương pháp độc lập tham số (sử dụng khi tách được tham số)

Bước 1: Tách tham số $m$ ở ${y’ \ge 0}$ (hoặc $y’ \le 0$) đưa về dạng $f(x) \ge g(m)$ hoặc $f(x) \le g(m).$

Bước 2: Xét hàm số $y = f(x)$ trên khoảng $(a;b)$, tính đạo hàm, lập bảng biến thiên.

Bước 3: Dựa vào bảng biến thiên của $f(x)$ để suy ra được giá trị của $g(x)$: “lớn hơn giá trị lớn nhất – nhỏ hơn giá trị nhỏ nhất”.

Phương pháp delta (sử dụng khi không tách được tham số)
Xét $\Delta ‘ = {b^2} – 3ac.$

+ Trường hợp 1: $\Delta ‘ \le 0$. Kiểm tra dấu của hệ số $a$ để suy ra hàm số đồng biến, nghịch biến trên $R.$ Đối chiếu yêu cầu bài toán để suy ra giá trị $m.$

+ Trường hợp 2: $\Delta ‘ > 0$. Khi đó $y’ = 0$ có hai nghiệm phân biệt. Lập bảng xét dấu, dựa vào yêu cầu của bài toán để suy ra giá trị $m.$

Lưu ý: Nếu hệ số $a$ phụ thuộc vào tham số, ta cần xét thêm trường hợp $a = 0.$

2. VÍ DỤ MINH HỌA
## Bài 1. Tìm các giá trị của tham số $m$ để hàm số $y = {x^3} – mx + 1$ đồng biến trên $R.$

Ta có $y’ = 3{x^2} – m.$

Hàm số đồng biến trên $R$ $\Leftrightarrow y’ \ge 0$, $\forall x \in R$ $\Leftrightarrow \Delta ‘ = 3m \ge 0$ $\Leftrightarrow m \ge 0.$

## Bài 2. Tìm các giá trị của tham số $m$ để hàm số $y = (m – 2){x^3} – (2m – 1){x^2} – x + m – 1$ nghịch biến trên $R.$

Với $m = 2$, hàm số trở thành $y = – 3{x^2} – x + 1.$ Hàm số bậc hai không thể nghịch biến trên $R.$ Do đó $m = 2$ không thỏa mãn bài toán.

Với $m \ne 2$, ta có $y’ = 3(m – 2){x^2} – 2(2m – 1)x – 1.$

Hàm số nghịch biến trên $R$ $\Leftrightarrow y’ \le 0$, $\forall x \in R.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = m – 2 < 0}\\
{\Delta ‘ = {{(2m – 1)}^2} + 3(m – 2) \le 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 2}\\
{4{m^2} – m – 5 \le 0}
\end{array}} \right.
$$
 $\Leftrightarrow – 1 \le m \le \frac{5}{4}.$

Vậy $m \in \left[ { – 1;\frac{5}{4}} \right].$

## Bài 3. Tìm điều kiện của tham số $m$ để hàm số $y = {x^3} – m{x^2} + (m + 6)x – 1$ đồng biến trên khoảng $(1; + \infty ).$

Ta có $y’ = 3{x^2} – 2mx + m + 6.$

Hàm số đồng biến trên $(1; + \infty )$ $\Leftrightarrow y’ \ge 0$, $\forall x \in (1; + \infty ).$

$\Leftrightarrow m \le \frac{{3{x^2} + 6}}{{2x – 1}}$, $\forall x \in (1; + \infty ).$

Xét $g(x) = \frac{{3{x^2} + 6}}{{2x – 1}}$ với $x \in (1; + \infty ).$

Ta có $g'(x) = \frac{{6{x^2} – 6x – 12}}{{{{(2x – 1)}^2}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 2}
\end{array}} \right..
$$

<img link="data_for_rag/toan12/images/dieu-kien-ham-so-bac-ba-don-dieu-tren-khoang-cho-truoc-1.png" alt="">

Từ bảng biến thiên ta suy ra $m \le 6.$

## Bài 4. Tìm điều kiện của tham số $m$ để hàm số $y = m{x^3} – {x^2} + 3x + m – 2$ đồng biến trên khoảng $(-3;0).$

Với $m = 0$: hàm số $y = – {x^2} + 3x – 2$ đồng biến trên $\left( { – \infty ;\frac{3}{2}} \right).$

Suy ra $m = 0$ thỏa bài toán.

Với $m \ne 0$: $y’ = 3m{x^2} – 2x + 3.$

Hàm số đồng biến trên $( – 3;0)$ $\Leftrightarrow y’ \ge 0$, $\forall x \in ( – 3;0).$

$\Leftrightarrow m \ge \frac{{2x – 3}}{{3{x^2}}}$, $\forall x \in ( – 3;0).$

Xét $g(x) = \frac{{2x – 3}}{{3{x^2}}}$ với $x \in ( – 3;0).$

Ta có $g'(x) = \frac{{ – 2x + 6}}{{3{x^3}}} < 0$, $\forall x \in ( – 3;0).$

<img link="data_for_rag/toan12/images/dieu-kien-ham-so-bac-ba-don-dieu-tren-khoang-cho-truoc-2.png" alt="">

Từ bảng biến thiên suy ra $m \ge – \frac{1}{3}.$

## Bài 5. Tìm điều kiện của tham số $m$ để hàm số $y = {x^3} – (m + 1){x^2} – \left( {{m^2} – 2m} \right)x + 2{m^2} – m$ nghịch biến trên khoảng $(1;2).$

Ta có $y’ = 3{x^2} – 2(m + 1)x – \left( {{m^2} – 2m} \right)$ $= (x – m)(3x + m – 2).$

Khi đó $y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = m}\\
{x = \frac{{2 – m}}{3}}
\end{array}} \right..
$$

Yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \le 1}\\
{\frac{{2 – m}}{3} \ge 2}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{m \ge 2}\\
{\frac{{2 – m}}{3} \le 1}
\end{array}} \right.
$$
 $\Leftrightarrow m \le – 4$ hoặc $m \ge 2.$

## Bài 6. Tìm điều kiện của tham số $m$ để hàm số $y = {x^3} + 3{x^2} + (m + 1)x + 4m$ nghịch biến trên khoảng $(-1;1).$

Ta có $y’ = 3{x^2} + 6x + m + 1$ có $\Delta ‘ = 6 – 3m.$

Trường hợp 1: $\Delta ‘ \le 0$ $\Leftrightarrow m \ge 2$, hàm số đồng biến trên $R$ $\Rightarrow m \ge 2$ không thỏa bài toán.

Trường hợp 2: $\Delta ‘ > 0$ $\Leftrightarrow m < 2$, $y’ = 0$ có hai nghiệm phân biệt $x = – 1 \pm \frac{{\sqrt {6 – 3m} }}{3}.$

Yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 – \frac{{\sqrt {6 – 3m} }}{3} \le – 1}\\
{ – 1 + \frac{{\sqrt {6 – 3m} }}{3} \ge 1}
\end{array}} \right.
$$
 $\Leftrightarrow m \le – 10.$

Vậy $m \le – 10.$

## Bài 7. Tìm điều kiện của tham số $m$ để hàm số $y = {x^3} + 3{x^2} + mx + m$ nghịch biến trên đoạn có độ dài bằng $1.$

Ta có $y’ = 3{x^2} + 6x + m$ có $\Delta ‘ = 9 – 3m.$

Yêu cầu bài toán $\Leftrightarrow y’ = 0$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ thỏa $\left| {{x_1} – {x_2}} \right| = 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ > 0}\\
{{{\left( {{x_1} + {x_2}} \right)}^2} – 4{x_1}{x_2} = 1}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{9 – 3m > 0}\\
{4 – \frac{{4m}}{3} = 1}
\end{array}} \right..
$$

$\Leftrightarrow m = \frac{9}{4}.$

## Bài tập
## Bài 1. Tìm tất cả giá trị của tham số $m$ để hàm số $y = \frac{1}{3}{x^3} – 2m{x^2} + 4x – 5$ đồng biến trên $R.$

A. $– 1 < m < 1.$

B. $– 1 \le m \le 1.$

C. $0 \le m \le 1.$

D. $0 < m < 1.$

Hàm số đồng biến trên $R$ khi ${b^2} – 3ac = 4{m^2} – 4 \le 0$ $\Leftrightarrow – 1 \le m \le 1.$

> **Đáp án: B**

## Bài 2. Tìm tập hợp các giá trị của tham số $m$ để hàm số $y = {x^3} + 3{x^2} + mx + m$ đồng biến trên $R.$

A. $[3; + \infty ).$

B. $( – \infty ;3).$

C. $R.$

D. $\emptyset .$

Hàm số đồng biến trên $R$ khi ${b^2} – 3ac = 9 – 3m \le 0$ $\Leftrightarrow m \ge 3.$

> **Đáp án: A**

## Bài 3. Tìm tất cả các giá trị của tham số $m$ để hàm số $y = – {x^3} + 2{x^2} – (m – 1)x + 2$ nghịch biến trên $R.$

A. $m \ge \frac{7}{3}.$

B. $m \le \frac{7}{3}.$

C. $m > \frac{7}{3}.$

D. $m \ge \frac{1}{3}.$

Hàm số nghịch biến trên $R$ khi ${b^2} – 3ac = 7 – 3m \le 0$ $\Leftrightarrow m \ge \frac{7}{3}.$

> **Đáp án: A**

## Bài 4. Tìm tất cả các giá trị của tham số $m$ để hàm số: $y = – \frac{1}{3}{x^3} + (m + 2){x^2} + mx – 7$ nghịch biến trên $R.$

A. $m \le – 4.$

B. $m \le – 1.$

C. $m \le – 4$ hoặc $m \ge – 1.$

D. $– 4 \le m \le – 1.$

Hàm số nghịch biến trên $R$ khi ${b^2} – 3ac = {(m + 2)^2} + m \le 0$ $\Leftrightarrow – 4 \le m \le – 1.$

> **Đáp án: D**

## Bài 5. Tìm tất cả các giá trị của tham số $m$ để hàm số: $y = (m – 1){x^3} + (m – 1){x^2} + x + m$ đồng biến trên $R.$

A. $m < 1$ hoặc $m \ge 4.$

B. $1 < m \le 4.$

C. $1 < m < 4.$

D. $1 \le m \le 4.$

Với $m = 1$: hàm số $y = x + 1$ đồng biến trên $R$, suy ra $m = 1$ thỏa bài toán.

Với $m \ne 1$: Hàm số đồng biến trên $R$ khi:

$$
\left\{ {\begin{array}{l}
{a = m – 1 > 0}\\
{{b^2} – 3ac = {{(m – 1)}^2} – 3(m – 1) \le 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > 1}\\
{1 \le m \le 4}
\end{array}} \right.
$$
 $\Leftrightarrow 1 < m \le 4.$

Vậy $1 \le m \le 4.$

> **Đáp án: D**

## Bài 6. Tìm tất cả các giá trị của tham số $m$ để hàm số: $y = \left( {{m^2} – 1} \right)\frac{{{x^3}}}{3} + (m + 1){x^2} + 3x – 1$ đồng biến trên $R.$

A. $m \le – 1$ hoặc $m \ge 1.$

B. $m < – 1$ hoặc $m \ge 1.$

C. $m < – 1$ hoặc $m \ge 2.$

D. $m \le – 1$ hoặc $m \ge 2.$

Với $m = 1$: hàm số $y = 2{x^2} + 3x – 1$ không thỏa bài toán.

Với $m = -1$: hàm số $y = 3x -1$ đồng biến trên $R$, suy ra $m = – 1$ thỏa bài toán.

Với $m \ne \pm 1$: Hàm số đồng biến trên $R$ khi:

$$
\left\{ {\begin{array}{l}
{a = {m^2} – 1 > 0}\\
{{b^2} – 3ac = {{(m + 1)}^2} – 3\left( {{m^2} – 1} \right) \le 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\left[ {\begin{array}{l}
{m < – 1}\\
{m > 1}
\end{array}} \right.}\\
{\left[ {\begin{array}{l}
{m \le – 1}\\
{m \ge 2}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m < – 1}\\
{m \ge 2}
\end{array}} \right..
$$

Vậy $m \le – 1$ hoặc $m \ge 2.$

> **Đáp án: D**

## Bài 7. Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \frac{1}{3}{x^3} – (m – 1){x^2} – 4mx$ đồng biến trên $[1;4].$

A. $m \le \frac{1}{2}.$

B. $m \in R.$

C. $\frac{1}{2} < m < 2.$

D. $m \le 2.$

Hàm số đồng biến trên $[1;4]$ khi:

$y’ = {x^2} – 2(m – 1)x – 4m \ge 0$, $\forall x \in [ – 1;4]$ $\Leftrightarrow m \le \frac{x}{2}$, $\forall x \in [ – 1;4]$ $\Leftrightarrow m \le – \frac{1}{2}.$

> **Đáp án: A**

## Bài 8. Tìm các giá trị của $m$ để hàm số $y = \frac{1}{3}{x^3} – m{x^2} + (2m – 1)x – m + 2$ nghịch biến trên khoảng $(-2;0).$

A. $m < – \frac{1}{2}.$

B. $m \le – \frac{1}{2}.$

C. $m > 1.$

D. $m = 0.$

Hàm số đồng biến trên $(-2;0)$ khi:

$y’ = {x^2} – 2mx + 2m – 1 \le 0$, $\forall x \in ( – 2;0)$ $\Leftrightarrow m \le \frac{{x + 1}}{2}$, $\forall x \in ( – 2;0)$ $\Leftrightarrow m \le – \frac{1}{2}.$

> **Đáp án: B**

## Bài 9. Tìm tất cả giá trị thực của $m$ để hàm số $y = {x^3} – 6{x^2} + mx + 1$ đồng biến trên $(0; + \infty ).$

A. $m \ge 0.$

B. $m \le 0.$

C. $m \ge 12.$

D. $m \le 12.$

Hàm số đồng biến trên $R$ khi:

$y’ = 3{x^2} – 12x + m \ge 0$, $\forall x \in (0; + \infty )$ $\Leftrightarrow m \ge – 3{x^2} + 12x$, $\forall x \in (0; + \infty ).$

Xét $g(x) = – 3{x^2} + 12x$ trên $(0; + \infty ).$

Lập bảng biến thiên ta suy ra $m \ge 12.$

> **Đáp án: C**

## Bài 10. Tìm các giá trị của $m$ để hàm số $y = – \frac{1}{3}{x^3} + (m – 1){x^2} + (m + 3)x – 10$ đồng biến trên khoảng $(0;3).$

A. $m = 0.$

B. $m \le \frac{{12}}{7}.$

C. $m \ge \frac{{12}}{7}.$

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/dieu-kien-ham-so-bac-ba-don-dieu-tren-khoang-cho-truoc.html -->
## D. Mọi giá trị $m.$

Hàm số đồng biến trên $R$ khi:

$y’ = – {x^2} + 2(m – 1)x + m + 3 \ge 0$, $\forall x \in (0;3)$ $\Leftrightarrow m \ge \frac{{{x^2} + 2x – 3}}{{2x + 1}}$, $\forall x \in (0;3).$

Xét $g(x) = \frac{{{x^2} + 2x – 3}}{{2x + 1}}$ $\Rightarrow g'(x) = \frac{{2{x^2} + 2x + 8}}{{{{(2x + 1)}^2}}} > 0$, $\forall x \in (0;3).$

Suy ra $m \ge g(3) = \frac{{12}}{7}.$

> **Đáp án: C**

## Bài 11. Cho hàm số $y = {x^3} – 3(m + 2){x^2} + 3\left( {{m^2} + 4m} \right)x + 1.$ Có bao nhiêu giá trị nguyên của tham số $m$ để hàm số nghịch biến trên khoảng $(0;1).$

A. $1.$

B. $4.$

C. $3.$

D. $2.$

Ta có $y’ = 3{x^2} – 6(m + 2)x + 3\left( {{m^2} + 4m} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = m}\\
{x = m + 4}
\end{array}} \right..
$$

Yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \le 0}\\
{m + 4 \ge 1}
\end{array}} \right.
$$
 $\Leftrightarrow – 3 \le m \le 0$. Vì $m \in Z$ nên $m \in \{ – 3; – 2; – 1;0\} .$

> **Đáp án: B**

## Bài 12. Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = {x^3} – 3m{x^2} – 9{m^2}x$ nghịch biến trên $(0;1).$

A. $m \ge \frac{1}{3}.$

B. $m \le – 1.$

C. $m \ge \frac{1}{3}$ hoặc $m \le – 1.$

D. $– 1 \le m \le 3.$

Ta có $y’ = 3{x^2} – 6mx – 9{m^2}$ $= 3(x + m)(x – 3m) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – m}\\
{x = 3m}
\end{array}} \right..
$$

+ Với $m = 0$, ta có $y’ = 3{x^2} \ge 0$, $\forall x \in R$ nên hàm số đồng biến trên $R.$

Do đó $m = 0$ không thỏa bài toán.

+ Với $m \ne 0$:

Với $m > 0$: yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – m \le 0}\\
{3m \ge 1}
\end{array}} \right.
$$
 $\Leftrightarrow m \ge \frac{1}{3}$ (thỏa mãn).

Với $m < 0$, yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – m \ge 1}\\
{3m \le 0}
\end{array}} \right.
$$
 $\Leftrightarrow m \le – 1$ (thỏa mãn).

Vậy $m \ge \frac{1}{3}$ hoặc $m \le – 1.$

> **Đáp án: C**

## Bài 13. Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = {x^3} + 3{x^2} + mx + m$ nghịch biến trên một khoảng có độ dài bằng $1.$

A. $m = \frac{9}{4}.$

B. $m = – \frac{9}{4}.$

C. $m = \frac{9}{2}.$

D. $m = – \frac{9}{2}.$

Ta có $y’ = 3{x^2} + 6x + m.$

Yêu cầu bài toán $\Leftrightarrow y’ = 0$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ thỏa $\left| {{x_1} – {x_2}} \right| = 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta {‘_{y’}} = {b^2} – 3ac = 9 – 3m > 0}\\
{{{\left( {{x_1} + {x_2}} \right)}^2} – 4{x_1}{x_2} = 4 – \frac{{4m}}{3} = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 3}\\
{m = \frac{9}{4}}
\end{array}} \right.
$$
 $\Leftrightarrow m = \frac{9}{4}.$

> **Đáp án: A**

## Bài 14. Tìm tất cả các giá trị thực của tham số $m$ để hàm số $y = {x^3} – 3(2m + 1){x^2} + (m + 1)x + 2$ nghịch biến trên đoạn có độ dài bằng $2.$

A. $m = – \frac{1}{{12}}$ hoặc $m = – 1.$

B. $m = – \frac{1}{{12}}$ hoặc $m = 1.$

C. $m = \frac{1}{{12}}$ hoặc $m = – 1.$

D. $m = \frac{1}{{12}}$ hoặc $m = 1.$

Ta có $y’ = 3{x^2} – 6(2m + 1)x + m + 1.$

Yêu cầu bài toán $\Leftrightarrow y’ = 0$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ thỏa $\left| {{x_1} – {x_2}} \right| = 2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta {‘_{y’}} = {b^2} – 3ac = 9{{(2m + 1)}^2} – 3(m + 1) > 0}\\
{{{\left( {{x_1} + {x_2}} \right)}^2} – 4{x_1}{x_2} = 4{{(2m + 1)}^2} – \frac{{4(m + 1)}}{3} = 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – 1}\\
{m = \frac{1}{{12}}}
\end{array}} \right..
$$

> **Đáp án: C**