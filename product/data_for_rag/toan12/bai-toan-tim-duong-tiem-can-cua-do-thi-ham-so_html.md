# Bài toán tìm đường tiệm cận của đồ thị hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
TOANMATH.com giới thiệu bài viết hướng dẫn giải bài toán tìm đường tiệm cận của đồ thị hàm số trong chương trình Giải tích 12 chương 1.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## I. TIỆM CẬN ĐỨNG
Đường thẳng $x = {x_0}$ được gọi là tiệm cận đứng của đồ thị hàm số $y = f(x)$ nếu ít nhất một trong các điều kiện sau được thỏa mãn:

$\mathop {\lim }\limits_{x \to x_0^ – } f(x) = + \infty .$

$\mathop {\lim }\limits_{x \to x_0^ + } f(x) = + \infty .$

$\mathop {\lim }\limits_{x \to x_0^ – } f(x) = – \infty .$

$\mathop {\lim }\limits_{x \to x_0^ + } f(x) = – \infty .$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## II. TIỆM CẬN NGANG

Đường thẳng $y = {y_0}$ được gọi là tiệm cận ngang của đồ thị hàm số $y = f(x)$ nếu ít nhất một trong các điều kiện sau được thỏa mãn:

$\mathop {\lim }\limits_{x \to + \infty } y = {y_0}.$

$\mathop {\lim }\limits_{x \to – \infty } y = {y_0}.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## III. TIỆM CẬN XIÊN

Đường thẳng $y = ax + b$ $(a \ne 0)$ được gọi là tiệm cận xiên của đồ thị hàm số $y = f(x)$ nếu ít nhất một trong các điều kiện sau được thỏa mãn:

$\mathop {\lim }\limits_{x \to + \infty } \left[ {f(x) – (ax + b)} \right] = 0.$

$\mathop {\lim }\limits_{x \to – \infty } \left[ {f(x) – (ax + b)} \right] = 0.$

Chú ý: Để xác định các hệ số $a$, $b$ trong phương trình của tiệm cận xiên ta có thể áp dụng các công thức sau:

$a = \mathop {\lim }\limits_{x \to + \infty } \frac{{f(x)}}{x}$ $(a \ne 0)$, $b = \mathop {\lim }\limits_{x \to + \infty } [f(x) – ax]$ hoặc $a = \mathop {\lim }\limits_{x \to – \infty } \frac{{f(x)}}{x}$ $(a \ne 0)$, $b = \mathop {\lim }\limits_{x \to – \infty } [f(x) – ax].$

Nếu $a = 0$ thì ta có tiệm cận ngang.

<!-- chunk:4 level:2 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## Vấn đề 1: Tìm tiệm cận đứng của đồ thị hàm số.

1. PHƯƠNG PHÁP

+ Tìm tập xác định.

+ Tìm các giới hạn: $\mathop {\lim }\limits_{x \to x_0^ + \left( {x_0^ – } \right)} f(x)$ trong đó ${x_0}$ là các điểm đầu khoảng xác định.

+ Nếu một trong giới hạn trên bằng $\pm \infty$ thì đường thẳng $x = {x_0}$ là tiệm cận đứng của đồ thị hàm số.

2. CÁC VÍ DỤ

Ví dụ: Tìm các tiệm cận đứng của đồ thị các hàm số sau:

a) $y = \frac{{3x – 7}}{{4x – 4}}.$

b) $y = \frac{{3x – 8}}{{{x^2} – 3x + 2}}.$

c) $y = \frac{{2x + 5}}{{\sqrt {x – 3} }}.$

d) $y = \frac{{x – 3}}{{{x^2} + 9}}.$

e) $y = \frac{{x – 2}}{{{x^2} – 3x + 2}}.$

a) Tập xác định: $D = R\backslash \left\{ 1 \right\}.$

$\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{3x – 7}}{{4x – 4}} = – \infty$ và $\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{3x – 7}}{{4x – 4}} = + \infty .$

Vậy đồ thị có tiệm cận đứng là $x = 1.$

b) Tập xác định: $D = R\backslash \{ 1;2\} .$

$\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{3x – 8}}{{(x – 1)(x – 2)}} = – \infty$ và $\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{3x – 8}}{{(x – 1)(x – 2)}} = + \infty .$

$\Rightarrow x = 1$ là một tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to {2^ – }} y = \mathop {\lim }\limits_{x \to {2^ – }} \frac{{3x – 8}}{{(x – 1)(x – 2)}} = + \infty$ và $\mathop {\lim }\limits_{x \to {2^ + }} y = \mathop {\lim }\limits_{x \to {2^ + }} \frac{{3x – 8}}{{(x – 1)(x – 2)}} = – \infty .$

$\Rightarrow x = 1$ là một tiệm cận đứng của đồ thị.

Vậy đồ thị hàm số có hai tiệm cận đứng là $x = 1$ và $x = 2.$

c) Tập xác định: $D = (3; + \infty ).$

