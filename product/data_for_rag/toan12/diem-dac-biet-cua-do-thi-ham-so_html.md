# Điểm đặc biệt của đồ thị hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
Bài viết hướng dẫn phương pháp giải một số dạng toán thường gặp liên quan đến điểm đặc biệt của đồ thị hàm số trong chương trình Giải tích 12.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Dạng 1. Điểm cố định của họ đồ thị hàm số.

1. Phương pháp

Định nghĩa:

Cho hàm số $y = f(x;m)$ ($m$ là tham số) có đồ thị $\left( {{C_m}} \right).$

Điểm $M\left( {{x_0};{y_0}} \right)$ được gọi là điểm cố định của đồ thị $\left( {{C_m}} \right)$ nếu $f\left( {{x_0};m} \right) = {y_0}$ với mọi giá trị của tham số $m.$

Cách xác định điểm cố định của đồ thị hàm số:

Bước 1: Biến đổi hàm số $y = f(x;m)$ về phương trình theo ẩn $m$ dạng:

${f_n}(x;y){m^n}$ $+ \ldots + {f_1}(x;y)m$ $+ {f_0}(x;y) = 0$ $(1).$

Bước 2: Phương trình $(1)$ nghiệm đúng với mọi $m \in R$ khi và chỉ khi:

$$
\left\{ {\begin{array}{l}
{{f_n}(x;y) = 0}\\
\cdots \\
{{f_1}(x;y) = 0}\\
{{f_0}(x;y) = 0}
\end{array}} \right.
$$
 $(I).$

Nghiệm $(x;y)$ của hệ phương trình $(I)$ là tọa độ điểm cố định của đồ thị $\left( {{C_m}} \right).$

Nếu hệ phương trình $(I)$ vô nghiệm thì đồ thị $\left( {{C_m}} \right)$ không có điểm cố định.

2. Ví dụ minh họa

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 1. Cho hàm số $y = m{x^3} + (2 – 3m)x + 2m – 1$ ($m$ là tham số) có đồ thị $\left( {{C_m}} \right).$ Tìm những điểm cố định mà $\left( {{C_m}} \right)$ luôn đi qua.

Biến đổi hàm số về phương trình theo ẩn $m$, ta được:

$y = m{x^3} + (2 – 3m)x + 2m – 1$ $\Leftrightarrow \left( {{x^3} – 3x + 2} \right)m + 2x – y – 1 = 0.$

Phương trình trên nghiệm đúng với mọi giá trị $m \in R$ khi và chỉ khi:

$$
\left\{ {\begin{array}{l}
{{x^3} – 3x + 2 = 0}\\
{2x – y – 1 = 0}
\end{array}} \right..
$$

Giải hệ phương trình trên, ta được nghiệm $(x;y)$ là $(1;1)$ và $(-2;-5).$

Vậy đồ thị hàm số $\left( {{C_m}} \right)$ luôn đi qua hai điểm cố định $A(1;1)$ và $B(-2;-5)$ với mọi giá trị của tham số $m.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 2. Cho hàm số $y = \frac{{mx + 2m – 1}}{{x + m}}$ ($m$ là tham số) có đồ thị $\left( {{C_m}} \right).$ Biết rằng $\left( {{C_m}} \right)$ luôn tiếp xúc với một đường thẳng cố định. Viết phương trình của đường thẳng đó.

Phân tích: Với bài toán này, ta có nhận định đường thẳng cố định tiếp xúc với đồ thị $\left( {{C_m}} \right)$ tại một điểm cố định. Ta sẽ đi tìm điểm cố định này và viết phương trình tiếp tuyến tại điểm đó để kiểm chứng.

Điều kiện: $x \ne – m.$

Biến đổi hàm số về phương trình theo ẩn $m$ ta được:

$y = \frac{{mx + 2m – 1}}{{x + m}}$ $\Leftrightarrow (x – y + 2)m – xy – 1 = 0.$

Phương trình trên nghiệm đúng với mọi giá trị $m$ khi và chỉ khi:

$$
\left\{ {\begin{array}{l}
{x – y + 2 = 0}\\
{ – xy – 1 = 0}
\end{array}} \right..
$$

Giải hệ phương trình trên ta được nghiệm $(x;y)$ là $(-1;1).$

Khi đó $\left( {{C_m}} \right)$ luôn đi qua điểm cố định $M(-1;1).$

Mặt khác $y’ = \frac{{{{(m – 1)}^2}}}{{{{(x + m)}^2}}}$ $\Rightarrow y'( – 1) = 1.$

Suy ra đường thẳng tiếp xúc với $\left( {{C_m}} \right)$ tại điểm $M$ có phương trình $y = (x + 1) + 1$ hay $y = x + 2.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Dạng 2. Điểm đối xứng của đồ thị hàm số.

1. Phương pháp

Cho hàm số $y = f(x)$ có đồ thị $(C).$

a) Hai điểm $A$, $B$ nằm trên đồ thị $(C)$ đối xứng nhau qua điểm $I(a;b)$ cho trước. 

Cách 1:

Bước 1: Giả sử A\left(x_{0} ; y_{0}\right) nằm trên đồ thị $(C)$, từ giả thiết $I$ là trung điểm của $AB$, ta có tọa độ điểm B\left(2 a-x_{0} ; 2 b-y_{0}\right)

Bước 2: Điểm $B$ nằm trên đồ thị $(C)$ nên ta có: $2b – {y_0} = f\left( {2a – {x_0}} \right).$

Giải hệ phương trình trên, ta tìm được $\left( {{x_0};{y_0}} \right).$

Từ đó xác định được tọa độ điểm $A$ và $B.$

Cách 2:

Giả sử $A\left( {{x_1};{y_1}} \right)$, $B\left( {{x_2};{y_2}} \right)$ nằm trên đồ thị $(C).$ Khi đó tọa độ $A$, $B$ thỏa mãn hệ phương trình: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = 2a}\\
{{y_1} + {y_2} = 2b}
\end{array}} \right..
$$

Giải hệ phương trình trên, kết hợp định lí Vi ét đảo, ta xác định được tọa độ điểm $A$ và $B.$

b) Hai điểm $A$, $B$ đối xứng nhau qua đường thẳng $\Delta :y = ax + b$ cho trước. 

Cách 1:

Bước 1: Gọi $d$ là đường thẳng vuông góc với $\Delta .$

Khi đó đường thẳng $d$ có phương trình: $y = – \frac{1}{a}x + m.$

Bước 2: Tìm điều kiện của $m$ để $d$ cắt $(C)$ tại hai điểm phân biệt ${x_1}$, ${x_2}.$ Khi đó $A\left( {{x_1};{y_1}} \right)$, $B\left( {{x_2};{y_2}} \right).$

Bước 3: Hai điểm $A$, $B$ đối xứng nhau qua $\Delta$ khi trung điểm của $AB$ nằm trên $\Delta$ hay $\frac{{{y_1} + {y_2}}}{2} = a\frac{{{x_1} + {x_2}}}{2} + b.$

Kết hợp định lí Vi ét và giải phương trình trên, ta tìm được tọa độ của $A$ và $B.$

Cách 2:

Giả sử $A$, $B$ nằm trên đồ thị $(C).$ Gọi $I$ là trung điểm của $AB.$

