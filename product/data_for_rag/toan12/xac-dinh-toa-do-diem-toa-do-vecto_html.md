# Xác định tọa độ điểm, tọa độ vectơ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
Bài viết hướng dẫn phương pháp xác định tọa độ điểm, tọa độ vectơ trong hệ trục tọa độ không gian Oxyz, đây là dạng toán cơ bản thường gặp trong chương trình Hình học 12 chương 3, lý thuyết và các ví dụ trong bài viết được tham khảo từ các tài liệu phương pháp tọa độ trong không gian được chia sẻ trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## A. PHƯƠNG PHÁP XÁC ĐỊNH TỌA ĐỘ ĐIỂM – TỌA ĐỘ VECTƠ
+ Dựa vào định nghĩa tọa độ của điểm, tọa độ của véc tơ.

+ Dựa vào các phép toán véctơ.

+ Áp dụng các tính chất sau: Cho các vectơ $\overrightarrow u = ({u_1};{u_2};{u_3})$, $\overrightarrow v = ({v_1};{v_2};{v_3})$ và số thực $k$ tùy ý. Khi đó ta có:

$$
\overrightarrow u = \overrightarrow v \Leftrightarrow \left\{ \begin{array}{l}
{u_1} = {v_1}\\
{u_2} = {v_2}\\
{u_3} = {v_3}
\end{array} \right.
$$

$\overrightarrow u + \overrightarrow v = ({u_1} + {v_1};{u_2} + {v_2};{u_3} + {v_3}).$

$\overrightarrow u – \overrightarrow v = ({u_1} – {v_1};{u_2} – {v_2};{u_3} – {v_3}).$

$k\overrightarrow u = (k{u_1};k{u_2};k{u_3}).$

<!-- chunk:2 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 1: Cho hai véctơ $\overrightarrow a$, $\overrightarrow b$ thỏa $\widehat {\left( {\overrightarrow a ,\overrightarrow b } \right)} = {120^0}$, $\left| {\overrightarrow a } \right| = 2$, $\left| {\overrightarrow b } \right| = 3.$

1. Tính $\left| {\overrightarrow a – 2\overrightarrow b } \right|.$

2. Tính góc giữa hai véctơ $\overrightarrow a$ và $\overrightarrow x = 3\overrightarrow a + 2\overrightarrow b .$

1. Ta có: $\overrightarrow a .\overrightarrow b = \left| {\overrightarrow a } \right|.\left| {\overrightarrow b } \right|.\cos \widehat {\left( {\overrightarrow a ,\overrightarrow b } \right)}$ $= 2.3.\cos {120^0} = – 3.$

$\Rightarrow {\left( {\overrightarrow a – 2\overrightarrow b } \right)^2}$ $= {\overrightarrow a ^2} – 4\overrightarrow a .\overrightarrow b + 4{\overrightarrow b ^2}$ $= {2^2} + 4.3 + {4.3^2}$ $= 52$ $\Rightarrow \left| {\overrightarrow a – 2\overrightarrow b } \right| = 2\sqrt {13} .$

2. Ta có: $\overrightarrow a .\overrightarrow x = \overrightarrow a \left( {3\overrightarrow a + 2\overrightarrow b } \right)$ $= 3{\overrightarrow a ^2} + 2\overrightarrow a .\overrightarrow b = 6$ và $\left| {\overrightarrow x } \right| = \sqrt {{{(3\overrightarrow a + 2\overrightarrow b )}^2}} = 6.$

Suy ra $\cos \widehat {\left( {\overrightarrow x ,\overrightarrow a } \right)} = \frac{{\overrightarrow a .\overrightarrow x }}{{\left| {\overrightarrow a } \right|.\left| {\overrightarrow x } \right|}}$ $= \frac{6}{{6.2}} = \frac{1}{2}$ $\Rightarrow \widehat {\left( {\overrightarrow a ,\overrightarrow x } \right)} = {60^0}.$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 2: Trong không gian $Oxyz$, cho ba vectơ $\overrightarrow a = (1;0; – 2)$, $\overrightarrow b = ( – 2;1;3)$, $\overrightarrow c = ( – 4;3;5).$

1. Tìm toạ độ vectơ $3\overrightarrow a – 4\overrightarrow b + 2\overrightarrow c .$

2. Tìm hai số thực $m$, $n$ sao cho $m\overrightarrow a + n\overrightarrow b = \overrightarrow c .$

1. Tọa độ vectơ $3\overrightarrow a – 4\overrightarrow b + 2\overrightarrow c .$

$\overrightarrow a = (1;0; – 2)$ $\Rightarrow 3\overrightarrow a = (3;0; – 6).$

$\overrightarrow b = ( – 2;1;3)$ $\Rightarrow – 4\overrightarrow b = (8; – 4; – 12).$

$\overrightarrow c = ( – 4;3;5)$ $\Rightarrow 2\overrightarrow c = ( – 8;3;10).$

Suy ra $3\overrightarrow a – 4\overrightarrow b + 2\overrightarrow c$ $= \left( {3 + 8 – 8;0 – 4 + 3; – 6 – 12 + 10} \right)$ $= \left( {3; – 1;4} \right).$

2. Tìm $m$, $n.$

Ta có $m\overrightarrow a + n\overrightarrow b$ $= (m – 2n;n; – 2m + 3n).$

Suy ra $m\overrightarrow a + n\overrightarrow b = \overrightarrow c$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m – 2n = – 4\\
n = 3\\
– 2m + 3n = 5
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
m = 2\\
n = 3
\end{array} \right. .
$$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 3: Trong không gian $Oxyz$, cho tam giác $ABC$ có $A\left( {2; – 3;1} \right)$, $B\left( {1; – 1;4} \right)$ và $C\left( { – 2;1;6} \right).$

1. Xác định toạ độ trọng tâm $G$ của tam giác $ABC.$

2. Xác định toạ độ điểm $D$ sao cho tứ giác $ABCD$ là hình bình hành và tìm toạ độ giao điểm hai đường chéo của hình bình hành này.

3. Xác định toạ độ điểm $M$ sao cho $\overrightarrow {MA} = – 2\overrightarrow {MB} .$

1. Xác định tọa độ trọng tâm $G.$

Theo tính chất của trọng tâm $G$, ta có:

$\overrightarrow {OG} = \frac{1}{3}(\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} )$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_G} = \frac{{{x_A} + {x_B} + {x_C}}}{3} = \frac{1}{3}\\
{y_G} = \frac{{{y_A} + {y_B} + {y_C}}}{3} = – 1\\
{z_G} = \frac{{{z_A} + {z_B} + {z_C}}}{3} = \frac{{11}}{3}
\end{array} \right. .
$$

