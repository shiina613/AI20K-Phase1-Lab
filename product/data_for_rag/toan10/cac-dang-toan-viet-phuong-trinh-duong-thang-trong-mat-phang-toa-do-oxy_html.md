# Các dạng toán viết phương trình đường thẳng trong mặt phẳng tọa độ Oxy

<!-- chunk:0 level:0 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
Bài viết hướng dẫn phương pháp giải các dạng toán viết phương trình đường thẳng trong mặt phẳng tọa độ Oxy.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## I. KIẾN THỨC CẦN NẮM VỮNG
1. Định nghĩa véctơ chỉ phương, véctơ pháp tuyến của đường thẳng
a) Véctơ chỉ phương của đường thẳng
Véctơ $\overrightarrow u$ được gọi là véctơ chỉ phương của đường thẳng $d$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\vec u \ne \vec 0}\\
{\vec u{\rm{//}}d}
\end{array}} \right.
$$

Nhận xét: Nếu $\overrightarrow u$ là một véctơ chi phương (vtcp) của đường thẳng $d$ thì mọi véctơ $k\overrightarrow u$, với $k ≠ 0$ đều là véctơ chỉ phương của đường thẳng đó.

b) Véctơ pháp tuyến của đường thẳng

Một véctơ $\vec n$ được gọi là véctơ pháp tuyến của đường thẳng $d$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\vec n \ne \vec 0}\\
{\vec n \bot d}
\end{array}} \right.
$$

Nhận xét:

+ Nếu $\vec n$ là một véctơ pháp tuyến (vtpt) của đường thẳng $d$ thì mọi véctơ $k\overrightarrow n$, với $k ≠ 0$ đều là véctơ pháp tuyến của đường thẳng đó.

+ Nếu đường thẳng $d$ có véctơ pháp tuyến $\vec n = (a;b)$ thì nó có véctơ chỉ phương là $\overrightarrow u = ( – b;a)$.

+ Ngược lại nếu đường thẳng $d$ có véctơ chỉ phương $\vec u = (a;b)$ thì nó có véctơ pháp tuyến là $\vec n = ( – b;a).$

2. Phương trình tổng quát của đường thẳng
Đường thẳng trong mặt phẳng có dạng tổng quát $d:$ $ax + by + c = 0$ $\left( {{a^2} + {b^2} > 0} \right)$, trong đó $a$, $b$, $c$ là các hệ số thực.

+ Đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ $\Leftrightarrow a{x_0} + b{y_0} + c = 0.$

+ Véctơ pháp tuyến vuông góc với $d$ là $\vec n = (a;b).$

+ Véctơ chỉ phương song song với $d$ là $\overrightarrow u = ( – b;a).$

+ Phương trình tham số của đường thẳng: $d:$ 
$$
\left\{ {\begin{array}{l}
{x = {x_0} – bt}\\
{y = {y_0} + at}
\end{array}} \right.
$$
 $(t \in R).$

+ Phương trình chính tắc của đường thẳng $d:\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b}.$

3. Các dạng phương trình đường thẳng đặc biệt
+ Trục hoành $Ox$: $y = 0.$

+ Trục tung $Oy$: $x = 0.$

+ Phương trình đường thẳng đi qua hai điểm $A(a;0)$ và $B(0;b)$ (phương trình đoạn chắn) có phương trình là $d$: $\frac{x}{a} + \frac{y}{b} = 1$ (áp dụng khi đường thẳng cắt hai trục tọa độ).

+ Phương trình đường thẳng đi qua hai điểm phân biệt $M\left( {{x_1};{y_1}} \right)$, $N\left( {{x_2};{y_2}} \right)$ là $MN$: $\frac{{x – {x_1}}}{{{x_2} – {x_1}}} = \frac{{y – {y_1}}}{{{y_2} – {y_1}}}$ (áp dụng khi đường thẳng đi qua hai điểm xác định cho trước).

+ Phương trình đường thẳng đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có hệ số góc $k$ là $d$: $y = k\left( {x – {x_0}} \right) + {y_0}$ (áp dụng khi chỉ biết đường thẳng đi qua một điểm và thỏa mãn một điều kiện khác).

