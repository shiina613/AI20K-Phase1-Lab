# Phương trình tổng quát của đường thẳng

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
Bài viết trình bày lý thuyết và hướng dẫn phương pháp giải các dạng toán thường gặp liên quan đến phương trình tổng quát của đường thẳng trong chương trình Hình học 10 chương 3: phương pháp tọa độ trong mặt phẳng.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## A. TÓM TẮT LÝ THUYẾT
1. Vectơ pháp tuyến và phương trình tổng quát của đường thẳng

a. Định nghĩa: Cho đường thẳng $\Delta .$ Vectơ $\vec n \ne \vec 0$ gọi là vectơ pháp tuyến (VTPT) của $\Delta$ nếu giá của $\vec n$ vuông góc với $\Delta .$

Nhận xét: Nếu $\overrightarrow n$ là VTPT của $\Delta$ thì $k\overrightarrow n$ $(k \ne 0)$ cũng là VTPT của $\Delta .$

b. Phương trình tổng quát của đường thẳng
Cho đường thẳng $\Delta$ đi qua ${M_0}\left( {{x_0};{y_0}} \right)$ và có VTPT $\vec n = (a;b).$

Khi đó $M(x;y) \in \Delta$ $\Leftrightarrow \overrightarrow {M{M_0}} \bot \overrightarrow n$ $\Leftrightarrow \overrightarrow {M{M_0}} .\overrightarrow n = 0$ $\Leftrightarrow a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0$ $\Leftrightarrow ax + by + c = 0$ (với ${c = – a{x_0} – b{y_0}}$).

Phương trình $ax + by + c = 0$ gọi là phương trình tổng quát của đường thẳng $\Delta .$

Chú ý: Nếu đường thẳng $\Delta :ax + by + c = 0$ thì $\overrightarrow n = (a;b)$ là VTPT của $\Delta .$

c. Các dạng đặc biệt của phương trình tổng quát

$\Delta$ song song hoặc trùng với trục $Ox$ $\Leftrightarrow \Delta :by + c = 0.$

$\Delta$ song song hoặc trùng với trục $Oy$ $\Leftrightarrow \Delta :ax + c = 0.$

$\Delta$ đi qua gốc tọa độ $\Leftrightarrow \Delta :ax + by = 0.$

$\Delta$ đi qua hai điểm $A(a;0)$ và $B(0;b)$ $\Leftrightarrow \Delta :\frac{x}{a} + \frac{y}{b} = 1$ với $ab \ne 0.$

Phương trình đường thẳng có hệ số góc $k$ là $y = kx + m$ với $k = \tan \alpha$, $\alpha$ là góc hợp bởi tia $Mt$ của $\Delta$ ở phía trên trục $Ox$ và tia $Mx.$

2. Vị trí tương đối của hai đường thẳng

Cho hai đường thẳng ${d_1}:{a_1}x + {b_1}y + {c_1} = 0$ và ${d_2}:{a_2}x + {b_2}y + {c_2} = 0.$

+ ${d_1}$ cắt ${d_2}$ khi và chỉ khi 
$$
\left| {\begin{array}{l}
{{a_1}}&{{b_1}}\\
{{a_2}}&{{b_2}}
\end{array}} \right| \ne 0.
$$

+ ${d_1}//{d_2}$ khi và chỉ khi 
$$
\left| {\begin{array}{l}
{{a_1}}&{{b_1}}\\
{{a_2}}&{{b_2}}
\end{array}} \right| = 0
$$
 và 
$$
\left| {\begin{array}{l}
{{b_1}}&{{c_1}}\\
{{b_2}}&{{c_2}}
\end{array}} \right| \ne 0
$$
 hoặc 
$$
\left| {\begin{array}{l}
{{a_1}}&{{b_1}}\\
{{a_2}}&{{b_2}}
\end{array}} \right| = 0
$$
 và 
$$
\left| {\begin{array}{l}
{{c_1}}&{{a_1}}\\
{{c_2}}&{{a_2}}
\end{array}} \right| \ne 0.
$$

+ ${d_1} \equiv {d_2}$ khi và chỉ khi 
$$
\left| {\begin{array}{l}
{{a_1}}&{{b_1}}\\
{{a_2}}&{{b_2}}
\end{array}} \right|
$$
 
$$
= \left| {\begin{array}{l}
{{b_1}}&{{c_1}}\\
{{b_2}}&{{c_2}}
\end{array}} \right|
$$
 
$$
= \left| {\begin{array}{l}
{{c_1}}&{{a_1}}\\
{{c_2}}&{{a_2}}
\end{array}} \right| = 0.
$$

Chú ý: Với trường hợp ${a_2}{b_2}{c_2} \ne 0$ khi đó:

+ Nếu $\frac{{{a_1}}}{{{b_1}}} \ne \frac{{{a_2}}}{{{b_2}}}$ thì hai đường thẳng cắt nhau.

+ Nếu $\frac{{{a_1}}}{{{b_1}}} = \frac{{{a_2}}}{{{b_2}}} \ne \frac{{{c_1}}}{{{c_2}}}$ thì hai đường thẳng song song nhau.

