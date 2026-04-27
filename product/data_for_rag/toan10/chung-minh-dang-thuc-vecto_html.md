# Chứng minh đẳng thức vectơ

<!-- chunk:0 level:0 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
Bài viết hướng dẫn phương pháp giải một số bài toán chứng minh đẳng thức vectơ, đây là dạng toán thường gặp trong chương trình Hình học 10 chương 1.

Phương pháp giải toán:

Để chứng minh một đẳng thức vectơ ta chú ý:

1) Sử dụng:

+ Quy tắc $3$ điểm: $\overrightarrow {AB} + \overrightarrow {BC} = \overrightarrow {AC}$, $\overrightarrow {AC} – \overrightarrow {AB} = \overrightarrow {BC}$ với mọi $A$, $B$, $C.$

+ Quy tắc hình bình hành: $\overrightarrow {AB} + \overrightarrow {AD} = \overrightarrow {AC}$ với $ABCD$ là hình bình hành.

+ Quy tắc trung điểm: $\overrightarrow {MA} + \overrightarrow {MB} = 2\overrightarrow {MI}$ với $I$ là trung điểm của $AB.$

+ Quy tắc trọng tâm: $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ với $G$ là trọng tâm tam giác $ABC.$

+ Các tính chất của các phép toán.

2) Thực hiện các phép biến đổi theo một trong các hướng sau:

+ Biến đổi vế này thành vế kia của đẳng thức (thông thường là xuất phát từ vế phức tạp biến đổi rút gọn để đưa về vế đơn giản hơn).

+ Biến đổi đẳng thức cần chứng minh về tương đương với một đẳng thức luôn đúng.

+ Xuất phát từ một đẳng thức luôn đúng để biến đổi về đẳng thức cần chứng minh.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 1: Cho $4$ điểm $A$, $B$, $C$, $D$. Chứng minh rằng:

a) $\overrightarrow {AB} + \overrightarrow {CD} = \overrightarrow {AD} + \overrightarrow {CB} .$

b) $\overrightarrow {AB} – \overrightarrow {CD} = \overrightarrow {AC} – \overrightarrow {BD} .$

a)

Cách 1: Biến đổi vế trái (VT) ta có:

$VT = \overrightarrow {AB} + \overrightarrow {CD}$ $= (\overrightarrow {AD} + \overrightarrow {DB} ) + (\overrightarrow {CB} + \overrightarrow {BD} )$ $= \overrightarrow {AD} + \overrightarrow {CB} + \overrightarrow {DB} + \overrightarrow {BD}$ $= \overrightarrow {AD} + \overrightarrow {CB} + \vec 0$ $= \overrightarrow {AD} + \overrightarrow {CB} = VP.$

Nhận xét: Sử dụng cách giải này, ta cần chú ý khi biến đổi các số hạng của một vế cần quan tâm phân tích làm xuất hiện các số hạng có ở vế bên kia. Chẳng hạn số hạng ở vế trái là $\overrightarrow {AB}$ nhưng vế phải có chứa $\overrightarrow {AD}$ nên ta viết $\overrightarrow {AB} = \overrightarrow {AD} + \overrightarrow {DB} .$

Cách 2: Ta có: $\overrightarrow {AB} + \overrightarrow {CD} = \overrightarrow {AD} + \overrightarrow {CB}$ $(1)$ $\Leftrightarrow \overrightarrow {AB} – \overrightarrow {AD} = \overrightarrow {CB} – \overrightarrow {CD}$ $\Leftrightarrow \overrightarrow {DB} = \overrightarrow {DB}$ $(2).$

Ta có $(2)$ luôn đúng vậy $(1)$ được chứng minh.

Cách 3: Ta có: $\overrightarrow {AB} + \overrightarrow {BC} + \overrightarrow {CD} + \overrightarrow {DA} = \vec 0.$

Suy ra: $\overrightarrow {AB} + \overrightarrow {CD} = – \overrightarrow {DA} – \overrightarrow {BC} .$

Do đó: $\overrightarrow {AB} + \overrightarrow {CD} = \overrightarrow {AD} + \overrightarrow {CB} .$

b) Ta có: $VT = \overrightarrow {AB} – \overrightarrow {CD}$ $= (\overrightarrow {AC} + \overrightarrow {CB} ) – (\overrightarrow {CB} + \overrightarrow {BD} )$ $= \overrightarrow {AC} – \overrightarrow {BD} + \overrightarrow {CB} – \overrightarrow {CB}$ $= \overrightarrow {AC} – \overrightarrow {BD} = VP.$

