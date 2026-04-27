# Trục tọa độ và hệ trục tọa độ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
Bài viết giới thiệu lý thuyết và hướng dẫn giải một số dạng toán điển hình thuộc chủ đề trục tọa độ và hệ trục tọa độ trong chương trình Hình học 10 chương 1.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## I. TRỤC TỌA ĐỘ
1. Định nghĩa: Trục tọa độ (trục hay trục số) là một đường thẳng trên đó ta đã xác định một điểm $O$ và một vectơ đơn vị $\overrightarrow i$ (tức là $\left| {\overrightarrow i } \right| = 1$).

<img link="data_for_rag/toan10/images/truc-toa-do-va-he-truc-toa-do-1.png" alt="">

Điểm $O$ được gọi là gốc tọa độ, vectơ $\overrightarrow i$ được gọi là vectơ đơn vị của trục tọa độ. Kí hiệu $(O;\overrightarrow i )$ hay $x’Ox$ hoặc đơn giản là $Ox.$

2. Tọa độ của vectơ và của điểm trên trục
+ Cho vectơ $\overrightarrow u$ nằm trên trục $(O;\vec i)$ thì có số thực $a$ sao cho $\overrightarrow u = a\overrightarrow i$ với $a \in R.$ Số $a$ như thế được gọi là tọa độ của vectơ $\overrightarrow u$ đối với trục $(O;\overrightarrow i ).$

+ Cho điểm $M$ nằm trên $(O;\overrightarrow i )$ thì có số $m$ sao cho $\overrightarrow {OM} = m\overrightarrow i .$ Số $m$ như thế được gọi là tọa độ của điểm $M$ đối với trục $(O;\vec i).$

Như vậy tọa độ điểm $M$ là tọa độ vectơ $\overrightarrow {OM} .$

3. Độ dài đại số của vectơ trên trục

Cho hai điểm $A$, $B$ nằm trên trục $Ox$ thì tọa độ của vectơ $\overrightarrow {AB}$ kí hiệu là $\overline {AB}$ và gọi là độ dài đại số của vectơ $\overrightarrow {AB}$ trên trục $Ox.$

Như vậy $\overrightarrow {AB} = \overline {AB} .\overrightarrow i .$

Tính chất:

+ $\overline {AB} = – \overline {BA} .$

+ $\overrightarrow {AB} = \overrightarrow {CD} \Leftrightarrow \overline {AB} = \overline {CD} .$

+ $\forall A,B,C \in (O;\overrightarrow i )$: $\overline {AB} + \overline {BC} = \overline {AC} .$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## II. HỆ TRỤC TỌA ĐỘ
 1. Định nghĩa: Hệ trục tọa độ gồm hai trục vuông góc $Ox$ và $Oy$ với hai vectơ đơn vị lần lượt là $\overrightarrow i$, $\overrightarrow j .$ Điểm $O$ gọi là gốc tọa độ, $Ox$ gọi là trục hoành và $Oy$ gọi là trục tung. Kí hiệu $Oxy$ hay $(O;\overrightarrow i ,\overrightarrow j ).$

2. Tọa độ điểm, tọa độ vectơ

+ Trong hệ trục tọa độ $(O;\overrightarrow i ,\overrightarrow j )$ nếu $\overrightarrow u = x\overrightarrow i + y\overrightarrow j$ thì cặp số $(x;y)$ được gọi là tọa độ của vectơ $\overrightarrow u$, kí hiệu là $\overrightarrow u = (x;y)$ hay $\overrightarrow u (x;y).$

$x$ được gọi là hoành độ, $y$ được gọi là tung độ của vectơ $\overrightarrow u .$

+ Trong hệ trục tọa độ $(O;\overrightarrow i ,\overrightarrow j )$, tọa độ của vectơ $\overrightarrow {OM}$ gọi là tọa độ của điểm $M$, kí hiệu là $M = (x;y)$ hay $M(x;y).$ $x$ được gọi là hoành độ, $y$ được gọi là tung độ của điểm $M.$

<img link="data_for_rag/toan10/images/truc-toa-do-va-he-truc-toa-do-2.png" alt="">

Nhận xét: Gọi $H$, $K$ lần lượt là hình chiếu của $M$ lên $Ox$ và $Oy$ thì $M(x;y)$ $\Leftrightarrow \overrightarrow {OM} = x\vec i + y\vec j$ $= \overrightarrow {OH} + \overrightarrow {OK} .$

Như vậy $\overrightarrow {OH} = x\overrightarrow i$, $\overrightarrow {OK} = y\overrightarrow j$ hay $x = \overline {OH}$, $y = \overline {OK} .$

3. Tọa độ trung điểm của đoạn thẳng. Tọa độ trọng tâm tam giác
+ Cho $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$ và $M$ là trung điểm $AB.$ Tọa độ trung điểm $M\left( {{x_M};{y_M}} \right)$ của đoạn thẳng $AB$ là ${x_M} = \frac{{{x_A} + {x_B}}}{2}$, ${y_M} = \frac{{{y_A} + {y_B}}}{2}.$

+ Cho tam giác $ABC$ có $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$, $C\left( {{x_C};{y_C}} \right).$ Tọa độ trọng tâm $G\left( {{x_G};{y_G}} \right)$ của tam giác $ABC$ là ${x_G} = \frac{{{x_A} + {x_B} + {x_C}}}{3}$ và ${y_G} = \frac{{{y_A} + {y_B} + {y_C}}}{3}.$

4. Biểu thức tọa độ của các phép toán vectơ

Cho $\overrightarrow u = (x;y)$, $\overrightarrow {u’} = \left( {x’;y’} \right)$ và số thực $k.$ Khi đó ta có:

1) 
$$
\overrightarrow u = \overrightarrow {u’} \Leftrightarrow \left\{ {\begin{array}{l}
{x = x’}\\
{y = y’}
\end{array}} \right..
$$

2) $\vec u \pm \vec v = \left( {x \pm x’;y \pm y’} \right).$

3) $k\overrightarrow u = (kx;ky).$

