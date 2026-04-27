# Một số bài toán đưa về hệ phương trình bậc nhất

<!-- chunk:0 level:0 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
Bài viết hướng dẫn phương pháp giải một số bài toán đưa về hệ phương trình bậc nhất, giúp học sinh học tốt chương trình Đại số 10.

<!-- chunk:1 level:2 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài toán 1. Ứng dụng hệ phương trình bậc nhất hai ẩn để xét hai phương trình bậc hai có nghiệm chung.

Phương pháp chung: Thực hiện theo các bước sau:

+ Bước 1. Xét hệ phương trình tạo bởi hai phương trình bậc hai:

$$
\left\{ {\begin{array}{l}
{{a_1}{x^2} + {b_1}x + {c_1} = 0}\\
{{a_2}{x^2} + {b_2}x + {c_2} = 0}
\end{array}} \right.
$$
 $(I).$

+ Bước 2. Đặt ${x^2} = y$, ta được hệ:

$$
(I) \Leftrightarrow \left\{ {\begin{array}{l}
{{b_1}x + {a_1}y = {c_1}}\\
{{b_2}x + {a_2}y = {c_2}}
\end{array}} \right.
$$
 $(II).$

+ Bước 3. Để hai phương trình có nghiệm chung trước hết $(II)$ phải có nghiệm thoả mãn ${x^2} = y$, ta có điều kiện là:

$$
\left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{D \ne 0}\\
{{{\left( {\frac{{{D_x}}}{D}} \right)}^2} = \frac{{{D_y}}}{D}}
\end{array}} \right.}\\
{D = {D_x} = {D_y} = 0}
\end{array}} \right..
$$

Bước 4. Thử lại.

Ví dụ minh họa:

<!-- chunk:2 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 1: Với giá trị nào của $m$ thì hai phương trình sau có nghiệm chung: $2{x^2} + mx – 1 = 0$ và $m{x^2} – x + 2 = 0.$

Lời giải:

Các phương trình đã cho có nghiệm chung $\Leftrightarrow$ khi hệ sau có nghiệm:

