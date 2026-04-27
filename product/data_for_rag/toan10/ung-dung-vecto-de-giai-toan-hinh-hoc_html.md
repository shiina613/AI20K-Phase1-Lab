# Ứng dụng vectơ để giải toán hình học

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
Bài viết hướng dẫn áp dụng các kiến thức về vectơ để giải quyết các bài toán hình học.

## A. PHƯƠNG PHÁP CHUNG

Để giải một bài toán tổng hợp bằng phương pháp vectơ ta thường thực hiện theo các bước sau:

+ *Bước 1*: Chuyển giả thiết và kết luận của bài toán sang ngôn ngữ của vectơ, chuyển bài toán tổng hợp về bài toán vectơ.

+ *Bước 2*: Sử dụng các kiến thức vectơ để giải quyết bài toán đó.

+ *Bước 3*: Chuyển kết quả bài toán vectơ sang kết quả bài toán tổng hợp.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## I. CHỨNG MINH BA ĐIỂM THẲNG HÀNG – ĐƯỜNG THẲNG ĐI QUA ĐIỂM CỐ ĐỊNH VÀ ĐIỂM THUỘC ĐƯỜNG THẲNG CỐ ĐỊNH.

1. PHƯƠNG PHÁP GIẢI
+ Để chứng minh ba điểm $A$, $B$, $C$ thẳng hàng ta chứng minh hai vectơ $\overrightarrow {AB}$ và $\overrightarrow {AC}$ cùng phương, tức là tồn tại số thực $k$ sao cho: $\overrightarrow {AB} = k\overrightarrow {AC} .$

+ Để chứng minh đường thẳng $AB$ đi qua điểm cố định ta đi chứng minh ba điểm $A$, $B$, $H$ thẳng hàng với $H$ là một điểm cố định.

2. CÁC VÍ DỤ

<!-- chunk:2 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 1: Cho hai điểm phân biệt $A$, $B.$ Chứng minh rằng $M$ thuộc đường thẳng $AB$ khi và chỉ khi có hai số thực $\alpha$, $\beta$ có tổng bằng $1$ sao cho: $\overrightarrow {OM} = \alpha \overrightarrow {OA} + \beta \overrightarrow {OB} .$

Nếu $A$, $B$, $M$ thẳng hàng $\Rightarrow \overrightarrow {AM} = k\overrightarrow {AB}$ $\Leftrightarrow \overrightarrow {AO} + \overrightarrow {OM} = k(\overrightarrow {AO} + \overrightarrow {OB} ).$

$\Rightarrow \overrightarrow {OM} = (1 – k)\overrightarrow {OA} + k\overrightarrow {OB} .$

Đặt $\alpha = 1 – k$, $\beta = k$ $\Rightarrow \alpha + \beta = 1$ và $\overrightarrow {OM} = \alpha \overrightarrow {OA} + \beta \overrightarrow {OB} .$

Nếu $\overrightarrow {OM} = \alpha \overrightarrow {OA} + \beta \overrightarrow {OB}$ với $\alpha + \beta = 1$ $\Rightarrow \beta = 1 – \alpha .$

$\Rightarrow \overrightarrow {OM} = \alpha \overrightarrow {OA} + (1 – \alpha )\overrightarrow {OB}$ $\Rightarrow \overrightarrow {OM} – \overrightarrow {OB} = \alpha (\overrightarrow {OA} – \overrightarrow {OB} )$ $\Rightarrow \overrightarrow {BM} = \alpha \overrightarrow {BA} .$

Suy ra $M$, $A$, $B$ thẳng hàng.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 2: Cho góc $xOy.$ Các điểm $A$, $B$ thay đổi lần lượt nằm trên $Ox$, $Oy$ sao cho $OA + 2OB = 3.$ Chứng minh rằng trung điểm $I$ của $AB$ thuộc một đường thẳng cố định.

Định hướng: Ta có hệ thức vectơ xác định điểm $I$ là $\overrightarrow {OI} = \frac{1}{2}\overrightarrow {OA} + \frac{1}{2}\overrightarrow {OB}$ $(*).$

Từ ví dụ 1 ta cần xác định hai điểm cố định $A’$, $B’$ sao cho $\overrightarrow {OI} = \alpha \overrightarrow {OA’} + \beta \overrightarrow {OB’}$ với $\alpha + \beta = 1.$

Do đó từ hệ thức $(*)$ ta nghĩ tới việc xác định hai điểm cố định $A’$, $B’$ lần lượt trên $Ox$, $Oy.$

Ta có: $(*) \Leftrightarrow \overrightarrow {OI} = \frac{{OA}}{{2OA’}}\overrightarrow {OA’} + \frac{{OB}}{{2OB’}}\overrightarrow {OB’} .$ Từ đó ta cần chọn các điểm đó sao cho $\frac{{OA}}{{2OA’}} + \frac{{OB}}{{2OB’}} = 1.$ Kết hợp với giả thiết $OA + 2OB = 3$ ta chọn được điểm $A’$ và $B’$ sao cho $OA’ = \frac{3}{2}$, $OB’ = \frac{3}{4}.$

Lời giải: Trên $Ox$, $Oy$ lần lượt lấy hai điểm $A’$, $B’$ sao cho $OA’ = \frac{3}{2}$, $OB’ = \frac{3}{4}.$

Do $I$ là trung điểm của $AB$ nên $\overrightarrow {OI} = \frac{1}{2}\overrightarrow {OA} + \frac{1}{2}\overrightarrow {OB}$ $= \frac{{OA}}{{2OA’}}\overrightarrow {OA’} + \frac{{OB}}{{2OB’}}\overrightarrow {OB’} .$

Ta có: $\frac{{OA}}{{2OA’}} + \frac{{OB}}{{2OB’}}$ $= \frac{{OA}}{{2.\frac{3}{2}}} + \frac{{OB}}{{2.\frac{3}{4}}}$ $= \frac{1}{3}(OA + 2OB) = 1.$

Do đó điểm $I$ thuộc đường thẳng $A’B’$ cố định.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 3: Cho hình bình hành $ABCD$, $I$ là trung điểm của cạnh $BC$ và $E$ là điểm thuộc đoạn $AC$ thỏa mãn $\frac{{AE}}{{AC}} = \frac{2}{3}.$ Chứng minh ba điểm $D$, $E$, $I$ thẳng hàng.

Định hướng: Để chứng minh $D$, $E$, $I$ thẳng hàng ta đi tìm số $k$ sao cho $\overrightarrow {DE} = k\overrightarrow {DI}$, muốn vậy ta sẽ phân tích các vectơ $\overrightarrow {DE}$, $\overrightarrow {DI}$ qua hai vectơ không cùng phương $\overrightarrow {AB}$ và $\overrightarrow {AD}$ và sử dụng nhận xét: $m\vec a + n\vec b = \vec 0$ $\Leftrightarrow m = n = 0$ với $\overrightarrow a$, $\overrightarrow b$ là hai vectơ không cùng phương, từ đó tìm được $k = \frac{2}{3}.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-1.png" alt="">

Lời giải: Ta có $\overrightarrow {DI} = \overrightarrow {DC} + \overrightarrow {CI}$ $= \overrightarrow {DC} + \frac{1}{2}\overrightarrow {CB}$ $= \overrightarrow {AB} – \frac{1}{2}\overrightarrow {AD}$ $(1).$

Mặt khác theo giả thiết ta có $\overrightarrow {AE} = \frac{2}{3}\overrightarrow {AC}$ suy ra:

$\overrightarrow {DE} = \overrightarrow {DA} + \overrightarrow {AE}$ $= \overrightarrow {DA} + \frac{2}{3}\overrightarrow {AC}$ $= – \overrightarrow {AD} + \frac{2}{3}(\overrightarrow {AB} + \overrightarrow {AD} )$ $= \frac{2}{3}\overrightarrow {AB} – \frac{1}{3}\overrightarrow {AD}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\overrightarrow {DE} = \frac{2}{3}\overrightarrow {DI} .$

Vậy ba điểm $D$, $E$, $I$ thẳng hàng.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 4: Hai điểm $M$, $N$ chuyển động trên hai đoạn thẳng cố định $BC$ và $BD$ $(M \ne B,N \ne B)$ sao cho $2\frac{{BC}}{{BM}} + 3\frac{{BD}}{{BN}} = 10.$ Chứng minh rằng đường thẳng $MN$ luôn đi qua một điểm cố định.

Dễ thấy luôn tồn tại điểm $I$ thuộc $MN$ sao cho $2\frac{{BC}}{{BM}}\overrightarrow {IM} + 3\frac{{BD}}{{BN}}\overrightarrow {IN} = \vec 0$ $(1).$

Gọi $H$ là điểm thỏa mãn $2\overrightarrow {HC} + 3\overrightarrow {HD} = \vec 0$ $(2)$, do đó $H$ cố định.

Ta có $(2) \Leftrightarrow 5\overrightarrow {HB} + 2\overrightarrow {BC} + 3\overrightarrow {BD} = \vec 0.$

$\Leftrightarrow \frac{{2BC}}{{BM}}\overrightarrow {BM} + \frac{{3BD}}{{BN}}\overrightarrow {BN} = 5\overrightarrow {BH} .$

$\Leftrightarrow \frac{{2BC}}{{BM}}(\overrightarrow {BI} + \overrightarrow {IM} ) + \frac{{3BD}}{{BN}}(\overrightarrow {BI} + \overrightarrow {IN} ) = 5\overrightarrow {BH} .$

$\Leftrightarrow \left( {2\frac{{BC}}{{BM}} + 3\frac{{BD}}{{BN}}} \right)\overrightarrow {BI} = 5\overrightarrow {BH}$ (theo $(1)$).