2. Xác định tọa độ điểm $D.$

Vì $A$, $B$, $C$ là ba đỉnh của một tam giác, do đó:

$ABCD$ là hình bình hành $\Leftrightarrow \overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_B} – {x_A} = {x_C} – {x_D}\\
{y_B} – {y_A} = {y_C} – {y_D}\\
{z_B} – {z_A} = {z_C} – {z_D}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
– 1 = – 2 – {x_D}\\
2 = 1 – {y_D}\\
3 = 6 – {z_D}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_D} = – 1\\
{y_D} = – 1\\
{z_D} = 3
\end{array} \right. .
$$

Vậy $D\left( { – 1; – 1;3} \right).$

Giao điểm $I$ của hai đường chéo $AC$ và $BD$ của hình bình hành $ABCD$ là trung điểm của $AC$, suy ra: 
$$
I\left\{ \begin{array}{l}
{x_I} = \frac{{{x_A} + {x_C}}}{2} = 0\\
{y_I} = \frac{{{y_A} + {y_C}}}{2} = – 1\\
{z_I} = \frac{{{z_A} + {z_C}}}{2} = \frac{7}{2}
\end{array} \right. .
$$

3. Xác định tọa độ $M.$

Gọi $\left( {x;y;z} \right)$ là toạ độ của $M$, ta có:

$\overrightarrow {MA} = – 2\overrightarrow {MB}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
2 – x = – 2(1 – x)\\
– 3 – y = – 2( – 1 – y)\\
1 – z = – 2(4 – z)
\end{array} \right.
$$
 
$$
\left\{ \begin{array}{l}
x = \frac{4}{3}\\
y = – \frac{5}{3}\\
z = 3
\end{array} \right. .
$$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 4: Cho tam giác $ABC$ có $A(1;0; – 2)$, $B( – 1;1;0)$, $C( – 2;4; – 2).$

1. Tìm tọa độ trọng tâm $G$, trực tâm $H$, tâm đường tròn ngoại tiếp $I$ của tam giác $ABC.$

2. Tìm tọa độ giao điểm của phân giác trong, phân giác ngoài góc $A$ với đường thẳng $BC.$

1. $\overrightarrow {AB} ( – 2;1;2)$, $\overrightarrow {BC} ( – 1;3; – 2)$, $\overrightarrow {CA} (3; – 4;0).$

Trọng tâm $G\left( { – \frac{2}{3};\frac{5}{3}; – \frac{4}{3}} \right).$

Ta có $\left[ {\overrightarrow {AB} ;\overrightarrow {AC} } \right] = ( – 8; – 6; – 5).$

Tọa độ điểm $H$ thỏa mãn hệ:

$$
\left\{ \begin{array}{l}
\overrightarrow {AH} .\overrightarrow {BC} = 0\\
\overrightarrow {BH} .\overrightarrow {CA} = 0\\
\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right].\overrightarrow {AH} = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x – 3y + 2z = – 3\\
3x – 4y = – 7\\
8x + 6y + 5z = – 2
\end{array} \right.
$$
 $\Rightarrow H\left( { – \frac{{29}}{{25}};\frac{{22}}{{25}};\frac{2}{5}} \right).$

Tọa độ điểm $I$ thỏa mãn hệ:

$$
\left\{ \begin{array}{l}
IA = IB\\
IA = IC\\
\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right].\overrightarrow {AI} = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
4x – 2y – 4z = 3\\
6x – 8y = – 19\\
8x + 6y + 5z = – 2
\end{array} \right.
$$
 $\Rightarrow I\left( { – \frac{{21}}{{50}};\frac{{103}}{{50}}; – \frac{{11}}{5}} \right).$

2. Gọi $E$, $F$ lần lượt là giao điểm của phân giác trong, phân giác ngoài góc $A$ với đường thẳng $BC.$ Từ $\frac{{EB}}{{EC}} = \frac{{FB}}{{FC}} = \frac{{AB}}{{AC}} = \frac{3}{5}$ ta tính được tọa độ các điểm $E\left( { – \frac{{11}}{8}; – \frac{7}{8}; – \frac{3}{4}} \right)$, $F\left( {\frac{1}{2}; – \frac{7}{2};3} \right).$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Ví dụ 5: Trong không gian $Oxyz$, cho hình hộp $ABCD.A’B’C’D’$ có $A(-1,2,3)$, $C(1; 4; 5)$, $B'(-3;3;-2)$, $D'(5;3;2)$. Xác định toạ độ các đỉnh còn lại của hình hộp.

<img link="data_for_rag/toan12/images/xac-dinh-toa-do-diem-toa-do-vecto-1.png" alt="">

Gọi $E$, $E’$ lần lượt là trung điểm của $AC$ và $B’D’$ thì ta có: $\overrightarrow {EE’} = \overrightarrow {AA’} = \overrightarrow {BB’} = \overrightarrow {CC’} = \overrightarrow {DD’}$ và 
$$
\left\{ \begin{array}{l}
{x_E} = \frac{{{x_A} + {x_C}}}{2} = 0\\
{y_E} = \frac{{{y_A} + {y_C}}}{2} = 3\\
{z_E} = \frac{{{z_A} + {z_C}}}{2} = 4
\end{array} \right.
$$
, 
$$
\left\{ \begin{array}{l}
{x_{E’}} = \frac{{{x_{B’}} + {x_{D’}}}}{2} = 1\\
{y_{E’}} = \frac{{{y_{B’}} + {y_{D’}}}}{2} = 3\\
{z_{E’}} = \frac{{{z_{B’}} + {z_{D’}}}}{2} = 0
\end{array} \right. .
$$

Suy ra $\overrightarrow {EE’} = (1;0; – 4).$

$\overrightarrow {AA’} = \overrightarrow {EE’}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_{A’}} + 1 = 1\\
{y_{A’}} – 2 = 0\\
{z_{A’}} – 3 = – 4
\end{array} \right.
$$
 $\Leftrightarrow A'(0;2; – 1).$

$\overrightarrow {BB’} = \overrightarrow {EE’}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
– 3 – {x_B} = 1\\
3 – {y_B} = 0\\
– 2 – {z_B} = – 4
\end{array} \right.
$$
 $\Leftrightarrow B( – 4;3;2).$

$\overrightarrow {CC’} = \overrightarrow {EE’}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_{C’}} – 1 = 1\\
{y_{C’}} – 4 = 0\\
{z_{C’}} – 5 = – 4
\end{array} \right.
$$
 $\Leftrightarrow C'(2;4;1).$

$\overrightarrow {DD’} = \overrightarrow {EE’}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
5 – {x_D} = 1\\
3 – {y_D} = 0\\
2 – {z_D} = – 4
\end{array} \right.
$$
 $\Leftrightarrow D(4;3;6).$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 6: Cho hình chóp $S.ABCD$ với điểm $A(4; – 1;2)$ và $C(0;0; – 2)$, $D(10; – 2;4).$ Gọi $M$ là trung điểm của $CD.$ Biết $SM$ vuông góc với mặt phẳng $(ABCD)$ và thể tích khối chóp ${V_{S.ABCD}} = 66$ (đvtt). Tìm tọa độ đỉnh $S.$

Ta có $\overrightarrow {AB} ( – 5;1; – 3)$, $\overrightarrow {DC} ( – 10;2; – 6)$ $\Rightarrow \overrightarrow {DC} = 2.\overrightarrow {AB}$ nên $ABCD$ là hình thang và ${S_{ADC}} = 2{S_{ABC}}$ hay ${S_{ABCD}} = 3{S_{ABC}}.$

Vì $\overrightarrow {AB} ( – 5;1; – 3)$, $\overrightarrow {AC} ( – 4;1; – 4)$ nên $\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right] = ( – 1; – 8; – 1)$, do đó ${S_{ABC}} = \frac{1}{2}\left| {\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right]} \right| = \frac{{\sqrt {66} }}{2}$ $\Rightarrow {S_{ABCD}} = \frac{{3\sqrt {66} }}{2}$ (đvdt).