+ Nếu $\frac{{{a_1}}}{{{b_1}}} = \frac{{{a_2}}}{{{b_2}}} = \frac{{{c_1}}}{{{c_2}}}$ thì hai đường thẳng trùng nhau.

<!-- chunk:2 level:1 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI

DẠNG TOÁN 1: VIẾT PHƯƠNG TRÌNH TỔNG QUÁT CỦA ĐƯỜNG THẲNG. 

1. PHƯƠNG PHÁP GIẢI

Để viết phương trình tổng quát của đường thẳng $\Delta$ ta cần xác định:

+ Điểm $A\left( {{x_0};{y_0}} \right) \in \Delta .$

+ Một vectơ pháp tuyến $\vec n(a;b)$ của $\Delta .$

Khi đó phương trình tổng quát của $\Delta$ là $a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0.$

Chú ý:

Đường thẳng $\Delta$ có phương trình tổng quát là $ax + by + c = 0$, ${a^2} + {b^2} \ne 0$ nhận $\vec n(a;b)$ làm vectơ pháp tuyến.

Nếu hai đường thẳng song song với nhau thì VTPT đường thẳng này cũng là VTPT của đường thẳng kia.

Phương trình đường thẳng $\Delta$ qua điểm $M\left( {{x_0};{y_0}} \right)$ có dạng: $\Delta :a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0$ với ${a^2} + {b^2} \ne 0$, hoặc ta chia làm hai trường hợp:

+ $x = {x_0}$: nếu đường thẳng song song với trục $Oy.$

+ $y – {y_0} = k\left( {x – {x_0}} \right)$: nếu đường thẳng cắt trục $Oy.$

Phương trình đường thẳng đi qua $A(a;0)$, $B(0;b)$ với $ab \ne 0$ có dạng: $\frac{x}{a} + \frac{y}{b} = 1.$

2. CÁC VÍ DỤ

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 1: Cho tam giác $ABC$ biết $A(2;0)$, $B(0;4)$, $C(1;3).$ Viết phương trình tổng quát của:

a) Đường cao $AH.$

b) Đường trung trực của đoạn thẳng $BC.$

c) Đường thẳng $AB.$

d) Đường thẳng qua $C$ và song song với đường thẳng $AB.$

a) Vì $AH \bot BC$ nên $\overrightarrow {BC}$ là vectơ pháp tuyến của $AH.$

Ta có $\overrightarrow {BC} (1; – 1)$ suy ra đường cao $AH$ đi qua $A$ và nhận $\overrightarrow {BC}$ là vectơ pháp tuyến có phương trình tổng quát là $1.(x – 2) – 1.(y – 0) = 0$ hay $x – y – 2 = 0.$

b) Đường trung trực của đoạn thẳng $BC$ đi qua trung điểm $BC$ và nhận vectơ $\overrightarrow {BC}$ làm vectơ pháp tuyến.

Gọi $I$ là trung điểm $BC$ khi đó ${x_I} = \frac{{{x_B} + {x_C}}}{2} = \frac{1}{2}$, ${y_I} = \frac{{{y_B} + {y_C}}}{2} = \frac{7}{2}$ $\Rightarrow I\left( {\frac{1}{2};\frac{7}{2}} \right).$

Suy ra phương trình tổng quát của đường trung trực $BC$ là:

$1.\left( {x – \frac{1}{2}} \right) – 1.\left( {y – \frac{7}{2}} \right) = 0$ hay $x – y + 3 = 0.$

c) Phương trình tổng quát của đường $AB$ có dạng: $\frac{x}{2} + \frac{y}{4} = 1$ hay $2x + y – 4 = 0.$

d) Cách 1: Đường thẳng $AB$ có VTPT là $\vec n(2;1)$ do đó vì đường thẳng cần tìm song song với đường thẳng $AB$ nên nhận $\vec n(2;1)$ làm VTPT do đó có phương trình tổng quát là $2.(x – 1) + 1.(y – 3) = 0$ hay $2x + y – 5 = 0.$

Cách 2: Đường thẳng $\Delta$ song song với đường thẳng $AB$ có dạng $2x + y + c = 0.$

Điểm $C$ thuộc $\Delta$ suy ra $2.1 + 3 + c = 0$ $\Rightarrow c = – 5.$

Vậy đường thẳng cần tìm có phương trình tổng quát là $2x + y – 5 = 0.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 2: Cho đường thẳng $d:x – 2y + 3 = 0$ và điểm $M(-1;2).$ Viết phương trình tổng quát của đường thẳng $\Delta$ biết:

a) $\Delta$ đi qua điểm $M$ và có hệ số góc $k = 3.$

b) $\Delta$ đi qua $M$ và vuông góc với đường thẳng $d.$

c) $\Delta$ đối xứng với đường thẳng $d$ qua $M.$

a) Đường thẳng $\Delta$ có hệ số góc $k = 3$ có phương trình dạng $y = 3x + m.$ Mặc khác $M \in \Delta$ $\Rightarrow 2 = 3.( – 1) + m$ $\Rightarrow m = 5.$