$\Leftrightarrow 10\overrightarrow {BI} = 5\overrightarrow {BH}$ $\Leftrightarrow \overrightarrow {BI} = \frac{1}{2}\overrightarrow {BH}$ $(3).$

Do các điểm $B$, $H$ cố định, nên điểm $I$ cố định (xác định bởi hệ thức $(3)$).

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 5: Cho ba dây cung song song $A{A_1}$, $B{B_1}$, $C{C_1}$ của đường tròn $(O).$ Chứng minh rằng trực tâm của ba tam giác $AB{C_1}$, $BC{A_1}$, $CA{B_1}$ nằm trên một đường thẳng.

Gọi ${H_1}$, ${H_2}$, ${H_3}$ lần lượt là trực tâm của các tam giác $AB{C_1}$, $BC{A_1}$, $CA{B_1}.$

Ta có: $\overrightarrow {O{H_1}} = \overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {O{C_1}}$, $\overrightarrow {O{H_2}} = \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {O{A_1}}$ và $\overrightarrow {O{H_3}} = \overrightarrow {OC} + \overrightarrow {OA} + \overrightarrow {O{B_1}} .$

Suy ra $\overrightarrow {{H_1}{H_2}} = \overrightarrow {O{H_2}} – \overrightarrow {O{H_1}}$ $= \overrightarrow {OC} – \overrightarrow {O{C_1}} + \overrightarrow {O{A_1}} – \overrightarrow {OA}$ $= \overrightarrow {{C_1}C} + \overrightarrow {A{A_1}} .$

$\overrightarrow {{H_1}{H_3}} = \overrightarrow {O{H_3}} – \overrightarrow {O{H_1}}$ $= \overrightarrow {OC} – \overrightarrow {O{C_1}} + \overrightarrow {O{B_1}} – \overrightarrow {OB}$ $= \overrightarrow {{C_1}C} + \overrightarrow {B{B_1}} .$

Vì các dây cung $A{A_1}$, $B{B_1}$, $C{C_1}$ song song với nhau.

Nên ba vectơ $\overrightarrow {A{A_1}}$, $\overrightarrow {B{B_1}}$, $\overrightarrow {C{C_1}}$ có cùng phương.

Do đó hai vectơ $\overrightarrow {{H_1}{H_2}}$ và $\overrightarrow {{H_1}{H_3}}$ cùng phương hay ba điểm ${H_1}$, ${H_2}$, ${H_3}$ thẳng hàng.

## Bài tập
## Bài 1: Cho tam giác $ABC.$ Gọi $M$ là điểm thuộc cạnh $AB$, $N$ là điểm thuộc cạnh $AC$ sao cho $AM = \frac{1}{3}AB$, $AN = \frac{3}{4}AC.$ Gọi $O$ là giao điểm của $CM$ và $BN.$ Trên đường thẳng $BC$ lấy $E.$ Đặt $\overrightarrow {BE} = x\overrightarrow {BC} .$ Tìm $x$ để $A$, $O$, $E$ thẳng hàng.

Ta có: $\overrightarrow {AO} = \frac{1}{9}\overrightarrow {AB} + \frac{1}{4}\overrightarrow {AC} .$, $\overrightarrow {AE} = (1 – x)\overrightarrow {AB} + x\overrightarrow {AC} .$

$A$, $E$, $O$ thẳng hàng $\Leftrightarrow \overrightarrow {AE} = k\overrightarrow {AO} .$

$\Leftrightarrow (1 – x)\overrightarrow {AB} + x\overrightarrow {AC}$ $= \frac{k}{9}\overrightarrow {AB} + \frac{k}{4}\overrightarrow {AC}$ $\Leftrightarrow k = \frac{{36}}{{13}}$, $x = \frac{9}{{13}}.$

Vậy $x = \frac{9}{{13}}$ là giá trị cần tìm.

## Bài 2: Cho $\Delta ABC$ lấy các điểm $I$, $J$ thoả mãn $\overrightarrow {IA} = 2\overrightarrow {IB}$, $3\overrightarrow {JA} + 2\overrightarrow {JC} = \vec 0.$ Chứng minh rằng $IJ$ đi qua trọng tâm $G$ của $\Delta ABC.$

$\overrightarrow {IA} = 2\overrightarrow {IB}$ $\Leftrightarrow \overrightarrow {IA} – 2\overrightarrow {IB} = \vec 0.$

$3\overrightarrow {JA} + 2\overrightarrow {JC} = \vec 0$ $\Leftrightarrow 3\overrightarrow {IA} + 2\overrightarrow {IC} = 5\overrightarrow {IJ} .$

Suy ra $2(\overrightarrow {IA} + \overrightarrow {IB} + \overrightarrow {IC} ) = 5\overrightarrow {IJ}$ $\Leftrightarrow 6\overrightarrow {IG} = 5\overrightarrow {IJ}$ $\Leftrightarrow I$, $J$, $G$ thẳng hàng.

## Bài 3: Cho tam giác $ABC.$ Hai điểm $M$, $N$ di động thỏa mãn:

$\overrightarrow {MN} = \overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} .$

a) Chứng minh rằng $MN$ đi qua điểm cố định.

b) $P$ là trung điểm của $AM.$ Chứng minh rằng $MP$ đi qua điểm cố định.

a) Gọi $G$ là trọng tâm tam giác $ABC$ suy ra:

$\overrightarrow {MN} = \overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC}$ $\Leftrightarrow \overrightarrow {MN} = \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} + 3\overrightarrow {MG}$ $= 3\overrightarrow {MG} .$

Suy ra $M$, $N$, $G$ thẳng hàng hay $MN$ đi qua điểm cố định $G.$

b) $P$ là trung điểm $AM$ $\Rightarrow \overrightarrow {MP} = \frac{1}{2}(\overrightarrow {MA} + \overrightarrow {MN} )$ $= \frac{1}{2}(2\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} ).$

Gọi $I$ là trung điểm $BC$, $J$ là trung điểm $AI$ suy ra $2\overrightarrow {JA} + \overrightarrow {JB} + \overrightarrow {JC} = \vec 0.$

Do đó $\overrightarrow {MP} = 2\overrightarrow {MJ}$ suy ra $MP$ đi qua điểm cố định $J.$

## Bài 4: Cho hai điểm $M$, $P$ là hai điểm di động thỏa mãn:

$\overrightarrow {MP} = a\overrightarrow {MA} + b\overrightarrow {MB} + c\overrightarrow {MC} .$

Chứng minh rằng $MP$ đi qua điểm cố định.

Gọi $I$ là tâm đường tròn nội tiếp tam giác $ABC$ suy ra $a\overrightarrow {IA} + b\overrightarrow {IB} + c\overrightarrow {IC} = \vec 0.$

Do đó $\overrightarrow {MP} = a\overrightarrow {MA} + b\overrightarrow {MB} + c\overrightarrow {MC}$ $\Leftrightarrow \overrightarrow {MP} = (a + b + c)\overrightarrow {MI} .$

Vậy $MP$ đi qua điểm cố định $I.$

## Bài 5: Cho hình bình hành $ABCD.$ Gọi $E$ là điểm đối xứng của $D$ qua điểm $A$, $F$ là điểm đối xứng của tâm $O$ của hình bình hành qua điểm $C$ và $K$ là trung điểm của đoạn $OB.$ Chứng minh ba điểm $E$, $K$, $F$ thẳng hàng và $K$ là trung điểm của $EF.$

Ta có: $\overrightarrow {EF} = \frac{5}{2}\overrightarrow {AD} + \frac{3}{2}\overrightarrow {AB}$, $\overrightarrow {EK} = \frac{5}{4}\overrightarrow {AD} + \frac{3}{4}\overrightarrow {AB} .$

$\Rightarrow \overrightarrow {EF} = 2\overrightarrow {EK} .$

Vì vậy $K$ là trung điểm $EF.$

## Bài 6: Cho hai tam giác $ABC$ và ${A_1}{B_1}{C_1}$, ${A_2}$, ${B_2}$, ${C_2}$ lần lượt là trọng tâm các tam giác $BC{A_1}$, $CA{B_1}$, $AB{C_1}.$ Gọi $G$, ${G_1}$, ${G_2}$ lần lượt là trọng tâm các tam giác $ABC$, ${A_1}{B_1}{C_1}$, ${A_2}{B_2}{C_2}.$ Chứng minh rằng $G$, ${G_1}$, ${G_2}$ thẳng hàng và tính $\frac{{G{G_1}}}{{G{G_2}}}.$

Vì $G$, ${G_1}$ là trọng tâm tam giác $ABC$, ${A_1}{B_1}{C_1}$ suy ra:

$3\overrightarrow {G{G_1}} = \overrightarrow {G{A_1}} + \overrightarrow {G{B_1}} + \overrightarrow {G{C_1}} .$

$\Leftrightarrow 3\overrightarrow {G{G_1}} = \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC}$ $+ \overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} .$

$\Leftrightarrow 3\overrightarrow {G{G_1}} = \overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} .$

Tương tự $G$, ${G_2}$ là trọng tâm tam giác $ABC$, ${A_2}{B_2}{C_2}$ suy ra:

$3\overrightarrow {G{G_1}} = \overrightarrow {G{A_1}} + \overrightarrow {G{B_1}} + \overrightarrow {G{C_1}}$ $\Leftrightarrow 3\overrightarrow {G{G_2}} = \overrightarrow {A{A_2}} + \overrightarrow {B{B_2}} + \overrightarrow {C{C_2}} .$

Mặt khác $\overrightarrow {A{A_2}} + \overrightarrow {B{B_2}} + \overrightarrow {C{C_2}}$ $= \overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}}$ $+ \overrightarrow {{A_1}{A_2}} + \overrightarrow {{B_1}{B_2}} + \overrightarrow {{C_1}{C_2}} .$