4) $\overrightarrow {u’}$ cùng phương $\overrightarrow u$ $(\overrightarrow u \ne \vec 0)$ khi và chỉ khi có số $k$ sao cho 
$$
\left\{ {\begin{array}{l}
{x’ = kx}\\
{y’ = ky}
\end{array}} \right..
$$

5) Cho $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$ thì $\overrightarrow {AB} = \left( {{x_B} – {x_A};{y_B} – {y_A}} \right).$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI
DẠNG TOÁN 1: TÌM TỌA ĐỘ CỦA MỘT ĐIỂM – TỌA ĐỘ VECTƠ – ĐỘ DÀI ĐẠI SỐ CỦA VECTƠ VÀ CHỨNG MINH HỆ THỨC LIÊN QUAN TRÊN TRỤC $(O;\vec i).$
1. PHƯƠNG PHÁP GIẢI

Sử dụng các kiến thức cơ bản sau:

+ Điểm $M$ có tọa độ $a$ $\Leftrightarrow \overrightarrow {OM} = a\overrightarrow i .$

+ Vectơ $\overrightarrow {AB}$ có độ dài đại số là $m = \overline {AB} \Leftrightarrow \overrightarrow {AB} = m\overrightarrow i .$

+ Nếu $a$, $b$ lần lượt là tọa độ của $A$, $B$ thì $\overline {AB} = b – a.$

Các tính chất:

+ $\overline {AB} = – \overline {BA} .$

+ $\overrightarrow {AB} = \overrightarrow {CD} \Leftrightarrow \overline {AB} = \overline {CD} .$

+ $\forall A,B,C \in (O;\overrightarrow i )$: $\overline {AB} + \overline {BC} = \overline {AC} .$

2. CÁC VÍ DỤ

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 1: Trên trục tọa độ $(O;\overrightarrow i )$ cho ba điểm $A$, $B$, $C$ có tọa độ lần lượt là $– 2$, $1$ và $4.$

a) Tính tọa độ các vectơ $\overrightarrow {AB}$, $\overrightarrow {BC}$, $\overrightarrow {CA} .$

b) Chứng minh $B$ là trung điểm của $AC.$

a) Ta có $\overline {AB} = 1 + 2 = 3$, $\overline {BC} = 3$, $\overline {CA} = – 6.$

b) Ta có $\overline {BA} = – 3 = – \overline {BC}$ $\Rightarrow \overrightarrow {BA} = – \overrightarrow {BC}$ suy ra $B$ là trung điểm $AC.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 2: Trên trục tọa độ $(O;\overrightarrow i )$ cho $4$ điểm $A$, $B$, $C$, $D$ bất kỳ. Chứng minh $\overline {AB} .\overline {CD} + \overline {AC} .\overline {DB} + \overline {AD} .\overline {BC} = 0.$

Cách 1: Giả sử tọa độ các điểm $A$, $B$, $C$, $D$ lần lượt là $a$, $b$, $c$, $d.$

Ta có:

$\overline {AB} .\overline {CD} = (b – a)(d – c)$ $= bd + ac – bc – ad.$

$\overline {AC} .\overline {DB} = (c – a)(b – d)$ $= bc + ad – cd – ab.$

$\overline {AD} .\overline {BC} = (d – a)(c – b)$ $= cd + ab – ac – bd.$

Cộng vế với vế lại ta được $\overline {AB} .\overline {CD} + \overline {AC} .\overline {DB} + \overline {AD} .\overline {BC} = 0.$

Cách 2: $\overline {AB} .\overline {CD} + \overline {AC} .\overline {DB} + \overline {AD} .\overline {BC} .$

$= \overline {AB} .(\overline {AD} – \overline {AC} )$ $+ \overline {AC} .(\overline {AB} – \overline {AD} )$ $+ \overline {AD} .(\overline {AC} – \overline {AB} ).$

$= \overline {AB} .\overline {AD} – \overline {AB} .\overline {AC}$ $+ \overline {AC} .\overline {AB} – \overline {AC} .\overline {AD}$ $+ \overline {AD} .\overline {AC} – \overline {AD} .\overline {AB}$ $= 0.$

## Bài tập

## Bài 1: Trên trục tọa độ $(O;\overrightarrow i )$ cho hai điểm $A$ và $B$ có tọa độ lần lượt $a$ và $b.$

a) Tìm tọa độ điểm $M$ sao cho $\overrightarrow {MA} = k\overrightarrow {MB}$ $(k \ne 1).$

b) Tìm tọa độ trung điểm $I$ của $AB.$

c) Tìm tọa độ điểm $N$ sao cho $2\overline {NA} = – 5\overline {NB} .$

a) ${x_M} = \frac{{kb – a}}{{k – 1}}.$

b) ${x_1} = \frac{{a + b}}{2}.$

c) ${x_N} = \frac{{5b + 2a}}{7}.$

## Bài 2: Trên trục tọa độ $(O;\overrightarrow i )$ cho $4$ điểm $A$, $B$, $C$, $D$ có tọa độ lần lượt là $a$, $b$, $c$, $d$ và thỏa mãn hệ thức $2(ab + cd) = (a + b)(c + d).$ Chứng minh rằng $\frac{{\overline {DA} }}{{\overline {DB} }} = – \frac{{\overline {CA} }}{{\overline {CB} }}.$

Ta có: $\frac{{\overline {DA} }}{{\overline {DB} }} = – \frac{{\overline {CA} }}{{\overline {CB} }}$ $\Leftrightarrow \frac{{a – d}}{{b – d}} = – \frac{{a – c}}{{b – c}}.$

$\Leftrightarrow ab – ac – bd + cd$ $= bc – ab – cd + ad.$

$\Leftrightarrow 2(ab + cd)$ $= c(a + b) + d(a + b).$

$\Leftrightarrow 2(ab + cd)$ $= (a + b)(c + d).$

DẠNG TOÁN 2: TÌM TỌA ĐỘ ĐIỂM – TỌA ĐỘ VECTƠ TRÊN MẶT PHẲNG $Oxy.$

1. PHƯƠNG PHÁP

