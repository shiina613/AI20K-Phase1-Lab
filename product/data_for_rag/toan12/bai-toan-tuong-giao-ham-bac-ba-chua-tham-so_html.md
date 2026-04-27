# Bài toán tương giao hàm bậc ba chứa tham số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
Bài viết hướng dẫn phương pháp tìm điều kiện tham số liên quan bài toán tương giao của hàm bậc ba trong chương trình Giải tích 12: ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN
Để giải quyết bài toán tương giao của hàm bậc ba, ta có các chú ý sau đây:

a) Cho hàm số bậc ba $y = f(x)$ có đồ thị $(C).$

Số giao điểm của đồ thị $(C)$ với trục $Ox$
**Điều kiện** | 
**Đồ thị minh họa** | 

Có ba giao điểm phân biệt | 
Hàm số có hai cực trị ${x_1}$, ${x_2}$ và $y\left( {{x_1}} \right).y\left( {{x_2}} \right) < 0$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so-1.png" alt="">
 | 

Có hai giao điểm phân biệt | 
Hàm số có hai cực trị ${x_1}$, ${x_2}$ và $y\left( {{x_1}} \right).y\left( {{x_2}} \right) = 0$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so-2.png" alt="">
 | 

Có một giao điểm | 
Hàm số không có cực trị hoặc hàm số có hai cực trị ${x_1}$, ${x_2}$ và $y\left( {{x_1}} \right).y\left( {{x_2}} \right) > 0$

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so-3.png" alt="">
 | 

b) Tuy nhiên trong nhiều bài toán về tương giao của hàm bậc ba, đôi khi ta cũng không xác định được các giá trị $y\left( {{x_1}} \right)$, $y\left( {{x_2}} \right)$ thì ta có thể sử dụng phương pháp phân tích đa thức thành nhân tử bằng phương pháp nhóm cô lập tham số $m.$

+ Bước 1: Biến đổi phương trình $f(x) = 0$ $\Leftrightarrow Am + B = 0.$

+ Bước 2: Giải hệ điều kiện 
$$
\left\{ {\begin{array}{l}
{A = 0}\\
{B = 0}
\end{array}} \right.
$$
 và tìm nghiệm ${x_0}.$

+ Bước 3: Phương trình $Am + B = 0$ $\Leftrightarrow \left( {x – {x_0}} \right)g(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x – {x_0} = 0}\\
{g(x) = 0}
\end{array}} \right..
$$

Từ đó biện luận phương trình dạng bậc hai $g(x) = 0$ từ đó xác định được điều kiện của tham số cần tìm.

Chú ý: Trong trường hợp phương trình hoành độ giao điểm có dạng $A{m^2} + Bm + C = 0$ thì ta làm hoàn toàn tương tự bằng cách giải hệ điều kiện $A = B = C = 0$ để tìm nhân tử chung.

c) Ngoài hai cách làm ở trên ta có thể áp dụng phương pháp cô lập $m$ đã được nói đến trong các chuyên đề khác.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## Ví dụ 1. Tìm điều kiện của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3x + {m^2} + m$ cắt trục hoành tại ba điểm phân biệt.

Ta có $f'(x) = 3{x^2} – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 1}
\end{array}.} \right.
$$

Do đó hàm số đã cho có hai cực trị là ${x_1} = 1$, ${x_2} = – 1.$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi $f(1).f( – 1) < 0.$

$\Leftrightarrow \left( {{m^2} + m – 2} \right)\left( {{m^2} + m + 2} \right) < 0$ $\Leftrightarrow {m^2} + m – 2 < 0$ $\Leftrightarrow – 2 < m < 1.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## Ví dụ 2. Tìm điều kiện của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3{x^2} + 2m – 6$:

a) Cắt trục hoành tại đúng hai điểm phân biệt.

b) Cắt trục hoành tại một điểm duy nhất.

Ta có $f(x) = {x^3} – 3{x^2} + 2m – 6$ có $f'(x) = 3{x^2} – 6x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Do đó hàm số đã cho có hai cực trị là ${x_1} = 0$, ${x_2} = 2.$

a) Để đồ thị hàm số cắt trục hoành tại hai điểm phân biệt khi:

$f(0).f(2) = 0$ $\Leftrightarrow (2m – 6)(2m – 10) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 3}\\
{m = 5}
\end{array}} \right..
$$

b) Để đồ thị hàm số cắt trục hoành tại đúng một điểm duy nhất khi:

$f(0).f(2) > 0$ $\Leftrightarrow (2m – 6)(2m – 10) > 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 5}\\
{m < 3}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## Ví dụ 3. Tìm điều kiện của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3{x^2} + (m + 1)x – m + 1$:

a) Cắt trục hoành tại ba điểm phân biệt.

b) Cắt trục hoành tại ba điểm phân biệt có hoành độ đều dương.

c) Cắt trục hoành tại hai điểm phân biệt.