Suy ra phương trình tổng quát đường thẳng $\Delta$ là $y = 3x + 5$ hay $3x – y + 5 = 0.$

b) Ta có $x – 2y + 3 = 0$ $\Leftrightarrow y = \frac{1}{2}x + \frac{3}{2}$ do đó hệ số góc của đường thẳng $d$ là ${k_d} = \frac{1}{2}.$

Vì $\Delta \bot d$ nên hệ số góc của $\Delta$ là ${k_\Delta }$ thì ${k_d}.{k_\Delta } = – 1$ $\Rightarrow {k_\Delta } = – 2.$

Do đó $\Delta :y = – 2x + m$, $M \in \Delta$ $\Rightarrow 2 = – 2.( – 1) + m$ $\Rightarrow m = 0.$

Suy ra phương trình tổng quát đường thẳng $\Delta$ là $y = – 2x – 2$ hay $2x + y + 2 = 0.$

c) Cách 1: Ta có $– 1 – 2.2 + 3 \ne 0$ do đó $M \notin d$ vì vậy đường thẳng $\Delta$ đối xứng với đường thẳng $d$ qua $M$ sẽ song song với đường thẳng $d$ suy ra đường thẳng $\Delta$ có VTPT là $\vec n(1; – 2).$

Ta có $A(1;2) \in d$, gọi $A’$ đối xứng với $A$ qua $M$ khi đó $A’ \in \Delta .$

Ta có $M$ là trung điểm của $AA’.$

$$
\Rightarrow \left\{ {\begin{array}{l}
{{x_M} = \frac{{{x_A} + {x_{A’}}}}{2}}\\
{{y_M} = \frac{{{y_A} + {y_{A’}}}}{2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{c}
{{x_{A’}} = 2{x_M} – {x_A} = – 3}\\
{{y_{A’}} = 2{y_M} – {y_A} = 2}
\end{array}} \right.
$$
 $\Rightarrow A'( – 3;2).$

Vậy phương trình tổng quát đường thẳng $\Delta$ là $1.(x + 3) – 2.(y – 2) = 0$ hay $x – 2y + 7 = 0.$

Cách 2: Gọi $A\left( {{x_0};{y_0}} \right)$ là điểm bất kỳ thuộc đường thẳng $d$, $A'(x;y)$ là điểm đối xứng với $A$ qua $M.$

Khi đó $M$ là trung điểm của $AA’$ suy ra:

$$
\left\{ {\begin{array}{l}
{{x_M} = \frac{{{x_0} + x}}{2}}\\
{{y_M} = \frac{{{y_0} + y}}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 = \frac{{{x_0} + x}}{2}}\\
{2 = \frac{{{y_0} + y}}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_0} = – 2 – x}\\
{{y_0} = 4 – y}
\end{array}} \right..
$$

Ta có $A \in d$ $\Rightarrow {x_0} – 2{y_0} + 3 = 0$ suy ra $( – 2 – x) – 2(4 – y) + 3 = 0$ $\Leftrightarrow x – 2y + 7 = 0.$

Vậy phương trình tổng quát của $\Delta$ đối xứng với đường thẳng $d$ qua $M$ là $x – 2y + 7 = 0.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 3: Biết hai cạnh của một hình bình hành có phương trình $x – y = 0$ và $x + 3y – 8 = 0$, tọa độ một đỉnh của hình bình hành là $( – 2;2).$ Viết phương trình các cạnh còn lại của hình bình hành.

Đặt tên hình bình hành là $ABCD$ với $A(-2;2)$, do tọa độ điểm $A$ không là nghiệm của hai phương trình đường thẳng trên nên ta giả sử $BC:x – y = 0$, $CD:x + 3y – 8 = 0.$

Vì $AB//CD$ nên cạnh $AB$ nhận $\overrightarrow {{n_{CD}}} (1;3)$ làm VTPT, do đó có phương trình là $1.(x + 2) + 3.(y – 2) = 0$ hay $x + 3y – 4 = 0.$

Tương tự cạnh $AD$ nhận $\overrightarrow {{n_{BC}}} (1; – 1)$ làm VTPT, do đó có phương trình là $1.(x + 2) – 1.(y – 2) = 0$ hay $x – y + 4 = 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 4: Cho điểm $M(1;4).$ Viết phương trình đường thẳng qua $M$ lần lượt cắt hai tia $Ox$, tia $Oy$ tại $A$ và $B$ sao cho tam giác $OAB$ có diện tích nhỏ nhất.

Giả sử $A(a;0)$, $B(0;b)$ với $a > 0$, $b > 0.$ Khi đó đường thẳng đi qua $A$, $B$ có dạng $\frac{x}{a} + \frac{y}{b} = 1.$ Do $M \in AB$ nên $\frac{1}{a} + \frac{4}{b} = 1.$

Mặt khác ${S_{OAB}} = \frac{1}{2}OA.OB = \frac{1}{2}ab.$

Áp dụng BĐT Côsi ta có $1 = \frac{1}{a} + \frac{4}{b} \ge 2\sqrt {\frac{4}{{ab}}}$ $\Rightarrow ab \ge 16$ $\Rightarrow {S_{OAB}} \ge S.$

Suy ra ${S_{OAB}}$ nhỏ nhất khi $\frac{1}{a} = \frac{4}{b}$ và $\frac{1}{a} + \frac{4}{b} = 1$, do đó $a = 2$, $b = 8.$

Vậy phương trình đường thẳng cần tìm là $\frac{x}{2} + \frac{y}{8} = 1$ hay $4x + y – 8 = 0.$

## Bài tập
## Bài 1: Cho điểm $A(1;-3).$ Viết phương trình tổng quát của đường thẳng $\Delta$ đi qua $A$ và:

a) vuông góc với trục tung.

b) song song với đường thẳng $d:x + 2y + 3 = 0.$

a) $\Delta \bot Oy$ $\Rightarrow \Delta$ nhận $\vec j(0;1)$ làm VTPT, do đó phương trình tổng quát của đường thẳng $\Delta$ là $0.(x – 1) + 1.(y + 3) = 0$ hay $y + 3 = 0.$

