# Bài toán đường tiệm cận của đồ thị hàm số chứa tham số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán đường tiệm cận của đồ thị hàm số chứa tham số trong chương trình Giải tích 12.

## I. PHƯƠNG PHÁP GIẢI TOÁN

Đối với bài toán chứa tham số, để biện luận số tiệm cận hay tìm điều kiện để đồ thị hàm số có tiệm cận thỏa mãn điều kiện nào đó, ta thường thực hiện theo các bước sau:

+ Bước 1: Tìm điều kiện của tham số để hàm số không suy biến.

+ Bước 2: Tìm các đường tiệm cận của đồ thị hàm số.

+ Bước 3: Giải điều kiện của bài toán để tìm tham số.

+ Bước 4: Kết luận.

<!-- chunk:1 level:3 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## Ví dụ 1. Tìm điều kiện của tham số $m$ để đồ thị của hàm số $y = \frac{{(2m + 1)x + 3}}{{x + 1}}$ có đường tiệm cận đi qua điểm $A( – 2;7).$

Nếu $m = 1$, khi đó ta có hàm số $y = \frac{{3x + 3}}{{x + 1}} = 3$ không có tiệm cận qua điểm $A( – 2;7).$

Với $m \ne 1$ thì đồ thị của hàm số có tiệm cận đứng là $x = -1$ và tiệm cận ngang là $y = 2m + 1.$

Đường tiệm cận ngang đi qua điểm $A(-2;7)$ khi và chỉ khi $7 = 2m + 1$ $\Leftrightarrow m = 3.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## Ví dụ 2. Tìm hai số $a$, $b$ để đồ thị hàm số $y = \frac{{(4a – b){x^2} + ax + 1}}{{{x^2} + ax + b – 12}}$ nhận trục hoành và trục tung làm hai tiệm cận.

Do đồ thị nhận trục hoành làm tiệm cận ngang nên:

$\mathop {\lim }\limits_{x \to \pm \infty } \frac{{(4a – b){x^2} + ax + 1}}{{{x^2} + ax + b – 12}} = 0$ $\Leftrightarrow 4a – b = 0.$

Do đồ thị nhận trục tung làm tiệm cận đứng, suy ra biểu thức ${x^2} + ax + b – 12$ nhận $x = 0$ làm nghiệm $\Leftrightarrow b = 12.$ Suy ra $a = 3.$

Thử lại: Ta có $a = 3$ và $b = 12$ là hai số cần tìm.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## Ví dụ 3. Tìm tất cả các giá trị thực của $m$ để đồ thị hàm số $y = \frac{{x + 1}}{{\sqrt {m{x^2} + 1} }}$ có hai tiệm cận ngang.

Nếu $m = 0$ đồ thị hàm số $y = x + 1$ không có tiệm cận ngang.

Nếu $m < 0$ hàm số có tập xác định là khoảng $\left( { – \frac{1}{{\sqrt { – m} }};\frac{1}{{\sqrt { – m} }}} \right)$ nên đồ thị không có tiệm cận ngang.

Nếu $m > 0$ hàm số có tập xác định là $R.$

$\mathop {\lim }\limits_{x \to + \infty } y = \mathop {\lim }\limits_{x \to + \infty } \frac{{x + 1}}{{\sqrt {m{x^2} + 1} }}$ $= \mathop {\lim }\limits_{x \to + \infty } \frac{{x + 1}}{{x\sqrt m \sqrt {1 + \frac{1}{{mx}}} }} = \frac{1}{{\sqrt m }}$ $\Rightarrow y = \frac{1}{{\sqrt m }}$ là một tiệm cận ngang của đồ thị hàm số.

$\mathop {\lim }\limits_{x \to – \infty } y = \mathop {\lim }\limits_{x \to – \infty } \frac{{x + 1}}{{\sqrt {m{x^2} + 1} }}$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{x + 1}}{{ – x\sqrt m \sqrt {1 + \frac{1}{{mx}}} }} = – \frac{1}{{\sqrt m }}$ $\Rightarrow y = – \frac{1}{{\sqrt m }}$ là một tiệm cận ngang của đồ thị hàm số.

