# Các hệ thức lượng trong tam giác

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
Bài viết trình bày lý thuyết và hướng dẫn phương pháp giải các dạng toán hệ thức lượng trong tam giác.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## A. TÓM TẮT LÝ THUYẾT

1. Định lí côsin: Trong tam giác $ABC$ với $BC = a$, $AC = b$ và $AB = c.$ Ta có:

${a^2} = {b^2} + {c^2} – 2bc.\cos A.$

${b^2} = {c^2} + {a^2} – 2ca.\cos B.$

${c^2} = {a^2} + {b^2} – 2ab.\cos C.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-1.png" alt="">

Hệ quả:

$\cos A = \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}.$

$\cos B = \frac{{{c^2} + {a^2} – {b^2}}}{{2ca}}.$

$\cos C = \frac{{{a^2} + {b^2} – {c^2}}}{{2ab}}.$

2. Định lí sin: Trong tam giác $ABC$ với $BC = a$, $AC = b$, $AB = c$ và $R$ là bán kính đường tròn ngoại tiếp. Ta có: $\frac{a}{{\sin A}} = \frac{b}{{\sin B}} = \frac{c}{{\sin C}} = 2R.$

3. Độ dài trung tuyến: Cho tam giác $ABC$ với ${m_a}$, ${m_b}$, ${m_c}$ lần lượt là các trung tuyến kẻ từ $A$, $B$, $C.$ Ta có:

$m_a^2 = \frac{{2\left( {{b^2} + {c^2}} \right) – {a^2}}}{4}.$

$m_b^2 = \frac{{2\left( {{a^2} + {c^2}} \right) – {b^2}}}{4}.$

$m_c^2 = \frac{{2\left( {{a^2} + {b^2}} \right) – {c^2}}}{4}.$

4. Diện tích tam giác

Với tam giác $ABC$ ta kí hiệu ${h_a}$, ${h_b}$, ${h_c}$ là độ dài đường cao lần lượt tương ứng với các cạnh $BC$, $CA$, $AB$, $R$, $r$ lần lượt là bán kính đường tròn ngoại tiếp, nội tiếp tam giác, $P = \frac{{a + b + c}}{2}$ là nửa chu vi tam giác, $S$ là diện tích tam giác. Khi đó ta có:

$S = \frac{1}{2}a{h_a} = \frac{1}{2}b{h_b} = \frac{1}{2}c{h_c}$ $= \frac{1}{2}bc\sin A = \frac{1}{2}ca\sin B = \frac{1}{2}ab\sin C$ $= \frac{{abc}}{{4R}}$ $= pr$ $= \sqrt {p(p – a)(p – b)(p – c)}$ (công thức Hê-rông).

## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI

**DẠNG TOÁN 1: XÁC ĐỊNH CÁC YẾU TỐ TRONG TAM GIÁC.

****1. PHƯƠNG PHÁP

**Sử dụng định lí côsin và định lí sin.

Sử dụng công thức xác định độ dài đường trung tuyến và mối liên hệ của các yếu tố trong các công thức tính diện tích trong tam giác.

2. CÁC VÍ DỤ

<!-- chunk:2 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 1: Cho tam giác $ABC$ có $AB = 4$, $AC = 5$ và $\cos A = \frac{3}{5}.$ Tính cạnh $BC$ và độ dài đường cao kẻ từ $A.$

Áp dụng định lí côsin ta có:

$B{C^2} = A{B^2} + A{C^2} – 2AB.AC.\cos A$ $= {4^2} + {5^2} – 2.4.5.\frac{3}{5} = 29.$

Suy ra $BC = \sqrt {29} .$

Vì ${\sin ^2}A + {\cos ^2}A = 1$ nên $\sin A = \sqrt {1 – {{\cos }^2}A}$ $= \sqrt {1 – \frac{9}{{25}}} = \frac{4}{5}.$

Theo công thức tính diện tích ta có ${S_{ABC}} = \frac{1}{2}AB.AC.\sin A$ $= \frac{1}{2}.4.5.\frac{4}{5} = 8$ $(1).$

Mặt khác ${S_{ABC}} = \frac{1}{2}a.{h_a}$ $= \frac{1}{2}.\sqrt {29} .{h_a}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\frac{1}{2}.\sqrt {29} .{h_a} = 8$ $\Rightarrow {h_a} = \frac{{16\sqrt {29} }}{{29}}.$

Vậy độ dài đường cao kẻ từ $A$ là ${h_a} = \frac{{16\sqrt {29} }}{{29}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 2: Cho tam giác $ABC$ nội tiếp đường tròn bán kính bằng $3$, biết $\widehat A = {30^0}$, $\widehat B = {45^0}.$ Tính độ dài trung tuyến kẻ từ $A$ và bán kính đường tròn nội tiếp tam giác.

Ta có $\widehat C = {180^0} – \widehat A – \widehat B$ $= {180^0} – {30^0} – {45^0}$ $= {105^0}.$

Theo định lí sin ta có:

$a = 2R\sin A$ $= 2.3.\sin {30^0} = 3.$

$b = 2R\sin B$ $= 2.3.\sin {45^0} = 6.\frac{{\sqrt 2 }}{2} = 3\sqrt 2 .$

$c = 2R\sin C$ $= 2.3.\sin {105^0} \approx 5,796.$

Theo công thức đường trung tuyến ta có:

$m_a^2 = \frac{{2\left( {{b^2} + {c^2}} \right) – {a^2}}}{4}$ $\approx \frac{{2\left( {18 + {{5,796}^2}} \right) – 9}}{4}$ $= 23,547.$

Theo công thức tính diện tích tam giác ta có:

${S_{ABC}} = pr = \frac{1}{2}bc\sin A$ $\Rightarrow r = \frac{{bc\sin A}}{{2p}}$ $\approx \frac{{3\sqrt 2 .5,796\sin {{30}^0}}}{{3 + 3\sqrt 2 + 5,796}} \approx 0,943.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 3: Cho tam giác $ABC$ có $M$ là trung điểm của $BC.$ Biết $AB = 3$, $BC = 8$, $\cos \widehat {AMB} = \frac{{5\sqrt {13} }}{{26}}.$ Tính độ dài cạnh $AC$ và góc lớn nhất của tam giác $ABC.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-2.png" alt="">

$BC = 8$ $\Rightarrow BM = 4.$

Đặt $AM = x.$

Theo định lí côsin ta có:

$\cos \widehat {AMB} = \frac{{A{M^2} + B{M^2} – A{B^2}}}{{2AM.BM}}.$

Suy ra $\frac{{5\sqrt {13} }}{{26}} = \frac{{{x^2} + 16 – 9}}{{2.4.x}}.$

$\Leftrightarrow 13{x^2} – 20\sqrt {13} x + 91 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \sqrt {13} }\\
{x = \frac{{7\sqrt {13} }}{{13}}}
\end{array}} \right..
$$

Theo công thức tính đường trung tuyến ta có: $A{M^2} = \frac{{2\left( {A{B^2} + A{C^2}} \right) – B{C^2}}}{{2AB.AC}}.$

Trường hợp 1: Nếu $x = \sqrt {13}$ $\Rightarrow 13 = \frac{{2\left( {{3^2} + A{C^2}} \right) – {8^2}}}{4}$ $\Rightarrow AC = 7.$

Ta có $BC > AC > AB$ $\Rightarrow$ góc $A$ lớn nhất.

Theo định lí côsin ta có:

$\cos A = \frac{{A{B^2} + A{C^2} – B{C^2}}}{{2AB.AC}}$ $= \frac{{9 + 49 – 64}}{{2.3.7}} = – \frac{1}{7}.$

Suy ra $A \approx {98^0}12′.$

Trường hợp 2: Nếu $x = \frac{{7\sqrt {13} }}{{13}}$ $\Rightarrow \frac{{49}}{{13}} = \frac{{2\left( {{3^2} + A{C^2}} \right) – {8^2}}}{4}$ $\Rightarrow AC = \sqrt {\frac{{397}}{{13}}} .$

Ta có $BC > AC > AB$ $\Rightarrow$ góc $A$ lớn nhất.

Theo định lí côsin ta có:

$\cos A = \frac{{A{B^2} + A{C^2} – B{C^2}}}{{2AB.AC}}$ $= \frac{{9 + \frac{{397}}{{13}} – 64}}{{2.3.\sqrt {\frac{{397}}{{13}}} }}$ $= – \frac{{53}}{{\sqrt {5161} }}.$

Suy ra $A \approx {137^0}32′.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 4: Cho hình chữ nhật $ABCD$ biết $AD = 1.$ Giả sử $E$ là trung điểm $AB$ và thỏa mãn $\widehat {BDE} = \frac{1}{3}.$ Tính độ dài cạnh $AB.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-3.png" alt="">

Đặt $AB = 2x$ $(x > 0)$ $\Rightarrow AE = EB = x.$

Vì góc $\widehat {BDE}$ nên $\cos \widehat {BDE} > 0$ suy ra:

$\cos \widehat {BDE} = \sqrt {1 – {{\sin }^2}\widehat {BDE}}$ $= \frac{{2\sqrt 2 }}{3}.$