Để tìm tọa độ của vectơ $\overrightarrow a$ ta làm như sau: Dựng vectơ $\overrightarrow {OM} = \overrightarrow a .$ Gọi $H$, $K$ lần lượt là hình chiếu vuông góc của $M$ lên $Ox$, $Oy.$ Khi đó $\vec a\left( {{a_1};{a_2}} \right)$ với ${a_1} = \overline {OH}$, ${a_2} = \overline {OK} .$

Để tìm tọa độ điểm $A$ ta đi tìm tọa độ vectơ $\overrightarrow {OA} .$

Nếu biết tọa độ hai điểm $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$ suy ra tọa độ $\overrightarrow {AB}$ được xác định theo công thức $\overrightarrow {AB} = \left( {{x_B} – {x_A};{y_B} – {y_A}} \right).$

Chú ý: $\overline {OH} = OH$ nếu $H$ nằm trên tia $Ox$ (hoặc $Oy$) và $\overline {OH} = – OH$ nếu $H$ nằm trên tia đối tia $Ox$ (hoặc $Oy$).

2. CÁC VÍ DỤ

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 1: Trong mặt phẳng tọa độ $Oxy$, cho điểm $M(x;y).$ Tìm tọa độ của các điểm:

a) ${M_1}$ đối xứng với $M$ qua trục hoành.

b) ${M_2}$ đối xứng với $M$ qua trục tung.

c) ${M_3}$ đối xứng với $M$ qua gốc tọa độ.

<img link="data_for_rag/toan10/images/truc-toa-do-va-he-truc-toa-do-3.png" alt="">

a) ${M_1}$ đối xứng với $M$ qua trục hoành suy ra ${M_1}(x; – y).$

b) ${M_2}$ đối xứng với $M$ qua trục tung suy ra ${M_2}( – x;y).$

c) ${M_3}$ đối xứng với $M$ qua gốc tọa độ suy ra ${M_3}( – x; – y).$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 2: Trong hệ trục tọa độ $(O;\vec i,\vec j)$, cho hình vuông $ABCD$ tâm $I$ và có $A(1;3).$ Biết điểm $B$ thuộc trục $(O;\overrightarrow i )$ và $\overrightarrow {BC}$ cùng hướng với $\overrightarrow i .$ Tìm tọa độ các vectơ $\overrightarrow {AB}$, $\overrightarrow {BC}$ và $\overrightarrow {AC} .$

<img link="data_for_rag/toan10/images/truc-toa-do-va-he-truc-toa-do-4.png" alt="">

Từ giả thiết ta xác định được hình vuông trên mặt phẳng tọa độ (hình bên).

Vì điểm $A(1;3)$ suy ra $AB = 3$, $OB =1.$

Do đó $B(1;0)$, $C(4;0)$, $D(4;3).$

Vậy $\overrightarrow {AB} (0; – 3)$, $\overrightarrow {BC} (3;0)$ và $\overrightarrow {AC} (3; – 3).$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 3: Trong mặt phẳng tọa độ $Oxy.$ Cho hình thoi $ABCD$ cạnh $a$ và $\widehat {BAD} = {60^0}.$ Biết $A$ trùng với gốc tọa độ $O$, $C$ thuộc trục $Ox$ và ${x_B} \ge 0$, ${y_B} \ge 0.$ Tìm tọa độ các đỉnh của hình thoi $ABCD.$

<img link="data_for_rag/toan10/images/truc-toa-do-va-he-truc-toa-do-5.png" alt="">

Từ giả thiết ta xác định được hình thoi trên mặt phẳng tọa độ $Oxy.$

Gọi $I$ là tâm hình thoi ta có:

$BI = AB\sin \widehat {BAI}$ $= a\sin {30^0} = \frac{a}{2}.$

$AI = \sqrt {A{B^2} – B{I^2}}$ $= \sqrt {{a^2} – \frac{{{a^2}}}{4}} = \frac{{a\sqrt 3 }}{2}.$

Suy ra:

$A(0;0)$, $B\left( {\frac{{a\sqrt 3 }}{2};\frac{a}{2}} \right)$, $C(a\sqrt 3 ;0)$, $D\left( {\frac{{a\sqrt 3 }}{2}; – \frac{a}{2}} \right).$

## Bài tập
## Bài 1: Cho hình bình hành $ABCD$ có $AD = 4$ và chiều cao ứng với cạnh $AD = 3$, $\widehat {BAD} = {60^0}.$ Chọn hệ trục tọa độ $(A;\overrightarrow i ,\overrightarrow j )$ sao cho $\vec i$ và $\overrightarrow {AD}$ cùng hướng, ${y_B} > 0.$ Tìm tọa độ các vectơ $\overrightarrow {AB}$, $\overrightarrow {BC}$, $\overrightarrow {CD}$ và $\overrightarrow {AC} .$

Kẻ $BH \bot AD$ $\Rightarrow BH = 3$, $AB = 2\sqrt 3$, $AH = \sqrt 3 .$

$A(0;0)$, $B(\sqrt 3 ;3)$, $C(4 + \sqrt 3 ;3)$, $D(4;0).$

$\overrightarrow {AB} = (\sqrt 3 ;3)$, $\overrightarrow {BC} = (4;0)$, $\overrightarrow {CD} = ( – \sqrt 3 ; – 3)$, $\overrightarrow {AC} = (4 + \sqrt 3 ;3).$

## Bài 2: Cho lục giác đều $ABCDEF.$ Chọn hệ trục tọa độ $(O;\overrightarrow i ,\overrightarrow j )$ trong đó $O$ là tâm lục giác đều, $\vec i$ cùng hướng với $\overrightarrow {OD}$, $\overrightarrow j$ cùng hướng $\overrightarrow {EC} .$ Tính tọa độ các đỉnh lục giác đều, biết cạnh của lục giác là $6.$

$A( – 6;0)$, $D(6;0)$, $B( – 3;3\sqrt 3 )$, $C(3;3\sqrt 3 )$, $F( – 3; – 3\sqrt 3 )$, $E(3; – 3\sqrt 3 ).$