Chiều cao của khối chóp là $SM = \frac{{3{V_{S.ABCD}}}}{{{S_{ABCD}}}} = 2\sqrt {66} .$

Vì $\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right] \bot \overrightarrow {AB}$, $\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right] \bot \overrightarrow {AC}$ nên giá của véctơ $\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right]$ vuông góc với mặt phẳng $(ABCD)$, mà $SM \bot (ABCD)$ nên tồn tại số thực $k$ sao cho: $\overrightarrow {SM} = k.\left[ {\overrightarrow {AB} ,\overrightarrow {AC} } \right]$ $= ( – k; – 8k; – k).$

Suy ra $2\sqrt {66} = \left| {\overrightarrow {SM} } \right|$ $= \sqrt {{{( – k)}^2} + {{( – 8k)}^2} + {{( – k)}^2}}$ $\Leftrightarrow \left| k \right| = 2$ $\Leftrightarrow k = \pm 2.$

$M$ là trung điểm $CD$ nên $M(5; – 1;1)$ $\Rightarrow \overrightarrow {SM} (5 – {x_S}; – 1 – {y_S};1 – {z_S}).$

Nếu $k = 2$ thì $\overrightarrow {SM} = (5 – {x_S}; – 1 – {y_S};1 – {z_S})$ $= ( – 2; – 16; – 2)$ nên tọa độ của điểm $S$ là $S(7;15;3).$

