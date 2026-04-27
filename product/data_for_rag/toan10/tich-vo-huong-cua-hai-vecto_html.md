# Tích vô hướng của hai vectơ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
Bài viết tóm tắt lý thuyết và hướng dẫn phương pháp giải một số dạng toán điển hình thuộc chủ đề tích vô hướng của hai vectơ trong chương trình Hình học 10.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## A. TÓM TẮT LÝ THUYẾT

1. Định nghĩa

a) Góc giữa hai vectơ

Cho hai vectơ $\overrightarrow a$ và $\overrightarrow b$ đều khác $\vec 0.$ Từ điểm $O$ bất kỳ dựng các vectơ $\overrightarrow {OA} = \overrightarrow a$ và $\overrightarrow {OB} = \overrightarrow b .$ Số đo góc $AOB$ được gọi là số đo góc giữa hai vectơ $\overrightarrow a$ và $\overrightarrow b .$

Quy ước: Nếu $\overrightarrow a = \vec 0$ hoặc $\overrightarrow b = \vec 0$ thì ta xem góc giữa hai vectơ $\vec a$ và $\vec b$ là tùy ý (từ ${0^0}$ đến ${180^0}$).

Kí hiệu: $(\vec a;\vec b).$

b) Tích vô hướng của hai vectơ

Tích vô hướng của hai vectơ $\overrightarrow a$ và $\overrightarrow b$ là một số thực được xác định bởi:

$\vec a.\vec b = |\vec a||\vec b|.\cos (\vec a,\vec b).$

2. Tính chất: Với ba vectơ bất kì $\vec a$, $\vec b$, $\vec c$ và mọi số thực $k$ ta luôn có:

1) $\overrightarrow a .\overrightarrow b = \overrightarrow b .\overrightarrow a .$

2) $\vec a(\vec b \pm \vec c) = \vec a.\vec b \pm \vec a.\vec c.$

3) $(k\overrightarrow a )\overrightarrow b = k(\overrightarrow a .\overrightarrow b ) = \overrightarrow a (k\overrightarrow b ).$

4) ${\vec a^2} \ge 0$, ${\vec a^2} = 0 \Leftrightarrow \vec a = \vec 0.$

Chú ý: Ta có kết quả sau:

+ Nếu hai vectơ $\overrightarrow a$ và $\overrightarrow b$ khác $\vec 0$ thì $\vec a \bot \vec b \Leftrightarrow \vec a.\vec b = 0.$

+ $\vec a.\vec a = {\vec a^2} = |\vec a{|^2}$ gọi là bình phương vô hướng của vectơ $\overrightarrow a .$

+ ${(\vec a \pm \vec b)^2} = {\vec a^2} \pm 2\vec a.\vec b + {\vec b^2}$, $(\vec a + \vec b)(\vec a – \vec b) = {\vec a^2} – {\vec b^2}.$

3. Công thức hình chiếu và phương tích của một điểm với đường tròn

a) Công thức hình chiếu

Cho hai vectơ $\overrightarrow {AB}$, $\overrightarrow {CD} .$ Gọi $A’$, $B’$ lần lượt là hình chiếu của $A$, $B$ lên đường thẳng $CD$, khi đó ta có $\overrightarrow {AB} .\overrightarrow {CD} = \overrightarrow {A’B’} .\overrightarrow {CD} .$

b) Phương tích của một điểm với đường tròn

Cho đường tròn $(O;R)$ và điểm $M.$ Một đường thẳng qua $M$ cắt đường tròn tại hai điểm $A$ và $B.$ Biểu thức $\overrightarrow {MA} .\overrightarrow {MB}$ được gọi là phương tích của điểm $M$ đối với đường tròn $(O;R)$. Kí hiệu là ${P_{M/(O)}}.$

Chú ý: Ta có ${P_{M/(O)}} = \overrightarrow {MA} .\overrightarrow {MB}$ $= M{O^2} – {R^2} = M{T^2}$ với $T$ là tiếp điểm của tiếp tuyến kẻ từ điểm $M.$

4. Biểu thức tọa độ của tích vô hướng

Cho hai vectơ $\vec a = \left( {{x_1};{y_1}} \right)$ và $\vec b = \left( {{x_2};{y_2}} \right).$ Khi đó:

1) $\vec a.\vec b = {x_1}{x_2} + {y_1}{y_2}.$

2) $\overrightarrow a = (x;y)$ $\Rightarrow |\overrightarrow a | = \sqrt {{x^2} + {y^2}} .$

3) $\cos (\vec a,\vec b) = \frac{{\vec a.\vec b}}{{|\vec a||\vec b|}}$ $= \frac{{{x_1}{x_2} + {y_1}{y_2}}}{{\sqrt {x_1^2 + y_1^2} \sqrt {x_2^2 + y_2^2} }}.$

Hệ quả:

+ $\vec a \bot \vec b$ $\Leftrightarrow {x_1}{x_2} + {y_1}{y_2} = 0.$

+ Nếu $A\left( {{x_A};{y_A}} \right)$ và $B\left( {{x_B};{y_B}} \right)$ thì $AB = \sqrt {{{\left( {{x_B} – {x_A}} \right)}^2} + {{\left( {{y_B} – {y_A}} \right)}^2}} .$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI

DẠNG TOÁN 1: XÁC ĐỊNH BIỂU THỨC TÍCH VÔ HƯỚNG – GÓC GIỮA HAI VECTƠ.

1. PHƯƠNG PHÁP GIẢI

Dựa vào định nghĩa $\vec a.\vec b = |\vec a|.|\vec b|\cos (\vec a;\vec b).$

Sử dụng tính chất và các hằng đẳng thức của tích vô hướng của hai vectơ.

2. CÁC VÍ DỤ

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 1: Cho tam giác $ABC$ vuông tại $A$ có $AB = a$, $BC = 2a$ và $G$ là trọng tâm.

a) Tính các tích vô hướng: $\overrightarrow {BA} .\overrightarrow {BC}$, $\overrightarrow {BC} .\overrightarrow {CA} .$

b) Tính giá trị của biểu thức: $\overrightarrow {AB} .\overrightarrow {BC} + \overrightarrow {BC} .\overrightarrow {CA} + \overrightarrow {CA} .\overrightarrow {AB} .$

c) $\overrightarrow {GA} .\overrightarrow {GB} + \overrightarrow {GB} .\overrightarrow {GC} + \overrightarrow {GC} .\overrightarrow {GA} .$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-1.png" alt="">

a) Theo định nghĩa tích vô hướng ta có:

$\overrightarrow {BA} .\overrightarrow {BC}$ $= |\overrightarrow {BA} |.|\overrightarrow {BC} |\cos (\overrightarrow {BA} ,\overrightarrow {BC} )$ $= 2{a^2}\cos (\overrightarrow {BA} ,\overrightarrow {BC} ).$

Mặt khác $\cos (\overrightarrow {BA} ,\overrightarrow {BC} )$ $= \cos \widehat {ABC}$ $= \frac{a}{{2a}} = \frac{1}{2}.$

Nên $\overrightarrow {BA} .\overrightarrow {BC} = {a^2}.$