$\mathop {\lim }\limits_{x \to {3^ + }} y = \mathop {\lim }\limits_{x \to {3^ + }} \frac{{2x + 5}}{{\sqrt {x – 3} }} = + \infty$ $\Rightarrow x = 3$ là tiệm cận đứng của đồ thị hàm số.

Chú ý: Vì tập xác định là $(3; + \infty )$ nên ta chỉ xét giới hạn khi $x \to {3^ + }.$

d) Tập xác định: $D = R.$

Vì tập xác định của hàm số là $R$ nên đồ thị hàm số không có tiệm cận đứng.

e) Tập xác định: $D = R\backslash \{ 1;2\} .$

$\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{x – 2}}{{{x^2} – 3x + 2}}$ $= \mathop {\lim }\limits_{x \to {1^ + }} \frac{1}{{x – 1}} = + \infty .$

$\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{x – 2}}{{{x^2} – 3x + 2}}$ $= \mathop {\lim }\limits_{x \to {1^ – }} \frac{1}{{x – 1}} = – \infty .$

Nên $x = 1$ là tiệm cận đứng của đồ thị hàm số.

$\mathop {\lim }\limits_{x \to 2} y = \mathop {\lim }\limits_{x \to 2} \frac{{x – 2}}{{{x^2} – 3x + 2}}$ $= \mathop {\lim }\limits_{x \to 2} \frac{1}{{x – 1}} = 1.$

Nên $x = 2$ không là tiệm cận đứng của đồ thị hàm số.

Vậy đồ thị hàm số có một tiệm cận đứng là $x = 1.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## Vấn đề 2: Tìm tiệm cận ngang của đồ thị hàm số.

1. PHƯƠNG PHÁP

+ Tìm tập xác định.

+ Tìm các giới hạn: $\mathop {\lim }\limits_{x \to + \infty ( – \infty )} f(x).$

+ Nếu một trong giới hạn trên bằng $b$ thì đường thẳng $y = b$ là tiệm cận ngang của đồ thị hàm số.

2. VÍ DỤ

Ví dụ: Tìm các tiệm cận ngang của đồ thị các hàm số sau:

a) $y = \frac{{{x^2} + 2x + 3}}{{5 – 4x – {x^2}}}.$

b) $y = \frac{{\sqrt {{x^2} – 1} + 5x + 3}}{{2x + 2}}.$

a) Tập xác định: $D = R\backslash \{ 1; – 5\} .$

$\mathop {\lim }\limits_{x \to \pm \infty } y = \mathop {\lim }\limits_{x \to \pm \infty } \frac{{{x^2} + 2x + 3}}{{5 – 4x – {x^2}}}$ $= \mathop {\lim }\limits_{x \to \pm \infty } \frac{{1 + \frac{2}{x} + \frac{3}{{{x^2}}}}}{{\frac{5}{{{x^2}}} – \frac{4}{x} – 1}} = – 1.$

Suy ra đường $y = -1$ là tiệm cận ngang của đồ thị hàm số.

b) Tập xác định: $D = ( – \infty ; – 1) \cup [1; + \infty ).$

$\mathop {\lim }\limits_{x \to + \infty } y = \mathop {\lim }\limits_{x \to + \infty } \frac{{\sqrt {{x^2} – 1} + 5x + 3}}{{2x + 2}}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{\sqrt {1 – \frac{1}{{{x^2}}}} + 5 + \frac{3}{x}}}{{2 + \frac{2}{x}}} = 3.$

Suy ra đường $y = 3$ là tiệm cận ngang của đồ thị khi $x \to + \infty .$

$\mathop {\lim }\limits_{x \to – \infty } y = \mathop {\lim }\limits_{x \to – \infty } \frac{{\sqrt {{x^2} – 1} + 5x + 3}}{{2x + 2}}$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{ – \sqrt {1 – \frac{1}{{{x^2}}}} + 5 + \frac{3}{x}}}{{2 + \frac{2}{x}}} = 2.$

Suy ra đường $y = 2$ là tiệm cận ngang của đồ thị khi $x \to – \infty .$

<!-- chunk:6 level:2 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## Vấn đề 3: Tìm tiệm cận xiên của đồ thị hàm số.

1. PHƯƠNG PHÁP

+ Tìm tập xác định.

+ Tìm các giới hạn:

Nếu $f(x) = ax + b + \frac{c}{{mx + n}}$ thì $\mathop {\lim }\limits_{x \to \pm \infty } [f(x) – (ax + b)] = 0$ nên $y = ax + b$ là tiệm cận xiên (hay ngang) của đồ thị hàm số.

+ Nếu $f(x)$ chưa viết được như trên thì ta tìm $a$, $b$ theo cách sau:

$a = \mathop {\lim }\limits_{x \to + \infty } \frac{{f(x)}}{x}$ $(a \ne 0)$, $b = \mathop {\lim }\limits_{x \to + \infty } [f(x) – ax]$ hoặc $a = \mathop {\lim }\limits_{x \to – \infty } \frac{{f(x)}}{x}$ $(a \ne 0)$, $b = \mathop {\lim }\limits_{x \to – \infty } [f(x) – ax].$

