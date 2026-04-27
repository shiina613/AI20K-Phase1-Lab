# Hệ phương trình bậc nhất

<!-- chunk:0 level:0 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
Bài viết hướng dẫn phương pháp giải hệ phương trình bậc nhất, giúp học sinh học tốt chương trình Đại số 10.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN

Định nghĩa: Hệ phương trình bậc nhất với hai ẩn số $x$ và $y$ là hệ phương trình có dạng: 
$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y = {c_1}}\\
{{a_2}x + {b_2}y = {c_2}}
\end{array}} \right..
$$

Chúng ta đi xem xét hai bài toán cơ bản đối với hệ trên.

<!-- chunk:2 level:2 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài toán 1. Giải và biện luận hệ phương trình:
$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y = {c_1}}\\
{{a_2}x + {b_2}y = {c_2}}
\end{array}} \right..
$$

Phương pháp chung: Giải hệ phương trình $(I)$ bằng cách tính các định thức (cũng có thể sử dụng phép thế):

$$
D = \left| {\begin{array}{l}
{{a_1}}&{{b_1}}\\
{{a_2}}&{{b_2}}
\end{array}} \right|
$$
 $= {a_1}{b_2} – {a_2}{b_1}.$

$$
{D_x} = \left| {\begin{array}{l}
{{c_1}}&{{b_1}}\\
{{c_2}}&{{b_2}}
\end{array}} \right| = {c_1}{b_2} – {c_2}{b_1}.
$$

$$
{D_y} = \left| {\begin{array}{l}
{{a_1}}&{{c_1}}\\
{{a_2}}&{{c_2}}
\end{array}} \right| = {a_1}{c_2} – {a_2}{c_1}.
$$

a. Nếu $D \ne 0$ thì hệ có nghiệm duy nhất $x = \frac{{{D_x}}}{D}$ và $y = \frac{{{D_y}}}{D}.$

b. Nếu $D = 0$ thì:

