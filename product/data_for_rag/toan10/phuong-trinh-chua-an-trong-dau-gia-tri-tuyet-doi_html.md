# Phương trình chứa ẩn trong dấu giá trị tuyệt đối

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
Bài viết hướng dẫn phương pháp giải phương trình chứa ẩn trong dấu giá trị tuyệt đối (GTTĐ), đây là dạng phương trình thường gặp trong chủ đề *một số phương trình quy về phương trình bậc nhất hoặc bậc hai* trong chương trình Đại số 10.

Phương pháp:

Để giải phương trình chứa ẩn trong dấu giá trị tuyệt đối (GTTĐ), ta tìm cách để khử dấu giá trị tuyệt đối (GTTĐ), bằng cách:

• Dùng định nghĩa hoặc tính chất của giá trị tuyệt đối (GTTĐ).

• Bình phương hai vế của phương trình.

• Đặt ẩn phụ.

Các dạng phương trình chứa ẩn trong dấu giá trị tuyệt đối (GTTĐ) tổng quát và cách giải:

• $\left| {f(x)} \right| = \left| {g(x)} \right|$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
f(x) = g(x)\\
f(x) = – g(x)
\end{array} \right.
$$
 hoặc $\left| {f(x)} \right| = \left| {g(x)} \right|$ $\Leftrightarrow {f^2}(x) = {g^2}(x).$

