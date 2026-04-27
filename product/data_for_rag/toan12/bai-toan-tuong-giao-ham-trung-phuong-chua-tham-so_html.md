# Bài toán tương giao hàm trùng phương chứa tham số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
Bài viết hướng dẫn phương pháp tìm điều kiện tham số liên quan đến bài toán tương giao hàm trùng phương trong chương trình Giải tích 12: ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN

Cho hàm số trùng phương có dạng: $y = f(x) = a{x^4} + b{x^2} + c$ $(C)$ (điều kiện $a \ne 0$).

Phương trình hoành độ giao điểm của đồ thị hàm số với trục hoành là:

$a{x^4} + b{x^2} + c = 0$ $(1).$

Đặt $t = {x^2} \ge 0$, $\forall x \in R.$

Phương trình $(1)$ trở thành: $a{t^2} + bt + c = 0$ $(2).$

Số giao điểm của đồ thị $(C)$ với trục $Ox$
**Điều kiện** | 
**Đồ thị minh họa** | 

Có bốn giao điểm phân biệt | 
Phương trình $(2)$ có hai nghiệm phân biệt dương 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {b^2} – 4ac > 0}\\
{ – \frac{b}{a} > 0,\frac{c}{a} > 0}
\end{array}} \right.
$$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so-1.png" alt="">
 | 

Có ba giao điểm phân biệt | 
Phương trình $(2)$ có một nghiệm bằng $0$ và nghiệm còn lại dương 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{c = 0}\\
{ – \frac{b}{a} > 0}
\end{array}} \right.
$$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so-2.png" alt="">
 | 

Có hai giao điểm phân biệt | 
Phương trình $(2)$ có một nghiệm dương và nghiệm còn lại âm hoặc phương trình $(2)$ có nghiệm kép dương 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{ac < 0}\\
{\left\{ {\begin{array}{c}
{\Delta = 0}\\
{ – \frac{b}{{2a}} > 0}
\end{array}} \right.}
\end{array}} \right.
$$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so-3.png" alt="">
 | 

Trong các bài toán về tương giao của hàm trùng phương, chúng ta nên lưu ý dạng phương trình $a{t^2} + bt + c = 0$ $(2)$ có thể nhẩm được nghiệm khi xác định được mối quan hệ đặc biệt giữa các hệ số $a$, $b$, $c:$

+ Nếu $a + b + c = 0$ thì phương trình $(2)$ có hai nghiệm là $t = 1$ và $t = \frac{c}{a}.$

+ Nếu $a – b + c = 0$ thì phương trình $(2)$ có hai nghiệm là $t = – 1$ và $t = – \frac{c}{a}.$

Chú ý: Đồ thị hàm số $y = f(x) = a{x^4} + b{x^2} + c$ $(C)$ cắt trục hoành tại bốn điểm phân biệt có hoành độ lập thành cấp số cộng thì điều kiện cần là $9{b^2} = 100ac.$ Sau khi sử dụng điều kiện cần ta sẽ xác định được giá trị của tham số, sau đó cần thay vào phương trình hoành độ giao điểm để kiểm tra xem có đúng $4$ giao điểm không. Nếu có thì giá trị tham số đó là giá trị thỏa mãn bài toán.

Trong nhiều trường hợp về bài toán tương giao của hàm trùng phương, ta có thể sử dụng phương pháp cô lập theo tham số $m$ để biện luận số giao điểm bằng bảng biến thiên hoặc đồ thị của hàm số trùng phương.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## Ví dụ 1. Tìm tất cả các giá trị của tham số thực $m$ để đồ thị hàm số $f(x) = {x^4} – 2{x^2} + 3 – m$ $(C)$ cắt trục hoành:

a) Tại bốn điểm phân biệt.

b) Tại ba điểm phân biệt.

c) Tại hai điểm phân biệt.

d) Không cắt trục hoành.

Xét phương trình hoành độ giao điểm: ${x^4} – 2{x^2} + 3 – m = 0$ $(1).$

Đặt $t = {x^2} \ge 0$, phương trình $(1)$ trở thành: ${t^2} – 2t + 3 – m = 0$ $(2).$