Theo định lí Pitago ta có:

$D{E^2} = A{D^2} + A{E^2}$ $= 1 + {x^2}$ $\Rightarrow DE = \sqrt {1 + {x^2}} .$

$B{D^2} = D{C^2} + B{C^2}$ $= 4{x^2} + 1$ $\Rightarrow BD = \sqrt {4{x^2} + 1} .$

Áp dụng định lí côsin trong tam giác $BDE$ ta có:

$\cos \widehat {BDE} = \frac{{D{E^2} + D{B^2} – E{B^2}}}{{2DE.DB}}$ $\Leftrightarrow \frac{{2\sqrt 2 }}{3} = \frac{{4{x^2} + 2}}{{2\sqrt {\left( {1 + {x^2}} \right)\left( {4{x^2} + 1} \right)} }}.$

$\Leftrightarrow 4{x^4} – 4{x^2} + 1 = 0$ $\Leftrightarrow 2{x^2} = 1$ $\Leftrightarrow x = \frac{{\sqrt 2 }}{2}$ (do $x > 0$).

Vậy độ dài cạnh $AB$ là $\sqrt 2 .$

## Bài tập
## Bài 1: Cho tam giác $ABC$ có đoạn thẳng nối trung điểm $AB$ và $BC$ bằng $3$, cạnh $AB = 9$ và $\widehat {ACB} = {60^0}.$ Tính cạnh $BC.$

Đặt $BC = x$ $(x > 0).$

$MN = 3$ $\Rightarrow AC = 6.$

Theo định lí côsin ta có $A{B^2} = C{A^2} + C{B^2} – 2.CA.CB.\cos C.$

Hay $81 = 36 + {x^2} – 2.6.x.\frac{1}{2}$ $\Leftrightarrow x = 3(1 + \sqrt 6 ).$

## Bài 2: Cho tam giác $ABC$ vuông tại $B$ có $AB = 1.$ Trên tia đối của $AC$ lấy điểm $D$ sao cho $CD = AB.$ Giả sử $\widehat {CBD} = {30^0}.$ Tính $AC.$

Đặt $AC = x$ $(x > 0).$

Áp dụng định lí côsin trong tam giác $ABD$ ta có:

$B{D^2} = 1 + {(1 + x)^2} – 2(1 + x).\frac{1}{x}.$

Áp dụng định lí sin trong tam giác $BCD$ ta có:

$BD = \frac{1}{{\sin {{30}^0}}}\sin \widehat {BCD} = \frac{2}{x}.$

Suy ra ta được phương trình:

${x^4} + 2{x^3} – 2x – 4 = 0$ $\Leftrightarrow (x + 2)\left( {{x^3} – 2} \right) = 0$ $\Leftrightarrow x = \sqrt[3]{2}.$

Vậy $AC = \sqrt[3]{2}.$

## Bài 3: Cho tam giác $ABC$ có $AB = 3$, $AC =7$, $BC = 8.$

a) Tính diện tích tam giác $ABC.$

b) Tính bán kính đường tròn nội tiếp, ngoại tiếp tam giác.

c) Tính đường cao kẻ từ đỉnh $A.$

a) Áp dụng công thức Hê-rông ta có $S = \sqrt {p(p – a)(p – b)(p – c)}$ $= 6\sqrt 3 .$

b) Áp dụng công thức tính diện tích $S = \frac{{abc}}{{4R}}$ và $S = pr$ suy ra:

$R = \frac{{7\sqrt 3 }}{3}$, $r = \frac{{2\sqrt 3 }}{3}.$

c) ${h_a} = \frac{{2S}}{a} = \frac{{12\sqrt 6 }}{8} = \frac{{3\sqrt 6 }}{2}.$

## Bài 4: Cho tam giác $ABC$ thỏa mãn $\frac{a}{{\sqrt 3 }} = \frac{b}{{\sqrt 2 }} = \frac{{2c}}{{\sqrt 6 – \sqrt 2 }}.$

a) Tính các góc của tam giác.

b) Cho $a = 2\sqrt 3 .$ Tính bán kính đường tròn ngoại tiếp tam giác $ABC.$

a) Đặt $\frac{a}{{\sqrt 3 }} = t > 0$ $\Rightarrow a = \sqrt 3 t$, $b = \sqrt 2 t$, $c = \frac{{\sqrt 6 – \sqrt 2 }}{2}t.$

Áp dụng định lí côsin ta có:

$\cos A = \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}$ $= \frac{{2{t^2} + (2 – \sqrt 3 ){t^2} – 3{t^2}}}{{2(\sqrt 3 – 1){t^2}}}$ $= – \frac{1}{2}$ $\Rightarrow A = {120^0}.$

$\cos B = \frac{{{a^2} + {c^2} – {b^2}}}{{2ac}}$ $= \frac{{3{t^2} + (2 – \sqrt 3 ){t^2} – 2{t^2}}}{{\sqrt 2 (3 – \sqrt 3 ){t^2}}} = \frac{{\sqrt 2 }}{2}$ $\Rightarrow B = {45^0}$, $C = {15^0}.$

b) Áp dụng định lí sin, ta có: $R = \frac{a}{{2\sin A}}$ $= \frac{{2\sqrt 3 }}{{2\sin {{120}^0}}} = 2.$

## Bài 5: Cho tam giác $ABC$ có $\widehat A = {60^0}$, $a = 10$, $r = \frac{{5\sqrt 3 }}{3}.$

a) Tính $R.$

b) Tính $b$, $c.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-4.png" alt="">

a) $2R = \frac{a}{{\sin A}} = \frac{{20\sqrt 3 }}{3}$ $\Rightarrow R = \frac{{10\sqrt 3 }}{3}.$

b) Gọi $M$, $N$, $P$ lần lượt là các tiếp điểm của $BC$, $CA$ và $AB$ với đường tròn nội tiếp tam giác $ABC.$

Ta có:

$AP = AN – r.\cot {30^0} = 5$, $BP + NC$ $= BM + MC$ $= a = 10.$

$\Rightarrow (b – AN) + (c – AP) = 10$ $\Rightarrow b + c = 20$ $(1).$

Theo định lí côsin ta có:

${a^2} = {b^2} + {c^2} – 2bc\cos {60^0}$ $\Rightarrow bc = \frac{{{{(b + c)}^2} – {a^2}}}{3} = 100$ $(2).$

Từ $(1)$ và $(2)$ suy ra $b$, $c$ là nghiệm của phương trình ${x^2} – 20x + 100 = 0$ $\Leftrightarrow x = 10.$

Vậy $b = c = 10$ $\Rightarrow \Delta ABC$ đều.

## Bài 6: Cho tam giác $ABC$ có $AB = 10$, $AC = 4$ và $\widehat A = {60^0}.$

a) Tính chu vi của tam giác.

b) Tính $\tan C.$

c) Lấy điểm $D$ trên tia đối của tia $AB$ sao cho $AD = 6$ và điểm $E$ trên tia $AC$ sao cho $AE = x.$ Tìm $x$ để $BE$ là tiếp tuyến của đường tròn $(C)$ ngoại tiếp tam giác $ADE.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-5.png" alt="">

a) Theo định lí côsin ta có:

$B{C^2} = {10^2} + {4^2} – 2.10.4\cos {60^0} = 76.$

$\Rightarrow BC \approx 8,72.$

Suy ra chu vi tam giác là $2p \approx 10 + 4 + 8,72 = 22,72.$

b) Kẻ đường cao $BH$ ta có:

$AH = AB\cos {60^0} = 5$ $\Rightarrow HC = 5 – 4 = 1.$

$BH = AB\sin {60^0} = 5\sqrt 3 .$

Vậy $\tan C = – \tan \widehat {BCH}$ $= – \frac{{HB}}{{HC}} = – 5\sqrt 3 .$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-6.png" alt="">

c) Để $BE$ là tiếp tuyến đường tròn $(C)$ ta phải có:

$B{E^2} = BA.BD$ $= 10(10 + 6) = 160.$

Áp dụng định lí côsin trong tam giác $ABE$ ta có:

$B{E^2} = {x^2} + 100 – 10x$ $\Rightarrow {x^2} – 10x – 60 = 0.$

$\Rightarrow x = 5 + \sqrt {85} .$

## Bài 7: Cho tam giác $ABC$ cân có cạnh bên bằng $b$ và nội tiếp đường tròn $(O;R).$

a) Tính côsin của các góc tam giác.

b) Tính bán kính đường tròn nội tiếp tam giác.

c) Với giá trị nào của $b$ thì tam giác có diện tích lớn nhất?

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-7.png" alt="">

a) Giả sử tam giác cân tại đỉnh $A.$

Đặt $\widehat B = \widehat C = \alpha$ $\Rightarrow \alpha < {90^0}.$

Ta có $\sin \alpha = \frac{b}{{2R}}$ $\Rightarrow \cos B = \cos C = \cos \alpha$ $= \sqrt {1 – \frac{{{b^2}}}{{4{R^2}}}} .$

$\cos A = \frac{{A{B^2} + A{C^2} – B{C^2}}}{{2AB.AC}}$ $= \frac{{{b^2} – 2{R^2}}}{{2{R^2}}}.$