Mà ${A_2}$, ${B_2}$, ${C_2}$ lần lượt là trọng tâm các tam giác $BC{A_1}$, $CA{B_1}$, $AB{C_1}.$

Suy ra $3(\overrightarrow {{A_1}{A_2}} + \overrightarrow {{B_1}{B_2}} + \overrightarrow {{C_1}{C_2}} )$ $= 3(\overrightarrow {{A_1}B} + \overrightarrow {{A_1}C} + \overrightarrow {{B_1}C} + \overrightarrow {{B_1}A} + \overrightarrow {{C_1}A} + \overrightarrow {{C_1}B} ).$

$= 6(\overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} ).$

Do đó $\overrightarrow {A{A_2}} + \overrightarrow {B{B_2}} + \overrightarrow {C{C_2}}$ $= 3(\overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} )$ $\Rightarrow \overrightarrow {G{G_2}} = \overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} .$

Vậy $\overrightarrow {G{G_2}} = 3\overrightarrow {G{G_1}} .$

## Bài 7: Cho tam giác $ABC.$ Các điểm $M$, $N$, $P$ lần lượt nằm trên đường thẳng $BC$, $CA$, $AB$ sao cho $\overrightarrow {MB} = \alpha \overrightarrow {MC}$, $\overrightarrow {NC} = \beta \overrightarrow {NA}$, $\overrightarrow {PA} = \gamma \overrightarrow {PB} .$ Tìm điều kiện của $\alpha$, $\beta$, $\gamma$ để $M$, $N$, $P$ thẳng hàng.

Ta có: $\overrightarrow {MB} = \frac{\alpha }{{1 – \alpha }}\overrightarrow {BC}$, $\overrightarrow {BP} = \frac{1}{{\gamma – 1}}\overrightarrow {AB}$, $\overrightarrow {BC} = (1 – \alpha )\overrightarrow {MC}$, $\overrightarrow {CN} = \frac{\beta }{{1 – \beta }}\overrightarrow {AC} .$

Ta có:

$\overrightarrow {MN} = – \frac{1}{{1 – \alpha }}\overrightarrow {AB} + \left( {\frac{1}{{1 – \alpha }} + \frac{\beta }{{1 – \beta }}} \right)\overrightarrow {AC} .$

$\overrightarrow {MP} = \left( { – \frac{\alpha }{{1 – \alpha }} – \frac{1}{{1 – \gamma }}} \right)\overrightarrow {AB} + \frac{\alpha }{{1 – \alpha }}\overrightarrow {AC} .$

Để $M$, $N$, $P$ thẳng hàng thì ta phải có:

$\frac{{ – \frac{\alpha }{{1 – \alpha }} – \frac{1}{{1 – \gamma }}}}{{ – \frac{1}{{1 – \alpha }}}}$ $= \frac{{\frac{\alpha }{{1 – \alpha }}}}{{\frac{1}{{1 – \alpha }} + \frac{\beta }{{1 – \beta }}}}$ $\Leftrightarrow \alpha \beta \gamma = 1.$

## Bài 8: Cho tứ giác $ABCD$ ngoại tiếp đường tròn tâm $O.$ Chứng minh rằng trung điểm hai đường chéo $AC$, $BD$ và tâm $O$ thẳng hàng.

Gọi $P$, $Q$, $R$, $S$ lần lượt là các tiếp điểm của các đoạn thẳng $AB$, $BC$, $CD$, $DA$ đối với đường tròn tâm $O.$

Đặt $SA = AP=a$, $BP =BQ=b$, $CQ=CR = c$, $DR = DS=d.$

Áp dụng định lý con nhím cho tứ giác $ABCD$ ta có:

$(a + b)\overrightarrow {OP} + (b + c)\overrightarrow {OQ}$ $+ (c + d)\overrightarrow {OR} + (d + a)\overrightarrow {OS} = \vec 0.$

$\Leftrightarrow (a + b)\left( {\frac{b}{{a + b}}\overrightarrow {OA} + \frac{a}{{a + b}}\overrightarrow {OB} } \right)$ $+ (b + c)\left( {\frac{c}{{b + c}}\overrightarrow {OB} + \frac{b}{{b + c}}\overrightarrow {OC} } \right)$ $+ (c + d)\left( {\frac{d}{{c + d}}\overrightarrow {OC} + \frac{c}{{c + d}}\overrightarrow {OD} } \right)$ $+ (d + a)\left( {\frac{a}{{d + a}}\overrightarrow {OD} + \frac{d}{{d + a}}\overrightarrow {OA} } \right).$

$\Leftrightarrow (b + d)(\overrightarrow {OA} + \overrightarrow {OC} )$ $+ (a + c)(\overrightarrow {OB} + \overrightarrow {OD} ) = \vec 0.$

$\Leftrightarrow (b + d)\overrightarrow {OM} + (a + c)\overrightarrow {ON} = \vec 0.$

Suy ra $O$, $M$, $N$ thẳng hàng.

## Bài 9: Cho lục giác $ABCDEF$ nội tiếp đường tròn tâm $O$ thỏa mãn $AB = CD = EF.$ Về phía ngoài lục giác dựng các tam giác $AMB$, $BNC$, $CPD$, $DQE$, $ERF$, $FSA$ đồng dạng và cân tại $M$, $N$, $P$, $Q$, $R$, $S.$ Gọi ${O_1}$, ${O_2}$ lần lượt là trọng tâm tam giác $MPR$ và $NQS.$ Chứng minh rằng ba điểm $O$, ${O_1}$, ${O_2}$ thẳng hàng.

Gọi ${M_1}$, ${N_1}$, ${P_1}$, ${Q_1}$, ${R_1}$, ${S_1}$ lần lượt là hình chiếu của $M$, $N$, $P$, $Q$, $R$, $S$ lên $AB$, $BC$, $CD$, $DE$, $EF$, $FA.$ Suy ra ${M_1}$, ${N_1}$, ${P_1}$, ${Q_1}$, ${R_1}$, ${S_1}$ lần lượt là trung điểm của $AB$, $BC$, $CD$, $DE$, $EF$, $FA.$

Ta có: $\overrightarrow {MS} + \overrightarrow {RQ} + \overrightarrow {PN}$ $= (\overrightarrow {M{M_1}} + \overrightarrow {{M_1}A} + \overrightarrow {A{S_1}} + \overrightarrow {{S_1}S} )$ $+ (\overrightarrow {R{R_1}} + \overrightarrow {{R_1}E} + \overrightarrow {E{Q_1}} + \overrightarrow {{Q_1}Q} )$ $+ (\overrightarrow {P{P_1}} + \overrightarrow {{P_1}C} + \overrightarrow {C{N_1}} + \overrightarrow {{N_1}N} )$ (vì theo định lí con nhím thì $\overrightarrow {M{M_1}} + \overrightarrow {P{P_1}} + \overrightarrow {R{R_1}} + \overrightarrow {{N_1}N} + \overrightarrow {{Q_1}Q} + \overrightarrow {{S_1}S} = \vec 0$).

Mặt khác $AB = CD = EF$ suy ra $\frac{{M{M_1}}}{{O{M_1}}} = \frac{{R{R_1}}}{{O{R_1}}} = \frac{{P{P_1}}}{{O{P_1}}} = \frac{1}{k}.$

Do đó $\overrightarrow {MS} + \overrightarrow {RQ} + \overrightarrow {PN}$ $= k(\overrightarrow {OM} + \overrightarrow {OP} + \overrightarrow {OR} ).$

$\Leftrightarrow \overrightarrow {OS} + \overrightarrow {OQ} + \overrightarrow {ON}$ $= (k + 1)(\overrightarrow {OM} + \overrightarrow {OP} + \overrightarrow {OR} )$ $\Leftrightarrow \overrightarrow {O{O_2}} = (k + 1)\overrightarrow {O{O_1}} .$

Hay ba điểm $O$, ${O_1}$, ${O_2}$ thẳng hàng.

<!-- chunk:7 level:1 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## II. CHỨNG MINH HAI ĐƯỜNG THẲNG SONG SONG – BA ĐƯỜNG THẲNG ĐỒNG QUY.

1. PHƯƠNG PHÁP GIẢI

Để chứng minh đường thẳng $AB$ song song với $CD$ ta đi chứng minh $\overrightarrow {AB} = k\overrightarrow {CD}$ và điểm $A$ không thuộc đường thẳng $CD.$

Để chứng minh ba đường thẳng đồng quy ta có thể chứng minh theo hai hướng sau:

+ Chứng minh mỗi đường thẳng cùng đi qua một điểm cố định.

+ Chứng minh một đường thẳng đi qua giao điểm của hai đường thẳng còn lại.

2. CÁC VÍ DỤ

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 1: Cho ngũ giác $ABCDE.$ Gọi $M$, $N$, $P$, $Q$ lần lượt là trung điểm của các cạnh $AB$, $BC$, $CD$, $DE.$ Gọi $I$, $J$ lần lượt là trung điểm của các đoạn $MP$ và $NQ.$ Chứng minh rằng $IJ$ song song với $AE.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-2.png" alt="">

Ta có: $2\overrightarrow {IJ} = \overrightarrow {IQ} + \overrightarrow {IN}$ $= \overrightarrow {IM} + \overrightarrow {MQ} + \overrightarrow {IP} + \overrightarrow {PN} .$

$= \overrightarrow {MQ} + \overrightarrow {PN}$ $= \frac{1}{2}(\overrightarrow {AE} + \overrightarrow {BD} ) + \frac{1}{2}\overrightarrow {DB}$ $= \frac{1}{2}\overrightarrow {AE} .$