a) Để $(C)$ cắt trục hoành tại bốn điểm phân biệt $\Leftrightarrow (2)$ có hai nghiệm phân biệt dương 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 1 – (3 – m) > 0}\\
{\frac{{ – b}}{a} = 2 > 0}\\
{\frac{c}{a} = 3 – m > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m – 2 > 0}\\
{3 – m > 0}
\end{array}} \right.
$$
 $\Leftrightarrow 3 > m > 2.$

b) Để $(C)$ cắt trục hoành tại ba điểm phân biệt $\Leftrightarrow (2)$ có một nghiệm bằng $0$ và nghiệm còn lại dương 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{c = 3 – m = 0}\\
{\frac{{ – b}}{a} = 2 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = 3.$

c) Để $(C)$ cắt trục hoành tại hai điểm phân biệt $\Leftrightarrow (2)$ có hai nghiệm trái dấu hoặc có nghiệm kép dương 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{1(3 – m) < 0}\\
{\left\{ {\begin{array}{l}
{1 – (3 – m) = 0}\\
{ – \frac{b}{{2a}} = 1 > 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 3}\\
{m = 2}
\end{array}} \right..
$$

d) Để $(C)$ không cắt trục hoành $\Leftrightarrow (2)$ vô nghiệm hoặc có hai nghiệm đều âm.

$$
\Leftrightarrow \left[ \begin{array}{l}
\Delta ‘ = m – 2 < 0\\
\left\{ {\begin{array}{l}
{\Delta ‘ = m – 2 \ge 0}\\
{ – \frac{b}{a} = 2 < 0\:\:{\rm{(loại)}}}\\
{\frac{c}{a} = 3 – m > 0}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow m < 2.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## Ví dụ 2. Tìm điều kiện của tham số $m$ để đồ thị hàm số: $f(x) = {x^4} – \left( {1 + 4{m^2}} \right){x^2} + 4{m^2}.$

a) Cắt trục hoành tại đúng hai điểm phân biệt.

b) Cắt trục hoành tại bốn điểm phân biệt $A$, $B$, $C$, $D$ có hoành độ theo thứ tự lập thành cấp số cộng.

Ta có phương trình hoành độ giao điểm: ${x^4} – \left( {1 + 4{m^2}} \right){x^2} + 4{m^2} = 0$ $(1).$

Đặt $t = {x^2} \ge 0$, ta có phương trình ${t^2} – \left( {1 + 4{m^2}} \right)t + 4{m^2} = 0$ $(2).$

Nhận xét phương trình có $a+b+c=0.$

Do đó phương trình $(2)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = \frac{c}{a} = 4{m^2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left[ {\begin{array}{l}
{{x^2} = 1}\\
{{x^2} = 4{m^2}}
\end{array}} \right..
$$

a) Để đồ thị hàm số đã cho cắt trục hoành tại đúng hai điểm phân biệt $\Leftrightarrow 4{m^2} = 1$ $\Leftrightarrow m = \pm \frac{1}{2}.$

b) Để đồ thị hàm số đã cho cắt trục hoành tại bốn điểm phân biệt $A$, $B$, $C$, $D$ có hoành độ theo thứ tự lập thành cấp số cộng $\Rightarrow 4{m^2} \ne 1$ $\Leftrightarrow m \ne \pm \frac{1}{2}.$

Giả sử ${t_1} < {t_2}$ là hai nghiệm dương phân biệt của phương trình $(2)$ thì phương trình $(1)$ có bốn nghiệm sắp thứ tự là:

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so-4.png" alt="">

Vì $– \sqrt {{t_2}}$, $– \sqrt {{t_1}}$, $\sqrt {{t_1}}$, $\sqrt {{t_2}}$ theo thứ tự lập thành cấp số cộng nên ta có:

$\frac{{\sqrt {{t_1}} + ( – \sqrt {{t_2}} )}}{2} = – \sqrt {{t_1}}$ $\Leftrightarrow \sqrt {{t_2}} = 3\sqrt {{t_1}}$ $\Leftrightarrow {t_2} = 9{t_1}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{1 = 9.4{m^2}}\\
{4{m^2} = 9.1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = \pm \frac{1}{6}}\\
{m = \pm \frac{3}{2}}
\end{array}} \right..
$$

<!-- chunk:4 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM

## Bài 1. Tìm tất cả các giá trị thực của tham số $m$ để đường thẳng $y = 4m$ cắt đồ thị hàm số $y = {x^4} – 8{x^2} + 3$ tại bốn điểm phân biệt?

A. $– \frac{{13}}{4} < m < \frac{3}{4}.$

B. $– \frac{{13}}{4} \le m \le \frac{3}{4}.$

C. $m \le \frac{3}{4}.$

D. $m \ge – \frac{{13}}{4}.$

Ta có: $y’ = 4{x^3} – 16x$, $y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so-5.png" alt="">

Từ bảng biến thiên trên, để đường thẳng $y = 4m$ cắt đồ thị hàm số $y = {x^4} – 8{x^2} + 3$ tại bốn điểm phân biệt thì $– 13 < 4m < 3$ $\Leftrightarrow – \frac{{13}}{4} < m < \frac{3}{4}.$

Vậy giá trị cần tìm của $m$ là $– \frac{{13}}{4} < m < \frac{3}{4}.$

> **Đáp án: A**

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^4} – 2m{x^2} + m + 2$ cắt trục hoành tại bốn điểm phân biệt.

