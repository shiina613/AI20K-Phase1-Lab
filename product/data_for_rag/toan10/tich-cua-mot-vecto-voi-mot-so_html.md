# Tích của một vectơ với một số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
Bài viết trình bày các kiến thức cần nắm vững và hướng dẫn phương pháp giải một số dạng toán về chủ đề tích của một vectơ với một số trong chương trình Hình học 10.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## A. TÓM TẮT LÝ THUYẾT

1. Định nghĩa: Tích của vectơ $\overrightarrow a$ với số thực $k \ne 0$ là một vectơ, kí hiệu là $k\overrightarrow a$, cùng hướng với $\overrightarrow a$ nếu $k>0$, ngược hướng với $\overrightarrow a$ nếu $k<0$ và có độ dài bằng $\left| k \right|\left| {\overrightarrow a } \right|.$

Quy ước: $0\overrightarrow a = \vec 0$ và $k\vec 0 = \vec 0.$

2. Tính chất

i) $(k + m)\overrightarrow a = k\overrightarrow a + m\overrightarrow a .$

ii) $k(\vec a \pm \vec b) = k\vec a \pm k\vec b.$

iii) $k(m\overrightarrow a ) = (km)\overrightarrow a .$

iv) 
$$
k\overrightarrow a = \vec 0 \Leftrightarrow \left[ {\begin{array}{l}
{k = 0}\\
{\overrightarrow a = \vec 0}
\end{array}} \right..
$$

v) $1\overrightarrow a = \overrightarrow a$, $( – 1)\overrightarrow a = – \overrightarrow a .$

3. Điều kiện để hai vectơ cùng phương
$\overrightarrow b$ cùng phương $\vec a$ $(\vec a \ne \vec 0)$ khi và chỉ khi có số $k$ thỏa $\overrightarrow b = k\overrightarrow a .$

Điều kiện cần và đủ để $A$, $B$, $C$ thẳng hàng là có số $k$ sao cho $\overrightarrow {AB} = k\overrightarrow {AC} .$

4. Phân tích một vectơ theo hai vectơ không cùng phương

Cho $\overrightarrow a$ không cùng phương $\overrightarrow b .$ Với mọi vectơ $\vec x$ luôn được biểu diễn $\overrightarrow x = m\overrightarrow a + n\overrightarrow b$ với $m$, $n$ là các số thực duy nhất.

## B. CÁC DẠNG TOÁN VÀ PHƯƠNG PHÁP GIẢI

**DẠNG TOÁN 1: DỰNG VÀ TÍNH ĐỘ DÀI VECTƠ CHỨA TÍCH MỘT VECTƠ VỚI MỘT SỐ.**

**1. PHƯƠNG PHÁP GIẢI**

Sử dụng định nghĩa tích của một vectơ với một số và các quy tắc về phép toán vectơ để dựng vectơ chứa tích một vectơ với một số, kết hợp với các định lí pitago và hệ thức lượng trong tam giác vuông để tính độ dài của chúng.

2. CÁC VÍ DỤ

<!-- chunk:2 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho tam giác đều $ABC$ cạnh $a$, điểm $M$ là trung điểm $BC.$ Dựng các vectơ sau và tính độ dài của chúng.

a) $\frac{1}{2}\overrightarrow {CB} + \overrightarrow {MA} .$

b) $\overrightarrow {BA} – \frac{1}{2}\overrightarrow {BC} .$

c) $\frac{1}{2}\overrightarrow {AB} + 2\overrightarrow {AC} .$

d) $\frac{3}{4}\overrightarrow {MA} – 2,5\overrightarrow {MB} .$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-1.png" alt="">

a) Do $\frac{1}{2}\overrightarrow {CB} = \overrightarrow {CM}$ suy ra theo quy tắc ba điểm, ta có:

$\frac{1}{2}\overrightarrow {CB} + \overrightarrow {MA} = \overrightarrow {CM} + \overrightarrow {MA} = \overrightarrow {CA} .$

Vậy $\left| {\frac{1}{2}\overrightarrow {CB} + \overrightarrow {MA} } \right| = CA = a.$

b) Vì $\frac{1}{2}\overrightarrow {BC} = \overrightarrow {BM}$ nên theo quy tắc trừ ta có: $\overrightarrow {BA} – \frac{1}{2}\overrightarrow {BC} = \overrightarrow {BA} – \overrightarrow {BM} = \overrightarrow {MA} .$

Theo định lí Pitago ta có:

$MA = \sqrt {A{B^2} – B{M^2}}$ $= \sqrt {{a^2} – {{\left( {\frac{a}{2}} \right)}^2}} = \frac{{a\sqrt 3 }}{2}.$

Vậy $\left| {\overrightarrow {BA} – \frac{1}{2}\overrightarrow {BC} } \right| = MA = \frac{{a\sqrt 3 }}{2}.$

c) Gọi $N$ là trung điểm $AB$, $Q$ là điểm đối xứng của $A$ qua $C$ và $P$ là đỉnh của hình bình hành $AQPN.$

Khi đó ta có: $\frac{1}{2}\overrightarrow {AB} = \overrightarrow {AN}$, $2\overrightarrow {AC} = \overrightarrow {AQ}$ suy ra theo quy tắc hình bình hành ta có: $\frac{1}{2}\overrightarrow {AB} + 2\overrightarrow {AC} = \overrightarrow {AN} + \overrightarrow {AQ} = \overrightarrow {AP} .$

Gọi $L$ là hình chiếu của $A$ lên $PN.$

Vì $MN//AC$ $\Rightarrow \widehat {ANL} = \widehat {MNB} = \widehat {CAB} = {60^0}.$

Xét tam giác vuông $ANL$ ta có:

$\sin \widehat {ANL} = \frac{{AL}}{{AN}}$ $\Rightarrow AL = AN\sin \widehat {ANL}$ $= \frac{a}{2}\sin {60^0} = \frac{{a\sqrt 3 }}{4}.$

$\cos \widehat {ANL} = \frac{{NL}}{{AN}}$ $\Rightarrow NL = AN\cos \widehat {ANL}$ $= \frac{a}{2}\cos {60^0} = \frac{a}{4}.$

Ta lại có $AQ = PN$ $\Rightarrow PL = PN + NL$ $= AQ + NL$ $= 2a + \frac{a}{4} = \frac{{9a}}{4}.$

Áp dụng định lí Pitago trong tam giác $ALP$ ta có:

$A{P^2} = A{L^2} + P{L^2}$ $= \frac{{3{a^2}}}{{16}} + \frac{{81{a^2}}}{{16}} = \frac{{21{a^2}}}{4}$ $\Rightarrow AP = \frac{{a\sqrt {21} }}{2}.$

Vậy $\left| {\frac{1}{2}\overrightarrow {AB} + 2\overrightarrow {AC} } \right| = AP = \frac{{a\sqrt {21} }}{2}.$

d) Gọi $K$ là điểm nằm trên đoạn $AM$ sao cho $MK = \frac{3}{4}MA$, $H$ thuộc tia $MB$ sao cho $MH = 2,5MB.$

Khi đó $\frac{3}{4}\overrightarrow {MA} = \overrightarrow {MK}$, $2,5\overrightarrow {MB} = \overrightarrow {MH} .$

Do đó: $\frac{3}{4}\overrightarrow {MA} – 2,5\overrightarrow {MB}$ $= \overrightarrow {MK} – \overrightarrow {MH} = \overrightarrow {HK} .$

Ta có $MK = \frac{3}{4}AM$ $= \frac{3}{4}.\frac{{a\sqrt 3 }}{2} = \frac{{3\sqrt 3 a}}{8}$, $MH = 2,5MB$ $= 2,5.\frac{a}{2} = \frac{{5a}}{4}.$

Áp dụng định lí Pitago cho tam giác vuông $KMH$ ta có:

$KH = \sqrt {M{H^2} + M{K^2}}$ $= \sqrt {\frac{{25{a^2}}}{{16}} + \frac{{27{a^2}}}{{64}}}$ $= \frac{{a\sqrt {127} }}{8}.$

Vậy $\left| {\frac{3}{4}\overrightarrow {MA} – 2,5\overrightarrow {MB} } \right| = KH = \frac{{a\sqrt {127} }}{8}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho hình vuông $ABCD$ cạnh $a.$

a) Chứng minh rằng $\overrightarrow u = 4\overrightarrow {MA} – 3\overrightarrow {MB} + \overrightarrow {MC} – 2\overrightarrow {MD}$ không phụ thuộc vào vị trí điểm $M.$

b) Tính độ dài vectơ $\overrightarrow u .$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-2.png" alt="">

a) Gọi $O$ là tâm hình vuông.

Theo quy tắc ba điểm ta có:

$\overrightarrow u = 4(\overrightarrow {MO} + \overrightarrow {OA} ) – 3(\overrightarrow {MO} + \overrightarrow {OB} )$ $+ (\overrightarrow {MO} + \overrightarrow {OC} ) – 2(\overrightarrow {MO} + \overrightarrow {OD} )$ $= 4\overrightarrow {OA} – 3\overrightarrow {OB} + \overrightarrow {OC} – 2\overrightarrow {OD} .$

Mà $\overrightarrow {OD} = – \overrightarrow {OB}$, $\overrightarrow {OC} = – \overrightarrow {OA}$ nên $\overrightarrow u = 3\overrightarrow {OA} – \overrightarrow {OB} .$

Suy ra $\overrightarrow u$ không phụ thuộc vào vị trí điểm $M.$

b) Lấy điểm $A’$ trên tia $OA$ sao cho $OA’ = 3OA$, khi đó $\overrightarrow {OA’} = 3\overrightarrow {OA}$, do đó $\overrightarrow u = \overrightarrow {OA’} – \overrightarrow {OB} = \overrightarrow {BA’} .$

Mặt khác $BA’ = \sqrt {O{B^2} + OA{‘^2}}$ $= \sqrt {O{B^2} + 9O{A^2}} = a\sqrt 5 .$

Suy ra $|\overrightarrow u | = a\sqrt 5 .$

## Bài tập
## Bài 1: Cho tam giác đều $ABC$ cạnh $a.$ Gọi điểm $M$, $N$ lần lượt là trung điểm $BC$, $CA.$ Dựng các vectơ sau và tính độ dài của chúng.

a) $\overrightarrow {AN} + \frac{1}{2}\overrightarrow {CB} .$

b) $\frac{1}{2}\overrightarrow {BC} – 2\overrightarrow {MN} .$

c) $\overrightarrow {AB} + 2\overrightarrow {AC} .$