d) Cắt trục hoành tại một điểm duy nhất.

Ta có phương trình hoành độ giao điểm của đồ thị hàm số đã cho với trục hoành là:

${x^3} – 3{x^2} + (m + 1)x – m + 1 = 0$ $\Leftrightarrow m(x – 1) + {x^3} – 3{x^2} + x + 1 = 0.$

$\Leftrightarrow m(x – 1)$ $+ (x – 1)\left( {{x^2} – 2x – 1} \right) = 0$ $\Leftrightarrow (x – 1)\left( {{x^2} – 2x – 1 + m} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{g(x) = {x^2} – 2x – 1 + m = 0\:\:(1)}
\end{array}} \right..
$$

a) Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi $(1)$ có hai nghiệm phân biệt khác $1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 1 + 1 – m > 0}\\
{g(1) = 1 – 1 – 1 + m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2 > m}\\
{m \ne 1}
\end{array}} \right..
$$

b) Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt có hoành độ đều dương khi phương trình $(1)$ có hai nghiệm dương phân biệt khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 1 + 1 – m > 0}\\
{g(1) = 1 – 1 – 1 + m \ne 0}\\
{ – \frac{b}{a} > 0}\\
{\frac{c}{a} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 2}\\
{m \ne 1}\\
{2 > 0}\\
{m – 1 > 0}
\end{array}} \right.
$$
 $\Leftrightarrow 1 < m < 2.$

c) Để đồ thị hàm số cắt trục hoành tại đúng hai điểm phân biệt khi $(1)$ có nghiệm kép khác $1$ hoặc có một nghiệm bằng $1$ và một nghiệm còn lại khác $1.$

+ Nếu $(1)$ có nghiệm kép khác $1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 2 – m = 0}\\
{{x_1} = {x_2} = \frac{{ – b}}{{2a}} \ne 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m = 2}\\
{1 \ne 1\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

+ Nếu $(1)$ có một nghiệm bằng $1$ và một nghiệm còn lại khác $1.$

$\Rightarrow g(1) = m – 2 = 0$ $\Leftrightarrow m = 2.$

Thử lại với $m = 2$, ta có $g(x) = {x^2} – 2x + 1$ $= {(x – 1)^2} = 0$ $\Leftrightarrow x = 1$ (loại).

Vậy không có giá trị nào của $m$ để đồ thị hàm số cắt trục hoành tại đúng hai điểm phân biệt.

d) Để đồ thị hàm số cắt trục hoành tại đúng một điểm duy nhất khi $(1)$ có nghiệm kép bằng $1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 0}\\
{g(1) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2 – m = 0}\\
{m – 2 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = 2.$

Chú ý: Định lí Vi-et cho phương trình bậc ba:

Cho phương trình bậc ba có dạng: $a{x^3} + b{x^2} + cx + d = 0$ $(a \ne 0)$ có ba nghiệm ${x_1}$, ${x_2}$, ${x_3}.$ Khi đó ta luôn có:

$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} + {x_3} = – \frac{b}{a}}\\
{{x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1} = \frac{c}{a}}\\
{{x_1}{x_2}{x_3} = \frac{{ – d}}{a}}
\end{array}} \right..
$$

Áp dụng định lí Vi-et cho phương trình bậc ba giúp ta giải quyết các bài toán tương giao hàm bậc ba có liên quan cấp số cộng, cấp số nhân một cách tương đối ngắn gọn.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## Ví dụ 4. Tìm điều kiện của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 6{x^2} + 11x – m – 4$ cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành cấp số cộng.

+ Điều kiện cần:

Xét phương trình hoành độ giao điểm: ${x^3} – 6{x^2} + 11x – m – 4 = 0$ $(1).$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành cấp số cộng thì phương trình trình $(1)$ có ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ theo thứ tự lập thành cấp số cộng.

Khi đó ta có ${x_1} + {x_2} + {x_3} = – \frac{b}{a} = 6$ mà ${x_1} + {x_3} = 2{x_2}$ $\Rightarrow {x_1} + {x_2} + {x_3} = 3{x_2}.$

Do đó ${x_2} = 2.$

Thay ${x_2} = 2$ vào phương trình $(1)$ ta có: ${2^3} – {6.2^2} + 11.2 – m – 4 = 0$ $\Leftrightarrow m = 2.$

+ Điều kiện đủ: Thay $m = 2$ vào phương trình $(1)$, ta có:

${x^3} – 6{x^2} + 11x – 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2}\\
{x = 3}
\end{array}} \right.
$$
 (thỏa mãn).

Vậy $m = 2$ là giá trị cần tìm.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## Ví dụ 5. Tìm điều kiện của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – (4 + m){x^2} + (11 + m)x – 8$ cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành cấp số nhân.

+ Điều kiện cần:

Xét phương trình hoành độ giao điểm ${x^3} – (4 + m){x^2} + (11 + m)x – 8 = 0$ $(1).$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành cấp số nhân thì phương trình $(1)$ có ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ theo thứ tự lập thành cấp số nhân.