+ Phương trình tổng quát của đường thẳng đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có véctơ pháp tuyến $\vec n = (a;b)$ là $d$: $a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0$, $\left( {{a^2} + {b^2} > 0} \right)$ (có thể sử dụng thay thế cho dạng đường thẳng đi qua điểm và có hệ số góc).

4. Vị trí tương đối của điểm so với đường thẳng
Xét đường thẳng $d$: $ax + by + c = 0$ $\left( {{a^2} + {b^2} > 0} \right)$ và hai điểm $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right).$

Xét tích $T = \left( {a{x_A} + b{y_B} + c} \right)\left( {a{x_B} + b{y_B} + c} \right).$

+ Nếu $T>0$ thì $A$, $B$ nằm về hai phía so với $d.$

+ Nếu $T<0$ thì $A$, $B$ nằm về cùng một phía so với $d.$

+ Nếu $T= 0$ thì hoặc $A$ hoặc $B$ nằm trên $d.$

5. Khoảng cách từ một điểm đến một đường thẳng

Xét đường thẳng $d$: $ax + by + c = 0$ $\left( {{a^2} + {b^2} > 0} \right)$ và điểm $M\left( {{x_0};{y_0}} \right).$

Khoảng cách từ điểm $M$ đến đường thẳng $d$ được ký hiệu là $d(M;d)$ và được xác định theo công thức: $d(M;d) = \frac{{\left| {a{x_0} + b{y_0} + c} \right|}}{{\sqrt {{a^2} + {b^2}} }}.$

Ứng dụng: Viết phương trình đường phân giác của góc tạo bởi hai đường thẳng.

Xét hai đường thẳng: ${d_1}$: ${a_1}x + {b_1}y + {c_1} = 0$ $\left( {a_1^2 + b_1^2 > 0} \right)$ và ${d_2}$: ${a_2}x + {b_2}y + {c_2} = 0$ $\left( {a_2^2 + b_2^2 > 0} \right).$

Nếu điểm $M(x;y)$ nằm trên đường phân giác của góc tạo bởi $d_1$ và $d_2$ thì $d\left( {M;{d_1}} \right) = d\left( {M;{d_2}} \right)$. Suy ra phương trình đường phân giác của góc tạo bởi ${d_1}$, ${d_2}$ có phương trình là: $\Delta :\frac{{\left| {{a_1}x + {b_1}y + {c_1}} \right|}}{{\sqrt {a_1^2 + b_1^2} }} = \frac{{\left| {{a_2}x + {b_2}y + {c_2}} \right|}}{{\sqrt {a_2^2 + b_2^2} }}$ $\Leftrightarrow \Delta :\frac{{{a_1}x + {b_1}y + {c_1}}}{{\sqrt {a_1^2 + b_1^2} }} = \pm \frac{{{a_2}x + {b_2}y + {c_2}}}{{\sqrt {a_2^2 + b_2^2} }}.$

6. Góc giữa hai đường thẳng
Xét hai đường thẳng ${d_1}$: ${a_1}x + {b_1}y + {c_1} = 0$ $\left( {a_1^2 + b_1^2 > 0} \right)$ có véctơ pháp tuyến $\overrightarrow {{n_1}} = \left( {{a_1};{b_1}} \right)$ và đường thẳng ${d_2}$: ${a_2}x + {b_2}y + {c_2} = 0$ $\left( {a_2^2 + b_2^2 > 0} \right)$ có véctơ pháp tuyến $\overrightarrow {{n_2}} = \left( {{a_2};{b_2}} \right)$.

Khi đó góc $\alpha$ $\left( {0 \le \alpha \le {{90}^0}} \right)$ giữa hai đường thẳng được xác định theo công thức: $\cos \alpha = \frac{{\left| {\overrightarrow {{n_1}} .\overrightarrow {{n_2}} } \right|}}{{\left| {\overrightarrow {{n_1}} } \right|.\left| {\overrightarrow {{n_2}} } \right|}} = \frac{{\left| {{a_1}{a_2} + {b_1}{b_2}} \right|}}{{\sqrt {a_1^2 + b_1^2} .\sqrt {a_2^2 + b_2^2} }}.$

7. Vị trí tương đối của hai đường thẳng