+ Nếu 
$$
\left[ {\begin{array}{l}
{{D_x} \ne 0}\\
{{D_y} \ne 0}
\end{array}} \right.
$$
, hệ vô nghiệm.

+ Nếu ${D_x} = {D_y}$, hệ nghiệm đúng với mọi $x.$

Kết luận:

+ Với $D \ne 0$, hệ phương trình có nghiệm duy nhất $x = \frac{{{D_x}}}{D}$ và $y = \frac{{{D_y}}}{D}.$

+ Với $D = {D_x} = {D_y} = 0$, hệ phương trình có vô số nghiệm.

+ Với $D = 0$ và ${D_x} \ne 0$ hoặc ${D_y} \ne 0$, hệ phương trình vô nghiệm.

Chú ý. Để nhớ cách tính các định thức ta có minh hoạ sau:

$$
\begin{array}{l}
{a_1}\quad \mathop {\overline {{b_1}\quad {c_1}} }\limits^{{D_x}} \quad {a_1}\\
\mathop {\underline {{a_2}\quad {b_2}} }\limits_D \quad \mathop {\underline {{c_2}\quad {a_2}} }\limits_{{D_y}}
\end{array}
$$

Ví dụ minh họa:

<!-- chunk:3 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 1: Giải và biện luận hệ phương trình:
$$
\left\{ {\begin{array}{l}
{mx + y = m + 1}\\
{x + my = 2}
\end{array}} \right..
$$

Lời giải:

Ta có:

$$
D = \left| {\begin{array}{c}
m&1\\
1&m
\end{array}} \right| = {m^2} – 1.
$$

$$
{D_x} = \left| {\begin{array}{c}
{m + 1}&1\\
2&m
\end{array}} \right| = {m^2} + m – 2.
$$

$$
{D_y} = \left| {\begin{array}{c}
m&{m + 1}\\
1&2
\end{array}} \right| = m – 1.
$$

a. Nếu $D \ne 0$ $\Leftrightarrow {m^2} – 1 \ne 0$ $\Leftrightarrow m \ne \pm 1$ thì hệ có nghiệm duy nhất:

$x = \frac{{m + 2}}{{m + 1}}$ và $y = \frac{1}{{m + 1}}.$

b. Nếu $D = 0$ $\Leftrightarrow {m^2} – 1 = 0$ $\Leftrightarrow m = 1$ hoặc $m = – 1.$

+ Với $m = 1$, suy ra ${D_x} = {D_y} = 0$, hệ có vô số nghiệm thoả mãn $x + y = 2.$

+ Với $m = -1$, suy ra ${D_x} = – 2 \ne 0$, hệ vô nghiệm.

Kết luận:

+ Với $m \ne \pm 1$, hệ có nghiệm duy nhất $x = \frac{{m + 2}}{{m + 1}}$ và $y = \frac{1}{{m + 1}}.$

+ Với $m = 1$, hệ có vô số nghiệm thoả mãn $x + y = 2.$

+ Với $m = -1$, hệ vô nghiệm.

Chú ý. Với bài toán có nhiều hơn một tham số cần khéo léo vét cạn các trường hợp có thể xảy ra.

<!-- chunk:4 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 2. Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{ax + by = a + b}\\
{bx + ay = a – b}
\end{array}} \right..
$$

Lời giải:

Ta có:

$D = {a^2} – {b^2}.$

${D_x} = {a^2} + {b^2}.$

${D_y} = {a^2} – 2ab – {b^2}.$

a. Nếu $D \ne 0$ $\Leftrightarrow {a^2} – {b^2} \ne 0$ $\Leftrightarrow a \ne \pm b$ thì hệ có nghiệm duy nhất:

$x = \frac{{{a^2} + {b^2}}}{{{a^2} – {b^2}}}$ và $y = \frac{{{a^2} – 2ab – {b^2}}}{{{a^2} – {b^2}}}.$

b. Nếu $D = 0$ $\Leftrightarrow {a^2} – {b^2} = 0$ $\Leftrightarrow a = \pm b.$

Với $a = b$, suy ra:

$$
\left\{ {\begin{array}{l}
{{D_x} = 2{a^2}}\\
{{D_y} = – 2{a^2}}
\end{array}} \right..
$$

+ Khi $a = b = 0$ $\Rightarrow {D_x} = {D_y} = 0$, hệ có vô số nghiệm.

+ Khi $a = b \ne 0$ $\Rightarrow {D_x} \ne 0$, hệ vô nghiệm.

Với $a = – b$, suy ra ${D_x} = {D_y} = 2{a^2}.$

+ Khi $a = – b = 0$ $\Rightarrow {D_x} = {D_y} = 0$, hệ có vô số nghiệm.

+ Khi $a = – b \ne 0$ $\Rightarrow {D_x} \ne 0$, hệ vô nghiệm.

Kết luận:

+ Với $a \ne \pm b$, hệ có nghiệm duy nhất $x = \frac{{{a^2} + {b^2}}}{{{a^2} – {b^2}}}$ và $y = \frac{{{a^2} – 2ab – {b^2}}}{{{a^2} – {b^2}}}.$

+ Với $a = b = 0$, hệ có vô số nghiệm.

+ Với $a = \pm b \ne 0$, hệ vô nghiệm.

Chú ý. Với bài toán yêu cầu tìm hệ thức liên hệ giữa nghiệm $x$, $y$ không phụ thuộc vào tham số, khi đó từ hệ nghiệm $x$, $y$ hoặc từ hệ ban đầu ta khử tham số sẽ được hệ thức cần tìm.

<!-- chunk:5 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 3: Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{x – my = 0}\\
{mx – y = m + 1}
\end{array}} \right..
$$

a. Giải và biện luận hệ phương trình.

b. Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $m.$

Lời giải:

a. Ta có:

$D = {m^2} – 1$; ${D_x} = m(m + 1)$; ${D_y} = m + 1.$

Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow {m^2} – 1 \ne 0$ $\Leftrightarrow m \ne \pm 1$ hệ có nghiệm duy nhất:

$x = \frac{m}{{m – 1}}$ và $y = \frac{1}{{m – 1}}$ $(*).$

Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow {m^2} – 1 = 0$ $\Leftrightarrow m = \pm 1.$

+ Với $m = -1$, suy ra ${D_x} = {D_y} = 0$, hệ có vô số nghiệm thoả mãn $x + y = 0.$

+ Với $m = 1$, suy ra ${D_x} = 2 \ne 0$, hệ vô nghiệm.

Kết luận:

+ Với $m \ne \pm 1$, hệ có nghiệm duy nhất $x = \frac{m}{{m – 1}}$ và $y = \frac{1}{{m – 1}}.$

+ Với $m = -1$, hệ có vô số nghiệm thoả mãn $x + y = 0.$

+ Với $m = 1$, hệ vô nghiệm.

b. Từ các giá trị của nghiệm $(x;y)$ từ $(*)$ ta được:

$$
\left\{ {\begin{array}{l}
{x – my = 0}\\
{mx – y = m + 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{my = x}\\
{(x – 1)m = y + 1}
\end{array}} \right.
$$
 $\Rightarrow x(x – 1) = y(y + 1).$

Đó là hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $m.$

Chú ý. Trong nhiều trường hợp việc khử tham số cần áp dụng các hằng đẳng thức lượng giác, ví dụ như: ${\sin ^2}\alpha + {\cos ^2}\alpha = 1$, $\tan \alpha .\cot \alpha = 1$ ….

<!-- chunk:6 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 4: Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{x\sin 2\alpha + y(1 + \cos 2\alpha ) = \sin 2\alpha }\\
{x(1 + \cos 2\alpha ) – y\sin 2\alpha = 0}
\end{array}} \right..
$$

a. Giải và biện luận hệ phương trình.

b. Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $\alpha .$

Lời giải:

a. Ta có:

$D = – {\sin ^2}2\alpha – {(\cos 2\alpha – 1)^2}$ $= – 2(1 + \cos 2\alpha ).$

${D_x} = – {\sin ^2}2\alpha$; ${D_y} = – \sin 2\alpha (1 + \cos 2\alpha ).$

Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow – 2(1 + \cos 2\alpha ) \ne 0$ $\Leftrightarrow \cos 2\alpha \ne – 1$ $\Leftrightarrow \alpha \ne \frac{\pi }{2} + k\pi .$

Hệ có nghiệm duy nhất $x = \frac{1}{2}(1 – \cos 2\alpha )$ và $y = \frac{1}{2}\sin 2\alpha$ $(*).$

Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow – 2(1 + \cos 2\alpha ) = 0$ $\Leftrightarrow \cos 2\alpha = – 1$ $\Leftrightarrow \alpha = \frac{\pi }{2} + k\pi .$

+ Với $\alpha = \frac{\pi }{2} + k\pi$, suy ra ${D_x} = {D_y} = 0$, hệ có vô số nghiệm.

Kết luận:

+ Với $\alpha \ne \frac{\pi }{2} + k\pi$, hệ có nghiệm duy nhất $x = \frac{1}{2}(1 – \cos 2\alpha )$ và $y = \frac{1}{2}\sin 2\alpha .$

+ Với $\alpha = \frac{\pi }{2} + k\pi$, hệ có vô số nghiệm.

b. Thay các giá trị của nghiệm $(x;y)$ từ $(*)$ vào hệ ta được:

$$
\left\{ {\begin{array}{l}
{\cos 2\alpha = 1 – 2x}\\
{\sin 2\alpha = 2y}
\end{array}} \right.
$$
 $\Rightarrow {(1 – 2x)^2} + {(2y)^2} = 1$ $\Leftrightarrow {(1 – 2x)^2} + 4{y^2} = 1.$

Đó là hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $\alpha .$

<!-- chunk:7 level:2 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài toán 2. Hệ phương trình có nghiệm thoả mãn điều kiện cho trước.

Phương pháp chung: Xác định điều kiện cho ẩn số nếu có.

Biến đổi hệ về dạng:

$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y = {c_1}}\\
{{a_2}x + {b_2}y = {c_2}}
\end{array}} \right..
$$

Ta có các nhận xét sau:

(i). Với $D \ne 0$, hệ phương trình có nghiệm duy nhất $x = \frac{{{D_x}}}{D}$ và $y = \frac{{{D_y}}}{D}.$

(ii). Với $D = {D_x} = {D_y} = 0$, hệ phương trình có vô số nghiệm.

(iii). Với $D= 0$ và ${D_x} \ne 0$ hoặc ${D_y} \ne 0$, hệ phương trình vô nghiệm.

Trong trường hợp (i), (iii) phải so sánh giá trị của nghiệm số với điều kiện nếu có.

Ví dụ minh họa:

<!-- chunk:8 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 5: Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{mx + y = 2m}\\
{x + my = m + 1}
\end{array}} \right..
$$