Ta có $\overrightarrow {BC} .\overrightarrow {CA} = – \overrightarrow {CB} .\overrightarrow {CA}$ $= – |\overrightarrow {CB} |.|\overrightarrow {CA} |\cos \widehat {ACB}.$

Theo định lý Pitago ta có $CA = \sqrt {{{(2a)}^2} – {a^2}} = a\sqrt 3 .$

Suy ra $\overrightarrow {BC} .\overrightarrow {CA}$ $= – a\sqrt 3 .2a.\frac{{a\sqrt 3 }}{{2a}} = – 3{a^2}.$

b) Cách 1: Vì tam giác $ABC$ vuông tại $A$ nên $\overrightarrow {CA} .\overrightarrow {AB} = 0$ và từ câu a ta có: $\overrightarrow {AB} .\overrightarrow {BC} = – {a^2}$, $\overrightarrow {BC} .\overrightarrow {CA} = – 3{a^2}.$

Suy ra $\overrightarrow {AB} .\overrightarrow {BC} + \overrightarrow {BC} .\overrightarrow {CA} + \overrightarrow {CA} .\overrightarrow {AB} = – 4{a^2}.$

Cách 2: Từ $\overrightarrow {AB} + \overrightarrow {BC} + \overrightarrow {CA} = \vec 0$ và hằng đẳng thức:

${(\overrightarrow {AB} + \overrightarrow {BC} + \overrightarrow {CA} )^2}$ $= A{B^2} + B{C^2} + C{A^2}$ $+ 2(\overrightarrow {AB} .\overrightarrow {BC} + \overrightarrow {BC} .\overrightarrow {CA} + \overrightarrow {CA} .\overrightarrow {AB} ).$

Ta có: $\overrightarrow {AB} .\overrightarrow {BC} + \overrightarrow {BC} .\overrightarrow {CA} + \overrightarrow {CA} .\overrightarrow {AB}$ $= – \frac{1}{2}\left( {A{B^2} + B{C^2} + C{A^2}} \right)$ $= – 4{a^2}.$

c) Tương tự cách 2 của câu b vì: $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ nên:

$\overrightarrow {GA} .\overrightarrow {GB} + \overrightarrow {GB} .\overrightarrow {GC} + \overrightarrow {GC} .\overrightarrow {GA}$ $= – \frac{1}{2}\left( {G{A^2} + G{B^2} + G{C^2}} \right).$

Gọi $M$, $N$, $P$ lần lượt là trung điểm của $BC$, $CA$, $AB.$

Dễ thấy tam giác $ABM$ đều nên $G{A^2} = {\left( {\frac{2}{3}AM} \right)^2} = \frac{{4{a^2}}}{9}.$

Theo định lý Pitago ta có:

$G{B^2} = \frac{4}{9}B{N^2}$ $= \frac{4}{9}\left( {A{B^2} + A{N^2}} \right)$ $= \frac{4}{9}\left( {{a^2} + \frac{{3{a^2}}}{4}} \right)$ $= \frac{{7{a^2}}}{9}.$

$G{C^2} = \frac{4}{9}C{P^2}$ $= \frac{4}{9}\left( {A{C^2} + A{P^2}} \right)$ $= \frac{4}{9}\left( {3{a^2} + \frac{{{a^2}}}{4}} \right)$ $= \frac{{13{a^2}}}{9}.$

Suy ra: $\overrightarrow {GA} .\overrightarrow {GB} + \overrightarrow {GB} .\overrightarrow {GC} + \overrightarrow {GC} .\overrightarrow {GA}$ $= – \frac{1}{2}\left( {\frac{{4{a^2}}}{9} + \frac{{7{a^2}}}{9} + \frac{{13{a^2}}}{9}} \right)$ $= – \frac{{4{a^2}}}{3}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 2: Cho hình vuông $ABCD$ cạnh $a.$ $M$ là trung điểm của $AB$, $G$ là trọng tâm tam giác $ADM.$ Tính giá trị các biểu thức sau:

a) $(\overrightarrow {AB} + \overrightarrow {AD} )(\overrightarrow {BD} + \overrightarrow {BC} ).$

b) $\overrightarrow {CG} .(\overrightarrow {CA} + \overrightarrow {DM} ).$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-2.png" alt="">

a) Theo quy tắc hình bình hành ta có $\overrightarrow {AB} + \overrightarrow {AD} = \overrightarrow {AC} .$

Do đó $(\overrightarrow {AB} + \overrightarrow {AD} )(\overrightarrow {BD} + \overrightarrow {BC} )$ $= \overrightarrow {AC} .\overrightarrow {BD} + \overrightarrow {AC} .\overrightarrow {BC}$ $= \overrightarrow {CA} .\overrightarrow {CB}$ $= |\overrightarrow {CA} |.|\overrightarrow {CB} |\cos \widehat {ACB}$ ($\overrightarrow {AC} .\overrightarrow {BD} = 0$ vì $\overrightarrow {AC} \bot \overrightarrow {BD}$).

Mặt khác $\widehat {ACB} = {45^0}$ và theo định lý Pitago ta có:

$AC = \sqrt {{a^2} + {a^2}} = a\sqrt 2 .$

Suy ra $(\overrightarrow {AB} + \overrightarrow {AD} )(\overrightarrow {BD} + \overrightarrow {BC} )$ $= a.a\sqrt 2 \cos {45^0} = {a^2}.$

b) Vì $G$ là trọng tâm tam giác $ADM$ nên $\overrightarrow {CG} = \overrightarrow {CD} + \overrightarrow {CA} + \overrightarrow {CM} .$

Mặt khác theo quy tắc hình bình hành và hệ thức trung điểm ta có:

$\overrightarrow {CA} = – (\overrightarrow {AB} + \overrightarrow {AD} ).$

$\overrightarrow {CM} = \frac{1}{2}(\overrightarrow {CB} + \overrightarrow {CA} )$ $= \frac{1}{2}[\overrightarrow {CB} – (\overrightarrow {AB} + \overrightarrow {AD} )]$ $= – \frac{1}{2}(\overrightarrow {AB} + 2\overrightarrow {AD} ).$

Suy ra $\overrightarrow {CG} = – \overrightarrow {AB} – (\overrightarrow {AB} + \overrightarrow {AD} )$ $– \frac{1}{2}(\overrightarrow {AB} + 2\overrightarrow {AD} )$ $= – \left( {\frac{5}{2}\overrightarrow {AB} + 2\overrightarrow {AD} } \right).$

Ta lại có $\overrightarrow {CA} + \overrightarrow {DM}$ $= – (\overrightarrow {AB} + \overrightarrow {AD} ) + \overrightarrow {AM} – \overrightarrow {AD}$ $= – \left( {\frac{1}{2}\overrightarrow {AB} + 2\overrightarrow {AD} } \right).$

Nên $\overrightarrow {CG} .(\overrightarrow {CA} + \overrightarrow {DM} )$ $= \left( {\frac{5}{2}\overrightarrow {AB} + 2\overrightarrow {AD} } \right)\left( {\frac{1}{2}\overrightarrow {AB} + 2\overrightarrow {AD} } \right)$ $= \frac{5}{4}A{B^2} + 4A{D^2}$ $= \frac{{21{a^2}}}{4}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 3: Cho tam giác $ABC$ có $BC = a$, $CA = b$, $AB = c.$ $M$ là trung điểm của $BC$, $D$ là chân đường phân giác trong góc $A.$

