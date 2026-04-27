# Tìm cực trị của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/tim-cuc-tri-cua-ham-so.html -->
Bài viết hướng dẫn tìm cực trị của hàm số thông qua các bước giải cụ thể và các ví dụ minh họa có lời giải chi tiết, các ví dụ được chọn lọc với nhiều dạng bài khác nhau như: cực trị hàm đa thức, cực trị hàm chứa căn, cực trị hàm chứ dấu giá trị tuyệt đối, cực trị hàm lượng giác …

Phương pháp
Để tìm cực trị của hàm số $y = f(x)$, ta thực hiện theo các bước sau đây:

+ Tìm tập xác định $D$ của hàm số $f$.

+ Tính $f’(x)$.

+ Tìm nghiệm của phương trình $f’(x) = 0$ (nếu có) và tìm các điểm ${x_0} \in D$ mà tại đó hàm $f$ liên tục nhưng $f'({x_0})$ không tồn tại.

+ Vận dụng một trong các định lý sau đây để xác định điểm cực trị của hàm số:

Định lý 1: Giả sử hàm số $f$ liên tục trên khoảng $\left( {a;b} \right)$ chứa điểm ${x_0}$ và có đạo hàm trên các khoảng $\left( {a;{x_0}} \right)$ và $\left( {{x_0};b} \right)$. Khi đó:

Nếu 
$$
\left\{ \begin{array}{l}
f’\left( {{x_0}} \right) < 0,x \in \left( {a;{x_0}} \right)\\
f’\left( {{x_0}} \right) > 0,x \in \left( {{x_0};b} \right)
\end{array} \right.
$$
 thì hàm số đạt cực tiểu tại điểm ${x_0}.$

<img link="data_for_rag/toan12/images/tim-cuc-tri-cua-ham-so-1.png" alt="tim-cuc-tri-cua-ham-so-1">

Nếu 
$$
\left\{ \begin{array}{l}
f’\left( {{x_0}} \right) > 0,x \in \left( {a;{x_0}} \right)\\
f’\left( {{x_0}} \right) < 0,x \in \left( {{x_0};b} \right)
\end{array} \right.
$$
 thì hàm số đạt cực đại tại điểm ${x_0}.$

<img link="data_for_rag/toan12/images/tim-cuc-tri-cua-ham-so-2.png" alt="tim-cuc-tri-cua-ham-so-2">

Định lý 2: Giả sử hàm số $f$ có đạo hàm cấp một trên khoảng $\left( {a;b} \right)$ chứa điểm ${x_0}$, $f’\left( {{x_0}} \right) = 0$ và $f$ có đạo hàm cấp hai khác $0$ tại điểm ${x_0}.$

Nếu $f”\left( {{x_0}} \right) < 0$ thì hàm số $f$ đạt cực đại tại điểm ${x_0}.$

Nếu $f”\left( {{x_0}} \right) > 0$ thì hàm số $f$ đạt cực tiểu tại điểm ${x_0}.$

Chú ý: Cho hàm số $y = f(x)$ xác định trên $D.$ Điểm $x = {x_0} \in D$ là điểm cực trị của hàm số khi và chỉ khi hai điều kiện sau đây cùng thảo mãn:

+ Tại $x = {x_0}$, đạo hàm triệt tiêu (tức $f'({x_0}) = 0$) hoặc không tồn tại.

+ Đạo hàm đổi dấu khi $x$ đi qua ${x_0}.$

Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/04/tim-cuc-tri-cua-ham-so.html -->
## Ví dụ 1. Tìm cực trị (nếu có) của các hàm số sau:

a. $y = – {x^4} + 2{x^2} + 1.$

b. $y = – {x^4} + 6{x^2} – 8x + 1.$

a. TXĐ: $D = R.$

Ta có: $y’ = – 4{x^3} + 4x$ $= – 4x({x^2} – 1)$ $\Rightarrow y’ = 0 \Leftrightarrow x = 0$ hoặc $x = \pm 1.$

Cách 1: (Dùng định lý 1, xét dấu $y’$)

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty ,\mathop {\lim }\limits_{x \to + \infty } y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-cuc-tri-cua-ham-so-3.png" alt="tim-cuc-tri-cua-ham-so-3">

Hàm số đạt cực đại tại các điểm $x = \pm 1$ với giá trị cực đại của hàm số là $y( \pm 1) = 2$ và hàm số đạt cực tiểu tại điểm $x = 0$ với giá trị cực tiểu của hàm số là $y(0) = 1.$

Cách 2: (Dùng định lý 2)

$y” = – 12{x^2} + 4 = – 4(3{x^2} – 1).$

$y”\left( { \pm 1} \right) = – 8 < 0$ suy ra $x = \pm 1$ là điểm cực đại của hàm số và ${{\rm{y}}_{CĐ}} = 2.$

$y”\left( 0 \right) = 4 > 0$ suy ra  $x = 0$ là điểm cực đại của hàm số và ${{\rm{y}}_{{\rm{CT}}}} = {\rm{1}}{\rm{.}}$

b. TXĐ: $D = R.$

Ta có: $y’ = – 4{x^3} + 12x – 8$ $= – 4{(x – 1)^2}(x + 2)$ $\Rightarrow y’ = 0 \Leftrightarrow x = – 2, x = 1.$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty ,\mathop {\lim }\limits_{x \to + \infty } y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-cuc-tri-cua-ham-so-4.png" alt="tim-cuc-tri-cua-ham-so-4">

Hàm đạt cực đại tại $x = – 2$ với giá trị cực đại của hàm số là $y( – 2) = 25$, hàm số không có cực tiểu.

Nhận xét: Trong bài toán này, vì 
$$
\left\{ \begin{array}{l}
y'(1) = 0\\
y”(1) = 0
\end{array} \right.
$$
 do đó định lý 2 không khẳng định được điểm $x = 2$ có phải là điểm cực trị của hàm số hay không.

[ads]

<!-- chunk:2 level:3 source:https://toanmath.com/2018/04/tim-cuc-tri-cua-ham-so.html -->
## Ví dụ 2. Tìm cực trị (nếu có) của các hàm số sau:

a. $y = – {x^3} – \frac{3}{2}{x^2} + 6x + 1.$

b. $y = \sqrt {x + \sqrt {{x^2} – x + 1} } .$

a. TXĐ: $D = R.$

Ta có: $y’ = – 3{x^2} – 3x + 6$ $= – 3({x^2} + x – 2)$ $\Rightarrow y’ = 0 \Leftrightarrow x = – 2 , x = 1.$

$y” = – 6x – 3,$ $y”( – 2) = 9 > 0,$ $y”(1) = – 9 < 0.$

Suy ra hàm số đạt cực tiểu tại ${\rm{x}} = – {\rm{ 2}}$, ${{\rm{y}}_{{\rm{CT}}}} = {\rm{y}}\left( { – {\rm{2}}} \right) = – {\rm{9}}$ hàm số đạt cực đại tại ${\rm{x}} = {\rm{1}}$, ${{\rm{y}}_{{\rm{CĐ}}}} = {\rm{y}}\left( {\rm{1}} \right) = \frac{9}{2}.$

b. Hàm số xác định $\Leftrightarrow x + \sqrt {{x^2} – x + 1} \ge 0$ $\Leftrightarrow \sqrt {{x^2} – x + 1} \ge – x$

$$
\Leftrightarrow \left\{ \begin{array}{l}
{x^2} – x + 1 \ge 0\\
– x \le 0
\end{array} \right.
$$
 
$$
\vee \left\{ \begin{array}{l}
– x \ge 0\\
{x^2} – x + 1 \ge {( – x)^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\forall x \in R\\
x \ge 0
\end{array} \right. \vee \left\{ \begin{array}{l}
x \le 0\\
x \le 1
\end{array} \right.
$$
 $\Leftrightarrow x \ge 0 \vee x \le 0 \Leftrightarrow x \in R.$

Vậy tập xác định của hàm số: $D = R.$

$y’ = \frac{{\left( {x + \sqrt {{x^2} – x + 1} } \right)’}}{{2\sqrt {x + \sqrt {{x^2} – x + 1} } }}$ $= \frac{{1 + \frac{{2x – 1}}{{2\sqrt {{x^2} – x + 1} }}}}{{2\sqrt {x + \sqrt {{x^2} – x + 1} } }}$ $= \frac{{2\sqrt {{x^2} – x + 1} + 2x – 1}}{{2\sqrt {{x^2} – x + 1} .\sqrt {x + \sqrt {{x^2} – x + 1} } }}.$

$y’ = 0$ $\Leftrightarrow 2\sqrt {{x^2} – x + 1} = 1 – 2x$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
1 – 2x \ge 0\\
4({x^2} – x + 1) = {(1 – 2x)^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \le \frac{1}{2}\\
4 = 1
\end{array} \right.
$$

Vậy phương trình $y’ = 0$ vô nghiệm, lại có $y’$ luôn tồn tại, suy ra hàm số không có điểm cực trị.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/04/tim-cuc-tri-cua-ham-so.html -->
## Ví dụ 3. Tìm cực trị (nếu có) của các hàm số sau:

a. $y = \frac{{4 – \left| x \right|}}{{4 + \left| x \right|}}.$

b. $y = \left| {x + 3} \right| + \frac{1}{{x + 1}}.$

a. TXĐ: $D = R.$

Nếu ${\rm{x}} \in [0; + \infty )$ thì $y = \frac{{4 – x}}{{4 + x}}$ $\Rightarrow y’ = – \frac{8}{{{{(4 + x)}^2}}} < 0,$ $\forall x \in [0; + \infty ).$

Nếu ${\rm{x}} \in ( – \infty ;0]$ thì $y = \frac{{4 + x}}{{4 – x}}$ $\Rightarrow y’ = \frac{8}{{{{(4 – x)}^2}}} > 0,$ $\forall x \in ( – \infty ;0].$

Tại $x = 0$ thì $y'({0^ + }) = – \frac{1}{2}$, $y'({0^ – }) = \frac{1}{2}$. Vì $y'({0^ + }) \ne y'({0^ – })$ nên $y'(0)$ không tồn tại.

Vậy hàm số đạt cực đại tại ${\rm{x}} = 0,{\rm{ }}{{\rm{y}}_{{\rm{CĐ}}}} = {\rm{1}}.$

b. $y = \left| {x + 3} \right| + \frac{1}{{x + 1}}$ 
$$
= \left\{ \begin{array}{l}
x + 3 + \frac{1}{{x + 1}} khi x \ge – 3\\
– (x + 3) + \frac{1}{{x + 1}} khi x < – 3
\end{array} \right.
$$

TXĐ: ${\rm{D}} = R\backslash \left\{ { – 1} \right\}.$

Nếu $x \ge – 3$ thì $y = x + 3 + \frac{1}{{x + 1}}$, ta có: $y’ = 1 – \frac{1}{{{{(x + 1)}^2}}}$ $= \frac{{{{(x + 1)}^2} – 1}}{{{{(x + 1)}^2}}}.$

Và 
$$
y’ = 0 \Leftrightarrow \left\{ \begin{array}{l}
{(x + 1)^2} = 1\\
x > – 3
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x + 1 = \pm 1\\
x > – 3
\end{array} \right. \Leftrightarrow \left[ \begin{array}{l}
x = 0\\
x = – 2
\end{array} \right.
$$

Tại $x = – 3$, ta có: $y'( – {3^ + })$ $= 1 – \frac{1}{{{{( – 3 + 1)}^2}}} = \frac{3}{4}$, $y'( – {3^ – })$ $= – 1 – \frac{1}{{{{( – 3 + 1)}^2}}} = – \frac{5}{4}.$

Vì $y'( – {3^ + }) \ne y'( – {3^ – })$ nên $y'( – 3)$ không tồn tại.

Nếu $x < – 3$ thì $y = – (x + 3) + \frac{1}{{x + 1}}$, ta có: $y’ = – 1 – \frac{1}{{{{(x + 1)}^2}}} < 0$, $\forall x < – 3.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-cuc-tri-cua-ham-so-5.png" alt="tim-cuc-tri-cua-ham-so-5">

Suy ra điểm cực tiểu của hàm số là $x = – 3$, ${{\rm{y}}_{{\rm{CT}}}} = – \frac{1}{2}$ và ${\rm{x}} = 0$, ${{\rm{y}}_{{\rm{CT}}}} = {\rm{ 4}}$, điểm cực đại của hàm số là ${\rm{x}} = – {\rm{ 2}}$, ${{\rm{y}}_{{\rm{CD}}}} = 0.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/04/tim-cuc-tri-cua-ham-so.html -->
## Ví dụ 4. Tìm cực trị (nếu có) của hàm số: $y = 3 – 2\cos x – \cos 2x.$

TXĐ: ${\rm{D}} = R.$

Ta có: $y’ = 2\sin x\left( {2\cos x + 1} \right)$ và $y” = 2\cos x + 4\cos 2x.$

$y’ = 0$ ⇔ 
$$
\left[ \begin{array}{l}
\sin x = 0 \Leftrightarrow x = k\pi \\
\cos x = – \frac{1}{2} \Leftrightarrow x = \pm \frac{{2\pi }}{3} + k2\pi
\end{array} \right.
$$

$y”\left( {k\pi } \right)$ $= 2\cos \left( {k\pi } \right) + 2\cos 2\left( {k\pi } \right).$

$y”\left( {k\pi } \right) = 6 > 0$ nếu $k$ chẵn, suy ra hàm số đạt cực tiểu tại điểm $x = 2n\pi, n \in Z$ và $y\left( {2n\pi } \right) = 0.$

$y”\left( {k\pi } \right) = 2 > 0$ nếu $k$ lẻ, suy ra hàm số đạt cực tiểu tại điểm $x = \left( {2n + 1} \right)\pi, n \in Z$ và $y\left( {2n + 1} \right)\pi = 4.$

$y”\left( { \pm \frac{{2\pi }}{3} + k2\pi } \right) < 0$ suy ra hàm số đạt cực đại tại điểm $x = \pm \frac{{2\pi }}{3} + k2\pi$ và $y\left( { \pm \frac{{2\pi }}{3} + k2\pi } \right) = \frac{9}{2}.$