Vậy đồ thị có hai tiệm cận ngang khi $m > 0.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## Ví dụ 4. Với giá trị nào của tham số $m$ thì đồ thị hàm số $y = \frac{{2mx – 3}}{{x + m}}$ có tiệm cận ngang là đường thẳng $y = 2$?

Dễ thấy tiệm cận ngang là đường thẳng $y = 2m.$ Do đó $m = 1$ thì đồ thị hàm số $y = \frac{{2mx – 3}}{{x + m}}$ có tiệm cận ngang là đường thẳng $y = 2.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## Ví dụ 5. Tìm tất cả các giá trị của tham số $m$ để hàm số $y = \frac{{x – 3}}{{mx – 1}}$ không có tiệm cận đứng.

Điều kiện để hàm số không có tiệm cận đứng là $m = 0$ hoặc $mx – 1$ có nghiệm là $3$ $\Leftrightarrow m = \frac{1}{3}.$

Vậy $m = 0$, $m = \frac{1}{3}$ là các giá trị cần tìm.

<!-- chunk:6 level:1 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Cho hàm số $y = \frac{{mx + 3}}{{4x – 2n + 5}}.$ Đồ thị hàm số có đường tiệm cận ngang là $y = 2$ và nhận trục tung là tiệm cận đứng. Khi đó tổng $m + n$ bằng?

A. $\frac{9}{2}$.

B. $\frac{{21}}{2}$.

C. $\frac{{11}}{2}$.

D. $\frac{{13}}{2}$.

Tiệm cận ngang: $y = 2$ $\Leftrightarrow \frac{m}{4} = 2$ $\Leftrightarrow m = 8.$

Tiệm cận đứng: $x = \frac{{2n – 5}}{4} = 0$ $\Leftrightarrow n = \frac{5}{2}.$

$\Rightarrow m + n = \frac{{21}}{2}.$

> **Đáp án: B**

## Bài 2. Với giá trị $m$ nào thì tiệm cận đứng của đồ thị hàm số $y = \frac{{3x – 1}}{{2x – m}}$ đi qua điểm $M(1;3).$

A. $m = 1.$

B. $m = 2.$

C. $m = 3.$

D. $m = -2.$

Phương trình tiệm cận đứng là: $d:x = \frac{m}{2}.$

$d$ đi qua $M(1;3)$ khi $1 = \frac{m}{2}$ $\Leftrightarrow m = 2.$

> **Đáp án: B**

## Bài 3. Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = \frac{{{m^2}x – 4}}{{mx – 1}}$ có tiệm cận đứng đi qua điểm $A(1;4).$

A. $m = 4.$

B. $m = 1.$

C. $m = 2.$

D. $m = 3.$

Tiệm cận đứng của đồ thị hàm số: $x = \frac{1}{m}.$

Tiệm cận đứng của đồ thị hàm số đi qua điểm $A(1;4)$ $\Rightarrow \frac{1}{m} = 1$ $\Leftrightarrow m = 1.$

Thử lại thỏa mãn.

> **Đáp án: B**

## Bài 4. Biết rằng đồ thị của hàm số $y = \frac{{(n – 3)x + n – 2017}}{{x + m + 3}}$ nhận trục hoành làm tiệm cận ngang và trục tung làm tiệm cận đứng. Khi đó giá trị của $m + n$ là?

A. $0.$

B. $-3.$

C. $6.$

D. $3.$

Tiệm cận ngang: $y = n – 3$ $\Rightarrow n – 3 = 0$ $\Leftrightarrow n = 3.$

Tiệm cận đứng: $x = – m – 3$ $\Rightarrow – m – 3 = 0$ $\Leftrightarrow m = – 3.$

Vậy $m + n = 3 – 3 = 0.$

> **Đáp án: A**

## Bài 5. Biết đồ thị hàm số $y = \frac{{(m – 2n){x^2} + mx + 1}}{{{x^2} – mx + m – n}}$ nhận đường thẳng $x = 1$ làm một tiệm cận đứng và trục hoành làm tiệm cận ngang thì $m + n$ bằng:

A. $3.$

B. $2.$

C. $4.$

D. $1.$

$y = \frac{{(m – 2n){x^2} + mx + 1}}{{{x^2} – mx + m – n}}.$

+ Để $y = 0$ là tiệm cận ngang của đồ thị hàm số:

$\Leftrightarrow \mathop {\lim }\limits_{x \to \pm \infty } y = 0$ $\Leftrightarrow m – 2n = 0$ $(1).$

+ Để $x = 1$ là tiệm cận đứng của đồ thị hàm số $\Leftrightarrow \mathop {\lim }\limits_{x \to 1} y = \infty .$

Trường hợp: ${x^2} – mx + m – n = 0$ có nghiệm kép $x = 1.$

$\Leftrightarrow \Delta = {m^2} – 4m + 4n = 0$ $(2).$

Từ $(1)$ và $(2)$ suy ra: 
$$
\left[ {\begin{array}{l}
{m = 0 \to n = 0\:\:{\rm{(loại)}}}\\
{m = 2 \to n = 1\:\:(nhận)}
\end{array}} \right..
$$

Vậy $m + n = 3.$

Vì có một đáp án nên ta không cần giải trường hợp khác.

> **Đáp án: A**

## Bài 6. Các giá trị của tham số $a$ để đồ thị hàm số $y = ax + \sqrt {4{x^2} + 1}$ có tiệm cận ngang là:

A. $a = \pm 2.$

B. $a = – 2$ và $a = \frac{1}{2}.$

C. $a = \pm 1.$

D. $a = \pm \frac{1}{2}.$

Trường hợp 1: $a > 0$: Ta có:

$\mathop {\lim }\limits_{x \to + \infty } (ax + \sqrt {4{x^2} + 1} ) = + \infty .$

$\mathop {\lim }\limits_{x \to – \infty } (ax + \sqrt {4{x^2} + 1} )$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{\left( {{a^2} – 4} \right){x^2} – 1}}{{ax – \sqrt {4{x^2} + 1} }}$ $= \mathop {\lim }\limits_{x \to – \infty } \frac{{\left( {{a^2} – 4} \right)x – \frac{1}{x}}}{{a + \sqrt {4 + \frac{1}{{{x^2}}}} }}.$

Vậy để $\mathop {\lim }\limits_{x \to – \infty } (ax + \sqrt {4{x^2} + 1} )$ là hữu hạn khi 
$$
\left\{ {\begin{array}{l}
{{a^2} – 4 = 0}\\
{a \ne – 2}
\end{array}} \right.
$$
 $\Rightarrow a = 2.$

Trường hợp 2: $a < 0$: Trình bày tương tự ta được $a = -2.$

Trường hợp 3: $a = 0$: $\mathop {\lim }\limits_{x \to \pm \infty } \sqrt {4{x^2} + 1} = + \infty$ nên loại $a = 0.$

Vậy các giá trị thỏa mãn là: $a = \pm 2.$

> **Đáp án: A**

## Bài 7. Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = \frac{{{x^2} + m}}{{{x^2} – 3x + 2}}$ có đúng hai đường tiệm cận.

A. $m = – 1.$

B. $m \in [1;4].$

C. $m \in \{ – 1; – 4\} .$

D. $m = 4.$

Ta luôn có một đường tiệm cận ngang $y = 1.$

Đồ thị hàm số có đúng hai đường tiệm cận $\Leftrightarrow {x^2} + m = 0$ có nghiệm $x = 1$ hoặc $x = 2$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – 1}\\
{m = – 4}
\end{array}} \right..
$$

> **Đáp án: C**

## Bài 8. Tìm tập hợp các giá trị của $m$ để đồ thị hàm số $y = \frac{{1 + \sqrt {x + 1} }}{{\sqrt {{x^2} – mx – 3m} }}$ có đúng hai tiệm cận đứng.

A. $( – \infty ; – 12) \cup (0; + \infty ).$

B. $(0; + \infty ).$

C. $\left[ {\frac{1}{4};\frac{1}{2}} \right].$

D. $\left( {0;\frac{1}{2}} \right].$

Đồ thị hàm số có hai tiệm cận đứng 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 1}\\
{{x^2} – mx – 3m = 0}
\end{array}} \right.
$$
 có hai nghiệm phân biệt.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 1}\\
{{x^2} = m(x + 3)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge – 1}\\
{m = \frac{{{x^2}}}{{x + 3}}}
\end{array}} \right.
$$
 $\Rightarrow f(x) = \frac{{{x^2}}}{{x + 3}} = m$ có hai nghiệm phân biệt $x \ge – 1$ $(*).$