b) $S = \frac{1}{2}BC.AH$ $= \frac{1}{2}.2b\cos \alpha .b\sin \alpha$ $= \frac{{{b^3}\sqrt {4{R^2} – {b^2}} }}{{4{R^2}}}.$

Chu vi tam giác là $2p = 2b + 2b\frac{{\sqrt {4{R^2} – {b^2}} }}{{2R}}.$

Bán kính đường tròn nội tiếp tam giác $r = \frac{S}{P}$ $= \frac{{{b^2}\sqrt {4{R^2} – {b^2}} }}{{2R(2R + \sqrt {4{R^2} – {b^2}} )}}.$

c) Ta phải tìm $b$ để $y = {b^3}\sqrt {4{R^2} – {b^2}}$ đạt GTLN.

Áp dụng bất đẳng thức Cauchy cho bốn số ta có:

$y = 3\sqrt 3 \sqrt {\frac{{{b^2}}}{3}.\frac{{{b^2}}}{3}.\frac{{{b^2}}}{3}.\left( {4{R^2} – {b^2}} \right)}$ $\le 3\sqrt 3 \sqrt {{{\left( {\frac{{\frac{{{b^2}}}{3} + \frac{{{b^2}}}{3} + \frac{{{b^2}}}{3} + \left( {4{R^2} – {b^2}} \right)}}{4}} \right)}^4}}$ $= 3\sqrt 3 {R^4}.$

Dấu bằng xảy ra khi và chỉ khi $\frac{{{b^2}}}{3} = 4{R^2} – {b^2}$ $\Leftrightarrow b = R\sqrt 3 .$

DẠNG TOÁN 2: GIẢI TAM GIÁC.

1. PHƯƠNG PHÁP

Giải tam giác là tính các cạnh và các góc của tam giác dựa trên một số điều kiện cho trước.

Trong các bài toán giải tam giác người ta thường cho tam giác với ba yếu tố như sau: biết một cạnh và hai góc kề cạnh đó, biết một góc và hai cạnh kề góc đó, biết ba cạnh. Để tìm các yếu tố còn lại ta sử dụng định lí côsin và định lí sin, định lí tổng ba góc trong một tam giác bằng $180°$ và trong một tam giác đối diện với góc lớn hơn thì có cạnh lớn hơn và ngược lại đối diện với cạnh lớn hơn thì có góc lớn hơn.

2. CÁC VÍ DỤ

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 1: Giải tam giác $ABC$ biết $b = 32$, $c = 45$ và $\widehat A = {87^0}.$

Theo định lí côsin ta có: ${a^2} = {b^2} + {c^2} – 2bc\cos A$ $= {32^2} + {4^2} – 2.32.4.\sin {87^0}.$

Suy ra $a \approx 53,8.$

Theo định lí sin ta có: $\sin B = \frac{{b\sin A}}{a}$ $= \frac{{32\sin {{87}^0}}}{{53,8}}$ $\Rightarrow \widehat B \approx {36^0}.$

Suy ra $\widehat C = {180^0} – \widehat A – \widehat B$ $\approx {180^0 } – {87^0} – {36^0} = {57^0}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 2: Giải tam giác $ABC$ biết $\widehat A = {60^0}$, $\widehat B = {40^0}$ và $c = 14.$

Ta có $\widehat C = {180^0} – \widehat A – \widehat B$ $= {180^0} – {60^0} – {40^0} = {80^0}.$

Theo định lí sin ta có:

$a = \frac{{c\sin A}}{{\sin C}} = \frac{{14.\sin {{60}^0}}}{{\sin {{80}^0}}}$ $\Rightarrow a \approx 12,3.$

$b = \frac{{c\sin B}}{{\sin C}} = \frac{{14.\sin {{40}^0}}}{{\sin {{80}^0}}}$ $\Rightarrow b \approx 9,1.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 3: Cho tam giác $ABC$ biết $a = 2\sqrt 3$, $b = 2\sqrt 2$, $c = \sqrt 6 – \sqrt 2 .$ Tính góc lớn nhất của tam giác.

Theo giải thiết ta có $c < b < a$ suy ra $\widehat C < \widehat B < \widehat A$ do đó góc $A$ là lớn nhất.

Theo định lí côsin ta có:

$\cos A = \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}$ $= \frac{{8 + {{(\sqrt 6 – \sqrt 2 )}^2} – {{12}^2}}}{{2.2\sqrt 2 .(\sqrt 6 – \sqrt 2 )}}$ $= \frac{{4 – 4\sqrt 3 }}{{8\sqrt 3 – 8}} = – \frac{1}{2}.$

Suy ra $\widehat A = {120^0}.$

Vậy góc lớn nhất là góc $A$ có số đo là ${120^0}.$

## Bài tập
## Bài 1: Giải tam giác $ABC$ biết:

a) $a = 2$, $b=3$, $c =4.$

b) $a = 12$, $c=8,2$ và $\widehat A = {110^0}.$

a) Theo định lí côsin ta có:

$\cos A = \frac{{{3^2} + {4^2} – {2^2}}}{{2.3.4}} = \frac{7}{8}$ $\Rightarrow \widehat A \approx {28^0}57′.$

$\cos B = \frac{{{2^2} + {4^2} – {3^2}}}{{2.2.4}} = \frac{{11}}{{16}}$ $\Rightarrow \widehat B \approx {46^0}34′.$

$\widehat C = {180^0} – \widehat A – \widehat B \approx {104^0}29′.$

b) Theo định lí sin ta có:

$\sin C = \frac{{c\sin A}}{a}$ $= \frac{{8,2.\sin {{110}^0}}}{{12}}$ $\Rightarrow \widehat C \approx {39^0}57’$ hoặc $\widehat C \approx {180^0} – {39^0}57′ = {140^0}3′.$

Vì góc $A$ tù nên góc $C$ nhọn do đó $\widehat C \approx {39^0}57′.$

Suy ra $\widehat B = {180^0} – \widehat A – \widehat C$ $\approx {180^0} – {110^0} – {39^0}57’$ $= {33^0}3′.$

Mặt khác $b = \frac{{a\sin B}}{{\sin A}}$ $= \frac{{12.\sin {{33}^0}3′}}{{\sin {{110}^0}}} \approx 6,96.$

## Bài 2: Giải tam giác $ABC$ biết:

a) $a = 109$, $\widehat B = {33^0}24’$, $\widehat C = {66^0}59′.$

b) $a = 20$, $b = 13$, $\widehat A = {67^0}23′.$

a) $\widehat A = {180^0} – \left( {{{33}^0}24′ + {{66}^0}59′} \right)$ $= {79^0}37′.$

$b = \frac{{a.\sin {{33}^0}24′}}{{\sin {{79}^0}37′}} \approx 61.$

$c = \frac{{a.\sin {{66}^0}59′}}{{\sin {{79}^0}37′}} \approx 102.$

b) $\sin B = \frac{{13.\sin {{67}^0}23′}}{{20}} \approx 0,6.$

Vì $b < a$ $\Rightarrow \widehat B < \widehat A$ $\Rightarrow \widehat B \approx {36^0}52′.$

$\widehat C \approx {75^0}45′.$

$c = \frac{{20.\sin {{75}^0}45′}}{{\sin {{67}^0}23′}} \approx 21.$

## Bài 3: Giải tam giác $ABC$ biết:

a) $b = 4,5$, $\widehat A = {30^0}$, $\widehat C = {75^0}.$

b) $b = 14$, $c = 10$, $\widehat A = {145^0}.$

c) $a = 14$, $b = 18$, $c = 20.$

a) Ta có: $\widehat B = {180^0} – \widehat A – \widehat C$ $= {180^0} – {30^0} – {75^0} = {75^0}.$

Theo định lí sin ta có:

$a = \frac{{b\sin A}}{{\sin B}}$ $= \frac{{4,5.\sin {{30}^0}}}{{\sin {{75}^0}}}$ $\Rightarrow a \approx 2,33.$

$c = \frac{{b\sin C}}{{\sin B}}$ $= \frac{{4,5.\sin {{75}^0}}}{{\sin {{75}^0}}}$ $\Rightarrow c \approx 4,5.$

b) Theo định lí côsin ta có:

${a^2} = {b^2} + {c^2} – 2bc.\cos A$ $= {14^2} + {10^2} – 2.14.10.\cos {145^0}.$

Suy ra $a \approx 22,92.$

Theo định lí sin ta có: $\sin B = \frac{{b\sin A}}{a}$ $= \frac{{14\sin {{145}^0}}}{{22,92}} \approx 0,35$ $\Rightarrow \widehat B \approx {20^0}29′.$

Suy ra $\widehat C = {180^0} – \widehat A – \widehat B$ $\approx {180^0} – {145^0} – {20^0}29’$ $= {14^0}31′.$

c) Áp dụng định lí côsin ta có:

$\cos A = \sqrt {\frac{{11}}{{15}}}$ $\Rightarrow A \approx {31^0}5′.$

$\cos B = \sqrt {\frac{{17}}{{35}}}$ $\Rightarrow B \approx {45^0}49′.$