Tương tự ta cũng có các cách chứng minh khác cho câu b.

<!-- chunk:2 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 2: Cho tam giác $ABC$ và $G$ là trọng tâm tam giác $ABC.$

a) Chứng minh rằng: $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = 3\overrightarrow {MG} .$

b) Tìm tập hợp điểm $M$ sao cho $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = 0.$

a) Ta có: $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC}$ $= (\overrightarrow {MG} + \overrightarrow {GA} ) + (\overrightarrow {MG} + \overrightarrow {GB} ) + (\overrightarrow {MG} + \overrightarrow {GC} )$ $= 3\overrightarrow {MG} + (\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $= 3\overrightarrow {MG} + \vec 0$ $= 3\overrightarrow {MG} .$

b) Vì $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \vec 0.$

$3\overrightarrow {MG} = \vec 0$ hay $\overrightarrow {MG} = \vec 0$ do đó $M \equiv G.$

Suy ra tập hợp $M$ thỏa mãn $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \vec O$ là $\{ G\} .$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 3: Cho tam giác $ABC$ có $D$, $E$, $F$ lần lượt là trung điểm của các cạnh $BC$, $CA$, $AB$. Chứng minh rằng:

a) $\overrightarrow {AD} + \overrightarrow {BE} + \overrightarrow {CF} = \vec 0.$

b) Với mọi điểm $M$ ta có $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \overrightarrow {MD} + \overrightarrow {ME} + \overrightarrow {MF} .$

<img link="data_for_rag/toan10/images/chung-minh-dang-thuc-vecto-1.png" alt="chung-minh-dang-thuc-vecto-1">

Vì $D$ là trung điểm của $BC$ nên $\overrightarrow {AB} + \overrightarrow {AC} = 2\overrightarrow {AD} .$

Suy ra $\overrightarrow {AD} = \frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} ).$

Tương tự $\overrightarrow {BE} = \frac{1}{2}(\overrightarrow {BA} + \overrightarrow {BC} )$, $\overrightarrow {CF} = \frac{1}{2}(\overrightarrow {CA} + \overrightarrow {CB} ).$

Do đó: $\overrightarrow {AD} + \overrightarrow {BE} + \overrightarrow {CF}$ $= \frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} + \overrightarrow {BA} + \overrightarrow {BC} + \overrightarrow {CA} + \overrightarrow {CB} )$ $= \frac{1}{2}\left[ {(\overrightarrow {AB} + \overrightarrow {BA} ) + (\overrightarrow {AC} + \overrightarrow {CA} ) + (\overrightarrow {BC} + \overrightarrow {CB} )} \right]$ $= \frac{1}{2}(\vec 0 + \vec 0 + \vec 0) = \vec 0.$

Cách khác: Gọi $G$ là trọng tâm tam giác $ABC$, khi đó ta có:

$\overrightarrow {AD} = – \frac{3}{2}\overrightarrow {GA}$, $\overrightarrow {BE} = – \frac{3}{2}\overrightarrow {GB}$, $\overrightarrow {CF} = – \frac{3}{2}\overrightarrow {GC} .$

Suy ra: $\overrightarrow {AD} + \overrightarrow {BE} + \overrightarrow {CF}$ $= – \frac{3}{2}(\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $= – \frac{3}{2}.\vec 0 = \vec 0.b.$

b) Với mọi điểm $M$ ta có:

$\overrightarrow {MA} + \overrightarrow {MB} = 2\overrightarrow {MF} .$

$\overrightarrow {MB} + \overrightarrow {MC} = 2\overrightarrow {MD} .$

$\overrightarrow {MC} + \overrightarrow {MA} = 2\overrightarrow {ME} .$

Suy ra $2(\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} )$ $= 2(\overrightarrow {MF} + \overrightarrow {MD} + \overrightarrow {ME} ).$

Vậy $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC}$ $= \overrightarrow {MD} + \overrightarrow {ME} + \overrightarrow {MF} .$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 4: Cho tam giác $ABC$ và $G$, $H$, $O$ lần lượt là trọng tâm, trực tâm, tâm đường tròn ngoại tiếp của tam giác. Gọi $D$ là điểm đối xứng của $A$ qua $O$. Chứng minh rằng:

a) $\overrightarrow {HB} + \overrightarrow {HC} = \overrightarrow {HD} .$

b) $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} = 2\overrightarrow {HO} .$

c) $\overrightarrow {HA} – \overrightarrow {HB} – \overrightarrow {HC} = 2\overrightarrow {OA} .$

d) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = \overrightarrow {OH} .$