a) Tính $\overrightarrow {AB} .\overrightarrow {AC}$ rồi suy ra $\cos A.$

b) Tính ${\overrightarrow {AM} ^2}$ và ${\overrightarrow {AD} ^2}.$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-3.png" alt="">

a) Ta có $\overrightarrow {AB} .\overrightarrow {AC}$ $= \frac{1}{2}\left[ {{{\overrightarrow {AB} }^2} + {{\overrightarrow {AC} }^2} – {{(\overrightarrow {AB} – \overrightarrow {AC} )}^2}} \right]$ $= \frac{1}{2}\left[ {A{B^2} + A{C^2} – C{B^2}} \right]$ $= \frac{1}{2}\left( {{c^2} + {b^2} – {a^2}} \right).$

Mặt khác $\overrightarrow {AB} .\overrightarrow {AC}$ $= AB.AC\cos A$ $= cb\cos A.$

Suy ra $\frac{1}{2}\left( {{c^2} + {b^2} – {a^2}} \right) = cb\cos A$ hay $\cos A = \frac{{{c^2} + {b^2} – {a^2}}}{{2bc}}.$

b) Vì $M$ là trung điểm của $BC$ nên $\overrightarrow {AM} = \frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} ).$

Suy ra ${\overrightarrow {AM} ^2} = \frac{1}{4}{(\overrightarrow {AB} + \overrightarrow {AC} )^2}$ $= \frac{1}{4}\left( {{{\overrightarrow {AB} }^2} + 2\overrightarrow {AB} .\overrightarrow {AC} + {{\overrightarrow {AC} }^2}} \right).$

Theo câu a ta có: $\overrightarrow {AB} .\overrightarrow {AC} = \frac{1}{2}\left( {{c^2} + {b^2} – {a^2}} \right)$ nên ${\overrightarrow {AM} ^2}$ $= \frac{1}{4}\left( {{c^2} + 2.\frac{1}{2}\left( {{c^2} + {b^2} – {a^2}} \right) + {b^2}} \right)$ $= \frac{{2\left( {{b^2} + {c^2}} \right) – {a^2}}}{4}.$

Theo tính chất đường phân giác thì $\frac{{BD}}{{DC}} = \frac{{AB}}{{AC}} = \frac{c}{b}.$

Suy ra $\overrightarrow {BD} = \frac{{BD}}{{DC}}\overrightarrow {DC} = \frac{b}{c}\overrightarrow {DC}$ $(*).$

Mặt khác $\overrightarrow {BD} = \overrightarrow {AD} – \overrightarrow {AB}$ và $\overrightarrow {DC} = \overrightarrow {AC} – \overrightarrow {AD}$ thay vào $(*)$ ta được:

$\overrightarrow {AD} – \overrightarrow {AB}$ $= \frac{b}{c}(\overrightarrow {AC} – \overrightarrow {AD} )$ $\Leftrightarrow (b + c)\overrightarrow {AD} = b\overrightarrow {AB} + c\overrightarrow {AC} .$

$\Leftrightarrow {(b + c)^2}{\overrightarrow {AD} ^2}$ $= {(b\overrightarrow {AB} )^2} + 2bc\overrightarrow {AB} .\overrightarrow {AC} + {(c\overrightarrow {AC} )^2}.$

$\Leftrightarrow {(b + c)^2}{\overrightarrow {AD} ^2}$ $= {b^2}{c^2} + 2bc.\frac{1}{2}\left( {{c^2} + {b^2} – {a^2}} \right) + {c^2}{b^2}.$

$\Leftrightarrow {\overrightarrow {AD} ^2}$ $= \frac{{bc}}{{{{(b + c)}^2}}}(b + c – a)(b + c + a).$

Hay ${\overrightarrow {AD} ^2} = \frac{{4bc}}{{{{(b + c)}^2}}}p(p – a).$

Nhận xét: Từ câu b suy ra độ dài đường phân giác kẻ từ đỉnh $A$ là:

${l_a} = \frac{{2\sqrt {bc} }}{{b + c}}\sqrt {p(p – a)} .$

## Bài tập
## Bài 1: Cho tam giác $ABC$ đều cạnh bằng $a.$ Tính các tích vô hướng:

a) $\overrightarrow {AB} .\overrightarrow {AC} .$

b) $\overrightarrow {AC} .\overrightarrow {CB} .$

c) $\overrightarrow {AB} .\overrightarrow {BC} .$

## Bài 2: Cho tam giác $ABC$ có $AB = 5$, $BC =7$, $AC = 8.$

a) Tính $\overrightarrow {AB} .\overrightarrow {AC}$ rồi suy ra giá trị của góc $A.$

b) Tính $\overrightarrow {AC} .\overrightarrow {BC} .$

c) Gọi $D$ là điểm trên $CA$ sao cho $CD = 3.$ Tính $\overrightarrow {CD} .\overrightarrow {CB} .$

## Bài 3: Cho các vectơ $\overrightarrow a$, $\overrightarrow b$ có độ dài bằng $1$ và thoả mãn điều kiện $|2\vec a – 3\vec b| = \sqrt 7 .$ Tính $\cos (\overrightarrow a ,\overrightarrow b ).$

## Bài 4: Cho các vectơ $\vec a$, $\vec b$ có độ dài bằng $1$ và góc tạo bởi hai vectơ bằng ${60^0}.$ Xác định cosin góc giữa hai vectơ $\overrightarrow u$ và $\overrightarrow v$ với $\overrightarrow u = \overrightarrow a + 2\overrightarrow b$, $\overrightarrow v = \overrightarrow a – \overrightarrow b .$

## Bài 5: Cho hình vuông $ABCD$ cạnh bằng $3.$ Trên cạnh $AB$ lấy điểm $M$ sao cho $BM = 1$, trên cạnh $CD$ lấy điểm $N$ sao cho $DN =1$ và $P$ là trung điểm $BC.$ Tính $\cos \widehat {MNP}.$

## Bài 6: Cho hình chữ nhật $ABCD$ có $AB = 2.$ $M$ là điểm được xác định bởi $\overrightarrow {AM} = 3\overrightarrow {MB}$, $G$ là trọng tâm tam giác $ADM.$ Tính $\overrightarrow {MB} .\overrightarrow {GC} .$

## Bài 7: Cho tứ giác $ABCD.$ Gọi $M$, $N$ lần lượt là trung điểm của $DA$, $BC.$ Tính góc giữa hai đường thẳng $AB$ và $CD$ biết $AB = CD = 2a$, $MN = a\sqrt 3 .$

## Bài 8: Cho tứ giác $ABCD$ có $AB = BC = 2\sqrt 5$, $CD = BD = 5\sqrt 2$, $BD = 3\sqrt {10}$, $AC = 10.$ Tìm góc giữa hai vectơ $\overrightarrow {AC}$, $\overrightarrow {DB} .$

## Bài 9: Cho tam giác $ABC$ đều có cạnh bằng $1.$ Gọi $D$ là điểm đối xứng với $C$ qua đường thẳng $AB$, $M$ là trung điểm của cạnh $CB.$