Suy ra $IJ$ song song với $AE.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 2: Cho tam giác $ABC.$ Các điểm $M$, $N$, $P$ thuộc các đường thẳng $BC$, $CA$, $AB$ thỏa mãn $\alpha + \beta + \gamma \ne 0$, $\beta \overrightarrow {MB} + \gamma \overrightarrow {MC}$ $= \gamma \overrightarrow {NC} + \alpha \overrightarrow {NA}$ $= \alpha \overrightarrow {PA} + \beta \overrightarrow {PB} = \vec 0$ thì $AM$, $BN$, $CP$ đồng quy tại $O$, với $O$ là điểm được xác định bởi $\alpha \overrightarrow {OA} + \beta \overrightarrow {OB} + \gamma \overrightarrow {OC} = \overrightarrow 0 .$

Ta có $\beta \overrightarrow {MB} + \gamma \overrightarrow {MC} = \vec 0$ $\Leftrightarrow \beta (\overrightarrow {MO} + \overrightarrow {OB} )$ $+ \gamma (\overrightarrow {MO} + \overrightarrow {OC} ) = \vec 0.$

$\Leftrightarrow \alpha \overrightarrow {OA} + \beta \overrightarrow {OB} + \gamma \overrightarrow {OC}$ $+ (\beta + \gamma )\overrightarrow {MO} = \alpha \overrightarrow {OA} .$

$\Leftrightarrow (\beta + \gamma )\overrightarrow {MO} = \alpha \overrightarrow {OA} .$

Suy ra $M$, $O$, $A$ thẳng hàng hay $AM$ đi qua điểm cố định $O.$

Tương tự ta có $BN$, $CP$ đi qua $O.$

Vậy ba đường thẳng $AM$, $BN$, $CP$ đồng quy.

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 3: Cho sáu điểm trong đó không có ba điểm nào thẳng hàng. Gọi $Δ$ là một tam giác có ba đỉnh lấy trong sáu điểm đó và $Δ’$ là tam giác có ba đỉnh còn lại. Chứng minh rằng với các cách chọn $Δ$ khác nhau, các đường thẳng nối trọng tâm hai tam giác $Δ$ và $Δ’$ đồng quy.

Định hướng: Giả sử sáu điểm đó là $A$, $B$, $C$, $D$, $E$, $F.$

Ta cần chứng minh tồn tại một điểm $H$ cố định sao cho với các cách chọn $Δ$ khác nhau thì $H$ thuộc các đường thẳng nối trọng tâm hai tam giác $Δ$ và $Δ’$. Nếu $Δ$ là tam giác $ABC$ thì $Δ$ là tam giác $DEF.$ Gọi $G$ và $G’$ lần lượt là trọng tâm của tam giác $ABC$ và tam giác $DEF.$

$H$ thuộc đường thẳng $GG’$ khi có số thực $k$ sao cho $\overrightarrow {HG} = k\overrightarrow {HG’} .$

$\Leftrightarrow \frac{1}{3}(\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} )$ $= \frac{k}{3}(\overrightarrow {HD} + \overrightarrow {HE} + \overrightarrow {HF} ).$

$\Leftrightarrow \frac{1}{3}\overrightarrow {HA} + \frac{1}{3}\overrightarrow {HB} + \frac{1}{3}\overrightarrow {HC}$ $– \frac{k}{3}\overrightarrow {HD} – \frac{k}{3}\overrightarrow {HE} – \frac{k}{3}\overrightarrow {HF} = \vec 0.$

Vì vai trò của các điểm $A$, $B$, $C$, $D$, $E$, $F$ trong bài toán bình đẳng nên chọn $k$ sao cho $– \frac{k}{3} = \frac{1}{3} \Leftrightarrow k = – 1$ khi đó $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} + \overrightarrow {HD} + \overrightarrow {HE} + \overrightarrow {HF} = \vec 0.$

Lời giải: Gọi $H$ là trọng tâm sáu điểm $A$, $B$, $C$, $D$, $E$, $F$ khi đó:

$\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} + \overrightarrow {HD} + \overrightarrow {HE} + \overrightarrow {HF} = \vec 0$ $(*).$

Giả sử $G$, $G’$ lần lượt là trọng tâm của hai tam giác $ABC$, $DEF$ suy ra:

$\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$, $\overrightarrow {G’D} + \overrightarrow {G’E} + \overrightarrow {G’F} = \vec 0.$

Suy ra: $(*) \Leftrightarrow 3\overrightarrow {HG} + \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC}$ $= 3\overrightarrow {HG’} + \overrightarrow {G’D} + \overrightarrow {G’E} + \overrightarrow {G’F} .$

$\Leftrightarrow \overrightarrow {HG} = \overrightarrow {HG’}$

Do đó $GG’$ đi qua điểm cố định $H$, do đó các đường thẳng nối trọng tâm hai tam giác $\Delta$ và $\Delta’$ đồng quy.

## Bài tập
## Bài 1: Cho tứ giác $ABCD$, gọi $K$, $L$ lần lượt là trọng tâm của các tam giác $ABC$ và tam giác $BCD.$ Chứng minh rằng hai đường thẳng $KL$ và $AD$ song song với nhau.

Ta có $\overrightarrow {KA} + \overrightarrow {KB} + \overrightarrow {KC} = \vec 0$ và $\overrightarrow {LB} + \overrightarrow {LC} + \overrightarrow {LD} = \vec 0.$

Trừ vế với vế ta được:

$\overrightarrow {KA} – \overrightarrow {LD} + 2\overrightarrow {KL} = \vec 0$ $\Leftrightarrow (\overrightarrow {KL} + \overrightarrow {LA} ) – \overrightarrow {LD} + 2\overrightarrow {KL} = \vec 0$ $\Leftrightarrow \overrightarrow {DA} + 3\overrightarrow {KL} = \vec 0.$

Suy ra $KL // AD.$

## Bài 2: Trên các cạnh $BC$, $CA$, $AB$ của tam giác $ABC$ lần lượt lấy các điểm ${A_1}$, ${B_1}$, ${C_1}$ sao cho $\frac{{{A_1}B}}{{{A_1}C}} = \frac{{{B_1}C}}{{{B_1}A}} = \frac{{{C_1}A}}{{{C_1}B}} = k$ $(k > 0).$ Trên các cạnh ${B_1}{C_1}$, ${C_1}{A_1}$, ${A_1}{B_1}$ lần lượt lấy các điểm ${A_2}$, ${B_2}$, ${C_2}$ sao cho $\frac{{{A_2}{B_1}}}{{{A_2}{C_1}}} = \frac{{{B_2}{C_1}}}{{{B_2}{A_1}}} = \frac{{{C_2}{A_1}}}{{{C_2}{B_1}}} = \frac{1}{k}.$ Chứng minh rằng tam giác ${A_2}{B_2}{C_2}$ có các cạnh tương ứng song song với các cạnh của tam giác $ABC.$

$\overrightarrow {{A_2}{C_2}} = \frac{{{k^2} – k + 1}}{{{{(k + 1)}^2}}}\overrightarrow {AC}$, vì ${k^2} – k + 1 > 0$ và ${A_2} \notin AC$ nên ${A_2}{C_2}//AC.$

Tương tự ta có ${B_2}{C_2}//BC$ và ${A_2}{B_2}//AB.$

**Bài 3**: Trên đường tròn cho năm điểm trong đó không có ba điểm nào thẳng hàng. Qua trọng tâm của ba trong năm điểm đó kẻ đường thẳng vuông góc với đường thẳng đi qua hai điểm còn lại. Chứng minh rằng mười đường thẳng nhận được cắt nhau tại một điểm.

Giả sử năm điểm đó là ${A_1}$, ${A_2}$, ${A_3}$, ${A_4}$, ${A_5}$ nằm trên đường tròn $(O).$ Ta cần chứng minh tồn tại điểm $H$ thuộc mười đường thẳng đó.

Gọi $G$ là trọng tâm của tam giác ${A_1}{A_2}{A_3}$, $P$ là trung điểm của đoạn thẳng ${A_4}{A_5}.$ Vì $OP \bot {A_4}{A_5}$ (do $O{A_4} = O{A_5}$) nên điểm $H$ thuộc đường thẳng đi qua $G$ và vuông góc với đường thẳng ${A_4}{A_5}$ khi có số thực $k$ sao cho $\overrightarrow {HG} = k\overrightarrow {OP} .$ Mà $\overrightarrow {OG} = \frac{1}{3}(\overrightarrow {O{A_1}} + \overrightarrow {O{A_2}} + \overrightarrow {O{A_3}} )$ (vì $G$ là trọng tâm của tam giác ${A_1}{A_2}{A_3}$). $\overrightarrow {OP} = \frac{1}{2}(\overrightarrow {O{A_4}} + \overrightarrow {O{A_5}} )$ (vì $P$ là trung điểm của đoạn thẳng ${A_4}{A_5}$).

Do đó $\overrightarrow {HG} = k\overrightarrow {OP}$ $\Leftrightarrow \overrightarrow {OG} – \overrightarrow {OH} = k\overrightarrow {OP} .$

Hay $\frac{1}{3}(\overrightarrow {O{A_1}} + \overrightarrow {O{A_2}} + \overrightarrow {O{A_3}} ) – \overrightarrow {OH}$ $= \frac{k}{2}(\overrightarrow {O{A_4}} + \overrightarrow {O{A_5}} ).$

$\Leftrightarrow \overrightarrow {OH} = \frac{1}{3}\overrightarrow {O{A_1}} + \frac{1}{3}\overrightarrow {O{A_2}}$ $+ \frac{1}{3}\overrightarrow {O{A_3}} – \frac{k}{2}\overrightarrow {O{A_4}} – \frac{k}{2}\overrightarrow {O{A_5}} .$