Khi đó $A$, $B$ đối xứng nhau qua $\Delta$ khi và chỉ khi $I \in \Delta$ và $AB \bot \Delta .$

Từ đó ta tìm được tọa độ của $A$ và $B.$

Lưu ý:

+ Đồ thị hàm số $(C):y = a{x^3} + b{x^2} + cx + d$ $(a \ne 0)$ có tâm đối xứng có hoành độ ${x_0}$ là nghiệm của phương trình $y” = 0.$ Khi đó điểm $A\left( {{x_0};{y_0}} \right) \in (C)$ được gọi là điểm uốn của đồ thị hàm số $(C).$

+ Đồ thị hàm số $y = \frac{{ax + b}}{{cx + d}}$ nhận giao điểm của hai đường tiệm cận làm tâm đối xứng.

2. Ví dụ minh họa

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 3. Cho hàm số $y = {x^3} – 3x – 2$ có đồ thị $(C).$ Tìm hai điểm $M$, $N$ nằm trên $(C)$ đối xứng nhau qua điểm $A(1;-1).$

Giả sử $M\left( {{x_0};x_0^3 – 3x – 2} \right) \in (C).$ Suy ra $N\left( {2 – {x_0}; – x_0^3 + 3{x_0}} \right).$

Ta có $N \in (C)$ nên $– x_0^3 + 3{x_0}$ $= {\left( {2 – {x_0}} \right)^3} – 3\left( {2 – {x_0}} \right) – 2.$

Giải phương trình trên, ta được hai nghiệm ${x_0} = 0$ hoặc ${x_0} = 2.$

Với ${x_0} = 0$ ta có $M(0;2)$, $N(2;4).$

Với ${x_0} = 2$ ta có $M(2;4)$, $N(0;2).$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 4. Cho hàm số $y = \frac{{2x – 1}}{{x + 1}}$ có đồ thị $(C).$ Tìm hai điểm nằm trên $(C)$ đối xứng nhau qua đường thẳng $d:y = 3x + 5.$

Gọi $\Delta$ là đường thẳng vuông góc với $d.$ Khi đó $\Delta$ có phương trình: $y = – \frac{1}{3}x + a.$

Xét phương trình hoành độ giao điểm của $\Delta$ và $(C):$

$\frac{{2x – 1}}{{x + 1}} = – \frac{1}{3}x + a$ $\Leftrightarrow {x^2} + (7 – 3a)x – 3 – 3a = 0$ $(x \ne – 1)$ $(1).$

$\Delta$ cắt $(C)$ tại hai điểm phân biệt khi $(1)$ có hai nghiệm phân biệt khác $-1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta = {{(7 – 3a)}^2} + 12(1 + a) > 0}\\
{1 – (7 – 3a) – 3 – 3a \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow 9{a^2} – 30a + 61 > 0$ đúng với mọi $a.$

Khi đó $\Delta$ cắt $(C)$ tại hai điểm $A$, $B$ có hoành độ lần lượt là ${x_1}$, ${x_2}$ là nghiệm của phương trình $(1).$

Gọi $I$ là trung điểm của $AB$, ta có:

$I\left( {\frac{{{x_1} + {x_2}}}{2}; – \frac{{{x_1} + {x_2}}}{6} + a} \right)$ hay $I\left( {\frac{{3a – 7}}{2};\frac{{3a + 7}}{6}} \right).$

Mặt khác $I \in d$ nên $\frac{{3a + 7}}{6} = \frac{{3(3a – 7)}}{2} + 5$ $\Leftrightarrow a = \frac{5}{3}.$

Suy ra $(1)$ trở thành: ${x^2} + 2x – 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2 \Rightarrow y = 1}\\
{x = – 4 \Rightarrow y = 3}
\end{array}} \right..
$$

Vậy $A(2;1)$ và $B(-4;3).$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 5. Cho hàm số $y = {x^3} – (m – 2){x^2} + 2m – 1$ có đồ thị $(C).$ Tìm tất cả các giá trị của tham số $m$ để trên $\left( {{C_m}} \right)$ tồn tại một cặp điểm đối xứng nhau qua gốc tọa độ $O.$

Gọi $A\left( {{x_0};{y_0}} \right) \in \left( {{C_m}} \right)$ với ${y_0} = x_0^3 – (m – 2)x_0^2 + 2m – 1.$

Khi đó $B\left( { – {x_0}; – {y_0}} \right)$ là điểm đối xứng của $A$ qua $I.$

Ta có $B \in \left( {{C_m}} \right)$ $\Leftrightarrow – {y_0} = – x_0^3 – (m – 2)x_0^2 + 2m – 1.$

$\Leftrightarrow – \left[ {x_0^3 – (m – 2)x_0^2 + 2m – 1} \right]$ $= – x_0^3 – (m – 2)x_0^2 + 2m – 1.$

$\Leftrightarrow (m – 2)x_0^2 – 2m + 1 = 0$ $(1).$

$\left( {{C_m}} \right)$ tồn tại cặp điểm đối xứng $A$, $B$ khi phương trình $(1)$ có nghiệm khác $0.$

Với $m = 2$, phương trình $(1)$ vô nghiệm.

Với $m \ne 2$, phương trình $(1)$ có nghiệm khác $0$ khi và chỉ khi:

$(m – 2)( – 2m + 1) < 0$ $\Leftrightarrow m < \frac{1}{2}$ hoặc $m > 2.$

Vậy tập hợp các giá trị $m$ cần tìm là $m \in \left( { – \infty ;\frac{1}{2}} \right) \cup (2; + \infty ).$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 6. Cho hàm số $y = 3{x^3} – {m^2}x – m + 2$ có đồ thị $\left( {{C_m}} \right).$ Tìm tất cả các giá trị của tham số $m$ để $\left( {{C_m}} \right)$ có hai điểm cực trị đối xứng nhau qua đường thẳng $\Delta :y = x + 2.$

Ta có $y’ = 9{x^2} – {m^2}.$ Suy ra $y’ = 0$ $\Leftrightarrow 9{x^2} – {m^2} = 0.$

$\left( {{C_m}} \right)$ có hai điểm cực trị khi và chỉ khi $m \ne 0.$

Khi đó $\left( {{C_m}} \right)$ có hai điểm cực trị $A\left( { – \frac{m}{3};\frac{2}{9}{m^3} – m + 2} \right)$ và $B\left( {\frac{m}{3}; – \frac{2}{9}{m^3} – m + 2} \right).$

Ta có $\overrightarrow {AB} = \left( {\frac{{2m}}{3}; – \frac{{4{m^3}}}{9}} \right)$ và $I(0;2 – m)$ là trung điểm của $AB.$

$\Delta$ có vectơ chỉ phương $\overrightarrow u = (1;1).$

$A$, $B$ đối xứng nhau qua $\Delta$ khi và chỉ khi:

$$
\left\{ {\begin{array}{l}
{\overrightarrow {AB} .\vec u = 0}\\
{I \in \Delta }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{2m}}{3} – \frac{{4{m^3}}}{9} = 0}\\
{2 – m = 2}
\end{array}} \right.
$$
 $\Leftrightarrow m = 0.$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Dạng 3. Điểm có tọa độ nguyên.

1. Phương pháp