• $\left| {f(x)} \right| = g(x)$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
g(x) \ge 0\\
{f^2}(x) = {g^2}(x)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
g(x) \ge 0\\
\left[ \begin{array}{l}
f(x) = g(x)\\
f(x) = – g(x)
\end{array} \right.
\end{array} \right.
$$
 hoặc $\left| {f(x)} \right| = g(x)$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{\left\{ {\begin{array}{c}
{f(x) = g(x)}\\
{f(x) \ge 0}
\end{array}} \right.}\\
{\left\{ {\begin{array}{c}
{ – f(x) = g(x)}\\
{f(x) < 0}
\end{array}} \right.}
\end{array}} \right.
$$

Ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Ví dụ 1. Giải các phương trình sau:

a. $\left| {2x + 1} \right| = \left| {{x^2} – 3x – 4} \right|.$

b. $\left| {3x – 2} \right| = 3 – 2x.$

c. $\left| {{x^2} – 4x – 5} \right| = 4x – 17.$

d. $\left| {2x – 5} \right| + \left| {2{x^2} – 7x + 5} \right| = 0.$

a. Phương trình 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{2x + 1 = {x^2} – 3x – 4}\\
{2x + 1 = – \left( {{x^2} – 3x – 4} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{{x^2} – 5x – 5 = 0}\\
{{x^2} – x – 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = \frac{{5 \pm \sqrt {45} }}{2}}\\
{x = \frac{{1 \pm \sqrt {13} }}{2}}
\end{array}} \right.
$$

Vậy phương trình có nghiệm: $x = \frac{{5 \pm \sqrt {45} }}{2}$ và $\frac{{1 \pm \sqrt {13} }}{2}.$

b. Ta giải phương trình theo $2$ cách:

• Cách 1:

+ Với $3 – 2x < 0 \Leftrightarrow x > \frac{3}{2}$, ta có: $VT \ge 0$, $VP < 0$, suy ra phương trình vô nghiệm.

+ Với $3 – 2x \ge 0 \Leftrightarrow x \le \frac{3}{2}$ khi đó hai vế của phương trình không âm, suy ra:

Phương trình $\Leftrightarrow {\left| {3x – 2} \right|^2} = {\left( {3 – 2x} \right)^2}$ $\Leftrightarrow 9{x^2} – 12x + 4 = 4{x^2} – 12x + 9$ $\Leftrightarrow 5{x^2} = 5$ $\Leftrightarrow x = \pm 1$ (thỏa mãn).

Vậy phương trình có nghiệm là: $x = \pm 1.$

• Cách 2:

+ Với $3x – 2 \ge 0 \Leftrightarrow x \ge \frac{2}{3}$, phương trình tương đương với: $3{\rm{x}} – 2 = 3 – 2{\rm{x}}$ $\Leftrightarrow 5{\rm{x}} = 5$ $\Leftrightarrow x = 1$ (thỏa mãn).

+ Với  $3x – 2 < 0 \Leftrightarrow x < \frac{2}{3}$, phương trình tương đương với: $– \left( {3{\rm{x}} – 2} \right) = 3 – 2{\rm{x}}$ $\Leftrightarrow {\rm{x}} = – 1$ (thỏa mãn).

Vậy phương trình có nghiệm: $x = \pm 1.$

c.

+ Với $4x – 17 < 0 \Leftrightarrow x < \frac{{17}}{4}$, ta có: $VT \ge 0$, $VP < 0$ suy ra phương trình vô nghiệm.

+ Với $4x – 17 \ge 0 \Leftrightarrow x \ge \frac{{17}}{4}$ khi đó hai vế của phương trình không âm, suy ra:

Phương trình $\Leftrightarrow {\left| {{x^2} – 4x – 5} \right|^2} = {\left( {4x – 17} \right)^2}$ $\Leftrightarrow {\left( {{x^2} – 4x – 5} \right)^2} = {\left( {4x – 17} \right)^2}$ $\Leftrightarrow \left( {{x^2} – 8x + 12} \right)\left( {{x^2} – 22} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{{x^2} – 8x + 12 = 0}\\
{{x^2} – 22 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{\left[ {\begin{array}{c}
{x = 2}\\
{x = 6}
\end{array}} \right.}\\
{x = \pm \sqrt {22} }
\end{array}} \right.
$$

Đối chiếu với điều kiện $x \ge \frac{{17}}{4}$, ta thấy chỉ có $x = 6$ và $x = \sqrt {22}$ thỏa mãn.

Vậy phương trình có nghiệm: $x = 6$ và $x = \sqrt {22} .$

d. Ta có: $\left| {2x – 5} \right| \ge 0$, $\left| {2{x^2} – 7x + 5} \right| \ge 0$, suy ra: $\left| {2x – 5} \right| + \left| {2{x^2} – 7x + 5} \right| \ge 0.$

Dấu bằng xảy ra khi và chỉ khi: 
$$
\left\{ {\begin{array}{c}
{2x – 5 = 0}\\
{2{x^2} – 7x + 5 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{x = \frac{5}{2}}\\
{\left[ {\begin{array}{c}
{x = 1}\\
{x = \frac{5}{2}}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{5}{2}.$

Vậy phương trình có nghiệm: $x = \frac{5}{2}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Ví dụ 2. Giải các phương trình sau:

a. ${\left( {x + 1} \right)^2} – 3\left| {x + 1} \right| + 2 = 0.$

b. $4x\left( {x – 1} \right) = \left| {2x – 1} \right| + 1.$

c. ${x^2} + \frac{9}{{{{\left( {x – 1} \right)}^2}}} + 1$ $= 2x + 7\left| {\frac{{{x^2} – 2x – 2}}{{x – 1}}} \right|.$

a. Đặt $t = \left| {x + 1} \right|$, $t \ge 0.$

Phương trình trở thành: ${t^2} – 3t + 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = 1}\\
{t = 2}
\end{array}} \right.
$$

+ Với $t = 1$, ta có: $\left| {x + 1} \right| = 1$ $\Leftrightarrow x + 1 = \pm 1$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = 0}\\
{x = – 2}
\end{array}} \right.
$$

+ Với $t = 2$, ta có: $\left| {x + 1} \right| = 2$ $\Leftrightarrow x + 1 = \pm 2$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = 1}\\
{x = – 3}
\end{array}} \right.
$$

Vậy phương trình có nghiệm: $x = – 3$, $x = – 2$, $x = 0$ và $x = 1.$

b. Phương trình tương đương với: $4{x^2} – 4x – \left| {2x – 1} \right| – 1 = 0.$

Đặt $t = \left| {2x – 1} \right|$, $t \ge 0$ $\Rightarrow {t^2} = 4{x^2} – 4x + 1$ $\Rightarrow 4{x^2} – 4x = {t^2} – 1.$

Phương trình trở thành: ${t^2} – 1 – t – 1 = 0$ $\Leftrightarrow {t^2} – t – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = – 1}\\
{t = 2}
\end{array}} \right.
$$

Vì $t \ge 0 \Rightarrow t = 2$ nên $\left| {2x – 1} \right| = 2$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{2x – 1 = 2}\\
{2x – 1 = – 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = \frac{3}{2}}\\
{x = – \frac{1}{2}}
\end{array}} \right.
$$

Vậy phương trình có nghiệm là: $x = \frac{3}{2}$ và $x = – \frac{1}{2}.$

c. Điều kiện xác định: $x \ne 1.$

Phương trình tương đương: ${\left( {x – 1} \right)^2} + \frac{9}{{{{\left( {x – 1} \right)}^2}}}$ $= 7\left| {x – 1 – \frac{3}{{x – 1}}} \right|.$

Đặt $t = \left| {x – 1 – \frac{3}{{x – 1}}} \right|.$

Suy ra: ${t^2} = {\left( {x – 1} \right)^2} + \frac{9}{{{{\left( {x – 1} \right)}^2}}} – 6$ $\Rightarrow {\left( {x – 1} \right)^2} + \frac{9}{{{{\left( {x – 1} \right)}^2}}}$ $= {t^2} + 6.$

Phương trình trở thành: ${t^2} + 6 = 7t$ $\Leftrightarrow {t^2} – 7t + 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = 1}\\
{t = 6}
\end{array}} \right.
$$

