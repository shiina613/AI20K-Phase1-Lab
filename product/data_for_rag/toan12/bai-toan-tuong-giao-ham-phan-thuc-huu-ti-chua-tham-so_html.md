# Bài toán tương giao hàm phân thức hữu tỉ chứa tham số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
Bài viết hướng dẫn phương pháp tìm điều kiện tham số liên quan đến bài toán tương giao của hàm phân thức hữu tỉ trong chương trình Giải tích 12: ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN
Cho hàm số có dạng: $y = \frac{{ax + b}}{{cx + d}}$ (điều kiện $ad – bc \ne 0$).

Đường thẳng $d:y = mx + n.$

Phương trình hoành độ giao điểm của hai đồ thị là:

$\frac{{ax + b}}{{cx + d}} = mx + n$ (điều kiện $x \ne – \frac{d}{c}$).

$\Leftrightarrow ax + b = (cx + d)(mx + n)$ $\Leftrightarrow g(x) = {a_1}{x^2} + {b_1}x + {c_1} = 0$ $(1).$

Hai đồ thị cắt nhau tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $– \frac{d}{c}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{a_1} \ne 0;\Delta > 0}\\
{g\left( { – \frac{d}{c}} \right) > 0}
\end{array}} \right..
$$

Nhận xét:

+ Nếu $A$, $B$ là giao điểm của của hai đồ thị thì $A\left( {{x_1};m{x_1} + n} \right)$ và $B\left( {{x_2};m{x_2} + n} \right)$ với ${x_1}$, ${x_2}$ là hai nghiệm phân biệt của phương trình $(1).$

+ Nếu hai giao điểm $A$, $B$ thuộc hai nhánh của đồ thị thì ta có ${x_A} < – \frac{d}{c} < {x_B}.$

+ Nếu hai giao điểm $A$, $B$ cùng thuộc một nhánh của đồ thị hàm số thì ta có ${x_A}$, ${x_B} > – \frac{d}{c}$ hoặc ${x_A}$, ${x_B} < – \frac{d}{c}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## Ví dụ 1. Tìm điều kiện của tham số $m$ để đường thẳng $y = x + m$ cắt đồ thị hàm số $y = \frac{{x – 2}}{{x – 1}}$ tại hai điểm phân biệt $A$, $B$ sao cho:

a) Hai điểm $A$, $B$ thuộc về cùng một nhánh của đồ thị hàm số.

b) Độ dài đoạn thẳng $AB = 2\sqrt 3 .$

c) Diện tích tam giác $OAB$ bằng $4\sqrt 3$ với $O$ là gốc tọa độ.

Xét phương trình hoành độ giao điểm: $\frac{{x – 2}}{{x – 1}} = x + m$ (điều kiện $x \ne 1$).

$\Leftrightarrow x – 2 = (x + m)(x – 1)$ $\Leftrightarrow {x^2} + (m – 2)x + 2 – m = 0.$

$\Leftrightarrow {x^2} + (m – 2)x + 2 – m = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(m – 2)}^2} – 4(2 – m) > 0}\\
{{1^2} + m – 2 + 2 – m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {m^2} – 4 > 0}\\
{1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 2}\\
{m < – 2}
\end{array}} \right..
$$

Gọi ${x_1}$, ${x_2}$ là hai nghiệm phân biệt của phương trình $(1).$

Áp dụng định lí Vi-ét ta có: 
$$
\left\{\begin{array}{l}
{x_{1}+x_{2}=2-m} \\
{x_{1} x_{2}=2-m}
\end{array}\right.
$$

a) Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm thuộc cùng một nhánh của đồ thị hàm số $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1} > 1$, ${x_2} > 1$ hoặc ${x_1} < 1$, ${x_2} < 1$ $\Leftrightarrow \left( {{x_1} – 1} \right)\left( {{x_2} – 1} \right) > 0$ $\Leftrightarrow {x_1}{x_2} – \left( {{x_1} + {x_2}} \right) + 1 > 0.$

$\Leftrightarrow (2 – m) – (2 – m) + 1 > 0$ $\Leftrightarrow 1 > 0$ (luôn đúng).