Cho đồ thị hàm số phân thức $(C):y = \frac{{f(x)}}{{g(x)}}$ trong đó $f(x)$, $g(x)$ là đa thức.

Bước 1: Biến đổi $(C):y = \frac{{f(x)}}{{g(x)}}$ về dạng $y = h(x) + \frac{c}{{g(x)}}$ trong đó $h(x)$ là đa thức, $c$ là hằng số.

Bước 2: Tìm các giá trị của ${x_0}$ sao cho $g(x)$ là ước của $c.$

Khi đó $A\left( {{x_0};\frac{{f\left( {{x_0}} \right)}}{{g\left( {{x_0}} \right)}}} \right)$ là điểm có tọa độ nguyên cần tìm.

2. Ví dụ minh họa

<!-- chunk:10 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 7. Tìm trên đồ thị hàm số $(C):y = \frac{{2x – 1}}{{x + 2}}$ các điểm có tọa độ nguyên.

Giả sử $A\left( {{x_0};\frac{{2{x_0} – 1}}{{{x_0} + 2}}} \right) \in (C).$

Biến đổi hàm số $y = \frac{{2x – 1}}{{x + 2}}$ $= 2 – \frac{5}{{x + 2}}.$

Khi đó $A$ có tọa độ nguyên khi ${x_0} + 2 \in \{ – 5; – 1;1;5\}$ hay ${x_0} \in \{ – 7; – 3; – 1;3\} .$

Vậy có bốn điểm trên đồ thị hàm số $(C)$ có tọa độ nguyên là:

$A(-7;3)$, $B(-3;7)$, $C (-1;-3)$, $D(3;1).$

<!-- chunk:11 level:2 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Dạng 4. Điểm thuộc đồ thị hàm số thỏa điều kiện cho trước.

1. Phương pháp

Dựa vào điều kiện cho trước, ta đi tìm mối liên hệ với bài toán để tìm ra kết quả.

Lưu ý: Một số điều kiện cho trước thường gặp:

a) Khoảng cách giữa hai điểm: Giả sử $A\left( {{x_1};{y_1}} \right)$, $B\left( {{x_2};{y_2}} \right).$

Khi đó độ dài đoạn $AB$ là: $AB = \sqrt {{{\left( {{x_2} – {x_1}} \right)}^2} + {{\left( {{y_2} – {y_1}} \right)}^2}} .$

b) Khoảng cách từ một điểm đến một đường thẳng:

Cho điểm $M\left( {{x_0};{y_0}} \right)$ và đường thẳng $\Delta :ax + by + c = 0.$

Khi đó khoảng cách từ điểm $M$ đến $\Delta$ là: $d(M;\Delta ) = \frac{{\left| {a{x_0} + b{y_0} + c} \right|}}{{\sqrt {{a^2} + {b^2}} }}.$

Đặc biệt:

+ Với $\Delta 😡 – a = 0$ ta có $d(M;\Delta ) = \left| {{x_0} – a} \right|.$

+ Với $\Delta :y – b = 0$ ta có $d(M;\Delta ) = \left| {{y_0} – b} \right|.$

c) Diện tích của tam giác: Cho tam giác $ABC$ có các cạnh có độ dài như hình vẽ.

<img link="data_for_rag/toan12/images/diem-dac-biet-cua-do-thi-ham-so-1.png" alt="">

Khi đó $S = \frac{1}{2}a{h_a} = \frac{1}{2}ab\sin C$ $= \sqrt {p(p – a)(p – b)(p – c)}$ (với $P$ là nửa chu vi của tam giác).

2. Ví dụ minh họa

<!-- chunk:12 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 8. Cho hàm số $y = \frac{{x – 2}}{{x + 1}}$ có đồ thị $(C).$ Tìm tọa độ điểm $M$ nằm trên $(C)$ sao cho khoảng cách từ $M$ đến đường thẳng $y = -x$ bằng $\sqrt 2 .$

Giả sử $M\left( {{x_0};\frac{{{x_0} – 2}}{{{x_0} + 1}}} \right)$ nằm trên $(C)$, ${x_0} \ne – 1.$

Đường thẳng $\Delta :y = – x$ hay $\Delta 😡 + y = 0.$

Theo giả thiết $d(M;\Delta ) = \frac{{\left| {{x_0} + \frac{{{x_0} – 2}}{{{x_0} + 1}}} \right|}}{{\sqrt 2 }} = \sqrt 2$ $\Leftrightarrow \left| {\frac{{x_0^2 + 2{x_0} – 2}}{{{x_0} + 1}}} \right| = 2.$

Giải phương trình trên ta được ${x_0} \in \{ – 4; – 2;0;2\} .$

Vậy có bốn điểm nằm trên $(C)$ thỏa yêu cầu bài toán là ${M_1}( – 4;2)$, ${M_2}( – 2;4)$, ${M_3}(0; – 2)$ ${M_4}(2;0).$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 9. Cho hàm số $y = \frac{{x + 2}}{{2x – 1}}$ có đồ thị $(C).$ Tìm những điểm nằm trên đồ thị $(C)$ cách đều hai điểm $A(1;-3)$ và $B(-1;3).$

Cách 1: Giả sử $M\left( {{x_0};\frac{{{x_0} + 2}}{{2{x_0} – 1}}} \right)$ nằm trên $(C)$, ${x_0} \ne \frac{1}{2}.$

Ta có $AM = \sqrt {{{\left( {{x_0} – 1} \right)}^2} + {{\left( {\frac{{7{x_0} – 1}}{{2{x_0} – 1}}} \right)}^2}}$, $BM = \sqrt {{{\left( {{x_0} + 1} \right)}^2} + {{\left( {\frac{{ – 5{x_0} + 5}}{{2{x_0} – 1}}} \right)}^2}} .$

Theo giả thiết ta suy ra ${\left( {{x_0} – 1} \right)^2} + {\left( {\frac{{7{x_0} – 1}}{{2{x_0} – 1}}} \right)^2}$ $= {\left( {{x_0} + 1} \right)^2} + {\left( {\frac{{ – 5{x_0} + 5}}{{2{x_0} – 1}}} \right)^2}.$

Giải phương trình trên, ta được các nghiệm ${x_0} = 3$ hoặc ${x_0} = – 1$ (nghiệm ${x_0} = \frac{1}{2}$ bị loại).

Vậy có hai điểm nằm trên $(C)$ thỏa yêu cầu bài toán là ${M_1}(3;1)$ và ${M_2}\left( { – 1; – \frac{1}{3}} \right).$

Cách 2:

Nhận xét: Điểm $M$ cách đều hai điểm $A$, $B$ nên $M$ nằm trên đường trung trực $\Delta$ của đoạn $AB.$ Ta xác định giao điểm của $\Delta$ với đồ thị hàm số để tìm ra điểm thỏa yêu cầu bài toán.

Gọi $\Delta$ là đường trung trực của đoạn $AB.$

Khi đó: $\Delta 😡 – 3y = 0$ hay $\Delta :y = \frac{1}{3}x.$

Phương trình hoành độ giao điểm của $\Delta$ và $(C)$ là: $\frac{1}{3}x = \frac{{x + 2}}{{2x – 1}}.$

Giải phương trình trên, ta được các nghiệm $x = 3$ hoặc $x = -1.$