Nếu $k = – 2$ thì $\overrightarrow {SM} = (5 – {x_S}; – 1 – {y_S};1 – {z_S})$ $= (2;16;2)$ nên tọa độ của điểm $S$ là $S(3; – 17; – 1).$

Vậy tọa độ các điểm $S$ cần tìm là $S(7;15;3)$ hoặc $S(3; – 17; – 1).$

<!-- chunk:8 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 7: Trong không gian với hệ toạ độ $Oxyz$, cho tam giác $ABC$ có $A(2; -1;3)$, $B(3;0; -2)$, $C(5; – 1; -6).$

1. Tính $\cos \widehat {BAC}$, suy ra số đo của $\widehat {BAC}.$

2. Xác định toạ độ hình chiếu vuông góc $H$ của $A$ trên $BC$ và toạ độ điểm $A’$ đối xứng của $A$ qua đường thẳng $BC.$

1. Tính $\cos \widehat {BAC}$ và số đo của $\widehat {BAC}.$

Ta có: $\overrightarrow {AB} = (1;1; – 5)$, $\overrightarrow {AC} = (3;0; – 9)$, suy ra: $\cos \widehat {BAC} = \cos (\overrightarrow {AB} ,\overrightarrow {AC} ) = \frac{{\overrightarrow {AB} .\overrightarrow {AC} }}{{\left| {\overrightarrow {AB} } \right|\left| {\overrightarrow {AC} } \right|}} .$ $= \frac{{3 + 45}}{{\sqrt {{1^2} + {1^2} + {{( – 5)}^2}} .\sqrt {{3^2} + {0^2} + {{( – 9)}^2}} }}$ $= \frac{{48}}{{\sqrt {27} .\sqrt {90} }} = \frac{{16}}{{3\sqrt {30} }}.$