Xét hàm số $f(x) = \frac{{{x^2}}}{{x + 3}}$ trên $[ – 1; + \infty )$.

Ta có:

$f'(x) = \frac{{x(x + 6)}}{{{{(x + 3)}^2}}}.$

$f'(x) = 0\mathop \Leftrightarrow \limits^{x \ge – 1} x = 0.$

Ta có bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so-1.png" alt="">

Khi đó, yêu cầu $(*) \Leftrightarrow m \in \left( {0;\frac{1}{2}} \right].$

Vậy $m \in \left( {0;\frac{1}{2}} \right]$ là giá trị cần tìm.

> **Đáp án: D**

## Bài 9. Cho hàm số: $y = \frac{{x – 1}}{{m{x^2} – 2x + 3}}.$ Tìm tất cả các giá trị của $m$ để đồ thị hàm số có ba đường tiệm cận.

A. 
$$
\left\{ {\begin{array}{l}
{m \ne 0}\\
{m \ne – 1}\\
{m < \frac{1}{3}}
\end{array}} \right..
$$

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
{m \ne 0}\\
{m \ne – 1}\\
{m < \frac{1}{5}}
\end{array}} \right..
$$

D. 
$$
\left\{ {\begin{array}{l}
{m \ne 0}\\
{m < \frac{1}{3}}
\end{array}} \right..
$$

Nhận thấy đồ thị hàm số $y = \frac{{x – 1}}{{m{x^2} – 2x + 3}}$ có ba đường tiện cận khi hàm số đã cho có dạng bậc nhất trên bậc hai hay $m \ne 0$ (khi $m = 0$ thì hàm số $y = \frac{{x – 1}}{{ – 2x + 3}}$ có một tiệm cận đứng và một tiệm cận ngang).

Điều kiện để đồ thị hàm số $y = \frac{{x – 1}}{{m{x^2} – 2x + 3}}$ có ba tiệm cận là $m{x^2} – 2x + 3$ có hai nghiệm phân biệt khác $1.$ Điều kiện để phương trình $m{x^2} – 2x + 3 = 0$ có hai nghiệm phân biệt và khác $1$ là $\Delta = {b^2} – 4ac$ $= 4 – 12m > 0$ và $m + 1 \ne 0$ hay $m < \frac{1}{3}$ và $m \ne – 1.$

Vậy 
$$
\left\{ {\begin{array}{l}
{m \ne – 1}\\
{m \ne 0}\\
{m < \frac{1}{3}}
\end{array}} \right.
$$
 thỏa mãn yêu cầu bài toán.

> **Đáp án: A**

## Bài 10. Hỏi có bao nhiêu giá trị nguyên của $m$ để đồ thị hàm số $y = \frac{{{x^2} – 3x + 2}}{{{x^2} – mx – m + 5}}$ không có đường tiệm cận đứng?

A. $9.$

B. $8.$

C. $11.$

D. $10.$

Điều kiện xác định: ${x^2} – mx – m + 5 \ne 0.$

Hàm số không có đường tiệm cận đứng khi không tồn tại điểm ${x_0} \notin D$ của hàm số ($D$ là tập xác định của hàm số) sao cho $\mathop {\lim }\limits_{x \to {x_0}^ \pm } f(x) = \pm \infty .$

Vậy điều kiện để hàm số không có đường tiệm cận đứng gồm:

+ Phương trình ${x^2} – mx – m + 5 = 0$ vô nghiệm.

$\Leftrightarrow \Delta < 0$ $\Leftrightarrow {m^2} + 4m – 20 < 0$ $\Leftrightarrow – 2 – 2\sqrt 6 < m < – 2 + 2\sqrt 6 .$

+ Hàm số là hằng số: Khi $m = 3$ thì $y = 1$ (thỏa mãn).

Vậy có $10$ giá trị nguyên của $m.$

> **Đáp án: D**

<!-- chunk:7 level:1 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Tìm tất cả các giá trị của tham số $a$ để đồ thị hàm số $y = \frac{{{x^2} + a}}{{{x^3} + a{x^2}}}$ có ba đường tiệm cận.

A. 
$$
\left\{ {\begin{array}{l}
{a \ne 0}\\
{a \ne \pm 1}
\end{array}} \right..
$$

B. 
$$
\left\{ {\begin{array}{l}
{a \ne 0}\\
{a \ne – 1}
\end{array}} \right..
$$

C. 
$$
\left\{ {\begin{array}{l}
{a \ne 0}\\
{a \ne 1}
\end{array}} \right..
$$

D. $a > 0.$

## Bài 2. Số các giá trị của $m$ để đồ thị hàm số $y = \frac{{x + m}}{{mx + 1}}$ không có tiệm cận đứng là:

A. $1.$

B. $2.$

C. $3.$

D. $0.$

## Bài 3. Tìm $m$ để đồ thị hàm số $y = \frac{{{x^2} + 1}}{{{x^2} – m}}$ có hai đường tiệm cận đứng.

A. $m \ge 0$.

B. $m > 0$.

C. $m < 0$.

D. $m \ne 0$.

## Bài 4. Cho hàm số $y = \frac{{2{x^2} – 3x + m}}{{x – m}}.$ Để đồ thị hàm số không có tiệm cận đứng thì:

A. $m = 0.$

B. $m = 0$, $m = 1.$

C. $m = 1.$

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## D. Không tồn tại $m.$

## Bài 5. Tìm $m$ để đồ thị hàm số $y = \frac{{{x^2} – 6x + m}}{{4x – m}}$ không có tiệm cận đứng?

A. $m = 2.$

B. 
$$
\left[ {\begin{array}{l}
{m = 0}\\
{m = 8}
\end{array}} \right..
$$

C. $m = 16.$

D. $m = 1.$

## Bài 6. Cho hàm số $y = \frac{{ax + 1}}{{bx – 2}}.$ Tìm $a$, $b$ để đồ thị hàm số có $x = 1$ là tiệm cận đứng và $y = \frac{1}{2}$ là tiệm cận ngang.

A. $a = -1$, $b= -2.$

B. $a = 1$, $b = 2.$

C. $a = -1$, $b = 2.$

D. $a = 4$, $b = 4.$

## Bài 7. Cho hàm số $y = \sqrt {m{x^2} + 2x} – x.$ Tìm các giá trị của $m$ để đồ thị hàm số có đường tiệm cận ngang.

A. $m = 1.$

B. $m \in \{ – 2;2\} .$

C. $m \in \{ – 1;1\} .$

D. $m > 0.$

## Bài 8. Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = \frac{{x – 3}}{{\sqrt {{x^2} + m} }}$ có ba tiệm cận.

A. 
$$
\left\{ {\begin{array}{l}
{m < 0}\\
{m \ne – 9}
\end{array}} \right..
$$

B. $m = 0.$

C. $m > 0.$

D. 
$$
\left[ {\begin{array}{l}
{m = 0}\\
{m = 9}
\end{array}} \right..
$$

## Bài 9. Tìm tất cả các giá trị thực của tham số $m$ để đồ thị hàm số $y = \frac{{x + 1}}{{\sqrt {m{{(x – 1)}^2} + 4} }}$ có hai tiệm cận đứng.

A. $m < 0.$

B. $m = 0.$

C. 
$$
\left\{ {\begin{array}{l}
{m < 0}\\
{m \ne – 1}
\end{array}} \right..
$$

D. $m < 1.$

## Bài 10. Cho hàm số $y = \frac{{12 + \sqrt {4x – {x^2}} }}{{\sqrt {{x^2} – 6x + 2m} }}$ có đồ thị là $\left( {{C_m}} \right).$ Tìm tất cả các giá trị thực của tham số $m$ để $\left( {{C_m}} \right)$ có đúng hai đường tiệm cận đứng.

A. $S = \left[ {4;\frac{9}{2}} \right).$

B. $S = [8;9).$

C. $S = \left( {4;\frac{9}{2}} \right).$

D. $S = (0;9].$

<!-- chunk:9 level:1 source:https://toanmath.com/2019/11/bai-toan-duong-tiem-can-cua-do-thi-ham-so-chua-tham-so.html -->
## V. ĐÁP ÁN BÀI TẬP TỰ LUYỆN
1. $B.$

2. $C.$

3. $B.$

4. $B.$

5. $B.$

6. $B.$

7. $A.$

8. $A.$

9. $C.$

10. $A.$