Khi đó ta có ${x_1}{x_2}{x_3} = – \frac{d}{a} = 8$ mà ${x_1}{x_3} = x_2^2$ $\Rightarrow {x_1}{x_2}{x_3} = x_2^3$ do đó ${x_2} = 2.$

Thay ${x_2} = 2$ vào $(1)$ ta có: ${2^3} – (4 + m){2^2} + (11 + m)2 – 8 = 0$ $\Leftrightarrow m = 3.$

+ Điều kiện đủ: Thay $m = 3$ vào phương trình $(1)$, ta có:

${x^3} – 7{x^2} + 14x – 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2}\\
{x = 4}
\end{array}} \right.
$$
 (thỏa mãn).

Vậy $m = 3$ là giá trị cần tìm.

<!-- chunk:7 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3x + m – 2$ cắt trục hoành tại ba điểm phân biệt.

A. $m \le 2.$

B. $m < 0$ hoặc $m > 4.$

C. $0<m<4.$

D. $m>3.$

Ta có $f(x) = {x^3} – 3x + m – 2.$ Suy ra $f'(x) = 3{x^2} – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 1}
\end{array}} \right..
$$

Do đó đồ thị hàm số có hai điểm cực trị là $A(1;m – 4)$, $B(-1;m).$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi:

$(m – 4)m < 0$ $\Leftrightarrow 0 < m < 4.$

> **Đáp án: C**

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^3} + 3{x^2} – m + 1$ cắt trục hoành tại ba điểm phân biệt.

A. $(-2;5).$

B. $(1; + \infty ).$

C. $m \in ( – \infty ;1] \cup [5; + \infty ).$

D. $m \in (1;5).$

Ta có $f(x) = {x^3} + 3{x^2} – m + 1.$ Suy ra $f'(x) = 3{x^2} + 6x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = – 2}
\end{array}} \right..
$$

Do đó đồ thị hàm số có hai điểm cực trị là $A(0;1- m)$, $B(-2;5-m).$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi $(1 – m)(5 – m) < 0$ $\Leftrightarrow 1 < m < 5.$

Chọn đán án D.

## Bài 3. Có bao nhiêu giá trị nguyên của tham số $m$ để đồ thị hàm số $f(x) = {x^3} + 3{x^2} – 9x + m – 1$ cắt trục hoành tại ba điểm phân biệt.

A. $33.$

B. $31.$

C. $32.$

D. $34.$

Ta có $f(x) = {x^3} + 3{x^2} – 9x + m – 1$ $\Rightarrow f'(x) = 3{x^2} + 6x – 9 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = – 3}
\end{array}} \right..
$$

Do đó đồ thị hàm số có hai điểm cực trị là $A(1;m –6)$, $B(-3;m+26).$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi:

$(m – 6)(m + 26) < 0$ $\Leftrightarrow – 26 < m < 6.$

Mà $m \in Z$ $\Rightarrow m \in \{ – 25; – 24; – 23; \ldots ;4;5\}$ nên ta có $31$ giá trị thỏa mãn bài toán.

> **Đáp án: B**

## Bài 4. Tính tổng các giá trị nguyên của tham số $m$ để để đồ thị hàm số $f(x) = 2{x^3} – 3{x^2} – 12x – m + 26$ cắt trục hoành tại ba điểm phân biệt.

A. $507.$

B. $500.$

C. $540.$

D. $579.$

Ta có $f(x) = 2{x^3} – 3{x^2} – 12x – m + 26.$

Suy ra $f'(x) = 6{x^2} – 6x – 12$, $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 2}
\end{array}} \right..
$$

Do đó đồ thị hàm số có hai đểm cực trị là $A(-1;33 – m)$, $B(2;6-m).$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi:

$(33 – m)(6 – m) < 0$ $\Leftrightarrow 6 < m < 33.$

Mà $m \in Z$ $\Rightarrow m \in \{ 7;8;9; \ldots ;31;32\}$ nên tổng cần tìm là:

$S = 7 + 8 + 9 + \ldots + 32 = 507.$

> **Đáp án: A**

## Bài 5. Biết đồ thị hàm số $f(x) = {x^3} – 3{x^2} + 2m – 4$ cắt trục hoành tại đúng hai điểm phân biệt. Khi đó $m$ có giá trị thuộc khoảng nào sau đây?

A. $(-1;3).$

B. $(3;7).$

C. $(-5;-1).$

D. $(7;10).$

Ta có $f(x) = {x^3} – 3{x^2} + 2m – 4$ $\Rightarrow f'(x) = 3{x^2} – 6x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Do đó đồ thị hàm số có hai điểm cực trị là $A(0;2m – 4)$, $B(2;2m).$

Để đồ thị hàm số cắt trục hoành tại đúng hai điểm phân biệt khi:

$(2m – 4).2m = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{m = 2}
\end{array}} \right..
$$

> **Đáp án: A**

## Bài 6. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = \frac{1}{3}{x^3} + m{x^2} – m$ cắt trục hoành tại một điểm duy nhất.

A. $\left( { – \frac{{\sqrt 3 }}{2};\frac{{\sqrt 3 }}{2}} \right)\backslash \{ 0\} .$

B. $\left( { – \frac{{\sqrt 3 }}{2};\frac{{\sqrt 3 }}{2}} \right).$

C. $\left( { – \infty ; – \frac{{\sqrt 3 }}{2}} \right) \cup \left( {\frac{{\sqrt 3 }}{2}; + \infty } \right).$

D. $m \in \left[ { – \frac{{\sqrt 3 }}{2};\frac{{\sqrt 3 }}{2}} \right].$

Ta có $f(x) = \frac{1}{3}{x^3} + m{x^2} – m$ $\Rightarrow f'(x) = {x^2} + 2mx = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = – 2m}
\end{array}} \right..
$$

Trường hợp 1: Nếu $– 2m = 0$ $\Leftrightarrow m = 0$, khi đó hàm số không có cực trị và đồ thị chỉ cắt trục hoành tại một điểm duy nhất nên $m = 0$ thỏa mãn bài toán.

Trường hợp 2: Nếu $– 2m \ne 0$ $\Leftrightarrow m \ne 0.$

Khi đó đồ thị hàm số có hai điểm cực trị là $A(0; – m)$, $B\left( { – 2m;\frac{4}{3}{m^3} – m} \right).$

Để đồ thị hàm số cắt trục hoành tại một điểm duy nhất khi:

$$
\left\{ {\begin{array}{l}
{( – m)\left( {\frac{4}{3}{m^3} – m} \right) > 0}\\
{m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2}\left( {1 – \frac{4}{3}{m^2}} \right) > 0}\\
{m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{1 – \frac{4}{3}{m^2} > 0}\\
{m \ne 0}
\end{array}} \right..
$$

$\Leftrightarrow m \in \left( { – \frac{{\sqrt 3 }}{2};\frac{{\sqrt 3 }}{2}} \right)\backslash \{ 0\} .$

Từ hai trường hợp, ta có điều kiện cần tìm là $m \in \left( { – \frac{{\sqrt 3 }}{2};\frac{{\sqrt 3 }}{2}} \right).$

> **Đáp án: B**

## Bài 7. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 4{x^2} + (m + 1)x + 6 – 2m$ cắt trục hoành tại ba điểm phân biệt.

A. $( – \infty ;3) \cup (3;4).$

B. $( – \infty ;4).$

C. $(4; + \infty ).$

D. $(0;3).$

Phương trình hoành độ giao điểm của đồ thị hàm số đã cho với trục hoành là:

${x^3} – 4{x^2} + (m + 1)x + 6 – 2m = 0$ $\Leftrightarrow m(x – 2) + {x^3} – 4{x^2} + x + 6 = 0.$

$\Leftrightarrow m(x – 2) + (x – 2)\left( {{x^2} – 2x – 3} \right) = 0$ $\Leftrightarrow (x – 2)\left( {{x^2} – 2x – 3 + m} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2}\\
{g(x) = {x^2} – 2x – 3 + m = 0\:\:(1)}
\end{array}} \right..
$$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt khi và chỉ khi phương trình $(1)$ có hai nghiệm phân biệt khác $2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = 1 – (m – 3) > 0}\\
{g(2) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{4 – m > 0}\\
{m – 3 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m < 4}\\
{m \ne 3}
\end{array}} \right..
$$

> **Đáp án: A**

## Bài 8. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc khoảng $( – 15;15)$ để đồ thị hàm số $f(x) = {x^3} + 2(1 – m){x^2} – 3mx + 2$ cắt đường thẳng $d:y = – 2x – 2m – 2$ tại ba điểm phân biệt?

A. $27.$

B. $24.$

C. $25.$

D. $23.$

Phương trình hoành độ giao điểm của đồ thị hàm số đã cho với đường thẳng $d$ là:

${x^3} + 2(1 – m){x^2} – 3mx + 2$ $= – 2x – 2m – 2.$

$\Leftrightarrow {x^3} + 2(1 – m){x^2}$ $+ (2 – 3m)x + 2m + 4 = 0.$

$\Leftrightarrow m\left( { – 2{x^2} – 3x + 2} \right)$ $+ {x^3} + 2{x^2} + 2x + 4 = 0.$

$\Leftrightarrow m(x + 2)( – 2x + 1)$ $+ (x + 2)\left( {{x^2} + 2} \right) = 0.$

