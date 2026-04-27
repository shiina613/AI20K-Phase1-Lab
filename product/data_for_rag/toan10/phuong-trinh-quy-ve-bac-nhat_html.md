# Phương trình quy về bậc nhất

<!-- chunk:0 level:0 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
Bài viết giới thiệu và hướng dẫn giải một số dạng phương trình quy về bậc nhất, giúp học sinh học tốt chương trình Đại số lớp 10.

<!-- chunk:1 level:2 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài toán 1. Giải và biện luận phương trình $\left( {{a_1}x + {b_1}} \right)\left( {{a_2}x + {b_2}} \right) = 0.$
Phương pháp chung: Tập hợp nghiệm của phương trình là nghiệm của hệ:

$$
\left[ {\begin{array}{l}
{{a_1}x + {b_1} = 0\,\,\,(1)}\\
{{a_2}x + {b_2} = 0\,\,\,(2)}
\end{array}} \right..
$$

Với bài toán giải và biện luận ta cần thực hiện theo các bước sau:

+ Bước 1. Giải và biện luận $(1).$

+ Bước 2. Giải và biện luận $(2).$

+ Bước 3. Kết luận: Trong bước này các em học sinh cần biết cách kết hợp các trường hợp đã xét trong cả hai bước 1 và bước 2 để có được lời kết luận đầy đủ và tường minh.

Ví dụ minh họa:

<!-- chunk:2 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 1: Giải phương trình: $(5x – 3)(4x + 1)(x – 8)(x + 3) = 0.$

Lời giải:

Phương trình tương đương với:

$$
\left[ {\begin{array}{l}
{5x – 3 = 0}\\
{4x + 1 = 0}\\
{x – 8 = 0}\\
{x + 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 3/5}\\
{x = – 1/4}\\
{x = 8}\\
{x = – 3}
\end{array}} \right..
$$

Vậy phương trình có $4$ nghiệm phân biệt.

<!-- chunk:3 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 2: Giải và biện luận phương trình: $(m – 2){x^2} – (2m – 1)x + m + 1 = 0$ $(1).$

Lời giải:

Biến đổi phương trình về dạng:

$[(m – 2)x – m – 1](x – 1) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{(m – 2)x = m + 1\,\,\,(2)}
\end{array}} \right..
$$

Ta đi giải và biện luận $(2).$

a. Nếu $m – 2 = 0$ $\Leftrightarrow m = 2.$

$(2) \Leftrightarrow 0x = 3$ mâu thuẩn $\Rightarrow (2)$ vô nghiệm.

b. Nếu $m – 2 \ne 0$ $\Leftrightarrow m \ne 2.$

$(2) \Leftrightarrow x = \frac{{m + 1}}{{m – 2}}.$

Kết luận:

+ Với $m = 2$, phương trình có nghiệm duy nhất $x = 1.$

+ Với $m \ne 2$, phương trình có $2$ nghiệm $x = 1$ và $x = \frac{{m + 1}}{{m – 2}}.$

Nhận xét: Bằng việc biến đổi phương trình ban đầu về dạng tích ta đã biện luận được một phương trình bậc hai, tuy nhiên sau này ta có được một phương pháp tổng quát hơn để giải và biện luận một phương trình bậc hai bất kỳ.

<!-- chunk:4 level:2 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài toán 2. Giải và biện luận phương trình $\frac{{A(x)}}{{B(x)}} = 0.$
Phương pháp chung: Tập hợp nghiệm của phương trình này là nghiệm của phương trình $A(x) = 0$ không làm cho $B(x)$ bằng $0$, tức là:

$$
\left\{ {\begin{array}{l}
{B(x) \ne 0}\\
{A(x) = 0}
\end{array}} \right..
$$

Để tường minh hơn ta đi xét bài toán: Giải và biện luận phương trình $\frac{{ax + b}}{{cx + d}} = e$ với $c \ne 0$ $(1).$

Ta thực hiện theo các bước sau:

Bước 1. Đặt điều kiện $cx + d \ne 0$ $\Leftrightarrow x \ne – \frac{d}{c}.$

Bước 2: Biến đổi $(1)$ về dạng: $(a – ce)x = de – b$ $(2).$

Bước 3. Biện luận:

a. Nếu $a – ce = 0$ thì:

$(2) \Leftrightarrow 0 = de – b.$

+ Nếu $de – b = 0$, phương trình nghiệm đúng với $\forall x \in R\backslash \left\{ { – \frac{d}{c}} \right\}.$

+ Nếu $de – b \ne 0$, phương trình vô nghiệm.

b. Nếu $a – ce \ne 0$ thì:

$(2) \Leftrightarrow x = \frac{{de – b}}{{a – ce}}.$

Kiểm tra điều kiện:

$x \ne – \frac{d}{c}$ $\Leftrightarrow \frac{{de – b}}{{a – ce}} \ne – \frac{d}{c}$ $\Leftrightarrow ad \ne bc.$

Bước 4. Kết luận.

Ví dụ minh họa:

<!-- chunk:5 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 3: Giải và biện luận phương trình:

$\frac{{mx – m – 3}}{{x + 1}} = 1$ $(1).$

Lời giải:

Điều kiện $x + 1 \ne 0$ $\Leftrightarrow x \ne – 1.$

Biến đổi $(1)$ về dạng:

$(m – 1)x = m + 4$ $(2).$

a. Nếu $m – 1 = 0$ $\Leftrightarrow m = 1.$

$(2) \Leftrightarrow 0 = 5$ mâu thuẫn $\Rightarrow$ phương trình vô nghiệm.

b. Nếu $m – 1 \ne 0$ $\Leftrightarrow m \ne 1.$

$(2) \Leftrightarrow x = \frac{{m + 4}}{{m – 1}}.$

Kiểm tra điều kiện:

$x \ne – 1$ $\Leftrightarrow \frac{{m + 4}}{{m – 1}} \ne – 1$ $\Leftrightarrow m \ne – \frac{3}{2}.$

Kết luận:

+ Với $m = 1$ hoặc $m = – \frac{3}{2}$, phương trình vô nghiệm.

+ Với $m \in R\backslash \left\{ {1; – \frac{3}{2}} \right\}$, phương trình có nghiệm $x = \frac{{m + 4}}{{m – 1}}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 4: Giải và biện luận phương trình:

$\frac{a}{{ax – 1}} + \frac{b}{{bx – 1}}$ $= \frac{{a + b}}{{(a + b)x – 1}}$ $(1).$

Lời giải:

Điều kiện:

$$
\left\{ {\begin{array}{l}
{ax – 1 \ne 0}\\
{bx – 1 \ne 0}\\
{(a + b)x – 1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ax \ne 1}\\
{bx \ne 1}\\
{(a + b)x \ne 1}
\end{array}} \right.
$$
 $(I).$

Viết lại phương trình dưới dạng:

$abx[(a + b)x – 2] = 0$ $(2).$

a. Nếu $a = b = 0$ thì điều kiện $(I)$ luôn đúng.

Khi đó:

$(2) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với $\forall x \in R.$

b. Nếu $a = 0$ và $b \ne 0$ thì điều kiện $(I)$ trở thành $x \ne \frac{1}{b}.$

Khi đó:

$(2) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với mọi $x \ne \frac{1}{b}.$

c. Nếu $a \ne 0$ và $b = 0$ thì điều kiện $(I)$ trở thành $x \ne \frac{1}{a}.$

Khi đó:

$(2) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với mọi $x \ne \frac{1}{a}.$

d. Nếu $a \ne 0$ và $a + b = 0$ $\Leftrightarrow b = – a \ne 0$ thì điều kiện $(I)$ trở thành $x \ne \frac{1}{a}$ và $x \ne \frac{1}{b}.$

Khi đó:

$(2) \Leftrightarrow x = 0$ là nghiệm duy nhất của phương trình.

e. Nếu $a \ne 0$, $b \ne 0$ và $a + b \ne 0$ thì điều kiện $(I)$ trở thành $x \ne \frac{1}{a}$ và $x \ne \frac{1}{b}$ và $x \ne \frac{1}{{a + b}}.$

Khi đó:

$$
(2) \Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \frac{2}{{a + b}}}
\end{array}} \right..
$$

Nghiệm $x = \frac{2}{{a + b}}$ chỉ thoả mãn điều kiện khi $a \ne b.$

Kết luận:

+ Với $a = b = 0$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $a = 0$ và $b \ne 0$, phương trình nghiệm đúng với mọi $x \ne \frac{1}{b}.$

+ Với $a \ne 0$ và $b = 0$, phương trình nghiệm đúng với mọi $x \ne \frac{1}{a}.$

+ Với $b = \pm a \ne 0$, phương trình có nghiệm duy nhất $x = 0.$

+ Với $a \ne 0$, $b \ne 0$, $a + b \ne 0$, $a \ne b$, phương trình có nghiệm $x = 0$ và $x = \frac{2}{{a + b}}.$

<!-- chunk:7 level:2 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài toán 3. Giải và biện luận phương trình $|ax + b| = |cx + d|.$
Phương pháp chung:

Tập xác định của phương trình $D = R.$

Áp dụng tính chất:

$|A| = |B|$ $\Leftrightarrow {A^2} = {B^2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{A = B}\\
{A = – B}
\end{array}} \right..
$$

Phương trình được chuyển thành dạng:

$$
\left[ {\begin{array}{l}
{ax + b = cx + d\,\,\,(2)}\\
{ax + b = – cx – d\,\,\,(3)}
\end{array}} \right..
$$

Như vậy tập nghiệm của phương trình là hợp hai tập nghiệm của $(2)$ và $(3).$

Ví dụ minh họa:

<!-- chunk:8 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 5: Giải và biện luận phương trình: $|mx + 1| = |3x + m – 2|$ $(1).$

Lời giải:

Phương trình được chuyển thành dạng:

$$
\left[ {\begin{array}{l}
{mx + 1 = 3x + m – 2}\\
{mx + 1 = – 3x – m + 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{(m – 3)x = m – 3}&{(2)}\\
{(m + 3)x = 1 – m}&{(3)}
\end{array}} \right..
$$

a. Giải và biện luận phương trình $(2).$

Nếu $m – 3 = 0$ $\Leftrightarrow m = 3.$

$(2) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với $\forall x \in R.$

Nếu $m – 3 \ne 0$ $\Leftrightarrow m \ne 3.$

$(2) \Leftrightarrow x = 1$: phương trình có nghiệm duy nhất.

b. Giải và biện luận phương trình $(3).$

Nếu $m + 3 = 0$ $\Leftrightarrow m = – 3.$

$(3) \Leftrightarrow 0x = 4$, phương trình vô nghiệm.

Nếu $m + 3 \ne 0$ $\Leftrightarrow m \ne – 3.$

$(3) \Leftrightarrow x = \frac{{1 – m}}{{m + 3}}$: là nghiệm duy nhất.

Kết luận:

+ Với $m = 3$, phương trình nghiệm đúng với mọi $x \in R.$

+ Với $m = -3$, phương trình có một nghiệm là $x = 1.$

+ Với $m \ne \pm 3$, phương trình có hai nghiệm là $x = 1$ và $x = \frac{{1 – m}}{{m + 3}}.$

<!-- chunk:9 level:2 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài toán 4. Giải và biện luận phương trình $|ax + b| = cx + d.$
Phương pháp chung: Áp dụng phép biến đổi:

$|A| = B$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{B \ge 0}\\
{\left[ {\begin{array}{l}
{A = B}\\
{A = – B}
\end{array}} \right.}
\end{array}} \right.
$$
 $(I).$

Hoặc:

$|A| = B$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{A \ge 0}\\
{A = B}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{A \le 0}\\
{ – A = B}
\end{array}} \right.}
\end{array}} \right.
$$
 $(II).$

Lưu ý: Ta thấy:

1. Nếu $B$ không chứa tham số ta lựa chọn phép biến đổi $(I).$

2. Nếu $B$ chứa tham số ta lựa chọn phép biến đổi $(II).$

3. Trong trường hợp cả $A$, $B$ đều chứa tham số thì tuỳ vào độ phức tạp của $A$, $B$ ta lựa chọn phép biến đổi $(I)$ hoặc $(II).$

Ví dụ minh họa:

<!-- chunk:10 level:3 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Ví dụ 6: Giải và biện luận phương trình: $|x – 1| = mx – 1.$

Lời giải:

Phương trình tương đương với:

$$
\left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{x – 1 \ge 0}\\
{x – 1 = mx – 1}
\end{array}} \right.}\\
{\left\{ {\begin{array}{l}
{x – 1 \le 0}\\
{1 – x = mx – 1}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\left\{ {\begin{array}{l}
{x \ge 1}\\
{(m – 1)x = 0\,\,\,(1)}
\end{array}} \right.\,\,\,(I)}\\
{\left\{ {\begin{array}{l}
{x \le 1}\\
{(m + 1)x = 2\,\,\,(2)}
\end{array}\,\,\,(II)} \right.}
\end{array}} \right..
$$

a. Giải và biện luận $(I).$

Nếu $m – 1 = 0$ $\Leftrightarrow m = 1.$

$(1) \Leftrightarrow 0x = 0$, phương trình nghiệm đúng với mọi $x \in R.$

$\Leftrightarrow$ hệ nghiệm đúng với mọi $x \ge 1.$

Nếu $m – 1 \ne 0$ $\Leftrightarrow m \ne 1.$

$(1) \Leftrightarrow x = 0$ loại vì $x \ge 1$ $\Rightarrow$ hệ phương trình vô nghiệm.

b. Giải và biện luận $(II).$

Nếu $m + 1 = 0$ $\Leftrightarrow m = – 1.$

$(2) \Leftrightarrow 0x = 2$, phương trình vô nghiệm.

Nếu $m + 1 \ne 0$ $\Leftrightarrow m \ne – 1.$

$(2) \Leftrightarrow x = \frac{2}{{m + 1}}.$

Vì điều kiện $x \le 1$, nên ta phải có:

$\frac{2}{{m + 1}} \le 1$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m \ge 1}\\
{m < – 1}
\end{array}} \right..
$$

Khi đó hệ phương trình có nghiệm duy nhất $x = \frac{2}{{m + 1}}.$

Kết luận:

+ Với $m = 1$, phương trình nghiệm đúng với mọi $x \ge 1.$

+ Với $– 1 \le m < 1$, phương trình vô nghiệm.

+ Với $m < – 1 \vee m \ge 1$, phương trình có nghiệm là $x = \frac{2}{{m + 1}}.$

<!-- chunk:11 level:4 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài tập 1. Giải và biện luận các phương trình:

a. $\frac{{x – m}}{{x – 1}} + \frac{{x – 1}}{{x – m}} = 2.$

b. $\frac{{mx + 1}}{{x – 1}} = 2.$

c. $\frac{{(m + 1)x + m – 2}}{{x + 3}} = m.$

d. $\frac{x}{{\sqrt {x – 2} }} = \frac{m}{{\sqrt {x – 2} }}.$

e. $|mx + 1| = |2x + m – 3|.$

f. $|x – 1| = mx + 2m – 1.$

g. $\frac{x}{{\sqrt {x + m} }} = \frac{x}{{\sqrt {x + 1} }}.$

<!-- chunk:12 level:4 source:https://toanmath.com/2020/04/phuong-trinh-quy-ve-bac-nhat.html -->
## Bài tập 2. Xác định $m$ để các phương trình sau có nghiệm:

a. ${m^2}(x – 1) = 4x – 3m + 2$ với $x > 0.$

b. $\frac{{2x + m}}{{\sqrt {x – 1} }} – 4\sqrt {x – 1}$ $= \frac{{x – 2m + 3}}{{\sqrt {x – 1} }}.$

c. $\frac{{(2m + 1)x + 3}}{{\sqrt {4 – {x^2}} }}$ $= \frac{{(2m + 3)x + m – 2}}{{\sqrt {4 – {x^2}} }}.$

d. $2(|x| + m – 1) = |x| – m + 3.$