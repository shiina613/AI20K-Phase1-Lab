# Viết phương trình đường tròn (Oxy)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/03/viet-phuong-trinh-duong-tron-oxy.html -->
Bài viết hướng dẫn phương pháp viết phương trình đường tròn trong hệ tọa độ Oxy thông qua việc trình bày các bước giải toán cụ thể kèm theo các ví dụ minh họa có lời giải chi tiết, đây là một nội dung quan trọng trong chương trình Hình học 10 chương 3: phương pháp tọa độ trong mặt phẳng.

Để viết phương trình đường tròn $(C)$ trong hệ tọa độ $Oxy$ thỏa mãn các yêu cầu cho trước, ta thường sử dụng 2 phương pháp sau đây:

Phương pháp 1

+  Tìm toạ độ tâm $I\left( {a;b} \right)$ của đường tròn $(C).$

+  Tìm bán kính $R$ của đường tròn $(C).$

+  Viết phương trình của $(C)$ theo dạng ${(x – a)^2} + {(y – b)^2} = {R^2}.$

Phương pháp 2

Giả sử phương trình đường tròn $(C)$ là: ${x^2} + {y^2} – 2ax – 2by + c = 0{\rm{ }}$ (hoặc ${x^2} + {y^2} + 2ax + 2by + c = 0{\rm{ }}$).

+ Từ điều kiện của đề bài thành lập hệ phương trình với ba ẩn là $a, b, c.$

+ Giải hệ để tìm $a, b, c$ từ đó tìm được phương trình đường tròn $(C).$

Chú ý:

+ $A \in \left( C \right) \Leftrightarrow IA = R.$

+ $\left( C \right)$ tiếp xúc với đường thẳng $\Delta$ tại $A$ $\Leftrightarrow IA = d\left( {I;\Delta } \right) = R.$

+ $\left( C \right)$ tiếp xúc với hai đường thẳng ${\Delta _1}$ và ${\Delta _2}$ $\Leftrightarrow d\left( {I;{\Delta _1}} \right) = d\left( {I;{\Delta _2}} \right) = R.$

<!-- chunk:1 level:3 source:https://toanmath.com/2018/03/viet-phuong-trinh-duong-tron-oxy.html -->
## Ví dụ 1: Viết phương trình đường tròn trong mỗi trường hợp sau:

a. Có tâm $I\left( {1; – 5} \right)$ và đi qua $O\left( {0;0} \right).$

b. Nhận $AB$ làm đường kính với $A\left( {1;1} \right),B\left( {7;5} \right).$

c. Đi qua ba điểm: $M\left( { – 2;4} \right),N\left( {5;5} \right),P\left( {6; – 2} \right).$

a. Đường tròn cần tìm có bán kính là $OI = \sqrt {{1^2} + {5^2}} = \sqrt {26}$ nên có phương trình là ${\left( {x – 1} \right)^2} + {\left( {y + 5} \right)^2} = 26.$

b. Gọi $I$ là trung điểm của đoạn $AB$ suy ra $I\left( {4;3} \right).$

$AI = \sqrt {{{\left( {4 – 1} \right)}^2} + {{\left( {3 – 1} \right)}^2}} = \sqrt {13} .$

Đường tròn cần tìm có đường kính là $AB$ suy ra nó nhận $I\left( {4;3} \right)$ làm tâm và bán kính $R = AI = \sqrt {13}$ nên có phương trình là: ${\left( {x – 4} \right)^2} + {\left( {y – 3} \right)^2} = 13.$

c. Gọi phương trình đường tròn $(C)$ có dạng là: ${x^2} + {y^2} – 2ax – 2by + c = 0.$

Do đường tròn đi qua ba điểm $M,N,P$ nên ta có hệ phương trình:

$$
\left\{ \begin{array}{l}
4 + 16 + 4a – 8b + c = 0\\
25 + 25 – 10a – 10b + c = 0\\
36 + 4 – 12a + 4b + c = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = 2\\
b = 1\\
c = – 20
\end{array} \right.
$$

Vậy phương trình đường tròn cần tìm là: ${x^2} + {y^2} – 4x – 2y – 20 = 0.$

Nhận xét:  Đối với ý c ta có thể làm theo cách sau:

Gọi $I\left( {x;y} \right)$ và $R$ là tâm và bán kính đường tròn cần tìm.

Vì $IM = IN = IP$ 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{I{M^2} = I{N^2}}\\
{I{M^2} = I{P^2}}
\end{array}} \right.
$$
 nên ta có hệ:

${{{\left( {x + 2} \right)}^2} + {{\left( {y – 4} \right)}^2}}$ ${ = {{\left( {x – 5} \right)}^2} + {{\left( {y – 5} \right)}^2}}$

${{{\left( {x + 2} \right)}^2} + {{\left( {y – 4} \right)}^2}}$ ${ = {{\left( {x – 6} \right)}^2} + {{\left( {y + 2} \right)}^2}}$