Suy ra $\widehat {BAC} \approx {13^0}10′ .$

2. Tọa độ hình chiếu vuông góc $H$ của $A$ lên đường thẳng $BC.$

<img link="data_for_rag/toan12/images/xac-dinh-toa-do-diem-toa-do-vecto-2.png" alt="">

Kí hiệu $(x;y;z)$ là toạ độ của $H$, ta có:

$\overrightarrow {AH} \bot \overrightarrow {BC}$ và $\overrightarrow {BH}$ cùng phương $\overrightarrow {BC} .$

$\overrightarrow {AH} = (x – 2;y + 1;z – 3)$, $\overrightarrow {BC} = (2; – 1; – 4)$, $\overrightarrow {BH} = (x – 3;y;z + 2).$

$\overrightarrow {AH} \bot \overrightarrow {BC}$ $\Leftrightarrow \overrightarrow {AH} .\overrightarrow {BC} = 0$ $\Leftrightarrow 2(x – 2) – (y + 1) – 4(z – 3) = 0$ $\Leftrightarrow 2x – y – 4z + 7 = 0.$

$\overrightarrow {BH}$ cùng phương với $\overrightarrow {BC}$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x + 2y = 3\\
4y – z = 2
\end{array} \right. .
$$

Giải hệ 
$$
\left\{ \begin{array}{l}
2x – y – 4z = – 7\\
x + 2y = 3\\
4y – z = 2
\end{array} \right.
$$
 ta được $H(1;1;2).$

Tọa độ $A’$ đối xứng của $A$ qua $BC.$

$A’$ là điểm đối xứng của $A$ qua đường thẳng $BC$ $⇔H$ là trung điểm của $AA’$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_H} = \frac{{{x_A} + {x_{A’}}}}{2}\\
{y_H} = \frac{{{y_A} + {y_{A’}}}}{2}\\
{z_H} = \frac{{{z_A} + {z_{A’}}}}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_{A’}} = 2{x_H} – {x_A} = 0\\
{y_{A’}} = 2{y_H} – {y_A} = 3\\
{z_{A’}} = 2{z_H} – {z_A} = 1
\end{array} \right. .
$$
 Vậy $A'(0;3;1).$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài toán 8: Trong không gian với hệ tọa độ $Oxyz$, cho tam giác $ABC$ có $A(4;2;0)$, $B(2;4;0)$ và $C(2;2;1).$ Xác định tọa độ trực tâm và tâm đường tròn ngoại tiếp của tam giác $ABC.$