$\cos C = \sqrt {\frac{5}{{21}}}$ $\Rightarrow C \approx {50^0}47′.$

## Bài 4: Cho $\Delta ABC$ ta có $a = 13$, $b = 4$ và $\cos C = – \frac{5}{{13}}.$ Tính bán kính đường tròn ngoại tiếp và nội tiếp tam giác.

${c^2} = {a^2} + {b^2} – 2ab\cos C$ $= {13^2} + {4^2} – 2.13.4.\left( { – \frac{5}{{13}}} \right)$ $= 225$ $\Rightarrow c = 15.$

$\sin C = \frac{{12}}{{13}}$ $\Rightarrow R = \frac{c}{{2\sin C}}$ $= \frac{{15}}{{2.\frac{{12}}{{13}}}} = \frac{{65}}{8}.$

$S = \frac{1}{2}ab\sin C$ $= \frac{1}{2}.13.4.\frac{{12}}{{13}} = 24.$

$p = \frac{{a + b + c}}{2}$ $= \frac{{13 + 4 + 15}}{2} = 16.$

$r = \frac{S}{p} = \frac{{24}}{{16}} = \frac{3}{2}.$

**DẠNG TOÁN 3: CHỨNG MINH ĐẲNG THỨC – BẤT ĐẲNG THỨC LIÊN QUAN ĐẾN CÁC YẾU TỐ CỦA TAM GIÁC – TỨ GIÁC.**

**1. PHƯƠNG PHÁP GIẢI**

Để chứng minh đẳng thức ta sử dụng các hệ thức cơ bản để biến đổi vế này thành vế kia, hai vế cùng bằng một vế hoặc biến đổi tương đương về một đẳng thức đúng.

Để chứng minh bất đẳng thức ta sử dụng các hệ thức cơ bản, bất đẳng thức cạnh trong tam giác và bất đẳng thức cổ điển (Cauchy, Bunhiacôpxki …).

2. CÁC VÍ DỤ

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 1: Cho tam giác $ABC$ thỏa mãn ${\sin ^2}A = \sin B.\sin C.$ Chứng minh rằng:

a) ${a^2} = bc.$

b) $\cos A \ge \frac{1}{2}.$

a) Áp dụng định lí sin ta có $\sin A = \frac{a}{{2R}}$, $\sin B = \frac{b}{{2R}}$, $\sin C = \frac{c}{{2R}}.$

Suy ra ${\sin ^2}A = \sin B.\sin C$ $\Leftrightarrow {\left( {\frac{a}{{2R}}} \right)^2} = \frac{b}{{2R}}.\frac{c}{{2R}}$ $\Leftrightarrow {a^2} = bc.$

b) Áp dụng định lí côsin và câu a ta có:

$\cos A = \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}$ $= \frac{{{b^2} + {c^2} – bc}}{{2bc}}$ $\ge \frac{{2bc – bc}}{{2bc}} = \frac{1}{2}.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 2: Cho tam giác $ABC$, chứng minh rằng:

a) $\cos \frac{A}{2} = \sqrt {\frac{{p(p – a)}}{{bc}}} .$

b) $\sin A + \sin B + \sin C$ $= 4\cos \frac{A}{2}\cos \frac{B}{2}\cos \frac{C}{2}.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-8.png" alt="">

a) Trên tia đối của tia $AC$ lấy $D$ thỏa $AD = AB = c.$

Suy ra tam giác $BDA$ cân tại $A$ và $\widehat {BDA} = \frac{1}{2}\widehat A.$

Áp dụng định lý hàm số côsin cho $\Delta ABD$, ta có:

$B{D^2} = A{B^2} + A{D^2} – 2AB.AD\cos \widehat {BAD}$ $= 2{c^2} – 2{c^2}\cos \left( {{{180}^0} – A} \right)$ $= 2{c^2}(1 + \cos A)$ $= 2{c^2}\left( {1 + \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}} \right)$ $= \frac{c}{b}(a + b + c)(b + c – a)$ $= \frac{{4c}}{b}p(p – a).$

Suy ra $BD = 2\sqrt {\frac{{cp(p – a)}}{b}} .$

Gọi $I$ là trung điểm của $BD$ suy ra $AI \bot BD.$

Trong tam giác $ADI$ vuông tại $I$, ta có:

$\cos \frac{A}{2} = \cos \widehat {ADI}$ $= \frac{{DI}}{{AD}} = \frac{{BD}}{{2c}}$ $= \sqrt {\frac{{p(p – a)}}{{bc}}} .$

Vậy $\cos \frac{A}{2} = \sqrt {\frac{{p(p – a)}}{{bc}}} .$

b) Từ định lý hàm số sin, ta có: $\sin A + \sin B + \sin C$ $= \frac{a}{{2R}} + \frac{b}{{2R}} + \frac{c}{{2R}} = \frac{p}{R}$ $(1).$

Theo câu a ta có: $\cos \frac{A}{2} = \sqrt {\frac{{p(p – a)}}{{bc}}} .$

Tương tự thì $\cos \frac{B}{2} = \sqrt {\frac{{p(p – b)}}{{ca}}}$ và $\cos \frac{C}{2} = \sqrt {\frac{{p(p – c)}}{{ab}}} .$

Kết hợp với công thức $S = \sqrt {p(p – a)(p – b)(p – c)}$ $= \frac{{abc}}{{4R}}.$

Suy ra $4\cos \frac{A}{2}\cos \frac{B}{2}\cos \frac{C}{2}$ $= 4\sqrt {\frac{{p(p – a)}}{{bc}}} \sqrt {\frac{{p(p – b)}}{{ca}}} \sqrt {\frac{{p(p – c)}}{{ab}}}$ $= \frac{{4p}}{{abc}}\sqrt {p(p – a)(p – b)(p – c)}$ $= \frac{{4pS}}{{abc}} = \frac{p}{R}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\sin A + \sin B + \sin C$ $= 4\cos \frac{A}{2}\cos \frac{B}{2}\cos \frac{C}{2}.$

Nhận xét: Từ câu a và hệ thức lượng giác cơ bản ta suy ra được các công: $\sin \frac{A}{2} = \sqrt {\frac{{(p – b)(p – c)}}{{bc}}}$, $\tan \frac{A}{2} = \sqrt {\frac{{(p – b)(p – c)}}{{p(p – a)}}}$, $\cot \frac{A}{2} = \sqrt {\frac{{p(p – a)}}{{(p – b)(p – c)}}} .$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 3: Cho tam giác $ABC$, chứng minh rằng:

a) $\cot A = \frac{{{b^2} + {c^2} – {a^2}}}{{4S}}.$

b) $\cot A + \cot B + \cot C \ge \sqrt 3 .$

a) Áp dụng định lí côsin và công thức $S = \frac{1}{2}bc\sin A$ ta có:

$\cot A = \frac{{\cos A}}{{\sin A}}$ $= \frac{{{b^2} + {c^2} – {a^2}}}{{2bc\sin A}}$ $= \frac{{{b^2} + {c^2} – {a^2}}}{{4S}}.$

b) Theo câu a tương tự ta có: $\cot B = \frac{{{c^2} + {a^2} – {b^2}}}{{4S}}$, $\cot C = \frac{{{a^2} + {b^2} – {c^2}}}{{4S}}.$

Suy ra $\cot A + \cot B + \cot C$ $= \frac{{{b^2} + {c^2} – {a^2}}}{{4S}}$ $+ \frac{{{c^2} + {a^2} – {b^2}}}{{4S}}$ $+ \frac{{{a^2} + {b^2} – {c^2}}}{{4S}}$ $= \frac{{{a^2} + {b^2} + {c^2}}}{{4S}}.$

Theo bất đẳng thức Cauchy ta có:

$(p – a)(p – b)(p – c)$ $\le {\left( {\frac{{3p – a – b – c}}{3}} \right)^3}$ $= {\left( {\frac{p}{3}} \right)^3}.$

Mặt khác $S = \sqrt {p(p – a)(p – b)(p – c)}$ $\Rightarrow S \le \sqrt {p\frac{{{p^3}}}{{27}}} = \frac{{{p^2}}}{{3\sqrt 3 }}.$

Ta có ${p^2} = \frac{{{{(a + b + c)}^2}}}{4}$ $\le \frac{{3\left( {{a^2} + {b^2} + {c^2}} \right)}}{4}$ suy ra $S \le \frac{{{a^2} + {b^2} + {c^2}}}{{4\sqrt 3 }}.$

Do đó $\cot A + \cot B + \cot C$ $\ge \frac{{{a^2} + {b^2} + {c^2}}}{{4.\frac{{{a^2} + {b^2} + {c^2}}}{{4\sqrt 3 }}}} = \sqrt 3 .$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 4: Cho tam giác $ABC.$ Chứng minh rằng điều kiện cần và đủ để hai trung tuyến kẻ từ $B$ và $C$ vuông góc với nhau là ${b^2} + {c^2} = 5{a^2}.$

Gọi $G$ là trọng tâm của tam giác $ABC.$

Khi đó hai trung tuyến kẻ từ $B$ và $C$ vuông góc với nhau khi và chỉ khi tam giác $GBC$ vuông tại $G.$