d) $0,25\overrightarrow {MA} – \frac{3}{2}\overrightarrow {MB} .$

## Bài 2: Cho hình vuông $ABCD$ cạnh $a.$

a) Chứng minh rằng $\overrightarrow u = \overrightarrow {MA} – 2\overrightarrow {MB} + 3\overrightarrow {MC} – 2\overrightarrow {MD}$ không phụ thuộc vào vị trí điểm $M.$

b) Tính độ dài vectơ $\overrightarrow u .$

DẠNG TOÁN 2: CHỨNG MINH ĐẲNG THỨC VECTƠ.

1. PHƯƠNG PHÁP GIẢI

Sử dụng các kiến thức sau để biến đổi vế này thành vế kia hoặc cả hai biểu thức ở hai vế cùng bằng biểu thức thứ ba hoặc biến đổi tương đương về đẳng thức đúng:

+ Các tính chất phép toán vectơ.

+ Các quy tắc: quy tắc ba điểm, quy tắc hình bình hành và quy tắc phép trừ.

+ Tính chất trung điểm:

$M$ là trung điểm đoạn thẳng $AB$ $\Leftrightarrow \overrightarrow {MA} + \overrightarrow {MB} = \vec 0.$

$M$ là trung điểm đoạn thẳng $AB$ $\Leftrightarrow \overrightarrow {OA} + \overrightarrow {OB} = 2\overrightarrow {OM}$ (với $O$ là điểm tuỳ ý).

+ Tính chất trọng tâm:

$G$ là trọng tâm của tam giác $ABC$ $\Leftrightarrow \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \overrightarrow 0 .$

$G$ là trọng tâm của tam giác $ABC$ $\Leftrightarrow \overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = 3\overrightarrow {OG}$ (với $O$ là điểm tuỳ ý).

2. CÁC VÍ DỤ

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho tứ giác $ABCD.$ Gọi $I$, $J$ lần lượt là trung điểm của $AB$ và $CD$, $O$ là trung điểm của $IJ.$ Chứng minh rằng:

a) $\overrightarrow {AC} + \overrightarrow {BD} = 2\overrightarrow {IJ} .$

b) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \vec 0.$

c) $\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} + \overrightarrow {MD} = 4\overrightarrow {MO}$ với $M$ là điểm bất kì.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-3.png" alt="">

a) Theo quy tắc ba điểm ta có:

$\overrightarrow {AC} = \overrightarrow {AI} + \overrightarrow {IJ} + \overrightarrow {JC} .$

Tương tự $\overrightarrow {BD} = \overrightarrow {BI} + \overrightarrow {IJ} + \overrightarrow {JD} .$

Mà $I$, $J$ lần lượt là trung điểm của $AB$ và $CD$ nên $\overrightarrow {AI} + \overrightarrow {BI} = \vec 0$, $\overrightarrow {JC} + \overrightarrow {JD} = \vec 0.$

Vậy $\overrightarrow {AC} + \overrightarrow {BD}$ $= (\overrightarrow {AI} + \overrightarrow {BI} ) + (\overrightarrow {JC} + \overrightarrow {JD} ) + 2\overrightarrow {IJ}$ $= 2\overrightarrow {IJ} .$

b) Theo hệ thức trung điểm ta có: $\overrightarrow {OA} + \overrightarrow {OB} = 2\overrightarrow {OI}$, $\overrightarrow {OC} + \overrightarrow {OD} = 2\overrightarrow {OJ} .$

Mặt khác $O$ là trung điểm $IJ$ nên $\overrightarrow {OI} + \overrightarrow {OJ} = \vec 0.$

Suy ra $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD}$ $= 2(\overrightarrow {OI} + \overrightarrow {OJ} ) = \vec 0.$

c) Theo câu $b$ ta có $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \vec 0$ do đó với mọi điểm $M$ thì $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \vec 0.$

$\Leftrightarrow (\overrightarrow {OM} + \overrightarrow {MA} ) + (\overrightarrow {OM} + \overrightarrow {MB} )$ $+ (\overrightarrow {OM} + \overrightarrow {MC} ) + (\overrightarrow {OM} + \overrightarrow {MD} ) = \vec 0.$

$\Leftrightarrow \overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} + \overrightarrow {MD} = 4\overrightarrow {MO} .$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho hai tam giác $ABC$ và ${A_1}{B_1}{C_1}$ có cùng trọng tâm $G.$ Gọi ${G_1}$, ${G_2}$, ${G_3}$ lần lượt là trọng tâm tam giác $BC{A_1}$, $AB{C_1}$, $AC{B_1}.$ Chứng minh rằng $\overrightarrow {G{G_1}} + \overrightarrow {G{G_2}} + \overrightarrow {G{G_3}} = \overrightarrow 0 .$

Vì ${G_1}$ là trọng tâm tam giác $BC{A_1}$ nên $3\overrightarrow {G{G_1}} = \overrightarrow {GB} + \overrightarrow {GC} + \overrightarrow {G{A_1}} .$

Tương tự ${G_2}$, ${G_3}$ lần lượt là trọng tâm tam giác $AB{C_1}$, $AC{B_1}$ suy ra:

$3\overrightarrow {G{G_2}} = \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {G{C_1}}$ và $3\overrightarrow {G{G_3}} = \overrightarrow {GA} + \overrightarrow {GC} + \overrightarrow {G{B_1}} .$

Cộng theo vế với vế các đẳng thức trên ta có:

$3\left( {\overrightarrow {G{G_1}} + \overrightarrow {G{G_2}} + \overrightarrow {G{G_3}} } \right)$ $= 2(\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} ) + (\overrightarrow {G{A_1}} + \overrightarrow {G{B_1}} + \overrightarrow {G{C_1}} ).$

Mặt khác hai tam giác $ABC$ và ${A_1}{B_1}{C_1}$ có cùng trọng tâm $G$ nên:

$\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ và $\overrightarrow {G{A_1}} + \overrightarrow {G{B_1}} + \overrightarrow {G{C_1}} = \vec 0.$

Suy ra $\overrightarrow {G{G_1}} + \overrightarrow {G{G_2}} + \overrightarrow {G{G_3}} = \vec 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho tam giác $ABC$ có trực tâm $H$, trọng tâm $G$ và tâm đường tròn ngoại tiếp $O.$ Chứng minh rằng:

a) $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} = 2\overrightarrow {HO} .$

b) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = \overrightarrow {OH} .$

c) $\overrightarrow {GH} + 2\overrightarrow {GO} = \vec 0.$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-4.png" alt="">

a) Dễ thấy $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} = 2\overrightarrow {HO}$ nếu tam giác $ABC$ vuông.

Nếu tam giác $ABC$ không vuông, gọi $D$ là điểm đối xứng của $A$ qua $O$ khi đó $BH //DC$ (vì cùng vuông góc với $AC$) và $BD // CH$ (vì cùng vuông góc với $AB$).

Suy ra $BDCH$ là hình bình hành.

Do đó theo quy tắc hình bình hành thì: $\overrightarrow {HB} + \overrightarrow {HC} = \overrightarrow {HD}$ $(1).$

Mặt khác vì $O$ là trung điểm của $AD$ nên $\overrightarrow {HA} + \overrightarrow {HD} = 2\overrightarrow {HO}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} = 2\overrightarrow {HO} .$

b) Theo câu a ta có:

$\overrightarrow {HA} + \overrightarrow {HB} + \overrightarrow {HC} = 2\overrightarrow {HO} .$

$\Leftrightarrow (\overrightarrow {HO} + \overrightarrow {OA} ) + (\overrightarrow {HO} + \overrightarrow {OB} )$ $+ (\overrightarrow {HO} + \overrightarrow {OC} ) = 2\overrightarrow {HO} .$

$\Leftrightarrow \overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = \overrightarrow {OH} .$

c) Vì $G$ là trọng tâm tam giác $ABC$ nên $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = 3\overrightarrow {OG} .$

Mặt khác theo câu b ta có: $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = \overrightarrow {OH} .$

Suy ra $\overrightarrow {OH} = 3\overrightarrow {OG}$ $\Leftrightarrow (\overrightarrow {OG} + \overrightarrow {GH} ) – 3\overrightarrow {OG} = \vec 0$ $\Leftrightarrow \overrightarrow {GH} + 2\overrightarrow {GO} = \vec 0.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 4: Cho tam giác $ABC$ với $AB = c$, $BC = a$, $CA = b$ và có trọng tâm $G.$ Gọi $D$, $E$, $F$ lần lượt là hình chiếu $G$ lên cạnh $BC$, $CA$, $AB.$ Chứng minh rằng: ${a^2}\overrightarrow {GD} + {b^2}\overrightarrow {GE} + {c^2}\overrightarrow {GF} = \overrightarrow 0 .$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-5.png" alt="">

Trên tia $GD$, $GE$, $MF$ lần lượt lấy các điểm $N$, $P$, $Q$ sao cho $GN=a$, $GP = b$, $GQ=c$ và dựng hình bình hành $GPRN.$

Ta có: ${a^2}\overrightarrow {GD} + {b^2}\overrightarrow {GE} + {c^2}\overrightarrow {GF} = \overrightarrow 0 .$

$\Leftrightarrow a.GD.\overrightarrow {GN} + b.GE.\overrightarrow {GP} + c.GF.\overrightarrow {GQ} = \vec 0$ $(*).$

Ta có: $a.GD = 2{S_{\Delta GBC}}$, $b.GE = 2{S_{\Delta GCA}}$, $c.GF = 2{S_{\Delta GAB}}.$

Mặt khác $G$ là trọng tâm tam giác $ABC$ nên ${S_{\Delta GBC}} = {S_{\Delta GCA}} = {S_{\Delta GAB}}.$

Suy ra $a.GD = b.GE = c.GF.$

Vậy $(*) \Leftrightarrow \overrightarrow {GN} + \overrightarrow {GP} + \overrightarrow {GQ} = \overrightarrow 0 .$

Ta có $AC = GP = b$, $PR = BC = a$ và $\widehat {ACB} = \widehat {GPR}$ (góc có cặp cạnh vuông góc với nhau).

Suy ra $\Delta ACB = \Delta GPR$ (c.g.c).

$\Rightarrow GR = AB = c$ và $\widehat {PGR} = \widehat {BAC}.$

Ta có $\widehat {QGP} + \widehat {BAC} = {180^0}$ $\Rightarrow \widehat {QGP} + \widehat {GPR} = {180^0}.$

$\Rightarrow Q$, $G$, $R$ thẳng hàng, do đó $G$ là trung điểm của $QR.$