a) Xác định trên đường thẳng $AC$ điểm $N$ sao cho tam giác $MDN$ vuông tại $D.$ Tính diện tích tam giác đó.

b) Xác định trên đường thẳng $AC$ điểm $P$ sao cho tam giác $MPD$ vuông tại $M.$ Tính diện tích tam giác đó.

c) Tính côsin góc hợp bởi hai đường thẳng $MP$ và $PD.$

DẠNG TOÁN 2: CHỨNG MINH CÁC ĐẲNG THỨC VỀ TÍCH VÔ HƯỚNG HOẶC ĐỘ DÀI CỦA ĐOẠN THẲNG.
1. PHƯƠNG PHÁP GIẢI

Nếu trong đẳng thức chứa bình phương độ dài của đoạn thẳng thì ta chuyển về vectơ nhờ đẳng thức $A{B^2} = {\overrightarrow {AB} ^2}.$

Sử dụng các tính chất của tích vô hướng, các quy tắc phép toán vectơ.

Sử dụng hằng đẳng thức vectơ về tích vô hướng.

2. CÁC VÍ DỤ

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 1: Cho $I$ là trung điểm của đoạn thẳng $AB$ và $M$ là điểm tùy ý. Chứng minh rằng: $\overrightarrow {MA} .\overrightarrow {MB} = I{M^2} – I{A^2}.$

Đẳng thức cần chứng minh được viết lại là $\overrightarrow {MA} .\overrightarrow {MB} = {\overrightarrow {IM} ^2} – {\overrightarrow {IA} ^2}.$

Để làm xuất hiện $\overrightarrow {IM}$, $\overrightarrow {IA}$ ở VP, sử dụng quy tắc ba điểm để xen điểm $I$ vào, ta được:

$VT = (\overrightarrow {MI} + \overrightarrow {IA} ).(\overrightarrow {MI} + \overrightarrow {IB} )$ $= (\overrightarrow {MI} + \overrightarrow {IA} ).(\overrightarrow {MI} – \overrightarrow {IA} )$ $= {\overrightarrow {IM} ^2} – {\overrightarrow {IA} ^2} = VP.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 2: Cho bốn điểm $A$, $B$, $C$, $D$ bất kì. Chứng minh rằng:

$\overrightarrow {DA} .\overrightarrow {BC} + \overrightarrow {DB} .\overrightarrow {CA} + \overrightarrow {DC} .\overrightarrow {AB} = 0$ $(*).$

Từ đó suy ra một cách chứng minh định lí: “Ba đường cao trong tam giác đồng quy”.

Ta có: $\overrightarrow {DA} .\overrightarrow {BC} + \overrightarrow {DB} .\overrightarrow {CA} + \overrightarrow {DC} .\overrightarrow {AB} .$

$= \overrightarrow {DA} .(\overrightarrow {DC} – \overrightarrow {DB} )$ $+ \overrightarrow {DB} .(\overrightarrow {DA} – \overrightarrow {DC} )$ $+ \overrightarrow {DC} .(\overrightarrow {DB} – \overrightarrow {DA} ).$

$= \overrightarrow {DA} .\overrightarrow {DC} – \overrightarrow {DA} .\overrightarrow {DB}$ $+ \overrightarrow {DB} .\overrightarrow {DA} – \overrightarrow {DB} .\overrightarrow {DC}$ $+ \overrightarrow {DC} .\overrightarrow {DB} – \overrightarrow {DC} .\overrightarrow {DA} = 0.$

Gọi $H$ là giao của hai đường cao xuất phát từ đỉnh $A$, $B.$

Khi đó ta có: $\overrightarrow {HA} .\overrightarrow {BC} = 0$, $\overrightarrow {HC} .\overrightarrow {AB} = 0$ $(1).$

Từ đẳng thức $(*)$ ta cho điểm $D$ trùng với điểm $H$ ta được:

$\overrightarrow {HA} .\overrightarrow {BC} + \overrightarrow {HB} .\overrightarrow {CA} + \overrightarrow {HC} .\overrightarrow {AB} = 0$ $(2).$

Từ $(1)$ và $(2)$ ta có $\overrightarrow {HB} .\overrightarrow {CA} = 0$ suy ra $BH$ vuông góc với $AC.$

Hay ba đường cao trong tam giác đồng quy.

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 3: Cho nửa đường tròn đường kính $AB.$ Có $AC$ và $BD$ là hai dây thuộc nửa đường tròn cắt nhau tại $E.$ Chứng minh rằng: $\overrightarrow {AE} .\overrightarrow {AC} + \overrightarrow {BE} .\overrightarrow {BD} = A{B^2}.$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-4.png" alt="">

Ta có $VT = \overrightarrow {AE} .(\overrightarrow {AB} + \overrightarrow {BC} )$ $+ \overrightarrow {BE} .(\overrightarrow {BA} + \overrightarrow {AD} ).$

$= \overrightarrow {AE} .\overrightarrow {AB} + \overrightarrow {AE} .\overrightarrow {BC}$ $+ \overrightarrow {BE} .\overrightarrow {BA} + \overrightarrow {BE} .\overrightarrow {AD} .$

Vì $AB$ là đường kính nên $\widehat {ADB} = {90^0}$, $\widehat {ACB} = {90^0}.$

Suy ra $\overrightarrow {AE} .\overrightarrow {BC} = 0$, $\overrightarrow {BE} .\overrightarrow {AD} = 0.$

Do đó $VT = \overrightarrow {AE} .\overrightarrow {AB} + \overrightarrow {BE} .\overrightarrow {BA}$ $= \overrightarrow {AB} (\overrightarrow {AE} + \overrightarrow {EB} )$ $= {\overrightarrow {AB} ^2} = VP.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 4: Cho tam giác $ABC$ có $BC = a$, $CA = b$, $AB = c$ và $I$ là tâm đường tròn nội tiếp. Chứng minh rằng $aI{A^2} + bI{B^2} + cI{C^2} = abc.$

Ta có: $a\overrightarrow {IA} + b\overrightarrow {IB} + c\overrightarrow {IC} = \vec 0$ $\Rightarrow {(a\overrightarrow {IA} + b\overrightarrow {IB} + c\overrightarrow {IC} )^2} = 0.$

$\Rightarrow {a^2}I{A^2} + {b^2}I{B^2} + {c^2}I{C^2}$ $+ 2ab\overrightarrow {IA} .\overrightarrow {IB} + 2bc\overrightarrow {IB} .\overrightarrow {IC} + 2ca\overrightarrow {IC} .\overrightarrow {IA} = 0.$

$\Rightarrow {a^2}I{A^2} + {b^2}I{B^2} + {c^2}I{C^2}$ $+ ab\left( {I{A^2} + I{B^2} – A{B^2}} \right)$ $+ bc\left( {I{B^2} + I{C^2} – B{C^2}} \right)$ $+ ca\left( {I{A^2} + I{C^2} – C{A^2}} \right) = 0.$

$\Rightarrow \left( {{a^2} + ab + ca} \right)I{A^2}$ $+ \left( {{b^2} + ba + bc} \right)I{B^2}$ $+ \left( {{c^2} + ca + cb} \right)I{C^2}$ $– \left( {ab{c^2} + a{b^2}c + {a^2}bc} \right) = 0.$