$$
\left\{ {\begin{array}{l}
{2{x^2} + mx – 1 = 0}\\
{m{x^2} – x + 2 = 0}
\end{array}} \right..
$$

Đặt ${x^2} = y$, ta được hệ:

$$
\left\{ {\begin{array}{l}
{mx + 2y = 1}\\
{x – my = 2}
\end{array}} \right..
$$

Ta có $D = – {m^2} – 2$; ${D_x} = – m – 4$; ${D_y} = 2m – 1.$

Vì $D \ne 0$, $\forall m$, hệ có nghiệm duy nhất $x = \frac{{m + 4}}{{{m^2} + 2}}$ và $y = \frac{{1 – 2m}}{{{m^2} + 2}}.$

Do ${x^2} = y$ nên ta phải có:

${\left( {\frac{{m + 4}}{{{m^2} + 2}}} \right)^2} = \frac{{1 – 2m}}{{{m^2} + 2}}$ $\Leftrightarrow {m^3} + 6m + 7 = 0$ $\Leftrightarrow m = – 1.$

Vậy với $m = -1$ hai phương trình có nghiệm chung là $x = 1.$

**Bài toán 2**. Ứng dụng hệ phương trình bậc nhất hai ẩn để giải các hệ phương trình bậc cao, trị tuyệt đối, vô tỉ và hệ siêu việt.

**Phương pháp chung**: Thực hiện theo các bước sau:

+ Bước 1. Bằng phép đặt ẩn phụ ta có thể chuyển các hệ phương trình bậc cao, trị tuyệt đối, vô tỉ, hệ siêu việt và lượng giác về hệ phương trình bậc nhất hai ẩn (cần lưu ý tới điều kiện cho các ẩn phụ).

+ Bước 2. Giải và biện luận hệ nhận được.

Ví dụ minh họa:

<!-- chunk:3 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 2:

a. Giải hệ phương trình:

$$
\left\{ {\begin{array}{l}
{5u – 9v = 50}\\
{3u + 7v = 154}
\end{array}} \right.
$$
 $(I).$

b. Từ đó suy ra nghiệm của hệ phương trình:

$$
\left\{ {\begin{array}{l}
{\frac{5}{{x + 3}} – \frac{9}{{y – 2}} = 100}\\
{\frac{3}{{x + 3}} + \frac{7}{{y – 2}} = 308}
\end{array}} \right.
$$
 $(II).$

Lời giải:

a. Ta có $D = 62$; ${D_u} = 1736$; ${D_v} = 620$ do đó hệ có nghiệm duy nhất $u = 28$ và $v = 10.$

b. Đặt:

$$
\left\{ {\begin{array}{l}
{\frac{5}{{x + 3}} = 2u}\\
{\frac{9}{{y – 2}} = 2v}
\end{array}} \right..
$$

Khi đó hệ $(II)$ có dạng:

$$
\left\{ {\begin{array}{l}
{5u – 9v = 50}\\
{3u + 7v = 154}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{u = 28}\\
{v = 10}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{5}{{x + 3}} = 56}\\
{\frac{9}{{y – 2}} = 20}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – \frac{{163}}{{56}}}\\
{y = \frac{{49}}{{20}}}
\end{array}} \right..
$$

Vậy hệ có nghiệm $x = – \frac{{163}}{{56}}$ và $y = \frac{{49}}{{20}}.$

Chú ý. Trong nhiều trường hợp cần xác định điều kiện cho các ẩn phụ.

<!-- chunk:4 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 3: Giải và biện luận hệ phương trình:

$$
\left\{ {\begin{array}{l}
{m\sqrt {x + 1} + \sqrt y = m + 1}\\
{\sqrt {x + 1} + m\sqrt y = 2}
\end{array}} \right..
$$

Lời giải:

Đặt: 
$$
\left\{ {\begin{array}{l}
{\sqrt {x + 1} = u}\\
{\sqrt y = v}
\end{array}} \right.
$$
, $u,v \ge 0.$

Khi đó hệ $(II)$ có dạng:

$$
\left\{ {\begin{array}{l}
{mu + v = m + 1}\\
{ux + mv = 2}
\end{array}} \right..
$$

Ta có: $D = {m^2} – 1$; ${D_u} = {m^2} + m – 2$; ${D_v} = m – 1.$

Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow {m^2} – 1 \ne 0$ $\Leftrightarrow m \ne \pm 1.$

Hệ có nghiệm duy nhất $u = \frac{{m + 2}}{{m + 1}}$ và $v = \frac{1}{{m + 1}}.$

Vì điều kiện $u,v \ge 0$ nên ta phải có:

$$
\left\{ {\begin{array}{l}
{\frac{{m + 2}}{{m + 1}} \ge 0}\\
{\frac{1}{{m + 1}} \ge 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > – 1.$

Khi đó ta được:

$$
\left\{ {\begin{array}{l}
{\sqrt {x + 1} = \frac{{m + 2}}{{m + 1}}}\\
{\sqrt y = \frac{1}{{m + 1}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{{2m + 3}}{{{{(m + 1)}^2}}}}\\
{y = \frac{1}{{{{(m + 1)}^2}}}}
\end{array}} \right..
$$

Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow {m^2} – 1 = 0$ $\Leftrightarrow m = \pm 1.$

+ Với $m = 1$, suy ra ${D_u} = {D_v} = 0$, hệ có vô số nghiệm thoả $\sqrt {x + 1} + \sqrt y = 2.$

+ Với $m = -1$, suy ra ${D_u} = – 2 \ne 0$, hệ vô nghiệm.

Kết luận:

+ Với $m > -1$, hệ phương trình có nghiệm duy nhất: $x = \frac{{2m + 3}}{{{{(m + 1)}^2}}}$ và $y = \frac{1}{{{{(m + 1)}^2}}}.$

+ Với $m = 1$, hệ phương trình có vô số nghiệm thoả mãn $\sqrt {x + 1} + \sqrt y = 2.$

+ Với $m = -1$, hệ phương trình vô nghiệm.

<!-- chunk:5 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 4: Giải hệ phương trình:

$$
\left\{ {\begin{array}{l}
{{2^x}{{.3}^y} = 12}\\
{{3^x}{{.2}^y} = 18}
\end{array}} \right..
$$

Lời giải:

Lấy logarit cơ số $2$ cả hai vế của hai phương trình, ta được:

$$
\left\{ {\begin{array}{l}
{{{\log }_2}\left( {{2^x}{{.3}^y}} \right) = {{\log }_2}12}\\
{{{\log }_2}\left( {{3^x}{{.2}^y}} \right) = {{\log }_2}18}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x + y{{\log }_2}3 = 2 + {{\log }_2}3}\\
{x{{\log }_2}3 + y = 1 + 2{{\log }_2}3}
\end{array}} \right..
$$

Ta có:

$D = 1 – \log _2^23 \ne 0$, hệ luôn có nghiệm duy nhất.

${D_x} = 2 – 2\log _2^23$; ${D_y} = 1 – \log _2^23.$

Suy ra hệ có nghiệm $x = 2$ và $y = 1.$

<!-- chunk:6 level:2 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài toán 3. (Ứng dụng hệ phương trình bậc nhất hai ẩn để xác định vị trí tương đối của hai đường thẳng trong mặt phẳng): Cho hai đường thẳng $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có phương trình tổng quát: $\left( {{d_1}} \right):{A_1}x + {B_1}y + {C_1} = 0$; $\left( {{d_2}} \right):{A_2}x + {B_2}y + {C_2} = 0.$ Tuỳ theo giá trị của tham số, hãy xác định vị trí tương đối của $\left( {{d_1}} \right)$, $\left( {{d_2}} \right).$

Phương pháp chung:

Thực hiện theo các bước sau:

Bước 1. Thiết lập hệ phương trình tạo bởi $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ là:

$$
\left\{ {\begin{array}{l}
{{A_1}x + {B_1}y + {C_1} = 0}\\
{{A_2}x + {B_2}y + {C_2} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{A_1}x + {B_1}y = – {C_1}}\\
{{A_2}x + {B_2}y = – {C_2}}
\end{array}} \right.
$$
 $(I).$

Bước 2: Bằng việc biện luận $(I)$ ta có được vị trí tương đối của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$, cụ thể:

+ Nếu $(I)$ vô nghiệm $\Leftrightarrow \left( {{d_1}} \right)//\left( {{d_2}} \right).$

+ Nếu $(I)$ có nghiệm duy nhất $\Leftrightarrow \left( {{d_1}} \right) \cap \left( {{d_2}} \right)$ $= \left\{ {M\left( {\frac{{{D_x}}}{D};\frac{{{D_y}}}{D}} \right)} \right\}.$

+ Nếu $(I)$ có vô số nghiệm $\Leftrightarrow \left( {{d_1}} \right) \equiv \left( {{d_2}} \right).$

Ví dụ minh họa:

<!-- chunk:7 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 5: Cho ${a^2} + {b^2} > 0$ và hai đường thẳng $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có phương trình:

$(a – b)x + y = 1$ và $\left( {{a^2} – {b^2}} \right)x + ay = b.$

a. Xác định giao điểm của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right).$

b. Tìm điều kiện với $a$, $b$ để giao điểm đó thuộc trục hoành.

Lời giải:

a. Xét hệ phương trình tạo bởi $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có dạng:

$$
\left\{ \begin{array}{l}
(a – b)x + y = 1\\
\left( {{a^2} – {b^2}} \right)x + ay = b
\end{array} \right..
$$

Ta có $D = {b^2} – ab$; ${D_x} = a – b$; ${D_y} = ab – {a^2}.$

Vậy suy ra:

$\left( {{d_1}} \right) \cap \left( {{d_2}} \right) = \left\{ I \right\}$ $\Leftrightarrow D \ne 0$ $\Leftrightarrow {b^2} – ab \ne 0.$

Khi đó giao điểm $I$ có toạ độ: $I\left( { – \frac{1}{b};\frac{a}{b}} \right).$

b. Điểm $I \in Ox$:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{b^2} – ab \ne 0}\\
{\frac{a}{b} = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 0}\\
{b \ne 0}
\end{array}} \right..
$$

<!-- chunk:8 level:2 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài toán 4. (Ứng dụng hệ phương trình bậc nhất hai ẩn để biện luận giá trị nhỏ nhất của biểu thức hai ẩn): Hãy biện luận giá trị nhỏ nhất của: $F = {\left( {{a_1}x + {b_1}y + {c_1}} \right)^2} + {\left( {{a_2}x + {b_2}y + {c_2}} \right)^2}$ theo tham số (giả sử là $m$).

Phương pháp chung: Thực hiện theo các bước sau:

Bước 1. Xét hai đường thẳng:

$\left( {{d_1}} \right):{a_1}x + {b_1}y + {c_1} = 0$ và $\left( {{d_2}} \right):{a_2}x + {b_2}y + {c_2} = 0.$

Vậy giá trị nhỏ nhất của $F$ tuỳ thuộc vào vị trí tương đối của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right).$

Bước 2: Xét hệ phương trình tạo bởi $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có dạng:

$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y = – {c_1}}\\
{{a_2}x + {b_2}y = – {c_2}}
\end{array}} \right..
$$

Xác định các giá trị $D$; ${D_x}$; ${D_y}.$

Bước 3: Xét hai trường hợp:

+ Trường hợp 1: Nếu $D \ne 0.$

$\Leftrightarrow$ Hệ có nghiệm duy nhất $x = \frac{{{D_x}}}{D}$ và $y = \frac{{{D_y}}}{D}.$

Khi đó $\left( {{d_1}} \right)$ cắt $\left( {{d_2}} \right)$ do đó $\min F = 0.$

+ Trường hợp 2: Nếu $D = 0$ thì đặt $t = {a_1}x + {b_1}y + {c_1}$, ta được:

$F = 2{t^2} + At + B \ge – \frac{\Delta }{4}.$

Vậy $\min F = – \frac{\Delta }{4}$, đạt được khi $t = – \frac{A}{4}$ $\Rightarrow {a_1}x + {b_1}y + {c_1} = – \frac{A}{4}.$

Bước 4. Kết luận:

+ Với $D \ne 0$ thì $\min F = 0$, đạt được khi $x = \frac{{{D_x}}}{D}$ và $y = \frac{{{D_y}}}{D}.$

+ Với $D = 0$ thì $\min F = – \frac{\Delta }{4}$, đạt được khi $x$, $y$ thuộc đường thẳng có phương trình ${a_1}x + {b_1}y + {c_1} = – \frac{A}{4}.$

Ví dụ minh họa:

<!-- chunk:9 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 6: Hãy biện luận giá trị nhỏ nhất của biểu thức sau theo $a:$

$F = {(x + y – 2)^2} + {(x + ay – 3)^2}.$

Lời giải:

Xét hai đường thẳng:

$\left( {{d_1}} \right):x – y + 2 = 0$ và $\left( {{d_2}} \right):x – ay + 3 = 0.$

Vậy giá trị nhỏ nhất của $F$ tuỳ thuộc vào vị trí tương đối của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right).$

Xét hệ phương trình tạo bởi $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có dạng:

$$
\left\{ {\begin{array}{l}
{x + y = 2}\\
{x + ay = 3}
\end{array}} \right..
$$

Ta có $D = a – 1$; ${D_x} = 2a – 3$; ${D_y} = 1.$

+ Trường hợp 1: Nếu $D \ne 0$ $\Leftrightarrow a – 1 \ne 0$ $\Leftrightarrow a \ne 1.$

Hệ có nghiệm duy nhất $x = \frac{{2a – 3}}{{a – 1}}$ và $y = \frac{1}{{a – 1}}.$

Khi đó $\left( {{d_1}} \right)$ cắt $\left( {{d_2}} \right)$ do đó $\min F = 0.$

+ Trường hợp 2: Nếu $D = 0$ $\Leftrightarrow a – 1 = 0$ $\Leftrightarrow a = 1.$

Với $a = 1$, suy ra ${D_x} = – 1 \ne 0$, hệ vô nghiệm.

Khi đó $\left( {{d_1}} \right)$ song song $\left( {{d_2}} \right)$ và ta được:

$F = {(x + y – 2)^2} + {(x + y – 3)^2}.$

Đặt $t = x + y – 2$ ta được:

$F = {t^2} + {(t – 1)^2}$ $= 2{t^2} – 2t + 1 \ge \frac{3}{4}.$

Vậy $\min F = \frac{3}{4}$, đạt được khi $t = \frac{1}{2}$ $\Leftrightarrow x + y – 2 = \frac{1}{2}$ $\Leftrightarrow 2x + 2y – 5 = 0.$

Kết luận:

+ Với $a \ne 1$ thì $\min F = 0$, đạt được khi $x = \frac{{2a – 3}}{{a – 1}}$ và $y = \frac{1}{{a – 1}}.$

+ Với $a = 1$ thì $\min F = \frac{3}{4}$, đạt được khi $x$, $y$ thuộc đường thẳng có phương trình $2x + 2y – 5 = 0.$

<!-- chunk:10 level:3 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Ví dụ 7: Hãy xác định tất cả các giá trị của $a$, $b$ sao cho nghiệm của bất phương trình: $|x – a + 1| \le 2b + 3$ là đoạn $[ – 2;5].$

Lời giải:

1. Nếu $2b + 3 < 0$ $\Leftrightarrow b < – \frac{3}{2}$ thì bất phương trình vô nghiệm.

2. Nếu $2b + 3 \ge 0$ $\Leftrightarrow b \ge – \frac{3}{2}$ thì bất phương trình được viết lại dưới dạng:

$– 2b – 3 \le x – a + 1 \le 2b + 3$ $\Leftrightarrow a – 2b – 4 \le x \le a + 2b + 2.$

Vậy để nghiệm của bất phương trình là đoạn $[ – 2;5]$ điều kiện cần và đủ là:

$$
\left\{ {\begin{array}{l}
{a – 2b – 4 = – 2}\\
{a + 2b + 2 = 5}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a – 2b = 2}\\
{a + 2b = 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = \frac{5}{2}}\\
{b = \frac{1}{4}}
\end{array}} \right..
$$

Vậy với $a = \frac{5}{2}$ và $b = \frac{1}{4}$ thoả mãn điều kiện đầu bài.

<!-- chunk:11 level:4 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài tập 1. Với giá trị nào của $m$ thì các cặp phương trình sau có nghiệm chung:

a. ${x^2} + ax + ac = 0$ và ${x^2} – ax + {c^2} = 0.$

b. ${x^2} + 5x + m = 0$ và ${x^2} + 2mx + {m^2} – 4m + 25 = 0.$

c. $2{x^2} + (3m + 1)x – 9 = 0$ và $6{x^2} + (7m – 1)x – 19 = 0.$

d. $a{x^2} + x + 1 = 0$ và ${x^2} + ax + 1 = 0.$

<!-- chunk:12 level:4 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài tập 2. Cho ${a^2} + {b^2} > 0$ và hai đường thẳng $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có phương trình:

$\left( {{d_1}} \right):ax + by = a + b$; $\left( {{d_2}} \right):bx + ay = a – b.$

a. Xác định giao điểm của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right).$

b. Tìm quỹ tích toạ độ giao điểm khi $a$, $b$ thay đổi.

<!-- chunk:13 level:4 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài tập 5. Giải hệ phương trình:

$$
\left\{ {\begin{array}{l}
{{3^{\log x}} = {4^{\log y}}}\\
{{{(4x)}^{\log 4}} = {{(3y)}^{\log 3}}}
\end{array}} \right..
$$

<!-- chunk:14 level:4 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài tập 6. Cho hai đường thẳng $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right)$ có phương trình:

$\left( {{d_1}} \right):kx – y + k = 0$; $\left( {{d_2}} \right):\left( {1 – {k^2}} \right)x + 2ky – \left( {1 + {k^2}} \right) = 0.$

a. Chứng minh rằng khi $k$ thay đổi đường thẳng $\left( {{d_1}} \right)$ luôn đi qua một điểm cố định.

b. Với mỗi giá trị của $k$, hãy xác định giao điểm của $\left( {{d_1}} \right)$ và $\left( {{d_2}} \right).$

c. Tìm quỹ tích của giao điểm đó khi $k$ thay đổi.

<!-- chunk:15 level:4 source:https://toanmath.com/2020/04/mot-so-bai-toan-dua-ve-he-phuong-trinh-bac-nhat.html -->
## Bài tập 9. Hãy biện luận giá trị nhỏ nhất của biểu thức sau theo $a:$

$F = {(x – 2y + 1)^2} + {(2x + ay + 5)^2}.$