Toạ độ trực tâm của tam giác $ABC.$

Gọi $H(x;y;z)$ là trực tâm của tam giác $ABC$, ta có:

$$
\left\{ \begin{array}{l}
\overrightarrow {AH} \bot \overrightarrow {BC} \\
\overrightarrow {BH} \bot \overrightarrow {AC} \\
\overrightarrow {BC} ,\overrightarrow {AC} ,\overrightarrow {AH} {\rm{\:đồng\: phẳng}}
\end{array} \right. .
$$

Trong đó: $\overrightarrow {AH} = (x – 4;y – 2;z)$, $\overrightarrow {BC} = \left( {0; – 2;1} \right)$, $\overrightarrow {BH} = (x – 2;y – 4;z)$, $\overrightarrow {AC} = ( – 2;0;1).$

$\overrightarrow {AH} \bot \overrightarrow {BC}$ $\Leftrightarrow \overrightarrow {AH} .\overrightarrow {BC} = 0$ $\Leftrightarrow – 2(y – 2) + z = 0$ $\Leftrightarrow 2y – z = 4.$

$\overrightarrow {BH} \bot \overrightarrow {AC}$ $\Leftrightarrow \overrightarrow {BH} .\overrightarrow {AC} = 0$ $\Leftrightarrow – 2(x – 2) + z = 0$ $\Leftrightarrow 2x – z = 4.$

$\overrightarrow {BC}$, $\overrightarrow {AC}$, $\overrightarrow {AH}$ đồng phẳng $\Leftrightarrow [\overrightarrow {BC} ,\overrightarrow {AC} ].\overrightarrow {AH} = 0$ (trong đó $[\overrightarrow {BC} ,\overrightarrow {AC} ] = ( – 2; – 2; – 4)$) $\Leftrightarrow – 2(x – 4) -2(y – 2) – 4z =0$ $\Leftrightarrow x + y + 2z = 6.$

Giải hệ: 
$$
\left\{ \begin{array}{l}
2y – z = 4\\
2x – z = 4\\
x + y + 2z = 6
\end{array} \right.
$$
, ta được $H\left( {\frac{7}{3};\frac{7}{3};\frac{2}{3}} \right).$

Toạ độ tâm đường tròn ngoại tiếp tam giác $ABC.$

Gọi $I(x;y;z)$ là tâm đường tròn ngoại tiếp tam giác $ABC$, ta có: 
$$
\left\{ \begin{array}{l}
AI = BI = CI\\
\overrightarrow {BC} ,\overrightarrow {AC} ,\overrightarrow {AI} {\rm{\:đồng\:phẳng}}
\end{array} \right. .
$$

$AI = BI = CI$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
A{I^2} = B{I^2}\\
A{I^2} = C{I^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{(x – 4)^2} + {(y – 2)^2} + {z^2} = {(x – 2)^2} + {(y – 4)^2} + {z^2}\\
{(x – 4)^2} + {(y – 2)^2} + {z^2} = {(x – 2)^2} + {(y – 2)^2} + {(z – 1)^2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x – y = 0\\
4x – 2z = 11
\end{array} \right. .
$$

$\overrightarrow {BC}$, $\overrightarrow {AC}$, $\overrightarrow {AI}$ đồng phẳng $\Leftrightarrow [\overrightarrow {BC} ,\overrightarrow {AC} ].\overrightarrow {AI} = 0$ $\Leftrightarrow x + y + 2z = 6 .$

Giải hệ 
$$
\left\{ \begin{array}{l}
x – y = 0\\
4x – 2z = 11\\
x + y + 2z = 6
\end{array} \right.
$$
, ta được $I\left( {\frac{{23}}{8};\frac{{23}}{8};\frac{1}{4}} \right).$

<!-- chunk:10 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 1:

1. Trong không gian với hệ tọa độ $Oxyz$ cho ba véctơ $\overrightarrow a = 2\overrightarrow i + 3\overrightarrow j – 5\overrightarrow k$, $\overrightarrow b = – 3\overrightarrow j + 4\overrightarrow k$, $\overrightarrow c = – \overrightarrow i – 2\overrightarrow j .$

a) Xác định tọa độ các véctơ $\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c$, $\overrightarrow x = 3\overrightarrow a + 2\overrightarrow b$ và tính $\left| {\overrightarrow x } \right|.$

b) Tìm gi trị của $x$ để véctơ $\overrightarrow y = \left( {2x – 1; – x;3x + 2} \right)$ vuông góc với véctơ $2\overrightarrow b – \overrightarrow c .$

c) Chứng minh rằng các véctơ $\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c$ không đồng phẳng và phân tích véctơ $\overrightarrow u = \left( {3;7; – 14} \right)$ qua ba véctơ $\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c .$

2. Trong không gian với hệ trục tọa độ $Oxyz$, cho các véctơ $\overrightarrow a = 2\overrightarrow i + 3\overrightarrow j – \overrightarrow k$, $\overrightarrow b = – \overrightarrow i + 2\overrightarrow k$, $\overrightarrow c = 2\overrightarrow j – 3\overrightarrow k .$

a) Xác định tọa độ các véctơ $\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c .$

b) Tìm tọa độ véctơ $\overrightarrow u = 2\overrightarrow a + 3\overrightarrow b – 4\overrightarrow c$ và tính $\left| {\overrightarrow u } \right|.$

c) Tìm $x$ để véctơ $\overrightarrow v = (3x – 1;x + 2;3 – x)$ vuông góc với $\overrightarrow b .$