$\Rightarrow (a + b + c)\left( {{a^2}I{A^2} + {b^2}I{B^2} + {c^2}I{C^2}} \right)$ $= (a + b + c)abc.$

$\Rightarrow {a^2}I{A^2} + {b^2}I{B^2} + {c^2}I{C^2} = abc.$

## Bài tập
## Bài 1: Cho tam giác $ABC$ với ba trung tuyến $AD$, $BE$, $CF.$ Chứng minh rằng: $\overrightarrow {BC} .\overrightarrow {AD} + \overrightarrow {CA} .\overrightarrow {BE} + \overrightarrow {AB} .\overrightarrow {CF} = 0.$

## Bài 2: Cho hình chữ nhật $ABCD$ có tâm $O$ và $M$ là một điểm bất kì. Chứng minh rằng:

a) $\overrightarrow {MA} .\overrightarrow {MC} = \overrightarrow {MB} .\overrightarrow {MD} .$

b) $M{A^2} + \overrightarrow {MB} .\overrightarrow {MD} = 2\overrightarrow {MA} .\overrightarrow {MO} .$

## Bài 3: Cho tam giác $ABC$ có trực tâm $H$, $M$ là trung điểm của $BC.$ Chứng minh rằng $\overrightarrow {MH} .\overrightarrow {MA} = \frac{1}{4}B{C^2}.$

## Bài 4: Cho tam giác $ABC$ có trọng tâm $G$ và $BC = a$, $CA = b$, $AB = c.$ Chứng minh rằng: $G{A^2} + G{B^2} + G{C^2}$ $= \frac{1}{3}\left( {{a^2} + {b^2} + {c^2}} \right).$

## Bài 5: Cho tam giác $ABC$ có ba đường cao là $AA’$, $BB’$, $CC’.$ Gọi $M$, $N$, $P$ lần lượt là trung điểm của $BC$, $CA$, $AB.$ Chứng minh rằng $\overrightarrow {A’M} .\overrightarrow {BC} + \overrightarrow {B’N} .\overrightarrow {CA} + \overrightarrow {C’P} .\overrightarrow {AB} = 0.$

## Bài 6: Cho hình bình hành $ABCD.$ Gọi $M$ là một điểm tùy ý. Chứng minh rằng: $\overrightarrow {MA} .\overrightarrow {MC} – \overrightarrow {MB} .\overrightarrow {MD} = \overrightarrow {BA} .\overrightarrow {BC} .$

## Bài 7: Cho hai điểm $M$, $N$ nằm trên đường tròn đường kính $AB = 2R.$ Gọi $I$ là giao điểm của hai đường thẳng $AM$ và $BN.$

a) Chứng minh: $\overrightarrow {AM} .\overrightarrow {AI} = \overrightarrow {AB} .\overrightarrow {AI}$, $\overrightarrow {BN} .\overrightarrow {BI} = \overrightarrow {BA} .\overrightarrow {BI} .$

b) Tính $\overrightarrow {AM} .\overrightarrow {AI} + \overrightarrow {BN} .\overrightarrow {BI}$ theo $R.$

## Bài 8: Cho tam giác $ABC$, $M$ là một điểm bất kỳ trên cạnh $BC$ không trùng với $B$ và $C.$ Gọi $a$, $b$, $c$ lần lượt là độ dài các cạnh $BC$, $CA$, $AB.$ Chứng minh rằng: $A{M^2} = {b^2}B{M^2} + {c^2}C{M^2}$ $+ \left( {{b^2} + {c^2} – {a^2}} \right)BM.CM.$

## Bài 9: Cho lục giác $ABCDEF$ có $AB$ vuông góc với $EF$ và hai tam giá $ACE$ và $BDF$ có cùng trọng tâm. Chứng minh rằng $A{B^2} + E{F^2} = C{D^2}.$

## Bài 10: Cho tam giác $ABC$ cạnh $a$ nội tiếp đường tròn $(O).$ $M$ là điểm bất kì nằm trên đường tròn $(O).$ Chứng minh rằng $M{A^2} + M{B^2} + M{C^2} = 2{a^2}.$

## Bài 11: Cho hình vuông $ABCD$ nội tiếp đường tròn $(O;R).$ $MN$ là một đường kính bất kỳ của đường tròn $(O;R).$

a) Chứng minh rằng $M{A^2} + M{B^2} + M{C^2} + M{D^2} = 8{R^2}.$

b) Chứng minh rằng $M{A^4} + M{B^4} + M{C^4} + M{D^4}$ $= N{A^4} + N{B^4} + N{C^4} + N{D^4}.$

## Bài 12: Cho tứ giác $ABCD.$ Chứng minh rằng $\overrightarrow {AB} .\overrightarrow {AD} + \overrightarrow {BA} .\overrightarrow {BC} + \overrightarrow {CB} .\overrightarrow {CD} + \overrightarrow {DC} .\overrightarrow {DA} = 0$ khi và chỉ khi tứ giác $ABCD$ là hình bình hành.

## Bài 13: Cho lục giác đều ${A_1}{A_2}{A_3}{A_4}{A_5}{A_6}$ tâm $I$ và đường tròn $(O;R)$ bất kỳ chứa $I.$ Các tia $I{A_i}$ $\left( {i = \overline {1,6} } \right)$ cắt $(O)$ tại ${B_i}$ $\left( {i = \overline {1,6} } \right).$ Chứng minh rằng $IB_1^2 + IB_2^2 + IB_3^2$ $+ IB_4^2 + IB_5^2 + IB_6^2$ $= 6{R^2}.$

## Bài 14: Tam giác $ABC$ có trọng tâm $G.$ Chứng minh rằng:

a) $M{A^2} + M{B^2} + M{C^2}$ $= 3M{G^2} + G{A^2} + G{B^2} + G{C^2}$ với $M$ là điểm bất kỳ.

b) ${a^2} + {b^2} + {c^2} \le 9{R^2}$

## Bài 15: Cho tam giác $ABC$ có $\widehat {BAC} < {90^0}$, $BC = a$, $CA = b$, $AB = c.$ $M$ là điểm nằm trong tam giác $ABC$ và nằm trên đường trên đường tròn đường kính $BC.$ Gọi $x$, $y$, $z$ theo thứ tự là diện tích của các tam giác $MBC$, $MCA$, $MAB.$ Chứng minh rằng $(x – y + z){c^2}$ $+ (x – z + y){b^2}$ $= \left( {x + y + z + \frac{{2yz}}{x}} \right){a^2}.$

DẠNG TOÁN 3: TÌM TẬP HỢP ĐIỂM THỎA MÃN ĐẲNG THỨC VỀ TÍCH VÔ HƯỚNG HOẶC TÍCH ĐỘ DÀI.

1. PHƯƠNG PHÁP GIẢI

Ta sử dụng các kết quả cơ bản sau:

Cho $A$, $B$ là các điểm cố định. $M$ là điểm di động.

+ Nếu $|\overrightarrow {AM} | = k$ với $k$ là số thực dương cho trước thì tập hợp các điểm $M$ là đường tròn tâm $A$, bán kính $R = k.$

+ Nếu $\overrightarrow {MA} .\overrightarrow {MB} = 0$ thì tập hợp các điểm $M$ là đường tròn đường kính $AB.$