$$
\Leftrightarrow \left\{ {\begin{array}{c}
{x = 2}\\
{y = 1}
\end{array}} \right.
$$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/03/viet-phuong-trinh-duong-tron-oxy.html -->
## Ví dụ 2: Viết phương trình đường tròn $(C)$ trong các trường hợp sau:

a. $(C)$ có tâm $I\left( { – 1;2} \right)$ và tiếp xúc với đường thẳng $Δ: x – 2y + 7 = 0.$

b. $(C)$ đi qua $A\left( {2; – 1} \right)$ và tiếp xúc với hai trục toạ độ $Ox$ và $Oy.$

c. $(C)$ có tâm nằm trên đường thẳng $d:x – 6y – 10 = 0$ và tiếp xúc với hai đường thẳng có phương trình  ${d_1}:3x + 4y + 5 = 0$ và ${d_2}:4x – 3y – 5 = 0.$

a. Bán kính đường tròn $(C)$ chính là khoảng cách từ $I$ tới đường thẳng $\Delta$ nên $R = d\left( {I;\Delta } \right)$ $= \frac{{\left| { – 1 – 4 – 7} \right|}}{{\sqrt {1 + 4} }} = \frac{2}{{\sqrt 5 }}.$

Vậy phương trình đường tròn $(C)$ là ${\left( {x + 1} \right)^2} + {\left( {y – 2} \right)^2} = \frac{4}{5}.$

b. Vì điểm $A$ nằm ở góc phần tư thứ tư và đường tròn tiếp xúc với hai trục toạ độ nên tâm của đường tròn có dạng $I\left( {R; – R} \right)$ trong đó $R$ là bán kính đường tròn $(C).$

Ta có:

${R^2} = I{A^2}$ $\Leftrightarrow {R^2} = {\left( {2 – R} \right)^2} + {\left( { – 1 + R} \right)^2}$ $\Leftrightarrow {R^2} – 6R + 5 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{c}
{R = 1}\\
{R = 5}
\end{array}} \right.
$$

Vậy có hai đường tròn thoả mãn đầu bài là: ${\left( {x – 1} \right)^2} + {\left( {y + 1} \right)^2} = 1$ và ${\left( {x – 5} \right)^2} + {\left( {y + 5} \right)^2} = 25.$

c. Vì đường tròn cần tìm có tâm $K$ nằm trên đường thẳng $d$ nên gọi  $K\left( {6a + 10;a} \right).$

Mặt khác đường tròn tiếp xúc với ${d_1},{d_2}$ nên khoảng cách từ tâm $I$ đến hai đường thẳng này bằng nhau và bằng bán kính $R$ suy ra:

$\frac{{\left| {3(6a + 10) + 4a + 5} \right|}}{5}$ $= \frac{{\left| {4(6a + 10) – 3a – 5} \right|}}{5}$ $\left| { \Leftrightarrow 22a + 35} \right| = \left| {21a + 35} \right|$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
a = 0\\
a = \frac{{ – 70}}{{43}}
\end{array} \right.
$$

+ Với $a = 0$ thì $K\left( {10;0} \right)$ và $R = 7$ suy ra $\left( C \right):{\left( {x – 10} \right)^2} + {y^2} = 49.$

+ Với $a = \frac{{ – 70}}{{43}}$ thì $K\left( {\frac{{10}}{{43}};\frac{{ – 70}}{{43}}} \right)$ và $R = \frac{7}{{43}}$ suy ra $\left( C \right):{\left( {x – \frac{{10}}{{43}}} \right)^2} + {\left( {y + \frac{{70}}{{43}}} \right)^2} = {\left( {\frac{7}{{43}}} \right)^2}.$

Vậy có hai đường tròn thỏa mãn có phương trình là $\left( C \right):{\left( {x – 10} \right)^2} + {y^2} = 49$ và  $\left( C \right):{\left( {x – \frac{{10}}{{43}}} \right)^2} + {\left( {y + \frac{{70}}{{43}}} \right)^2} = {\left( {\frac{7}{{43}}} \right)^2}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/03/viet-phuong-trinh-duong-tron-oxy.html -->
## Ví dụ 3: Cho hai điểm $A\left( {8;0} \right)$ và $B\left( {0;6} \right).$

a. Viết phương trình đường tròn ngoại tiếp tam giác $OAB.$

b. Viết phương trình đường tròn nội tiếp tam giác $OAB.$

<img link="data_for_rag/toan10/images/viet-phuong-trinh-duong-tron-oxy-1.png" alt="viet-phuong-trinh-duong-tron-oxy-1">

