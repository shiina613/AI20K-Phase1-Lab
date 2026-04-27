# Phương trình bậc nhất

<!-- chunk:0 level:0 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán điển hình về chủ đề phương trình bậc nhất, giúp học sinh học tốt chương trình Đại số lớp 10.

<!-- chunk:1 level:2 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài toán 1. Giải và biện luận phương trình $ax + b = 0.$
Phương pháp chung:

Viết lại phương trình dưới dạng: $ax = – b$ $(1).$

a. Nếu $a = 0.$

$(1) \Leftrightarrow 0 = – b$ $\Leftrightarrow b = 0.$

Khi đó:

+ Nếu $b = 0$, phương trình nghiệm đúng với mọi $x \in R.$

+ Nếu $b \ne 0$, phương trình vô nghiệm.

b. Nếu $a \ne 0$ thì:

$(1) \Leftrightarrow x = – \frac{b}{a}$: phương trình có nghiệm duy nhất.

Kết luận:

+ Với $a \ne 0$, phương trình có nghiệm duy nhất $x = – \frac{b}{a}.$

+ Với $a = b = 0$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $a \ne 0$ và $b = 0$, phương trình vô nghiệm.

Ví dụ minh họa:

<!-- chunk:2 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 1: Giải và biện luận phương trình: ${m^2}x + 6 = 4x + 3m.$

Lời giải:

Viết lại phương trình dưới dạng:

$\left( {{m^2} – 4} \right)x = 3m – 6$ $(1).$

a. Nếu ${m^2} – 4 = 0$ $\Leftrightarrow m = \pm 2.$

+ Với $m = 2$, phương trình $(1) \Leftrightarrow 0x = 0$, luôn đúng.

Vậy phương trình nghiệm đúng với $\forall x \in R.$

+ Với $m = -2$, phương trình $(1) \Leftrightarrow 0x = – 12$, mâu thuẫn.

Vậy phương trình vô nghiệm.

b. Nếu ${m^2} – 4 \ne 0$ $\Leftrightarrow m \ne \pm 2.$

$(2) \Leftrightarrow x = \frac{3}{{m + 2}}$ là nghiệm duy nhất của phương trình.

Kết luận:

+ Với $m \ne \pm 2$, phương trình có nghiệm duy nhất $x = \frac{3}{{m + 2}}.$

+ Với $m = 2$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $m = -2$, phương trình vô nghiệm.

Nhận xét: Trong ví dụ trên ta thấy tồn tại đầy đủ các khả năng được minh hoạ trong bài toán tổng quát, tuy nhiên sẽ tồn tại những bài toán là một trường hợp đặc biệt:

1. Hệ số $a \ne 0$ với mọi giá trị của tham số, khi đó ta kết luận ngay tính duy nhất nghiệm của phương trình.

2. Hệ số $a = 0$ với mọi giá trị của tham số, khi đó ta biện luận cho $b.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 2: Giải và biện luận phương trình: ${m^2}x + 1 = (m – 1)x + m.$

Lời giải:

Viết lại phương trình dưới dạng:

$\left( {{m^2} – m + 1} \right)x = m – 1$ $(1).$

Ta có ${m^2} – m + 1$ $= {\left( {m – \frac{1}{2}} \right)^2} + \frac{3}{4} \ne 0$, $\forall m.$ Do đó:

$(1) \Leftrightarrow x = \frac{{m – 1}}{{{m^2} – m + 1}}.$

Vậy với $\forall m$, phương trình có nghiệm duy nhất $x = \frac{{m – 1}}{{{m^2} – m + 1}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 3: Giải và biện luận phương trình: $m(x – m + 3) = m(x – 2) + 6.$

Lời giải:

Viết lại phương trình dưới dạng:

${m^2} – 5m + 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 2}\\
{m = 3}
\end{array}.} \right.
$$

Kết luận:

+ Với $m = 2$ hoặc $m = 3$, phương trình nhận mọi $x$ làm nghiệm.

+ Với $m \in R\backslash \{ 2;3\}$, phương trình vô nghiệm.

Chú ý. Trong trường hợp bài toán có nhiều tham số chúng ta cần khéo léo biện luận theo các tham số đó để vét cạn được các trường hợp.

<!-- chunk:5 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 4: Giải và biện luận phương trình: ${a^2}x = a(x + b) – b$ $(1).$

Lời giải:

Viết lại phương trình dưới dạng: $a(a – 1)x = b(a – 1)$ $(2).$

a. Nếu ${a^2} – a = 0$ $\Leftrightarrow a = 0$ hoặc $a = 1.$

Với $a = 0$ thì $(2) \Leftrightarrow 0x = – b.$

+ Với $b = 0$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $b \ne 0$, phương trình vô nghiệm.

Với $a = 1$, thì $(2) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với mọi $x \in R.$