+ Nếu $\overrightarrow {MA} .\overrightarrow a = 0$ với $\overrightarrow a$ khác $\vec 0$ cho trước thì tập hợp các điểm $M$ là đường thẳng đi qua $A$ và vuông góc với giá của vectơ $\overrightarrow a .$

2. CÁC VÍ DỤ

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 1. Cho hai điểm $A$, $B$ cố định có độ dài bằng $a$, vectơ $\vec a$ khác $\vec 0$ và số thực $k$ cho trước. Tìm tập hợp điểm $M$ sao cho:

a) $\overrightarrow {MA} .\overrightarrow {MB} = \frac{{3{a^2}}}{4}.$

b) $\overrightarrow {MA} .\overrightarrow {MB} = M{A^2}.$

a) Gọi $I$ là trung điểm của $AB$ ta có:

$\overrightarrow {MA} .\overrightarrow {MB} = \frac{{3{a^2}}}{4}$ $\Leftrightarrow (\overrightarrow {MI} + \overrightarrow {IA} )(\overrightarrow {MI} + \overrightarrow {IB} ) = \frac{{3{a^2}}}{4}.$

$\Leftrightarrow M{I^2} – I{A^2} = \frac{{3{a^2}}}{4}$ (do $\overrightarrow {IB} = – \overrightarrow {IA}$).

$\Leftrightarrow M{I^2} = \frac{{{a^2}}}{4} + \frac{{3{a^2}}}{4}$ $\Leftrightarrow MI = a.$

Vậy tập hợp điểm $M$ là đường tròn tâm $I$ bán kính $R = a.$

b) Ta có $\overrightarrow {MA} .\overrightarrow {MB} = M{A^2}$ $\Leftrightarrow \overrightarrow {MA} .\overrightarrow {MB} = {\overrightarrow {MA} ^2}.$

$\Leftrightarrow \overrightarrow {MA} .(\overrightarrow {MA} – \overrightarrow {MB} ) = 0$ $\Leftrightarrow \overrightarrow {MA} .\overrightarrow {BA} = 0$ $\Leftrightarrow \overrightarrow {MA} \bot \overrightarrow {BA} .$

Vậy tập hợp điểm $M$ là đường thẳng vuông góc với đường thẳng $AB$ tại $A.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 2: Cho tam giác $ABC.$ Tìm tập hợp điểm $M$ sao cho $(\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {CB} )\overrightarrow {BC} = 0.$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-5.png" alt="">

Gọi $I$ là điểm xác định bởi $\overrightarrow {IA} + 2\overrightarrow {IB} = \vec 0.$

Khi đó $(\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {CB} )\overrightarrow {BC} = 0.$

$\Leftrightarrow \left[ {(\overrightarrow {MI} + \overrightarrow {IA} ) + 2(\overrightarrow {MI} + \overrightarrow {IB} )} \right].\overrightarrow {BC}$ $= 3B{C^2}.$

$\Leftrightarrow \overrightarrow {MI} .\overrightarrow {BC} = B{C^2}.$

Gọi $M’$, $I’$ lần lượt là hình chiếu của $M$, $I$ lên đường thẳng $BC.$

Theo công thức hình chiếu ta có $\overrightarrow {MI} .\overrightarrow {BC} = \overrightarrow {M’I’} .\overrightarrow {BC}$, do đó $\overrightarrow {M’I’} .\overrightarrow {BC} = B{C^2}.$

Vì $B{C^2} > 0$ nên $\overrightarrow {M’I’}$, $\overrightarrow {BC}$ cùng hướng suy ra:

$\overrightarrow {M’I’} .\overrightarrow {BC} = B{C^2}$ $\Leftrightarrow M’I’.BC = B{C^2}$ $\Leftrightarrow M’I’ = BC.$

Do $I$ cố định nên $I’$ cố định suy ra $M’$ cố định.

Vậy tập hợp điểm $M$ là đường thẳng đi qua $M’$ và vuông góc với $BC.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 3: Cho hình vuông $ABCD$ cạnh $a$ và số thực $k$ cho trước. Tìm tập hợp điểm $M$ sao cho $\overrightarrow {MA} .\overrightarrow {MC} + \overrightarrow {MB} .\overrightarrow {MD} = k.$

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-6.png" alt="">

Gọi $I$ là tâm của hình vuông $ABCD.$

Ta có: $\overrightarrow {MA} .\overrightarrow {MC}$ $= (\overrightarrow {MI} + \overrightarrow {IA} )(\overrightarrow {MI} + \overrightarrow {IC} )$ $= M{I^2} + \overrightarrow {MI} (\overrightarrow {IC} + \overrightarrow {IA} ) + \overrightarrow {IA} .\overrightarrow {IC}$ $= M{I^2} + \overrightarrow {IA} .\overrightarrow {IC} .$

Tương tự $\overrightarrow {MB} .\overrightarrow {MD} = M{I^2} + \overrightarrow {IB} .\overrightarrow {ID} .$

Nên $\overrightarrow {MA} .\overrightarrow {MC} + \overrightarrow {MB} .\overrightarrow {MD} = k$ $\Leftrightarrow 2M{I^2} + \overrightarrow {IB} .\overrightarrow {ID} + \overrightarrow {IA} .\overrightarrow {IC} = k.$

$\Leftrightarrow 2M{I^2} – I{B^2} – I{A^2} = k$ $\Leftrightarrow M{I^2} = \frac{k}{2} + I{A^2}$ $\Leftrightarrow M{I^2} = \frac{k}{2} + {a^2}.$

$\Leftrightarrow MI = \sqrt {\frac{k}{2} + I{A^2}}$ $= \sqrt {\frac{{k + {a^2}}}{2}} .$

Nếu $k < – {a^2}$: Tập hợp điểm $M$ là tập rỗng.

Nếu $k = – {a^2}$ thì $MI = 0$ $\Leftrightarrow M \equiv I$ suy ra tập hợp điểm $M$ là điểm $I.$

Nếu $k > – {a^2}$ thì $MI = \sqrt {\frac{{k + {a^2}}}{2}} .$

Suy ra tập hợp điểm $M$ là đường tròn tâm $I$ bán kính $R = \sqrt {\frac{{k + {a^2}}}{2}} .$

## Bài tập
## Bài 1: Cho đoạn thẳng $AB.$ Tìm tập hợp điểm $M$ trong mỗi trường hợp sau:

a) $2M{A^2} = \overrightarrow {MA} .\overrightarrow {MB} .$

b) $M{A^2} + 2M{B^2} = k$ với $k$ là số thực dương cho trước.

c) $\overrightarrow {AM} .\vec a = k$ với $k$ là số thực cho trước.

## Bài 2: Cho tam giác $ABC.$ Tìm tập hợp điểm $M$ trong các trường hợp sau:

a) $(\overrightarrow {MA} – \overrightarrow {MB} )(2\overrightarrow {MB} – \overrightarrow {MC} ) = 0.$

b) $(\overrightarrow {MA} + 2\overrightarrow {MB} )(\overrightarrow {MB} + 2\overrightarrow {MC} ) = 0.$