Vậy có hai điểm nằm trên $(C)$ thỏa yêu cầu bài toán là ${M_1}(3;1)$ và ${M_2}\left( { – 1; – \frac{1}{3}} \right).$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## Ví dụ 10. Cho hàm số $y = {x^3} – 3x – 2$ có đồ thị $(C).$ Gọi $A$, $B$ lần lượt là hai điểm cực trị của đồ thị $(C).$ Tìm điểm $M$ nằm trên đồ thị $(C)$ sao cho tam giác $MAB$ có diện tích bằng $6.$

Ta có $y’ = 3{x^2} – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1 \Rightarrow y = – 4}\\
{x = – 1 \Rightarrow y = 0}
\end{array}} \right..
$$

Do đó $A(1;-4)$, $B(-1;0).$

Suy ra $AB = 2\sqrt 5$ và $AB:2x + y + 2 = 0.$

Giả sử $M\left( {{x_0};x_0^3 – 3{x_0} + 1} \right).$

Khi đó $d(M;AB)$ $= \frac{{\left| {2{x_0} + x_0^3 – 3{x_0} – 2 + 2} \right|}}{{\sqrt 5 }}$ $= \frac{{\left| {x_0^3 – {x_0}} \right|}}{{\sqrt 5 }}.$

Diện tích tam giác $MAB$ là: ${S_{\Delta MAB}} = \frac{1}{2}AB.d(M;AB)$ $= \left| {x_0^3 – {x_0}} \right| = 6.$

Giải phương trình trên, ta được các nghiệm ${x_0} = 2$ hoặc ${x_0} = – 2.$

Vậy có hai điểm nằm trên $(C)$ thỏa yêu cầu bài toán là ${M_1}(2;0)$ và ${M_2}( – 2; – 4).$

<!-- chunk:15 level:1 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## II. BÀI TẬP TRẮC NGHIỆM

## Bài 1. Đồ thị của hàm số $y = (m – 1)x + 3 – m$ với $m$ là tham số luôn đi qua một điểm cố định. Xác định tọa độ của điểm đó.

A. $M(0;3).$

B. $N(1;2).$

C. $P( – 1; – 2).$

D. $Q(2;0).$

Ta có $y = (m – 1)x + 3 – m$ $\Leftrightarrow (x – 1)m – x – y + 3 = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{x – 1 = 0}\\
{x + y – 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 1}\\
{y = 2}
\end{array}} \right..
$$

Suy ra $N(1;2)$ là điểm cố định của đồ thị hàm số.

> **Đáp án: B**

## Bài 2. Đồ thị của hàm số $y = {x^2} + 2mx – m + 1$ với $m$ là tham số luôn đi qua một điểm $M(a;b)$ cố định. Tính giá trị của $a + b.$

A. $1.$

B. $\frac{3}{2}.$

C. $\frac{7}{4}.$

D. $– \frac{3}{2}.$

Ta có $y = {x^2} + 2mx – m + 1$ $\Leftrightarrow (2x – 1)m + {x^2} – y + 1 = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{2x – 1 = 0}\\
{{x^2} – y + 1 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{1}{2}}\\
{y = \frac{5}{4}}
\end{array}} \right..
$$

Suy ra $M\left( {\frac{1}{2};\frac{5}{4}} \right)$ là điểm cố định của đồ thị hàm số. Khi đó $\frac{1}{2} + \frac{5}{4} = \frac{7}{4}.$

> **Đáp án: C**

## Bài 3. Đồ thị của hàm số $y = {x^3} – 3{x^2} + mx + m$ với $m$ là tham số luôn đi qua một điểm $M$ cố định. Tính độ dài của đoạn $OM$ với $O$ là gốc tọa độ.

A. $\sqrt 5$.

B. $\sqrt {10}$.

C. $\sqrt {13}$.

D. $\sqrt {17}$.

Ta có $y = {x^3} – 3{x^2} + mx + m$ $\Leftrightarrow (x + 1)m + {x^3} – 3{x^2} – y = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{x + 1 = 0}\\
{{x^3} – 3{x^2} – y = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – 1}\\
{y = – 4}
\end{array}} \right..
$$

Suy ra $M(-1;-4)$ là điểm cố định của đồ thị hàm số.

Khi đó $OM = \sqrt {17} .$

> **Đáp án: D**

## Bài 4. Đồ thị của hàm số $y = {x^4} – 2m{x^2} + 3$ luôn đi qua một điểm $M$ cố định. Xác định tọa độ của điểm $M.$

A. $M(-1;1).$

B. $M(1;4).$

C. $M(0;-2).$

D. $M(0;3).$

Ta có $y = {x^4} – 2m{x^2} + 3$ $\Leftrightarrow 2{x^2}m – {x^4} + y – 3 = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{2{x^2} = 0}\\
{{x^4} – y + 3 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 3}
\end{array}} \right..
$$

Suy ra $M(0;3)$ là điểm cố định của đồ thị hàm số.

> **Đáp án: D**

## Bài 5. Đồ thị của hàm số $y = \frac{{x – m}}{{x + m}}$ với $m$ là tham số $(m \ne 0)$ luôn đi qua một điểm $M$ cố định. Tính khoảng cách từ $M$ đến đường tiệm cận ngang của đồ thị hàm số.

A. $d = 1.$

B. $d = 2.$

C. $d = 3.$

D. $d = 4.$

Đồ thị hàm số có đường tiệm cận ngang $\Delta :y – 1 = 0.$

Ta có $y = \frac{{x – m}}{{x + m}}$ $\Leftrightarrow (y + 1)m + xy – x = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{y + 1 = 0}\\
{xy – x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = – 1}
\end{array}} \right..
$$

Suy ra $M(0;-1)$ là điểm cố định của đồ thị hàm số.

Khi đó $d(M;\Delta ) = | – 1 – 1| = 2.$

> **Đáp án: B**

## Bài 6. Đồ thị của hàm số $y = {x^3} – 3m{x^2} – x + 3m$ với $m$ là tham số đi qua bao nhiêu điểm cố định?

A. $1.$

B. $2.$

C. $3.$

D. $4.$

Ta có $y = {x^3} – 3m{x^2} – x + 3m$ $\Leftrightarrow \left( {3{x^2} – 3} \right)m + y – {x^3} + x = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{3{x^2} – 3 = 0}\\
{y – {x^3} + x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 1}\\
{y = 0}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{l}
{x = – 1}\\
{y = 0}
\end{array}} \right..
$$
 Đồ thị hàm số có hai điểm cố định.

> **Đáp án: B**

## Bài 7. Đồ thị của hàm số $y = (1 – 2m){x^4} + 3m{x^2} – m – 1$ với $m$ là tham số đi qua bao nhiêu điểm cố định?

A. $4.$

B. $3.$

C. $2.$

D. $1.$

Ta có $y = (1 – 2m){x^4} + 3m{x^2} – m – 1$ $\Leftrightarrow \left( {2{x^4} – 3{x^2} + 1} \right)m + y – {x^4} + 1 = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{2{x^4} – 3{x^2} + 1 = 0\:\:(1)}\\
{y – {x^4} + 1 = 0}
\end{array}} \right..
$$

Phương trình $(1)$ có bốn nghiệm phân biệt nên hệ có bốn nghiệm $(x;y).$