A. $(2; + \infty ).$

B. $(0; + \infty ).$

C. $( – 3; + \infty ).$

D. $m \in ( – \infty ;1).$

Phương trình hoành độ giao điểm của đồ thị hàm số với trục hoành là:

${x^4} – 2m{x^2} + m + 2 = 0$ $(1).$

Đặt $t = {x^2} \ge 0$, phương trình trở thành: ${t^2} – 2mt + m + 2 = 0$ $(2).$

Để đồ thị hàm số đã cho cắt trục hoành tại bốn điểm phân biệt $\Leftrightarrow (2)$ có hai nghiệm phân biệt dương.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {m^2} – m – 2 > 0}\\
{ – \frac{b}{a} > 0}\\
{\frac{c}{a} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {m^2} – m – 2 > 0}\\
{2m > 0}\\
{m + 2 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\left[ {\begin{array}{l}
{m > 2}\\
{m < – 1}
\end{array}} \right.}\\
{m > 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > 2.$

> **Đáp án: A**

## Bài 3. Có bao nhiêu giá trị nguyên của tham số $m \in [ – 5;15]$ để đồ thị hàm số $f(x) = {x^4} – 2(m + 3){x^2} + m + 2$ cắt $d:y = – 3$ tại bốn điểm phân biệt.

A. $15.$

B. $16.$

C. $20.$

D. $21.$

Phương trình hoành độ giao điểm của đồ thị hàm số $y = f(x)$ với đường thẳng $d$ là: ${x^4} – 2(m + 3){x^2} + m + 2 = – 3$ $\Leftrightarrow {x^4} – 2(m + 3){x^2} + m + 5 = 0$ $(1).$

Đặt $t = {x^2} \ge 0$, phương trình trở thành ${t^2} – 2(m + 3)t + m + 5 = 0$ $(2).$

Để đồ thị hàm số đã cho cắt trục hoành tại bốn điểm phân biệt $\Leftrightarrow (2)$ có hai nghiệm phân biệt dương.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {{(m + 3)}^2} – m – 5 > 0}\\
{ – \frac{b}{a} > 0}\\
{\frac{c}{a} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {m^2} + 5m + 4 > 0}\\
{m + 3 > 0}\\
{m + 5 > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\left[ {\begin{array}{l}
{m > – 1}\\
{m < – 4}
\end{array}} \right.}\\
{m > – 3}
\end{array}} \right.
$$
 $\Leftrightarrow m > – 1.$

Mà $m \in Z$, $m \in [ – 5;15]$ do đó $m \in \{ 0;1;2; \ldots ;14;15\}$ có $16$ giá trị.

> **Đáp án: B**

## Bài 4. Tính tổng các giá trị của tham số $m$ biết $m > 0$, sao cho đồ thị hàm số $f(x) = {x^4} – \left( {9{m^2} + 1} \right){x^2} + 9{m^2}$ cắt trục hoành tại bốn điểm phân biệt có hoành độ lập thành cấp số cộng.

A. $\frac{{10}}{9}$.

B. $\frac{{82}}{9}$.

C. $\frac{{19}}{9}$.

D. $\frac{{37}}{9}$.

Ta có phương trình hoành độ giao điểm với trục hoành là:

${x^4} – \left( {9{m^2} + 1} \right){x^2} + 9{m^2} = 0$ $\Leftrightarrow \left( {{x^2} – 1} \right)\left( {{x^2} – 9{m^2}} \right) = 0.$

Áp dụng ví dụ 2, yêu cầu bài toán 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{9{m^2} \ne 1}\\
{\left[ {\begin{array}{l}
{9{m^2} = 9}\\
{1 = 9.9{m^2}}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne \pm \frac{1}{3}}\\
{\left[ {\begin{array}{l}
{m = \pm 1}\\
{m = \pm \frac{1}{9}}
\end{array}} \right.}
\end{array}} \right..
$$

Mà $m > 0$ thì 
$$
\left[ {\begin{array}{l}
{m = 1}\\
{m = \frac{1}{9}}
\end{array}} \right.
$$
 do đó tổng các giá trị $m$ cần tìm là $1 + \frac{1}{9}$ $= \frac{{10}}{9}.$

> **Đáp án: A**

## Bài 5. Cho $m$ là tham số thực có điều kiện $m >1$, biết đường thẳng $y = m + 2$ cắt đồ thị hàm số $y = {x^4} – (2m + 3){x^2} + 3m + 4$ tại bốn điểm phân biệt $A$, $B$, $C$, $D$ theo thứ tự có hoành độ tăng dần sao cho ${S_{OAD}} = 3{S_{OBC}}.$ Hỏi $m$ thuộc khoảng nào sau đây?

A. $(2;3).$

B. $(3;4).$

C. $(4;5).$

D. $(5;6).$

Ta có phương trình hoành độ giao điểm là:

${x^4} – (2m + 3){x^2} + 3m + 4 = m + 2$ $\Leftrightarrow {x^4} – (2m + 3){x^2} + 2m + 2 = 0.$

$\Leftrightarrow \left( {{x^2} – 1} \right)\left[ {{x^2} – (2m + 2)} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} = 1}\\
{{x^2} = 2m + 2}
\end{array}} \right..
$$

Vì $m >1$ nên ta có 
$$
\left[ {\begin{array}{l}
{x = \pm 1}\\
{x = \pm \sqrt {2m + 2} }
\end{array}} \right..
$$
 Khi đó $– \sqrt {2m + 2} < – 1 < 1 < \sqrt {2m + 2} .$

Suy ra: $A( – \sqrt {2m + 2} ;m + 2)$, $B( – 1;m + 2)$, $C(1;m + 2)$, $D(\sqrt {2m + 2} ;m + 2).$

Theo bài ra ta có ${S_{OAD}} = 3{S_{OBC}}$ $\Leftrightarrow AD = 3BC$ $\Leftrightarrow 2\sqrt {2m + 2} = 6$ $\Leftrightarrow m = \frac{7}{2}.$

> **Đáp án: B**

## Bài 6. Cho $m$ là tham số thực biết đồ thị hàm số $y = {x^4} – (m + 4){x^2} + 1$ cắt đường thẳng $y=-m-2$ tại bốn điểm phân biệt $A$, $B$, $C$, $D$ sao cho $x_A^2 + x_B^2 + x_C^2 + x_D^2 = 12$ khi $m = {m_0}.$ Tính giá trị biểu thức $T = m_0^5 + 2{m_0} – 8.$

Ta có phương trình hoành độ giao điểm của hai đồ thị là:

${x^4} – (m + 4){x^2} + 1 = – m – 2$ $\Leftrightarrow {x^4} – (m + 4){x^2} + m + 3 = 0.$

$\Leftrightarrow \left( {{x^2} – 1} \right)\left[ {{x^2} – (m + 3)} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} = 1}\\
{{x^2} = m + 3}
\end{array}} \right.
$$
 $(1).$

Để hai đồ thị cắt nhau tại bốn điểm phân biệt 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m + 3 > 0}\\
{m + 3 \ne 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > – 3}\\
{m \ne – 2}
\end{array}} \right..
$$