Theo quy tắc hình bình hành và hệ thức trung điểm ta có:

$\overrightarrow {GN} + \overrightarrow {GP} + \overrightarrow {GQ} = \overrightarrow {GR} + \overrightarrow {GQ} = \overrightarrow 0 .$

Vậy ${a^2}\overrightarrow {GD} + {b^2}\overrightarrow {GE} + {c^2}\overrightarrow {GF} = \overrightarrow 0 .$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 5: Cho tam giác $ABC$ với các cạnh $AB = c$, $BC = a$, $CA = b.$ Gọi $I$ là tâm đường tròn nội tiếp tam giác $ABC.$ Chứng minh rằng $a\overrightarrow {IA} + b\overrightarrow {IB} + c\overrightarrow {IC} = \vec 0.$

Cách 1:

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-6.png" alt="">

Gọi $D$ là chân đường phân giác góc $A.$

Do $D$ là chân đường phân giác giác trong góc $A$ nên ta có:

$\frac{{DB}}{{DC}} = \frac{c}{b}$ $\Rightarrow \overrightarrow {BD} = \frac{c}{b}\overrightarrow {DC} .$

$\Leftrightarrow \overrightarrow {ID} – \overrightarrow {IB} = \frac{c}{b}(\overrightarrow {IC} – \overrightarrow {ID} )$ $\Leftrightarrow (b + c)\overrightarrow {ID} = b\overrightarrow {IB} + c\overrightarrow {IC}$ $(1).$

Do $I$ là chân đường phân giác nên ta có:

$\frac{{ID}}{{IA}} = \frac{{BD}}{{BA}} = \frac{{CD}}{{CA}}$ $= \frac{{BD + CD}}{{BA + CA}} = \frac{a}{{b + c}}.$

$\Rightarrow (b + c)\overrightarrow {ID} = – a\overrightarrow {IA}$ $(2).$

Từ $(1)$ và $(2)$ ta có điều phải chứng minh.

Cách 2:

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-7.png" alt="">

Qua $C$ dựng đường thẳng song song với $AI$ cắt $BI$ tại $B’$, song song với $BI$ cắt $AI$ tại $A’.$

Ta có $\overrightarrow {IC} = \overrightarrow {IA’} + \overrightarrow {IB’}$ $(*).$

Theo định lý Talet và tính chất đường phân giác trong ta có:

$\frac{{IB}}{{IB’}} = \frac{{B{A_1}}}{{C{A_1}}} = \frac{c}{b}$ $\Rightarrow \overrightarrow {IB’} = – \frac{b}{c}\overrightarrow {IB}$ $(1).$

Tương tự: $\overrightarrow {IA’} = – \frac{a}{c}\overrightarrow {IA}$ $(2).$

Từ $(1)$ và $(2)$ thay vào $(*)$ ta có: $\overrightarrow {IC} = – \frac{a}{c}\overrightarrow {IA} – \frac{b}{c}\overrightarrow {IB}$ $\Leftrightarrow a\overrightarrow {IA} + b\overrightarrow {IB} + c\overrightarrow {IC} = \vec 0.$

## Bài tập

## Bài 1: Cho tam giác $ABC.$ Gọi $M$, $N$, $P$ lần lượt là trung điểm của $BC$, $CA$, $AB.$ Chứng minh rằng:

a) $\overrightarrow {AM} + \overrightarrow {BN} + \overrightarrow {CP} = \vec 0.$

b) $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} = \overrightarrow {OM} + \overrightarrow {ON} + \overrightarrow {OP}$ với $O$ là điểm bất kỳ.

## Bài 2: Cho tam giác $ABC.$ Gọi $H$ là điểm đối xứng với $B$ qua $G$ với $G$ là trọng tâm tam giác. Chứng minh rằng:

a) $\overrightarrow {AH} = \frac{2}{3}\overrightarrow {AC} – \frac{1}{3}\overrightarrow {AB}$, $\overrightarrow {CH} = – \frac{1}{3}\overrightarrow {AB} – \frac{1}{3}\overrightarrow {AC} .$

b) $\overrightarrow {MH} = \frac{1}{6}\overrightarrow {AC} – \frac{5}{6}\overrightarrow {AB}$ với $M$ là trung điểm của $BC.$

## Bài 3: Cho tam giác $ABC$ có điểm $M$ thuộc cạnh $BC.$ Chứng minh rằng $\overrightarrow {AM} = \frac{{MC}}{{BC}}\overrightarrow {AB} + \frac{{MB}}{{BC}}\overrightarrow {AC} .$

## Bài 4: Cho hai hình bình hành $ABCD$ và $AB’C’D’$ có chung đỉnh $A.$ Chứng minh rằng $\overrightarrow {B’B} + \overrightarrow {CC’} + \overrightarrow {D’D} = \vec 0.$

## Bài 5: Cho $n$ vectơ đôi một khác phương và tổng của $n-1$ vectơ bất kì trong $n$ vectơ trên cùng phương với vectơ còn lại. Chứng minh rằng tổng $n$ vectơ cho ở trên bằng vectơ $\vec 0.$

## Bài 6: Cho tam giác $ABC$ với các cạnh $AB = c$, $BC = a$, $CA = b.$ Gọi $I$ là tâm và $D$, $E$, $F$ lần lượt là tiếp điểm của cạnh $BC$, $CA$, $AB$ của đường tròn nội tiếp tam giác $ABC.$ $M$, $N$, $P$ lần lượt là trung điểm của $BC$, $CA$, $AB.$ Chứng minh rằng:

a) $\left( {\cot \frac{B}{2} + \cot \frac{C}{2}} \right)\overrightarrow {IA}$ $+ \left( {\cot \frac{C}{2} + \cot \frac{A}{2}} \right)\overrightarrow {IB}$ $+ \left( {\cot \frac{A}{2} + \cot \frac{B}{2}} \right)\overrightarrow {IC} = \vec 0.$

b) $\cot \frac{A}{2}\overrightarrow {IM} + \cot \frac{B}{2}\overrightarrow {IN} + \cot \frac{C}{2}\overrightarrow {IP} = \vec 0.$

c) $(b + c – a)\overrightarrow {IM} + (a + c – b)\overrightarrow {IN}$ $+ (a + b – c)\overrightarrow {IP} = \overrightarrow 0 .$

d) $a\overrightarrow {AD} + b\overrightarrow {BE} + c\overrightarrow {CF} = \vec 0.$

## Bài 7: Cho tam giác $ABC.$ $M$ là điểm bất kỳ nằm trong tam giác. Chứng minh rằng: ${S_{MBC}}\overrightarrow {MA} + {S_{MCA}}\overrightarrow {MB} + {S_{MAB}}\overrightarrow {MC} = \overrightarrow 0 .$

## Bài 8: Cho đa giác lồi ${A_1}{A_2} \ldots {A_n}$ $(n \ge 3)$, $\overrightarrow {{e_i}}$ với $1 \le i \le n$ là vectơ đơn vị vuông góc với $\overrightarrow {{A_i}{A_{i + 1}}}$ (xem ${A_{n + 1}} \equiv {A_1}$) và hướng ra phía ngoài đa giác. Chứng minh rằng: ${A_1}{A_2}\overrightarrow {{e_1}} + {A_2}{A_3}\overrightarrow {{e_2}} + \ldots + {A_n}{A_1}\overrightarrow {{e_n}} = \overrightarrow 0$ (định lý con nhím).

## Bài 9: Cho đa giác lồi ${A_1}{A_2} \ldots {A_n}$ $(n \ge 3)$ với $I$ là tâm đường tròn tiếp xúc các cạnh của đa giác, gọi $\overrightarrow {{e_i}}$, $1 \le i \le n$ là véctơ đơn vị cùng hướng với véctơ $\overrightarrow {I{A_i}} .$ Chứng minh rằng $\cos \frac{{{A_1}}}{2}\overrightarrow {{e_1}} + \cos \frac{{{A_2}}}{2}\overrightarrow {{e_2}} + \ldots + \cos \frac{{{A_n}}}{2}\overrightarrow {{e_n}} = \overrightarrow 0 .$

## Bài 10: Cho tam giác $ABC$ vuông tại $A.$ $I$ là trung điểm của đường cao $AH.$ Chứng minh rằng: ${a^2}\overrightarrow {IA} + {b^2}\overrightarrow {IB} + {c^2}\overrightarrow {IC} = \overrightarrow 0 .$

DẠNG TOÁN 3: XÁC ĐỊNH ĐIỂM $M$ THỎA MÃN MỘT ĐẲNG THỨC VECTƠ CHO TRƯỚC.

1. PHƯƠNG PHÁP GIẢI

Ta biến đổi đẳng thức vectơ về dạng $\overrightarrow {AM} = \overrightarrow a$ trong đó điểm $A$ và $\overrightarrow a$ đã biết. Khi đó tồn tại duy nhất điểm $M$ sao cho $\overrightarrow {AM} = \overrightarrow a$, để dựng điểm $M$ ta lấy $A$ làm gốc dựng một vectơ bằng vectơ $\overrightarrow a$, suy ra điểm ngọn vectơ này chính là điểm $M.$

Ta biến đổi về đẳng thức vectơ đã biết của trung điểm đoạn thẳng và trọng tâm tam giác.

2. CÁC VÍ DỤ

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho hai điểm $A$, $B$ phân biệt. Xác định điểm $M$ biết $2\overrightarrow {MA} – 3\overrightarrow {MB} = \vec 0.$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-8.png" alt="">

Ta có $2\overrightarrow {MA} – 3\overrightarrow {MB} = \vec 0$ $\Leftrightarrow 2\overrightarrow {MA} – 3(\overrightarrow {MA} + \overrightarrow {AB} ) = \overrightarrow 0$ $\Leftrightarrow \overrightarrow {AM} = 3\overrightarrow {AB} .$

$M$ nằm trên tia $AB$ và $AM = 3AB.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tứ giác $ABCD.$ Xác định điểm $M$, $N$, $P$ sao cho:

a) $2\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \vec 0.$

b) $\overrightarrow {NA} + \overrightarrow {NB} + \overrightarrow {NC} + \overrightarrow {ND} = \vec 0.$

c) $3\overrightarrow {PA} + \overrightarrow {PB} + \overrightarrow {PC} + \overrightarrow {PD} = \vec 0.$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-9.png" alt="">

a) Gọi $I$ là trung điểm $BC$, suy ra $\overrightarrow {MB} + \overrightarrow {MC} = 2\overrightarrow {MI} .$