Vì các điểm ${A_1}$, ${A_2}$, ${A_3}$, ${A_4}$, ${A_5}$ trong bài toán có vai trò bình đẳng nên chọn $k$ sao cho $– \frac{k}{2} = \frac{1}{3} \Leftrightarrow k = – \frac{2}{3}.$

Khi đó $\overrightarrow {OH} = \frac{1}{3}(\overrightarrow {O{A_1}} + \overrightarrow {O{A_2}} + \overrightarrow {O{A_3}} + \overrightarrow {O{A_4}} + \overrightarrow {O{A_5}} ).$

Hay $\overrightarrow {OH} = \frac{5}{3}\overrightarrow {OG}$ ($G$ là trọng tâm của hệ điểm $\left\{ {{A_1},{A_2},{A_3},{A_4},{A_5}} \right\}$).

## Bài 4: Cho tứ giác $ABCD$ nội tiếp đường tròn $(O).$ Gọi $M$, $N$, $P$, $Q$ lần lượt là trung điểm của các cạnh $AB$, $BC$, $CD$, $DA.$ Kẻ $MM’$, $NN’$, $PP’$, $QQ’$ lần lượt vuông góc với $CD$, $DA$, $AB$, $BC.$ Chứng tỏ rằng bốn đường thẳng $MM’$, $NN’$, $PP’$, $QQ’$ đồng quy tại một điểm. Nhận xét về điểm đồng quy và hai điểm $I$, $O$ ($I$ là giao điểm của $MP$ và $NQ$).

Ta cần chứng minh tồn tại điểm $H$ thuộc đường thẳng $MM’$, $NN’$, $PP’$, $QQ’.$

Vì $OP \bot CD$ (do $OC = OD$) nên điểm $H$ thuộc đường thẳng $MM’$ khi có số thực $k$ sao cho $\overrightarrow {HM} = k\overrightarrow {OP} .$

Mà $M$ và $P$ lần lượt là trung điểm của $AB$ và $CD$ nên:

$\overrightarrow {HM} = \frac{1}{2}(\overrightarrow {HA} + \overrightarrow {HB} )$, $\overrightarrow {OP} = \frac{1}{2}(\overrightarrow {OC} + \overrightarrow {OD} ).$

Do đó $\overrightarrow {HM} = k\overrightarrow {OP}$ hay $\frac{1}{2}(\overrightarrow {HA} + \overrightarrow {HB} ) = \frac{k}{2}(\overrightarrow {OC} + \overrightarrow {OD} ).$

$\Leftrightarrow \overrightarrow {HO} + \overrightarrow {OA} + \overrightarrow {HO} + \overrightarrow {OB}$ $= k(\overrightarrow {OC} + \overrightarrow {OD} )$ $\Leftrightarrow 2\overrightarrow {OH} = \overrightarrow {OA} + \overrightarrow {OB} – k\overrightarrow {OC} – k\overrightarrow {OD} .$

Vì các điểm $A$, $B$, $C$, $D$ trong bài toán có vai trò bình đẳng nên chọn $k=-1.$

Khi đó $2\overrightarrow {OH} = \overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} .$

Hay $2\overrightarrow {OH} = 4\overrightarrow {OI}$ (dễ thấy $I$ là trọng tâm của tứ giác $ABCD$) $\Leftrightarrow \overrightarrow {OH} = 2\overrightarrow {OI} .$

Vậy $H$ là điểm đối xứng của $O$ qua $I.$

## Bài 5: Cho năm điểm trong đó không có ba điểm nào thẳng hàng. Gọi $\Delta$ là một tam giác có ba đỉnh lấy trong năm điểm đó, hai điểm còn lại xác định một đoạn thẳng $\theta .$ Chứng minh rằng với các cách chọn $\Delta$ khác nhau, các đường thẳng nối trọng tâm tam giác $\Delta$ và trung điểm đoạn thẳng $\theta$ luôn đi qua một điểm cố định.

Gọi $A$, $B$, $C$ là ba đỉnh của tam giác $\Delta$ và $DE$ là đoạn thẳng $\theta .$ Gọi $G$ là trọng tâm tam giác $\Delta$ và $M$ là trung điểm của $DE$, thì với điểm $O$ tùy ý ta có: $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} + \overrightarrow {OE}$ $= 3\overrightarrow {OG} + 2\overrightarrow {IM} .$

Do đó $GM$ luôn đi qua điểm cố định $O$ là trọng tâm hệ điểm $A$, $B$, $C$, $D$, $E.$

## Bài 6: Cho tam giác $ABC.$ Ba đường thẳng $x$, $y$, $z$ lần lượt đi qua $A$, $B$, $C$ và chúng chia đôi chu vi tam giác $ABC.$ Chứng minh rằng $x$, $y$, $z$ đồng quy.

Đặt $BC = a$, $CA = b$, $AB = c.$

Giả sử đường thẳng $x$ đi qua $A$ cắt $BC$ tại $M$ khi đó ta có:

$AB + BM = AC + MC$ $\Leftrightarrow c + BM = b + MC$ $\Rightarrow c + 2BM = b + (BM + MC).$

Suy ra $BM = \frac{{a + b – c}}{2}$, $CM = \frac{{a – b + c}}{2}.$

Do đó: $(a + c – b)\overrightarrow {MB} + (a + b – c)\overrightarrow {MC} = \vec 0.$

Tương tự ta có:

$(a + b – c)\overrightarrow {NC} + (b + c – a)\overrightarrow {NA}$ $= (b + c – a)\overrightarrow {PA} + (a + c – b)\overrightarrow {PB} = \vec 0.$

Do đó $x$, $y$, $z$ đồng quy tại $I$ được xác định bởi:

$(b + c – a)\overrightarrow {IA}$ $+ (a + c – b)\overrightarrow {IB}$ $+ (a + b – c)\overrightarrow {IC} = \vec 0.$

## Bài 7: Cho tam giác $ABC$, các đường tròn bàng tiếp góc $A$, $B$, $C$ tương ứng tiếp xúc với các cạnh $BC$, $CA$, $AB$ tại $M$, $N$, $P.$ Chứng minh $AM$, $BN$, $CP$ cùng đi qua một điểm, xác định điểm đó.

Giả sử đường tròn bàng tiếp góc $A$ tiếp xúc $BC$ tại $M.$

Gọi $B’$, $C’$ là tiếp điểm của cạnh $AB$, $AC$ với đường tròn bàng tiếp góc $A.$

Khi đó $AB’ = AC’$ $\Leftrightarrow AB + BB’ = AC + CC’$ $\Leftrightarrow c + BM = c + CM.$

Bạn đọc tự giải tiếp.

## Bài 8: Cho tứ giác $ABCD.$ Gọi $M$, $N$, $P$, $Q$ là trung điểm các cạnh $AB$, $BC$, $CD$, $DA.$

a) Gọi $G$ là giao điểm của $MP$ và $NQ.$ Chứng minh rằng $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} + \overrightarrow {GD} = \vec 0.$

b) Gọi ${A_1}$, ${B_1}$, ${C_1}$, ${D_1}$ lần lượt là trọng tâm các tam giác $BCD$, $CDA$, $DAB$, $ABC.$ Chứng minh rằng các đường thẳng $A{A_1}$, $B{B_1}$, $C{C_1}$, $D{D_1}$ đồng quy tại điểm $G.$

a) Ta có: $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} + \overrightarrow {GD}$ $= 2\overrightarrow {GM} + \overrightarrow {MA} + \overrightarrow {MB} + 2\overrightarrow {GP} + \overrightarrow {PC} + \overrightarrow {PD}$ $= 2(\overrightarrow {GM} + \overrightarrow {GP} )$ $+ (\overrightarrow {MA} + \overrightarrow {MB} )$ $+ (\overrightarrow {PC} + \overrightarrow {PD} ) = \vec 0.$

b) $3\overrightarrow {A{A_1}} = \overrightarrow {AB} + \overrightarrow {AC} + \overrightarrow {AD}$, $4\overrightarrow {AG} = \overrightarrow {AB} + \overrightarrow {AC} + \overrightarrow {AD}$ $\Rightarrow \overrightarrow {A{A_1}} = \frac{4}{3}\overrightarrow {AG} .$

$\Rightarrow \overrightarrow {A{A_1}}$, $\overrightarrow {AG}$ cùng phương hay $A{A_1}$ đi qua $G.$

Tương tự ta có $B{B_1}$ đi qua $G$, $C{C_1}$ đi qua $G$, $D{D_1}$ đi qua $G.$

Vậy ta có $A{A_1}$, $B{B_1}$, $C{C_1}$, $D{D_1}$ đồng quy tại $G.$

## Bài 9: Cho tam giác $ABC$ có trọng tâm $G$, $M$ là một điểm tùy ý. Gọi ${A_1}$, ${B_1}$, ${C_1}$ lần lượt là các điểm đối xứng với $M$ qua các trung điểm $I$, $J$, $K$ của các cạnh $BC$, $CA$, $AB.$ Chứng minh rằng:

a) Các đường thẳng $A{A_1}$, $B{B_1}$, $C{C_1}$ đồng quy tại trung điểm $O$ của mỗi đường.

b) $M$, $G$, $O$ thẳng hàng và $\frac{{MO}}{{MG}} = \frac{3}{2}.$

a) Gọi $O$ là trung điểm $C{C_1}.$

$\overrightarrow {A{A_1}} = \overrightarrow {AM} + \overrightarrow {M{A_1}}$ $= \overrightarrow {AM} + \overrightarrow {MB} + \overrightarrow {MC}$ $= \overrightarrow {AC} + \overrightarrow {MB} .$