$\Leftrightarrow G{B^2} + G{C^2} = B{C^2}$ $\Leftrightarrow {\left( {\frac{2}{3}{m_b}} \right)^2} + {\left( {\frac{2}{3}{m_c}} \right)^2} = {a^2}$ $(*).$

Mặt khác theo công thức đường trung tuyến ta có:

$m_b^2 = \frac{{2\left( {{a^2} + {c^2}} \right) – {b^2}}}{4}$, $m_c^2 = \frac{{2\left( {{a^2} + {b^2}} \right) – {c^2}}}{4}.$

Suy ra $(*) \Leftrightarrow \frac{4}{9}\left( {m_b^2 + m_c^2} \right) = {a^2}.$

$\Leftrightarrow \frac{4}{9}\left[ {\frac{{2\left( {{a^2} + {c^2}} \right) – {b^2}}}{4} + \frac{{2\left( {{a^2} + {b^2}} \right) – {c^2}}}{4}} \right]$ $= {a^2}.$

$\Leftrightarrow 4{a^2} + {b^2} + {c^2} = 9{a^2}$ $\Leftrightarrow {b^2} + {c^2} = 5{a^2}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 5: Cho tứ giác $ABCD$ có $E$, $F$ là trung điểm các đường chéo. Chứng minh: $A{B^2} + B{C^2} + C{D^2} + D{A^2}$ $= A{C^2} + B{D^2} + 4E{F^2}.$

<img link="data_for_rag/toan10/images/cac-he-thuc-luong-trong-tam-giac-9.png" alt="">

Áp dụng công thức đường trung tuyến với tam giác $ABC$ và $ADC$ ta có:

$A{B^2} + B{C^2} = 2B{E^2} + \frac{{A{C^2}}}{2}$ $(1).$

$C{D^2} + D{A^2} = 2D{E^2} + \frac{{A{C^2}}}{2}$ $(2).$

Từ $(1)$ và $(2)$ suy ra:

$A{B^2} + B{C^2} + C{D^2} + D{A^2}$ $= 2\left( {B{E^2} + D{E^2}} \right) + A{C^2}.$

Mặt khác $EF$ là đường trung tuyến tam giác $BDF$ nên: $B{E^2} + D{E^2} = 2E{F^2} + \frac{{B{D^2}}}{2}.$

Suy ra $A{B^2} + B{C^2} + C{D^2} + D{A^2}$ $= A{C^2} + B{D^2} + 4E{F^2}.$

## Bài tập
## Bài 1: Chứng minh rằng trong mọi tam giác $ABC$ ta có:

a) $a = b.\cos C + c.\cos B.$

b) $\sin A = \sin B\cos C + \sin C\cos B.$

c) ${h_a} = 2R\sin B\sin C.$

d) $m_a^2 + m_b^2 + m_c^2$ $= \frac{3}{4}\left( {{a^2} + {b^2} + {c^2}} \right).$

e) ${S_{\Delta ABC}} = \frac{1}{2}\sqrt {A{B^2}.A{C^2} – {{(\overrightarrow {AB} .\overrightarrow {AC} )}^2}} .$

a) Áp dụng định lí côsin ta có:

$VP = b.\frac{{{a^2} + {b^2} – {c^2}}}{{2ab}}$ $+ c.\frac{{{c^2} + {a^2} – {b^2}}}{{2ca}}$ $= \frac{{{a^2} + {b^2} – {c^2} + {c^2} + {a^2} – {b^2}}}{{2a}}$ $= a = VT.$

b) $\sin A = \sin B\cos C + \sin C\cos B$ $\Leftrightarrow \frac{a}{{2R}} = \frac{b}{{2R}}.\cos C + \frac{c}{{2R}}.\cos B$ $\Leftrightarrow a = b\cos C + c\cos B$ (câu a).

c) ${h_a} = 2R\sin B\sin C$ $\Leftrightarrow \frac{{2S}}{a} = 2R\frac{b}{{2R}}\sin C$ $\Leftrightarrow S = \frac{1}{2}ab\sin C$ (đúng).

d) Áp dụng công thức đường trung tuyến.

e) $\sqrt {A{B^2}.A{C^2} – {{(\overrightarrow {AB.} \overrightarrow {AC} )}^2}}$ $= AB.AC\sqrt {1 – {{\cos }^2}A}$ $= AB.AC.\sin A.$

Từ đó suy ra điều phải chứng minh.

## Bài 2: Cho tam giác $ABC.$ Chứng minh rằng:

a) $b + c = 2a$ $\Leftrightarrow \frac{2}{{{h_a}}} = \frac{1}{{{h_b}}} + \frac{1}{{{h_c}}}.$

b) Góc $A$ vuông $\Leftrightarrow m_b^2 + m_c^2 = 5m_a^2.$

a) $b + c = 2a$ $\Leftrightarrow \frac{{2S}}{{{h_b}}} + \frac{{2S}}{{{h_c}}} = 2.\frac{{2S}}{{{h_a}}}$ $\Leftrightarrow \frac{1}{{{h_b}}} + \frac{1}{{{h_c}}} = \frac{2}{{{h_a}}}.$

b) $m_b^2 + m_c^2 = 5m_a^2$ $\Leftrightarrow \frac{{2\left( {{a^2} + {c^2}} \right) – {b^2}}}{4}$ $+ \frac{{2\left( {{a^2} + {b^2}} \right) – {c^2}}}{4}$ $= 5.\frac{{2\left( {{b^2} + {c^2}} \right) – {a^2}}}{4}.$

$\Leftrightarrow {b^2} + {c^2} = {a^2}$ $\Leftrightarrow$ góc $A$ vuông.

## Bài 3: Cho tam giác $ABC$ thỏa mãn ${a^4} = {b^4} + {c^4}.$ Chứng minh rằng:

a) Tam giác $ABC$ nhọn.

b) $2{\sin ^2}A = \tan B\tan C.$

a) Dễ thấy $a > b$, $a > c$ $\Rightarrow$ góc $A$ là lớn nhất.

Và ${a^4} = {b^4} + {c^4} < {a^2}.{b^2} + {a^2}.{c^2}$ $\Rightarrow {a^2} < {b^2} + {c^2}.$

Mặt khác theo định lí côsin ta có: $\cos A = \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}$ $\Rightarrow \cos A > 0.$

Do đó $\widehat A < {90^0}.$ Vậy tam giác $ABC$ nhọn.

b) $2{\sin ^2}A = \tan B\tan C$ $\Leftrightarrow 2{\sin ^2}A\cos B\cos C = \sin B\sin C.$

$\Leftrightarrow 2{\left( {\frac{a}{{2R}}} \right)^2}.\frac{{{a^2} + {c^2} – {b^2}}}{{2ac}}.\frac{{{a^2} + {b^2} – {c^2}}}{{2ab}}$ $= \frac{b}{{2R}}.\frac{c}{{2R}}$ $\Leftrightarrow {a^4} = {b^4} + {c^4}.$

## Bài 4: Gọi $S$ là diện tích tam giác $ABC.$ Chứng minh rằng:

a) $S = 2{R^2}\sin A\sin B\sin C.$

b) $S = Rr(\sin A + \sin B + \sin C).$

a) Ta có $S = \frac{{abc}}{{4R}}$ $= \frac{{2R\sin A.2R\sin B.2R\sin C}}{{4R}}$ $= 2{R^2}\sin A\sin B\sin C.$

b) $S = pr$ $= \frac{{a + b + c}}{2}r$ $= \frac{{2R\sin A + 2R\sin B + 2R\sin C}}{2}r.$

## Bài 5: Cho tứ giác lồi $ABCD$, gọi $\alpha$ là góc hợp bởi hai đường chéo $AC$ và $BD.$ Chứng minh diện tích $S$ của tứ giác cho bởi công thức: $S = \frac{1}{2}AC.BD.\sin \alpha .$

Gọi $I$ là giao điểm hai đường chéo. Khi đó:

$S = {S_{ABI}} + {S_{BC1}} + {S_{CDI}} + {S_{DAI}}.$

$= \frac{1}{2}AI.BI.\sin \widehat {AIB}$ $+ \frac{1}{2}BI.CI.\sin \widehat {BIC}$ $+ \frac{1}{2}CI.DI.\sin \widehat {CID}$ $+ \frac{1}{2}DI.AI.\sin \widehat {DIA}.$

Ta có các góc $\widehat {AIB}$, $\widehat {BIC}$, $\widehat {CID}$ và $\widehat {DIA}$ đôi một bù nhau suy ra:

$\sin \widehat {AIB} = \sin \widehat {BIC}$ $= \sin \widehat {CID} = \sin \widehat {DIA}$ $= \sin \alpha .$

Do đó $S = \frac{1}{2}BI.AC.\sin \alpha$ $+ \frac{1}{2}ID.AC.\sin \alpha$ $= \frac{1}{2}AC.BD.\sin \alpha .$

## Bài 6: Cho tam giác $ABC$ có $\widehat {BAC} = {120^0}$, $AD$ là đường phân giác trong ($D$ thuộc $BC$). Chứng minh rằng $\frac{1}{{AD}} = \frac{1}{{AB}} + \frac{1}{{AC}}.$