$\Leftrightarrow (x + 2)\left( {{x^2} – 2mx + m + 2} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 2}\\
{g(x) = {x^2} – 2mx + m + 2 = 0\:\:(1)}
\end{array}} \right..
$$

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt khi $(1)$ có hai nghiệm phân biệt khác $–2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {m^2} – m – 2 > 0}\\
{g( – 2) = 4 + 4m + m + 2 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\left[ {\begin{array}{l}
{m > 2}\\
{m < – 1}
\end{array}} \right.}\\
{m \ne – \frac{6}{5}}
\end{array}} \right..
$$

Mà $m \in Z$, $m \in ( – 15;15)$ $\Rightarrow m \in \{ – 14; – 13; \ldots ; – 2;3;4;5; \ldots ;14\} .$

> **Đáp án: C**

## Bài 9. Biết đồ thị hàm số $f(x) = {x^3} + 3{x^2} – x – 3m – 2$ cắt trục hoành tại ba điểm phân biệt cách đều nhau. Khi đó giá trị của tham số $m$ thuộc khoảng nào sau đây?

A. $\left( {0;\frac{1}{4}} \right)$.

B. $\left( {\frac{1}{4};\frac{1}{2}} \right)$.

C. $\left( {\frac{1}{2};\frac{3}{4}} \right)$.

D. $\left( {\frac{3}{4};1} \right)$.

Ta có phương trình hoành độ giao điểm: ${x^3} + 3{x^2} – x – 3m – 2 = 0$ $(1).$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt cách đều nhau thì ba giao điểm này phải có hoành độ lập thành cấp số cộng. Khi đó phương trình $(1)$ có ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ theo thứ tự lập thành cấp số cộng.

Khi đó ta có ${x_1} + {x_2} + {x_3}$ $= – \frac{b}{q} = – 3$ mà ${x_1} + {x_3} = 2{x_2}$ $\Rightarrow {x_1} + {x_2} + {x_3} = 3{x_2}.$

Do đó ${x_2} = – 1.$

Thay ${x_2} = – 1$ vào phương trình $(1)$ ta có: $– 1 + 3 + 1 – 3m – 2 = 0$ $\Leftrightarrow m = \frac{1}{3}.$

> **Đáp án: B**

## Bài 10. Biết đồ thị hàm số $f(x) = {x^3} – (2m + 1){x^2} – (m + 5)x + 8$ cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành một cấp số nhân khi $m = {m_0}.$ Tính giá trị biểu thức $T = 2{m_0} + 3m_0^3 – 1.$

A. $27.$

B. $-1.$

C. $-6.$

D. $4.$

Ta có phương trình hoành độ giao điểm: ${x^3} – (2m + 1){x^2} – (m + 5)x + 8 = 0$ $(1).$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt có hoành độ lập thành cấp số nhân thì phương trình $(1)$ có ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ theo thứ tự lập thành cấp số nhân.

Khi đó ta có ${x_1}{x_2}{x_3} = – \frac{d}{a} = – 8$ mà ${x_1}{x_3} = x_2^2$ $\Rightarrow {x_1}{x_2}{x_3} = x_2^3.$ Do đó ${x_2} = – 2.$

Thay ${x_2} = – 2$ vào phương trình $(1)$ ta có:

${( – 2)^3} – (2m + 1){( – 2)^2}$ $– (m + 5)( – 2) + 8 = 0$ $\Leftrightarrow m = 1.$

Do đó ${m_0} = 1$ $\Rightarrow T = 4.$

> **Đáp án: D**

## Bài 11. Cho hàm số $y = {x^3} – \frac{9}{2}{x^2} + 6x + m$ ($m$ là tham số) có đồ thị $(C).$ Biết rằng $(C)$ cắt trục hoành tại ba điểm phân biệt có hoành độ tương ứng là ${x_1}$, ${x_2}$, ${x_3}$ với ${x_1} < {x_2} < {x_3}.$ Khẳng định nào sau đây đúng?

A. $1 < {x_1} < 2 < {x_2} < 3 < {x_3}.$

B. $1 < {x_1} < {x_2} < 2 < {x_3} < 3.$

C. $0 < {x_1} < 1 < {x_2} < {x_3} < 3.$

D. ${x_1} < 0 < {x_2} < 1 < {x_3} < 2.$

Ta có $y = {x^3} – \frac{9}{2}{x^2} + 6x + m$ $\Rightarrow f'(x) = 3{x^2} – 9x + 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = 2}
\end{array}} \right..
$$

Ta có bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so-4.png" alt="">

Để đồ thị hàm số cắt trục hoành tại ba điểm phân biệt thì:

$(m + 2)\left( {m + \frac{5}{2}} \right) < 0$ $\Leftrightarrow – \frac{5}{2} < m < – 2.$

Khi đó $f(0) < 0$, $f(3) = m + \frac{9}{2} > 0.$

Ta có $f(0).f(1) < 0$, $f(1).f(2) < 0$, $f(2).f(3) < 0.$

Do đó trên mỗi khoảng này phương trình $f(x) = 0$ đều có một nghiệm.

Vì vậy $0 < {x_1} < 1 < {x_2} < 2 < {x_3} < 3.$