DẠNG TOÁN 3: XÁC ĐỊNH TỌA ĐỘ ĐIỂM – VECTƠ LIÊN QUAN ĐẾN BIỂU THỨC DẠNG $\vec u + \vec v$, $\vec u – \vec v$, $k\vec u.$

1. PHƯƠNG PHÁP

Dùng công thức tính tọa độ của vectơ $\vec u + \vec v$, $\vec u – \vec v$, $k\vec u.$

Với $\vec u = (x;y)$, $\overrightarrow {u’} = \left( {x’;y’} \right)$ và số thực $k$, khi đó $\vec u \pm \vec v = \left( {x \pm x’;y \pm y’} \right)$ và $k\overrightarrow u = (kx;ky).$

2. CÁC VÍ DỤ

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 1: Trong mặt phẳng $Oxy$, cho $3$ vectơ: $\vec a = (3;2)$, $\vec b = ( – 1;5)$, $\vec c = ( – 2; – 5).$ Tìm tọa độ của vectơ sau:

a) $\overrightarrow u + 2\overrightarrow v$ với $\vec u = 3\vec i – 4\vec j$ và $\vec v = \frac{\pi }{2}\vec i.$

b) $\overrightarrow k = 2\overrightarrow a + \overrightarrow b$ và $\overrightarrow l = – \overrightarrow a + 2\overrightarrow b + 5\overrightarrow c .$

a) Ta có: $\vec u + 2\vec v = 3\vec i – 4\vec j + \pi \vec i$ $= (3 + \pi )\vec i – 4\vec j$ suy ra $\overrightarrow u + 2\overrightarrow v = (3 + \pi ; – 4).$

b) Ta có $2\vec a = (6;4)$, $\vec b = ( – 1;5)$ suy ra $\vec k = (6 – 1;4 + 5) = (5;9).$

$– \vec a = ( – 3; – 2)$, $2\vec b = ( – 2;10)$ và $5\overrightarrow c = ( – 10; – 25)$ suy ra:

$\overrightarrow l = ( – 3 – 2 – 10; – 2 + 10 – 25)$ $= ( – 15; – 17).$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 2: Cho $\vec a = (1;2)$, $\vec b = ( – 3;4)$, $\vec c = ( – 1;3).$ Tìm tọa độ của vectơ $\overrightarrow u$ biết:

a) $2\overrightarrow u – 3\overrightarrow a + \overrightarrow b = \vec 0.$

b) $3\overrightarrow u + 2\overrightarrow a + 3\overrightarrow b = 3\overrightarrow c .$

a) Ta có: $2\overrightarrow u – 3\overrightarrow a + \overrightarrow b = \vec 0$ $\Leftrightarrow \overrightarrow u = \frac{3}{2}\overrightarrow a – \frac{1}{2}\overrightarrow b .$

Suy ra $\vec u = \left( {\frac{3}{2} + \frac{3}{2};3 – 2} \right) = (3;1).$

b) Ta có: $3\vec u + 2\vec a + 3\vec b = 3\vec c$ $\Leftrightarrow \vec u = – \frac{2}{3}\vec a – \vec b + \vec c.$

Suy ra: $\vec u = \left( { – \frac{2}{3} + 3 – 1; – \frac{4}{3} – 4 + 3} \right)$ $= \left( {\frac{4}{3}; – \frac{7}{3}} \right).$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 3: Cho ba điểm $A(-4;0)$, $B(0;3)$ và $C(2;1).$

a) Xác định tọa độ vectơ $\overrightarrow u = 2\overrightarrow {AB} – \overrightarrow {AC} .$

b) Tìm điểm $M$ sao cho $\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {MC} = \vec 0.$

a) Ta có: $\overrightarrow {AB} (4;3)$, $\overrightarrow {AC} (6;1)$ suy ra $\overrightarrow u = (2;5).$

b) Gọi $M(x;y)$, ta có: $\overrightarrow {MA} ( – 4 – x; – y)$, $\overrightarrow {MB} ( – x;3 – y)$, $\overrightarrow {MC} (2 – x;1 – y).$

Suy ra $\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {MC}$ $= ( – 6x + 2; – 6y + 9).$

Do đó $\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {MC} = \vec 0$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{ – 6x + 2 = 0}\\
{ – 6y + 9 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{1}{3}}\\
{y = \frac{3}{2}}
\end{array}} \right..
$$

Vậy $M\left( {\frac{1}{3};\frac{3}{2}} \right).$

## Bài tập
## Bài 1: Cho các vectơ $\vec a = (2;0)$, $\vec b = \left( { – 1;\frac{1}{2}} \right)$, $\vec c = (4;6).$ Tìm tọa độ vectơ $\overrightarrow u$ biết:

a) $\overrightarrow u = 2\overrightarrow a – 4\overrightarrow b + 5\overrightarrow c .$

b) $\vec a – 2\vec b + 2\vec u = \vec c.$

a) $\vec u = (28; – 28).$

b) $\overrightarrow u = \left( {0;\frac{7}{2}} \right).$

## Bài 2: Cho ba điểm $A(-4;0)$, $B(-5;0)$ và $C(3;-3).$

a) Tìm tọa độ vectơ $\overrightarrow u = \overrightarrow {AB} – 2\overrightarrow {BC} + 3\overrightarrow {CA} .$

b) Tìm điểm $M$ sao cho $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \vec 0.$

a) $\overrightarrow u ( – 38;3).$

b) $M( – 2; – 1).$

DẠNG TOÁN 4: XÁC ĐỊNH TỌA ĐỘ CÁC ĐIỂM CỦA MỘT HÌNH.

1. PHƯƠNG PHÁP

Dựa vào tính chất của hình và sử dụng công thức:

+ $M$ là trung điểm đoạn thẳng $AB$ suy ra ${x_M} = \frac{{{x_A} + {x_B}}}{2}$, ${y_M} = \frac{{{y_A} + {y_B}}}{2}.$

+ $G$ trọng tâm tam giác $ABC$ suy ra ${x_G} = \frac{{{x_A} + {x_B} + {x_C}}}{3}$, ${y_G} = \frac{{{y_A} + {y_B} + {y_C}}}{2}.$