Với $AB = AC$ ta có điều phải chứng minh.

Với $AB \ne AC.$ Ta có: $\frac{{BD}}{{DC}} = \frac{{AB}}{{AC}}.$

$B{D^2} = A{B^2} + A{D^2} – 2AB.AD.\cos {60^0}$ $= A{B^2} + A{D^2} – AB.AD.$

$C{D^2} = A{C^2} + A{D^2} – 2AC.AD.\cos {60^0}$ $= A{C^2} + A{D^2} – AC.AD.$

$\Rightarrow \frac{{A{B^2}}}{{A{C^2}}} = \frac{{B{D^2}}}{{D{C^2}}}$ $= \frac{{A{B^2} + A{D^2} – AB.AD}}{{A{C^2} + A{D^2} – AC.AD}}.$

$\Leftrightarrow A{B^2}\left( {A{C^2} + A{D^2} – AC.AD} \right)$ $= A{C^2}\left( {A{B^2} + A{D^2} – AB.AD} \right).$

$\Leftrightarrow \left( {A{B^2} – A{C^2}} \right)A{D^2}$ $= AB.AC.AD(AB – AC).$

$$
\Leftrightarrow \left[ {\begin{array}{c}
{AB = AC}\\
{AD = \frac{{AB.AC}}{{AB + AC}}}
\end{array}} \right.
$$
 $\Leftrightarrow \frac{1}{{AD}} = \frac{1}{{AB}} + \frac{1}{{AC}}.$

## Bài 7: Cho tam giác $ABC$, chứng minh rằng:

a) $\frac{{\cos A + \cos B}}{{a + b}}$ $= \frac{{(b + c – a)(c + a – b)}}{{2abc}}.$

b) $\left( {{c^2} + {b^2} – {a^2}} \right)\tan A$ $= \left( {{c^2} + {a^2} – {b^2}} \right)\tan B.$

a) Áp dụng định lí côsin, ta có:

$2abc(\cos A + \cos B)$ $= 2abc\left( {\frac{{{b^2} + {c^2} – {a^2}}}{{2bc}} + \frac{{{a^2} + {c^2} – {b^2}}}{{2ac}}} \right).$

$= a\left( {{b^2} + {c^2} – {a^2}} \right) + b\left( {{a^2} + {c^2} – {b^2}} \right)$ $= (a + b)\left[ {{c^2} – {{(a + b)}^2}} \right].$

$= (a + b)(b + c – a)(c + a – b).$

Suy ra $\frac{{\cos A + \cos B}}{{a + b}}$ $= \frac{{(b + c – a)(c + a – b)}}{{2abc}}.$

b) Áp dụng định lí sin và côsin, ta có:

$\frac{{\tan A}}{{\tan B}} = \frac{{\sin A\cos B}}{{\sin B\cos A}}$ $= \frac{{\frac{a}{{2R}}.\frac{{{a^2} + {c^2} – {b^2}}}{{2ac}}}}{{\frac{b}{{2R}}.\frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}}}$ $= \frac{{{a^2} + {c^2} – {b^2}}}{{{b^2} + {c^2} – {a^2}}}.$

Suy ra $\left( {{c^2} + {b^2} – {a^2}} \right)\tan A$ $= \left( {{c^2} + {a^2} – {b^2}} \right)\tan B.$

## Bài 8: Cho tam giác nhọn $ABC$ nội tiếp đường tròn $(O;R).$ Chứng minh rằng:

a) ${h_a} \le \sqrt {p(p – a)} .$

b) ${a^2}{b^2} + {b^2}{c^2} + {c^2}{a^2}$ $\le {R^2}{(a + b + c)^2}.$

a) Ta có ${S_{ABC}}$ $= \sqrt {p(p – a)(p – b)(p – c)}$ $= \frac{1}{2}a{h_a}.$

Mặt khác $(a + b – c)(a + c – b)$ $= {a^2} – {(b – c)^2} \le {a^2}.$

$\Rightarrow \sqrt {(p – b)(p – c)} \le \frac{1}{2}a$ $\Rightarrow {h_a} \le \sqrt {p(p – a)} .$

b) Vì $S = \frac{{abc}}{{4R}}$ $= \frac{1}{2}a{h_a} = \frac{1}{2}b{h_b} = \frac{1}{2}c{h_c}$ nên bất đẳng thức tương đương với:

$\frac{{{a^2}{b^2}}}{{{R^2}}} + \frac{{{b^2}{c^2}}}{{{R^2}}} + \frac{{{c^2}{a^2}}}{{{R^2}}}$ $\le {(a + b + c)^2}$ $\Leftrightarrow 4\left( {h_a^2 + h_b^2 + h_c^2} \right)$ $\le {(a + b + c)^2}.$

Sử dụng câu a suy ra:

$4\left( {h_a^2 + h_b^2 + h_c^2} \right)$ $\le {(b + c)^2} – {a^2}$ $+ {(c + a)^2} – {b^2}$ $+ {(a + b)^2} – {c^2}$ $= {(a + b + c)^2}.$

Vậy ${a^2}{b^2} + {b^2}{c^2} + {c^2}{a^2} \le {R^2}{(a + b + c)^2}.$

## Bài 9: Cho tam giác $ABC.$ Chứng minh rằng:

$\sqrt {{r^2} + {{(p – a)}^2}}$ $+ \sqrt {{r^2} + {{(p – b)}^2}}$ $+ \sqrt {{r^2} + {{(p – c)}^2}}$ $\le \sqrt {ab + bc + ca} .$

Ta có: $S = pr$ $\Rightarrow {r^2} = \frac{{{S^2}}}{{{p^2}}}$ $= \frac{{(p – a)(p – b)(p – c)}}{p}.$

$\Rightarrow {r^2} + {(p – a)^2}$ $= (p – a)\left[ {\frac{{(p – b)(p – c)}}{p} + p – a} \right]$ $= \frac{{(p – a)bc}}{p}.$

Tương tự: ${r^2} + {(p – b)^2} = \frac{{(p – b)ac}}{p}$, ${r^2} + {(p – c)^2} = \frac{{(p – c)ab}}{p}.$

Do đó bất đẳng thức cần chứng minh tương đương với:

$\sqrt {(p – a)bc}$ $+ \sqrt {(p – b)ac}$ $+ \sqrt {(p – c)ab}$ $\le \sqrt {p(ab + bc + ca)} .$

Bất đẳng thức này đúng vì theo Cauchy-Schwarz ta có:

$\sqrt {(p – a)bc}$ $+ \sqrt {(p – b)ac}$ $+ \sqrt {(p – c)ab}$ $\le \sqrt {(p – a + p – b + p – c)(ab + bc + ac)}$ $= \sqrt {p(ab + bc + ca)} .$

## Bài 10: Cho tam giác $ABC.$ Gọi $r$ là bán kính đường tròn nội tiếp. Chứng minh rằng: $r = (p – a)\tan \frac{A}{2}$ $= (p – b)\tan \frac{B}{2}$ $= (p – c)\tan \frac{C}{2}.$

Ta có $S = pr$ $\Leftrightarrow r = \frac{S}{p}$ $= \frac{{\sqrt {p(p – a)(p – b)(p – c)} }}{p}$ $= \sqrt {\frac{{(p – a)(p – b)(p – c)}}{p}} .$

$(p – a)\tan \frac{A}{2}$ $= (p – a)\sqrt {\frac{{(p – b)(p – c)}}{{p(p – a)}}}$ $= \sqrt {\frac{{(p – a)(p – b)(p – c)}}{p}} .$

Từ đó: $r = (p – a)\tan \frac{A}{2}.$

Tương tự: $r = (p – b)\tan \frac{B}{2}$ và $r = (p – c)\tan \frac{C}{2}.$

Do đó: $r = (p – a)\tan \frac{A}{2}$ $= (p – b)\tan \frac{B}{2}$ $= (p – c)\tan \frac{C}{2}.$

## Bài 11: Cho tam giác $ABC$ có $\frac{c}{b} = \frac{{{m_b}}}{{{m_c}}} \ne 1.$ Chứng minh rằng $2\cot A = \cot B + \cot C.$

Áp dụng $\cot A = \frac{{{b^2} + {c^2} – {a^2}}}{{4S}}$ suy ra $2\cot A = \cot B + \cot C$ $\Leftrightarrow {b^2} + {c^2} = 2{a^2}.$

Áp dụng công thức đường trung tuyến ta có:

$\frac{c}{b} = \frac{{{m_b}}}{{{m_c}}}$ $\Leftrightarrow {c^2}.\frac{{2\left( {{a^2} + {b^2}} \right) – {c^2}}}{4}$ $= {b^2}.\frac{{2\left( {{a^2} + {c^2}} \right) – {b^2}}}{4}$ $\Leftrightarrow {b^4} – {c^4} = 2{a^2}\left( {{b^2} – {c^2}} \right).$

Suy ra ${b^2} + {c^2} = 2{a^2}.$