Chú ý: Trong trường hợp ta đã lấy được điều kiện $– \frac{5}{2} < m < – 2$, ta có thể lấy một giá trị bất kì của $m$ trong khoảng này thay vào máy tính bỏ túi, kiểm tra xem phương trình $f(x)=0$ và xác định các nghiệm tương ứng của phương trình thì ta cũng thấy các nghiệm khi đó thỏa mãn đáp án C nên đáp án C đúng.

> **Đáp án: C**

## Bài 12. Đồ thị hàm số $y = {x^3} – m{x^2} + 4$ cắt trục hoành tại ba điểm phân biệt có hoành độ ${x_1}$, ${x_2}$, ${x_3}$ thoả mãn ${x_1} < 1 < {x_2} < {x_3}$ khi:

A. $m >5.$

B. $3<m< 5.$

C. $m< 3.$

D. $m=3.$

Ta có $y = {x^3} – m{x^2} + 4$ $\Rightarrow f'(x) = 3{x^2} – 2mx = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \frac{2}{3}m}
\end{array}} \right..
$$

Để đồ thị hàm số đã cho cắt trục hoành tại ba điểm phân biệt thì:

$$
\left\{ {\begin{array}{l}
{\frac{2}{3}m \ne 0 \Leftrightarrow m \ne 0}\\
{f(0).f\left( {\frac{2}{3}m} \right) < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{4\left( {4 – \frac{8}{{27}}{m^3}} \right) < 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > 3.$

Đồ thị hàm số khi đó có dạng:

<img link="data_for_rag/toan12/images/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so-5.png" alt="">

Từ đồ thị hàm số, yêu cầu bài toán $\Leftrightarrow f(1) = 5 – m > 0$ $\Leftrightarrow 5 > m.$

Vậy điều kiện cần tìm là $3 < m <5.$

> **Đáp án: B**

## Bài 13. Tìm tất cả giá trị thực của tham số $m$ để đường thẳng $d$ đi qua điểm $M(1;1)$ có hệ số góc $m$ cắt đồ thị $(C):y = {x^3} – 3{x^2} + 1$ tại ba điểm $D$, $E$, $F$ với ${x_D} < {x_E} < {x_F}$ sao cho tam giác $ODF$ cân tại $O$ (với $O$ là gốc toạ độ).

A. $m=-1.$

B. $m=1.$

C. $m=2.$

D. $m=-2.$

Phương trình đường thẳng $d:y = m(x – 1) – 1$ $= mx – m – 1.$

Xét phương trình hoành độ giao điểm của đường thẳng $d$ và đồ thị $(C):$

${x^3} – 3{x^2} + 1 = mx – m – 1$ $\Leftrightarrow (x – 1)\left( {{x^2} – 2x – 2 – m} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{{x^2} – 2x – 2 – m = 0\:\:(1)}
\end{array}} \right..
$$

$(d)$ cắt $(C)$ tại ba điểm phân biệt $D$, $E$, $F$ $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $1.$

$(1) \Leftrightarrow {(x – 1)^2} = m + 3$ có hai nghiệm phân biệt khác $1$ khi và chỉ khi $m>-3.$

Khi đó $(1)$ có hai nghiệm ${x_1} = 1 – \sqrt {m + 3}$, ${x_2} = 1 + \sqrt {m + 3}$ thỏa ${x_1} < 1 < {x_2}.$

Gọi $D(1 – \sqrt {m + 3} ; – m\sqrt {m + 3} – 1)$, $E(1; – 1)$, $F(1 + \sqrt {m + 3} ;m\sqrt {m + 3} – 1).$

Tam giác $DFO$ cân tại $O$ $\Leftrightarrow DO = FO$ $\Leftrightarrow D{O^2} = F{O^2}.$

$\Leftrightarrow {(1 – \sqrt {m + 3} )^2} + {( – m\sqrt {m + 3} – 1)^2}$ $= {(1 + \sqrt {m + 3} )^2} + {(m\sqrt {m + 3} – 1)^2}.$

$\Leftrightarrow 4\sqrt {m + 3} – 4m\sqrt {m + 3} = 0$ $\Leftrightarrow 4(m – 1)\sqrt {m + 3} = 0$ $\Leftrightarrow m = 1.$

Với $m =1$ ta có $D( – 1; – 3)$, $E(1; – 1)$, $F(3;1)$ thỏa mãn.

> **Đáp án: B**

## Bài 14. Cho hàm số $y = {x^3} – m{x^2} + 3x + 1$ và $M(1; – 2).$ Biết có hai giá trị của $m$ là ${m_1}$ và ${m_2}$ để đường thẳng $\Delta :y = x + 1$ cắt đồ thị tại ba điểm phân biệt $A(0;1)$, $B$ và $C$ sao cho tam giác $MBC$ có diện tích bằng $4\sqrt 2 .$ Tổng $m_1^2 + m_2^2$ thuộc khoảng nào dưới đây?

A. $(15;17).$

B. $(3;5).$

C. $(31;33).$

D. $(16;18).$

Ta có phương trình hoành độ giao điểm ${x^3} – m{x^2} + 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{{x^2} – mx + 2 = 0}
\end{array}} \right..
$$

Suy ra hoành độ $B$ và $C$ là nghiệm phương trình ${x^2} – mx + 2 = 0.$

Ta có $\Delta = {m^2} – 8$ và $S = m$, $P = 2.$

Để đường thẳng $\Delta :y = x + 1$ cắt đồ thị tại ba điểm phân biệt $A(0;1)$, $B$ và $C$ khi phương trình ${x^2} – mx + 2 = 0$ có hai nghiệm phân biệt khác $0$ hay $\Delta = {m^2} – 8 > 0$ $\Leftrightarrow |m| > 2\sqrt 2 .$

Khi đó $d(M;\Delta ) = 2\sqrt 2$, $BC = \left| {{x_1} – {x_2}} \right|.\sqrt 2$ với ${x_1}$, ${x_2}$ là hai nghiệm phương trình ${x^2} – mx + 2 = 0.$

Thay vào ${S_{\Delta MBC}} = \frac{1}{2}d(M;\Delta ).BC$ $= \frac{1}{2}.2\sqrt 2 .\left| {{x_1} – {x_2}} \right|.\sqrt 2$ $= 4\sqrt 2 .$

$\Leftrightarrow {S^2} – 4P = 8$ $\Leftrightarrow {m^2} – 8 = 8$ $\Leftrightarrow m = \pm 4$ $\Rightarrow m_1^2 + m_2^2$ $= {4^2} + {( – 4)^2} = 32.$

> **Đáp án: C**

## Bài 15. Cho hàm số $y = {x^3} – 2(m – 1){x^2}$ $+ 2\left( {{m^2} – 2m} \right)x + 4{m^2}$ có đồ thị $(C)$ và đường thẳng $d:y=4x+8.$ Đường thẳng $d$ cắt đồ thị $(C)$ tại ba điểm phân biệt có hoành độ ${x_1}$, ${x_2}$, ${x_3}.$ Tìm giá trị lớn nhất ${P_{\max }}$ của biểu thức $P = x_1^3 + x_2^3 + x_3^3.$

A. ${P_{\max }} = 16\sqrt 2 – 6.$

B. ${P_{\max }} = 16\sqrt 2 – 8.$

C. ${P_{\max }} = 23 – 6\sqrt 2 .$

D. ${P_{\max }} = 24 – 6\sqrt 2 .$

Xét phương trình hoành độ giao điểm của đường thẳng $d$ và đồ thị $(C)$ là:

${x^3} – 2(m – 1){x^2}$ $+ 2\left( {{m^2} – 2m} \right)x + 4{m^2}$ $= 4x + 8$ $(1).$

$\Leftrightarrow {x^3} – 2(m – 1){x^2}$ $+ 2\left( {{m^2} – 2m – 2} \right)x$ $+ 4{m^2} – 8 = 0.$

$\Leftrightarrow (x + 2)\left( {{x^2} – 2mx + 2{m^2} – 4} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 2}\\
{{x^2} – 2mx + 2{m^2} – 4 = 0\:\:(2)}
\end{array}} \right..
$$

Đường thẳng $d$ cắt đồ thị $(C)$ tại ba điểm phân biệt $\Leftrightarrow (1)$ có ba nghiệm phân biệt $\Leftrightarrow (2)$ có hai nghiệm phân biệt khác $-2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ = {m^2} – 2{m^2} + 4 > 0}\\
{4 + 4m + 2{m^2} – 4 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0,m \ne – 2}\\
{4 – {m^2} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{ – 2 < m < 2}
\end{array}} \right..
$$

Khi đó đường thẳng $d$ cắt đồ thị $(C)$ tại ba điểm phân biệt ${x_1}$, ${x_2}$, ${x_3}$, giả sử ${x_3} = – 2$ và ${x_1}$, ${x_2}$ là hai nghiệm của phương trình $(2).$

Theo định lý Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = 2m}\\
{{x_1}{x_2} = 2{m^2} – 4}
\end{array}} \right..
$$