Khi đó ta có 
$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x = \pm 1}\\
{x = \pm \sqrt {m + 3} }
\end{array}} \right..
$$

Theo bài ra, ta có bốn giao điểm phân biệt $A$, $B$, $C$, $D$ sao cho $x_A^2 + x_B^2 + x_C^2 + x_D^2 = 14$ $\Leftrightarrow 1 + 1 + m + 3 + m + 3 = 12$ $\Leftrightarrow m = 2$ $\Rightarrow T = 32 + 4 – 8 = 28.$

> **Đáp án: B**

## Bài 7. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^4} – (5m + 2){x^2} + 5m$ cắt đường thẳng $y = -1$ tại bốn điểm phân biệt đều có hoành độ nhỏ hơn $2.$

A. $\left( { – \frac{1}{5};\frac{3}{5}} \right)\backslash \{ 0\}$.

B. $\left( {0;\frac{3}{5}} \right)$.

C. $\left( { – 1; – \frac{1}{5}} \right)$.

D. $\left( {\frac{3}{5}; + \infty } \right)$.

Phương trình hoành độ giao điểm của hai đồ thị là:

${x^4} – (5m + 2){x^2} + 5m = – 1$ $\Leftrightarrow {x^4} – (5m + 2){x^2} + 5m + 1 = 0.$