b) $\Delta //d$ $\Rightarrow \Delta$ nhận $\vec n(1;2)$ làm VTPT, do đó phương trình tổng quát của đường thẳng $\Delta$ là $1.(x – 1) + 2.(y + 3) = 0$ hay $x + 2y + 5 = 0.$

## Bài 2: Cho tam giác $ABC$ biết $A(2;1)$, $B(-1;0)$, $C(0;3).$

a) Viết phương trình tổng quát của đường cao $AH.$

b) Viết phương trình tổng quát đường trung trực của đoạn thẳng $AB.$

c) Viết phương trình tổng quát đường thẳng $BC.$

d) Viết phương trình tổng quát đường thẳng qua $A$ và song song với đường thẳng $BC.$

a) Ta có đường cao $AH$ đi qua $A$ và nhận $\overrightarrow {BC} (1;3)$ là VTPT nên có phương trình tổng quát là $1.(x – 2) + 3.(y – 1) = 0$ hay $x + 3y – 5 = 0.$

b) Gọi $I$ là trung điểm $AB$ khi đó:

${x_I} = \frac{{{x_A} + {x_B}}}{2} = \frac{1}{2}$, ${y_I} = \frac{{{y_A} + {y_B}}}{2} = \frac{1}{2}$ $\Rightarrow I\left( {\frac{1}{2};\frac{1}{2}} \right).$

Đường trung trực đoạn thẳng $AB$ đi qua $I$ và nhận $\overrightarrow {AB} ( – 3; – 1)$ làm VTPT nên có phương trình tổng quát là $– 3.\left( {x – \frac{1}{2}} \right) – 1.\left( {y – \frac{1}{2}} \right) = 0$ hay $3x + y – 2 = 0.$

c) Phương trình tổng quát của đường thẳng $BC$ có dạng $\frac{x}{{ – 1}} + \frac{y}{3} = 1$ hay $3x – y + 3 = 0.$

d) Đường thẳng $BC$ có VTPT là $\vec n(3; – 1)$, do đó vì đường thẳng cần tìm song song với đường thẳng $BC$ nên nhận $\vec n(3; – 1)$ làm VTPT, do đó có phương trình tổng quát là $3.(x – 2) – 1.(y – 1) = 0$ hay $3x – y – 5 = 0.$

## Bài 3: Viết phương trình tổng quát của đường thẳng $\Delta$ trong mỗi trường hợp sau:

a) $\Delta$ đi qua điểm $M(2;5)$ và song song với đường thẳng $d: 4x – 7y + 3 = 0.$

b) $\Delta$ đi qua $P(2;-5)$ và có hệ số góc $k = 11.$

a) Vì $\Delta //d$ nên VTPT của $d$ cũng là VTPT của $\Delta$ nên đường thẳng $\Delta$ nhận $\vec n(4; – 7)$ làm VTPT và $\overrightarrow u (7;4)$ làm VTCP.

Do đó phương trình tổng quát là $4(x – 2) – 7(y – 5) = 0$ hay $4x – 7y – 27 = 0.$

b) Đường thẳng $\Delta$ có hệ số góc $k = 11$ nên có dạng $y = 11x + m.$ Mặt khác $P \in \Delta$ nên $– 5 = 11.2 + m$ $\Leftrightarrow m = – 27.$

Vậy phương trình tổng quát của $\Delta$ là $11x – y – 27 = 0.$

## Bài 4: Cho $M(8;6).$ Viết phương trình đường thẳng qua $M$ cắt chiều dương hai trục toạ độ tại $A$, $B$ sao cho $OA + OB$ đạt giá trị nhỏ nhất.

Gọi $A(a;0)$, $B(0;b)$ $(a, b >0).$

Vậy đường thẳng cần tìm có dạng:

$\Delta :\frac{x}{a} + \frac{y}{b} = 1$. Vì $M \in \Delta$ $\Rightarrow \frac{8}{a} + \frac{6}{b} = 1$ $\Rightarrow b = \frac{{6a}}{{a – 8}}.$