a. Ta có tam giác $OAB$ vuông ở $O$ nên tâm $I$ của đường tròn ngoại tiếp tam giác là trung điểm của cạnh huyền $AB$ suy ra $I\left( {4;3} \right)$ và bán kính $R = IA$ $= \sqrt {{{\left( {8 – 4} \right)}^2} + {{\left( {0 – 3} \right)}^2}} = 5.$

Vậy phương trình đường tròn ngoại tiếp tam giác $OAB$ là:

${\left( {x – 4} \right)^2} + {\left( {y – 3} \right)^2} = 25.$

b. Ta có $OA = 8;OB = 6$, $AB = \sqrt {{8^2} + {6^2}} = 10.$

Mặt khác $\frac{1}{2}OA.OB = pr$ (vì cùng bằng diện tích tam giác $ABC$).

Suy ra $r = \frac{{OA.OB}}{{OA + OB + AB}} = 2.$

Dễ thấy đường tròn cần tìm có tâm thuộc góc phần tư thứ nhất và tiếp xúc với hai trục tọa độ nên tâm của đường tròn có tọa độ là $\left( {2;2} \right).$

Vậy phương trình đường tròn nội tiếp tam giác $OAB$ là: ${\left( {x – 2} \right)^2} + {\left( {y – 2} \right)^2} = 4.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/03/viet-phuong-trinh-duong-tron-oxy.html -->
## Ví dụ 4: Trong mặt phẳng tọa độ $Oxy$, cho hai đường thẳng ${d_1}:\sqrt 3 x + y = 0$ và ${d_2}:\sqrt 3 x – y = 0.$ Gọi $(C)$ là đường tròn tiếp xúc với ${d_1}$ tại $A$, cắt ${d_2}$ tại hai điểm $B, C$ sao cho tam giác $ABC$ vuông tại $B$. Viết phương trình của $(C)$, biết tam giác $ABC$ có diện tích bằng $\frac{{\sqrt 3 }}{2}$ và điểm $A$ có hoành độ dương.

<img link="data_for_rag/toan10/images/viet-phuong-trinh-duong-tron-oxy-2.png" alt="viet-phuong-trinh-duong-tron-oxy-2">

Vì $A \in {d_1}$ $\Rightarrow A\left( {a; – \sqrt 3 a} \right),a > 0;$ $B,C \in {d_2}$ $\Rightarrow B\left( {b;\sqrt 3 b} \right),C\left( {c;\sqrt 3 c} \right).$

Suy ra $\overrightarrow {AB} \left( {b – a;\sqrt 3 \left( {a + b} \right)} \right),$ $\overrightarrow {AC} \left( {c – a;\sqrt 3 \left( {c + a} \right)} \right).$

Tam giác $ABC$ vuông tại $B$ do đó $AC$ là đường kính của đường tròn $C.$

Do đó $AC \bot {d_1}$ $\Rightarrow \overrightarrow {AC} .\overrightarrow {{u_1}} = 0$ $\Leftrightarrow – 1.\left( {c – a} \right) + \sqrt 3 .\sqrt 3 \left( {a + c} \right) = 0$ $\Leftrightarrow 2a + c = 0$ $(1).$

$AB \bot {d_2}$ $\Rightarrow \overrightarrow {AB} .\overrightarrow {{u_2}} = 0$ $\Leftrightarrow 1.\left( {b – a} \right) + 3\left( {a + b} \right) = 0$ $\Leftrightarrow 2b + a = 0$ $(2).$

Mặt khác: ${S_{ABC}} = \frac{1}{2}d\left( {A;{d_2}} \right).BC$ $\Rightarrow \frac{1}{2}.\frac{{\left| {2\sqrt 3 a} \right|}}{2}\sqrt {{{\left( {c – b} \right)}^2} + 3{{\left( {c – b} \right)}^2}}$ $= \frac{{\sqrt 3 }}{2}$ $\Leftrightarrow 2a\left| {c – b} \right| = 1$ $(3).$

Từ $(1)$, $(2)$ suy ra $2\left( {c – b} \right) = – 3a$ thế vào $(3)$ ta được:

$a\left| { – 3a} \right| = 1 \Leftrightarrow a = \frac{{\sqrt 3 }}{3}.$

Do đó $b = – \frac{{\sqrt 3 }}{6},c = – \frac{{2\sqrt 3 }}{3}$ $\Rightarrow A\left( {\frac{{\sqrt 3 }}{3}; – 1} \right),C\left( { – \frac{{2\sqrt 3 }}{3}; – 2} \right).$

Suy ra $(C)$ nhận $I\left( { – \frac{{\sqrt 3 }}{6}; – \frac{3}{2}} \right)$ là trung điểm $AC$ làm tâm và bán kính là $R = \frac{{AC}}{2} = 1.$

Vậy phương trình đường tròn cần tìm là $\left( C \right):{\left( {x + \frac{{\sqrt 3 }}{6}} \right)^2} + {\left( {x + \frac{3}{2}} \right)^2} = 1.$