Do đó $2\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} = \vec 0$ $\Leftrightarrow 2\overrightarrow {MA} + 2\overrightarrow {MI} = \vec 0$ $\Leftrightarrow \overrightarrow {MA} + \overrightarrow {MI} = \vec 0.$

Suy ra $M$ là trung điểm $AI.$

b) Gọi $K$, $H$ lần lượt là trung điểm của $AB$, $CD$, ta có:

$\overrightarrow {NA} + \overrightarrow {NB} + \overrightarrow {NC} + \overrightarrow {ND} = \vec 0$ $\Leftrightarrow 2\overrightarrow {NK} + 2\overrightarrow {NH} = \vec 0$ $\Leftrightarrow \overrightarrow {NK} + \overrightarrow {NH} = \vec 0$ $\Leftrightarrow N$ là trung điểm của $KH.$

c) Gọi $G$ là trọng tâm tam giác $BCD$, khi đó ta có:

$\overrightarrow {PB} + \overrightarrow {PC} + \overrightarrow {PD} = 3\overrightarrow {PG} .$

Suy ra $3\overrightarrow {PA} + \overrightarrow {PB} + \overrightarrow {PC} + \overrightarrow {PD} = \vec 0$ $\Leftrightarrow 3\overrightarrow {PA} + 3\overrightarrow {PG} = \vec 0$ $\Leftrightarrow \overrightarrow {PA} + \overrightarrow {PG} = \vec 0$ $\Leftrightarrow P$ là trung điểm $AG.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho trước hai điểm $A$, $B$ và hai số thực $\alpha$, $\beta$ thoả mãn $\alpha + \beta \ne 0.$ Chứng minh rằng tồn tại duy nhất điểm $I$ thoả mãn $\alpha \overrightarrow {IA} + \beta \overrightarrow {IB} = \vec 0.$ Từ đó suy ra với điểm bất kì $M$ thì $\alpha \overrightarrow {MA} + \beta \overrightarrow {MB} = (\alpha + \beta )\overrightarrow {MI} .$

Ta có: $\alpha \overrightarrow {IA} + \beta \overrightarrow {IB} = \vec 0$ $\Leftrightarrow \alpha \overrightarrow {IA} + \beta (\overrightarrow {IA} + \overrightarrow {AB} ) = \vec 0$ $\Leftrightarrow (\alpha + \beta )\overrightarrow {IA} + \beta \overrightarrow {AB} = \vec 0$ $\Leftrightarrow (\alpha + \beta )\overrightarrow {AI} = \beta \overrightarrow {AB}$ $\Leftrightarrow \overrightarrow {AI} = \frac{\beta }{{\alpha + \beta }}\overrightarrow {BA} .$

Vì $A$, $B$ cố định nên vectơ $\frac{\beta }{{\alpha + \beta }}\overrightarrow {BA}$ không đổi, do đó tồn tại duy nhất điểm $I$ thoả mãn điều kiện.

Từ đó suy ra: $\alpha \overrightarrow {MA} + \beta \overrightarrow {MB}$ $= \alpha (\overrightarrow {MI} + \overrightarrow {IA} ) + \beta (\overrightarrow {MI} + \overrightarrow {IB} )$ $= (\alpha + \beta )\overrightarrow {MI} + (\alpha \overrightarrow {IA} + \beta \overrightarrow {IB} )$ $= (\alpha + \beta )\overrightarrow {MI} .$

## Bài tập
## Bài 1: Xác định các điểm $I$, $J$, $K$, $L$ biết:

a) $\overrightarrow {IA} – 2\overrightarrow {IB} = \vec 0.$

b) $\overrightarrow {JA} – \overrightarrow {JB} – 2\overrightarrow {JC} = \vec 0.$

c) $\overrightarrow {KA} + \overrightarrow {KB} + \overrightarrow {KC} = \overrightarrow {BC} .$

d) $2\overrightarrow {LA} – \overrightarrow {LB} + 3\overrightarrow {LC} = \overrightarrow {AB} + \overrightarrow {AC} .$

## Bài 2: Cho tứ giác $ABCD.$ Tìm điểm cố định $I$ và hằng số $k$ để hệ thức sau thỏa mãn với mọi $M.$

a) $\overrightarrow {MA} + \overrightarrow {MB} + 2\overrightarrow {MC} = k\overrightarrow {MI} .$

b) $2\overrightarrow {MA} + 3\overrightarrow {MB} – \overrightarrow {MD} = k\overrightarrow {MI} .$

c) $\overrightarrow {MA} + 2\overrightarrow {MB} + 3\overrightarrow {MC} – 4\overrightarrow {MD} = k\overrightarrow {MI} .$

## Bài 3: Cho tam giác $ABC$ và ba số thực $\alpha$, $\beta$, $\gamma$ không đồng thời bằng không. Chứng minh rằng:

a) Nếu $\alpha + \beta + \gamma \ne 0$ thì tồn tại duy nhất điểm $M$ sao cho $\alpha \overrightarrow {MA} + \beta \overrightarrow {MB} + \gamma \overrightarrow {MC} = \vec 0.$

b) Nếu $\alpha + \beta + \gamma = 0$ thì không tồn tại điểm $N$ sao cho $\alpha \overrightarrow {NA} + \beta \overrightarrow {NB} + \gamma \overrightarrow {NC} = \vec 0.$

## Bài 4: Cho $n$ điểm ${A_1},{A_2}, \ldots ,{A_n}$ và $n$ số ${k_1},{k_2}, \ldots ,{k_n}$ mà ${k_1} + {k_2} + \ldots + {k_n} = k \ne 0.$

a) Chứng minh rằng có duy nhất điểm $G$ sao cho: ${k_1}\overrightarrow {G{A_1}} + {k_2}\overrightarrow {G{A_2}} + \ldots + {k_n}\overrightarrow {G{A_n}} = \overrightarrow 0 .$

Điểm $G$ như thế gọi là tâm tỉ cự của hệ điểm ${A_i}$ gắn với hệ số ${k_i}.$ Trong trường hợp các hệ số ${k_i}$ bằng nhau (ta có thể chọn các ${k_i}$ đều bằng $1$) thì $G$ gọi là trọng tâm của hệ điểm ${A_i}.$

b) Chứng minh rằng nếu $G$ là tâm tỉ cự nói ở câu a thì với điểm $M$ bất kỳ ta có: $\frac{1}{k}\left( {{k_1}\overrightarrow {M{A_1}} + {k_2}\overrightarrow {M{A_2}} + \ldots + {k_n}\overrightarrow {M{A_n}} } \right) = \overrightarrow {OG} .$

**DẠNG TOÁN 4: PHÂN TÍCH MỘT VECTƠ THEO HAI VECTƠ KHÔNG CÙNG PHƯƠNG.**

**1. PHƯƠNG PHÁP GIẢI**

Sử dụng các tính chất phép toán vectơ, ba quy tắc phép toán vectơ và tính chất trung điểm, trọng tâm trong tam giác.

2. CÁC VÍ DỤ

<!-- chunk:12 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho tam giác $ABC.$ Đặt $\vec a = \overrightarrow {AB}$, $\vec b = \overrightarrow {AC} .$

a) Hãy dựng các điểm $M$, $N$ thỏa mãn: $\overrightarrow {AM} = \frac{1}{3}\overrightarrow {AB}$, $\overrightarrow {CN} = 2\overrightarrow {BC} .$

b) Hãy phân tích $\overrightarrow {CM}$, $\overrightarrow {AN}$, $\overrightarrow {MN}$ qua các véctơ $\overrightarrow a$ và $\overrightarrow b .$

c) Gọi $I$ là điểm thỏa: $\overrightarrow {MI} = \overrightarrow {CM} .$ Chứng minh $I$, $A$, $N$ thẳng hàng.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-10.png" alt="">

a) Vì $\overrightarrow {AM} = \frac{1}{3}\overrightarrow {AB}$ suy ra $M$ thuộc cạnh $AB$ và $AM = \frac{1}{3}AB$, $\overrightarrow {CN} = 2\overrightarrow {BC}$ suy ra $N$ thuộc tia $BC$ và $CN = 2BC.$

b) Ta có: $\overrightarrow {CM} = \overrightarrow {CA} + \overrightarrow {AM}$ $= – \overrightarrow {AC} + \frac{1}{3}\overrightarrow {AB} = \frac{1}{3}\overrightarrow a – \overrightarrow b .$

$\overrightarrow {AN} = \overrightarrow {AB} + \overrightarrow {BN}$ $= \overrightarrow {AB} + 3\overrightarrow {BC}$ $= \overrightarrow {AB} + 3(\overrightarrow {AC} – \overrightarrow {AB} )$ $= – 2\overrightarrow a + 3\overrightarrow b .$

$\overrightarrow {MN} = \overrightarrow {MA} + \overrightarrow {AN}$ $= – \frac{1}{3}\overrightarrow a – 2\overrightarrow a + 3\overrightarrow b$ $= – \frac{7}{3}\overrightarrow a + 3\overrightarrow b .$

c) Ta có: $\overrightarrow {AI} = \overrightarrow {AM} + \overrightarrow {MI}$ $= \frac{1}{3}\overrightarrow {AB} + \overrightarrow {CM}$ $= \frac{1}{3}\overrightarrow a + \frac{1}{3}\overrightarrow a – \overrightarrow b$ $= – \frac{1}{3}( – 2\overrightarrow a + 3\overrightarrow b ).$

$\Rightarrow \overrightarrow {AI} = – \frac{1}{3}\overrightarrow {AN}$ $\Rightarrow A$, $I$, $N$ thẳng hàng.

<!-- chunk:13 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tam giác $ABC$, trên cạnh $BC$ lấy $M$ sao cho $BM = 3CM$, trên đoạn $AM$ lấy $N$ sao cho $2AN = 5MN$, $G$ là trọng tâm tam giác $ABC.$

a) Phân tích các vectơ $\overrightarrow {AM}$, $\overrightarrow {BN}$ qua các véctơ $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

b) Phân tích các vectơ $\overrightarrow {GC}$, $\overrightarrow {MN}$ qua các véctơ $\overrightarrow {GA}$ và $\overrightarrow {GB} .$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-11.png" alt="">

a) Theo giả thiết ta có: $\overrightarrow {BM} = \frac{3}{4}\overrightarrow {BC}$ và $\overrightarrow {AN} = \frac{5}{7}\overrightarrow {AM} .$

Suy ra $\overrightarrow {AM} = \overrightarrow {AB} + \overrightarrow {BM}$ $= \overrightarrow {AB} + \frac{3}{4}\overrightarrow {BC}$ $= \overrightarrow {AB} + \frac{3}{4}(\overrightarrow {AC} – \overrightarrow {AB} )$ $= \frac{1}{4}\overrightarrow {AB} + \frac{3}{4}\overrightarrow {AC} .$