$\Leftrightarrow \left( {{x^2} – 1} \right)\left[ {{x^2} – (5m + 1)} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} = 1}\\
{{x^2} = 5m + 1}
\end{array}} \right.
$$
 $(1).$

Để hai đồ thị cắt nhau tại bốn điểm phân biệt 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{5m + 1 > 0}\\
{5m + 1 \ne 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > – \frac{1}{5}}\\
{m \ne 0}
\end{array}} \right..
$$

Khi đó 
$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x = \pm 1}\\
{x = \pm \sqrt {5m + 1} }
\end{array}} \right..
$$
 Theo yêu cầu bài toán, ta có $\sqrt {5m + 1} < 2.$

Do $1$, $– 1$, $– \sqrt {5m + 1}$ luôn nhỏ hơn $2$ $\Rightarrow 5m + 1 < 4$ $\Leftrightarrow m < \frac{3}{5}.$

Vậy $m \in \left( { – \frac{1}{5};\frac{3}{5}} \right)\backslash \{ 0\} .$

> **Đáp án: A**

## Bài 8. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc khoảng $(-15;15)$ để đồ thị hàm số $f(x) = {x^4} – (m + 4){x^2} + 2m$ cắt đường thẳng $d:y = – 2m$ tại bốn điểm phân biệt sao cho khoảng cách lớn nhất giữa các giao điểm không nhỏ hơn $6.$

A. $29.$

B. $7.$

C. $5.$

D. $6.$

Phương trình hoành độ giao điểm của đồ thị là: ${x^4} – (m + 4){x^2} + 2m = – 2m.$

$\Leftrightarrow {x^4} – (m + 4){x^2} + 4m = 0$ $\Leftrightarrow \left( {{x^2} – 4} \right)\left( {{x^2} – m} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} – 4 = 0}\\
{{x^2} – m = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} = 4}\\
{{x^2} = m}
\end{array}} \right..
$$

Để hai đồ thị cắt nhau tại bốn điểm phân biệt 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m > 0}\\
{m \ne 4}
\end{array}} \right..
$$

Nếu $4 > m$ thì ta có $– 2 < – \sqrt m < \sqrt m < 2.$

Khi đó bốn giao điểm là $A( – 2; – 2m)$, $B( – \sqrt m ; – 2m)$, $C(\sqrt m ; – 2m)$, $D(2; – 2m).$

Khoảng cách lớn nhất giữa các giao điểm là $AD = 4 < 6$ (loại).

Nếu $4 < m$ thì ta có $– \sqrt m < – 2 < 2 < \sqrt m .$

Khi đó bốn giao điểm là $A( – \sqrt m ; – 2m)$, $B( – 2; – 2m)$, $C(2; – 2m)$, $D(\sqrt m ; – 2m).$

Khoảng cách lớn nhất giữa các giao điểm là $AD = 2\sqrt m > 6$ $\Leftrightarrow m > 9.$

Mà $m \in Z$, $m \in ( – 15;15)$ $\Rightarrow m \in \{ 10;11;12;13;14\} .$ Có $5$ giá trị thỏa bài toán.