Xét hai đường thẳng ${d_1}$: ${a_1}x + {b_1}y + {c_1} = 0$ $\left( {a_1^2 + b_1^2 > 0} \right)$ có véctơ pháp tuyến $\overrightarrow {{n_1}} = \left( {{a_1};{b_1}} \right)$ và đường thẳng ${d_2}$: ${a_2}x + {b_2}y + {c_2} = 0$ $\left( {a_2^2 + b_2^2 > 0} \right)$ có véctơ pháp tuyến $\overrightarrow {{n_2}} = \left( {{a_2};{b_2}} \right).$

+ ${d_1}$ cắt ${d_2}$ $\Leftrightarrow \frac{{{a_1}}}{{{a_2}}} \ne \frac{{{b_1}}}{{{b_2}}}.$

+ ${d_1}{\rm{//}}{d_2} \Leftrightarrow \frac{{{a_1}}}{{{a_2}}} = \frac{{{b_1}}}{{{b_2}}} \ne \frac{{{c_1}}}{{{c_2}}}.$

+ ${d_1} \equiv {d_2} \Leftrightarrow \frac{{{a_1}}}{{{a_2}}} = \frac{{{b_1}}}{{{b_2}}} = \frac{{{c_1}}}{{{c_2}}}.$

Đặc biệt: ${d_1} \bot {d_2}$ $\Leftrightarrow {a_1}{a_2} + {b_1}{b_2} = 0.$

Các bài toán được áp dụng là xét vị trí tương đối giữa hai đường thẳng phụ thuộc tham số.

[ads]

<!-- chunk:2 level:1 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## II. CÁC DẠNG TOÁN VIẾT PHƯƠNG TRÌNH ĐƯỜNG THẲNG (OXY)
Phương pháp:

+ Vận dụng công thức phương trình đường thẳng đi qua điểm và có hệ số góc $k.$

+ Vận dụng công thức phương trình đoạn chắn.

+ Vận dụng công thức phương trình đường thẳng đi qua điểm và có véctơ pháp tuyến $\vec n = (a;b)$.

+ Vận dụng công thức tính khoảng cách từ điểm đến đường thẳng.

+ Vận dụng công thức tính góc giữa hai đường thẳng.

+ Vận dụng công thức phương trình đường phân giác của góc tạo bởi hai đường

thẳng.

<!-- chunk:3 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 1: Viết phương trình đường thẳng $Δ$ đi qua hai điểm ${M_1}\left( {{x_1};{y_1}} \right)$ và ${M_2}\left( {{x_2};{y_2}} \right).$

Cách giải:

+ Nếu ${x_1} = {x_2}$ $\Rightarrow \Delta: x = {x_1}.$

+ Nếu ${y_1} = {y_2}$ $\Rightarrow \Delta: y = {y_1}.$

+ Nếu ${x_1} \ne {x_2}$, ${y_1} \ne {y_2}$ $\Rightarrow \Delta :\frac{{x – {x_1}}}{{{x_2} – {x_1}}} = \frac{{y – {y_1}}}{{{y_2} – {y_1}}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 1: Viết phương trình đường thẳng d đi qua hai điểm $M( – 1;2)$ và $N(3; – 6).$

Đường thẳng đi qua hai điểm $M$, $N$ xác định bởi: $d:\frac{{x + 1}}{{3 + 1}} = \frac{{y – 2}}{{ – 6 – 2}}$ $\Leftrightarrow d:2x + y = 0.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 2: Viết phương trình đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có véctơ pháp tuyến $(a;b)$.

Cách giải: Đường thẳng đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có véctơ pháp tuyến $(a;b)$ xác định bởi: $d:a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0$ $\Leftrightarrow d:ax + by – a{x_0} – b{y_0} = 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 2: Viết phương trình đường thẳng $d$ đi qua điểm $M(-1;2)$ và có véctơ pháp tuyến $\vec n = (2; – 3)$.

Đường thẳng $d$ đi qua điểm $M(-1;2)$ và có véctơ pháp tuyến $\vec n = (2; – 3)$ xác định bởi: $d:2(x + 1) – 3(y – 2) = 0$ $\Leftrightarrow d:2x – 3y + 8 = 0.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 3: Viết phương trình đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có véctơ chỉ phương $\overrightarrow u = (a;b).$

Cách giải: Đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có véctơ chỉ phương $\overrightarrow u = (a;b)$ xác định bởi:

+ Cách 1: Phương trình chính tắc $d:\frac{{x – {x_0}}}{a} = \frac{{y – {y_0}}}{b}.$

+ Cách 2: Phương trình tham số 
$$
d:\left\{ {\begin{array}{l}
{x = {x_0} + at}\\
{y = {y_0} + bt}
\end{array}} \right.
$$
 $(t \in R).$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 3: Viết phương trình đường thẳng $d$ đi qua điểm $M(3;4)$ và có véctơ chỉ phương $\overrightarrow u = (2;3)$.

Đường thẳng $d$ đi qua điểm $M(3;4)$ và có véctơ chỉ phương $\overrightarrow u = (2;3)$ xác định bởi: $d:\frac{{x – 3}}{2} = \frac{{y – 4}}{3}$ hoặc 
$$
d:\left\{ {\begin{array}{l}
{x = 3 + 2t}\\
{y = 4 + 3t}
\end{array}} \right.
$$
 $(t \in R).$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 4: Viết phương trình đường thẳng $d$ (phương trình đoạn chắn) đi qua hai điểm nằm trên các trục tọa độ $A(a;0)$, $B(0;b)$ ($ab ≠ 0$).

Cách giải: Đường thẳng $d$ xác định bởi: $d:\frac{x}{a} + \frac{y}{b} = 1.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 4: Viết phương trình đường thẳng $d$ đi qua hai điểm $A(4;0)$, $B(0;6).$

Đường thẳng $d$ đi qua hai điểm $A(4;0)$, $B(0;6)$ xác định bởi: $d:\frac{x}{4} + \frac{y}{6} = 1$ $\Leftrightarrow d:3x + 2y – 12 = 0.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 5: Viết phương trình đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có hệ số góc $k.$

Cách giải: Đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và có hệ số góc $k$ xác định bởi: $d:y = k\left( {x – {x_0}} \right) + {y_0}$, trong đó $k = \tan \alpha$, là góc tạo bởi đường thẳng $d$ và chiều dương trục hoành.

<!-- chunk:12 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 5: Viết phương trình đường thẳng $d$ trong các trường hợp sau đây:

a) Đi qua điểm $M(1;2)$ và có hệ số góc $k = 3.$

b) Đi qua điểm $A(-3;2)$ và tạo với chiều dương trục hoành một góc $45°.$

c) Đi qua điểm $B(3;2)$ và tạo với trục hoành một góc $60°.$

a) Đường thẳng đi qua điểm $M(1;2)$ và có hệ số góc $k = 3$ xác định bởi: $d:y = 3(x – 1) + 2$ $\Leftrightarrow d:3x – y – 1 = 0.$

b) Đường thẳng đi qua điểm $A(-3;2)$ và tạo với chiều dương trục hoành một góc $45°$ nên có hệ số góc $k = \tan {45^0} = 1$ $\Rightarrow d:y = 1(x + 3) + 2$ $\Leftrightarrow d:x – y + 5 = 0.$