d) Biểu diễn véctơ $\overrightarrow x = (3;1;7)$ qua ba véctơ $\overrightarrow a$, $\overrightarrow b$, $\overrightarrow c .$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 2:

1. Cho hai véctơ $\vec a$, $\vec b$ có $\left| {\vec a} \right| = 2\sqrt 3$, $\left| {\vec b} \right| = 3,(\vec a,\vec b) = {30^0}.$ Tính:

a) Độ dài các véctơ $\vec a + \vec b$, $5\vec a + 2\vec b$, $3\vec a – 2\vec b.$

b) Độ dài véctơ $\left[ {\vec a,\vec b} \right]$, $\left[ {\vec a,3\vec b} \right]$, $\left[ {5\vec a, – 2\vec b} \right].$

2. Tìm điều kiện của tham số $m$ sao cho:

a) Ba véctơ $\vec u(2;1; – m)$, $\vec v(m + 1; – 2;0)$, $\vec w(1; – 1;2)$ đồng phẳng.

b) $A(1; – 1;m)$, $B(m;3;2m – 1)$, $C(4;3;1)$, $D(m + 3; – m;2 – m)$ cùng thuộc một mặt phẳng.

c) Góc giữa hai véctơ $\vec a(2;m;2m – 1)$, $\vec b(m;2; – 1)$ là ${60^0}.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 3: Cho tam giác $ABC$ có $B( – 1;1; – 1)$, $C(2;3;5).$ Điểm $A$ có tung độ là $\frac{1}{3},$ hình chiếu của điểm $A$ trên $BC$ là $K\left( 1;\frac{7}{3};3 \right)$ và diện tích tam giác $ABC$ là $S=\frac{49}{3}.$

1. Tìm tọa độ đỉnh $A$ biết $A$ có hoành độ dương.

2. Tìm tọa độ chân đường vuông góc hạ từ $B$ đến $AC.$

3. Tìm tọa độ tâm $I$ của đường tròn ngoại tiếp và tọa độ trực tâm $H$ của tam giác $ABC.$

4. Chứng minh $\overrightarrow{HG}=2\overrightarrow{GI}$ với $G$ là trọng tâm tam giác $ABC.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 4: Cho tứ diện $ABCD$ có các cặp cạnh đối bằng nhau. Tọa độ các điểm $A(2;4;1)$, $B(0;4;4)$, $C(0;0;1)$ và $D$ có hoành độ dương.

1. Xác định tọa độ điểm $D.$