c) $2M{A^2} + \overrightarrow {MA} .\overrightarrow {MB} = \overrightarrow {MA} .\overrightarrow {MC} .$

## Bài 3: Cho hình vuông $ABCD$ cạnh $a.$ Tìm tập hợp các điểm $M$ sao cho:

a) $2M{A^2} + M{B^2} = M{C^2} + M{D^2}.$

b) $(\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} )(\overrightarrow {MC} – \overrightarrow {MB} ) = 3{a^2}.$

## Bài 4: Cho tứ giác $ABCD$, $I$, $J$ lần lượt là trung điểm của $AB$ và $CD.$ Tìm tập hợp điểm $M$ sao cho: $\overrightarrow {MA} .\overrightarrow {MB} + \overrightarrow {MC} .\overrightarrow {MD} = \frac{1}{2}I{J^2}.$

## Bài 5: Cho tam giác $ABC$ đều cạnh bằng $a.$ Tìm tập hợp những điểm $M$ sao cho: $\overrightarrow {MA} .\overrightarrow {MB} + \overrightarrow {MB} .\overrightarrow {MC} + \overrightarrow {MC} .\overrightarrow {MA} = \frac{{{a^2}}}{4}.$

## Bài 6: Cho tam giác $ABC$, góc $A$ nhọn, trung tuyến $AI.$ Tìm tập hợp những điểm $M$ di động trong góc $BAC$ sao cho: $AB.AH + AC.AK = A{I^2}$ trong đó $H$ và $K$ theo thứ tự là hình chiếu vuông góc của $M$ lên $AB$ và $AC.$

## Bài 7: Cho tam giác $ABC$ và $k$ là số thực cho trước. Tìm tập hợp những điểm $M$ sao cho $M{A^2} – M{B^2} = k.$

## Bài 8: Cho tam giác $ABC.$ Tìm tập hợp những điểm $M$ sao cho $\alpha M{A^2} + \beta M{B^2} + \gamma M{C^2} = k$ với $k$ là số cố định cho trước khi:

a) $\alpha + \beta + \gamma = 0.$

b) $\alpha + \beta + \gamma \ne 0.$

DẠNG TOÁN 4: BIỂU THỨC TỌA ĐỘ CỦA TÍCH VÔ HƯỚNG.

1. PHƯƠNG PHÁP GIẢI

Cho $\vec a = \left( {{x_1};{y_1}} \right)$, $\vec b = \left( {{x_2};{y_2}} \right).$ Khi đó:

+ Tích vô hướng hai vectơ là $\vec a.\vec b = {x_1}{x_2} + {y_1}{y_2}.$

+ Góc của hai vectơ được xác định bởi công thức:

$\cos (\vec a,\vec b) = \frac{{\vec a.\vec b}}{{|\vec a||\vec b|}}$ $= \frac{{{x_1}{x_2} + {y_1}{y_2}}}{{\sqrt {x_1^2 + y_1^2} \sqrt {x_2^2 + y_2^2} }}.$

Chú ý: $\vec a \bot \vec b$ $\Leftrightarrow \vec a.\vec b = 0$ $\Leftrightarrow {x_1}{x_2} + {y_1}{y_2} = 0.$

Để xác định độ dài một vectơ đoạn thẳng ta sử dụng công thức:

+ Nếu $\vec a = (x;y)$ thì $|\vec a| = \sqrt {{x^2} + {y^2}} .$

+ Nếu $A\left( {{x_A};{y_A}} \right)$, $B\left( {{x_B};{y_B}} \right)$ thì $AB = \sqrt {{{\left( {{x_B} – {x_A}} \right)}^2} + {{\left( {{y_B} – {y_A}} \right)}^2}} .$

2. CÁC VÍ DỤ

<!-- chunk:13 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 1: Cho tam giác $ABC$ có $A(1;2)$, $B( – 2;6)$, $C(9;8).$

a) Chứng minh tam giác $ABC$ vuông tại $A.$

b) Tính góc $B$ của tam giác $ABC.$

c) Xác định hình chiếu của $A$ lên cạnh $BC.$

a) Ta có $\overrightarrow {AB} ( – 3;4)$, $\overrightarrow {AC} (8;6)$ $\Rightarrow \overrightarrow {AB} .\overrightarrow {AC} = – 3.8 + 4.6 = 0.$

Do đó $\overrightarrow {AB} \bot \overrightarrow {AC}$ hay tam giác $ABC$ vuông tại $A.$

b) Ta có $\overrightarrow {BC} (11;2)$, $\overrightarrow {BA} (3; – 4).$

Suy ra $\cos B = \cos (\overrightarrow {BC} ,\overrightarrow {BA} )$ $= \frac{{11.3 + 2.( – 4)}}{{\sqrt {{{11}^2} + {2^2}} \sqrt {{3^2} + {{( – 4)}^2}} }}$ $= \frac{1}{{\sqrt 5 }}.$

c) Gọi $H(x;y)$ là hình chiếu của $A$ lên $BC.$

Ta có $\overrightarrow {AH} (x – 1;y – 2)$, $\overrightarrow {BH} (x + 2;y – 6)$, $\overrightarrow {BC} (11;2).$

$AH \bot BC$ $\Leftrightarrow \overrightarrow {AH} .\overrightarrow {BC} = 0$ $\Leftrightarrow 11(x – 1) + 2(y – 2) = 0.$

Hay $11x + 2y – 15 = 0$ $(1).$

Mặt khác $\overrightarrow {BH}$, $\overrightarrow {BC}$ cùng phương nên $\frac{{x + 2}}{{11}} = \frac{{y – 6}}{2}$ $\Leftrightarrow 2x – 11y + 70 = 0$ $(2).$

Từ $(1)$ và $(2)$ suy ra $x = \frac{1}{5}$, $y = \frac{{32}}{5}.$

Vậy hình chiếu của $A$ lên $BC$ là $H\left( {\frac{1}{5};\frac{{32}}{5}} \right).$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 2: Cho hình thoi $ABCD$ có tâm $I(1;1)$, đỉnh $A(3;2)$ và đỉnh $B$ nằm trên trục hoành. Tìm tọa độ các đỉnh còn lại của hình thoi.

Vì $B$ nằm trên trục hoành nên giả sử $B(0;y).$

Vì $I$ là tâm hình thoi $ABCD$ nên $I$ là trung điểm của $AC$ và $BD.$

Suy ra $C = \left( {2{x_I} – {x_A};2{y_I} – {y_A}} \right)$ $= ( – 1;0)$, $D = \left( {2{x_I} – {x_B};2{y_I} – {y_B}} \right)$ $= (2;2 – y).$

Do đó $AB = AD$ $\Leftrightarrow A{B^2} = A{D^2}$ $\Leftrightarrow 9 + {(y – 2)^2} = 1 + {y^2}$ $\Leftrightarrow y = 3.$

Vậy $B(0;3)$, $C( – 1;0)$, $D(2; – 1).$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 3: Cho ba điểm $A(3;4)$, $B(2;1)$ và $C( – 1; – 2).$ Tìm điểm $M$ trên đường thẳng $BC$ để góc $\widehat {AMB} = {45^0}.$

Giả sử $M(x;y)$ suy ra $\overrightarrow {MA} (3 – x;4 – y)$, $\overrightarrow {MB} (2 – x;1 – y)$, $\overrightarrow {BC} ( – 3; – 3).$