$2\overrightarrow {AO} = \overrightarrow {AC} + \overrightarrow {A{C_1}}$ $= \overrightarrow {AC} + \overrightarrow {MB}$ (vì $A{C_1}BM$ hình bình hành).

$\Rightarrow \overrightarrow {A{A_1}} = 2\overrightarrow {AO}$ hay $O$ là trung điểm $A{A_1}.$

Tương tự ta có $\overrightarrow {B{B_1}} = 2\overrightarrow {BO}$ hay $O$ là trung điểm $B{B_1}.$

Vậy $A{A_1}$, $B{B_1}$, $C{C_1}$ đồng quy tại trung điểm $O$ của mỗi đường.

b) Ta có: $3\overrightarrow {MG} = \overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} .$

$2\overrightarrow {MO} = \overrightarrow {MA} + \overrightarrow {M{A_1}}$ $= \overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC}$ $\Rightarrow 2\overrightarrow {MO} = 3\overrightarrow {MG} .$

$\Rightarrow M$, $G$, $O$ thẳng hàng và $\frac{{MO}}{{MG}} = \frac{3}{2}.$

## Bài 10: Cho tam giác $ABC.$ Gọi $M$, $N$, $P$ là các tiếp điểm của đường tròn nội tiếp tam giác $ABC$ với các cạnh $BC$, $CA$, $AB.$ Gọi ${\Delta _a}$ là đường thẳng đi qua trung điểm $PN$ và vuông góc với $BC$, ${\Delta _b}$ là đường thẳng đi qua trung điểm $PM$ và vuông góc với $AC$, ${\Delta _c}$ là đường thẳng đi qua trung điểm $MN$ và vuông góc với $AB.$ Chứng minh rằng ${\Delta _a}$, ${\Delta _b}$ và ${\Delta _c}$ đồng quy.

Đặt $\overrightarrow {IM} = \overrightarrow {{e_1}}$, $\overrightarrow {IN} = \overrightarrow {{e_2}}$, $\overrightarrow {IP} = \overrightarrow {{e_3}} .$

Gọi $X$, $Y$, $Z$ lần lượt là trung điểm của $NP$, $PM$, $MN.$

$O$ là điểm được xác định $2\overrightarrow {IO} = \overrightarrow {{e_1}} + \overrightarrow {{e_2}} + \overrightarrow {{e_3}} .$

Suy ra $\overrightarrow {OX} = \overrightarrow {OI} + \overrightarrow {IX}$ $= – \frac{1}{2}(\overrightarrow {{e_1}} + \overrightarrow {{e_2}} + \overrightarrow {{e_3}} )$ $+ \frac{1}{2}(\overrightarrow {{e_2}} + \overrightarrow {{e_3}} )$ $= – \frac{1}{2}\overrightarrow {{e_1}} .$

Suy ra $OX \bot BC$, tương tự ta có $OY \bot AC$, $OZ \bot AB.$

Suy ra ${\Delta _a}$, ${\Delta _b}$ và ${\Delta _c}$ đồng quy tại $O.$

## Bài 11: Cho hai hình bình hành $ABCD$ và $AB’C’D’$ sắp xếp sao cho $B’$ thuộc cạnh $AB$, $D’$ thuộc cạnh $AD.$ Chứng minh rằng các đường thẳng $DB’$, $CC’$, $BD’$ đồng quy.

Đặt $\frac{{AB’}}{{AB}} = m$, $\frac{{AD’}}{{AD}} = n$ $(0 < m,n < 1).$

Gọi $I$ là giao điểm $BD’$ và $DB’.$

Ta có $\overrightarrow {AC} = \overrightarrow {AB} + \overrightarrow {AD}$, $\overrightarrow {AC’} = \overrightarrow {AB’} + \overrightarrow {AD’}$ $= m\overrightarrow {AB} + n\overrightarrow {AD} .$

$\frac{{AD’}}{{AD}} = n$ $\Rightarrow \overrightarrow {D’A} = \frac{n}{{n – 1}}\overrightarrow {D’D}$ $\Rightarrow \overrightarrow {BD’} = \frac{{\overrightarrow {BA} – \frac{n}{{n – 1}}\overrightarrow {BD} }}{{1 – \frac{n}{{n – 1}}}}$ $= \frac{{1 – n}}{{1 – m}}\overrightarrow {BB’} + n\overrightarrow {BD} .$

$\Rightarrow \frac{{1 – n}}{{1 – m}}\overrightarrow {IB’} + n\overrightarrow {ID} = \vec 0$ $\Rightarrow \overrightarrow {IB’} = \frac{{n(m – 1)}}{{1 – n}}\overrightarrow {ID} .$

$\Rightarrow \overrightarrow {AI} = \frac{{\overrightarrow {AB’} + \frac{{n(m – 1)}}{{n – 1}}\overrightarrow {AD} }}{{1 + \frac{{n(m – 1)}}{{n – 1}}}}$ $= \frac{{m(n – 1)\overrightarrow {AB} + n(m – 1)\overrightarrow {AD} }}{{mn – 1}}.$

Do đó $\overrightarrow {IC} = \overrightarrow {AC} – \overrightarrow {AI}$ $= \frac{1}{{mn – 1}}\left( {(m – 1)\overrightarrow {AB} + (n – 1)\overrightarrow {AD} } \right).$

$\overrightarrow {C’C} = \overrightarrow {AC} – \overrightarrow {AC’}$ $= (1 – m)\overrightarrow {AB} + (1 – n)\overrightarrow {AD} .$

Suy ra $\overrightarrow {IC} = \frac{1}{{mn – 1}}\overrightarrow {C’C} .$

Suy ra $I$, $C’$, $C$ thẳng hàng, suy ra điều phải chứng minh.

<!-- chunk:11 level:1 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## III. BÀI TOÁN LIÊN QUAN ĐẾN TỈ SỐ ĐỘ DÀI ĐOẠN THẲNG.

1. PHƯƠNG PHÁP

Phân tích vectơ qua hai vectơ không cùng phương và sử dụng các kết quả sau:

Cho $\vec a$, $\vec b$ là hai vectơ không cùng phương, khi đó:

+ Với mọi vectơ $\overrightarrow x$ luôn tồn tại duy nhất các số thực $m$, $n$ sao cho $\overrightarrow x = m\vec a + n\vec b.$

+ $m\vec a + n\vec b = \vec 0$ $\Leftrightarrow m = n = 0.$

+ Nếu $\overrightarrow c = m\overrightarrow a + n\overrightarrow b$, $\overrightarrow {c’} = m’\overrightarrow a + n’\overrightarrow b$ $\left( {m’.n’ \ne 0} \right)$ và $\overrightarrow c$, $\overrightarrow {c’}$ là hai vectơ cùng phương thì $\frac{m}{{m’}} = \frac{n}{{n’}}.$

2. CÁC VÍ DỤ

<!-- chunk:12 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 1: Cho tam giác $ABC.$ Gọi $M$ là điểm thuộc cạnh $AB$, $N$ là điểm thuộc cạnh $AC$ sao cho $AM = \frac{1}{3}AB$, $AN = \frac{3}{4}AC.$ Gọi $O$ là giao điểm của $CM$ và $BN.$ Tính tỉ số $\frac{{ON}}{{BN}}$ và $\frac{{OM}}{{CM}}.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-3.png" alt="">

Giả sử $\overrightarrow {ON} = n\overrightarrow {BN}$, $\overrightarrow {OM} = m\overrightarrow {CM} .$

Ta có $\overrightarrow {AO} = \overrightarrow {AM} + \overrightarrow {MO}$ $= \overrightarrow {AM} – m\overrightarrow {CM} .$

$= \overrightarrow {AM} – m(\overrightarrow {AM} – \overrightarrow {AC} )$ $= \frac{1}{3}(1 – m)\overrightarrow {AB} + m\overrightarrow {AC} .$

Và $\overrightarrow {AO} = \overrightarrow {AN} + \overrightarrow {NO}$ $= \overrightarrow {AN} – n\overrightarrow {BN} .$

$= \overrightarrow {AN} – n(\overrightarrow {AN} – \overrightarrow {AB} )$ $= \frac{3}{4}(1 – n)\overrightarrow {AC} + n\overrightarrow {AB} .$

Vì $\overrightarrow {AO}$ chỉ có một cách biểu diễn duy nhất qua $\overrightarrow {AB}$ và $\overrightarrow {AC}$ suy ra:

$$
\left\{ {\begin{array}{l}
{\frac{1}{3}(1 – m) = n}\\
{\frac{3}{4}(1 – n) = m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m = \frac{2}{3}}\\
{n = \frac{1}{9}}
\end{array}} \right..
$$

Vậy $\frac{{ON}}{{BN}} = \frac{1}{9}$ và $\frac{{OM}}{{CM}} = \frac{2}{3}.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 2: Cho hình bình hành $ABCD.$ $M$ thuộc đường chéo $AC$ sao cho $AM =kAC.$ Trên các cạnh $AB$, $BC$ lấy các điểm $P$, $Q$ sao cho $MP // BC$, $MQ // AB.$ Gọi $N$ là giao điểm của $AQ$ và $CP.$ Tính tỉ số $\frac{{AN}}{{AQ}}$ và $\frac{{CN}}{{CP}}$ theo $k.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-4.png" alt="">

Đặt $\overrightarrow {AN} = x\overrightarrow {AQ}$, $\overrightarrow {CN} = y\overrightarrow {CP}$, ta có:

$\overrightarrow {DN} = \overrightarrow {DA} + \overrightarrow {AN}$ $= \overrightarrow {DA} + x\overrightarrow {AQ}$ $= \overrightarrow {DA} + x(\overrightarrow {AB} + \overrightarrow {BQ} )$ $= \overrightarrow {DA} + x\overrightarrow {DC} + x\frac{{BQ}}{{BC}}\overrightarrow {BC}$ $= \overrightarrow {DA} + x\overrightarrow {DC} – x\frac{{BQ}}{{BC}}\overrightarrow {DA} .$

Vì $MQ//AB$ $\Rightarrow \frac{{BQ}}{{BC}} = \frac{{AM}}{{AC}} = k$ nên $\overrightarrow {DN} = (1 – kx)\overrightarrow {DA} + x\overrightarrow {DC}$ $(1).$

Mặt khác $\overrightarrow {DN} = \overrightarrow {DC} + \overrightarrow {CN}$ $= \overrightarrow {DC} + y\overrightarrow {CP}$ $= \overrightarrow {DC} + y(\overrightarrow {CB} + \overrightarrow {BP} )$ $= \overrightarrow {DC} + y\overrightarrow {DA} + y\frac{{BP}}{{BA}}\overrightarrow {BA} .$

Vì $MP//BC$ $\Rightarrow \frac{{BP}}{{BA}} = \frac{{CM}}{{CA}}$ $= \frac{{CA – AM}}{{CA}} = 1 – k$ nên:

$\overrightarrow {DN} = \overrightarrow {DC} + y\overrightarrow {DA} – y(1 – k)\overrightarrow {DC}$ $= y\overrightarrow {DA} + (1 + ky – y)\overrightarrow {DC}$ $(2).$

Từ $(1)$ và $(2)$ ta suy ra: 
$$
\left\{ {\begin{array}{l}
{y = 1 – kx}\\
{x = 1 + ky – y}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x = \frac{k}{{{k^2} – k + 1}}}\\
{y = \frac{{1 – k}}{{{k^2} – k + 1}}}
\end{array}} \right..
$$

Do đó $\frac{{AN}}{{AQ}} = \frac{k}{{{k^2} – k + 1}}$ và $\frac{{CN}}{{CP}} = \frac{{1 – k}}{{{k^2} – k + 1}}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/09/ung-dung-vecto-de-giai-toan-hinh-hoc.html -->
## Ví dụ 3: Cho tam giác $ABC$ có trung tuyến $AM.$ Trên cạnh $AB$ và $AC$ lấy các điểm $B’$ và $C’.$ Gọi $M’$ là giao điểm của $B’C’$ và $AM.$ Chứng minh: $\frac{{AB}}{{AB’}} + \frac{{AC}}{{AC’}} = 2\frac{{AM}}{{AM’}}.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-5.png" alt="">

Đặt $\overrightarrow {AB} = x\overrightarrow {AB’}$, $\overrightarrow {AC} = y\overrightarrow {AC’}$, $\overrightarrow {AM} = z\overrightarrow {AM’} .$

Vì $M’ \in B’C’$ $\Rightarrow \exists k$: $\overrightarrow {B’M’} = k\overrightarrow {B’C’} .$

$\Leftrightarrow (\overrightarrow {AM’} – \overrightarrow {AB’} ) = k(\overrightarrow {AC’} – \overrightarrow {AB’} ).$

$\Rightarrow \overrightarrow {AM’} = (1 – k)\overrightarrow {AB’} + k\overrightarrow {AC’} .$

$\Leftrightarrow \frac{1}{z}\overrightarrow {AM} = \frac{{1 – k}}{x}\overrightarrow {AB} + \frac{k}{y}\overrightarrow {AC} .$

$\Leftrightarrow \frac{1}{z}.\frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} ) = \frac{{1 – k}}{x}\overrightarrow {AB} + \frac{k}{y}\overrightarrow {AC}$ $\Leftrightarrow \frac{1}{{2z}} = \frac{{1 – k}}{x} = \frac{k}{y} = \frac{1}{{x + y}}$ $\Rightarrow x + y = 2z.$

Hay $\frac{{AB}}{{AB’}} + \frac{{AC}}{{AC’}} = 2\frac{{AM}}{{AM’}}.$

## Bài tập

## Bài 1: Cho tam giác $ABC$, trên các cạnh $AB$, $BC$ ta lấy các điểm $M$, $N$ sao cho $\frac{{AM}}{{MB}} = \frac{2}{5}$, $\frac{{BN}}{{NC}} = \frac{1}{3}.$ Gọi $I$ là giao điểm của $AN$ và $CM.$ Tính tỉ số $\frac{{AI}}{{AN}}$ và $\frac{{CI}}{{IM}}.$

Đặt $\overrightarrow {AI} = x\overrightarrow {AN}$, $\overrightarrow {CI} = y\overrightarrow {CM} .$

Ta có: $\overrightarrow {AI} = x(\overrightarrow {AB} + \overrightarrow {BN} )$ $= x\overrightarrow {AB} + \frac{x}{4}\overrightarrow {BC} .$

$= x\overrightarrow {AB} + \frac{x}{4}(\overrightarrow {AC} – \overrightarrow {AB} )$ $= \frac{{3x}}{4}\overrightarrow {AB} + \frac{x}{4}\overrightarrow {AC}$ $= \frac{{21x}}{8}\overrightarrow {AM} + \frac{x}{4}\overrightarrow {AC} .$

Vì $M$, $I$, $C$ thẳng hàng nên ta có: $\frac{{21}}{8}x + \frac{x}{4} = 1$ $\Rightarrow x = \frac{8}{{23}}$ $\Rightarrow \frac{{AI}}{{AN}} = \frac{8}{{23}}.$

Tương tự: $\frac{{IC}}{{IM}} = \frac{{21}}{2}.$

## Bài 2: Cho tam giác $ABC$ và trung tuyến $AM.$ Một đường thẳng song song với $AB$ cắt các đoạn thẳng $AM$, $AC$ và $BC$ lần lượt tại $D$, $E$ và $F.$ Một điểm $G$ nằm trên cạnh $AB$ sao cho $FG$ song song $AC.$ Tính $\frac{{ED}}{{GB}}.$

Ta đặt: $\overrightarrow {CA} = \overrightarrow a$, $\overrightarrow {CB} = \overrightarrow b .$ Khi đó $\overrightarrow {CM} = \frac{{\overrightarrow b }}{2}$, $\overrightarrow {CE} = k\overrightarrow {CA} = k\overrightarrow a .$ Vì $E$ nằm ngoài đoạn thẳng $AC$ nên có số $k$ sao cho $\overrightarrow {CE} = k\overrightarrow {CA} = k\overrightarrow a$ với $0 <k <1.$ Khi đó $\overrightarrow {CF} = k\overrightarrow {CB} = k\overrightarrow b .$

Điểm $D$ nằm trên $AM$ và $EF$ nên có hai số $x$ và $y$ sao cho:

$\overrightarrow {CD} = x\overrightarrow {CA} + (1 – x)\overrightarrow {CM}$ $= y\overrightarrow {CE} + (1 – y)\overrightarrow {CF} .$

Hay $x\vec a + \frac{{1 – x}}{2}\vec b = ky\vec a + k(1 – y)\vec b.$

Vì hai vectơ $\overrightarrow a$, $\overrightarrow b$ không cùng phương nên $x = ky$ và $\frac{1-x}{2}=k(1-y)$

Suy ra $x = 2k -1$, do đó $\overrightarrow {CD} = (2k – 1)\overrightarrow a + (1 – k)\overrightarrow b .$

Ta có $\overrightarrow {ED} = \overrightarrow {CD} – \overrightarrow {CE}$ $= (1 – k)(\overrightarrow b – \overrightarrow a )$ $= (1 – k)\overrightarrow {AB} .$

Chú ý rằng vì $\overrightarrow {CF} = k\overrightarrow {CB}$ hay $\overrightarrow {AB} + \overrightarrow {BG} = k\overrightarrow {AB}$ suy ra $(1 – k)\overrightarrow {AB} = \overrightarrow {GB} .$

Do đó $\frac{{ED}}{{GB}} = 1.$

## Bài 3: Cho $\Delta ABC$ có $AB =3$, $AC = 4.$ Phân giác trong $AD$ của góc $BAC$ cắt trung tuyến $BM$ tại $I.$ Tính $\frac{{AD}}{{AI}}.$

Ta có: $\frac{{IB}}{{IM}} = \frac{{AB}}{{AM}} = \frac{3}{2}$ $\Rightarrow 2\overrightarrow {IB} + 3\overrightarrow {IM} = \vec 0$ $\Rightarrow 2\overrightarrow {AB} + 3\overrightarrow {AM} = 5\overrightarrow {AI}$ $(1).$

$\frac{{DB}}{{DC}} = \frac{{AB}}{{AC}} = \frac{3}{4}$ $\Rightarrow 4\overrightarrow {DB} + 3\overrightarrow {DC} = \vec 0$ $\Rightarrow 4\overrightarrow {AB} + 3\overrightarrow {AC} = 7\overrightarrow {AD}$ $(2).$

Từ $(1)$ và $(2)$ suy ra:

$3\overrightarrow {AC} – 6\overrightarrow {AM} = 7\overrightarrow {AD} – 10\overrightarrow {AI}$ $\Rightarrow 7\overrightarrow {AD} – 10\overrightarrow {AI} = \vec 0$ $\Rightarrow \frac{{AD}}{{AI}} = \frac{{10}}{7}.$

## Bài 4: Cho tam giác $ABC$, trên cạnh $AC$ lấy điểm $M$, trên cạnh $BC$ lấy điểm $N$ sao cho: $AM = 3MC$, $NC = 2NB$, gọi $O$ là giao điểm của $AN$ và $BM.$ Tính diện tích $\Delta ABC$ biết diện tích $\Delta OBN$ bằng $1.$

Vì $A$, $O$, $N$ thẳng hàng nên: $\overrightarrow {BO} = x\overrightarrow {BA} + (1 – x)\overrightarrow {BN} .$