a. Tìm $m$ để hệ có nghiệm duy nhất.

b. Tìm $m$ nguyên để nghiệm duy nhất của hệ là nghiệm nguyên.

Lời giải:

Ta có:

$D = {m^2} – 1$; ${D_x} = 2{m^2} – m – 1$; ${D_y} = {m^2} – m.$

a. Hệ có nghiệm duy nhất:

$\Leftrightarrow D \ne 0$ $\Leftrightarrow {m^2} – 1 \ne 0$ $\Leftrightarrow m \ne \pm 1$ $(*).$

Khi đó nghiệm duy nhất của hệ là:

$$
\left\{ {\begin{array}{l}
{x = \frac{{{D_x}}}{D} = \frac{{2m + 1}}{{m + 1}} = 2 – \frac{1}{{m + 1}}}\\
{y = \frac{{{D_y}}}{D} = \frac{m}{{m + 1}} = 1 – \frac{1}{{m + 1}}}
\end{array}} \right..
$$

b. Để nghiệm duy nhất của hệ là nghiệm nguyên với $m$ nguyên:

$\Leftrightarrow m$, $\frac{1}{{m + 1}} \in Z$ $\Leftrightarrow m + 1$ là ước của $1$ $\Leftrightarrow m + 1 = \pm 1$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{m = – 2}
\end{array}} \right..
$$