Ta có: $OA + OB = a + b$ $= a + \frac{{6a}}{{a – 8}}$ $= a – 8 + \frac{{48}}{{a – 8}} + 14$ $\ge 8\sqrt 3 + 14.$

Dấu bằng xảy ra $\Leftrightarrow a = 8 + 4\sqrt 3$, $b = 6 + 4\sqrt 3 .$

Suy ra $\Delta :\frac{x}{{8 + 4\sqrt 3 }} + \frac{y}{{6 + 4\sqrt 3 }} = 1.$

DẠNG TOÁN 2: XÉT VỊ TRÍ TƯƠNG ĐỐI CỦA HAI ĐƯỜNG THẲNG.

1. PHƯƠNG PHÁP GIẢI

Để xét vị trí tương đối của hai đường thẳng: ${d_1}:{a_1}x + {b_1}y + {c_1} = 0$ và ${d_2}:{a_2}x + {b_2}y + {c_2} = 0$, ta xét hệ:

$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y + {c_1} = 0}\\
{{a_2}x + {b_2}y + {c_2} = 0}
\end{array}} \right.
$$
 $(I).$

+ Hệ $(I)$ vô nghiệm suy ra ${d_1}//{d_2}.$

+ Hệ $(I)$ vô số nghiệm suy ra ${d_1} \equiv {d_2}.$

+ Hệ $(I)$ có nghiệm duy nhất suy ra ${d_1}$ và ${d_2}$ cắt nhau và nghiệm của hệ là tọa độ giao điểm.

Chú ý: Với trường hợp ${a_2}{b_2}{c_2} \ne 0$ khi đó:

+ Nếu $\frac{{{a_1}}}{{{a_2}}} \ne \frac{{{b_1}}}{{{b_2}}}$ thì hai đường thẳng cắt nhau.

+ Nếu $\frac{{{a_1}}}{{{a_2}}} = \frac{{{b_1}}}{{{b_2}}} \ne \frac{{{c_1}}}{{{c_2}}}$ thì hai đường thẳng song song nhau.

+ Nếu $\frac{{{a_1}}}{{{a_2}}} = \frac{{{b_1}}}{{{b_2}}} = \frac{{{c_1}}}{{{c_2}}}$ thì hai đường thẳng trùng nhau.

2. CÁC VÍ DỤ

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 1: Xét vị trí tương đối các cặp đường thẳng sau:

a) ${\Delta _1}:x + y – 2 = 0$ và ${\Delta _2}:2x + y – 3 = 0.$

b) ${\Delta _1}: – x – 2y + 5 = 0$ và ${\Delta _2}:2x + 4y – 10 = 0.$

c) ${\Delta _1}:2x – 3y + 5 = 0$ và ${\Delta _2}:x – 5 = 0.$

d) ${\Delta _1}:2x + 3y + 4 = 0$ và ${\Delta _2}: – 4x – 6y = 0.$

a) Ta có $\frac{1}{2} \ne \frac{1}{1}$ suy ra ${\Delta _1}$ cắt ${\Delta _2}.$

b) Ta có $\frac{{ – 1}}{2} = \frac{{ – 2}}{4} = \frac{5}{{ – 10}}$ suy ra ${\Delta _1}$ trùng ${\Delta _2}.$

c) Ta có $\frac{1}{2} \ne \frac{0}{{ – 3}}$ suy ra ${\Delta _1}$ cắt ${\Delta _2}.$

d) Ta có $\frac{{ – 4}}{2} = \frac{{ – 6}}{3} \ne \frac{0}{4}$ suy ra ${\Delta _1}//{\Delta _2}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 2: Cho tam giác $ABC$ có phương trình các đường thẳng $AB$, $BC$, $CA$ là $AB: 2x – y + 2 = 0$, $BC: 3x + 2y + 1 = 0$, $CA: 3x + y + 3 = 0.$ Xác định vị trí tương đối của đường cao kẻ từ đỉnh $A$ và đường thẳng $\Delta :3x – y – 2 = 0.$

Tọa độ điểm $A$ là nghiệm của hệ 
$$
\left\{ {\begin{array}{l}
{2x – y + 2 = 0}\\
{3x + y + 3 = 0}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = – 1}\\
{y = 0}
\end{array}} \right.
$$
 $\Rightarrow A( – 1;0).$

Ta xác định được hai điểm thuộc đường thẳng $BC$ là $M( – 1;1)$, $N(1; – 2).$

Đường cao kẻ từ đỉnh $A$ vuông góc với $BC$ nên nhận vectơ $\overrightarrow {MN} (2; – 3)$ làm vectơ pháp tuyến nên có phương trình là $2(x + 1) – 3y = 0$ hay $2x – 3y + 2 = 0.$

Ta có $\frac{3}{2} \ne \frac{{ – 1}}{{ – 3}}$ suy ra hai đường thẳng cắt nhau.

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 3: Cho hai đường thẳng: ${\Delta _1}:(m – 3)x + 2y + {m^2} – 1 = 0$ và ${\Delta _2}: – x + my + {(m – 1)^2} = 0.$

a) Xác định vị trí tương đối và xác định giao điểm (nếu có) của ${\Delta _1}$ và ${\Delta _2}$ trong các trường hợp $m = 0$, $m = 1.$