Đồ thị hàm số có bốn điểm cố định.

> **Đáp án: A**

## Bài 8. Đồ thị của hàm số $y = \frac{{2{x^2} + (1 – m)x + 1 + m}}{{m – x}}$ với $m$ là tham số $(m \ne – 2)$ luôn đi qua một điểm $M(a;b)$ cố định. Tính giá trị của $a + b.$

A. $-1.$

B. $-3.$

C. $1.$

D. $-2.$

Ta có $y = \frac{{2{x^2} + (1 – m)x + 1 + m}}{{m – x}}$ $\Leftrightarrow (x + y – 1)m$ $– 2{x^2} – x – xy – 1 = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{x + y – 1 = 0}\\
{2{x^2} + x + xy + 1 = 0}
\end{array}} \right..
$$

Giải hệ phương trình trên ta được nghiệm $(x;y)$ là $(-1;2).$

Do đó $M(-1;2)$ suy ra $a + b = -1 + 2 = 1.$

> **Đáp án: C**

## Bài 9. Cho hàm số $y = – {x^3} + m{x^2} – x – 4m$ có đồ thị $\left( {{C_m}} \right)$ và $A$ là điểm cố định có hoành độ âm nằm trên đồ thị $\left( {{C_m}} \right).$ Tìm các giá trị của $m$ để tiếp tuyến tại $A$ của đồ thị $\left( {{C_m}} \right)$ vuông góc với đường thẳng $x – y = 0.$

A. $m = -3.$

B. $m = -6.$

C. $m = 2.$

D. $m = – \frac{7}{2}.$

Ta có $y = – {x^3} + m{x^2} – x – 4m$ $\Leftrightarrow \left( {{x^2} – 4} \right)m – {x^3} – x – y = 0.$

Phương trình nghiệm đúng với mọi $m$ khi 
$$
\left\{ {\begin{array}{l}
{{x^2} – 4 = 0}\\
{ – {x^3} – x – y = 0}
\end{array}} \right..
$$

Giải hệ phương trình trên ta được các nghiệm $(x;y)$ là $(2;-10)$ hoặc $( – 2;10).$

Do đó $A( – 2;10).$

Ta có $y’ = – 3{x^2} + 2mx – 1$, $y'( – 2) = – 4m – 13.$

Tiếp tuyến tại $A$ của đồ thị $\left( {{C_m}} \right)$ vuông góc với đường thẳng $x – y = 0$ nên:

$y'(2) = – 1$ $\Leftrightarrow – 4m – 13 = – 1$ $\Leftrightarrow m = – 3.$

> **Đáp án: A**

## Bài 10. Cho hàm số $y = {x^3} – 3{x^2} + 2$ có đồ thị $(C).$ Có bao nhiêu cặp điểm $M$, $N$ nằm trên $(C)$ đối xứng nhau qua điểm $I(1;0)$?

A. $0.$

B. $1.$

C. $2.$

<!-- chunk:16 level:1 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## D. Vô số.

Ta có $y’ = 3{x^2} – 6x$, $y” = 6x – 6$, $y” = 0$ $\Leftrightarrow x = 1$ $\Rightarrow y = 0.$

Do đó $I(1;0)$ là tâm đối xứng của $(C).$

> **Đáp án: D**

## Bài 11. Cho hàm số $y = {x^3} – x + 1$ có đồ thị $(C).$ Có bao nhiêu cặp điểm $M$, $N$ nằm trên $(C)$ đối xứng nhau qua điểm $I(1;-1)$?

A. $0.$

B. $1.$

C. $2.$

<!-- chunk:17 level:1 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## D. Vô số.

Giả sử $M\left( {{x_0};x_0^3 – {x_0} + 1} \right) \in (C).$

Khi đó $N\left( {2 – {x_0}; – x_0^3 + {x_0} – 3} \right).$

Ta có $N \in (C)$ nên $– x_0^3 + {x_0} – 3$ $= {\left( {2 – {x_0}} \right)^3} – \left( {2 – {x_0}} \right) + 1$ $\Leftrightarrow 3x_0^2 – 6{x_0} + 5 = 0$ (vô nghiệm).

> **Đáp án: A**

## Bài 12. Cho hàm số $y = \frac{{2x – 1}}{{x – 1}}$ có đồ thị $(C).$ Có bao nhiêu cặp điểm $M$, $N$ nằm trên $(C)$ đối xứng nhau qua điểm $I(1;2)$?

A. $0.$

B. $1.$

C. $2.$

<!-- chunk:18 level:1 source:https://toanmath.com/2019/11/diem-dac-biet-cua-do-thi-ham-so.html -->
## D. Vô số.

Ta có $I(1;2)$ là giao điểm của hai đường tiệm cận của $(C).$

> **Đáp án: D**

## Bài 13. Cho hàm số $y = \frac{{x – 3}}{{x + 2}}$ có đồ thị $(C).$ Biết $A$, $B$ là hai điểm nằm trên $(C)$ đối xứng nhau qua điểm $I(1;-2).$ Tính độ dài đoạn $AB.$

A. $3\sqrt 2$.

B. $4\sqrt 2$.

C. $3\sqrt 3$.

D. $4\sqrt 3 .$

Giả sử $A\left( {{x_0};\frac{{{x_0} – 3}}{{{x_0} + 2}}} \right) \in (C).$ Khi đó $B\left( {2 – {x_0}; – 4 – \frac{{{x_0} – 3}}{{{x_0} + 2}}} \right).$

Ta có $B \in (C)$ nên $– 4 – \frac{{{x_0} – 3}}{{{x_0} + 2}} = \frac{{2 – {x_0} – 3}}{{2 – {x_0} + 2}}$ $\Leftrightarrow x_0^2 – 2{x_0} – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_0} = – 1}\\
{{x_0} = 3}
\end{array}} \right..
$$

Với ${x_0} = – 1$ ta có $A( – 1; – 4)$, $B(3;0)$ $\Rightarrow AB = 4\sqrt 2 .$

Với ${x_0} = 3$ ta có $A(3;0)$, $B( – 1; – 4)$ $\Rightarrow AB = 4\sqrt 2 .$

> **Đáp án: B**

## Bài 14. Cho hàm số $y = \frac{{{x^2} + x + 2}}{{x + 1}}$ có đồ thị $(C).$ Giả sử $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$ là hai điểm nằm trên $(C)$ đối xứng nhau qua điểm $I\left( { – \frac{1}{2}; – 1} \right).$ Tính giá trị của ${x_A}{x_B} + {y_A}{y_B}.$

A. $-6.$

B. $6.$

C. $-10.$

D. $10.$

Với $A\left( {{x_A};{y_A}} \right) \in (C)$ ta có ${y_A} = \frac{{x_A^2 + {x_A} + 2}}{{{x_A} + 1}}.$

Suy ra $B\left( { – 1 – {x_A}; – 2 – \frac{{x_A^2 + {x_A} + 2}}{{{x_A} + 1}}} \right).$

$B \in (C)$ nên $– 2 – \frac{{x_A^2 + {x_A} + 2}}{{{x_A} + 1}}$ $= \frac{{{{\left( { – 1 – {x_A}} \right)}^2} + \left( { – 1 – {x_A}} \right) + 2}}{{\left( { – 1 – {x_A}} \right) + 1}}.$