+ Với $t = 1$, ta có: $\left| {x – 1 – \frac{3}{{x – 1}}} \right| = 1$ $\Leftrightarrow \left| {\frac{{{x^2} – 2x – 2}}{{x – 1}}} \right| = 1$ $\Leftrightarrow \frac{{{x^2} – 2x – 2}}{{x – 1}} = \pm 1$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{{x^2} – 3x – 1 = 0}\\
{{x^2} – x – 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = \frac{{3 \pm \sqrt {13} }}{2}}\\
{x = \frac{{1 \pm \sqrt {13} }}{2}}
\end{array}} \right.
$$
 (thỏa mãn).

+ Với $t = 6$, ta có: $\left| {x – 1 – \frac{3}{{x – 1}}} \right| = 6$ $\Leftrightarrow \left| {\frac{{{x^2} – 2x – 2}}{{x – 1}}} \right| = 6$ $\Leftrightarrow \frac{{{x^2} – 2x – 2}}{{x – 1}} = \pm 6$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{{x^2} – 8x + 4 = 0}\\
{{x^2} + 4x – 8 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = 4 \pm 2\sqrt 3 }\\
{x = – 2 \pm 2\sqrt 3 }
\end{array}} \right.
$$
 (thỏa mãn).

Vậy phương trình có nghiệm: $x = \frac{{3 \pm \sqrt {13} }}{2}$, $x = \frac{{1 \pm \sqrt {13} }}{2}$, $x = 4 \pm 2\sqrt 3$ và $x = – 2 \pm 2\sqrt 3 .$

[ads]

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Ví dụ 3. Giải và biện luận các phương trình sau:

a. $\left| {mx + 2m} \right| = \left| {mx + x + 1} \right|$ $(*).$

b. $\left| {mx + 2x – 1} \right| = \left| {x – 1} \right|$ $(**).$