c) Đường thẳng đi qua điểm $B(3;2)$ và tạo với trục hoành một góc $60°$ nên có hệ số góc 
$$
k = \left[ \begin{array}{l}
\tan {60^0} = \sqrt 3 \\
\tan \left( {{{180}^0} – {{60}^0}} \right) = – \sqrt 3
\end{array} \right.
$$

Vậy có hai đường thẳng thỏa mãn là: ${d_1}:\sqrt 3 x – y + 2 – 3\sqrt 3 = 0$, ${d_2}:\sqrt 3 x + y – 2 – 3\sqrt 3 = 0.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 6: Viết phương trình đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và song song với đường thẳng $\Delta :Ax + By + C = 0$.

Cách giải: Đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và song song với đường thẳng $\Delta :Ax + By + C = 0$ nhận $\overrightarrow n = (A;B)$ véctơ pháp tuyến của $Δ$ làm véctơ pháp tuyến nên có phương trình là: $d:A\left( {x – {x_0}} \right) + B\left( {y – {y_0}} \right) = 0$ $\Leftrightarrow d:Ax + By – A{x_0} – B{y_0} = 0.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 6: Viết phương trình đường thẳng $d$ đi qua điểm $M(3;2)$ và song song với đường thẳng $\Delta :3x + 4y – 12 = 0$.

Đường thẳng $d$ đi qua điểm $M(3;2)$ và song song với đường thẳng $\Delta :3x + 4y – 12 = 0$ nên nhận $\vec n = (3;4)$ véctơ pháp tuyến của $Δ$ làm véctơ pháp tuyến nên có phương trình là: $d:3(x – 3) + 4(y – 2) = 0$ $\Leftrightarrow d:3x + 4y – 17 = 0.$

Áp dụng: Trong các bài toán về đường thẳng đi qua điểm song song với đường thắng cho trước, đường trung bình trong tam giác, hình bình hành, hình thoi, hình chữ nhật, hình vuông.

<!-- chunk:15 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 7: Viết phương trình đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và vuông góc với đường thẳng $\Delta :Ax + By + C = 0.$

Cách giải: Đường thẳng $d$ đi qua điểm $M\left( {{x_0};{y_0}} \right)$ và vuông góc với đường thẳng $\Delta :Ax + By + C = 0$ nhận $\overrightarrow u = (B; – A)$ véctơ chỉ phương của $Δ$ làm véctơ pháp tuyến nên có phương trình là: $d:B\left( {x – {x_0}} \right) – A\left( {y – {y_0}} \right) = 0$ $\Leftrightarrow d:Bx – Ay + A{y_0} – B{x_0} = 0.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 7: Viết phương trình đường thẳng $d$ đi qua điểm $M(1;2)$ và vuông góc với đường thẳng $\Delta :4x – 5y + 6 = 0$.

Vì $d$ vuông góc với $Δ$ nên nhận véctơ chỉ phương $\vec u = (5;4)$ của $Δ$ làm véctơ pháp tuyến nên có phương trình là: $d:5(x – 1) + 4(y – 2) = 0$ $\Leftrightarrow d:5x + 4y – 13 = 0.$

Áp dụng: Trong các bài toán về đường thẳng đi qua điểm và vuông góc với đường thẳng, đường cao, đường trung trực trong tam giác, hình thoi, hình chữ nhật, hình vuông, hình thang vuông.

<!-- chunk:17 level:2 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Dạng 8: Góc giữa hai đường thẳng, khoảng cách từ điểm đến đường thẳng.

Cách giải:

• Khoảng cách từ một điểm đến một đường thẳng.

Xét đường thẳng $d:ax + by + c = 0$ $\left( {{a^2} + {b^2} > 0} \right)$ và điểm $M\left( {{x_0};{y_0}} \right).$

Khoảng cách từ điểm $M$ đến đường thẳng $d$ được ký hiệu là $d(M;d)$ và được xác định theo công thức: $d(M;d) = \frac{{\left| {a{x_0} + b{y_0} + c} \right|}}{{\sqrt {{a^2} + {b^2}} }}.$

• Viết phương trình đường phân giác của góc tạo bởi hai đường thẳng.

Xét hai đường thẳng: ${d_1}:{a_1}x + {b_1}y + {c_1} = 0$ $\left( {a_1^2 + b_1^2 > 0} \right)$ và ${d_2}:{a_2}x + {b_2}y + {c_2} = 0$ $\left( {a_2^2 + b_2^2 > 0} \right).$

Nếu điểm $M(x;y)$ nằm trên đường phân giác của góc tạo bởi $d_1$ và $d_2$ thì $d\left( {M;{d_1}} \right) = d\left( {M;{d_2}} \right)$. Suy ra phương trình đường phân giác của góc tạo bởi $d_1$, $d_2$ có phương trình là: $\Delta :\frac{{\left| {{a_1}x + {b_1}y + {c_1}} \right|}}{{\sqrt {a_1^2 + b_1^2} }} = \frac{{\left| {{a_2}x + {b_2}y + {c_2}} \right|}}{{\sqrt {a_2^2 + b_2^2} }}$ $\Leftrightarrow \Delta :\frac{{{a_1}x + {b_1}y + {c_1}}}{{\sqrt {a_1^2 + b_1^2} }} = \pm \frac{{{a_2}x + {b_2}y + {c_2}}}{{\sqrt {a_2^2 + b_2^2} }}.$

• Góc giữa hai đường thẳng. 

Xét hai đường thẳng ${d_1}:{a_1}x + {b_1}y + {c_1} = 0$ $\left( {a_1^2 + b_1^2 > 0} \right)$ có véctơ pháp tuyến $\overrightarrow {{n_1}} = \left( {{a_1};{b_1}} \right)$ và đường thẳng ${d_2}:{a_2}x + {b_2}y + {c_2} = 0$ $\left( {a_2^2 + b_2^2 > 0} \right)$ có véc tơ pháp tuyến $\overrightarrow {{n_2}} = \left( {{a_2};{b_2}} \right)$.

Khi đó góc $\alpha \left( {0 \le \alpha \le {{90}^0}} \right)$ giữa hai đường thẳng được xác định theo công thức: $\cos \alpha = \frac{{\left| {\overrightarrow {{n_1}} .\overrightarrow {{n_2}} } \right|}}{{\left| {\overrightarrow {{n_1}} } \right|.\left| {\overrightarrow {{n_2}} } \right|}}$ $= \frac{{\left| {{a_1}{a_2} + {b_1}{b_2}} \right|}}{{\sqrt {a_1^2 + b_1^2} .\sqrt {a_2^2 + b_2^2} }}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 8: Viết phương trình đường thẳng đi qua điểm $P(2;5)$ sao cho khoảng cách từ điểm $Q(5;1)$ đến đường thẳng đó bằng $3.$

Đường thẳng cần tìm có phương trình dạng tổng quát là: $\Delta :a(x – 2) + b(y – 5) = 0$ $\Leftrightarrow \Delta :ax + by – 2a – 5b = 0$ $\left( {{a^2} + {b^2} > 0} \right).$

Khoảng cách từ $Q$ đến $Δ$ bằng $3$ khi và chỉ khi $\frac{{|5a + b – 2a – 5b|}}{{\sqrt {{a^2} + {b^2}} }} = 3$ $\Leftrightarrow {(3a – 4b)^2} = 9\left( {{a^2} + {b^2}} \right)$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{b = 0}\\
{a = \frac{7}{{24}}b}
\end{array}} \right.
$$