$\Leftrightarrow x_A^2 + {x_A} – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_A} = 1}\\
{{x_A} = – 2}
\end{array}} \right..
$$

Với ${x_A} = 1$ ta có $A(1;2)$, $B( – 2; – 4)$ $\Rightarrow {x_A}{x_B} + {y_A}{y_B} = – 10.$

Với ${x_A} = – 2$ ta có $A( – 2; – 4)$, $B(1;2)$ $\Rightarrow {x_A}{x_B} + {y_A}{y_B} = – 10.$

> **Đáp án: C**

## Bài 15. Cho hàm số $y = \frac{{x + 1}}{{x – 1}}$ có đồ thị $(C).$ Gọi $M$, $N$ là hai điểm nằm trên $(C)$ đối xứng nhau qua đường thẳng $y = 3 – 2x.$ Tính độ dài đoạn $MN.$

A. $\sqrt {10}$.

B. ${2\sqrt {10} }$.

C. ${4\sqrt 5 }$.

D. $5$.

Đường thẳng $\Delta$ vuông góc với đường thẳng $y = 1 – x$ có dạng $y = 2x + m.$

Hoành độ giao điểm của $(C)$ và $\Delta$ là nghiệm của phương trình:

$\frac{{x + 1}}{{x – 1}} = 2x + m$ hay $2{x^2} + (m – 3)x – m – 1 = 0$ $(*).$

$\Delta$ cắt $(C)$ tại hai điểm phân biệt khi và chỉ khi:

${(m – 3)^2} + 4.2(m + 1) > 0$ $\Leftrightarrow {m^2} + 2m + 17 > 0$ với mọi $m.$

Khi đó $\Delta$ cắt $(C)$ tại hai điểm phân biệt $M\left( {{x_1};2{x_1} + m} \right)$, $N\left( {{x_2};2{x_2} + m} \right).$

Suy ra $I\left( {\frac{{{x_1} + {x_2}}}{2};{x_1} + {x_2} + m} \right)$ là trung điểm của $MN.$

Mặt khác $M$, $N$ đối xứng nhau qua đường thẳng $y = 3 – 2x$ nên:

${x_1} + {x_2} + m = 3 – \left( {{x_1} + {x_2}} \right).$

$\Leftrightarrow 2\left( {{x_1} + {x_2}} \right) + m – 3 = 0.$

$\Leftrightarrow 2( – m + 3) + m – 3 = 0$ (theo định lí Vi-ét ${x_1} + {x_2} = – m + 3$).

$\Leftrightarrow m = 3.$

Khi đó $(*)$ trở thành $2{x^2} – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \sqrt 2 }\\
{x = – \sqrt 2 }
\end{array}} \right..
$$

Suy ra $M(\sqrt 2 ;3 + 2\sqrt 2 )$, $N( – \sqrt 2 ;3 – 2\sqrt 2 ).$

Do đó $MN = 2\sqrt {10} .$

> **Đáp án: B**

## Bài 16. Cho hàm số $y = \frac{{{x^2} + 2}}{{x – 1}}$ có đồ thị $(C).$ Gọi $M$, $N$ là hai điểm phân biệt nằm trên $(C)$ đối xứng nhau qua đường thẳng $x + 2y – 4 = 0.$ Tính diện tích tam giác $OMN.$

A. $2.$

B. $2\sqrt 5$.

C. $4.$

D. $4\sqrt 5$.

Gọi $\Delta$ là đường thẳng đi qua hai điểm $M$, $N.$

$\Delta$ vuông góc với đường thẳng $x + 2y + 4 = 0$ nên có dạng:

$2x – y + m = 0$ hay $y = 2x + m.$

Phương trình hoành độ giao điểm của $\Delta$ và $(C):$

$2x + m = \frac{{{x^2} + 2}}{{x – 1}}$ $\Leftrightarrow {x^2} + (m – 2)x – m – 2 = 0$ $(x \ne 1)$ $(*).$

$\Delta$ cắt $(C)$ tại hai điểm phân biệt khi $(*)$ có hai nghiệm phân biệt khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{(m – 2)}^2} + 4(m + 2) > 0}\\
{1 + m – 2 – m – 2 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow {m^2} + 12 > 0$ thỏa với mọi giá trị $m \in R.$

Khi đó $M\left( {{x_1};2{x_1} + m} \right)$, $N\left( {{x_2};2{x_2} + m} \right).$

Suy ra $I\left( {\frac{{{x_1} + {x_2}}}{2};{x_1} + {x_2} + m} \right)$ hay $I\left( {\frac{{2 – m}}{2};2} \right)$ là trung điểm của $MN.$

Ta có $I$ nằm trên đường thẳng $x + 2y – 4 = 0$ nên $\frac{{2 – m}}{2} + 2.2 – 4 = 0$ $\Leftrightarrow m = 2.$

Khi đó $(*)$ trở thành ${x^2} – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 2 \Rightarrow y = 6}\\
{x = – 2 \Rightarrow y = – 2}
\end{array}} \right..
$$

Khi đó $M(2;6)$, $N( – 2; – 2)$ $\Rightarrow MN = 4\sqrt 5$, $d(O;\Delta ) = \frac{2}{{\sqrt 5 }}.$

Vậy ${S_{\Delta OMN}} = \frac{1}{2}d(O;\Delta ).MN$ $= \frac{1}{2}.\frac{2}{{\sqrt 5 }}.4\sqrt 5 = 4.$

> **Đáp án: C**

## Bài 17. Đồ thị hàm số $y = \frac{2}{{x + 2}}$ có bao nhiêu điểm có tọa độ nguyên?

A. $4.$

B. $3.$

C. $2.$

D. $1.$

Giả sử $M\left( {{x_0};\frac{2}{{{x_0} + 2}}} \right)$ điểm nằm trên đồ thị hàm số.

Khi đó $M$ có tọa độ nguyên khi ${x_0}$ nguyên và $\frac{2}{{{x_0} + 2}}$ nguyên.

Suy ra ${x_0} + 2 \in \{ – 2; – 1;1;2\}$ hay ${x_0} \in \{ – 4; – 3; – 1;0\} .$

Vậy có bốn điểm thỏa mãn yêu cầu bài toán.

> **Đáp án: A**

## Bài 18. Đồ thị hàm số $y = \frac{3}{{2x – 1}}$ có bao nhiêu điểm có tọa độ nguyên dương?

A. $1.$

B. $2.$

C. $3.$

D. $4.$

Giả sử $M\left( {{x_0};\frac{3}{{2{x_0} – 1}}} \right)$ điểm nằm trên đồ thị hàm số.

Khi đó $M$ có tọa độ nguyên dương khi ${x_0}$ nguyên dương và $\frac{3}{{2{x_0} – 1}}$ nguyên dương. Suy ra $2{x_0} – 1 \in \{ 1;3\}$ hay ${x_0} \in \{ 1;2\} .$

Vậy có hai điểm thỏa mãn yêu cầu bài toán.

> **Đáp án: B**

## Bài 19. Đồ thị hàm số $y = \frac{4}{{3x – 2}}$ có bao nhiêu điểm có tọa độ nguyên?

A. $1.$