a. Ta có: $\left| {mx + 2m} \right| = \left| {mx + x + 1} \right|$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{mx + 2m = mx + x + 1}\\
{mx + 2m = – \left( {mx + x + 1} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = 2m – 1}\\
{\left( {2m + 1} \right)x = – 2m – 1\:(1)}
\end{array}} \right.
$$

Giải $(1):$

+ Với $2m + 1 = 0$ $\Leftrightarrow m = – \frac{1}{2}$, phương trình trở thành $0x = 0$, suy ra phương trình nghiệm đúng với mọi $x.$

+ Với $2m + 1 \ne 0$ $\Leftrightarrow m \ne – \frac{1}{2}$, phương trình tương đương với: $x = – 1.$

Kết luận:

+ Với $m = – \frac{1}{2}$, phương trình $(*)$ nghiệm đúng với mọi $x.$

+ Với $m \ne – \frac{1}{2}$, phương trình $(*)$ có hai nghiệm là: $x = – 1$ và $x = 2m – 1.$

b. Ta có: $\left| {mx + 2x – 1} \right| = \left| {x – 1} \right|$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{mx + 2x – 1 = x – 1}\\
{mx + 2x – 1 = – \left( {x – 1} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{(m + 1)x = 0\:(2)}\\
{(m + 3)x = 2\:(3)}
\end{array}} \right.
$$

• Với phương trình $(2)$, ta có:

$m = – 1$ thì phương trình $(2)$ nghiệm đúng với mọi $x.$

$m \ne – 1$ thì phương trình $(2)$ có nghiệm $x = 0.$

• Với phương trình $(3)$, ta có:

$m = – 3$, thì phương trình $(3)$ vô nghiệm.

$m \ne – 3$ thì phương trình $(3)$ có nghiệm $x = \frac{2}{{m + 3}}.$

Kết luận:

+ Với $m = – 1$, phương trình $(**)$ nghiệm đúng với mọi $x.$

+ Với $m = – 3$, phương trình $(**)$ có nghiệm $x = 0.$

+ Với $m \ne – 1$ và $m \ne – 3$, phương trình $(**)$ có nghiệm $x = 0$ và $x = \frac{2}{{m + 3}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Ví dụ 4. Tìm $m$ để phương trình: $\left| {{x^2} + x} \right|$ $= \left| {m{x^2} – (m + 1)x – 2m – 1} \right|$ có ba nghiệm phân biệt.

Phương trình tương đương với: $\left| {x\left( {x + 1} \right)} \right|$ $= \left| {\left( {x + 1} \right)\left( {mx – 2m – 1} \right)} \right|$ $\Leftrightarrow \left| {x + 1} \right|\left[ {\left| x \right| – \left| {mx – 2m – 1} \right|} \right] = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = – 1}\\
{\left| x \right| = \left| {mx – 2m – 1} \right|\:(*)}
\end{array}} \right.
$$