$\overrightarrow {BN} = \overrightarrow {BA} + \overrightarrow {AN}$ $= – \overrightarrow {AB} + \frac{5}{7}\overrightarrow {AM}$ $= – \overrightarrow {AB} + \frac{5}{7}\left( {\frac{1}{4}\overrightarrow {AB} + \frac{3}{4}\overrightarrow {AC} } \right)$ $= – \frac{{23}}{{28}}\overrightarrow {AB} + \frac{{15}}{{28}}\overrightarrow {AC} .$

b) Vì $G$ là trọng tâm tam giác $ABC$ nên $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$, suy ra:

$\overrightarrow {GC} = – \overrightarrow {GA} – \overrightarrow {GB} .$

Ta có $\overrightarrow {MN} = – \frac{2}{7}\overrightarrow {AM}$ $= – \frac{2}{7}\left( {\frac{1}{4}\overrightarrow {AB} + \frac{3}{4}\overrightarrow {AC} } \right)$ $= – \frac{1}{{14}}(\overrightarrow {GB} – \overrightarrow {GA} ) – \frac{3}{{14}}(\overrightarrow {GC} – \overrightarrow {GA} )$ $= – \frac{1}{{14}}(\overrightarrow {GB} – \overrightarrow {GA} )$ $– \frac{3}{{14}}( – \overrightarrow {GA} – \overrightarrow {GB} – \overrightarrow {GA} )$ $= \frac{1}{2}\overrightarrow {GA} + \frac{1}{7}\overrightarrow {GB} .$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho hình bình hành $ABCD.$ Gọi $M$, $N$ lần lượt là hai điểm nằm trên hai cạnh $AB$ và $CD$ sao cho $AB = 3AM$, $CD = 2CN$ và $G$ là trọng tâm tam giác $MNB.$ Phân tích các vectơ $\overrightarrow {AN}$, $\overrightarrow {MN}$, $\overrightarrow {AG}$ qua các véctơ $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-12.png" alt="">

Ta có: $\overrightarrow {AN} = \overrightarrow {AC} + \overrightarrow {CN}$ $= \overrightarrow {AC} – \frac{1}{2}\overrightarrow {AB} .$

$\overrightarrow {MN} = \overrightarrow {MA} + \overrightarrow {AN}$ $= – \frac{1}{3}\overrightarrow {AB} + \overrightarrow {AC} – \frac{1}{2}\overrightarrow {AB}$ $= – \frac{5}{6}\overrightarrow {AB} + \overrightarrow {AC} .$

Vì $G$ là trọng tâm tam giác $MNB$ nên:

$3\overrightarrow {AG} = \overrightarrow {AM} + \overrightarrow {AN} + \overrightarrow {AB}$ $= \frac{1}{3}\overrightarrow {AB} + \left( {\overrightarrow {AC} – \frac{1}{2}\overrightarrow {AB} } \right) + \overrightarrow {AB}$ $= \frac{5}{6}\overrightarrow {AB} + \overrightarrow {AC} .$

Suy ra $\overrightarrow {AG} = \frac{5}{{18}}\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} .$

## Bài tập
## Bài 1: Cho tam giác $ABC.$ Lấy các điểm $M$, $N$, $P$ sao cho $\overrightarrow {MB} = 3\overrightarrow {MC}$, $\overrightarrow {NA} + 2\overrightarrow {NC} = \vec 0$, $\overrightarrow {PA} + \overrightarrow {PB} = \vec 0.$

a) Biểu diễn các vectơ $\overrightarrow {AP}$, $\overrightarrow {AN}$, $\overrightarrow {AM}$ theo các vectơ $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

b) Biểu diễn các vectơ $\overrightarrow {MP}$, $\overrightarrow {MN}$ theo các vectơ $\overrightarrow {AB}$ và $\overrightarrow {AC} .$ Chứng minh rằng ba điểm $M$, $N$, $P$ thẳng hàng?

## Bài 2: Cho tam giác $ABC.$ Gọi $I$, $J$ là hai điểm xác định bởi:

$\overrightarrow {IA} = 2\overrightarrow {IB}$, $3\overrightarrow {JA} + 2\overrightarrow {JC} = \vec 0.$

a) Tính $\overrightarrow {IJ}$ theo $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

b) Chứng minh đường thẳng $IJ$ đi qua trọng tâm $G$ của tam giác $ABC.$

## Bài 3: Cho tam giác $ABC$ có trọng tâm $G.$ Gọi $I$ là điểm trên cạnh $BC$ sao cho $2CI = 3BI$ và $J$ là điểm trên $BC$ kéo dài sao cho $5JB = 2JC.$

a) Hãy phân tích $\overrightarrow {AI}$, $\overrightarrow {AJ}$ theo $\overrightarrow {AB}$ và $\overrightarrow {AC} .$

b) Hãy phân tích $\overrightarrow {AG}$ theo $\overrightarrow {AI}$ và $\overrightarrow {AJ} .$

## Bài 4: Cho hai vectơ $\vec a$, $\vec b$ không cùng phương. Tìm $x$ sao cho:

a) $\overrightarrow u = \overrightarrow a + (2x – 1)\overrightarrow b$ và $\overrightarrow v = x\overrightarrow a + \overrightarrow b$ cùng phương.

b) $\vec u = 3\vec a + x\vec b$ và $\overrightarrow u = (1 – x)\overrightarrow a – \frac{2}{3}\overrightarrow b$ cùng hướng.

DẠNG TOÁN 5: CHỨNG MINH HAI ĐIỂM TRÙNG NHAU – HAI TAM GIÁC CÙNG TRỌNG TÂM.

1. PHƯƠNG PHÁP GIẢI

Để chứng minh hai điểm ${A_1}$ và ${A_2}$ trùng nhau, ta lựa chọn một trong hai cách sau:

Cách 1: Chứng minh $\overrightarrow {{A_1}{A_2}} = \vec 0.$

Cách 2: Chứng minh $\overrightarrow {O{A_1}} = \overrightarrow {O{A_2}}$ với $O$ là điểm tuỳ ý.

Để chứng minh hai tam giác $ABC$ và $A’B’C’$ cùng trọng tâm ta làm như sau:

Cách 1: Chứng minh $G$ là trọng tâm $\Delta ABC$ trùng với $G’$ là trọng tâm $\Delta A’B’C’.$

Cách 2: Gọi $G$ là trọng tâm $\Delta ABC$ (tức ta có $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$) ta đi chứng minh $\overrightarrow {GA’} + \overrightarrow {GB’} + \overrightarrow {GC’} = \overrightarrow 0 .$

2. CÁC VÍ DỤ

<!-- chunk:15 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Chứng minh rằng $\overrightarrow {AB} = \overrightarrow {CD}$ khi và chỉ khi trung điểm của hai đoạn thẳng $AD$ và $BC$ trùng nhau.

Gọi $I$, $J$ lần lượt là trung điểm của $AD$ và $BC$, suy ra $\overrightarrow {AI} = \overrightarrow {ID}$, $\overrightarrow {CJ} = \overrightarrow {JB} .$

Do đó $\overrightarrow {AB} = \overrightarrow {CD}$ $\Leftrightarrow \overrightarrow {AI} + \overrightarrow {IJ} + \overrightarrow {JB} = \overrightarrow {CJ} + \overrightarrow {JI} + \overrightarrow {ID} .$

$\Leftrightarrow \overrightarrow {IJ} = \overrightarrow {JI} \Leftrightarrow \overrightarrow {IJ} = \vec 0$ hay $I$ trùng với $J.$

<!-- chunk:16 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tam giác $ABC$, trên các cạnh $AB$, $BC$, $CA$ ta lấy lần lượt các điểm $M$, $N$, $P$ sao cho $\frac{{AM}}{{AB}} = \frac{{BN}}{{BC}} = \frac{{CP}}{{CA}}.$ Chứng minh rằng hai tam giác $ABC$ và $MNP$ có cùng trọng tâm.

Giả sử $\frac{{AM}}{{AB}} = k$, suy ra $\overrightarrow {AM} = k\overrightarrow {AB}$, $\overrightarrow {BN} = k\overrightarrow {BC}$, $\overrightarrow {CP} = k\overrightarrow {CA} .$

Cách 1: Gọi $G$, $G’$ lần lượt là trọng tâm $\Delta ABC$ và $\Delta MNP.$

Suy ra $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ và $\overrightarrow {G’M} + \overrightarrow {G’N} + \overrightarrow {G’P} = \vec 0$ $(*).$

Ta có $\overrightarrow {AM} = k\overrightarrow {AB}$ $\Leftrightarrow \overrightarrow {AG} + \overrightarrow {GG’} + \overrightarrow {G’M} = k\overrightarrow {AB} .$

Tương tự $\overrightarrow {BG} + \overrightarrow {GG’} + \overrightarrow {G’N} = k\overrightarrow {BC} .$

Và $\overrightarrow {CG} + \overrightarrow {GG’} + \overrightarrow {G’P} = k\overrightarrow {CA} .$

Cộng vế với vế từng đẳng thức trên ta được:

$(\overrightarrow {AG} + \overrightarrow {BG} + \overrightarrow {CG} )$ $+ 3\overrightarrow {GG’} + (\overrightarrow {G’M} + \overrightarrow {G’N} + \overrightarrow {G’P} )$ $= k(\overrightarrow {AB} + \overrightarrow {BC} + \overrightarrow {CA} ).$

Kết hợp với $(*)$ ta được $\overrightarrow {GG’} = \vec 0.$

Suy ra điều phải chứng minh.

Cách 2: Gọi $G$ là trọng tâm tam giác $ABC$ suy ra $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \overrightarrow 0 .$

Ta có: $\overrightarrow {GM} + \overrightarrow {GN} + \overrightarrow {GP}$ $= \overrightarrow {GA} + \overrightarrow {AM}$ $+ \overrightarrow {GB} + \overrightarrow {BN}$ $+ \overrightarrow {GC} + \overrightarrow {CP}$ $= \overrightarrow {AM} + \overrightarrow {BN} + \overrightarrow {CP}$ $= k\overrightarrow {AB} + k\overrightarrow {BC} + k\overrightarrow {CA}$ $= k(\overrightarrow {AB} + \overrightarrow {BC} + \overrightarrow {CA} ) = \vec 0.$

Vậy hai tam giác $ABC$ và $MNP$ có cùng trọng tâm.