B. $2.$

C. $3.$

D. $6.$

Giả sử $M\left( {{x_0};\frac{4}{{3{x_0} – 2}}} \right)$ điểm nằm trên đồ thị hàm số.

Khi đó $M$ có tọa độ nguyên khi ${x_0}$ nguyên và $\frac{4}{{3{x_0} – 2}}$ nguyên.

Suy ra $3{x_0} – 2 \in \{ – 4; – 2; – 1;1;2;4\}$ hay ${x_0} \in \left\{ { – \frac{2}{3};0;\frac{1}{3};1;\frac{4}{3};2} \right\}.$

Suy ra ${x_0} \in \{ 0;1;2\} .$

Vậy có ba điểm thỏa mãn yêu cầu bài toán.

> **Đáp án: C**

## Bài 20. Đồ thị hàm số $y = \frac{{x + 10}}{{x + 1}}$ có bao nhiêu điểm có tọa độ nguyên?

A. $2.$

B. $4.$

C. $6.$

D. $7.$

Ta có $y = \frac{{x + 10}}{{x + 1}} = 1 + \frac{9}{{x + 1}}.$

Giả sử $M\left( {{x_0};1 + \frac{9}{{{x_0} + 1}}} \right)$ điểm nằm trên đồ thị hàm số.

Khi đó $M$ có tọa độ nguyên khi ${x_0}$ nguyên và $\frac{9}{{{x_0} + 1}}$ nguyên.

Suy ra ${x_0} + 1 \in \{ – 9; – 3; – 1;1;3;9\}$ hay ${x_0} \in \{ – 10; – 4; – 2;0;2;8\} .$

Vậy có sáu điểm thỏa mãn yêu cầu bài toán.

> **Đáp án: C**

## Bài 21. Giả sử $S$ là tập hợp các đường thẳng cắt đồ thị $(C)$ của hàm số $y = \frac{{x + 2}}{{2x – 1}}$ tại hai điểm có tọa độ nguyên. Tính số phần tử của $S.$

A. $4.$

B. $3.$

C. $5.$

D. $6.$

Ta có: $y = \frac{{x + 2}}{{2x – 1}}$ $= \frac{1}{2} + \frac{5}{{2(2x – 1)}}$ $= \frac{1}{2}\left( {1 + \frac{5}{{2x – 1}}} \right).$

Khi đó điểm $M$ có tọa độ nguyên khi ${x_0}$ nguyên và $\frac{1}{2}\left( {1 + \frac{5}{{2{x_0} – 1}}} \right)$ nguyên.

Suy ra $2{x_0} – 1 \in \{ – 5; – 1;1;5\}$ hay ${x_0} \in \{ – 2;0;1;3\} .$

Kiểm tra lại:

${x_0} = – 2$ $\Rightarrow {y_0} = 0$ thỏa mãn.

${x_0} = 0$ $\Rightarrow {y_0} = – 2$ thỏa mãn.

${x_0} = 1$ $\Rightarrow {y_0} = 3$ thỏa mãn.

${x_0} = 3$ $\Rightarrow {y_0} = 1$ thỏa mãn.

Do đó đồ thị hàm số $(C)$ đi qua bốn điểm có tọa độ nguyên là $( – 2;0)$, $(0; – 2)$, $(1;3)$, $(3;1).$ Bốn điểm này không có ba điểm nào thẳng hàng.

Vậy số đường thẳng cắt $(C)$ tại hai điểm phân biệt có tọa độ nguyên là: $C_4^2 = 6.$

> **Đáp án: D**

## Bài 22. Đồ thị hàm số $y = \frac{2}{{{x^2} + 2x + 2}}$ có bao nhiêu điểm có tọa độ nguyên?

A. $1.$

B. $3.$

C. $5.$

D. $6.$

Giả sử $M\left( {{x_0};\frac{2}{{x_0^2 + 2{x_0} + 2}}} \right)$ điểm nằm trên đồ thị hàm số.

Khi đó $M$ có tọa độ nguyên khi ${x_0}$ nguyên và $\frac{2}{{x_0^2 + 2{x_0} + 2}}$ nguyên.

Suy ra $x_0^2 + 2{x_0} + 2 \in \{ – 2; – 1;1;2\} .$

Phương trình $x_0^2 + 2{x_0} + 2 = – 2$ $\Leftrightarrow x_0^2 + 2{x_0} + 4 = 0$ vô nghiệm.

Phương trình $x_0^2 + 2{x_0} + 2 = – 1$ $\Leftrightarrow x_0^2 + 2{x_0} + 3 = 0$ vô nghiệm.

Phương trình $x_0^2 + 2{x_0} + 2 = 1$ $\Leftrightarrow x_0^2 + 2{x_0} + 1 = 0$ có nghiệm kép ${x_0} = – 1.$

Phương trình $x_0^2 + 2{x_0} + 2 = 2$ $\Leftrightarrow x_0^2 + 2{x_0} = 0$ có hai nghiệm ${x_0} = 0$ và ${x_0} = – 2.$

Do đó ${x_0} \in \{ – 2; – 1;0\} .$

Vậy có ba điểm thỏa mãn yêu cầu bài toán.

> **Đáp án: B**

## Bài 23. Có bao nhiêu điểm $M$ nằm trên đồ thị hàm số $(C):y = \frac{{2x – 1}}{{x – 1}}$ sao cho khoảng cách từ điểm $M$ đến tiệm cận đứng bằng $1$?

A. $1.$

B. $2.$

C. $3.$

D. $4.$

Giả sử $M\left( {{x_0};\frac{{2{x_0} – 1}}{{{x_0} – 1}}} \right) \in (C)$ $\left( {{x_0} \ne 1} \right).$

Đồ thị $(C)$ có đường tiệm cận đúng $y = 2.$

Theo giả thiết $\left| {\frac{{2{x_0} – 1}}{{{x_0} – 1}} – 2} \right| = 1$ $\Leftrightarrow \left| {\frac{1}{{{x_0} – 1}}} \right| = 1.$

Giải phương trình trên ta được nghiệm ${x_0} = 2$ hoặc ${x_0} = 0.$

> **Đáp án: B**

## Bài 24. Có bao nhiêu điểm nằm trên đồ thị hàm số $(C):y = \frac{{2x + 1}}{{x – 1}}$ sao cho tổng khoảng cách từ điểm đó đến hai đường tiệm cận của $(C)$ bằng $4$?

A. $1.$

B. $2.$

C. $3.$

D. $4.$

Giả sử $A\left( {{x_0};\frac{{2{x_0} + 1}}{{{x_0} – 1}}} \right) \in (C)$ $\left( {{x_0} \ne 1} \right).$

Đồ thị $(C)$ có hai đường tiệm cận lần lượt là $x = 1$ và $y = 2.$

Theo giả thiết $\left| {{x_0} – 1} \right| + \left| {\frac{{2{x_0} + 1}}{{{x_0} – 1}} – 2} \right| = 4$ $\Leftrightarrow \left| {{x_0} – 1} \right| + \left| {\frac{3}{{{x_0} – 1}}} \right| = 4.$

Giải phương trình trên ta được bốn nghiệm duy nhất ${x_0} \in \{ – 2;0;2;4\} .$