Tương tự: $\overrightarrow {AO} = y\overrightarrow {AM} + (1 – y)\overrightarrow {AB} .$

$\Rightarrow \overrightarrow {AB} = y\overrightarrow {AM}$ $+ (x – y + 1)\overrightarrow {AB} + (x – 1)\overrightarrow {BN} .$

Hay $(x – y)\overrightarrow {AB} + y\overrightarrow {AM} + (x – 1)\overrightarrow {BN} = \vec 0$ $(1).$

Đặt $\overrightarrow {CB} = \overrightarrow a$, $\overrightarrow {CA} = \overrightarrow b .$

Ta có: $\overrightarrow {AB} = \overrightarrow a – \overrightarrow b$, $\overrightarrow {AM} = – \frac{3}{4}\overrightarrow b$, $\overrightarrow {BN} = – \frac{1}{3}\overrightarrow a .$

Thay vào $(1)$ ta có: $(x – y)(\vec a – \vec b)$ $– \frac{3}{4}y\vec b + (x – y)\left( { – \frac{1}{3}\vec a} \right) = \vec 0.$

$\Leftrightarrow (x – y)\vec a – (x – y)\vec b$ $= \frac{{x – 1}}{3}\vec a – \frac{{3y}}{4}\vec b.$

Từ đó ta có:

$$
\left\{ {\begin{array}{c}
{x – y = \frac{{x – 1}}{3}}\\
{y – x = \frac{3}{4}y}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = \frac{1}{{10}}}\\
{y = \frac{2}{5}}
\end{array}} \right..
$$

Với $x = \frac{1}{{10}}$ $\Rightarrow \overrightarrow {BO} = \frac{1}{{10}}\overrightarrow {BA} + \left( {1 – \frac{1}{{10}}} \right)\overrightarrow {BN} .$

$\Rightarrow \overrightarrow {BO} – \overrightarrow {BN} = \frac{1}{{10}}(\overrightarrow {BA} – \overrightarrow {BN} )$ hay $\overrightarrow {NO} = \frac{1}{{10}}\overrightarrow {NA}$ $\Rightarrow \frac{{NA}}{{NO}} = 10.$

Vì ${S_{ONB}} = 1$ $\Rightarrow {S_{NAB}} = 10$ $\Rightarrow {S_{ABC}} = 30.$

## Bài 5: Cho hình bình hành $ABCD.$ Gọi $M$, $N$ lần lượt là điểm nằm trên cạnh $AB$, $CD$ sao cho $AB = 3AM$, $CD = 2CN$, $G$ là trọng tâm tam giác $MNB$ và $AG$ cắt $BC$ tại $I.$ Tính $\frac{{BI}}{{BC}}.$

Đặt $\frac{{BI}}{{BC}} = k$, $k > 0$ $\Rightarrow \overrightarrow {BI} = k\overrightarrow {BC} .$

Ta có: $\overrightarrow {AI} = \overrightarrow {AB} + \overrightarrow {BI}$ $= \overrightarrow {AB} + k\overrightarrow {BC}$ $= \overrightarrow {AB} + k\overrightarrow {AD} .$

Mặt khác $G$ là trọng tâm tam giác $MNB$ suy ra:

$3\overrightarrow {AG} = \overrightarrow {AM} + \overrightarrow {AN} + \overrightarrow {AB}$ $= \frac{1}{3}\overrightarrow {AB} + \frac{1}{2}(\overrightarrow {AD} + \overrightarrow {AC} ) + \overrightarrow {AB} .$

$= \frac{1}{3}\overrightarrow {AB} + \frac{1}{2}(2\overrightarrow {AD} + \overrightarrow {AB} ) + \overrightarrow {AB}$ $= \frac{{11}}{6}\overrightarrow {AB} + \overrightarrow {AD} .$

Vì $\overrightarrow {AG}$, $\overrightarrow {AI}$ cùng phương nên $\frac{{11}}{6} = \frac{1}{k} \Rightarrow k = \frac{6}{{11}}.$

## Bài 6: Cho tứ giác $ABCD$ có hai đường chéo cắt nhau tại $O.$ Qua trung điểm $M$ của $AB$ dựng đường thẳng $MO$ cắt $CD$ tại $N.$ Biết $OA =1$, $OB = 2$, $OC = 3$, $OD=4$, tính $\frac{{CN}}{{ND}}.$

Ta có $\overrightarrow {OC} = – 3\overrightarrow {OA}$, $\overrightarrow {OD} = – 2\overrightarrow {OB} .$

Vì $\overrightarrow {OM}$, $\overrightarrow {ON}$ cùng phương nên có số thực $k$ sao cho:

$\overrightarrow {ON} = k\overrightarrow {OM}$ $\Rightarrow \overrightarrow {ON} = \frac{k}{2}(\overrightarrow {OA} + \overrightarrow {OB} ).$

Đặt $\frac{{CN}}{{ND}} = k$, $k > 0$ ta có $\overrightarrow {ON} = – \frac{3}{{1 + k}}\overrightarrow {OA} – \frac{{2k}}{{k + 1}}\overrightarrow {OB} .$

Suy ra $– \frac{6}{{k(1 + k)}} = – \frac{{4k}}{{k(k + 1)}}$ $\Leftrightarrow k = \frac{3}{2}.$

## Bài 7: Cho tam giác $ABC.$ $M$ là điểm nằm trên cạnh $BC$ sao cho ${S_{ABC}} = 3{S_{AMC}}.$ Một đường thẳng cắt các cạnh $AB$, $AM$, $AC$ lần lượt tại $B’$, $M’$, $C’$ phân biệt. Chứng minh rằng $\frac{{AB}}{{AB’}} + 2\frac{{AC}}{{AC’}} = 3\frac{{AM}}{{AM’}}.$

Ta có ${S_{ABC}} = 3{S_{AMC}}$ $\Rightarrow BC = 3MC$ $\Rightarrow \overrightarrow {BM} = \frac{2}{3}\overrightarrow {BC} .$

Đặt $\overrightarrow {AB’} = x\overrightarrow {AB}$, $\overrightarrow {AC’} = y\overrightarrow {AC}$, $\overrightarrow {AM’} = z\overrightarrow {AM} .$

Ta có: $\overrightarrow {B’M’} = \overrightarrow {AM’} – \overrightarrow {AB’}$ $= z\overrightarrow {AM} – x\overrightarrow {AB} .$

$= z(\overrightarrow {AB} + \overrightarrow {BM} ) – x\overrightarrow {AB}$ $= (z – x)\overrightarrow {AB} + \frac{{2z}}{3}\overrightarrow {BC} .$

$= (z – x)\overrightarrow {AB} + \frac{{2z}}{3}(\overrightarrow {AC} – \overrightarrow {AB} )$ $= \left( {\frac{z}{3} – x} \right)\overrightarrow {AB} + \frac{{2z}}{3}\overrightarrow {AC} .$

$\overrightarrow {B’C’} = \overrightarrow {AC’} – \overrightarrow {AB’}$ $= y\overrightarrow {AC} – x\overrightarrow {AB} .$

Mặt khác $\overrightarrow {B’M’}$, $\overrightarrow {B’C’}$ cùng phương nên $\frac{{\frac{z}{3} – x}}{{ – x}} = \frac{{\frac{{2z}}{3}}}{y}$ $\Leftrightarrow \frac{3}{z} = \frac{1}{x} + \frac{2}{y}.$

Hay $\frac{{AB}}{{AB’}} + 2\frac{{AC}}{{AC’}} = 3\frac{{AM}}{{AM’}}.$

## Bài 8: Trong đường tròn $(O)$ với hai dây cung $AB$ và $CD$ cắt nhau tại $M.$ Qua trung điểm $S$ của $BD$ kẻ $SM$ cắt $AC$ tại $K.$ Chứng minh rằng $\frac{{A{M^2}}}{{C{M^2}}} = \frac{{AK}}{{CK}}.$

<img link="data_for_rag/toan10/images/ung-dung-vecto-de-giai-toan-hinh-hoc-6.png" alt="">

Đặt $\frac{{AK}}{{CK}} = x > 0.$

Ta có $\overrightarrow {MK} = \frac{1}{{1 + x}}\overrightarrow {MA} + \frac{x}{{1 + x}}\overrightarrow {MC}$ $(1).$

Do $\overrightarrow {MK}$, $\overrightarrow {MS}$ cùng phương nên $\overrightarrow {MK} = l.\overrightarrow {MS}$ $= \frac{l}{2}(\overrightarrow {MB} + \overrightarrow {MD} ).$

Mặt khác: $MA.MB = MC.MD = a > 0$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\overrightarrow {MB} = – \frac{a}{{M{A^2}}}\overrightarrow {MA} }\\
{\overrightarrow {MD} = – \frac{a}{{M{C^2}}}\overrightarrow {MC} }
\end{array}} \right..
$$

Suy ra $\overrightarrow {MK} = – \frac{{{\rm{ }}al{\rm{ }}}}{{2M{A^2}}}\overrightarrow {MA} – \frac{{{\rm{ }}al{\rm{ }}}}{{2M{C^2}}}\overrightarrow {MC}$ $(2).$

Từ $(1)$ và $(2)$ suy ra: 
$$
\left\{ {\begin{array}{l}
{\frac{1}{{1 + x}} = – \frac{{al}}{{2M{A^2}}}}\\
{\frac{x}{{1 + x}} = – \frac{{al}}{{2M{C^2}}}}
\end{array}} \right.
$$
 $\Rightarrow x = \frac{{M{A^2}}}{{M{C^2}}}$ $\Rightarrow \frac{{A{M^2}}}{{C{M^2}}} = \frac{{AK}}{{CK}}.$