## Bài 12: Cho $M$ là điểm nằm trong tam giác $ABC$ sao cho: $\widehat {MAB} = \widehat {MBC} = \widehat {MCA} = \alpha .$ Chứng minh rằng: $\cot \alpha = \cot A + \cot B + \cot C.$

Áp dụng định lí côsin trong tam giác $MAB$, ta có:

$B{M^2} = A{B^2} + A{D^2} – 2AB.AD.\cos \alpha .$

Mặt khác ${S_{ABM}} = \frac{1}{2}AB.AM.\sin \alpha$ $\Rightarrow B{M^2} = A{B^2} + A{D^2} – 4{S_{MAB}}.\cot \alpha .$

Tương tự ta có: $C{D^2} = B{C^2} + B{D^2} – 4{S_{MBC}}.\cot \alpha$, $A{D^2} = A{C^2} + C{D^2} – 4{S_{MCA}}.\cot \alpha .$

Cộng vế với vế suy ra: $\cot \alpha = \frac{{{a^2} + {b^2} + {c^2}}}{{4S}}$ $= \cot A + \cot B + \cot C.$

## Bài 13: Cho tam giác $ABC$ có trọng tâm $G$ và $\widehat {GAB} = \alpha$, $\widehat {GBC} = \beta$, $\widehat {GCA} = \gamma .$ Chứng minh rằng $\cot \alpha + \cot \beta + \cot \gamma$ $= \frac{{3\left( {{a^2} + {b^2} + {c^2}} \right)}}{{4S}}.$

Áp dụng $\cot A = \frac{{{b^2} + {c^2} – {a^2}}}{{4S}}$ và công thức đường trung tuyến với chú ý ${S_{GBC}} = {S_{GCA}} = {S_{GAB}}.$

## Bài 14: Cho tam giác $ABC.$ Chứng minh rằng $(a – b)\cot \frac{C}{2}$ $+ (b – c)\cot \frac{A}{2}$ $+ (c – a)\cot \frac{B}{2} = 0.$

Gọi $D$ là điểm tiếp xúc của đường tròn nội tiếp $(I;r)$ tam giác với $BC.$

Suy ra $a = BD + DC$ $= r\left( {\cot \frac{B}{2} + \cot \frac{C}{2}} \right)$, tương tự ta có $b = r\left( {\cot \frac{C}{2} + \cot \frac{A}{2}} \right).$

Do đó $(a – b)\cot \frac{C}{2}$ $= r\left( {\cot \frac{B}{2}\cot \frac{C}{2} – \cot \frac{C}{2}\cot \frac{A}{2}} \right).$

Xây dựng các biểu thức tương tự và cộng lại suy ra điều phải chứng minh.

## Bài 15: Cho hình bình hành $ABCD$ có $AC = 3AD.$ Chứng minh rằng $\cot \widehat {BAD} \ge \frac{4}{3}.$

Ta có $A{C^2} + B{D^2}$ $= 2\left( {A{B^2} + A{D^2}} \right)$ $\Rightarrow A{B^2} + A{C^2} = 5B{D^2}.$

Sử dụng định lý côsin và bất đẳng thức Cauchy ta chứng minh được:

$\cos \widehat {BAD} \ge \frac{4}{5}$ $\Rightarrow \cot \widehat {BAD} \ge \frac{4}{3}.$

## Bài 16: Cho tam giác $ABC$ có các cạnh $a$, $b$, $c$ và diện tích $S.$ Chứng minh rằng ${a^2} + {b^2} + {c^2} \ge 4\sqrt 3 S.$

Áp dụng công thức diện tích Hê-rông và bất đẳng thức Cauchy.

**DẠNG TOÁN 4: NHẬN DẠNG TAM GIÁC.

****1. PHƯƠNG PHÁP GIẢI**

Sử dụng định lí côsin, định lí sin, công thức đường trung tuyến, công thức tính diện tích tam giác để biến đổi giả thiết về hệ thức liên hệ cạnh (hoặc góc) từ đó suy ra dạng của tam giác.

2. CÁC VÍ DỤ

<!-- chunk:14 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 1: Cho tam giác $ABC$ thoả mãn $\sin C = 2\sin B\cos A.$ Chứng minh rằng tam giác $ABC$ cân.

Áp dụng định lí côsin và sin ta có:

$\sin C = 2\sin B\cos A$ $\Leftrightarrow \frac{c}{{2R}} = 2.\frac{b}{{2R}}.\frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}.$

Suy ra tam giác $ABC$ cân tại đỉnh $C.$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 2: Cho tam giác $ABC$ thoả mãn $\sin A = \frac{{\sin B + \sin C}}{{\cos B + \cos C}}.$ Chứng minh rằng tam giác $ABC$ vuông.

Ta có: $\sin A = \frac{{\sin B + \sin C}}{{\cos B + \cos C}}$ $\Leftrightarrow \sin A(\cos B + \cos C)$ $= \sin B + \sin C.$

$\Leftrightarrow \frac{a}{{2R}}\left( {\frac{{{c^2} + {a^2} – {b^2}}}{{2ca}} + \frac{{{a^2} + {b^2} – {c^2}}}{{2ab}}} \right)$ $= \frac{{b + c}}{{2R}}.$

$\Leftrightarrow b\left( {{c^2} + {a^2} – {b^2}} \right) + c\left( {{a^2} + {b^2} – {c^2}} \right)$ $= 2{b^2}c + 2{c^2}b.$

$\Leftrightarrow {b^3} + {c^3} + {b^2}c + b{c^2} – {a^2}b – {a^2}c = 0$ $\Leftrightarrow (b + c)\left( {{b^2} + {c^2}} \right) – {a^2}(b + c) = 0.$

${b^2} + {c^2} = {a^2}$ $\Leftrightarrow \Delta ABC$ vuông tại $A.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/09/cac-he-thuc-luong-trong-tam-giac.html -->
## Ví dụ 3: Nhận dạng tam giác $ABC$ trong các trường hợp sau:

a) $a\sin A + b\sin B + c\sin C$ $= {h_a} + {h_b} + {h_c}.$

b) $\frac{{{{\cos }^2}A + {{\cos }^2}B}}{{{{\sin }^2}A + {{\sin }^2}B}}$ $= \frac{1}{2}\left( {{{\cot }^2}A + {{\cot }^2}B} \right).$

a) Áp dụng công thức diện tích ta có $S = \frac{1}{2}bc\sin A = \frac{1}{2}a{h_a}$ suy ra:

$a\sin A + b\sin B + c\sin C$ $= {h_a} + {h_b} + {h_c}$ $\Leftrightarrow a.\frac{{2S}}{{bc}} + b.\frac{{2S}}{{ca}} + c.\frac{{2S}}{{ab}}$ $= \frac{{2S}}{a} + \frac{{2S}}{b} + \frac{{2S}}{c}.$

$\Leftrightarrow {a^2} + {b^2} + {c^2} = ab + bc + ca$ $\Leftrightarrow {(a – b)^2} + {(b – c)^2} + {(c – a)^2} = 0.$

$\Leftrightarrow a = b = c.$

Vậy tam giác $ABC$ đều.

b) Ta có: $\frac{{{{\cos }^2}A + {{\cos }^2}B}}{{{{\sin }^2}A + {{\sin }^2}B}}$ $= \frac{1}{2}\left( {{{\cot }^2}A + {{\cot }^2}B} \right).$

$\Leftrightarrow \frac{{{{\cos }^2}A + {{\cos }^2}B + {{\sin }^2}A + {{\sin }^2}B}}{{{{\sin }^2}A + {{\sin }^2}B}}$ $= \frac{1}{2}\left( {{{\cot }^2}A + 1 + {{\cot }^2}B + 1} \right).$

$\Leftrightarrow \frac{2}{{{{\sin }^2}A + {{\sin }^2}B}}$ $= \frac{1}{2}\left( {\frac{1}{{{{\sin }^2}A}} + \frac{1}{{{{\sin }^2}B}}} \right)$ $\Leftrightarrow {\left( {{{\sin }^2}A + {{\sin }^2}B} \right)^2}$ $= 4{\sin ^2}A{\sin ^2}B.$

$\Leftrightarrow {\sin ^2}A = {\sin ^2}B$ $\Leftrightarrow {\left( {\frac{a}{{2R}}} \right)^2} = {\left( {\frac{b}{{2R}}} \right)^2}$ $\Leftrightarrow a = b$ $\Leftrightarrow \Delta ABC$ cân tại $C.$

## Bài tập
## Bài 1: Cho tam giác $ABC.$ Chứng minh tam giác $ABC$ cân nếu ${h_a} = c\sin A.$

Sử dụng công thức $S = \frac{1}{2}a{h_a} = \frac{1}{2}bc\sin A$ ta có:

${h_a} = c\sin A\Leftrightarrow b{h_a} = a{h_a}$ $\Leftrightarrow a = b$ suy ra tam giác $ABC$ cân tại $C.$

## Bài 2: Cho tam giác $ABC.$ Chứng minh tam giác $ABC$ cân nếu $4m_a^2 = b(b + 4c\cos A).$

Sử dụng công thức đường trung tuyến và định lí sin.