Ta có: 
$$
(*) \Leftrightarrow \left[ {\begin{array}{c}
{mx – 2m – 1 = x}\\
{mx – 2m – 1 = – x}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{(m – 1)x = 1 + 2m\:(1)}\\
{(m + 1)x = 1 + 2m\:(2)}
\end{array}} \right.
$$

+ Nếu $m = 1$, thì phương trình $(1)$ vô nghiệm, khi đó phương trình ban đầu không thể có ba nghiệm phân biệt.

+ Nếu $m = – 1$, thì phương trình $(2)$ vô nghiệm, khi đó phương trình ban đầu không thể có ba nghiệm phân biệt.

+ Nếu $m \ne \pm 1$, thì 
$$
(*) \Leftrightarrow \left[ {\begin{array}{c}
{x = \frac{{1 + 2m}}{{m – 1}}}\\
{x = \frac{{1 + 2m}}{{m + 1}}}
\end{array}} \right.
$$

Suy ra để phương trình ban đầu có ba nghiệm phân biệt khi và chỉ khi: 
$$
\left\{ {\begin{array}{c}
{\frac{{1 + 2m}}{{m – 1}} \ne – 1}\\
\begin{array}{l}
\frac{{1 + 2m}}{{m + 1}} \ne – 1\\
\frac{{1 + 2m}}{{m – 1}} \ne \frac{{1 + 2m}}{{m + 1}}
\end{array}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{m \ne 0}\\
\begin{array}{l}
m \ne – \frac{2}{3}\\
m \ne – \frac{1}{2}
\end{array}
\end{array}} \right.
$$

Vậy với $m \notin \left\{ { – 1; – \frac{1}{2}; – \frac{2}{3};0;1} \right\}$ thì phương trình có ba nghiệm phân biệt.

Bài tập rèn luyện:
Phần đề bài:

<!-- chunk:5 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 1. Giải các phương trình sau:

a. $|3x – 2| = {x^2} + 2x + 3.$

b. $\left| {{x^3} – 1} \right| = \left| {{x^2} – 3x + 2} \right|.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 2. Giải các phương trình sau:

a. ${\left( {2x – 1} \right)^2} – 3\left| {2x – 1} \right| – 4 = 0.$

b. $\frac{{{x^4} – 6{x^2} + 4}}{{{x^2}}} = \left| {\frac{{{x^2} – 2}}{x}} \right|.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 3. Cho phương trình: ${x^2} – 2x – 2\left| {x – 1} \right| + m + 3 = 0.$

a. Giải phương trình khi $m = – 2.$

b. Tìm $m$ để phương trình sau có nghiệm.

<!-- chunk:8 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 4. Giải và biện luận các phương trình sau:

a. $\left| {mx + 2m} \right| = \left| {x + 1} \right|.$

b. $\left| {mx + 2x} \right| = \left| {mx – 1} \right|.$

Phần đáp số – hướng dẫn giải:

<!-- chunk:9 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 1.

a. Ta có: $|3x – 2| =$ 
$$
\left\{ \begin{array}{l}
3x – 2\:khi\:x \ge \frac{2}{3}\\
– 3x + 2\:khi\:x < \frac{2}{3}
\end{array} \right.
$$

• Nếu $x \ge \frac{2}{3}$, suy ra: $PT \Leftrightarrow 3x – 2 = {x^2} + 2x + 3$ $\Leftrightarrow {x^2} – x + 5 = 0$, phương trình vô nghiệm.

• Nếu $x < \frac{2}{3}$, suy ra: $PT \Leftrightarrow – 3x + 2 = {x^2} + 2x + 3$ $\Leftrightarrow {x^2} + 5x + 1 = 0$ $\Leftrightarrow x = \frac{{ – 5 \pm \sqrt {21} }}{2}$, hai nghiệm này đều thỏa mãn $x < \frac{2}{3}.$

Vậy nghiệm của phương trình đã cho là: $x = \frac{{ – 5 \pm \sqrt {21} }}{2}.$

b. $x = 1$, $x = – 1 \pm \sqrt 2 .$

<!-- chunk:10 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 2.

a. Đặt $t = \left| {2x – 1} \right|$, $t \ge 0.$

Phương trình trở thành ${t^2} – 3t – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = – 1\:(loại)}\\
{t = 4}
\end{array}} \right.
$$

Với $t = 4$, ta có: $\left| {2x – 1} \right| = 4$ $\Leftrightarrow 2x – 1 = \pm 4$ $\Leftrightarrow x = \frac{5}{2}$ hoặc $x = – \frac{3}{2}.$

Vậy phương trình có nghiệm là $x = – \frac{3}{2}$ và $x = \frac{5}{2}.$

b. Điều kiện xác định: $x \ne 0.$

Đặt $t = \left| {\frac{{{x^2} – 2}}{x}} \right|$, $t \ge 0.$

Phương trình trở thành: ${t^2} – t – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{t = – 1}\\
{t = 2}
\end{array}} \right.
$$

Với $t = 2$, ta có: $\left| {\frac{{{x^2} – 2}}{x}} \right| = 2$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = – 1 \pm \sqrt 3 }\\
{x = 1 \pm \sqrt 3 }
\end{array}} \right.
$$