<!-- chunk:17 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho lục giác $ABCDEF.$ Gọi $M$, $N$, $P$, $Q$, $R$, $S$ lần lượt là trung điểm của các cạnh $AB$, $BC$, $CD$, $DE$, $EF$, $FA.$ Chứng minh rằng hai tam giác $MPR$ và $NQS$ có cùng trọng tâm.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-13.png" alt="">

Gọi $G$ là trọng tâm của $\Delta MPR$, suy ra $\overrightarrow {GM} + \overrightarrow {GP} + \overrightarrow {GR} = \vec 0$ $(*).$

Mặt khác $2\overrightarrow {GM} = \overrightarrow {GA} + \overrightarrow {GB}$, $2\overrightarrow {GP} = \overrightarrow {GC} + \overrightarrow {GD}$, $2\overrightarrow {GR} = \overrightarrow {GE} + \overrightarrow {GF} .$

$\Rightarrow 2(\overrightarrow {GM} + \overrightarrow {GP} + \overrightarrow {GR} )$ $= \overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} + \overrightarrow {GD} + \overrightarrow {GE} + \overrightarrow {GF} .$

Kết hợp với $(*)$ ta được:

$\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} + \overrightarrow {GD} + \overrightarrow {GE} + \overrightarrow {GF} = \vec 0.$

$\Leftrightarrow (\overrightarrow {GA} + \overrightarrow {GF} )$ $+ (\overrightarrow {GB} + \overrightarrow {GC} )$ $+ (\overrightarrow {GD} + \overrightarrow {GE} ) = \overrightarrow 0 .$

$\Leftrightarrow 2\overrightarrow {GS} + 2\overrightarrow {GN} + 2\overrightarrow {GQ} = \vec 0.$

$\Leftrightarrow \overrightarrow {GS} + \overrightarrow {GN} + \overrightarrow {GQ} = \vec 0.$

Suy ra $G$ là trọng tâm của $\Delta SNQ.$

Vậy $\Delta MPR$ và $\Delta SNQ$ có cùng trọng tâm.

<!-- chunk:18 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 4: Cho hai hình bình hành $ABCD$ và $AB’C’D’$ chung đỉnh $A.$ Chứng minh rằng hai tam giác $BC’D$ và $B’CD’$ cùng trọng tâm.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-14.png" alt="">

Gọi $G$ là trọng tâm tam giác $BC’D$ suy ra $\overrightarrow {GB} + \overrightarrow {GC’} + \overrightarrow {GD} = \vec 0.$

$\Leftrightarrow \overrightarrow {GB’} + \overrightarrow {GC} + \overrightarrow {GD’} + \overrightarrow {B’B} + \overrightarrow {CC’} + \overrightarrow {D’D} = \vec 0$ $(1).$

Mặt khác theo quy tắc phép trừ và hình bình hành ta có:

$\overrightarrow {B’B} + \overrightarrow {CC’} + \overrightarrow {D’D}$ $= (\overrightarrow {AB} – \overrightarrow {AB’} )$ $+ (\overrightarrow {AC’} – \overrightarrow {AC} )$ $+ (\overrightarrow {AD} – \overrightarrow {AD’} )$ $= (\overrightarrow {AB} + \overrightarrow {AD} ) – \overrightarrow {AC}$ $– (\overrightarrow {AB’} + \overrightarrow {AD’} ) + \overrightarrow {AC’}$ $= \overrightarrow {AC} – \overrightarrow {AC} – \overrightarrow {AC’} + \overrightarrow {AC’} = \vec 0$ $(2).$

Từ $(1)$ và $(2)$ ta có: $\overrightarrow {GB’} + \overrightarrow {GC} + \overrightarrow {GD’} = \vec 0$ hay $G$ là trọng tâm tam giác $B’CD’.$

## Bài tập
## Bài 1: Cho các tam giác $ABC$, $A’B’C’$ có $G$, $G’$ lần lượt là trọng tâm. Chứng minh rằng: $\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} = 3\overrightarrow {GG’} .$ Từ đó suy ra điều kiện cần và đủ để hai tam giác có cùng trọng tâm.

## Bài 2: Cho tam giác $ABC$, vẽ các hình bình hành $ABIJ$, $BCPQ$, $CARS.$ Chứng minh rằng $\Delta RIP$, $\Delta JQS$ có cùng trọng tâm.

## Bài 3: Cho tứ giác $ABCD.$ Gọi $M$, $N$, $P$, $Q$ lần lượt là trung điểm của $AB$, $BC$, $CD$, $DA.$ Chứng minh rằng hai tam giác $ANP$ và $CMQ$ có cùng trọng tâm.

## Bài 4: Cho tam giác $ABC.$ Gọi $A’$, $B’$, $C’$ là các điểm xác định bởi $2011\overrightarrow {A’B} + 2012\overrightarrow {A’C} = \overrightarrow 0$, $2011\overrightarrow {B’C} + 2012\overrightarrow {B’A} = \overrightarrow 0$, $2011\overrightarrow {C’A} + 2012\overrightarrow {C’B} = \overrightarrow 0 .$ Chứng minh rằng $\Delta ABC$ và $\Delta A’B’C’$ cùng trọng tâm.

## Bài 5: Cho $\Delta ABC$ và $\Delta A’B’C’$ có cùng trọng tâm $G$, gọi ${G_1}$, ${G_2}$, ${G_3}$ là trọng tâm các tam giác $BCA’$, $CAB’$, $ABC’.$ Chứng minh rằng $\Delta {G_1}{G_2}{G_3}$ cũng có trọng tâm $G.$

## Bài 6: Cho tứ giác $ABCD$ có trọng tâm $G.$ Gọi ${G_1}$, ${G_2}$, ${G_3}$, ${G_4}$ lần lượt là trọng tâm các tam giác $\Delta ABC$, $\Delta BCD$, $\Delta CDA$, $\Delta DAB.$ Chứng minh rằng $G$ cũng là trọng tâm tứ giác ${G_1}{G_2}{G_3}{G_4}.$

## Bài 7: Cho tam giác $ABC$ đều và $M$ là một điểm nằm trong tam giác. Gọi ${A_1}$, ${B_1}$, ${C_1}$ lần lượt là điểm đối xứng $M$ qua $BC$, $CA$, $AB.$ Chứng minh rằng tam giác $ABC$ và ${A_1}{B_1}{C_1}$ có cùng trọng tâm.

## Bài 8: Cho tam giác $ABC$, điểm $O$ nằm trong tam giác. Gọi ${A_1}$, ${B_1}$, ${C_1}$ lần lượt là hình chiếu của $O$ lên $BC$, $CA$, $AB.$ Lấy các điểm ${A_2}$, ${B_2}$, ${C_2}$ lần lượt thuộc các tia $O{A_1}$, $O{B_1}$, $O{C_1}$ sao cho $O{A_2} = a$, $O{B_2} = b$, $O{C_2} = c.$ Chứng minh $O$ là trọng tâm tam giác ${A_2}{B_2}{C_2}.$

DẠNG TOÁN 6: TÌM TẬP HỢP ĐIỂM THỎA MÃN ĐIỀU KIỆN VECTƠ CHO TRƯỚC.

1. PHƯƠNG PHÁP GIẢI

Để tìm tập hợp điểm $M$ thỏa mãn mãn điều kiện vectơ ta quy về một trong các dạng sau:

– Nếu $|\overrightarrow {MA} | = |\overrightarrow {MB} |$ với $A$, $B$ phân biệt cho trước thì $M$ thuộc đường trung trực của đoạn $AB.$

– Nếu $|\overrightarrow {MC} | = k.|\overrightarrow {AB} |$ với $A$, $B$, $C$ phân biệt cho trước thì $M$ thuộc đường tròn tâm $C$, bán kính bằng $k.|\overrightarrow {AB} |.$

– Nếu $\overrightarrow {MA} = k\overrightarrow {BC}$ với $A$, $B$, $C$ phân biệt và $k$ là số thực thay đổi thì:

+ $M$ thuộc đường thẳng qua $A$ song song với $BC$ với $k \in R.$

+ $M$ thuộc nửa đường thẳng qua $A$ song song với $BC$ và cùng hướng $\overrightarrow {BC}$ với $k > 0.$

+ $M$ thuộc nửa đường thẳng qua $A$ song song với $BC$ và ngược hướng $\overrightarrow {BC}$ với $k < 0.$

– Nếu $\overrightarrow {MA} = k\overrightarrow {BC}$, $B \ne C$ với $A$, $B$, $C$ thẳng hàng và $k$ thay đổi thì tập hợp điểm $M$ là đường thẳng $BC.$

2. CÁC VÍ DỤ

<!-- chunk:19 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho tam giác $ABC.$

a) Chứng minh rằng tồn tại duy nhất điểm $I$ thỏa mãn: $2\overrightarrow {IA} + 3\overrightarrow {IB} + 4\overrightarrow {IC} = \vec 0.$

b) Tìm quỹ tích điểm $M$ thỏa mãn: $|2\overrightarrow {MA} + 3\overrightarrow {MB} + 4\overrightarrow {MC} | = |\overrightarrow {MB} – \overrightarrow {MA} |.$

a) Ta có: $2\overrightarrow {IA} + 3\overrightarrow {IB} + 4\overrightarrow {IC} = \vec 0$ $\Leftrightarrow 2\overrightarrow {IA} + 3(\overrightarrow {IA} + \overrightarrow {AB} ) + 4(\overrightarrow {IA} + \overrightarrow {AC} ) = \vec 0.$

$\Leftrightarrow 9\overrightarrow {IA} = – 3\overrightarrow {AB} – 4\overrightarrow {AC}$ $\Leftrightarrow \overrightarrow {IA} = – \frac{{3\overrightarrow {AB} + 4\overrightarrow {AC} }}{9}$ $\Rightarrow I$ tồn tại và duy nhất.

b) Với $I$ là điểm được xác định ở câu a, ta có:

$2\overrightarrow {MA} + 3\overrightarrow {MB} + 4\overrightarrow {MC}$ $= 9\overrightarrow {MI} + (2\overrightarrow {IA} + 3\overrightarrow {IB} + 4\overrightarrow {IC} )$ $= 9\overrightarrow {MI}$ và $\overrightarrow {MB} – \overrightarrow {MA} = \overrightarrow {AB}$ nên $|2\overrightarrow {MA} + 3\overrightarrow {MB} + 4\overrightarrow {MC} | = |\overrightarrow {MB} – \overrightarrow {MA} |$ $\Leftrightarrow |9\overrightarrow {MI} | = |\overrightarrow {AB} |$ $\Leftrightarrow MI = \frac{{AB}}{9}.$