+ $\vec u(x;y) = \overrightarrow {u’} \left( {x’;y’} \right)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = x’}\\
{y = y’}
\end{array}} \right..
$$

2. CÁC VÍ DỤ

<!-- chunk:12 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 1: Cho tam giác $ABC$ có $A(2;1)$, $B(-1;-2)$, $C(-3;2).$

a) Tìm tọa độ trung điểm $M$ sao cho $C$ là trung điểm của đoạn $MB.$

b) Xác định trọng tâm tam giác $ABC.$

c) Tìm điểm $D$ sao cho $ABCD$ là hình bình hành.

a) $C$ là trung điểm của $MB$ suy ra ${x_C} = \frac{{{x_M} + {x_B}}}{2}$ $\Rightarrow {x_M} = 2{x_C} – {x_B} = – 5$ và ${y_C} = \frac{{{y_M} + {y_B}}}{2}$ $\Rightarrow {y_M} = 2{y_C} – {y_B} = 6.$

Vậy $M( – 5;6).$

b) $G$ là trọng tâm tam giác suy ra:

${x_G} = \frac{{{x_A} + {x_B} + {x_C}}}{3}$ $= \frac{{2 – 1 – 3}}{3} = – \frac{2}{3}$ và ${y_G} = \frac{{{y_A} + {y_B} + {y_C}}}{2}$ $= \frac{{1 – 2 + 2}}{3} = \frac{1}{3}.$

Vậy $G\left( { – \frac{2}{3};\frac{1}{3}} \right).$

c) Gọi $D(x;y)$ $\Rightarrow \overrightarrow {DC} = ( – 3 – x;2 – y).$

Ta có: $ABCD$ là hình bình hành suy ra:

$\overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 3 – x = – 3}\\
{2 – y = – 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 5}
\end{array}} \right.
$$
 $\Rightarrow D(0;5).$

Vậy $D(0;5).$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 2: Trong mặt phẳng tọa độ $Oxy$ cho $A(3;-1)$, $B(-1;2)$ và $I(1;-1).$ Xác định tọa độ các điểm $C$, $D$ sao cho tứ giác $ABCD$ là hình bình hành, biết $I$ là trọng tâm tam giác $ABC.$ Tìm tọa độ tâm $O$ của hình bình hành $ABCD.$

Vì $I$ là trọng tâm tam giác $ABC$ nên:

${x_I} = \frac{{{x_A} + {x_B} + {x_C}}}{3}$ $\Rightarrow {x_C} = 3{x_I} – {x_A} – {x_B} = 1.$

${y_I} = \frac{{{y_A} + {y_B} + {y_C}}}{2}$ $\Rightarrow {y_C} = 3{y_I} – {y_A} – {y_B} = – 4.$

Suy ra $C(1;-4).$

Tứ giác $ABCD$ là hình bình hành suy ra:

$\overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 1 – 3 = 1 – {x_D}}\\
{2 + 1 = – 4 – {y_D}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_D} = 5}\\
{{y_D} = – 7}
\end{array}} \right.
$$
 $\Rightarrow D(5; – 7).$

Điểm $O$ của hình bình hành $ABCD$ suy ra $O$ là trung điểm $AC$ do đó:

${x_O} = \frac{{{x_A} + {x_C}}}{2} = 2$, ${y_O} = \frac{{{y_A} + {y_C}}}{2} = – \frac{5}{2}$ $\Rightarrow O\left( {2; – \frac{5}{2}} \right).$

## Bài tập
## Bài 1: Cho ba điểm $A(3;4)$, $B(2;1)$, $C(-1;-2).$

a) Tìm tọa độ trung điểm cạnh $BC$ và tọa độ trọng tâm của tam giác $ABC.$

b) Tìm tọa độ điểm $D$ sao cho $ABCD$ là hình bình hành.

a) Trung điểm $BC$ là $I\left( {\frac{1}{2}; – \frac{1}{2}} \right)$, trọng tâm của tam giác $ABC$ là $G\left( {\frac{4}{3};1} \right).$

b) Tứ giác $ABCD$ là hình bình hành $\Leftrightarrow \overrightarrow {AB} = \overrightarrow {DC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{y = 1}
\end{array}} \right.
$$
 $\Rightarrow D(0;1).$

## Bài 2: Trong mặt phẳng tọa độ $Oxy$ cho $A(3;4)$, $B(-1;2)$, $I(4;1).$ Xác định tọa độ các điểm $C$, $D$ sao cho tứ giác $ABCD$ là hình bình hành và $I$ là trung điểm cạnh $CD.$ Tìm tọa độ tâm $O$ của hình bình hành $ABCD.$

Do $I(4;-1)$ là trung điểm của $CD$ nên đặt:

$C(4 – x; – 1 – y)$, $D(4 + x; – 1 + y)$ $\Rightarrow \overrightarrow {CD} (2x;2y).$

Tứ giác $ABCD$ là hình bình hành $\Leftrightarrow \overrightarrow {CD} = \overrightarrow {BA}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 2}\\
{y = 1}
\end{array}} \right..
$$

Vậy $C(2; – 2)$, $D(6;0)$, $O\left( {\frac{9}{2};2} \right).$

## Bài 3: Cho tam giác $ABC$ có $A(3;1)$, $B(1;-3)$, đỉnh $C$ nằm trên $Oy$ và trọng tâm $G$ nằm trên trục $Ox.$ Tìm tọa độ đỉnh $C.$

Từ giả thiết ta có $C(0;y)$, $G(x;0).$