Vậy $P = x_1^3 + x_2^3 + x_3^3$ $= x_1^3 + x_2^3 – 8.$

$= {\left( {{x_1} + {x_2}} \right)^3} – 3{x_1}{x_2}\left( {{x_1} + {x_2}} \right)$ $= 8{m^3} – 3.2m\left( {2{m^2} – 4} \right) – 8$ $= – 4{m^3} + 24m – 8.$

Đặt $f(m) = – 4{m^3} + 24m – 8$ trên $[ – 2;2].$

Ta có $f'(m) = – 12{m^2} + 24 = 0$, $f'(m) = 0$ $\Leftrightarrow m = \pm \sqrt 2 .$

Ta có $f( – 2) = – 24$, $f(2) = 8$, $f(\sqrt 2 ) = – 8 + 16\sqrt 2$, $f( – \sqrt 2 ) = – 8 – 16\sqrt 2 .$

Vậy ${P_{\max }} = 16\sqrt 2 – 8.$

> **Đáp án: B**

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-bac-ba-chua-tham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Biết đồ thị hàm số $f(x) = {x^3} – 3{x^2} + 2m – 4$ cắt trục hoành tại đúng hai điểm phân biệt. Khi đó $m$ có giá trị thuộc khoảng nào sau đây?

A. $(-1;5).$