e) $\overrightarrow {OH} = 3\overrightarrow {OG} .$

<img link="data_for_rag/toan10/images/chung-minh-dang-thuc-vecto-2.png" alt="chung-minh-dang-thuc-vecto-2">

a) Ta có: $\widehat {ABD} = \widehat {ACD} = 1v$ (góc nội tiếp chắn nữa đường tròn).

Suy ra $BD \bot AB.$

Mặc khác $CH \bot AB$ (vì $H$ là trực tâm).

Do vậy $BD//CH.$

Tương tự ta có $CD//BH.$

Từ đó suy ra $HBDC$ là hình bình hành.

Do đó $\overrightarrow {HB} + \overrightarrow {HC} = \overrightarrow {HD} .$

b) $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC}$ $= \overrightarrow {HA} + (\overrightarrow {HB} + \overrightarrow {HC} )$ $= \overrightarrow {HA} + \overrightarrow {HD} = 2\overrightarrow {HO} .$

c) $\overrightarrow {HA} – \overrightarrow {HB} – \overrightarrow {HC}$ $= \overrightarrow {HA} – (\overrightarrow {HB} + \overrightarrow {HC} )$ $= \overrightarrow {HA} – \overrightarrow {HD}$ $= \overrightarrow {DA} = 2\overrightarrow {OA} .$

d) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC}$ $= (\overrightarrow {OH} + \overrightarrow {HA} ) + (\overrightarrow {OH} + \overrightarrow {HB} ) + (\overrightarrow {OH} + \overrightarrow {HC} )$ $= 3\overrightarrow {OH} + (\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} )$ $= 3\overrightarrow {OH} + 2\overrightarrow {HO}$ $= 3\overrightarrow {OH} – 2\overrightarrow {OH} = \overrightarrow {OH} .$

e) $\overrightarrow {OH} = \overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = 3\overrightarrow {OG} .$

[ads]

<!-- chunk:5 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 5: Cho tứ giác $ABCD.$ Gọi $E$, $F$ lần lượt là trung điểm của $AB$, $CD$, $O$  là trung điểm của $EF.$ Chứng minh rằng:

a) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \overrightarrow 0 .$

b) $\overrightarrow {MA} + \overrightarrow {MB} + \mathop {\overrightarrow {MC} }\limits^. + \overrightarrow {MD} = 4\overrightarrow {MO} .$

a) Ta có $VT = (\overrightarrow {OA} + \overrightarrow {OB} ) + (\overrightarrow {OC} + \overrightarrow {OD} )$ $= 2\overrightarrow {OE} + 2\overrightarrow {OF}$ $= 2(\overrightarrow {OE} + \overrightarrow {OF} )$ $= \overrightarrow 0 = VP.$

b) Ta có: $VT = (\overrightarrow {MO} + \overrightarrow {OA} ) + (\overrightarrow {MO} + \overrightarrow {OB} )$ $+ (\overrightarrow {MO} + \overrightarrow {OC} ) + (\overrightarrow {MO} + \overrightarrow {OD} )$ $= 4\overrightarrow {MO} + (\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} )$ $= 4\overrightarrow {MO} + \overrightarrow 0$ $= 4\overrightarrow {MO} = VP.$

<!-- chunk:6 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 6: Cho tam giác $ABC$ và tam giác ${A_1}{B_1}{C_1}.$ Gọi $G$, $G_1$ lần lượt là trọng tâm tam giác $ABC$ và tam giác ${A_1}{B_1}{C_1}.$ Chứng minh rằng: $\overrightarrow {A{A_1}} + \overrightarrow {B{B_1}} + \overrightarrow {C{C_1}} = 3\widehat {G{G_1}}.$

Ta có $VT = \left( {\overrightarrow {AG} + \overrightarrow {G{G_1}} + \overrightarrow {{G_1}{A_1}} } \right)$ $+ \left( {\overrightarrow {BG} + \overrightarrow {G{G_1}} + \overrightarrow {{G_1}{B_1}} } \right)$ $+ \left( {\overrightarrow {CG} + \overrightarrow {G{G_1}} + \overrightarrow {{G_1}{C_1}} } \right)$ $= 3\overrightarrow {G{G_1}} + (A\overrightarrow G + \overrightarrow {BG} + \overrightarrow {CG} )$ $+ \left( {\overrightarrow {{G_1}{A_1}} + \overrightarrow {{G_1}{B_1}} + \overrightarrow {{G_1}{C_1}} } \right)$ $= 3\overrightarrow {G{G_1}} + \overrightarrow 0 + \overrightarrow 0$ $= 3\overrightarrow {G{G_1}} = VP.$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 7: Cho tam giác $ABC.$ Gọi $M$ là trung điểm của $AB$ và $N$ là điểm trên cạnh $AC$ sao cho $NC = 2NA.$ Gọi $K$ là trung điểm của $MN.$