Vì $\widehat {AMB} = {45^0}$ suy ra $|\cos \widehat {AMB}| = |\cos (\overrightarrow {MA} ;\overrightarrow {BC} )|.$

$\Leftrightarrow \cos {45^0} = \frac{{|\overrightarrow {MA} .\overrightarrow {BC} |}}{{|\overrightarrow {MA} |.|\overrightarrow {BC} |}}$ $\Leftrightarrow \frac{{\sqrt 2 }}{2} = \frac{{| – 3(3 – x) – 3(4 – y)|}}{{\sqrt {{{(3 – x)}^2} + {{(4 – y)}^2}} \sqrt {9 + 9} }}.$

$\Leftrightarrow \sqrt {{{(3 – x)}^2} + {{(4 – y)}^2}}$ $= |x + y – 7|$ $(*).$

Mặt khác $M$ thuộc đường thẳng $BC$ nên hai vectơ $\overrightarrow {MB}$, $\overrightarrow {BC}$ cùng phương.

Suy ra $\frac{{2 – x}}{{ – 3}} = \frac{{1 – y}}{{ – 3}}$ $\Leftrightarrow x = y + 1$ thế vào $(*)$ ta được:

$\sqrt {{{(2 – y)}^2} + {{(4 – y)}^2}}$ $= |2y – 6|$ $\Leftrightarrow {y^2} – 6y + 8 = 0$ $\Leftrightarrow y = 2$ hoặc $y = 4.$

+ Với $y = 2 \Rightarrow x = 3$, ta có:

$\overrightarrow {MA} (0;2)$, $\overrightarrow {MB} ( – 1; – 1)$ $\Rightarrow \cos \widehat {AMB}$ $= \cos (\overrightarrow {MA} ;\overrightarrow {MB} )$ $= – \frac{1}{{\sqrt 2 }}.$

Khi đó $\widehat {AMB} = {135^0}$ (không thỏa mãn).

+ Với $y = 4 \Rightarrow x = 5$, ta có:

$\overrightarrow {MA} ( – 2;0)$, $\overrightarrow {MB} ( – 3; – 3)$ $\Rightarrow \cos \widehat {AMB}$ $= \cos (\overrightarrow {MA} ;\overrightarrow {MB} )$ $= \frac{1}{{\sqrt 2 }}.$

Khi đó $\widehat {AMB} = {45^0}.$

Vậy $M(5;4)$ là điểm cần tìm.

<!-- chunk:16 level:3 source:https://toanmath.com/2019/09/tich-vo-huong-cua-hai-vecto.html -->
## Ví dụ 4: Cho điểm $A(2;1).$ Lấy điểm $B$ nằm trên trục hoành có hoành độ không âm và điểm $C$ trên trục tung có tung độ dương sao cho tam giác $ABC$ vuông tại $A.$ Tìm toạ độ $B$, $C$ để tam giác $ABC$ có diện tích lớn nhất.

Gọi $B(b;0)$, $C(0;c)$ với $b \ge 0$, $c > 0.$

Suy ra $\overrightarrow {AB} (b – 2; – 1)$, $\overrightarrow {AC} ( – 2;c – 1).$

Theo giả thiết ta có tam giác $ABC$ vuông tại $A$ nên:

$\overrightarrow {AB} .\overrightarrow {AC} = 0$ $\Leftrightarrow (b – 2)( – 2) – 1.(c – 1) = 0$ $\Leftrightarrow c = – 2b + 5.$

Ta có ${S_{\Delta ABC}} = \frac{1}{2}AB.AC$ $= \frac{1}{2}\sqrt {{{(b – 2)}^2} + 1} .\sqrt {{2^2} + {{(c – 1)}^2}}$ $= {(b – 2)^2} + 1$ $= {b^2} – 4b + 5.$

Vì $c > 0$ nên $– 2b + 5 > 0$ $\Rightarrow 0 \le b < \frac{5}{2}.$

Xét hàm số $y = {x^2} – 4x + 5$ với $0 \le x < \frac{5}{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan10/images/tich-vo-huong-cua-hai-vecto-7.png" alt="">

Suy ra giá trị lớn nhất của hàm số $y = {x^2} – 4x + 5$ với $0 \le x < \frac{5}{2}$ là $y = 5$ khi $x =0.$

Do đó diện tích tam giác $ABC$ lớn nhất khi và chỉ khi $b = 0$, suy ra $c=5.$

Vậy $B(0;0)$, $C(0;5)$ là điểm cần tìm.

## Bài tập
## Bài 1: Cho hai vectơ $\vec a(0;4)$, $\vec b(4; – 2).$

a) Tính cosin góc giữa hai vectơ $\overrightarrow a$ và $\overrightarrow b .$

b) Xác định tọa độ của vectơ $\overrightarrow c$ biết $(\vec a + 2\vec b).\vec c = – 1$ và $( – \vec b + 2\vec c).\vec a = 6.$

## Bài 2: Cho tam giác $ABC$ có $A(5;3)$, $B(2; – 1)$, $C( – 1;5).$

a) Tìm tọa độ trực tâm tam giác $ABC.$

b) Tính tọa độ chân đường cao vẽ từ $A.$

c) Tính diện tích tam giác $ABC.$

## Bài 3: Cho tam giác $ABC$ với $A(3;1)$, $B(-1;-1)$, $C(6;0).$

a) Tính góc $A$ của tam giác $ABC.$

b) Tính tọa độ giao điểm của đường tròn đường kính $AB$ và đường tròn đường kính $OC.$

## Bài 4: Cho ba điểm $A(6;3)$, $B(-3;6)$, $C(1;-2).$ Tìm tọa độ tâm đường tròn ngoại tiếp tam giác $ABC.$

## Bài 5: Các điểm $B(-1;3)$, $C(3;1)$ là hai đỉnh của một tam giác $ABC$ vuông cân tại $A.$ Tìm tọa độ đỉnh $A.$

## Bài 6: Cho bốn điểm $A(-8;0)$, $B(0;4)$, $C(2;0)$, $D(-3;-5).$ Chứng minh rằng tứ giác nội tiếp được một đường tròn.

## Bài 7: Trong mặt phẳng toạ độ $Oxy$, cho các điểm $A(-2;-1)$, $B(2;-4).$

a) Tìm trên trục $Oy$ điểm $M$ sao cho $\widehat {MBA} = {45^0}.$

b) Tìm trên trục $Ox$ điểm $N$ sao cho $NA = NB.$

## Bài 8: Cho hai điểm $A(4;-3)$, $B(3;1).$ Tìm $M$ trên trục hoành sao cho $\widehat {AMB} = {135^0}.$

## Bài 9: Biết $A(1;-1)$, $B(3;0)$ là hai đỉnh của hình vuông $ABCD.$ Tìm tọa độ các đỉnh $C$ và $D.$

## Bài 10: Trong mặt phẳng tọa độ cho ba điểm $A(1;4)$, $B(-2;-2)$ và $C(4;2).$ Xác định tọa độ điểm $M$ sao cho tổng $M{A^2} + 2M{B^2} + 3M{C^2}$ nhỏ nhất.