> **Đáp án: C**

## Bài 9. Cho đồ thị hàm số $f(x) = {x^4} + (1 – 2m){x^2} – 4m$ cắt đường thẳng $d: y=2$ tại đúng hai điểm phân biệt $A\left( {{x_1};{y_1}} \right)$ và $B\left( {{x_2};{y_2}} \right)$ với ${x_1} < {x_2}.$ Biết $OB = 3$ với $O$ là gốc tọa độ. Khi đó $m$ thuộc khoảng nào sau đây?

A. $\left( {\frac{5}{2};\frac{7}{2}} \right)$.

B. $\left( { – \frac{1}{2};\frac{1}{2}} \right)$.

C. $\left( {\frac{1}{2};\frac{3}{2}} \right)$.

D. $\left( {\frac{3}{2};\frac{5}{2}} \right)$.

Ta có phương trình hoành độ giao điểm: ${x^4} + (1 – 2m){x^2} – 4m = 2.$

$\Leftrightarrow {x^4} + (1 – 2m){x^2} – 4m – 2 = 0$ $\Leftrightarrow \left( {{x^2} + 2} \right)\left( {{x^2} – 2m – 1} \right) = 0$ $\Leftrightarrow {x^2} = 2m + 1$ $(1).$

Để hai đồ thị cắt nhau tại đúng hai điểm phân biệt $\Leftrightarrow 2m + 1 > 0$ $\Leftrightarrow m > – \frac{1}{2}.$

Khi đó ta có 
$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x = – \sqrt {2m + 1} }\\
{x = \sqrt {2m + 1} }
\end{array}} \right.
$$
, do đó $A( – \sqrt {2m + 1} ;2)$ và $B(\sqrt {2m + 1} ;2).$

Theo bài ra ta có $OB = 3$ $\Leftrightarrow {(\sqrt {2m + 1} – 0)^2} + {(2 – 0)^2} = {3^2}.$

$\Leftrightarrow 2m + 1 + 4 = 9$ $\Leftrightarrow m = 2$ (thỏa mãn).

> **Đáp án: D**

## Bài 10. Biết đồ thị hàm số $f(x) = {x^4} – (m + 2){x^2} + m$ cắt đường thẳng $y = -1$ tại bốn điểm phân biệt $A$, $B$, $C$, $D$ có hoành độ theo thứ tự tăng dần sao cho ${S_{IAD}} = 4$ với $I(1; – m)$ và $m > 0.$ Hỏi $m$ có giá trị thuộc khoảng nào sau đây?

A. $(0;2).$

B. $(2;4).$

C. $(4;6).$

D. $(6;8).$

Ta có phương trình hoành độ giao điểm:

${x^4} – (m + 2){x^2} + m = – 1$ $\Leftrightarrow {x^4} – (m + 2){x^2} + m + 1 = 0.$

$\Leftrightarrow \left( {{x^2} – 1} \right)\left[ {{x^2} – (m + 1)} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x^2} = 1}\\
{{x^2} = m + 1}
\end{array}} \right.
$$
 $(1).$

Vì $m > 0$ $\Rightarrow m + 1 > 1.$

Khi đó 
$$
(1) \Leftrightarrow \left[ {\begin{array}{l}
{x = \pm 1}\\
{x = \pm \sqrt {m + 1} }
\end{array}} \right..
$$
 Ta có $– \sqrt {m + 1} < – 1 < 1 < \sqrt {m + 1} .$

Suy ra: $A( – \sqrt {m + 1} ; – 1)$, $B( – 1; – 1)$, $C(1; – 1)$, $D(\sqrt {m + 1} ; – 1).$

Do đó ${S_{IAD}} = \frac{1}{2}d(I;d).AD$ $\Leftrightarrow 4 = \frac{1}{2}.|m – 1|.2\sqrt {m + 1} .$

$\Leftrightarrow 4 = |m – 1|.\sqrt {m + 1}$ $\Leftrightarrow m = 3.$

> **Đáp án: B**

<!-- chunk:5 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^4} – (2m + 3){x^2} + 2m + 2$ cắt trục hoành tại đúng bốn điểm phân biệt.