a) Chứng minh rằng: $\overrightarrow {AK} = \frac{1}{4}\overrightarrow {AB} + \frac{1}{6}\overrightarrow {AC} .$

b) Gọi $D$ là trung điểm của $BC.$ Chứng minh rằng: $\overrightarrow {KD} = \frac{1}{4}\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} .$

<img link="data_for_rag/toan10/images/chung-minh-dang-thuc-vecto-3.png" alt="chung-minh-dang-thuc-vecto-3">

a) Ta có: $\overrightarrow {AK} = \frac{1}{2}(\overrightarrow {AM} + \overrightarrow {AN} )$ (vì $K$ là trung điểm của $MN$) $= \frac{1}{2}\left( {\frac{1}{2}\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} } \right)$ $= \frac{1}{4}\overrightarrow {AB} + \frac{1}{6}\overrightarrow {AC} .$

b) Ta có: $\overrightarrow {KD} = \frac{1}{2}(\overrightarrow {KB} + \overrightarrow {KC} )$ $= \frac{1}{2}(\overrightarrow {KA} + \overrightarrow {AB} + \overrightarrow {KA} + \overrightarrow {AC} )$ $= \overrightarrow {KA} + \frac{1}{2}\overrightarrow {AB} + \frac{1}{2}\overrightarrow {AC}$ $= – \overrightarrow {AK} + \frac{1}{2}\overrightarrow {AB} + \frac{1}{2}\overrightarrow {AC}$ $= – \frac{1}{4}\overrightarrow {AB} – \frac{1}{6}\overrightarrow {AC} + \frac{1}{2}\overrightarrow {AB} + \frac{1}{2}\overrightarrow {AC}$ $= \frac{1}{4}\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} .$

<!-- chunk:8 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 8: Cho hai điểm $A$ và $B$, $M$ là điểm trên đường thẳng $AB$ sao cho $n\overrightarrow {AM} = m\overrightarrow {MB}$. Chứng minh rằng với điểm $O$ bất kì, ta có: $\overrightarrow {OM} = \frac{n}{{m + n}}\overrightarrow {OA} + \frac{m}{{m + n}}\overrightarrow {OB} .$

Ta có $n\overrightarrow {AM} = m\overrightarrow {MB} .$

Suy ra $n(\overrightarrow {OM} – \overrightarrow {OA} ) = m(\overrightarrow {OB} – \overrightarrow {OM} ).$

Do đó $(m + n)\overrightarrow {OM} = n\overrightarrow {OA} + m\overrightarrow {OB} .$

Như vậy $\overrightarrow {OM} = \frac{n}{{m + n}}\overrightarrow {OA} + \frac{m}{{m + n}}\overrightarrow {OB} .$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/02/chung-minh-dang-thuc-vecto.html -->
## Bài toán 9: Cho tam giác $ABC.$ Trên cạnh $AB$, $AC$ lấy các điểm $M$, $N$ sao cho $\frac{{MA}}{{MB}} = a$, $\frac{{NA}}{{NC}} = b.$ Hai đường thẳng $CM$ và $BN$ cắt nhau tại $I.$ Chứng minh rằng $\overrightarrow {AI} = a\overrightarrow {IB} + b\overrightarrow {IC} .$

<img link="data_for_rag/toan10/images/chung-minh-dang-thuc-vecto-4.png" alt="chung-minh-dang-thuc-vecto-4">

Dựng $Ax$ song song $BN$ cắt $CM$ tại $E.$

Dựng $Ay$ song song $CM$ cắt $BN$ tại $F.$

Khi đó ta có $\overrightarrow {AI} = \overrightarrow {AE} + \overrightarrow {AF} .$

Mặc khác $\Delta MAE$ đồng dạng $\Delta MBI.$

Nên $\frac{{AE}}{{IB}} = \frac{{MA}}{{MB}} = a.$

Suy ra $\overrightarrow {AE} = a\overrightarrow {IB} .$

Tương tự $\Delta NAF$ đồng dạng $\Delta NCI$ nên $\overrightarrow {AF} = b\overrightarrow {CI} .$

Từ đó suy ra $\overrightarrow {AI} = a\overrightarrow {IB} + b\overrightarrow {IC} .$