$G$ là trọng tâm tam giác nên 
$$
\left\{ {\begin{array}{l}
{{x_A} + {x_B} + {x_C} = 3{x_G}}\\
{{y_A} + {y_B} + {y_C} = 3{y_G}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{4}{3}}\\
{y = 2}
\end{array}} \right..
$$

Vậy $C(0;2).$

## Bài 4: Cho tam giác $ABC$ có $M$, $N$, $P$ lần lượt là trung điểm của $BC$, $CA$, $AB.$ Biết $M(1;1)$, $N(-2;-3)$, $P(2;-1).$ Tìm tọa độ các đỉnh của tam giác $ABC.$

Ta có $\overrightarrow {MN} ( – 3; – 4)$, $\overrightarrow {PA} \left( {{x_A} – 2;{y_A} + 1} \right)$, $\overrightarrow {MN} = \overrightarrow {PA} \Rightarrow A( – 1; – 5).$

$N$ là trung điểm $AC$ suy ra $C(-3;-1).$

$M$ là trung điểm $BC$ suy ra $B(5;3).$

## Bài 5: Cho tam giác $ABC$ có $A(3;4)$, $B(-1;2)$, $C(4;1).$ $A’$ là điểm đối xứng của $A$ qua $B$, $B’$ là điểm đối xứng của $B$ qua $C$, $C’$ là điểm đối xứng của $C$ qua $A.$

a) Tìm tọa độ các điểm $A’$, $B’$, $C’.$

b) Chứng minh các tam giác $ABC$ và $A’B’C’$ có cùng trọng tâm.

a) $A’$ là điểm đối xứng của $A$ qua $B$ suy ra $B$ là trung điểm của $AA’$ do đó $A'(-5;0).$ Tương tự $B'(9;0)$, $C'(2;7).$

b) Trọng tâm của tam giác $ABC$ và $A’B’C’$ có cùng tọa độ là $\left( {2;\frac{7}{3}} \right).$

DẠNG TOÁN 5: BÀI TOÁN LIÊN QUAN ĐẾN SỰ CÙNG PHƯƠNG CỦA HAI VECTƠ – PHÂN TÍCH MỘT VECTƠ QUA HAI VECTƠ KHÔNG CÙNG PHƯƠNG.

1. PHƯƠNG PHÁP

Cho $\overrightarrow u = (x;y)$, $\overrightarrow {u’} = \left( {x’;y’} \right).$ Vectơ $\overrightarrow {u’}$ cùng phương với vectơ $\overrightarrow u$ $(\overrightarrow u \ne \vec 0)$ khi và chỉ khi có số $k$ sao cho: 
$$
\left\{ {\begin{array}{l}
{x’ = kx}\\
{y’ = ky}
\end{array}} \right..
$$

Chú ý: Nếu $xy \ne 0$ ta có $\overrightarrow {u’}$ cùng phương $\vec u$ $\Leftrightarrow \frac{{x’}}{x} = \frac{{y’}}{y}.$

Để phân tích $\overrightarrow c \left( {{c_1};{c_2}} \right)$ qua hai vectơ $\vec a\left( {{a_1};{a_2}} \right)$, $\vec b\left( {{b_1};{b_2}} \right)$ không cùng phương, ta giả sử $\overrightarrow c = x\overrightarrow a + y\overrightarrow b .$ Khi đó ta quy về giải hệ phương trình 
$$
\left\{ {\begin{array}{l}
{{a_1}x + {b_1}y = {c_1}}\\
{{a_2}x + {b_2}y = {c_2}}
\end{array}} \right..
$$

2. CÁC VÍ DỤ

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 1: Cho $\vec a = (1;2)$, $\vec b = ( – 3;0)$, $\vec c = ( – 1;3).$

a) Chứng minh hai vectơ $\vec a$, $\vec b$ không cùng phương.

b) Phân tích vectơ $\overrightarrow c$ qua $\overrightarrow a$ và $\overrightarrow b .$

a) Ta có: $\frac{{ – 3}}{1} \ne \frac{0}{2}$ $\Rightarrow \overrightarrow a$ và $\overrightarrow b$ không cùng phương.

b) Giả sử $\overrightarrow c = x\overrightarrow a + y\overrightarrow b .$ Ta có $x\vec a + y\vec b = (x – 3y;2x).$

Suy ra 
$$
\left\{ {\begin{array}{l}
{x – 3y = – 1}\\
{2x = 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{2}{3}}\\
{y = \frac{5}{9}}
\end{array}} \right.
$$
 $\Rightarrow \vec c = \frac{2}{3}\vec a + \frac{5}{9}\vec b.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 2: Cho $\overrightarrow u = \left( {{m^2} + m – 2;4} \right)$ và $\overrightarrow v = (m;2).$ Tìm $m$ để hai vectơ $\overrightarrow u$, $\overrightarrow v$ cùng phương.

+ Với $m = 0$: Ta có $\overrightarrow u = ( – 2;4)$, $\overrightarrow v = (0;2).$

Vì $\frac{0}{{ – 2}} \ne \frac{2}{4}.$ nên hai vectơ $\overrightarrow u$, $\overrightarrow v$ không cùng phương.

+ Với $m \ne 0$: Ta có $\overrightarrow u$, $\overrightarrow v$ cùng phương khi và chỉ khi:

$\frac{{{m^2} + m – 2}}{m} = \frac{4}{2}$ $\Leftrightarrow {m^2} – m – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – 1}\\
{m = 2}
\end{array}} \right..
$$

Vậy với $m = -1$ và $m = 2$ là các giá trị cần tìm.

<!-- chunk:16 level:3 source:https://toanmath.com/2019/08/truc-toa-do-va-he-truc-toa-do.html -->
## Ví dụ 3: Trong mặt phẳng tọa độ $Oxy$, cho ba điểm $A(6;3)$, $B(-3;6)$, $C(1;-2).$

a) Chứng minh $A$, $B$, $C$ là ba đỉnh một tam giác.

b) Xác định điểm $D$ trên trục hoành sao cho ba điểm $A$, $B$, $D$ thẳng hàng.

c) Xác định điểm $E$ trên cạnh $BC$ sao cho $BE = 2EC.$

d) Xác định giao điểm hai đường thẳng $DE$ và $AC.$

a) Ta có $\overrightarrow {AB} ( – 9;3)$, $\overrightarrow {AC} ( – 5; – 5).$ Vì $\frac{{ – 9}}{{ – 5}} \ne \frac{3}{{ – 5}}$ suy ra $\overrightarrow {AB}$ và $\overrightarrow {AC}$ không cùng phương.