b) Tìm $m$ để hai đường thẳng song song với nhau.

a) Với $m = 0$ xét hệ 
$$
\left\{ {\begin{array}{l}
{ – 3x + 2y – 1 = 0}\\
{ – x + 1 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 1}\\
{y = 2}
\end{array}} \right.
$$
 suy ra ${\Delta _1}$ cắt ${\Delta _2}$ tại điểm có tọa độ $(1;2).$

Với $m=1$ xét hệ 
$$
\left\{ {\begin{array}{l}
{2x + 2y = 0}\\
{ – x + y = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 0}
\end{array}} \right.
$$
 suy ra ${\Delta _1}$ cắt ${\Delta _2}$ tại gốc tọa độ.

b) Với $m =0$ hoặc $m=1$ theo câu a hai đường thẳng cắt nhau nên không thỏa mãn.

Với $m \ne 0$ và $m \ne 1$ hai đường thẳng song song khi và chỉ khi:

$\frac{{m – 3}}{{ – 1}} = \frac{2}{m} \ne \frac{{{m^2} – 1}}{{{{(m – 1)}^2}}}$ $\Leftrightarrow m = 2.$

Vậy với $m = 2$ thì hai đường thẳng song song với nhau.

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/phuong-trinh-tong-quat-cua-duong-thang.html -->
## Ví dụ 4: Cho tam giác $ABC$, tìm tọa độ các đỉnh của tam giác trong trường hợp sau:

a) Biết $A(2;2)$ và hai đường cao có phương trình: ${d_1}:x + y – 2 = 0$ và ${d_2}:9x – 3y + 4 = 0.$

b) Biết $A(4; – 1)$, phương trình đường cao kẻ từ $B$ là $\Delta :2x – 3y = 0$, phương trình trung tuyến đi qua đỉnh $C$ là $\Delta ‘:2x + 3y = 0.$

a) Tọa độ điểm $A$ không là nghiệm của phương trình ${d_1}$, ${d_2}$ suy ra $A \notin {d_1}$, $A \notin {d_2}$ nên ta có thể giả sử $B \in {d_1}$, $C \in {d_2}.$

Ta có $AB$ đi qua $A$ và vuông góc với ${d_2}$ nên nhận $\overrightarrow u = (3;9)$ làm VTPT nên có phương trình là $3(x – 2) + 9(y – 2) = 0$ hay $3x + 9y – 24 = 0$, $AC$ đi qua $A$ và vuông góc với ${d_1}$ nên nhận $\overrightarrow v ( – 1;1)$ làm VTPT nên có phương trình là $– 1(x – 2) + 1(y – 2) = 0$ hay $x – y = 0.$

$B$ là giao điểm của ${d_1}$ và $AB$ suy ra tọa độ của $B$ là nghiệm của hệ: 
$$
\left\{ {\begin{array}{l}
{x + y – 2 = 0}\\
{3x + 9y – 24 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – 1}\\
{y = 3}
\end{array}} \right.
$$
 $\Rightarrow B( – 1;3).$

Tương tự tọa độ $C$ là nghiệm của hệ:

$$
\left\{ {\begin{array}{l}
{9x – 3y + 4 = 0}\\
{x – y = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – \frac{2}{3}}\\
{y = – \frac{2}{3}}
\end{array}} \right.
$$
 $\Rightarrow C\left( { – \frac{2}{3}; – \frac{2}{3}} \right).$

Vậy $A(2;2)$, $B( – 1;3)$ và $C\left( { – \frac{2}{3}; – \frac{2}{3}} \right).$

b) Ta có $AC$ đi qua $A(4; – 1)$ và vuông góc với $\Delta$ nên nhận $\overrightarrow u (3;2)$ làm VTPT nên có phương trình là $3(x – 4) + 2(y + 1) = 0$ hay $3x + 2y – 10 = 0.$

Suy ra toạ độ $C$ là nghiệm của hệ: 
$$
\left\{ {\begin{array}{l}
{3x + 2y – 10 = 0}\\
{2x + 3y = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 6}\\
{y = – 4}
\end{array}} \right.
$$
 $\Rightarrow C(6; – 4).$

Giả sử $B\left( {{x_B};{y_B}} \right)$, suy ra trung điểm $M\left( {\frac{{{x_B} + 4}}{2};\frac{{{y_B} – 1}}{2}} \right)$ của $AB$ thuộc đường thẳng $\Delta ‘$ do đó: $2.\frac{{{x_B} + 4}}{2} + 3.\frac{{{y_B} – 1}}{2} = 0$ hay $2{x_B} + 3{y_B} + 5 = 0$ $(1).$

Mặt khác $B \in \Delta$ suy ra $2{x_B} – 3{y_B} = 0$ $(2).$

Từ $(1)$ và $(2)$ suy ra $B\left( { – \frac{5}{4}; – \frac{5}{6}} \right).$

Vậy $A(4; – 1)$, $B\left( { – \frac{5}{4}; – \frac{5}{6}} \right)$ và $C(6; – 4).$

## Bài tập
## Bài 1: Xét vị trí tương đối của các cặp đường thẳng sau:

a) ${d_1}:x + y – 3 = 0$ và ${d_2}:2x + 2y = 0.$

b) ${d_1}: – 4x + 6y – 2 = 0$ và ${d_2}:2x – 3y + 1 = 0.$