## Bài 25. Xác định tọa độ điểm $M$ có hoành độ dương nằm trên đồ thị hàm số $y = \frac{{x + 2}}{{x – 2}}$ sao cho tổng khoảng cách từ $M$ đến hai đường tiệm cận của đồ thị hàm số đạt giá trị nhỏ nhất. A. $M(4;3).$

B. $M(3;5).$

C. $M(1;-3).$

D. $M(0;-1).$

Giả sử $M\left( {{x_0};\frac{{{x_0} + 2}}{{{x_0} – 2}}} \right) \in (C)$ $\left( {{x_0} > 0;{x_0} \ne 2} \right).$

Đồ thị $(C)$ có hai đường tiệm cận lần lượt là $x = 2$ và $y = 1.$

Theo giả thiết $\left| {{x_0} – 2} \right| + \left| {\frac{{{x_0} + 2}}{{{x_0} – 2}} – 1} \right|$ $= \left| {{x_0} – 2} \right| + \left| {\frac{4}{{{x_0} – 2}}} \right| \ge 4.$

Dấu bằng xảy ra khi $\left| {{x_0} – 2} \right| = \frac{4}{{\left| {{x_0} – 2} \right|}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_0} = 4 \Rightarrow {y_0} = 3}\\
{{x_0} = 0\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Vậy $M(4;3).$

> **Đáp án: A**

## Bài 26. Cho hàm số $y = \frac{{x + 2}}{{x – 1}}$ có đồ thị $(C).$ Gọi $I$ là giao điểm hai đường tiệm cận của $(C).$ Biết tọa độ điểm $M(a;b)$ có hoành độ dương thuộc đồ thị $(C)$ sao cho $MI$ ngắn nhất. Tính giá trị của $ab.$

A. $1 + \sqrt 3$.

B. $1 – \sqrt 3$.

C. $4 + \sqrt 3$.

D. $4 + 2\sqrt 3 .$

Giả sử $M\left( {{x_0};\frac{{{x_0} + 2}}{{{x_0} – 1}}} \right) \in (C)$ $\left( {{x_0} > 0;{x_0} \ne 1} \right).$

Giao điểm của hai đường tiệm cận của $(C)$ là $I(1;1).$

Khi đó $MI = \sqrt {{{\left( {1 – {x_0}} \right)}^2} + {{\left( {1 – \frac{{{x_0} + 2}}{{{x_0} – 1}}} \right)}^2}}$ $= \sqrt {{{\left( {1 – {x_0}} \right)}^2} + \frac{9}{{{{\left( {{x_0} – 1} \right)}^2}}}}$ $\ge \sqrt 6 .$

Dấu bằng xảy ra khi ${\left( {1 – {x_0}} \right)^2} = \frac{9}{{{{\left( {{x_0} – 1} \right)}^2}}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_0} = 1 + \sqrt 3 \Rightarrow {y_0} = 1 + \sqrt 3 }\\
{{x_0} = 1 – \sqrt 3 \:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Suy ra $M(1 + \sqrt 3 ;1 + \sqrt 3 )$ $\Rightarrow {(1 + \sqrt 3 )^2} = 4 + 2\sqrt 3 .$

> **Đáp án: D**

## Bài 27. Xác định tọa độ điểm $M$ có hoành độ dương nằm trên đồ thị hàm số $(C):y = \frac{{x + 1}}{{x – 2}}$ sao cho khoảng cách từ $M$ đến tiệm cận ngang của $(C)$ bằng $1.$

A. $M(3;2).$

B. $M(1;-2).$

C. $M(5;2).$

D. $M\left( {4;\frac{5}{2}} \right).$

Giả sử $M\left( {{x_0};\frac{{{x_0} + 1}}{{{x_0} – 2}}} \right) \in (C)$ $\left( {{x_0} > 0;{x_0} \ne 2} \right).$

Đồ thị $(C)$ có đường tiệm cận ngang là $y = 1.$

Theo giả thiết $\left| {\frac{{{x_0} + 1}}{{{x_0} – 2}} – 1} \right| = 1$ $\Leftrightarrow \left| {\frac{3}{{{x_0} – 2}}} \right| = 1$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_0} = 5 \Rightarrow {y_0} = 2}\\
{{x_0} = – 1\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

> **Đáp án: C**

## Bài 28. Cho điểm $M$ thuộc đồ thị $(C)$ của hàm số $y = \frac{{x – 7}}{{x + 1}}.$ Biết $M$ có hoành độ $a$ nhận giá trị âm và khoảng cách từ $M$ đến trục $Ox$ bằng ba lần khoảng cách từ $M$ đến trục $Ox.$ Tính giá trị của $a.$

A. $a = – \frac{3}{7}$.

B. $x = – \frac{1}{7}$.

C. $a = – \frac{1}{3}$.

D. $a = – \frac{7}{3}$.

Giả sử $M\left( {a;\frac{{a – 7}}{{a + 1}}} \right) \in (C)$ $(a < 0,a \ne – 1).$

Theo giả thiết $d(M;Ox) = 3d(M;Oy)$ $\Leftrightarrow \left| {\frac{{a – 7}}{{a + 1}}} \right| = 3|a|$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{a = 1}&{{\rm{(loại)}}}\\
{a = – \frac{7}{3}}&{{\rm{(thỏa mãn)}}}
\end{array}} \right..
$$

> **Đáp án: D**

## Bài 29. Cho hàm số $y = \frac{{2x – 3}}{{x – 2}}$ có đồ thị $(C).$ Gọi $M$ là một điểm thuộc đồ thị $(C)$ và $d$ là tổng khoảng cách từ $M$ đến hai tiệm cận của $(C).$ Tính giá trị nhỏ nhất của $d.$

A. $6.$

B. $10.$

C. $2.$

D. $5.$

Đồ thị hàm số $(C)$ có hai đường tiệm cận là ${\Delta _1}:x = 2$ và ${\Delta _2}:y = 2.$

Giả sử $M\left( {a;\frac{{2a – 3}}{{a – 2}}} \right) \in (C)$ $(a \ne 2).$

Ta có $d\left( {M;{\Delta _1}} \right) = |a – 2|$ và $d\left( {M;{\Delta _2}} \right) = \left| {\frac{{2a – 3}}{{a – 2}} – 2} \right|$ $= \frac{1}{{|a – 2|}}.$

Khi đó $d\left( {M;{\Delta _1}} \right) + d\left( {M;{\Delta _2}} \right)$ $= |a – 2| + \frac{1}{{|a – 2|}} \ge 2.$

> **Đáp án: C**

## Bài 30. Có bao nhiêu điểm $M$ thuộc đồ thị $(C)$ của hàm số $y = \frac{{{x^2} + 5x + 15}}{{x + 3}}$ cách đều hai trục tọa độ?

A. $2.$

B. $1.$

C. $0.$

D. $3.$

Giả sử $M\left( {a;\frac{{{a^2} + 5a + 15}}{{a + 3}}} \right) \in (C)$ $(a \ne – 3).$

Theo giả thiết $d(M;Ox) = d(M;Oy)$ $\Leftrightarrow \left| {\frac{{{a^2} + 5a + 15}}{{a + 3}}} \right| = |a|$ $\Leftrightarrow a = – \frac{{15}}{2}.$

> **Đáp án: B**