B. $(5;7).$

C. $(-5;-1).$

D. $(7;10).$

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3{x^2} + m – 5$ cắt trục hoành tại ba điểm phân biệt.

A. $(3;6).$

B. $(5;9).$

C. $(0;5).$

D. $(-2;0).$

## Bài 3. Tìm tất cả các giá trị của tham số $m$ để đồ thị hàm số $f(x) = {x^3} – 3{x^2} + m – 5$ cắt trục hoành tại ba điểm phân biệt.

A. $( – \infty ; – 1).$

B. $( – 2;0).$

C. $( – \infty ; – 2) \cup (0; + \infty ).$

D. $( – \infty ; – 3) \cup (3; + \infty ).$

## Bài 4. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc $[-8;8]$ để đồ thị hàm số $f(x) = \frac{1}{3}{x^3} + {x^2} – 3x + 1 – m$ cắt trục hoành tại một điểm duy nhất.

A. $7.$

B. $8.$

C. $17.$

D. $6.$

## Bài 5. Có bao nhiêu giá trị nguyên của tham số $m$ thuộc $(-2;10)$ để đồ thị hàm số $f(x) = {x^3} – 2{x^2} + x + 1 + m$ cắt trục hoành tại một điểm duy nhất.

A. $11.$

B. $10.$

C. $12.$

D. $13.$

## Bài 6. Tìm tất cả các giá trị của $m$ để đồ thị hàm số $y = {x^3} – 3x + 2$ cắt đường thẳng $y = m – 1$ tại ba điểm phân biệt.

A. $0 < m < 4.$

B. $1 < m \le 5.$

C. $1 < m < 5.$

D. $1 \le m < 5.$

## Bài 7. Cho hàm số $y = {x^3} – 3x + 2$ có đồ thị $(C).$ Gọi $d$ là đường thẳng đi qua điểm $A(3;20)$ và có hệ số góc là $m.$ Với giá trị nào của $m$ thì $d$ cắt $(C)$ tại ba điểm phân biệt:

A. 
$$
\left\{ {\begin{array}{l}
{m < \frac{{15}}{4}}\\
{m \ne 24}
\end{array}} \right.
$$
.

B. 
$$
\left\{ {\begin{array}{l}
{m < \frac{1}{5}}\\
{m \ne 0}
\end{array}} \right..
$$

C. 
$$
\left\{ {\begin{array}{l}
{m > \frac{{15}}{4}}\\
{m \ne 24}
\end{array}} \right..
$$

D. 
$$
\left\{ {\begin{array}{l}
{m > \frac{1}{5}}\\
{m \ne 1}
\end{array}} \right..
$$

## Bài 8. Biết đường thẳng $y = (3m – 1)x + 6m + 3$ cắt đồ thị hàm số $y = {x^3} – 3{x^2} + 1$ tại ba điểm phân biệt sao cho có một giao điểm cách đều hai giao điểm còn lại. Khi đó $m$ thuộc khoảng nào dưới đây?

A. $(-1;0).$

B. $(0;1).$

C. $\left( {1;\frac{3}{2}} \right).$

D. $\left( {\frac{3}{2};2} \right).$

## Bài 9. Cho $\left( {{C_m}} \right):y = 2{x^3} – (3m + 3){x^2} + 6mx – 4.$ Gọi $T$ là tập giá trị của $m$ thỏa mãn $\left( {{C_m}} \right)$ có đúng hai điểm chung với trục hoành, tính tổng $S$ các phần tử của $T.$

A. $S = 7.$

B. $S = \frac{8}{3}.$

C. $S = 6.$

D. $S = \frac{2}{3}.$

## Bài 10. Có bao nhiêu giá trị nguyên của tham số $m$ để đồ thị hàm số $y = {x^3} – 3{x^2} + 2m – 1$ cắt trục hoành tại ba điểm phân biệt có hoành độ ${x_1}$, ${x_2}$, ${x_3}$ thỏa mãn ${x_1} < 1 < {x_2} < {x_3}.$

A. $1.$

B. $2.$

C. $3.$

D. $0.$

## V. ĐÁP ÁN BÀI TẬP TỰ LUYỆN

1. A.

2. B.

3. B.

4. B.

5. B.

6. C.

7. C.

8. A.

9. B.

10. A.