Vậy với 
$$
\left[ {\begin{array}{l}
{m > 2}\\
{m < – 2}
\end{array}} \right.
$$
 thì đường thẳng $d$ luôn cắt đồ thị hàm số đã cho tại hai điểm thuộc cùng một nhánh của đồ thị hàm số.

b) Ta có $A\left( {{x_1};{x_1} + m} \right)$ và $B\left( {{x_2};{x_2} + m} \right)$ do đó $AB = \sqrt {{{\left( {{x_2} – {x_1}} \right)}^2} + {{\left( {{x_2} – {x_1}} \right)}^2}} .$

$\Leftrightarrow A{B^2} = 2{\left( {{x_2} – {x_1}} \right)^2}.$

$\Leftrightarrow A{B^2} = 2{\left( {{x_1} + {x_2}} \right)^2} – 8{x_2}{x_1}$ $= 2{(2 – m)^2} – 8(2 – m)$ $= 2{m^2} – 8.$

Theo giả thiết, ta có $AB = 2\sqrt 3$ $\Leftrightarrow A{B^2} = 12$ $\Leftrightarrow 12 = 2{m^2} – 8$ $\Leftrightarrow m = \pm 2\sqrt 5 .$

c) Ta có ${S_{OAB}} = \frac{1}{2}d(O;AB).AB$ với $AB:y = x + m$ $\Leftrightarrow x – y + m = 0.$

$\Rightarrow d(O;AB) = \frac{{|m|}}{{\sqrt 2 }}.$

Khi đó ta có $4\sqrt 3 = \frac{1}{2}.\frac{{|m|}}{{\sqrt 2 }}.\sqrt {2{m^2} – 8}$ $\Leftrightarrow 8\sqrt 3 = |m|.\sqrt {{m^2} – 4} .$

$\Leftrightarrow {m^4} – 4{m^2} – 192 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{m^2} = 16}\\
{{m^2} = – 12\:\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow m = \pm 4.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## Ví dụ 2. Cho hàm số $y = \frac{{x + 3}}{{x + 1}}$ $(C).$ Đường thẳng $d:y=2x+m$ cắt $(C)$ tại hai điểm phân biệt $A$, $B.$ Tìm điều kiện của tham số $m$ sao cho:

a) Trọng tâm của tam giác $OAB$ thuộc đường thẳng ${d_1}:y = – x + \frac{1}{3}$ với $O$ là gốc tọa độ.

b) Độ dài đoạn thẳng $AB$ nhỏ nhất.

Ta có phương trình hoành độ giao điểm:

$\frac{{x + 3}}{{x + 1}} = 2x + m$ (điều kiện $x \ne – 1$) $\Leftrightarrow x + 3 = (x + 1)(2x + m).$

$\Leftrightarrow 2{x^2} + (m + 1)x + m – 3 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị $(C)$ tại hai điểm phân biệt khi và chỉ khi phương trình $(1)$ có hai nghiệm phân biệt khác $-1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(m + 1)}^2} – 4.2.(m – 3) > 0}\\
{2{{( – 1)}^2} + (m + 1)( – 1) + m – 3 \ne 0}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {m^2} – 6m + 25 > 0}\\
{ – 2 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow {(m – 3)^2} + 16 > 0$ (luôn đúng).

Gọi ${x_1}$, ${x_2}$ là hai nghiệm phân biệt của phương trình $(1).$

Áp dụng định lí Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{{ – (m + 1)}}{2}}\\
{{x_1}{x_2} = \frac{{m – 3}}{2}}
\end{array}} \right..
$$

a) Giả sử $A\left( {{x_1};2{x_1} + m} \right)$ và $B\left( {{x_2};2{x_2} + m} \right)$ do đó trọng tâm $G$ của tam giác $OAB$ là $G\left( {\frac{{{x_1} + {x_2} + 0}}{3};\frac{{2\left( {{x_1} + {x_2}} \right) + 2m}}{3}} \right)$ $\Leftrightarrow G\left( {\frac{{ – (m + 1)}}{6};\frac{{m – 1}}{3}} \right).$