Vậy quỹ tích của $M$ là đường tròn tâm $I$ bán kính $\frac{{AB}}{9}.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tam giác $ABC.$ Tìm tập hợp các điểm $M$ thoả mãn điều kiện sau:

a) $|\overrightarrow {MA} + \overrightarrow {MB} | = |\overrightarrow {MA} + \overrightarrow {MC} |.$

b) $\overrightarrow {MA} + \overrightarrow {MB} = k(\overrightarrow {MA} + 2\overrightarrow {MB} – 3\overrightarrow {MC} )$ với $k$ là số thực thay đổi.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-15.png" alt="">

a) Gọi $E$, $F$ lần lượt là trung điểm của $AB$, $AC$ suy ra:

$\overrightarrow {MA} + \overrightarrow {MB} = 2\overrightarrow {ME}$ và $\overrightarrow {MA} + \overrightarrow {MC} = 2\overrightarrow {MF} .$

Khi đó $|\overrightarrow {MA} + \overrightarrow {MB} | = |\overrightarrow {MA} + \overrightarrow {MC} |$ $\Leftrightarrow |2\overrightarrow {ME} | = |2\overrightarrow {MF} |$ $\Leftrightarrow ME = MF.$

Vậy tập hợp các điểm $M$ là đường trung trực của $EF.$

b) Ta có:

$\overrightarrow {MA} + 2\overrightarrow {MB} – 3\overrightarrow {MC}$ $= \overrightarrow {MA} + 2(\overrightarrow {MA} + \overrightarrow {AB} ) – 3(\overrightarrow {MA} + \overrightarrow {AC} )$ $= 2\overrightarrow {AB} – 3\overrightarrow {AC}$ $= 2\overrightarrow {AB} – 2\overrightarrow {AH}$ $= 2\overrightarrow {HB} .$

Với $H$ là điểm thỏa mãn $\overrightarrow {AH} = \frac{3}{2}\overrightarrow {AC} .$

Suy ra $\overrightarrow {MA} + \overrightarrow {MB} = k(\overrightarrow {MA} + 2\overrightarrow {MB} – 3\overrightarrow {MC} )$ $\Leftrightarrow 2\overrightarrow {ME} = 2k\overrightarrow {HB}$ $\Leftrightarrow \overrightarrow {ME} = k\overrightarrow {HB} .$

Vậy tập hợp điểm $M$ là đường thẳng đi qua $E$ và song song với $HB.$

<!-- chunk:21 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho tứ giác $ABCD.$ Với số $k$ tùy ý, lấy các điểm $M$ và $N$ sao cho $\overrightarrow {AM} = k\overrightarrow {AB}$, $\overrightarrow {DN} = k\overrightarrow {DC} .$ Tìm tập hợp các trung điểm $I$ của đoạn thẳng $MN$ khi $k$ thay đổi.

<img link="data_for_rag/toan10/images/tich-cua-mot-vecto-voi-mot-so-16.png" alt="">

Gọi $O$, $O’$ lần lượt là trung điểm của $AD$ và $BC$, ta có:

$\overrightarrow {AB} = \overrightarrow {AO} + \overrightarrow {OO’} + \overrightarrow {O’B}$ và $\overrightarrow {DC} = \overrightarrow {DO} + \overrightarrow {OO’} + \overrightarrow {O’C} .$

Suy ra $\overrightarrow {AB} + \overrightarrow {DC} = 2\overrightarrow {OO’} .$

Tương tự vì $O$, $I$ lần lượt là trung điểm của $AD$ và $MN$ nên $\overrightarrow {AM} + \overrightarrow {DN} = 2\overrightarrow {OI} .$

Do đó $\overrightarrow {OI} = \frac{1}{2}(k\overrightarrow {AB} + k\overrightarrow {DC} )$ $= k\overrightarrow {OO’} .$

Vậy khi $k$ thay đổi, tập hợp điểm $I$ là đường thẳng $OO’.$

## Bài tập
## Bài 1: Cho hai điểm cố định $A$, $B.$ Tìm tập hợp các điểm $M$ sao cho:

a) $|\overrightarrow {MA} + \overrightarrow {MB} | = |\overrightarrow {MA} – \overrightarrow {MB} |.$

b) $|2\overrightarrow {MA} + \overrightarrow {MB} | = |\overrightarrow {MA} + 2\overrightarrow {MB} |.$

## Bài 2: Cho $\Delta ABC$. Tìm tập hợp các điểm $M$ sao cho:

a) $\overrightarrow {MA} + k\overrightarrow {MB} = k\overrightarrow {MC}$ với $k$ là số thực thay đổi.

b) $\overrightarrow v = \overrightarrow {MA} + \overrightarrow {MB} + 2\overrightarrow {MC}$ cùng phương với vectơ $\overrightarrow {BC} .$

c) $|\overrightarrow {MA} + \overrightarrow {BC} | = |\overrightarrow {MA} – \overrightarrow {MB} |.$

## Bài 3: Cho $\Delta ABC$. Tìm tập hợp điểm $M$ trong các trường hợp sau:

a) $|2\overrightarrow {MA} + 3\overrightarrow {MB} | = |3\overrightarrow {MB} – 2\overrightarrow {MC} |.$

b) $|4\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} |$ $= |2\overrightarrow {MA} – \overrightarrow {MB} – \overrightarrow {MC} |.$

## Bài 4: Cho tứ giác $ABCD.$

a) Xác định điểm $O$ sao cho: $\overrightarrow {OB} + 4\overrightarrow {OC} = 2\overrightarrow {OD} .$

b) Tìm tập hợp điểm $M$ thoả mãn hệ thức: $|\overrightarrow {MB} + 4\overrightarrow {MC} – 2\overrightarrow {MD} | = |3\overrightarrow {MA} |.$

## Bài 5: Cho lục giác đều $ABCDEF.$ Tìm tập hợp các điểm $M$ sao cho: $|\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} |$ $+ |\overrightarrow {MD} + \overrightarrow {ME} + \overrightarrow {MF} |$ nhận giá trị nhỏ nhất.

## Bài 6: Trên hai tia $Ox$ và $Oy$ của góc $xOy$ lấy hai điểm $M$, $N$ sao cho $OM + ON = a$ với $a$ là số thực cho trước, tìm tập hợp trung điểm $I$ của đoạn thẳng $MN.$

DẠNG TOÁN 7: XÁC ĐỊNH TÍNH CHẤT CỦA HÌNH KHI BIẾT MỘT ĐẲNG THỨC VECTƠ.

1. PHƯƠNG PHÁP GIẢI

Phân tích được định tính xuất phát từ các đẳng thức vectơ của giả thiết, lưu ý tới những hệ thức đã biết về trung điểm của đoạn thẳng, trọng tâm của tam giác và kết quả: “$m\vec a + n\vec b = \vec 0$ $\Leftrightarrow m = n = 0$ với $\vec a$, $\vec b$ là hai vectơ không cùng phương”.

2. CÁC VÍ DỤ

<!-- chunk:22 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Gọi $M$, $N$ lần lượt là trung điểm của các cạnh $AD$ và $DC$ của tứ giác $ABCD.$ Các đoạn thẳng $AN$ và $BM$ cắt nhau tại $P.$ Biết $\overrightarrow {PM} = \frac{1}{5}\overrightarrow {BM}$, $\overrightarrow {AP} = \frac{2}{5}\overrightarrow {AN} .$ Chứng minh rằng tứ giác $ABCD$ là hình bình hành.

Ta có: $\overrightarrow {AB} = \overrightarrow {AM} + \overrightarrow {MB}$ $= \overrightarrow {AM} + 5\overrightarrow {MP} .$

$= 5\overrightarrow {AP} – 4\overrightarrow {AM} = 2\overrightarrow {AN} – 2\overrightarrow {AD} .$

$= 2(\overrightarrow {AD} + \overrightarrow {DN} ) – 2\overrightarrow {AD} .$

$= 2\overrightarrow {DN} = \overrightarrow {DC}$ $\Rightarrow ABCD$ là hình bình hành.

<!-- chunk:23 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tam giác $ABC$ có các cạnh bằng $a$, $b$, $c$ và trọng tâm $G$ thoả mãn: ${a^2}\overrightarrow {GA} + {b^2}\overrightarrow {GB} + {c^2}\overrightarrow {GC} = \vec 0.$ Chứng minh rằng $ABC$ là tam giác đều.

$G$ là trọng tâm tam giác $ABC$ nên $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ $\Leftrightarrow \overrightarrow {GA} = – \overrightarrow {GB} – \overrightarrow {GC} .$

Suy ra ${a^2}\overrightarrow {GA} + {b^2}\overrightarrow {GB} + {c^2}\overrightarrow {GC} = \vec 0.$

$\Leftrightarrow {a^2}( – \overrightarrow {GB} – \overrightarrow {GC} ) + {b^2}\overrightarrow {GB} + c\overrightarrow {GC} = \vec 0.$

$\Leftrightarrow \left( {{b^2} – {a^2}} \right)\overrightarrow {GB} + \left( {{c^2} – {a^2}} \right)\overrightarrow {GC} = \overrightarrow 0$ $(*).$

Vì $\overrightarrow {GB}$ và $\overrightarrow {GC}$ là hai vectơ không cùng phương, do đó $(*)$ tương đương với:

$$
\left\{ {\begin{array}{l}
{{b^2} – {a^2} = 0}\\
{{c^2} – {a^2} = 0}
\end{array}} \right.
$$
 $\Leftrightarrow a = b = c$ hay tam giác $ABC$ đều.

<!-- chunk:24 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 3: Cho tam giác $ABC$ có trung tuyến $AA’$ và $B’$, $C’$ là các điểm thay đổi trên $CA$, $AB$ thoả mãn $\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} = \vec 0.$ Chứng minh $BB’$, $CC’$ là các trung tuyến của tam giác $ABC.$

Giả sử $\overrightarrow {AB’} = m\overrightarrow {AC}$, $\overrightarrow {AC’} = n\overrightarrow {AB} .$

Suy ra $\overrightarrow {BB’} = \overrightarrow {AB’} – \overrightarrow {AB}$ $= m\overrightarrow {AC} – \overrightarrow {AB}$ và $\overrightarrow {CC’} = \overrightarrow {AC’} – \overrightarrow {AC}$ $= n\overrightarrow {AB} – \overrightarrow {AC} .$

Mặt khác $A’$ là trung điểm của $BC$ nên $\overrightarrow {AA’} = \frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} ).$