b. Nếu ${a^2} – a \ne 0$ $\Leftrightarrow a \ne 0$ và $a \ne 1.$

Khi đó:

$(2) \Leftrightarrow x = \frac{b}{a}$: phương trình có nghiệm duy nhất.

Kết luận:

+ Với $a = b = 0$ hoặc $a = 1$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $a = 0$ và $b \ne 0$, phương trình vô nghiệm.

+ Với $a \ne 0$ và $a \ne 1$, phương trình có nghiệm duy nhất $x = \frac{b}{a}.$

<!-- chunk:6 level:2 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài toán 2. Phương trình có nghiệm thoả mãn điều kiện cho trước.

Phương pháp chung:

Cho phương trình: $f(x;m) = 0$ $(1).$

Giả sử điều kiện cho ẩn số (nếu cần) là $D.$

Biến đổi phương trình về dạng:

$ax = – b$ $(2).$

Khi có:

(i). Phương trình $(1)$ vô nghiệm:

$$
\Leftrightarrow \left[ \begin{array}{l}
a = 0\,\,\,\& \,\,\,b \ne 0\\
\left\{ {\begin{array}{l}
{a \ne 0}\\
{ – \frac{b}{a} \notin D}
\end{array}} \right.
\end{array} \right..
$$

(ii). Phương trình $(1)$ có nghiệm:

$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = b = 0}\\
{\left\{ {\begin{array}{l}
{a \ne 0}\\
{ – \frac{b}{a} \in D}
\end{array}} \right.}
\end{array}} \right..
$$

(iii). Phương trình $(1)$ có nghiệm duy nhất:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \ne 0}\\
{ – \frac{b}{a} \in D}
\end{array}} \right..
$$

(iv). Phương trình $(1)$ có nghiệm $\forall x \in D$:

$\Leftrightarrow a = b = 0.$

Chú ý: Trong nhiều trường hợp các em học sinh nên trình bày đòi hỏi của bài toán thông qua các bước giải biện luận.

Ví dụ minh họa:

<!-- chunk:7 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 5: Tìm $m$ để phương trình sau vô nghiệm:

$\frac{{x – m}}{{x – 1}} + \frac{{x – 2}}{{x + 1}} = 2$ $(1).$

Lời giải:

Điều kiện $x \ne \pm 1.$

Viết lại phương trình dưới dạng:

$(m + 2)x = 4 – m$ $(2).$

a. Nếu $m + 2 = 0 \Leftrightarrow m = – 2.$

$(2) \Leftrightarrow 0x = 6$ (mâu thuẫn) $\Rightarrow$ phương trình vô nghiệm.

b. Nếu $m – 2 \ne 0$ $\Leftrightarrow m \ne 2.$

$(2) \Leftrightarrow x = \frac{{4 – m}}{{m + 2}}.$

Do đó $(1)$ vô nghiệm:

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\frac{{4 – m}}{{m + 2}} = 1}\\
{\frac{{4 – m}}{{m + 2}} = – 1}
\end{array}} \right.
$$
 $\Leftrightarrow m = 1.$

Vậy với $m = -2$ hoặc $m = 1$ phương trình $(1)$ vô nghiệm.

Nhận xét: Trong lời giải trên chúng ta trình bày theo các bước của bài toán giải biện luận, tuy nhiên cũng có thể trình bày dưới dạng:

Điều kiện $x \ne \pm 1.$

Viết lại phương trình dưới dạng:

$(m + 2)x = 4 – m$ $(2).$

Phương trình $(1)$ vô nghiệm:

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{m + 2 = 0}\\
{4 – m \ne 0}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{m + 2 \ne 0}\\
{\frac{{4 – m}}{{m + 2}} = 1 \vee \frac{{4 – m}}{{m + 2}} = – 1}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – 2}\\
{m = 1}
\end{array}} \right..
$$

Tuy nhiên cách trình bày kiểu này có thể khiến một vài em học sinh thấy phức tạp. Do vậy nếu bài toán yêu cầu “Tìm điều kiện của tham số để phương trình có nghiệm (hoặc vô nghiệm)” tốt nhất các em hãy trình bày theo các bước của bài toán giải biện luận.

<!-- chunk:8 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 6: Tìm $m$ để phương trình sau có nghiệm duy nhất:

$\frac{{x + 1}}{{x – 1}} = \frac{{x + 2}}{{x – m}}$ $(1).$

Lời giải:

Điều kiện $x \ne 1$ và $x \ne m.$

Viết lại phương trình dưới dạng:

$mx = 2 – m$ $(2).$