Theo bài ra ta có $G \in {d_1}:y = – x + \frac{1}{3}.$

$\Rightarrow \frac{{m – 1}}{3} = \frac{{m + 1}}{6} + \frac{1}{3}$ $\Leftrightarrow 2m – 2 = m + 1 + 2$ $\Leftrightarrow m = 5.$

b) Ta có $A{B^2} = {\left( {{x_2} – {x_1}} \right)^2} + {\left( {2{x_2} + m – 2{x_1} – m} \right)^2}.$

$= 5{\left( {{x_2} – {x_1}} \right)^2}$ $= 5{\left( {{x_2} + {x_1}} \right)^2} – 20{x_2}{x_1}$ $= 5.\frac{{{{(m + 1)}^2}}}{4} – 20.\frac{{m – 3}}{2}.$

$= \frac{5}{4}.\left[ {{m^2} – 6m + 25} \right]$ $= \frac{5}{4}\left[ {{{(m – 3)}^2} + 16} \right]$ $\ge \frac{5}{4}.16 = 20.$

Do đó $A{B_{\min }} = 2\sqrt 5$ khi $m = 3.$

<!-- chunk:4 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d:y=-x+m$ cắt đồ thị hàm số $y = \frac{{x + 2}}{{x – 1}}$ tại hai điểm phân biệt?

A. $( – \infty ;2 – 2\sqrt 3 ) \cup (2 + 2\sqrt 3 ; + \infty ).$

B. $(2 – 2\sqrt 3 ;2 + 2\sqrt 3 ).$

C. $( – \infty ;2 – 2\sqrt 3 ].$

D. $( – 2\sqrt 3 ;2\sqrt 3 ).$

Ta có phương trình hoành độ giao điểm: $\frac{{x + 2}}{{x – 1}} = – x + m$ (điều kiện $x \ne 1$).

$\Leftrightarrow x + 2 = – {x^2} + (m + 1)x – m$ $\Leftrightarrow {x^2} – mx + m + 2 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {m^2} – 4(m + 2) > 0}\\
{{1^2} – m.1 + m \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow {m^2} – 4m – 8 > 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 2 + 2\sqrt 3 }\\
{m < 2 – 2\sqrt 3 }
\end{array}} \right..
$$

> **Đáp án: A**

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d:y = – 2x + m$ cắt đồ thị hàm số $y = \frac{{2x – 1}}{{x – 2}}$ tại hai điểm phân biệt thuộc về cùng một nhánh của đồ thị.

A. 
$$
\left[ {\begin{array}{l}
{m > 6 + 2\sqrt 6 }\\
{m < 6 – 2\sqrt 6 }
\end{array}} \right..
$$

B. 
$$
\left[ {\begin{array}{l}
{m > 6 + 2\sqrt 3 }\\
{m < 6 – 2\sqrt 3 }
\end{array}} \right..
$$

C. 
$$
\left[ {\begin{array}{l}
{m > 6}\\
{m < 6}
\end{array}} \right..
$$

D. $– 6 < m < 6.$

Phương trình hoành độ giao điểm: $\frac{{2x – 1}}{{x – 2}} = – 2x + m$ (điều kiện $x \ne 2$).

$\Leftrightarrow 2x – 1 = – 2{x^2} + (m + 4)x – 2m.$

$\Leftrightarrow 2{x^2} – (m + 2)x + 2m – 1 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(m + 2)}^2} – 4.2(2m – 1) > 0}\\
{{{2.2}^2} – (m + 2)2 + 2m – 1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {m^2} – 12m + 12 > 0}\\
{3 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 6 + 2\sqrt 6 }\\
{m < 6 – 2\sqrt 6 }
\end{array}} \right..
$$

Áp dụng định lí Vi-et, ta có 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{{m + 2}}{2}}\\
{{x_1}{x_2} = \frac{{2m – 1}}{2}}
\end{array}} \right..
$$

Để hai giao điểm thuộc về cùng một nhánh của đồ thị:

$\Leftrightarrow \left( {{x_1} – 2} \right)\left( {{x_2} – 2} \right) > 0$ $\Leftrightarrow {x_1}{x_2} – 2\left( {{x_1} + {x_2}} \right) + 4 > 0$ $\Leftrightarrow \frac{{2m – 1}}{2} – 2.\frac{{m + 2}}{2} + 4 > 0.$

$\Leftrightarrow \frac{3}{2} > 0$ (luôn đúng).

> **Đáp án: A**

## Bài 3. Có bao nhiêu giá trị nguyên của tham số $m \in [ – 10;10]$ để đồ thị hàm số $y = \frac{{2x}}{{x – 1}}$ cắt $d: y=-x+ m$ tại hai điểm phân biệt.

A. $15.$

B. $16.$

C. $20.$

D. $21.$

Phương trình hoành độ giao điểm:

$\frac{{2x}}{{x – 1}} = – x + m$ $\Leftrightarrow 2x = – {x^2} + (m + 1)x – m$ $\Leftrightarrow {x^2} + (1 – m)x + m = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(1 – m)}^2} – 4m > 0}\\
{{1^2} + 1 – m + m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} – 6m + 1 > 0}\\
{2 \ne 0}
\end{array}} \right..
$$

Mà $m \in Z$, $m \in [ – 10;10]$ nên $m \in \{ – 10; – 9; \ldots ;0;6;7;8;9;10\} .$

> **Đáp án: B**

## Bài 4. Tính tổng các giá trị nguyên của tham số $m \in ( – 6;10)$ biết đường thẳng $d:y=-x+m$ cắt đồ thị hàm số $y = \frac{{x – 3}}{{x + 1}}$ tại hai điểm phân biệt.

A. $30.$

B. $40.$

C. $34.$

D. $21.$

Ta có phương trình hoành độ giao điểm:

$\frac{{x – 3}}{{x + 1}} = – x + m$ (điều kiện $x \ne – 1$) $\Leftrightarrow x – 3 = – {x^2} + (m – 1)x + m.$

$\Leftrightarrow {x^2} + (2 – m)x – m – 3 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $-1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(2 – m)}^2} – 4( – m – 3) > 0}\\
{{{( – 1)}^2} – 2 + m – m – 3 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + 16 > 0}\\
{ – 4 \ne 0}
\end{array}} \right.
$$
 (luôn đúng).

Theo bài ra ta có $m \in ( – 6;10)$ $\Rightarrow m \in \{ – 5; – 4; – 3; \ldots ;0;1; \ldots ;9\} .$

Do đó tổng các giá trị cần tìm của $m$ là $S = ( – 5) + ( – 4) + \ldots + 0 + 1 + \ldots + 9 = 30.$

> **Đáp án: A**

Bài 5. Tính tổng bình phương các giá trị của tham số $m$ sao cho đường thẳng $d:y=-x- m$ cắt đồ thị hàm số $y = \frac{{x – 2}}{{x – 1}}$ tại hai điểm phân biệt $M$, $N$ sao cho $MN = \sqrt {26} .$

A. $26.$

B. $25.$

C. $17.$

D. $10.$

Ta có phương trình hoành độ giao điểm là:

${\frac{{x – 2}}{{x – 1}} = – x – m}$ (điều kiện ${x \ne 1}$) $\Leftrightarrow x – 2 = – {x^2} + (1 – m)x + m.$

$\Leftrightarrow {x^2} + mx – m – 2 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {m^2} + 4(m + 2) > 0}\\
{1 + m – m – 2 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{(m + 2)}^2} + 4 > 0}\\
{ – 1 \ne 0}
\end{array}} \right.
$$
 (luôn đúng).

Áp dụng định lí Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = – m}\\
{{x_1}{x_2} = – m – 2}
\end{array}} \right..
$$

Khi đó gọi $M\left( {{x_1}; – {x_1} – m} \right)$, $N\left( {{x_2}; – {x_2} – m} \right)$ $\Rightarrow M{N^2} = {\left( {{x_2} – {x_1}} \right)^2} + {\left( { – {x_2} + {x_1}} \right)^2}.$