So sánh với điều kiện $(*)$ ta nhận được $m = 0 \vee m = – 2.$

<!-- chunk:9 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 6: Tìm $m$ để hệ phương trình có vô số nghiệm:

$$
\left\{ {\begin{array}{l}
{4x – my = – m – 1}\\
{(m + 6)x + 2y = m + 3}
\end{array}} \right..
$$

Lời giải:

Ta có:

$D = {m^2} + 6m + 8$; ${D_x} = {m^2} + m – 2$; ${D_y} = {m^2} + 11m + 18.$

Vậy hệ có vô số nghiệm:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{D = 0}\\
{{D_x} = 0}\\
{{D_y} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + 6m + 8 = 0}\\
{{m^2} + m – 2 = 0\quad }\\
{{m^2} + 11m + 18 = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = – 2.$

Vậy với $m = -2$ hệ có vô số nghiệm.

<!-- chunk:10 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 7: Tìm $m$ để hệ phương trình vô nghiệm:

$$
\left\{ {\begin{array}{l}
{mx – my = m + 1}\\
{\left( {{m^2} – m} \right)x + my = 2}
\end{array}} \right..
$$

Lời giải:

Ta có $D = {m^3}.$

Vậy hệ vô nghiệm.

$\Rightarrow D = 0$ $\Rightarrow m = 0.$

Với $m = 0$, hệ có dạng:

$$
\left\{ {\begin{array}{l}
{0.x – 0.y = 1}\\
{0.x + 0.y = 2}
\end{array}} \right.
$$
 nên hệ vô nghiệm.

Vậy với $m = 0$ hệ vô nghiệm.

Chú ý. Với bài toán tìm điều kiện để hệ có nghiệm thông thường ta đi giải bài toán ngược “Tìm tham số để hệ phương trình vô nghiệm“, giả sử khi đó $m \in K.$ Vậy với $m \in R\backslash K$ hệ có nghiệm.

<!-- chunk:11 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 8: Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{x + my = 3m}\\
{mx + y = 2m + 1}
\end{array}} \right.
$$
 $(I).$

a. Tìm $m$ để hệ phương trình có nghiệm.

b. Tìm $m$ để hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{\sin x + m\cos x = 3m}\\
{m\sin x + \cos x = 2m + 1}
\end{array}} \right.
$$
 $(II).$

Lời giải:

a. Xét hệ phương trình $(I)$, ta có $D = 1 – {m^2}.$

Hệ vô nghiệm $\Rightarrow D = 0$ $\Rightarrow 1 – {m^2} = 0$ $\Rightarrow m = \pm 1.$

+ Với $m = 1$, hệ $(I)$ có dạng:

$$
\left\{ {\begin{array}{l}
{x + y = 3}\\
{x + y = 3}
\end{array}} \right.
$$
 $\Leftrightarrow x + y = 3$ nên hệ có vô số nghiệm.

+ Với $m = -1$, hệ $(I)$ có dạng:

$$
\left\{ {\begin{array}{l}
{x – y = – 3}\\
{x – y = 1}
\end{array}} \right.
$$
 vô nghiệm.

Vậy với $m = -1$ hệ vô nghiệm, do đó hệ có nghiệm với $m \ne – 1.$

b. Bằng cách đặt:

$$
\left\{ {\begin{array}{l}
{X = \sin x}\\
{Y = \cos x}
\end{array}} \right.
$$
, điều kiện ${X^2} + {Y^2} = 1$ $(*).$

Ta đưa hệ $(II)$ về dạng:

$$
\left\{ {\begin{array}{l}
{X + mY = 3m}\\
{mX + Y = 2m + 1}
\end{array}} \right.
$$
 $(III).$

Xét hệ phương trình $(III)$, ta có:

$D = 1 – {m^2}$; ${D_x} = – 2{m^2} + 2m$; ${D_y} = – 3{m^2} + 2m + 1.$

(i). Nếu $D = 0$ $\Leftrightarrow 1 – {m^2} = 0$ $\Leftrightarrow m = \pm 1.$

+ Với $m = 1$, hệ $(III)$ có dạng:

$$
\left\{ {\begin{array}{l}
{X + Y = 3}\\
{X + Y = 3}
\end{array}} \right.
$$
 không thoả mãn $(*)$, nên hệ vô nghiệm.

+ Với $m = -1$, hệ $(III)$ có dạng:

$$
\left\{ {\begin{array}{l}
{X – Y = – 3}\\
{X – Y = 1}
\end{array}} \right.
$$
 nên hệ vô nghiệm.

(ii). Nếu $D \ne 0$ $\Leftrightarrow 1 – {m^2} \ne 1$ $\Leftrightarrow m \ne \pm 1$ $(**).$

Hệ $(III)$ có nghiệm duy nhất $X = \frac{{2m}}{{m + 1}}$ và $Y = \frac{{3m + 1}}{{m + 1}}.$

Nghiệm trên thoả mãn $(*)$ khi:

${\left( {\frac{{2m}}{{m + 1}}} \right)^2} + {\left( {\frac{{3m + 1}}{{m + 1}}} \right)^2} = 1$ $\Leftrightarrow 12{m^2} + 4m = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{m = – \frac{1}{3}}
\end{array}} \right..
$$

Nghiệm trên thoả mãn $(**).$

Vậy hệ có nghiệm khi $m = 0$ hoặc $m = – \frac{1}{3}.$

<!-- chunk:12 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 9: Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{bx – y = a{c^2}}\\
{(b – 6)x + 2by = c + 1}
\end{array}} \right..
$$

a. Tìm $a$ sao cho với mọi $b$ luôn tồn tại $c$ để hệ có nghiệm.

b. Tìm $a$ sao cho tồn tại $c$ để hệ có nghiệm với mọi $b.$

Lời giải:

Ta có $D = 2{b^2} + b – 6.$

Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow 2{b^2} + b – 6 \ne 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{b \ne 3/2}\\
{b \ne – 2}
\end{array}} \right..
$$

Hệ có nghiệm duy nhất với $\forall a$, $\forall c$ nên không cần đặt điều kiện cho $a.$

Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow 2{b^2} + b – 6 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{b = 3/2}\\
{b = – 2}
\end{array}} \right..
$$

+ Với $b = \frac{3}{2}$, hệ có dạng:

$$
\left\{ {\begin{array}{l}
{3x – 2y = 2a{c^2}}\\
{3x – 2y = – \frac{2}{3}(c + 1)}
\end{array}} \right..
$$

Hệ có nghiệm $\Leftrightarrow 2a{c^2} = – \frac{2}{3}(c + 1)$ $\Leftrightarrow 3a{c^2} + c + 1 = 0$ $(1).$

Do đó $c$ tồn tại $\Leftrightarrow$ phương trình $(1)$ có nghiệm theo $c.$

$\Leftrightarrow {\Delta _c} \ge 0$ $\Leftrightarrow 1 – 12a \ge 0$ $\Leftrightarrow a \le \frac{1}{{12}}.$

+ Với $b = – 2$, hệ có dạng:

$$
\left\{ {\begin{array}{l}
{2x – y = a{c^2}}\\
{2x – y = – \frac{1}{4}(c + 1)}
\end{array}} \right..
$$

Hệ có nghiệm $\Leftrightarrow a{c^2} = – \frac{1}{4}(c + 1)$ $\Leftrightarrow 4a{c^2} + c + 1 = 0$ $(2).$

Do đó $c$ tồn tại $\Leftrightarrow$ phương trình $(2)$ có nghiệm theo $c.$

$\Leftrightarrow {\Delta _c} \ge 0$ $\Leftrightarrow 1 – 16a \ge 0$ $\Leftrightarrow a \le \frac{1}{{16}}.$

a. Với $\forall b$ luôn tồn tại $c$ để hệ có nghiệm:

$\Leftrightarrow (1)$, $(2)$ phải đồng thời có nghiệm 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \le 1/12}\\
{a \le 1/16}
\end{array}} \right.
$$
 $\Leftrightarrow a \le \frac{1}{{16}}.$

b. Tồn tại $c$ để hệ có nghiệm với mọi $b:$

$\Leftrightarrow (1)$, $(2)$ phải có nghiệm chung $\Leftrightarrow$ hệ sau có nghiệm ẩn $c.$

$$
\left\{ {\begin{array}{l}
{3a{c^2} + c + 1 = 0}\\
{4a{c^2} + c + 1 = 0}
\end{array}} \right.
$$
 $\Rightarrow a = 0.$

Chú ý: Nếu bài toán cho hệ ba phương trình với hai ẩn, thì xét hệ gồm hai phương trình và yêu cầu nghiệm thoả mãn phương trình còn lại.

<!-- chunk:13 level:3 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Ví dụ 10: Tìm $m$ để hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{mx + y = 1}&{(1)}\\
{x + my = 1}&{(2)}\\
{x + y = m}&{(3)}
\end{array}} \right..
$$

Lời giải:

Xét hệ phương trình tạo bởi $(2)$ và $(3):$

$$
\left\{ {\begin{array}{l}
{x + my = 1}\\
{x + y = m}
\end{array}} \right..
$$

Ta có: $D = 1 – m$; ${D_x} = 1 – {m^2}$; ${D_y} = m – 1.$

Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow 1 – m \ne 0$ $\Leftrightarrow m \ne 1.$

Hệ có nghiệm duy nhất $x = 1 + m$ và $y = -1.$

Nghiệm trên thoả mãn $(1):$

$\Leftrightarrow m(1 + m) – 1 = 1$ $\Leftrightarrow {m^2} + m – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 1\,\,\,{\rm{(loại)}}}\\
{m = – 2}
\end{array}} \right..
$$

Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow 1 – m = 0$ $\Leftrightarrow m = 1.$

+ Với $m = 1$, suy ra hệ ban đầu có dạng: $x + y = 1$, có vô số nghiệm.

Vậy với $m = 1$ hoặc $m = -2$ hệ có nghiệm.

Chú ý. Nếu coi các phương trình $(1)$, $(2)$, $(3)$ theo thứ tự là phương trình của ba đường thẳng $\left( {{d_1}} \right)$, $\left( {{d_2}} \right)$, $\left( {{d_3}} \right)$ thì bài toán có thể phát biểu dưới dạng: “Tìm điều kiện của tham số để ba đường thẳng đồng quy“.

<!-- chunk:14 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 1. Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{(a + b)x + (a – b)y = a}\\
{(2a – b)x + (2a + b)y = b}
\end{array}} \right..
$$

<!-- chunk:15 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 2. Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{6mx – (m – 2)y = 3}\\
{(m – 1)x – my = 2}
\end{array}} \right..
$$

Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $m.$

<!-- chunk:16 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 3. Tìm $m$ nguyên để hệ phương trình sau có nghiệm nguyên:

$$
\left\{ {\begin{array}{l}
{2mx + 3y = m}\\
{x + y = m + 1}
\end{array}} \right..
$$

<!-- chunk:17 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 4. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{(2a – 1)x – y = 1}\\
{x + (a + 1)y = – 1}
\end{array}} \right..
$$

a. Xét nghiệm của hệ đó với $a = 0$; $a = \frac{1}{2}.$

b. Giải và biện luận hệ phương trình.

<!-- chunk:18 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 5. Giải và biện luận các hệ phương trình:

a. 
$$
\left\{ {\begin{array}{l}
{x – my = 0}\\
{mx – y = m + 1}
\end{array}} \right..
$$

b. 
$$
\left\{ {\begin{array}{l}
{(a – 1)x + y = a – 2}\\
{x + (a – 1)y = a}
\end{array}} \right..
$$

c. 
$$
\left\{ {\begin{array}{l}
{ax + by = {a^2} + {b^2}}\\
{bx + ay = 2ab}
\end{array}} \right..
$$

d. 
$$
\left\{ {\begin{array}{l}
{\left( {{a^3} – 1} \right)x + \left( {{a^2} – 1} \right)y = a – 1}\\
{\left( {{a^3} + 1} \right)x + \left( {{a^2} + 1} \right)y = a + 1}
\end{array}} \right..
$$

e. 
$$
\left\{ {\begin{array}{l}
{x\sin (a + b) + y\sin b = \sin a}\\
{x\cos (a + b) + y\cos b = \cos a}
\end{array}} \right..
$$

<!-- chunk:19 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 6. Tìm $m$ để hệ phương trình sau có nghiệm nguyên:

$$
\left\{ {\begin{array}{l}
{2mx + 3y = m}\\
{x + y = m + 1}
\end{array}} \right..
$$

<!-- chunk:20 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 7. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{mx + y = 2m}\\
{x + my = m + 1}
\end{array}} \right..
$$

a. Giải và biện luận hệ phương trình theo $m.$

b. Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ không phụ thuộc vào $m.$

<!-- chunk:21 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 8. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{(m – 2)x + 2my = m}\\
{(2m – 1)x – y = 2m + 5}
\end{array}} \right..
$$

a. Giải và biện luận hệ phương trình theo $m.$

b. Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ không phụ thuộc vào $m.$

c. Khi hệ có nghiệm duy nhất, tìm $m \in Z$ để hệ có nghiệm nguyên.

<!-- chunk:22 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 9. Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{x\sin \alpha + y\cos \alpha = \sin \alpha }\\
{x\cos \alpha + y\sin \alpha = \cos \alpha }
\end{array}} \right..
$$

Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $\alpha .$

<!-- chunk:23 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 10. Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{x(1 + \cos 2\alpha ) + y\sin 2\alpha = \sin 2\alpha }\\
{x(1 + \cos 2\alpha ) – y\sin 2\alpha = \cos 2\alpha }
\end{array}} \right..
$$

Tìm hệ thức liên hệ giữa nghiệm $x$, $y$ của hệ không phụ thuộc vào $\alpha .$

<!-- chunk:24 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 11. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{2x + by = a{c^2} + c}\\
{bx + 2y = c – 1}
\end{array}} \right..
$$

a. Tìm $a$ sao cho với mọi $b$ luôn tồn tại $c$ để hệ có nghiệm.

b. Tìm $a$ sao cho tồn tại $c$ để hệ có nghiệm với mọi $b.$

<!-- chunk:25 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 12. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{bx + y = a{c^2}}\\
{x + by = ac + 1}
\end{array}} \right..
$$

a. Tìm $a$ sao cho với mọi $b$ luôn tồn tại $c$ để hệ có nghiệm.

b. Tìm $a$ sao cho tồn tại $c$ để hệ có nghiệm với mọi $b.$

<!-- chunk:26 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 13. Tìm $a$, $b$ để hệ phương trình sau có nghiệm với mọi $c:$

$$
\left\{ {\begin{array}{l}
{(c + 3)x + 4y = 5a + 3b + c}\\
{x + cy = ac – 2b + 2c – 1}
\end{array}} \right..
$$

<!-- chunk:27 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 14. Tìm $m$ để hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{mx + y = m}\\
{x + my = 1}\\
{x – y = m}
\end{array}} \right..
$$

<!-- chunk:28 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 15. Cho hệ phương trình:

$$
\left\{ {\begin{array}{l}
{ax + y = b}\\
{x + ay = {c^2} + c}
\end{array}} \right..
$$

a. Với $b = 0$, hãy giải biện luận hệ theo $a$ và $c.$

b. Tìm $b$ để với mọi $a$, ta luôn tìm được $c$ sao cho hệ có nghiệm.

<!-- chunk:29 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 16. Giả sử hệ phương trình sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{ax + by = c}\\
{bx + cy = a}\\
{cx + ay = b}
\end{array}} \right..
$$

Chứng minh rằng ${a^3} + {b^3} + {c^3} = 3abc.$

<!-- chunk:30 level:4 source:https://toanmath.com/2020/04/he-phuong-trinh-bac-nhat.html -->
## Bài tập 17. Tìm $m$, $n$, $p$ để cả ba hệ sau đồng thời vô nghiệm:
$$
\left\{ {\begin{array}{l}
{x – py = n}\\
{ – px + y = m}
\end{array}} \right.
$$
; 
$$
\left\{ {\begin{array}{l}
{ – px + y = m}\\
{nx + my = 1}
\end{array}} \right.
$$
; 
$$
\left\{ {\begin{array}{l}
{nx + my = 1}\\
{x – py = n}
\end{array}} \right..
$$