Do đó $(1)$ có nghiệm duy nhất:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{x \ne 1}\\
{x \ne m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\frac{{2 – m}}{m} \ne 1}\\
{\frac{{2 – m}}{m} \ne m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{m \ne 1}\\
{{m^2} + m – 2 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m \notin \{ – 2;0;1\} .$

Vậy với $m \notin \{ – 2;0;1\}$ phương trình $(1)$ có nghiệm duy nhất.

<!-- chunk:9 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 7: Tìm $m$ để phương trình sau có tập hợp nghiệm là $R$:

$m\left( {{m^2}x – 1} \right) = 1 – x$ $(1).$

Lời giải:

Viết lại phương trình dưới dạng:

$\left( {{m^3} + 1} \right)x = m + 1$ $(2).$

Do đó $(1)$ có tập hợp nghiệm là $R.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^3} + 1 = 0}\\
{m + 1 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = – 1.$

Vậy với $m = -1$ phương trình $(1)$ có tập hợp nghiệm là $R.$

<!-- chunk:10 level:3 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Ví dụ 8: Tìm $m$ để phương trình sau có nghiệm:

$\frac{{3x – m}}{{\sqrt {x – 2} }} + \sqrt {x – 2} = \frac{{2x + 2m – 1}}{{\sqrt {x – 2} }}$ $(1).$

Lời giải:

Điều kiện: $x > 2.$

Viết lại phương trình dưới dạng:

$2x = 3m + 1$ $\Leftrightarrow x = \frac{{3m + 1}}{2}.$

Điều kiện để phương trình có nghiệm là:

$\frac{{3m + 1}}{2} > 2$ $\Leftrightarrow m > 1.$

Vậy với $m > 1$ phương trình $(1)$ có nghiệm.

<!-- chunk:11 level:2 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài toán 3. Giải và biện luận phương trình $ax + by = c.$
Phương pháp chung:

a. Nếu $a \ne 0$ và $b = 0$ thì phương trình trở thành:

$ax = c$ $\Leftrightarrow x = \frac{c}{a}.$

Vậy tập hợp nghiệm của phương trình là $S = \left\{ {\left( {\frac{c}{a};{y_0}} \right);{y_0} \in R} \right\}.$

b. Nếu $a = 0$ và $b \ne 0$ thì phương trình trở thành:

$by = c$ $\Leftrightarrow y = \frac{c}{b}.$

Vậy tập hợp nghiệm của phương trình là $S = \left\{ {\left( {{x_0};\frac{c}{b}} \right);{x_0} \in R} \right\}.$

c. Nếu $a \ne 0$ và $b \ne 0$ thì khi đó nếu:

+ Ta cho $x = {x_0}$ tuỳ ý, khi đó $y = \frac{{c – a{x_0}}}{b}.$

Vậy tập hợp nghiệm của phương trình là $S = \left\{ {\left( {{x_0};\frac{{c – a{x_0}}}{b}} \right);{x_0} \in R} \right\}.$

+ Ta cho $y = {y_0}$ tuỳ ý, khi đó $x = \frac{{c – b{y_0}}}{a}.$

Vậy tập hợp nghiệm của phương trình là $S = \left\{ {\left( {\frac{{c – b{y_0}}}{a};{y_0}} \right);{y_0} \in R} \right\}.$

d. Nếu $a = b = c = 0$ thì $x$ và $y$ có giá trị tuỳ ý.

e. Nếu $a = b = 0$ và $c \ne 0$ thì phương trình vô nghiệm.

<!-- chunk:12 level:4 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài tập 1. Giải và biện luận các phương trình:

a. ${m^2}(x + 1) = x + m.$

b. ${(m + 1)^2}x – m = (2m + 5)x + 2.$

c. $a\left( {ax + 2{b^2}} \right) – {a^2} = {b^2}(x + a).$

d. $a(x – b) – 1 = b(1 – 2x).$

e. $\frac{{x + a}}{{b – a}} + \frac{{x – a}}{{b + a}} = \frac{2}{{{a^2} + {b^2}}}.$

<!-- chunk:13 level:4 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài tập 2. Xác định $m$ để các phương trình sau vô nghiệm:

a. ${(m – 1)^2}x = 4x + m + 1.$

b. ${m^2}(x – 1) = 2(mx – 2).$

<!-- chunk:14 level:4 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài tập 3. Xác định tham số để các phương trình sau có nghiệm duy nhất:

a. $\frac{{x – m}}{{x + 1}} = \frac{{x – 2}}{{x – 1}}.$

b. $a\left( {ax + 2{b^2}} \right) – {a^3} = {b^2}(x + a).$

<!-- chunk:15 level:4 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài tập 4. Xác định tham số để các phương trình sau có tập hợp nghiệm là $R:$

a. ${m^2}(mx – 1) = 2m(2x + 1).$

b. $a(x – 1) + b(2x + 1) = x + 2.$

<!-- chunk:16 level:4 source:https://toanmath.com/2020/04/phuong-trinh-bac-nhat.html -->
## Bài tập 5. Giải và biện luận các phương trình:

a. $mx + (m – 1)y = {m^2} – 1.$

b. $(m + 1)x + \left( {{m^2} – 1} \right)y = 2m.$