2. Gọi $G$ là trọng tâm của tứ diện $ABCD.$ Chứng minh rằng $G$ cách đều các đỉnh của tứ diện.

3. Gọi $M,N$ lần lượt là trung điểm của $AB,CD.$ Chứng minh rằng $MN$ là đường vuông góc chung của hai đường thẳng $AB$ và $CD.$

4. Tính độ dài các đường trọng tuyến của tứ diện $ABCD.$ Tính tổng các góc phẳng ở mỗi đỉnh của tứ diện $ABCD.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 5: Trong không gian $Oxyz$ cho bốn điểm $A(0;2;0)$, $B( – 1;0; – 3)$, $C(0; – 2;0)$, $D(3;2;1).$

1. Chứng minh rằng bốn điểm $A$, $B$, $C$, $D$ không đồng phẳng.

2. Tính diện tích tam giác $BCD$ và đường cao $BH$ của tam giác $BCD.$

3. Tính thể tích tứ diện $ABCD$ và đường cao của tứ diện hạ từ $A.$

4. Tìm tọa độ $E$ sao cho $ABCE$ là hình bình hành.

5. Tính cosin của góc giữa hai đường thẳng $AC$ và $BD.$

6. Tìm điểm $M$ thuộc $Oy$ sao cho tam giác $BMC$ cân tại $M.$

7. Tìm tọa độ trọng tâm $G$ của tứ diện $ABCD$ và chứng minh $A$, $G$, $A’$ thẳng hàng với $A’$ là trọng tâm tam giác $BCD$.

<!-- chunk:15 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 6: Cho tam giác $ABC$ có $A(2;3;1)$, $B(-1;2;0)$, $C(1;1;-2).$

1. Tìm tọa độ chân đường vuông góc kẻ từ $A$ xuống $BC.$

2. Tìm tọa độ $H$ là trực tâm của tam giác $ABC.$

3. Tìm tọa độ $I$ là tâm đường tròn ngoại tiếp của tam giác $ABC.$

4. Gọi $G$ là trọng tâm của tam giác $ABC.$ Chứng minh rằng các điểm $G$, $H$, $I$ nằm trên một đường thẳng.

<!-- chunk:16 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 7: Trong không gian với hệ tọa độ Descartes vuông góc $Oxyz$ cho tam giác đều $ABC$ có $A(5;3;-1)$, $B(2;3;-4)$ và điểm $C$ nằm trong mặt phẳng $(Oxy)$ có tung độ nhỏ hơn $3.$

a) Tìm tọa độ điểm $D$ biết $ABCD$ là tứ diện đều.

b) Tìm tọa độ điểm $S$ biết $SA$, $SB$, $SC$ đôi một vuông góc.

<!-- chunk:17 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 8: Trong không gian với hệ tọa độ $Oxyz$ cho điểm $A\left( 3;-2;4 \right).$

a) Tìm tọa độ các hình chiếu của $A$ lên các trục tọa độ và các mặt phẳng tọa độ.

b) Tìm $M\in Ox$, $N\in Oy$ sao cho tam giác $AMN$ vuông cân tại $A.$

c) Tìm tọa độ điểm $E$ thuộc mặt phẳng $(Oyz)$ sao cho tam giác $AEB$ cân tại $E$ và có diện tích bằng $3\sqrt{29}$ với $B\left( -1;4;-4 \right) .$

<!-- chunk:18 level:4 source:https://toanmath.com/2019/03/xac-dinh-toa-do-diem-toa-do-vecto.html -->
## Bài tập 9: Trong không gian với hệ trục $Oxyz$ cho $A(4;0;0)$, $B({{x}_{0}};{{y}_{0}};0)$ với ${{x}_{0}},{{y}_{0}}>0$ thỏa mãn $AB=2\sqrt{10}$ và $\widehat{AOB}={{45}^{0}}.$

a) Tìm $C$ trên tia $Oz$ sao cho thể tích tứ diện $OABC$ bằng $8.$

b) Gọi $G$ là trọng tâm $\Delta ABO$ và $M$ trên cạnh $AC$ sao cho $AM=x.$ Tìm $x$ để $OM\bot GM.$