Vậy phương trình có nghiệm: $x = – 1 \pm \sqrt 3$ và $x = 1 \pm \sqrt 3 .$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 3.

Phương trình $\Leftrightarrow {\left( {x – 1} \right)^2} – 2\left| {x – 1} \right| + m + 2 = 0.$

Đặt $t = \left| {x – 1} \right|$, $t \ge 0$, ta có phương trình: ${t^2} – 2t + m + 2 = 0$ $(1).$

a. Khi $m = – 2$, ta có: 
$$
{t^2} – 2t = 0 \Leftrightarrow \left[ {\begin{array}{c}
{t = 0}\\
{t = 2}
\end{array}} \right.
$$

Suy ra nghiệm phương trình là $x = 1$, $x = 3$, $x = – 1.$

b. Phương trình đã cho có nghiệm $⇔$ phương trình $(1)$ có nghiệm $t \ge 0$ $\Leftrightarrow m = – {t^2} + 2t – 2$ có nghiệm $t \ge 0$ $\Leftrightarrow$ đồ thị hàm số $f\left( t \right) = – {t^2} + 2t – 2$ với $t \in \left[ {0; + \infty } \right)$ cắt trục hoành $\Leftrightarrow m \le – 2.$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/08/phuong-trinh-chua-an-trong-dau-gia-tri-tuyet-doi.html -->
## Bài toán 4.

a. Ta có 
$$
PT \Leftrightarrow \left[ {\begin{array}{c}
{mx + 2m = x + 1}\\
{mx + 2m = – \left( {x + 1} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{\left( {m – 1} \right)x = 1 – 2m \: \left( 1 \right)}\\
{\left( {m + 1} \right)x = – 2m – 1 \: \left( 2 \right)}
\end{array}} \right.
$$

• Giải $(1)$:

+ Với $m = 1$ phương trình trở thành $0x = – 1$, phương trình vô nghiệm.

+ Với $m \ne 1$ phương trình tương đương với $x = \frac{{1 – 2m}}{{m – 1}}.$

• Giải $(2)$:

+ Với $m = – 1$ phương trình trở thành $0x = 1$, phương trình vô nghiệm.

+ Với $m \ne – 1$ phương trình tương đương với $x = \frac{{ – 2m – 1}}{{m + 1}}.$

Kết luận:

+ Với 
$$
\left[ {\begin{array}{c}
{m = 1}\\
{m = – 1}
\end{array}} \right.
$$
 phương trình có nghiệm là $x = \frac{{ – 3}}{2}.$

+ Với 
$$
\left\{ {\begin{array}{c}
{m \ne 1}\\
{m \ne – 1}
\end{array}} \right.
$$
 phương trình có nghiệm là $x = \frac{{1 – 2m}}{{m – 1}}$ và $x = \frac{{ – 2m – 1}}{{m + 1}}.$

b. Ta có: $\left| {mx + 2x} \right| = \left| {mx – 1} \right|$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{mx + 2x = mx – 1}\\
{mx + 2x = – \left( {mx – 1} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{x = – \frac{1}{2}}\\
{(2m + 2)x = 1 \: (*)}
\end{array}} \right.
$$

Với phương trình $(*)$, ta có:

$m = – 1$ thì phương trình $(*)$ vô nghiệm.

$m \ne – 1$ thì phương trình $(*)$ có nghiệm $x = \frac{1}{{2m + 2}}.$

Kết luận:

$m = – 1$, phương trình có nghiệm $x = – \frac{1}{2}.$

$m \ne – 1$, phương trình có nghiệm $x = – \frac{1}{2}$ và $x = \frac{1}{{2m + 2}}.$