$= 2{\left( {{x_2} – {x_1}} \right)^2}$ $= 2\left[ {{{\left( {{x_2} + {x_1}} \right)}^2} – 4{x_2}{x_1}} \right]$ $= 2\left( {{m^2} + 4m + 8} \right).$

Theo bài ra ta có $2\left( {{m^2} + 4m + 8} \right) = 26$ $\Leftrightarrow {m^2} + 4m – 5 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 1}\\
{m = – 5}
\end{array}} \right..
$$

Do đó tổng cần tìm là $S = {1^2} + {( – 5)^2} = 26.$

> **Đáp án: A**

## Bài 6. Cho hàm số $y = \frac{{x + 1}}{{x – 1}}$ và đường thẳng $d$ đi qua điểm $M\left( {\frac{5}{2};4} \right)$ có hệ số góc $m.$ Tìm giá trị của $m$ để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $A$, $B$ sao cho $M$ là trung điểm $AB.$

A. $m=-3.$

B. $m=-2.$

C. $m = 2.$

D. $m=1.$

Phương trình đường thẳng $d:y = m\left( {x – \frac{5}{2}} \right) + 4.$

Ta có phương trình hoành độ giao điểm: $\frac{{x + 1}}{{x – 1}} = m\left( {x – \frac{5}{2}} \right) + 4.$

$\Leftrightarrow 2x + 2$ $= 2m{x^2} – (7m – 8)x + 5m – 8$ $\Leftrightarrow 2m{x^2} – (7m – 6)x + 5m – 10 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\Delta = {{(7m – 6)}^2} – 4.2m.(5m – 10) > 0}\\
{2m – (7m – 6) + 5m – 10 \ne 0}
\end{array}} \right..
$$

Áp dụng định lí Vi-et, ta có: ${x_1} + {x_2} = \frac{{7m – 6}}{{2m}}.$

Khi đó $A\left( {{x_1};{y_1}} \right)$, $B\left( {{x_2};{y_2}} \right).$

Vì $M$ là trung điểm $AB$ nên:

${x_1} + {x_2} = 2{x_M} = 5$ $\Leftrightarrow \frac{{7m – 6}}{{2m}} = 5$ $\Leftrightarrow m = – 2$ (thỏa mãn).

> **Đáp án: B**

## Bài 7. Cho hàm số $y = \frac{{2x + 1}}{{x + 1}}.$ Tìm $m$ để đường thẳng $d: y=-2x+ m$ cắt đồ thị hàm số đã cho tại hai điểm $M$, $N$ sao cho ${S_{OMN}} = \frac{{3\sqrt {17} }}{4}$ với $O$ là gốc tọa độ.

A. ${ \pm 1}$.

B. ${ \pm \frac{1}{2}}$.

C. ${ \pm 3}$.

D. ${ \pm 2}$.

Phương trình hoành độ giao điểm:

$\frac{{2x + 1}}{{x + 1}} = – 2x + m$ (điều kiện $x \ne – 1$) $\Leftrightarrow 2x + 3$ $= – 2{x^2} + (m – 2)x + m.$

$\Leftrightarrow 2{x^2} – (m – 4)x + 1 – m = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $-1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(m – 4)}^2} – 4.2.(1 – m) > 0}\\
{2.{{( – 1)}^2} – (m – 4)( – 1) + 1 – m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + 8 > 0}\\
{ – 1 \ne 0}
\end{array}} \right.
$$
 (luôn đúng).

Áp dụng định lí Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{{m – 4}}{2}}\\
{{x_1}{x_2} = \frac{{1 – m}}{2}}
\end{array}} \right..
$$

Gọi $M\left( {{x_1}; – 2{x_1} + m} \right)$, $N\left( {{x_2}; – 2{x_2} + m} \right).$

Khi đó $M{N^2} = {\left( {{x_2} – {x_1}} \right)^2} + {\left( { – 2{x_2} + 2{x_1}} \right)^2}$ $= 5{\left( {{x_2} – {x_1}} \right)^2}$ $= 5{\left( {{x_2} + {x_1}} \right)^2} – 20{x_1}{x_2}.$