$4m_a^2 = b(b + 4c\cos A)$ $\Leftrightarrow 4\frac{{2\left( {{b^2} + {c^2}} \right) – {a^2}}}{4}$ $= b\left( {b + 4c.\frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}} \right)$ $\Leftrightarrow a = b.$

## Bài 3: Chứng minh rằng tam giác $ABC$ đều khi và chỉ khi: ${a^2} + {b^2} + {c^2} = 36{r^2}.$

Ta có: ${r^2} = \frac{{{S^2}}}{{{p^2}}}$ $= \frac{{(p – a)(p – b)(p – c)}}{p}.$

Theo Cauchy: $(p – a)(p – b)(p – c)$ $\le {\left( {\frac{{3p – a – b – c}}{3}} \right)^3}$ $= {\left( {\frac{p}{3}} \right)^3}.$

Suy ra $36{r^2} \le \frac{{4{p^3}}}{{3p}}$ $= \frac{{{{(a + b + c)}^2}}}{3}$ $\le {a^2} + {b^2} + {c^2}.$

Dấu bằng xảy ra khi và chỉ khi $a = b = c$ hay tam giác $ABC$ đều.

## Bài 4: Cho tam giác $ABC.$ Tìm góc $A$ trong tam giác biết các cạnh $a$, $b$, $c$ thoả mãn hệ thức: $b\left( {{b^2} – {a^2}} \right) = c\left( {{c^2} – {a^2}} \right)$ $(b \ne c).$

$b\left( {{b^2} – {a^2}} \right) = c\left( {{c^2} – {a^2}} \right)$ $\Leftrightarrow {b^3} – {c^3} = {a^2}(b – c)$ $\Leftrightarrow {b^2} + bc + {c^2} = {a^2}.$

Theo định lí côsin thì ${a^2} = {b^2} + {c^2} – 2bc\cos A$ $\Leftrightarrow \cos A = \frac{1}{2}$ $\Leftrightarrow \widehat A = {60^0}.$

## Bài 5: Cho $\Delta ABC$ thoả mãn điều kiện:
\left\{ {\begin{array}{l}
{\frac{{{a^3} + {c^3} – {b^3}}}{{a + c – b}} = {b^2}}\\
{a = 2b\cos C}
\end{array}} \right..
Chứng minh rằng $\Delta ABC$ đều.

Ta có: $\frac{{{a^3} + {c^3} – {b^3}}}{{a + c – b}} = {b^2}$ $\Leftrightarrow (b + c)\left( {{b^2} – bc + {c^2}} \right) = {a^2}(b + c)$ $\Leftrightarrow \cos A = \frac{1}{2}$ $\Leftrightarrow \widehat A = {60^0}.$

$a = 2b\cos C$ $\Leftrightarrow a = 2b\frac{{{a^2} + {b^2} – {c^2}}}{{2ab}}$ $\Leftrightarrow b = c.$

Vậy tam giác $ABC$ đều.

## Bài 6: Trong tam giác $ABC$, chứng minh rằng nếu diện tích tính theo công thức $S = \frac{1}{4}(a + b – c)(a – b + c)$ thì tam giác $ABC$ vuông.

Ta có: $S = \frac{1}{4}(a + b – c)(a – b + c)$ $= \frac{1}{4}\left[ {{a^2} – {{(b – c)}^2}} \right].$

$= \frac{1}{4}\left[ {\left( {{b^2} + {c^2} – 2\cos A} \right) – {{(b – c)}^2}} \right]$ $= \frac{1}{4}.2bc(1 – \cos A)$ $= \frac{1}{2}bc(1 – \cos A).$

Mặt khác ta lại có $S = \frac{1}{2}bc\sin A.$

Nên: $1 – \cos A = \sin A$ $\Leftrightarrow 1 – 2\cos A + {\cos ^2}A = {\sin ^2}A.$

$\Leftrightarrow \cos A(\cos A – 1) = 0$ $\Leftrightarrow \cos A = 0$ $\Leftrightarrow A = {90^0}.$

Vậy $\Delta ABC$ vuông tại $A.$

## Bài 7: Cho $\Delta ABC$ thỏa mãn: $\frac{{1 + \cos B}}{{\sin B}} = \frac{{2a + c}}{{\sqrt {4{a^2} – {c^2}} }}.$ Chứng minh rằng tam giác $ABC$ là tam giác cân.

Ta có: $\frac{{1 + \cos B}}{{\sin B}} = \frac{{2a + c}}{{\sqrt {4{a^2} – {c^2}} }}$ $\Leftrightarrow \frac{{{{(1 + \cos B)}^2}}}{{{{\sin }^2}B}} = \frac{{2a + c}}{{2a – c}}.$

$\Leftrightarrow \frac{{\left( {1 + 2\cos B + {{\cos }^2}B} \right) + {{\sin }^2}B}}{{{{\sin }^2}B}}$ $= \frac{{2a + c + 2a – c}}{{2a – c}}.$

$\Leftrightarrow \frac{{1 + \cos B}}{{1 – {{\cos }^2}B}} = \frac{{2a}}{{2a – c}}$ $\Leftrightarrow 2a – c = 2a – 2a\cos B.$

$\Leftrightarrow 2a\frac{{{c^2} + {a^2} – {b^2}}}{{2ac}} = c$ $\Leftrightarrow {a^2} – {b^2} = 0$ $\Leftrightarrow a = b.$

$\Leftrightarrow \Delta ABC$ là tam giác cân tại $C.$

## Bài 8: Chứng minh rằng tam giác $ABC$ vuông tại $A$ hoặc $B$ khi và chỉ khi $\sin C = \cos A + \cos B.$

Ta có: $\cos A + \cos B$ $= \frac{{{b^2} + {c^2} – {a^2}}}{{2bc}}$ $+ \frac{{{c^2} + {a^2} – {b^2}}}{{2ca}}$ $= \frac{{2(a + b)(p – a)(p – b)}}{{abc}}.$

Vậy $\sin C = \cos A + \cos B$ $\Leftrightarrow \frac{c}{{2R}} = \frac{{2(a + b)(p – a)(p – b)}}{{abc}}.$

$\Leftrightarrow \frac{{2cS}}{{abc}} = \frac{{2(a + b)(p – a)(p – b)}}{{abc}}$ $\Leftrightarrow {c^2}\left[ {{{(a + b)}^2} – {c^2}} \right]$ $= {(a + b)^2}\left[ {{c^2} – {{(a – b)}^2}} \right].$

$\Leftrightarrow {c^4} = {\left( {{a^2} – {b^2}} \right)^2}$
\Leftrightarrow \left[ {\begin{array}{l}
{{a^2} = {b^2} + {c^2}}\\
{{b^2} = {c^2} + {a^2}}
\end{array}} \right.
$\Leftrightarrow \Delta ABC$ vuông tại $A$ hoặc $B.$

## Bài 9: Cho tam giác $ABC$ có hai trung tuyến kẻ từ $B$ và $C$ vuông góc với nhau và có $Rr = \frac{{bc}}{{2(1 + \sqrt {10} )}}.$ Chứng minh rằng tam giác $ABC$ cân.

Gọi $G$ là trọng tâm, khi đó tam giác $GBC$ vuông tại $G.$ Theo định lí Pitago và công thức đường trung tuyến suy ra ${b^2} + {c^2} = 5{a^2}.$

Sử dụng $Rr = \frac{{bc}}{{2(1 + \sqrt {10} )}}$ trong đó $R = \frac{{abc}}{{4S}}$, $r = \frac{S}{p}$ suy ra $b + c = a\sqrt {10} .$

Từ hai giả thiết trên suy ra $b = c = a\sqrt 5 .$

## Bài 10: Chứng minh rằng tam giác $ABC$ đều khi và chỉ khi: $\sin \frac{A}{2}\sin \frac{B}{2} = \frac{{\sqrt {ab} }}{{4c}}.$

Ta có: $\sin \frac{A}{2}\sin \frac{B}{2} = \frac{{\sqrt {ab} }}{{4c}}$ $\Leftrightarrow \sqrt {\frac{{(p – b)(p – c)}}{{bc}}} \sqrt {\frac{{(p – c)(p – a)}}{{ca}}}$ $= \frac{{\sqrt {ab} }}{{4c}}.$

$\Leftrightarrow {(p – c)^2}(p – a)(p – b) = \frac{{{a^2}{b^2}}}{{16}}.$

$\Leftrightarrow [(a + b – c)(b + c – a)][(a + b – c)(c + a – b)]$ $= {a^2}{b^2}$ $(1).$

Nhận thấy: $0 < {b^2} – {(c – a)^2} < {b^2}$ và $0 < {a^2} – {(b – c)^2} < {a^2}.$

Nên $\left[ {{b^2} – {{(c – a)}^2}} \right]\left[ {{a^2} – {{(b – c)}^2}} \right] \le {a^2}{b^2}.$

Vậy
(1) \Leftrightarrow \left\{ {\begin{array}{l}
{c – a = 0}\\
{b – c = 0}
\end{array}} \right.
$$
 $\Leftrightarrow a = b = c$ $\Leftrightarrow \Delta ABC$ đều.