Hay $A$, $B$, $C$ là ba đỉnh một tam giác.

b) $D$ trên trục hoành $\Rightarrow D(x;0).$

Ba điểm $A$, $B$, $D$ thẳng hàng suy ra $\overrightarrow {AB}$ và $\overrightarrow {AD}$ cùng phương.

Mặt khác $\overrightarrow {AD} (x – 6; – 3)$ do đó $\frac{{x – 6}}{{ – 9}} = \frac{{ – 3}}{3}$ $\Rightarrow x = 15.$

Vậy $D(15;0).$

c) Vì $E$ thuộc đoạn $BC$ và $BE = 2EC$ suy ra $\overrightarrow {BE} = 2\overrightarrow {EC} .$

Gọi $E(x;y)$ khi đó $\overrightarrow {BE} (x + 3;y – 6)$, $\overrightarrow {EC} (1 – x; – 2 – y).$

Do đó 
$$
\left\{ {\begin{array}{l}
{x + 3 = 2(1 – x)}\\
{y – 6 = 2( – 2 – y)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = – \frac{1}{3}}\\
{y = \frac{2}{3}}
\end{array}} \right..
$$

Vậy $E\left( { – \frac{1}{3};\frac{2}{3}} \right).$

d) Gọi $I(x;y)$ là giao điểm của $DE$ và $AC.$

Do đó $\overrightarrow {DI} (x – 15;y)$, $\overrightarrow {DE} \left( { – \frac{{46}}{3};\frac{2}{3}} \right)$ cùng phương, suy ra:

$\frac{{3(x – 15)}}{{ – 46}} = \frac{{3y}}{2}$ $\Rightarrow x + 23y – 15 = 0$ $(1).$

$\overrightarrow {AI} (x – 6;y – 3)$, $\overrightarrow {AC} ( – 5; – 5)$ cùng phương, suy ra:

$\frac{{x – 6}}{{ – 5}} = \frac{{y – 3}}{{ – 5}}$ $\Rightarrow x – y – 3 = 0$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $x = \frac{7}{2}$ và $y = \frac{1}{2}.$

Vậy giao điểm hai đường thẳng $DE$ và $AC$ là $I\left( {\frac{7}{2};\frac{1}{2}} \right).$

## Bài tập
## Bài 1: Trong mặt phẳng tọa độ $Oxy$ cho $4$ điểm $A(1;-2)$, $B(0;3)$, $C(-3;4)$ và $D(-1;8).$

a) Bộ ba trong $4$ điểm trên bộ nào thẳng hàng.

b) Chứng minh $\overrightarrow {AB}$ và $\overrightarrow {AC}$ không cùng phương.

c) Phân tích $\overrightarrow {CD}$ qua $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

a) $A$, $B$, $D$ thẳng hàng.

b) $\overrightarrow {AB} ( – 1;5)$, $\overrightarrow {AC} ( – 4;6).$ Vì $\frac{{ – 1}}{{ – 4}} \ne \frac{5}{6}$ $\Rightarrow \overrightarrow {AB}$ và $\overrightarrow {AC}$ không cùng phương.

c) $\overrightarrow {CD} (2;4)$. $\overrightarrow {CD} = x\overrightarrow {AB} + y\overrightarrow {AC}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – x – 4y = 2}\\
{5x + 6y = 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 2}\\
{y = – 1}
\end{array}} \right.
$$
 $\Rightarrow \overrightarrow {CD} = 2\overrightarrow {AB} – \overrightarrow {AC} .$

## Bài 2: Trong mặt phẳng tọa độ $Oxy$ cho $4$ điểm $A(0;1)$, $B(1;3)$, $C(2;7)$ và $D(0;3).$ Tìm giao điểm của $2$ đường thẳng $AC$ và $BD.$

Gọi $I(x;y)$ là giao điểm $AC$ và $BD$ suy ra $\overrightarrow {AI}$, $\overrightarrow {AC}$ cùng phương và $\overrightarrow {BI}$, $\overrightarrow {BD}$ cùng phương.

Mặt khác: $\overrightarrow {AI} = (x;y – 1)$, $\overrightarrow {AC} = (2;6)$ suy ra $\frac{x}{2} = \frac{{y – 1}}{6}$ $\Leftrightarrow 6x – 2y = – 2$ $(1).$

$\overrightarrow {BI} = (x – 1;y – 3)$, $\overrightarrow {BD} = ( – 1;0)$ suy ra $y = 3$, thế vào $(1)$ ta có $x = \frac{2}{3}.$

Vậy $I\left( {\frac{2}{3};3} \right)$ là điểm cần tìm.

## Bài 3: Cho $\vec a = (3;2)$, $\vec b = ( – 3;1).$

a) Chứng minh $\overrightarrow a$ và $\overrightarrow b$ không cùng phương.

b) Đặt $\vec u = (2 – x)\vec a + (3 + y)\vec b.$ Tìm $x$, $y$ sao cho $\overrightarrow u$ cùng phương với $x\vec a + \vec b$ và $\vec a + \vec b.$

a) $\overrightarrow a$ và $\overrightarrow b$ không cùng phương.

b) Ta có $\vec u = ( – 3x – 3y – 3; – 2x + y + 7).$

$x\vec a + \vec b = (3x – 3;2x + 1)$, $\vec a + \vec b = (0;3).$

$\overrightarrow u$ cùng phương với $x\vec a + \vec b$ và $\vec a + \vec b$ khi và chỉ khi có số $k$, $l$ sao cho $\vec u = k(x\vec a + \vec b)$, $\vec u = l(\vec a + \vec b).$