A. $\left( { – 1; – \frac{1}{2}} \right) \cup \left( { – \frac{1}{2}; + \infty } \right).$

B. $( – 1; + \infty ).$

C. $( – 3;0).$

D. $( – \infty ; – 1).$

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^4} – 2(m – 3){x^2} + m – 3$ cắt trục hoành tại bốn điểm phân biệt.

A. $(0;4).$

B. ${(4; + \infty ).}$

C. ${(3; + \infty )}.$

D. ${[2; + \infty )}.$

## Bài 3. Biết đồ thị hàm số $f(x) = {x^4} – (m + 3){x^2} + 2m + 2$ cắt trục hoành tại ba điểm phân biệt. Khi đó $m$ có giá trị thuộc khoảng nào sau đây?

A. $(-6;-3).$

B. $(0;3).$

C. $(-3;0).$

D. $(3;6).$

## Bài 4. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc $[-8;8]$ để đồ thị hàm số $f(x) = {x^4} – (m + 4){x^2} + 3m + 3$ cắt trục hoành tại bốn điểm phân biệt.

A. $7.$

B. $8.$

C. $17.$

D. $9.$

## Bài 5. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc $(-2;10)$ để đồ thị hàm số $f(x) = {x^4} – (2m + 4){x^2} + 6m + 6$ cắt đường thẳng $d: y=3$ tại bốn điểm phân biệt.

A. $9.$

B. $10.$

C. $8.$

D. $12.$

## Bài 6. Tính tổng tất cả các giá trị nguyên của tham số $m$ thuộc $(-7;7)$ để đồ thị hàm số $y = {x^4} – (2m + 1){x^2} + {m^2} + 2m$ cắt đường thẳng $y = m$ tại bốn điểm phân biệt.

A. $28.$

B. $18.$

C. $21.$

D. $20.$

## Bài 7. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc $(-10;10)$ để đồ thị hàm số $f(x) = {x^4} – (2m + 6){x^2} + 6m + 11$ cắt đường thẳng $d: y = 2$ tại đúng hai điểm phân biệt.

A. $7.$

B. $10.$

C. $9.$

D. $8.$

## Bài 8. Biết đồ thị hàm số $y = {x^4} – (3m + 1){x^2} + 2{m^2} + 2m$ cắt trục hoành tại bốn điểm phân biệt có hoành độ theo thứ tự lập thành một cấp số cộng. Khi đó $m$ có giá trị thuộc khoảng nào sau đây?

A. $\left( {\frac{1}{{16}};\frac{1}{{14}}} \right).$

B. $\left( {\frac{1}{{18}};\frac{1}{{16}}} \right).$

C. $\left( {\frac{1}{{20}};\frac{1}{{18}}} \right).$

D. $\left( {\frac{1}{{14}};\frac{1}{{12}}} \right).$

## Bài 9. Biết đồ thị hàm số $y = {x^4} – (2m – 3){x^2} + {m^2} – 3m + 4$ cắt đường thẳng $y=2$ tại bốn điểm phân biệt $A$, $B$, $C$, $D$ sao cho ${x_A} < {x_B} < {x_C} < {x_D}$ và $AB = BC = CD$ khi $m = \frac{a}{b}$, $a$, $b \in N$, $(a;b) = 1.$ Tính tổng $S=a+b.$

A. $S=-23.$

B. $S = 6.$

C. $S =9.$

D. $S = 25.$

## Bài 10. Cho $m \in R$, $m > 1.$ Biết đồ thị hàm số $y = {x^4} – (m + 5){x^2} + 3m + 8$ cắt đường thẳng $y=2$ tại bốn điểm phân biệt $A$, $B$, $C$, $D$ có ${x_A} < {x_B} < {x_C} < {x_D}$ sao cho ${S_{OAD}} = 6$ với $O$ là gốc tọa độ khi $m = {m_0}.$ Tính giá trị biểu thức ${T = 5{m_0} – 3.}$

A. $32.$

B. $1.$

C. $7.$

D. $22.$

<!-- chunk:6 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-trung-phuong-chua-tham-so.html -->
## **V. ĐÁP ÁN BÀI TẬP TỰ LUYỆN

**1. A.

2. B.

3. C.

4. B.

5. A.

6. C.

7. C.

8. B.

9. D.

10. A.