c) ${d_1}:3x + 2y – 1 = 0$ và ${d_2}:x + 3y – 4 = 0.$

a) ${d_1}//{d_2}.$

b) ${d_1} \equiv {d_2}.$

c) ${d_1}$ cắt ${d_2}.$

## Bài 2: Cho hai đường thẳng ${\Delta _1}:3x – y – 3 = 0$, ${\Delta _2}:x + y + 2 = 0$ và điểm $M(0;2).$

a) Tìm tọa độ giao điểm của ${\Delta _1}$ và ${\Delta _2}.$

b) Viết phương trình đường thẳng $\Delta$ đi qua $M$ và cắt ${\Delta _1}$ và ${\Delta _2}$ lần lượt tại $A$ và $B$ sao cho $B$ là trung điểm của đoạn thẳng $AM.$

a) $N\left( {\frac{1}{4}; – \frac{9}{4}} \right).$

b) $A \in {\Delta _1}$ $\Rightarrow 3{x_A} – {y_A} – 3 = 0$ $\Rightarrow {y_A} = 3{x_A} – 3.$

$B \in {\Delta _2}$ $\Rightarrow {x_B} + {y_B} + 2 = 0$ $\Rightarrow {y_B} = – {x_B} – 2.$

$B$ là trung điểm $AM.$

Suy ra 
$$
\left\{ {\begin{array}{c}
{2{x_B} = {x_A}}\\
{ – 4{x_B} – 4 = 2 + 3{x_A} – 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_A} = – \frac{3}{4}}\\
{{x_B} = – \frac{3}{8}}
\end{array}} \right.
$$
 $\Rightarrow \Delta :29x – 3y + 6 = 0.$

## Bài 3: Cho hai đường thẳng có phương trình: ${\Delta _1}:(a – b)x + y = 1$ và ${\Delta _2}:\left( {{a^2} – {b^2}} \right)x + ay = b$ với ${a^2} + {b^2} \ne 0.$

a) Tìm quan hệ giữa $a$ và $b$ để ${\Delta _1}$ và ${\Delta _2}$ cắt nhau.

b) Tìm điều kiện giữa $a$ và $b$ để ${\Delta _1}$ và ${\Delta _2}$ cắt nhau tại điểm thuộc trục hoành.

a) Nếu $a = b$ $\Rightarrow {\Delta _1} \equiv {\Delta _2}.$

Nếu $a \ne b$ $\Rightarrow {\Delta _1}$ và ${\Delta _2}$ cắt nhau $\Leftrightarrow \frac{{{a^2} – {b^2}}}{{a – b}} \ne \frac{1}{a}$ $\Leftrightarrow b \ne 0.$

Vậy $b \ne 0$ và $a \ne b$ là điều kiện cần tìm.

b) Cho $y = 0$ $\Rightarrow (a – b)x = 1$ và $\left( {{a^2} – {b^2}} \right)x = b$ suy ra $\frac{1}{{a – b}} = \frac{b}{{{a^2} – {b^2}}}$ $\Leftrightarrow a = 0.$

## Bài 4: Cho hai đường thẳng ${\Delta _1}:mx – y + 1 – m = 0$ và ${\Delta _2}: – x + my + 2 = 0.$ Biện luận theo $m$ vị trí tương đối của hai đường thẳng.

Trường hợp 1: Nếu $m = 0$ $\Rightarrow {\Delta _1}$ cắt ${\Delta _2}.$

Trường hợp 2: Nếu $m \ne 0:$

+ Nếu $\frac{m}{{ – 1}} \ne \frac{{ – 1}}{m}$ $\Leftrightarrow m \ne \pm 1$ $\Rightarrow {\Delta _1}$ cắt ${\Delta _2}.$

+ Nếu $\frac{m}{{ – 1}} = \frac{{ – 1}}{m} \ne \frac{{1 – m}}{2}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m = \pm 1}\\
{m \ne – 1}
\end{array}} \right.
$$
 $\Leftrightarrow m = 1$ thì ${\Delta _1}//{\Delta _2}.$

+ Nếu $\frac{m}{{ – 1}} = \frac{{ – 1}}{m} = \frac{{1 – m}}{2}$ $\Leftrightarrow m = – 1$ thì ${\Delta _1} \equiv {\Delta _2}.$

## Bài 5: Trong mặt phẳng với hệ tọa độ $Oxy$, cho các điểm $A(0;1)$, $B(2;-1)$ và các đường thẳng: ${d_1}:(m – 1)x + (m – 2)y + 2 – m = 0$ và ${d_2}:(2 – m)x + (m – 1)y + 3m – 5 = 0.$

a) Chứng minh ${d_1}$ và ${d_2}$ luôn cắt nhau.

b) Gọi $P$ là giao điểm của ${d_1}$ và ${d_2}$. Tìm $m$ sao cho $PA + PB$ lớn nhất.