Do đó $\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} = \vec 0$ $\Leftrightarrow \frac{1}{2}(\overrightarrow {AB} + \overrightarrow {AC} )$ $+ m\overrightarrow {AC} – \overrightarrow {AB}$ $+ n\overrightarrow {AB} – \overrightarrow {AC} = \vec 0.$

Hay $\left( {n – \frac{1}{2}} \right)\overrightarrow {AB} + \left( {m – \frac{1}{2}} \right)\overrightarrow {AC} = \vec 0.$

Vì $\overrightarrow {AB}$, $\overrightarrow {AC}$ không cùng phương suy ra $m = n = \frac{1}{2}$ do đó $B’$, $C’$ lần lượt là trung điểm của $CA$, $AB.$

Vậy $BB’$, $CC’$ là các trung tuyến của tam giác $ABC.$

## Bài tập
## Bài 1: Cho tứ giác $ABCD$ có hai đường chéo cắt nhau tại $O$ thoả mãn $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \vec 0.$ Chứng minh tứ giác $ABCD$ là hình bình hành.

## Bài 2: Cho tam giác $ABC$ có $BB’$, $CC’$ là các trung tuyến, $A’$ là điểm trên $BC$ thoả mãn $\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} = \vec 0.$ Chứng minh $AA’$ cũng là trung tuyến của tam giác $ABC.$

## Bài 3: Cho tam giác $ABC$ có $A’$, $B’$, $C’$ là các điểm thay đổi trên $BC$, $CA$, $AB$ sao cho $AA’$, $BB’$, $CC’$ đồng quy và thoả mãn $\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} = \vec 0.$ Chứng minh $AA’$, $BB’$, $CC’$ là các trung tuyến của tam giác $ABC.$

## Bài 4: Cho bốn điểm $A$, $B$, $C$, $D$, $I$ là trung điểm $AB$ và $J$ thuộc $CD$ thoả mãn $\overrightarrow {AD} + \overrightarrow {BC} = 2\overrightarrow {IJ} .$ Chứng minh $J$ là trung điểm của $CD.$

## Bài 5: Cho tứ giác $ABCD.$ Giả sử tồn tại điểm $O$ sao cho $OA = OB = OC = OD$ và $\overrightarrow {OA} + \overrightarrow {OB} + \overrightarrow {OC} + \overrightarrow {OD} = \vec 0.$ Chứng minh rằng $ABCD$ là hình chữ nhật.

## Bài 6: Cho tam giác $ABC$ nội tiếp đường tròn tâm $O$, gọi $G$ là trọng tâm tam giác $ABC.$ $A’$, $B’$, $C’$ là các điểm thỏa mãn: $\overrightarrow {OA} = 3\overrightarrow {OA’}$, $\overrightarrow {OB} = 3\overrightarrow {OB’}$, $\overrightarrow {OC} = 3\overrightarrow {OC’} .$ Chứng minh rằng $G$ là trực tâm tam giác $A’B’C’.$

## Bài 7: Cho tam giác $ABC$ nội tiếp đường tròn tâm $O$, gọi $H$ là trực tâm tam giác. $A’$, $B’$, $C’$ là các điểm thỏa mãn: $\overrightarrow {OA’} = 3\overrightarrow {OA}$, $\overrightarrow {OB’} = 3\overrightarrow {OB}$, $\overrightarrow {OC’} = 3\overrightarrow {OC} .$ Chứng minh rằng $H$ là trọng tâm tam giác $A’B’C’.$

## Bài 8: Cho tam giác $ABC$ và điểm $M$ nằm trong tam giác. Đường thẳng $AM$ cắt $BC$ tại $D$, $BM$ cắt $CA$ tại $E$ và $CM$ cắt $AB$ tại $F.$ Chứng minh rằng nếu $\overrightarrow {AD} + \overrightarrow {BE} + \overrightarrow {CF} = \vec 0$ thì $M$ là trọng tâm tam giác $ABC.$

DẠNG TOÁN 8: CHỨNG MINH BẤT ĐẲNG THỨC VÀ TÌM CỰC TRỊ LIÊN QUAN ĐẾN ĐỘ DÀI VECTƠ.

1. PHƯƠNG PHÁP

Sử dụng bất đẳng thức cơ bản: Với mọi vectơ $\vec a$, $\vec b$ ta luôn có:

+ $|\vec a + \vec b| \le |\vec a| + |\vec b|$, dấu bằng xảy ra khi $\vec a$, $\vec b$ cùng hướng.

+ $|\vec a – \vec b| \ge |\vec a| – |\vec b|$, dấu bằng xảy ra khi $\vec a$, $\vec b$ ngược hướng.

Đưa bài toán ban đầu về bài toán tìm cực trị của $|\overrightarrow {MI} |$ với $M$ thay đổi.

+ Nếu $M$ là điểm thay đổi trên đường thẳng $\Delta$ khi đó $|\overrightarrow {MI} |$ đạt giá trị nhỏ nhất khi và chỉ khi $M$ là hình chiếu của $I$ lên $\Delta .$

+ Nếu $M$ là điểm thay đổi trên đường tròn $(O)$ khi đó $|\overrightarrow {MI} |$ đạt giá trị nhỏ nhất khi và chỉ khi $M$ là giao điểm của tia $OI$ với đường tròn, $|\overrightarrow {MI} |$ đạt giá trị lớn nhất khi và chỉ khi $M$ là giao điểm của tia $IO$ với đường tròn.

2. CÁC VÍ DỤ

<!-- chunk:25 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 1: Cho tam giác $ABC$ và đường thẳng $d.$ Tìm điểm $M$ thuộc đường thẳng $d$ để biểu thức sau đạt giá trị nhỏ nhất $T = |\overrightarrow {MA} + \overrightarrow {MB} – \overrightarrow {MC} |.$

Gọi $I$ là đỉnh thứ tư của hình bình hành $ACBI$ thì $\overrightarrow {IA} + \overrightarrow {IB} – \overrightarrow {IC} = \vec 0.$

Khi đó: $T = |(\overrightarrow {MI} + \overrightarrow {IA} ) + (\overrightarrow {MI} + \overrightarrow {IB} ) – (\overrightarrow {MI} + \overrightarrow {IC} )|$ $= |\overrightarrow {MI} + \overrightarrow {IA} + \overrightarrow {IB} – \overrightarrow {IC} | = |\overrightarrow {MI} |.$

Vậy $T$ đạt giá trị nhỏ nhất khi và chỉ khi $M$ là hình chiếu của $I$ lên đường thẳng $d.$

<!-- chunk:26 level:3 source:https://toanmath.com/2019/09/tich-cua-mot-vecto-voi-mot-so.html -->
## Ví dụ 2: Cho tam giác $ABC$ và $A’B’C’$ là các tam giác thay đổi, có trọng tâm $G$ và $G’$ cố định. Tìm giá trị nhỏ nhất của tổng $T = AA’ + BB’ + CC’.$

Vì $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0$ và $\overrightarrow {G’A’} + \overrightarrow {G’B’} + \overrightarrow {G’C’} = \overrightarrow 0$ nên:

$\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’}$ $= \overrightarrow {AG} + \overrightarrow {GG’} + \overrightarrow {G’A’}$ $+ \overrightarrow {BG} + \overrightarrow {GG’} + \overrightarrow {G’B’}$ $+ \overrightarrow {CG} + \overrightarrow {GG’} + \overrightarrow {G’C’} .$

$= 3\overrightarrow {GG’}$ $– (\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $+ \left( {\overrightarrow {G’A’} + \overrightarrow {G’B’} + \overrightarrow {G’C’} } \right)$ $= 3\overrightarrow {GG’} .$

Do đó:

$AA’ + BB’ + CC’$ $= \left| {\overrightarrow {AA’} } \right| + \left| {\overrightarrow {BB’} } \right| + \left| {\overrightarrow {CC’} } \right|$ $\ge \left| {\overrightarrow {AA’} + \overrightarrow {BB’} + \overrightarrow {CC’} } \right|$ $= 3\left| {\overrightarrow {GG’} } \right|$ $= 3GG’.$

Đẳng thức xảy ra khi và chỉ khi các vectơ $\overrightarrow {AA’}$, $\overrightarrow {BB’}$, $\overrightarrow {CC’}$ cùng hướng.

Vậy giá trị nhỏ nhất của $T$ là $3GG’.$

## Bài tập
## Bài 1: Cho tam giác $ABC$, đường thẳng $d$ và ba số $\alpha$, $\beta$, $\gamma$ sao cho $\alpha + \beta + \gamma \ne 0.$ Tìm điểm $M$ thuộc đường thẳng $d$ để biểu thức $T = |\alpha \overrightarrow {MA} + \beta \overrightarrow {MB} + \gamma \overrightarrow {MC} |$ đạt giá trị nhỏ nhất.

## Bài 2: Cho tam giác $ABC.$ Tìm điểm $M$ trên đường tròn $(C)$ ngoại tiếp tam giác $ABC$ sao cho $|\overrightarrow {MA} + \overrightarrow {MB} + \overrightarrow {MC} |$:

a) Đạt giá trị lớn nhất.

b) Đạt giá trị nhỏ nhất.

## Bài 3: Cho tam giác $ABC.$ $M$, $N$, $P$ lần lượt là các điểm trên các cạnh $BC$, $CA$, $AB$ sao cho $\overrightarrow {BM} = k\overrightarrow {BC}$, $\overrightarrow {CN} = k\overrightarrow {CA}$, $\overrightarrow {AP} = k\overrightarrow {AB} .$ Chứng minh rằng các đoạn thẳng $AM$, $BN$, $CP$ là ba cạnh của một tam giác nào đó.

## Bài 4: Cho tam giác $ABC.$ Chứng minh rằng với mọi điểm $M$ thuộc cạnh $AB$ và không trùng với các đỉnh ta có: $MC.AB < MA.BC + MB.AC.$

## Bài 5: Cho tứ giác $ABCD$, $M$ là điểm thuộc đoạn $CD.$ Gọi $p$, ${p_1}$, ${p_2}$ lần lượt là chu vi của các tam giác $AMB$, $ACB$, $ADB.$ Chứng minh rằng $p < \max \left\{ {{p_1};{p_2}} \right\}.$

## Bài 6: Trên đường tròn tâm $O$ bán kính bằng $1$ lấy $2n+1$ điểm ${P_i}$, $i = 1,2, \ldots ,2n + 1$ $(n \in N)$ ở cùng phía với đối với đường kính nào đó. Chứng minh rằng $\left| {\sum\limits_{i = 1}^{2n + 1} {\overrightarrow {O{P_i}} } } \right| \ge 1.$