Chú ý: Nếu $a = 0$ thì ta có đường tiệm cận tìm được là tiệm cận ngang.

2. CÁC VÍ DỤ

Ví dụ: Tìm các tiệm cận xiên của đồ thị các hàm số sau:

a) $y = 4x + 5 + \frac{7}{{2x – 8}}.$

b) $y = \sqrt {{x^2} – 4x} + 4x.$

a) Tập xác định: $D = R\backslash \{ 4\} .$

$\mathop {\lim }\limits_{x \to \pm \infty } [y – (4x + 5)] = \mathop {\lim }\limits_{x \to \pm \infty } \frac{7}{{2x – 8}} = 0.$

Suy ra đường thẳng $y = 4x + 5$ là tiệm cận xiên của đồ thị hàm số.

b) Tập xác định: $D = ( – \infty ;0] \cup [4; + \infty ).$

+ Khi $x \to + \infty$:

$a = \mathop {\lim }\limits_{x \to + \infty } \frac{y}{x} = \mathop {\lim }\limits_{x \to + \infty } \frac{{\sqrt {{x^2} – 4x} + 4x}}{x}$ $= \mathop {\lim }\limits_{x \to + \infty } \left( {\sqrt {1 – \frac{4}{x}} + 4} \right) = 5.$

$b = \mathop {\lim }\limits_{x \to + \infty } (y – 5x)$ $= \mathop {\lim }\limits_{x \to + \infty } \left( {\sqrt {{x^2} – 4x} – x} \right)$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{{x^2} – 4x – {x^2}}}{{\sqrt {{x^2} – 4x} + x}}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{ – 4}}{{\sqrt {1 – \frac{4}{x}} + 1}} = – 2.$

Vậy khi $x \to + \infty$ thì đồ thị có tiệm cận xiên là $y = 5x – 2.$

+ Khi $x \to – \infty$:

$a = \mathop {\lim }\limits_{x \to – \infty } \frac{y}{x}$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{\sqrt {{x^2} – 4x} + 4x}}{x}$ $= \mathop {\lim }\limits_{x \to – \infty } \left( { – \sqrt {1 – \frac{4}{x}} + 4} \right) = 3.$

$b = \mathop {\lim }\limits_{x \to – \infty } (y – 3x)$ $= \mathop {\lim }\limits_{x \to – \infty } \left( {\sqrt {{x^2} – 4x} + x} \right)$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{{x^2} – 4x – {x^2}}}{{\sqrt {{x^2} – 4x} – x}}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{ – 4}}{{ – \sqrt {1 – \frac{4}{x}} – 1}} = 2.$

Vậy khi $x \to – \infty$ thì đồ thị có tiệm cận xiên là $y = 3x + 2.$

<!-- chunk:7 level:1 source:https://toanmath.com/2019/07/bai-toan-tim-duong-tiem-can-cua-do-thi-ham-so.html -->
## C. BÀI TẬP
 1. Tìm các tiệm cận của đồ thị các hàm số sau:

a) $y = \frac{{2x + 3}}{{4 – {x^2}}}.$

b) $y = \frac{{3{x^2} + 9x – 12}}{{{x^2} + x – 2}}.$

c) $y = 2x – 5 + \frac{2}{{3 – x}}.$

d) $y = \frac{{3{x^2} + 4x – 4}}{{x – 3}}.$

2. Tìm các tiệm cận của đồ thị các hàm số sau:

a) $y = 2x – 4 + \sqrt {{x^2} – 4x + 3} .$

b) $y = \frac{{x + 1}}{{\sqrt {{x^2} + 1} }}.$

3. Cho $\left( {{C_m}} \right):y = \frac{{2{x^2} + (m + 1)x – 3}}{{x + m}}.$

a) Định $m$ để tiệm cận xiên của $\left( {{{\rm{C}}_m}} \right)$ đi qua $A(1;5).$

b) Tìm $m$ để giao điểm $2$ tiệm cận của $\left( {{C_m}} \right)$ thuộc $(P):y = {x^2} – 3.$

4. Cho $(C):y = \frac{{{x^2} – 2x – 15}}{{x – 3}}.$ Chứng minh rằng tích các khoảng cách từ điểm $M$ bất kỳ trên $(C)$ đến hai tiệm cận của $(C)$ bằng một hằng số.

5. Cho $\left( {{C_m}} \right):y = \frac{{{x^2} + mx – 1}}{{x – 1}}.$ Tìm $m$ sao cho tiệm cận xiên của $\left( {{C_m}} \right)$ tạo với hai trục toạ độ một tam giác có diện tích bằng $2.$

6. Tìm những điểm trên (C): $(C):y = \frac{{2{x^2} + x – 1 + 4\sqrt 5 }}{{x + 1}}$ sao cho tổng khoảng cách từ điểm đó đến hai tiệm cận là nhỏ nhất.