${(PA + PB)^2}$ $\le 2\left( {P{A^2} + P{B^2}} \right)$ $= 2A{B^2} = 16.$

Do đó $\max (PA + PB) = 4$ khi $P$ là trung điểm của cung $AB.$

Khi đó $P(2;1)$ hay $P(0; – 1)$ suy ra $m=1$ hoặc $m=2.$

## Bài 6: Trong mặt phẳng với hệ tọa độ $Oxy$ cho hai đường thẳng ${\Delta _m}:mx + y – m – 1 = 0$ và $\Delta {‘_m}:x – my – 3 – m = 0$ (với $m$ là tham số thực). Chứng minh rằng với mọi $m \in R$ thì hai đường thẳng đó luôn cắt nhau tại một điểm nằm trên một đường tròn cố định.

Để ý rằng hai đường thẳng này vuông góc với nhau nên cắt nhau tại điểm $M.$ Rõ ràng đường thẳng thứ nhất đi qua điểm cố định $A(1;1)$ và đường thẳng thứ hai đi qua điểm cố định $B(3;-1)$, nên tập hợp điểm $M$ là đường tròn đường kính $AB.$

## Bài 7: Cho tam giác $ABC$ biết $AB:5x – 2y + 6 = 0$ và $AC:4x + 7y – 21 = 0$ và $H(0;0)$ là trực tâm của tam giác. Tìm tọa độ điểm $A$, $B.$

Toạ độ của $A$ là nghiệm của hệ phương trình:

$$
\left\{ {\begin{array}{l}
{5x – 2y + 6 = 0}\\
{4x + 7y – 21 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 3}
\end{array}} \right.
$$
 $\Rightarrow A(0;3).$

Vì $B(a;b)$ thuộc $AB$ nên $5a – 2b + 6 = 0$ $\Rightarrow b = \frac{{5a + 6}}{2}$ hay $B\left( {a;\frac{{5a + 6}}{2}} \right).$

Mặt khác $H$ là trực tâm nên $HB \bot AC$, suy ra $\overrightarrow {HB}$ là VTPT của $AC$, do đó $\overrightarrow {HB}$ cùng phương với $\overrightarrow {{n_{AC}}} (4;7)$ $\Leftrightarrow \frac{a}{4} = \frac{{5a + 6}}{{14}} = 0$ $\Leftrightarrow a = – 4$ $\Rightarrow B( – 4; – 7).$

## Bài 8: Cho điểm $A(2;1)$ và đường thẳng $d: 3x – y + 3 = 0.$ Tìm hình chiếu của $A$ lên $d.$

Gọi $\Delta$ là đường thẳng đi qua $A$ và vuông góc với $d.$ Ta có hệ số góc của đường thẳng $d$ là ${k_d} = 3$, do đó hệ số góc của đường thẳng $\Delta$ là ${k_\Delta } = – \frac{1}{3}.$

Do đó đường thẳng $\Delta$ có dạng: $y = – \frac{1}{3}x + m.$

$A \in \Delta$ $\Rightarrow 2 = – \frac{1}{3}.1 + m$ $\Rightarrow m = \frac{7}{3}.$

Vậy $\Delta :y = – \frac{1}{3}x + \frac{7}{3}$ hay $x + 3y – 7 = 0.$

Tọa độ giao điểm của $\Delta$ và $d$ là nghiệm của hệ:

$$
\left\{ {\begin{array}{l}
{3x – y + 3 = 0}\\
{x + 3y – 7 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – \frac{1}{5}}\\
{y = \frac{{12}}{5}}
\end{array}} \right..
$$

Suy ra hình chiếu của $A$ lên $d$ là $A’\left( { – \frac{1}{5};\frac{{12}}{5}} \right).$

## Bài 9: Cho tam giác $ABC$ biết $A(-4;6)$, $B(-1;2)$ và đường phân giác trong $CK$ có phương trình là $3x + 9y – 22 = 0.$ Tính toạ độ đỉnh $C$ của tam giác.

Qua $A$ kẻ đường thẳng vuông góc với $CK$ cắt $CK$ và $CB$ lần lượt tại ${A_1}$, ${A_2}.$

Đường thẳng ${A_1}{A_2}$ (hay ${A{A_2}}$) có phương trình là $3x – y + 18 = 0.$

Toạ độ điểm ${A_1}$ là nghiệm của hệ:

$$
\left\{ {\begin{array}{l}
{3x + 9y – 22 = 0}\\
{3x – y + 18 = 0}
\end{array}} \right.
$$
 $\Rightarrow {A_1}\left( { – \frac{{14}}{3};4} \right)$ $\Rightarrow {A_2}\left( { – \frac{{16}}{3};2} \right).$

Cạnh $BC$ (hay ${A_2}$) có phương trình là $y – 2 = 0.$

Toạ độ điểm $C$ là nghiệm của hệ 
$$
\left\{ {\begin{array}{c}
{3x + 9y – 22 = 0}\\
{y – 2 = 0}
\end{array}} \right.
$$
 $\Rightarrow C\left( {\frac{4}{3};2} \right).$