$= 5{\left( {\frac{{m – 4}}{2}} \right)^2} – 20.\frac{{1 – m}}{2}$ $= \frac{5}{4}\left[ {{m^2} + 8} \right].$

Ta có $d(O;MN)$ $= d(O;d)$ $= \frac{{|m|}}{{\sqrt 5 }}$ $\Rightarrow {S_{OMN}} = \frac{1}{2}.\frac{{|m|}}{{\sqrt 5 }}.\frac{{\sqrt 5 }}{2}.\sqrt {{m^2} + 8} .$

$\Leftrightarrow 4.\frac{{3\sqrt {17} }}{4} = |m|.\sqrt {{m^2} + 8}$ $\Leftrightarrow {m^4} + 8{m^2} – 153 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{m^2} = 9}\\
{{m^2} = – 17\:\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow m = \pm 3.$

> **Đáp án: C**

## Bài 8. Cho hàm số $y = \frac{{2x + 1}}{{x – 1}}$ có đồ thị $(C)$ và đường thẳng $d: y = mx + 2 – m.$ Tìm giá trị của tham số $m$ để đường thẳng $d$ cắt $(C)$ tại hai điểm phân biệt $A$ và $B$ sao cho tam giác $ABC$ cân tại $C(2;-1).$

A. $m = \frac{4}{3}.$

B. $m = – \frac{5}{3}.$

C. $m = – \frac{2}{3}.$

D. $m = \frac{1}{3}.$

Phương trình hoành độ giao điểm của đồ thị là:

$\frac{{2x + 1}}{{x – 1}} = mx + 2 – m$ (điều kiện $x \ne 1$) $\Leftrightarrow m{x^2} – 2mx + m – 3 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\Delta ‘ = {m^2} – m(m – 3) > 0}\\
{m – 2m + m – 3 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > 0.$

Áp dụng định lí Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = 2}\\
{{x_1}{x_2} = \frac{{m – 3}}{m}}
\end{array}} \right..
$$

Gọi $I$ là trung điểm $AB$ thì ${x_I} = \frac{{{x_1} + {x_2}}}{2} = 1$ mà $I \in AB$ $\Rightarrow I \in d$ $\Rightarrow I(1;2).$

Ta có đường thẳng $IC$ có hệ số góc là ${k_{IC}} = \frac{{{y_C} – {y_I}}}{{{x_C} – {x_I}}} = – 3.$

Theo giả thiết $\Delta ABC$ cân tại $C$ nên $IC \bot AB.$

$\Leftrightarrow {k_{IC}}.{k_d} = – 1$ $\Leftrightarrow m.( – 3) = – 1$ $\Leftrightarrow m = \frac{1}{3}.$

> **Đáp án: D**

## Bài 9. Cho hàm số $y = \frac{{2x – 4}}{{x + 1}}.$ Tìm tất cả các giá trị của tham số $m$ sao cho đường thẳng $y=-x+ m$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $B$, $C$ sao cho tứ giác $OABC$ là hình bình hành với $A(-5;5)$ và $O$ là gốc tọa độ.

A. $m=2.$

B. 
$$
\left[ {\begin{array}{l}
{m = 0}\\
{m = 2}
\end{array}} \right..
$$

C. 
$$
\left[ {\begin{array}{l}
{m = 1}\\
{m = 3}
\end{array}} \right..
$$

D. $m=-2.$

Ta có phương trình hoành độ giao điểm:

$\frac{{2x – 4}}{{x + 1}} = – x + m$ (điều kiện $x \ne – 1$) $\Leftrightarrow {x^2} + (3 – m)x – 4 – m = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ khác $-1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(3 – m)}^2} – 4( – 4 – m) > 0}\\
{{{( – 1)}^2} + (3 – m)( – 1) – 4 – m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} – 2m + 25 > 0}\\
{ – 6 \ne 0}
\end{array}} \right.
$$
 (luôn đúng).