+ Với $b = 0$, chọn $a = 1$ $\Rightarrow {\Delta _1}:x – 2 = 0.$

+ Với $a = \frac{7}{{24}}b$, chọn $b = 24 \Rightarrow a = 7$ $\Rightarrow {\Delta _2}:7x + 24y – 134 = 0.$

Vậy có hai đường thẳng cần tìm thỏa mãn yêu cầu bài toán là: ${\Delta _1}:x – 2 = 0$, ${\Delta _2}:7x + 24y – 134 = 0.$

<!-- chunk:19 level:3 source:https://toanmath.com/2018/10/cac-dang-toan-viet-phuong-trinh-duong-thang-trong-mat-phang-toa-do-oxy.html -->
## Ví dụ 9: Viết phương trình đường thẳng $d$ đi qua điểm $A(2;1)$ và tạo với đường thẳng $\Delta :2x + 3y + 4 = 0$ góc $45°$.

Giả sử $\vec n = (a;b)$ $\left( {{a^2} + {b^2} > 0} \right)$ là véctơ pháp tuyến của $d.$

Đường thẳng $Δ$ có véctơ pháp tuyến $\overrightarrow {{n_\Delta }} = (2;3).$

Góc giữa hai đường thẳng bằng $45°$ khi và chỉ khi $\cos {45^0} = \frac{{\left| {\overrightarrow n .\overrightarrow {{n_\Delta }} } \right|}}{{\left| {\overrightarrow n } \right|.\left| {\overrightarrow {{n_\Delta }} } \right|}}$ $\Leftrightarrow \frac{{|2a + 3b|}}{{\sqrt {{2^2} + {3^2}} .\sqrt {{a^2} + {b^2}} }} = \frac{1}{{\sqrt 2 }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 5b}\\
{a = – \frac{1}{5}b}
\end{array}} \right.
$$

+ Với $a = 5b$, chọn $b = 1 \Rightarrow a = 5$ $\Rightarrow d:5x + y – 11 = 0.$

+ Với $a = – \frac{1}{5}b$, chọn $b = – 5 \Rightarrow a = 1$ $\Rightarrow d:x – 5y + 3 = 0.$