Do đó: 
$$
\left\{ \begin{array}{l}
– 3x – 3y – 3 = k(3x – 3)\\
– 2x + y + 7 = k(2x + 1)\\
– 3x – 3y – 3 = 0\\
– 2x + y + 7 = 3l
\end{array} \right..
$$

Suy ra 
$$
\left\{ {\begin{array}{c}
{x = 2}\\
{y = – 3}
\end{array}} \right.
$$
 hoặc 
$$
\left\{ {\begin{array}{c}
{x = 1}\\
{y = – 2}
\end{array}} \right..
$$

## Bài 4: Cho tam giác $ABC$ có $A(3;4)$, $B(2;1)$, $C(-1;-2).$ Tìm điểm $M$ trên đường thẳng $BC$ sao cho ${S_{ABC}} = 3{S_{ABM}}.$

Ta có ${S_{ABC}} = 3{S_{ABM}}$ $\Leftrightarrow BC = 3BM$ $\Rightarrow \overrightarrow {BC} = \pm 3\overrightarrow {BM} .$

Gọi $M(x;y)$ $\Rightarrow \overrightarrow {BM} (x – 2;y – 1)$, $\overrightarrow {BC} ( – 3; – 3).$

Suy ra 
$$
\left\{ {\begin{array}{l}
{ – 3 = 3(x – 2)}\\
{ – 3 = 3(y – 1)}
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
{ – 3 = – 3(x – 2)}\\
{ – 3 = – 3(y – 1)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 3}\\
{y = 2}
\end{array}} \right..
$$

Vậy có hai điểm thỏa mãn: ${M_1}(1;0)$, ${M_2}(3;2).$

## Bài 5: Cho ba điểm $A(-1;-1)$, $B(0;1)$, $C(3;0).$

a) Chứng minh ba điểm $A$, $B$, $C$ tạo thành một tam giác.

b) Xác định tọa độ điểm $D$ biết $D$ thuộc đoạn thẳng $BC$ và $2BD = 5DC.$

c) Xác định tọa độ giao điểm của $AD$ và $BG$ trong đó $G$ là trọng tâm tam giác $ABC.$

a) Ta có $\overrightarrow {AB} (1;2)$, $\overrightarrow {AC} (4;1).$ Vì $\frac{1}{4} \ne \frac{2}{1}$ $\Rightarrow \overrightarrow {AB}$ và $\overrightarrow {AC}$ không cùng phương.

b) Ta có $2\overrightarrow {BD} = 5\overrightarrow {DC}$, $\overrightarrow {BD} \left( {{x_D};{y_D} – 1} \right)$, $\overrightarrow {DC} \left( {3 – {x_D}; – {y_D}} \right).$

Do đó 
$$
\left\{ {\begin{array}{c}
{2{x_D} = 5\left( {3 – {x_D}} \right)}\\
{2\left( {{y_D} – 1} \right) = 5\left( { – {y_D}} \right)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_D} = \frac{{15}}{7}}\\
{{y_D} = \frac{2}{7}}
\end{array}} \right.
$$
 $\Rightarrow D\left( {\frac{{15}}{7};\frac{2}{7}} \right).$

c) Ta có $G\left( {\frac{2}{3};0} \right).$ Gọi $I(x;y)$ là giao điểm của $AD$ và $BG.$

Do đó $\overrightarrow {AI} (x + 1;y + 1)$, $\overrightarrow {AD} \left( {\frac{{22}}{7};\frac{9}{7}} \right)$ cùng phương suy ra:

$\frac{{7(x + 1)}}{{22}} = \frac{{7(y + 1)}}{9}$ $\Rightarrow 9x – 22y – 13 = 0.$

$\overrightarrow {BI} (x;y – 1)$, $\overrightarrow {BG} \left( { – \frac{1}{3};0} \right)$ cùng phương suy ra tồn tại $k$: $\overrightarrow {BI} = k\overrightarrow {BG}$ $\Rightarrow y = 1.$

Từ đó $I\left( {\frac{{35}}{9};1} \right).$

## Bài 6: Tìm trên trục hoành điểm $P$ sao cho tổng khoảng cách từ $P$ tới hai điểm $A$ và $B$ là nhỏ nhất, biết:

a) $A(1;1)$ và $B(2;-4).$

b) $A(1;2)$ và $B(3;4).$

a) Dễ thấy điểm $A$, $B$ nằm ở hai phía với trục hoành.

Ta có $PA + PB \ge AB.$ Dấu bằng xảy ra $\Leftrightarrow \overrightarrow {AP}$ cùng phương với $\overrightarrow {AB} .$

Suy ra $\frac{{{x_P} – 1}}{{2 – 1}} = \frac{{0 – 1}}{{ – 4 – 1}}$ $\Rightarrow {x_P} = \frac{6}{5}$ $\Rightarrow P\left( {\frac{6}{5};0} \right).$

b) Dễ thấy $A$, $B$ cùng phía với trục hoành. Gọi $A’$ là điểm đối xứng với $A$ qua trục hoành, suy ra $A'(1;-2)$ và $PA = PA’.$

Ta có $PA + PB = PA’ + PB \ge A’B.$ Dấu bằng xảy ra $\Leftrightarrow \overrightarrow {A’P}$ cùng phương với $\overrightarrow {A’B} .$

Suy ra $\frac{{{x_P} – 1}}{{3 – 1}} = \frac{{0 + 2}}{{4 + 2}}$ $\Rightarrow {x_P} = \frac{5}{3}$ $\Rightarrow P\left( {\frac{5}{3};0} \right).$

## Bài 7: Cho hình bình hành $ABCD$ có $A(-2;3)$ và tâm $I(1;1).$ Biết điểm $K(-1;2)$ nằm trên đường thẳng $AB$ và điểm $D$ có hoành độ gấp đôi tung độ. Tìm các đỉnh còn lại của hình bình hành.

$I$ là trung điểm $AC$ nên $C(4;-1).$

Gọi $D(2a;a)$ $\Rightarrow B(2 – 2a;2 – a).$

$\overrightarrow {AK} (1; – 1)$, $\overrightarrow {AB} (4 – 2a; – 1 – a).$

Vì $\overrightarrow {AK}$, $\overrightarrow {AB}$ cùng phương nên $\frac{{4 – 2a}}{1} = \frac{{ – 1 – a}}{{ – 1}}$ $\Rightarrow a = 1$ $\Rightarrow D(2;1)$, $B(0;1).$