Áp dụng định lí Vi-ét, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = m – 3}\\
{{x_1}{x_2} = – 4 – m}
\end{array}} \right..
$$

Giả sử $B\left( {{x_1}; – {x_1} + m} \right)$, $C\left( {{x_2}; – {x_2} + m} \right)$ thì:

$B{C^2} = 2{\left( {{x_2} – {x_1}} \right)^2}$ $= 2{\left( {{x_2} + {x_1}} \right)^2} – 8{x_1}{x_2}$ $= 2{m^2} – 4m + 50.$

Ta có đường thẳng $OA:y = – x$ và $OA = \sqrt {50}$ mà $CB:y = – x + m.$

Do đó theo yêu cầu bài toán ta có $OA // CB$ và $OA = CB.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{2{m^2} – 4m + 50 = 50}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m \ne 0\\
\left[ {\begin{array}{l}
{m = 0}\\
{m = 2}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow m = 2.$

> **Đáp án: A**

## Bài 10. Cho hàm số $y = \frac{x}{{1 – x}}$ có đồ thị $(C)$ và điểm thỏa mãn $A(-1;1).$ Tìm $m$ để đường thẳng $d: y = mx – m–1$ cắt $(C)$ tại hai điểm phân biệt $M$, $N$ sao cho $A{M^2} + A{N^2}$ đạt giá trị nhỏ nhất.

A. $m=-2.$

B. $m=-1.$

C. $m=1.$

D. $m= -3.$

Phương trình hoành độ giao điểm là:

${\frac{x}{{1 – x}} = mx – m – 1}$ (điều kiện ${x \ne 1}$) $\Leftrightarrow m{x^2} – 2mx + m + 1 = 0$ $(1).$

Để đường thẳng $d$ cắt đồ thị hàm số đã cho tại hai điểm phân biệt $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $1$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\Delta = {m^2} – m(m + 1) > 0}\\
{m – 2m + m + 1 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m < 0.$

Giả sử ${x_M}$, ${x_N}$ là nghiệm của $(1)$, theo định lý Vi-et, ta có: 
$$
\left\{ {\begin{array}{l}
{{x_M} + {x_N} = 2}\\
{{x_M}{x_N} = \frac{{m + 1}}{m}}
\end{array}} \right..
$$

Gọi $I$ là trung điểm của $MN$ suy ra 
$$
\left\{ {\begin{array}{l}
{{x_I} = \frac{{{x_M} + {x_N}}}{2} = 1}\\
{{y_I} = m{x_I} – m – 1 = – 1}
\end{array}} \right..
$$

Ta có $A{M^2} + A{N^2} = 2A{I^2} + \frac{{M{N^2}}}{2}$ nên $A{M^2} + A{N^2}$ nhỏ nhất khi $M{N^2}$ nhỏ nhất.

$M{N^2}$ $= {\left( {{x_M} – {x_N}} \right)^2}$ $+ {\left( {\left( {m{x_M} – m – 1} \right) – \left( {m{x_N} – m – 1} \right)} \right)^2}$ $= \left( {{m^2} + 1} \right){\left( {{x_M} – {x_N}} \right)^2}.$

$= \left( {{m^2} + 1} \right)\left( {{{\left( {{x_M} + {x_N}} \right)}^2} – 4{x_M}{x_N}} \right)$ $= \left( {{m^2} + 1} \right)\left( {4 – 4\frac{{m + 1}}{m}} \right)$ $= 4\left( { – m + \frac{1}{{ – m}}} \right) \ge 8.$

Dấu bằng xảy ra khi $– m = \frac{1}{{ – m}}$ và $m <0$ suy ra $m=-1.$

> **Đáp án: B**

<!-- chunk:5 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d:y = x + m$ cắt đồ thị hàm số $y = \frac{{2x – 3}}{{x – 1}}$ tại hai điểm phân biệt.

A. $( – \infty ; – 1) \cup (3; + \infty ).$

B. $(4; + \infty ).$

C. (-1 ;+\infty)

D. $\forall m.$

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d:y = 2x + m$ cắt đồ thị hàm số $y = \frac{{x – 1}}{{x – 2}}$ tại hai điểm phân biệt.

A. $( – \infty ;1) \cup (3; + \infty ).$

B. $\forall m.$

C. $(1;3).$

D. $[0; + \infty ).$

## Bài 3. Có bao nhiêu giá trị nguyên của tham số $m \in [ – 12;12]$ để đường thẳng $d:y = 2mx + 1$ cắt đồ thị hàm số $y = \frac{{x – 3}}{{x – 1}}$ tại hai điểm phân biệt thuộc về cùng một nhánh của đồ thị hàm số.

A. $22.$

B. $8.$

C. $7.$

D. $25.$

## Bài 4. Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d:y = mx + 2$ cắt đồ thị hàm số $y = \frac{{2x – 1}}{{x – 2}}$ tại hai điểm phân biệt $M$, $N$ sao cho $I(1;3)$ là trung điểm $MN.$

A. $m=-4.$

B. $m=1.$

C. $m=2.$

D. $m=-1.$

## Bài 5. Tính tổng bình phương các giá trị của tham số $m$ để đường thẳng $d:y = 2x – m$ cắt đồ thị hàm số $y = \frac{{3x – 1}}{{x + 2}}$ tại hai điểm phân biệt $A$, $B$ sao cho $AB = \sqrt {10} .$

A. $226.$

B. $25.$

C. $149.$

D. $65.$

## Bài 6. Tính tổng tất cả các giá trị thực của $m$ để đường thẳng $y = x + m – 1$ cắt đồ thị hàm số $y = \frac{{2x + 1}}{{x + 1}}$ tại hai điểm phân biệt $A$, $B$ sao cho $AB = 2\sqrt 3 .$

A. $8.$

B. $6.$

C. $4.$

D. $10.$

## Bài 7. Cho hàm số $y = \frac{{x + 3}}{{x + 1}}$ có đồ thị $(C).$ Tìm tất cả các giá trị của tham số $m$ sao cho đường thẳng $d: y=x-m$ cắt $(C)$ tại hai điểm phân biệt $A$ và $B$ thỏa mãn điểm $G(2;-2)$ là trọng tâm của tam giác $OAB.$

A. $m = 4.$

B. $m=-3.$

C. $m=6.$

D. $m=7.$

## Bài 8. Cho hàm số $y = \frac{{x + 3}}{{x + 1}}$ $(C).$ Tìm tất cả các giá trị của tham số $m$ để đường thẳng $d: y = 2x + m$ cắt $(C)$ tại hai điểm phân biệt $M$, $N$ sao cho $MN$ đạt giá trị nhỏ nhất.

A. $m= -2.$

B. $m= 3.$

C. $m=4.$

D. $m=-1.$

## Bài 9. Cho hàm số $y = \frac{{x + 3}}{{x + 2}}$ có đồ thị $(C).$ Biết có hai giá trị tham số $m$ để đường thẳng $d: y=2x+ m$ cắt đồ thị $(C)$ tại hai điểm phân biệt $A$, $B$ và cắt tiệm cận đứng của $(C)$ tại điểm $M$ sao cho $M{A^2} + M{B^2} = 25$ là ${m_1}$, ${m_2}.$ Tính tổng $S = m_1^2 + m_2^2.$

A. $S =61.$

B. $S = 146.$

C. $S=37.$

D. $S = 269.$

## Bài 10. Có bao nhiêu số nguyên $m$ sao cho đường thẳng $y=x+m$ cắt đồ thị hàm số $y = \frac{{2x – 1}}{{x + 1}}$ tại hai điểm phân biệt $M$, $N$ và $MN \le 6$?

A. $10.$

B. $11.$

C. $4.$

D. $3.$

<!-- chunk:6 level:1 source:https://toanmath.com/2019/11/bai-toan-tuong-giao-ham-phan-thuc-huu-ti-chua-tham-so.html -->
## **V. ĐÁP ÁN BÀI TẬP TỰ LUYỆN

**1. A.

2. B.

3. C.

4. B.

5. A.

6. A.

7. C.

8. B.

9. B.

10. C.