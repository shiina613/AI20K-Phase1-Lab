# Một số ứng dụng của tích vô hướng

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
Tích vô hướng có rất nhiều ứng dụng trong giải toán, bài viết giúp chúng ta tiếp cận những ứng dụng của tích vô hướng trong giải các bài toán hình học.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## I. CHỨNG MINH TÍNH VUÔNG GÓC VÀ THIẾT LẬP ĐIỀU KIỆN VUÔNG GÓC

1. PHƯƠNG PHÁP GIẢI

Sử dụng điều kiện $\vec a \bot \vec b$ $\Leftrightarrow \vec a.\vec b = 0.$

Chú ý: Ta có $AB \bot CD$ $\Leftrightarrow \overrightarrow {AB} .\overrightarrow {CD} = 0$, để chứng minh $\overrightarrow {AB} .\overrightarrow {CD} = 0$ thông thường chúng ta phân tích $\overrightarrow {AB}$, $\overrightarrow {CD}$ qua hai vectơ không cùng phương.

2. CÁC VÍ DỤ

<!-- chunk:2 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 1: Cho tứ giác $ABCD.$ Chứng minh rằng hai đường chéo $AC$ và $BD$ vuông góc với nhau khi và chỉ khi $A{B^2} + C{D^2} = B{C^2} + A{D^2}.$

Ta có $A{B^2} + C{D^2} – B{C^2} – A{D^2}.$

$= {(\overrightarrow {CB} – \overrightarrow {CA} )^2}$ $+ C{D^2} – B{C^2}$ $– {(\overrightarrow {CD} – \overrightarrow {CA} )^2}.$

$= – 2\overrightarrow {CB} .\overrightarrow {CA} + 2\overrightarrow {CD} .\overrightarrow {CA}$ $= 2\overrightarrow {CA} (\overrightarrow {CD} – \overrightarrow {CB} ).$

$= 2\overrightarrow {CA} .\overrightarrow {BD} .$

Do đó đường chéo $AC$ và $BD$ vuông góc với nhau khi và chỉ khi: $\overrightarrow {CA} .\overrightarrow {BD} = 0$ $\Leftrightarrow A{B^2} + C{D^2} = B{C^2} + A{D^2}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 2: Cho hình vuông $ABCD$ cạnh $a.$ Gọi $M$, $N$ thuộc cạnh $AB$ và $AD$ sao cho $AM = DN = x.$

a) Chứng minh rằng $CN$ vuông góc với $DM.$

b) Giả sử $P$ là điểm được xác định bởi $\overrightarrow {BP} = y\overrightarrow {BC}$, tìm hệ thức liên hệ của $x$, $y$ và $a$ để $MN$ vuông góc với $MP.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-1.png" alt="">

a) Ta có: $\overrightarrow {DN} = – \frac{x}{a}\overrightarrow {AD}$, $\overrightarrow {AM} = \frac{x}{a}\overrightarrow {AB} .$

Suy ra: $\overrightarrow {CN} = \overrightarrow {CD} + \overrightarrow {DN}$ $= – \overrightarrow {AB} – \frac{x}{a}\overrightarrow {AD}$ và $\overrightarrow {DM} = \overrightarrow {DA} + \overrightarrow {AM}$ $= \frac{x}{a}\overrightarrow {AB} – \overrightarrow {AD} .$

Suy ra: $\overrightarrow {DM} .\overrightarrow {CN}$ $= \left( {\frac{x}{a}\overrightarrow {AB} – \overrightarrow {AD} } \right)\left( { – \overrightarrow {AB} – \frac{x}{a}\overrightarrow {AD} } \right).$

$= – \frac{x}{a}{\overrightarrow {AB} ^2} + \frac{x}{a}{\overrightarrow {AD} ^2}$ $– \frac{{{x^2}}}{{{a^2}}}\overrightarrow {AB} .\overrightarrow {AD} + \overrightarrow {AB} .\overrightarrow {AD} .$

Vì $ABCD$ là hình vuông nên $\overrightarrow {AB} .\overrightarrow {AD} = 0.$

Do đó $\overrightarrow {DM} .\overrightarrow {CN}$ $= – ax + ax = 0.$

Vậy $CN$ vuông góc với $DM.$

b) Ta có $\overrightarrow {MN} = \overrightarrow {AN} – \overrightarrow {AM}$ $= \frac{{a – x}}{a}\overrightarrow {AB} – \frac{x}{a}\overrightarrow {AD}$, $\overrightarrow {MP} = \overrightarrow {MB} + \overrightarrow {BP}$ $= \frac{{a – x}}{a}\overrightarrow {AB} + y\overrightarrow {AD} .$

Suy ra $MN \bot MP$ $\Leftrightarrow \overrightarrow {MN} .\overrightarrow {MP} = 0.$

$\Leftrightarrow \left( {\frac{{a – x}}{a}\overrightarrow {AB} – \frac{x}{a}\overrightarrow {AD} } \right)\left( {\frac{{a – x}}{a}\overrightarrow {AB} + y\overrightarrow {AD} } \right) = 0.$

$\Leftrightarrow \frac{{{{(a – x)}^2}}}{{{a^2}}}.{\overrightarrow {AB} ^2} – \frac{x}{a}.y.{\overrightarrow {AD} ^2} = 0$ $\Leftrightarrow {(a – x)^2} = axy.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 3: Cho tam giác đều $ABC.$ Lấy các điểm $M$, $N$ thỏa mãn $\overrightarrow {BM} = \frac{1}{3}\overrightarrow {BC}$, $\overrightarrow {AN} = \frac{1}{3}\overrightarrow {AB} .$ Gọi $I$ là giao điểm của $AM$ và $CN.$ Chứng minh rằng $BI \bot IC.$

Giả sử $\overrightarrow {AI} = k\overrightarrow {AM} .$ Ta có:

$\overrightarrow {CI} = \overrightarrow {AI} – \overrightarrow {AC}$ $= k\overrightarrow {AM} – \overrightarrow {AC}$ $= k(\overrightarrow {AB} + \overrightarrow {BM} ) – \overrightarrow {AC}$ $= k\left( {\overrightarrow {AB} + \frac{1}{3}\overrightarrow {BC} } \right) – \overrightarrow {AC} .$

Hay $\overrightarrow {CI} = k\left( {\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} – \frac{1}{3}\overrightarrow {AB} } \right) – \overrightarrow {AC}$ $= \frac{{2k}}{3}\overrightarrow {AB} + \left( {\frac{k}{3} – 1} \right)\overrightarrow {AC} .$

Mặt khác $\overrightarrow {CN} = \overrightarrow {AN} – \overrightarrow {AC}$ $= \frac{1}{3}\overrightarrow {AB} – \overrightarrow {AC} .$

Vì $\overrightarrow {CI}$, $\overrightarrow {CN}$ cùng phương nên $2k = 1 – \frac{k}{3}$ $\Rightarrow k = \frac{3}{7}.$

$\overrightarrow {AI} = \frac{3}{7}\overrightarrow {AM}$ $= \frac{3}{7}(\overrightarrow {AB} + \overrightarrow {BM} )$ $= \frac{3}{7}\left( {\overrightarrow {AB} + \frac{1}{3}\overrightarrow {AC} – \frac{1}{3}\overrightarrow {AB} } \right)$ $= \frac{2}{7}\overrightarrow {AB} + \frac{1}{7}\overrightarrow {AC} .$

Suy ra $\overrightarrow {BI} = \overrightarrow {AI} – \overrightarrow {AB}$ $= \frac{2}{7}\overrightarrow {AB} + \frac{1}{7}\overrightarrow {AC} – \overrightarrow {AB}$ $= – \frac{5}{7}\overrightarrow {AB} + \frac{1}{7}\overrightarrow {AC} .$

$\overrightarrow {IC} = \overrightarrow {AC} – \overrightarrow {AI}$ $= \overrightarrow {AC} – \left( {\frac{2}{7}\overrightarrow {AB} + \frac{1}{7}\overrightarrow {AC} } \right)$ $= – \frac{2}{7}\overrightarrow {AB} + \frac{6}{7}\overrightarrow {AC} .$

Do đó $\overrightarrow {BI} .\overrightarrow {IC}$ $= \left( { – \frac{5}{7}\overrightarrow {AB} + \frac{1}{7}\overrightarrow {AC} } \right)\left( { – \frac{2}{7}\overrightarrow {AB} + \frac{6}{7}\overrightarrow {AC} } \right)$ $= \frac{1}{{49}}\left( {10{{\overrightarrow {AB} }^2} + 6{{\overrightarrow {AC} }^2} – 32\overrightarrow {AB} .\overrightarrow {AC} } \right).$

Vì tam giác $ABC$ đều nên $AB = AC$, $\overrightarrow {AB} .\overrightarrow {AC} = AB.AC.\cos A$ $= \frac{1}{2}A{B^2}.$

Suy ra $\overrightarrow {BI} .\overrightarrow {IC} = 0.$

Vậy $BI \bot IC.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 4: Cho tam giác $ABC$ cân tại $A.$ Gọi $M$ là trung điểm $AB$, $G$ là trọng tâm tam giác $ACM$, $I$ là tâm đường tròn ngoại tiếp tam giác $ABC.$ Chứng minh rằng $GI$ vuông góc với $CM.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-2.png" alt="">

Đặt $\overrightarrow {AB} = \overrightarrow x$, $\overrightarrow {AC} = \overrightarrow y$ và $AB = AC = a.$ Ta có:

$\overrightarrow {CM} = \overrightarrow {AM} – \overrightarrow {AC}$ $= \frac{1}{2}\overrightarrow {AB} – \overrightarrow {AC}$ $= \frac{1}{2}\vec x – \overrightarrow y$ $(1).$

Gọi $J$ là trung điểm $CM$, ta có:

$\overrightarrow {AG} = \frac{2}{3}\overrightarrow {AJ}$ $= \frac{1}{3}(\overrightarrow {AM} + \overrightarrow {AC} )$ $= \frac{1}{3}\left( {\frac{1}{2}\overrightarrow {AB} + \overrightarrow {AC} } \right)$ $= \frac{1}{6}\overrightarrow x + \frac{1}{3}\overrightarrow y .$

Mặt khác:

$$
\left\{ {\begin{array}{l}
{IA = IB}\\
{IA = IC}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{I{A^2} = I{B^2}}\\
{I{A^2} = I{C^2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{I{A^2} = {{(\overrightarrow {IA} + \overrightarrow {AB} )}^2}}\\
{I{A^2} = {{(\overrightarrow {IA} + \overrightarrow {AC} )}^2}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\overrightarrow {AI} .\overrightarrow x = \frac{{{a^2}}}{2}}\\
{\overrightarrow {AI} .\vec y = \frac{{{a^2}}}{2}}
\end{array}} \right.
$$
 $(2).$

Từ $(1)$ và $(2)$ ta có:

$\overrightarrow {CM} .\overrightarrow {GI}$ $= \overrightarrow {CM} .(\overrightarrow {AI} – \overrightarrow {AG} )$ $= \left( {\frac{1}{2}\overrightarrow x – \overrightarrow y } \right)\left( {\overrightarrow {AI} – \frac{1}{6}\overrightarrow x – \frac{1}{3}\overrightarrow y } \right).$

$= \frac{1}{2}\vec x.\overrightarrow {AI} – \vec y.\overrightarrow {AI}$ $– \frac{1}{{12}}{x^2} + \frac{1}{6}\vec x.\vec y$ $– \frac{1}{6}\vec x.\vec y + \frac{1}{3}{y^2}.$

$= \frac{{{a^2}}}{4} – \frac{{{a^2}}}{2} – \frac{{{a^2}}}{{12}} + \frac{{{a^2}}}{3} = 0.$

Suy ra $GI$ vuông góc với $CM.$

## Bài tập
## Bài 1: Cho bốn điểm $A$, $B$, $C$, $D$ thỏa mãn hệ thức $A{C^2} + B{D^2} = A{D^2} + B{C^2}.$ Chứng minh rằng $AB \bot CD.$

## Bài 2: Cho hình vuông $ABCD$, $M$ là điểm nằm trên đoạn thẳng $AC$ sao cho $AM = \frac{{AC}}{4}$, $N$ là trung điểm của đoạn thẳng $DC.$ Chứng minh rằng $BMN$ là tam giác vuông cân.

## Bài 3: Cho tam giác $ABC$ vuông cân tại đỉnh $A.$ Trên các cạnh $AB$, $BC$, $CA$ ta lấy các điểm $M$, $N$, $E$ sao cho $\frac{{AM}}{{MB}} = \frac{{BN}}{{NC}} = \frac{{CE}}{{EA}}.$ Chứng minh rằng $AN \bot ME.$

## Bài 4: Cho tam giác đều $ABC$, độ dài cạnh là $3a.$ Lấy $M$, $N$, $P$ lần lượt nằm trên các cạnh $BC$, $CA$, $AB$ sao cho $BM = a$, $CN = 2a$, $AP = x.$ Tính $x$ để $AM$ vuông góc với $PN.$

## Bài 5: Cho hình chữ nhật $ABCD.$ Kẻ $BK \bot AC.$ Gọi $M$, $N$ lần lượt là trung điểm của $AK$ và $CD.$ Chứng minh rằng $\widehat {BMN} = {90^0}.$

## Bài 6: Cho hình thang vuông $ABCD$ có đường cao $AB = 2a$, đáy lớn $BC = 3a$, đáy nhỏ $AD = a.$ $I$ là trung điểm của $CD.$ Chứng minh rằng $AI \bot BD.$

## Bài 7: Cho tứ giác lồi $ABCD$, hai đường chéo $AC$ và $BD$ cắt nhau tại $O.$ Gọi $H$ và $K$ lần lượt là trực tâm các tam giác $ABO$ và $CDO.$ Và $I$, $J$ lần lượt là trung điểm $AD$ và $BC.$ Chứng minh rằng $HK$ vuông góc với $IJ.$

## Bài 8: Cho tam giác $ABC$ cân tại $A.$ Gọi $H$ là trung điểm của $BC.$ $D$ là hình chiếu của $H$ lên $AC$, $M$ là trung điểm của $HD.$ Chứng minh rằng $AM$ vuông góc với $DB.$

## Bài 9: Cho tam giác $ABC$ không cân. Đường tròn tâm $I$ nội tiếp tam giác $ABC$ tiếp xúc các cạnh $BC$, $CA$, $AB$ tương ứng tại $A’$, $B’$ và $C’.$ Gọi $P$ là giao điểm của $BC$ với $B’C’.$ Chứng minh rằng $IP$ vuông góc $AA’.$

## Bài 10: Cho tam giác $ABC$ có $AB = 4$, $AC = 8$ và $\widehat A = {60^0}.$ Lấy điểm $E$ trên tia $AC$ và đặt $\overrightarrow {AE} = k\overrightarrow {AC} .$ Tìm $k$ để $BE$ vuông góc với trung tuyến $AF$ của tam giác $ABC.$

## Bài 11: Cho tam giác $ABC$ có $BC = a$, $CA = b$, $AB = c$ và $G$ là trọng tâm, $I$ là tâm đường tròn nội tiếp. Tìm điều kiện của $a$, $b$, $c$ để $IG$ vuông góc với $IC.$

## Bài 12: Tứ giác $ABCD$ có hai đường chéo $AC$ và $BD$ vuông góc với nhau tại $M$, $P$ là trung điểm của đoạn thẳng $AD.$ Chứng minh rằng: $MP \bot BC$ $\Leftrightarrow \overrightarrow {MA} .\overrightarrow {MC} = \overrightarrow {MD} .\overrightarrow {MB} .$

## Bài 13: Cho tam giác $ABC$ có ba đường cao $AD$, $BE$, $CF$ cắt nhau tại $H.$ Qua $A$ vẽ các đường thẳng song song với $BE$, $CF$ lần lượt cắt các đường thẳng $CF$, $BE$ tại $P$ và $Q.$ Chứng minh rằng $PQ$ vuông góc với trung tuyến $AM$ của tam giác $ABC.$

<!-- chunk:6 level:1 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## II. CHỨNG MINH BẤT ĐẲNG THỨC VÀ TÌM CỰC TRỊ BIỂU THỨC HÌNH HỌC

1. PHƯƠNG PHÁP GIẢI

Sử dụng các bất đẳng thức:

Cho $\vec a$, $\vec b$ bất kì. Khi đó ta có:

+ $\vec a.\vec b \le |\vec a|.|\vec b|$, dấu bằng xảy ra khi và chỉ khi $\cos (\vec a,\vec b) = 1$ hay $\vec a$, $\vec b$ cùng hướng.

+ $\vec a.\vec b \ge – |\vec a|.|\vec b|$, dấu bằng xảy ra khi và chỉ khi $\cos (\vec a,\vec b) = – 1$ hay $\vec a$, $\vec b$ ngược hướng.

${\vec u^2} \ge 0$, dấu bằng xảy ra khi và chỉ khi $\overrightarrow u = \vec 0.$

Bất đẳng thức cổ điển (Cauchy, Bunhiacopxki …).

2. CÁC VÍ DỤ

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 1: Cho tam giác $ABC$ có trọng tâm $G$ và $M$ là một điểm bất kỳ. Chứng minh rằng: $M{A^2} + M{B^2} + M{C^2}$ $\ge MA.GA + MB.GB + MC.GC$ $\ge G{A^2} + G{B^2} + G{C^2}.$

Ta có $\overrightarrow {MA} .\overrightarrow {MG}$ $= MA.MG.\cos (\overrightarrow {MA} ;\overrightarrow {MG} )$ $\le MA.MG.$

Tương tự $MB.GB \ge \overrightarrow {MB} .\overrightarrow {GB}$, $MC.GC \ge \overrightarrow {MC} .\overrightarrow {GC} .$

Suy ra $MA.GA + MB.GB + MC.GC$ $\ge \overrightarrow {MA} .\overrightarrow {GA} + \overrightarrow {MB} .\overrightarrow {GB} + \overrightarrow {MC} .\overrightarrow {GC} .$

Mặt khác:

$\overrightarrow {MA} .\overrightarrow {GA} + \overrightarrow {MB} .\overrightarrow {GB} + \overrightarrow {MC} .\overrightarrow {GC}$ $= (\overrightarrow {MG} + \overrightarrow {GA} )\overrightarrow {GA}$ $+ (\overrightarrow {MG} + \overrightarrow {GB} )\overrightarrow {GB}$ $+ (\overrightarrow {MG} + \overrightarrow {GC} )\overrightarrow {GC} .$

$= \overrightarrow {MG} (\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $+ G{A^2} + G{B^2} + G{C^2}$ $= G{A^2} + G{B^2} + G{C^2}.$

Suy ra $MA.GA + MB.GB + MC.GC$ $\ge G{A^2} + G{B^2} + G{C^2}$ $(*).$

Theo bất đẳng thức Cauchy ta có:

$M{A^2} + M{B^2} + M{C^2}$ $+ G{A^2} + G{B^2} + G{C^2}$ $\ge 2MA.GA + 2MB.GB + 2MC.GC.$

Kết hợp $(*)$ suy ra:

$M{A^2} + M{B^2} + M{C^2}$ $+ G{A^2} + G{B^2} + G{C^2}$ $\ge MA.GA + MB.GB + MC.GC$ $+ G{A^2} + G{B^2} + G{C^2}.$

Hay $M{A^2} + M{B^2} + M{C^2}$ $\ge MA.GA + MB.GB + MC.GC.$

Vậy ta có điều phải chứng minh.

Nhận xét:

Ta có: $GA = \frac{2}{3}{m_a}$, $GB = \frac{2}{3}{m_b}$, $GC = \frac{2}{3}{m_c}.$

$\Rightarrow G{A^2} + G{B^2} + G{C^2}$ $= \frac{4}{9}\left( {m_a^2 + m_b^2 + m_c^2} \right)$ $= \frac{1}{3}\left( {{a^2} + {b^2} + {c^2}} \right).$

Suy ra với mọi điểm $M$ thì:

${m_a}.MA + {m_b}.MB + {m_c}.MC$ $\ge \frac{1}{2}\left( {{a^2} + {b^2} + {c^2}} \right).$

$3\left( {M{A^2} + M{B^2} + M{C^2}} \right)$ $\ge {a^2} + {b^2} + {c^2}.$

$3\left( {M{A^2} + M{B^2} + M{C^2}} \right)$ $\ge 2\left( {{m_a}.MA + {m_b}.MB + {m_c}.MC} \right).$

Đặc biệt:

Với $M \equiv O$ tâm đường tròn ngoại tiếp tam giác, ta có:

$O{A^2} + O{B^2} + O{C^2}$ $\ge OA.GA + OB.GB + OC.GC$ $\ge G{A^2} + G{B^2} + G{C^2}.$

Mặt khác ta có $OA = OB = OC = R$, ta có:

$R(GA + GB + GC) \le 3{R^2}$ hay ${m_a} + {m_b} + {m_c} \le \frac{9}{2}R$ suy ra $\frac{1}{{{m_a}}} + \frac{1}{{{m_b}}} + \frac{1}{{{m_c}}} \ge \frac{2}{R}.$

$R(GA + GB + GC)$ $\ge G{A^2} + G{B^2} + G{C^2}$ hay $\frac{{m_a^2 + m_b^2 + m_c^2}}{{{m_a} + {m_b} + {m_c}}} \le \frac{{3R}}{2}.$

$3{R^2} \ge G{A^2} + G{B^2} + G{C^2}$ hay $m_a^2 + m_b^2 + m_c^2 \le \frac{{27}}{4}{R^2}$, $9{R^2} \ge {a^2} + {b^2} + {c^2}.$

Với $M \equiv I$, tâm đường tròn nội tiếp tam giác, ta có:

$IA.GA + IB.GB + IC.GC$ $\ge G{A^2} + G{B^2} + G{C^2}.$

Mặt khác $IA = \frac{r}{{\sin \frac{A}{2}}}$, $IB = \frac{r}{{\sin \frac{B}{2}}}$, $IC = \frac{r}{{\sin \frac{C}{2}}}$ do đó ta có:

$\frac{{{m_a}}}{{\sin \frac{A}{2}}} + \frac{{{m_b}}}{{\sin \frac{B}{2}}} + \frac{{{m_c}}}{{\sin \frac{C}{2}}}$ $\ge \frac{{{a^2} + {b^2} + {c^2}}}{{2r}}.$

Với $M \equiv H$ ta được $3\left( {H{A^2} + H{B^2} + H{C^2}} \right)$ $\ge {a^2} + {b^2} + {c^2}.$

Xét tam giác $ABC$ nhọn khi đó ta có:

$HC = \frac{{CA’}}{{\sin CHA’}} = \frac{{CA’}}{{\sin B}}$ $= \frac{{AC.\cos C}}{{\sin B}} = 2R\cos C.$

Tương tự ta cũng có: $HB = 2R\cos B$, $HC = 2R\cos C.$

Do đó ${\cos ^2}A + {\cos ^2}B + {\cos ^2}C \ge {\left( {\frac{p}{{3R}}} \right)^2}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 2: Cho tam giác $ABC$ và điểm $M$ bất kỳ. Chứng minh rằng $\cos \frac{A}{2}.MA + \cos \frac{B}{2}.MB + \cos \frac{C}{2}.MC$ $\ge \frac{{a + b + c}}{2}.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-3.png" alt="">

Gọi $I$ là tâm đường tròn nội tiếp tam giác $ABC.$

Ta có: $a.\overrightarrow {IA} + b.\overrightarrow {IB} + c.\overrightarrow {IC} = \vec 0.$

$\Rightarrow \frac{{\cos \frac{A}{2}}}{{IA}}\overrightarrow {IA} + \frac{{\cos \frac{B}{2}}}{{IB}}\overrightarrow {IB} + \frac{{\cos \frac{C}{2}}}{{IC}}\overrightarrow {IC} = \vec 0.$

Vì $\cos \frac{A}{2}.MA = \frac{{\cos \frac{A}{2}}}{{IA}}.MA.IA$ $\ge \frac{{\cos \frac{A}{2}}}{{IA}}.\overrightarrow {MA} .\overrightarrow {IA} .$

Tương tự ta có $\cos \frac{B}{2}.MB \ge \frac{{\cos \frac{B}{2}}}{{IB}}.\overrightarrow {MB} .\overrightarrow {IB}$ và $\cos \frac{C}{2}.MC \ge \frac{{\cos \frac{C}{2}}}{{IC}}.\overrightarrow {MC} .\overrightarrow {IC} .$

Mà $\frac{{\cos \frac{A}{2}}}{{IA}}.\overrightarrow {MA} .\overrightarrow {IA}$ $+ \frac{{\cos \frac{B}{2}}}{{IB}}.\overrightarrow {MB} .\overrightarrow {IB}$ $+ \frac{{\cos \frac{C}{2}}}{{IC}}.\overrightarrow {MC} .\overrightarrow {IC} .$

$= \overrightarrow {MI} \left( {\frac{{\cos \frac{A}{2}}}{{IA}}\overrightarrow {IA} + \frac{{\cos \frac{B}{2}}}{{IB}}\overrightarrow {IB} + \frac{{\cos \frac{C}{2}}}{{IC}}\overrightarrow {IC} } \right)$ $+ \cos \frac{A}{2}.IA + \cos \frac{B}{2}.IB + \cos \frac{C}{2}.IC.$

$= \cos \frac{A}{2}.IA + \cos \frac{B}{2}.IB + \cos \frac{C}{2}.IC$ $= AE + BF + CD$ $= \frac{{a + b + c}}{2}.$

Do đó $\cos \frac{A}{2}.MA + \cos \frac{B}{2}.MB + \cos \frac{C}{2}.MC$ $\ge \frac{{a + b + c}}{2}.$

Tổng quát: Cho đa giác lồi ${A_1}{A_2} \ldots {A_n}$ $(n \ge 3)$ ngoại tiếp đường tròn tâm $J.$ Chứng minh rằng với điểm $M$ bất kỳ thì $\sum\limits_{i = 1}^n {\cos } \frac{{{A_i}}}{2}.\left( {M{A_i} – J{A_i}} \right) \ge 0.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 3: Cho tam giác $ABC$ với $G$ là trọng tâm. Qua điểm $O$ bất kỳ nằm trong tam giác kẻ đường thẳng song song với $GA$, $GB$, $GC$ tương ứng cắt $CA$, $AB$, $BC$ tại các điểm $A’$, $B’$, $C’.$ Xác định vị trí điểm $M$ để ${m_a}MA’ + {m_b}MB’ + {m_c}MC’$ đạt giá trị nhỏ nhất.

Ta có ${m_a}.MA’ = \frac{3}{2}GA.MA’$ $\ge \frac{3}{2}\overrightarrow {GA} .\overrightarrow {MA’}$ $= \frac{3}{2}\overrightarrow {GA} .(\overrightarrow {MO} + \overrightarrow {OA’} ).$

Tương tự ${m_b}.MB’ \ge \frac{3}{2}\overrightarrow {GB} .\left( {\overrightarrow {MO} + \overrightarrow {OB’} } \right)$, ${m_c}.MC’ \ge \frac{3}{2}\overrightarrow {GC} .(\overrightarrow {MO} + \overrightarrow {OC’} ).$

Suy ra:

${m_a}MA’ + {m_b}MB’ + {m_c}MC’$ $\ge \frac{3}{2}(\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $+ \frac{3}{2}\left( {\overrightarrow {GA} .\overrightarrow {OA’} + \overrightarrow {GB} .\overrightarrow {OB’} + \overrightarrow {GC} .\overrightarrow {OC’} } \right).$

Hay ${m_a}.MA’ + {m_b}.MB’ + {m_c}.MC’$ $\ge {m_a}OA’ + {m_b}OB’ + {m_c}OC’.$

Dấu bằng xảy ra khi và chỉ khi $M$ trùng với $O.$

Vậy với $M$ trùng với $O$ thì ${m_a}MA’ + {m_b}MB’ + {m_c}MC’$ đạt giá trị nhỏ nhất.

<!-- chunk:10 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 4: Cho tam giác $ABC$ và ba số thực $x$, $y$, $z.$ Chứng minh rằng ${x^2} + {y^2} + {z^2}$ $\ge 2yz\cos A + 2zx\cos B + 2xy\cos C.$

Gọi $(I;r)$ là đường tròn nội tiếp tam giác $ABC$, tiếp xúc với các cạnh $BC$, $CA$, $AB$ lần lượt tại $M$, $N$, $P.$

Khi đó ${(x.\overrightarrow {IM} + y.\overrightarrow {IN} + z.\overrightarrow {IP} )^2} \ge 0.$

$\Leftrightarrow {x^2}.I{M^2} + {y^2}.I{N^2} + {z^2}.I{P^2}$ $+ 2xy\overrightarrow {IM} .\overrightarrow {IN} + 2yz\overrightarrow {IN} .\overrightarrow {IP} + 2zx\overrightarrow {IP} .\overrightarrow {IM} \ge 0.$

$\Leftrightarrow \left( {{x^2} + {y^2} + {z^2}} \right){r^2}$ $+ 2{r^2}\left[ {xy\cos \left( {{{180}^0} – C} \right) + yz\cos \left( {{{180}^0} – A} \right) + zx\cos \left( {{{180}^0} – B} \right)} \right] \ge 0.$

$\Leftrightarrow {x^2} + {y^2} + {z^2}$ $\ge 2yz\cos A + 2zx\cos B + 2xy\cos C.$

Nhận xét:

+ Khi chọn $x = y = z = 1$ ta có: $\cos A + \cos B + \cos C \le \frac{3}{2}.$

+ Khi chọn $y = z = 1$ ta có $\cos A + x(\cos B + \cos C)$ $\le 1 + \frac{1}{2}{x^2}.$

## Bài tập
## Bài 1: Cho tam giác $ABC$ và ba số thực $x$, $y$, $z.$ Chứng minh rằng: $yz\cos 2A + zx\cos 2B + xy\cos 2C$ $\le – \frac{1}{2}\left( {{x^2} + {y^2} + {z^2}} \right).$

## Bài 2: Cho tam giác $ABC$ không đều nội tiếp đường tròn $(O).$ Tìm trên đường tròn điểm $M$ để có tổng bình phương khoảng cách từ đó đến ba đỉnh tam giác là nhỏ nhất, lớn nhất.

## Bài 3: Cho tam giác $ABC$ vuông tại $A.$ Gọi $\alpha$ là góc giữa hai trung tuyến $BD$ và $CK.$ Tìm giá trị nhỏ nhất của $\cos \alpha .$

## Bài 4: Cho $M$ là một điểm bất kì nằm trong mặt phẳng tam giác $ABC.$ Tìm giá trị nhỏ nhất của $T = \frac{{MA}}{a} + \frac{{MB}}{b} + \frac{{MC}}{c}.$

## Bài 5: Cho tam giác $ABC.$ Tìm điểm $M$ sao cho biểu thức sau đạt giá trị nhỏ nhất: $T = 2\cos \frac{A}{2}.MA + MB + MC.$

## Bài 6: Cho tam giác $ABC.$ Chứng minh rằng:

a) $am_a^2 + bm_b^2 + cm_c^2 \ge \frac{9}{4}abc.$

b) $a{m_b}{m_c} + b{m_c}{m_a} + c{m_a}{m_b} \ge \frac{9}{4}abc.$

c) $\frac{{m_a^2}}{a} + \frac{{m_b^2}}{b} + \frac{{m_c^2}}{c} \ge \frac{9}{4}.\frac{{{a^3} + {b^3} + {c^3}}}{{ab + bc + ca}}.$

## Bài 7: Cho tam giác $ABC.$ Chứng minh rằng:

a) ${a^2} + {b^2} + {c^2} \le 9{R^2}.$

b) $R \ge 2r.$

c) ${R^2} + {a^2} + {b^2} \ge {c^2}.$

d) $4S \le (ab + bc + ca)\sqrt {\frac{{abc}}{{{a^3} + {b^3} + {c^3}}}} .$

e) ${(a – b)^2} + {(b – c)^2} + {(c – a)^2}$ $\le 8R(R – 2r).$

## Bài 8: Cho tam giác $ABC$ nhọn. Tìm điểm $M$ sao cho $MA + 2MB + \sqrt 3 MC$ đạt giá trị nhỏ nhất.

## Bài 9: Cho đa giác lồi ${A_1}{A_2} \ldots {A_n}$ $(n \ge 3)$, $\overrightarrow {{e_i}}$ $(i = \overline {1,n} )$, $O$ là điểm bất kỳ nằm trong đa giác. Gọi ${B_i}$ là hình chiếu điểm $O$ lên ${A_i}{A_{i + 1}}.$ Chứng minh rằng với mọi điểm $M$ ta cό $\sum\limits_{i = 1}^n {{A_i}} {A_{i + 1}}\left( {M{B_i} – O{B_i}} \right) \ge 0.$

## Bài 10: Cho đa giác đều ${A_1}{A_2} \ldots {A_n}.$ Tìm điểm $M$ sao cho tổng $M{A_1} + M{A_2} + \ldots + M{A_n}$ nhỏ nhất.

## Bài 11: Cho tam giác $ABC$, $O$ là điểm trong tam giác, đặt $\widehat {BOC} = \alpha$, $\widehat {COA} = \beta$, $\widehat {AOB} = \gamma .$ Chứng minh rằng với mọi điểm $M$ ta có $MA\sin \alpha + MB\sin \beta + MC\sin \gamma$ $\ge OA\sin \alpha + OB\sin \beta + OC\sin \gamma .$

## Bài 12: Cho tam giác $ABC$, tìm vị trí điểm $M$ để $P = aM{A^2} + bM{B^2} + cM{C^2}$ đạt giá trị nhỏ nhất. Biết:

a) $M$ là điểm bất kì.

b) $M$ nằm trên đường tròn ngoại tiếp tam giác $ABC.$

c) $M$ nằm trên đường thẳng $d$ bất kỳ.

## Bài 13: Cho $n$ điểm ${A_1}{A_2} \ldots {A_n}$ và $n$ số dương ${\alpha _1}$, ${\alpha _2}$ … ${\alpha _n}$. $O$ là điểm thoả mãn $\sum\limits_{i = 1}^n {{\alpha _i}} \overrightarrow {O{A_i}} = \vec 0.$ Chứng minh rằng với mọi điểm $M$ ta có bất đẳng thức $\sum\limits_{i = 1}^n {{\alpha _i}} MA_i^2 \ge \sum\limits_{i = 1}^n {{\alpha _i}} O{A_i}.M{A_i} \ge \sum\limits_{i = 1}^n {{\alpha _i}} OA_i^2.$

## Bài 14: Cho tam giác $ABC$ vuông cân tại $A.$ Xác định điểm $M$ sao cho biểu thức sau đạt giá trị nhỏ nhất:

a) $\sqrt 2 MA + MB + MC.$

b) $2\sqrt 2 MA + \sqrt {10} (MB + MC).$

## Bài 15: Chứng minh rằng trong tam giác nhọn $ABC$ ta luôn có:

${\cos ^2}A + {\cos ^2}B + {\cos ^2}C$ $\ge 6\cos A.\cos B.\cos C.$

## Bài 16: Cho tam giác $ABC.$ Chứng minh rằng:

a) ${\sin ^2}A + {\sin ^2}B + {\sin ^2}C \le \frac{9}{4}.$

b) $\sin A + \sin B + \sin C \le \frac{{3\sqrt 3 }}{2}.$

c) $\sin A.\sin B.\sin C \le \frac{{3\sqrt 3 }}{8}.$

d) ${\cos ^2}\frac{A}{2} + {\cos ^2}\frac{B}{2} + {\cos ^2}\frac{C}{2} \le \frac{9}{4}.$

e) $\cos \frac{A}{2} + \cos \frac{B}{2} + \cos \frac{C}{2} \le \frac{{3\sqrt 3 }}{2}.$

f) $\cos \frac{A}{2}.\cos \frac{B}{2}.\cos \frac{C}{2} \le \frac{{3\sqrt 3 }}{8}.$

<!-- chunk:11 level:1 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## III. KHÁI NIỆM PHƯƠNG TÍCH CỦA MỘT ĐIỂM TỚI ĐƯỜNG TRÒN VÀ ỨNG DỤNG

1. PHƯƠNG PHÁP GIẢI

a) Bài toán: Cho đường tròn $(O;R)$ và điểm $M$ cố định. Một đường thẳng thay đổi đi qua $M$ cắt đường tròn tại hai điểm $A$, $B.$ Chứng minh rằng $\overrightarrow {MA} .\overrightarrow {MB} = M{O^2} – {R^2}.$

Chứng minh: Vẽ đường kính $BC$ của đường tròn $(O;R).$ Ta có $\overrightarrow {MA}$ là hình chiếu của $\overrightarrow {MC}$ lên đường thẳng $MB.$ Theo công thức hình chiếu ta có:

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-4.png" alt="">

$\overrightarrow {MA} .\overrightarrow {MB} = \overrightarrow {MC} .\overrightarrow {MB}$ $= (\overrightarrow {MO} + \overrightarrow {OC} ).(\overrightarrow {MO} + \overrightarrow {OB} )$ $= (\overrightarrow {MO} – \overrightarrow {OB} ).(\overrightarrow {MO} + \overrightarrow {OB} )$ $= M{O^2} – O{B^2}$ $= M{O^2} – {R^2}.$

Từ bài toán trên ta có định nghĩa sau:

b) Định nghĩa: Cho đường tròn $(O;R)$ và điểm $M$ cố định. Một đường thẳng thay đổi đi qua $M$ cắt đường tròn tại hai điểm $A$, $B.$ Khi đó $\overrightarrow {MA} .\overrightarrow {MB} = M{O^2} – {R^2}.$ là đại lượng không đổi được gọi là phương tích của điểm $M$ đối với đường tròn $(O;R)$, kí hiệu là ${P_{M/\left( O \right)}}.$

Chú ý: Nếu $M$ ở ngoài đường tròn, vẽ tiếp tuyến $MT.$ Khi đó: ${P_{M/(O)}} = M{T^2} = M{O^2} – {R^2}.$

c) Các tính chất

Cho hai đường thẳng $AB$ và $CD$ cắt nhau tại $M.$ Điều kiện cần và đủ để bốn điểm $A$, $B$, $C$, $D$ nội tiếp được đường tròn là:

$\overrightarrow {MA} .\overrightarrow {MB} = \overrightarrow {MC} .\overrightarrow {MD}$ (hay $\overline {MA} .\overline {MB} = \overline {MC} .\overline {MD}$).

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-5.png" alt="">

Cho đường thẳng $AB$ cắt đường thẳng $\Delta$ tại $M$ và điểm $C$ trên đường thẳng $\Delta$ $(C \ne M).$ Điều kiện cần và đủ để $\Delta$ là tiếp tuyến của đường tròn ngoại tiếp tam giác $ABC$ tại $C$ là $MA.MB = M{C^2}.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-6.png" alt="">

2. CÁC VÍ DỤ

<!-- chunk:12 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 1: Cho tam giác $ABC$ nhọn có các đường cao $AA’$, $BB’$, $CC’$ cắt nhau tại $H.$ Chứng minh rằng $HA.HA’ = HB.HB’ = HC.HC’.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-7.png" alt="">

Ta có $\widehat {BB’C} = \widehat {BC’C} = {90^0}$ suy ra tứ giác $BCB’C’$ nội tiếp trong đường tròn $(C)$ đường kính $BC.$ Do đó $HB.HB’ = HC.HC’$ (vì cùng bằng phương tích từ điểm $H$ tới đường tròn $(C)$) $(1).$

Tương tự tứ giác $ACA’C’$ nội tiếp được nên $HA.HA’ = HC.HC’$ $(2).$

Từ $(1)$ và $(2)$ suy ra $HA.HA’ = HB.HB’ = HC.HC’.$

<!-- chunk:13 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 2: Cho đường tròn $(O;R)$ và một điểm $P$ cố định ở bên trong đường tròn đó. Hai dây cung thay đổi $AB$ và $CD$ luôn đi qua điểm $P$ và vuông góc với nhau.

a) Chứng minh rằng $A{B^2} + C{D^2}$ không đổi.

b) Chứng minh rằng $P{A^2} + P{B^2} + P{C^2} + P{D^2}$ không phụ thuộc vị trí điểm $P.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-8.png" alt="">

a) Gọi $E$, $F$ theo thứ tự là trung điểm của $AB$, $CD$ suy ra $OE \bot AB$ và $OF \bot CD.$

Ta có $A{B^2} + C{D^2}$ $= {(2AE)^2} + {(2CF)^2}$ $= 4\left( {A{O^2} – O{E^2}} \right) + 4\left( {C{O^2} – O{F^2}} \right)$ $= 4\left[ {2{R^2} – \left( {O{E^2} + O{F^2}} \right)} \right]$ $= 4\left( {2{R^2} – O{P^2}} \right).$

Suy ra $A{B^2} + C{D^2}$ không đổi.

b) $P{A^2} + P{B^2} + P{C^2} + P{D^2}$ $= {(PA + PB)^2}$ $+ {(PC + PD)^2}$ $– 2PA.PB – 2PC.PD$ $= A{B^2} + C{D^2}$ $+ 2\overrightarrow {PA} .\overrightarrow {PB} + 2\overrightarrow {PC} .\overrightarrow {PD} .$

Mặt khác theo câu a ta có: $A{B^2} + C{D^2}$ $= 4\left( {2{R^2} – O{P^2}} \right)$ và ${P_{P/(O)}} = \overrightarrow {PA} .\overrightarrow {PB} = \overrightarrow {PC} .\overrightarrow {PD}$ $= P{O^2} – {R^2}.$

Suy ra $P{A^2} + P{B^2} + P{C^2} + P{D^2}$ $= 4\left( {2{R^2} – O{P^2}} \right) + 4\left( {P{O^2} – {R^2}} \right)$ $= 4{R^2}.$

Vậy $P{A^2} + P{B^2} + P{C^2} + P{D^2}$ không phụ thuộc vị trí điểm $P.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 3: Cho đường tròn đường kính $AB$ và đường thẳng $\Delta$ vuông góc với $AB$ ở $H$ ($H \ne A$, $H \ne B$). Một đường thẳng quay quanh $H$ cắt đường tròn ở $M$, $N$ và các đường thẳng $AM$, $AN$ lần lượt cắt $\Delta$ ở $M’$, $N’.$

a) Chứng minh rằng bốn điểm $M$, $N$, $M’$, $N’$ thuộc một đường tròn $(C)$ nào đó.

b) Chứng minh rằng các đường tròn $(C)$ luôn đi qua hai điểm cố định.

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-9.png" alt="">

a) Vì $\widehat {M’HB} = \widehat {M’MB} = {90^0}$ nên tứ giác $BHM’M$ nội tiếp được, suy ra: $\overrightarrow {AH} .\overrightarrow {AB} = \overrightarrow {AM’} .\overrightarrow {AM}$ $(1).$

Tương tự: Vì $\widehat {N’HB} = \widehat {N’NB} = {90^0}$ nên tứ giác $HBN’N$ nội tiếp được, suy ra: $\overrightarrow {AH} .\overrightarrow {AB} = \overrightarrow {AN’} .\overrightarrow {AN}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\overrightarrow {AM’} .\overrightarrow {AM} = \overrightarrow {AN’} .\overrightarrow {AN} .$

Suy ra bốn điểm $M$, $N$, $M’$, $N’$ thuộc một đường tròn.

b) Gọi $P$, $Q$ lần lượt là các giao điểm của đường tròn $(C)$ với đường thẳng $AB$ và $E$, $F$ lần lượt là giao điểm của $\Delta$ với đường tròn đường kính $AB.$

Khi đó ta có $\overrightarrow {AP} .\overrightarrow {AQ} = \overrightarrow {AM} .\overrightarrow {AM’} = \overrightarrow {AH} .\overrightarrow {AB} .$

Mặt khác:

$\overrightarrow {AH} .\overrightarrow {AB} = (\overrightarrow {AE} + \overrightarrow {EH} )\overrightarrow {AB}$ $= \overrightarrow {AE} .(\overrightarrow {AE} + \overrightarrow {EB} ) = A{E^2}$ và $\overrightarrow {AH} .\overrightarrow {AB} = (\overrightarrow {AF} + \overrightarrow {FH} )\overrightarrow {AB}$ $= \overrightarrow {AF} .(\overrightarrow {AF} + \overrightarrow {FB} ) = A{F^2}.$

Suy ra $\overrightarrow {AP} .\overrightarrow {AQ} = A{E^2} = A{F^2}.$

Do đó $P$, $Q$ thuộc đường tròn $(S)$ tiếp xúc với $AE$, $AF$ ở $E$, $F.$

Vì $(S)$ là đường tròn cố định nên $P$, $Q$ cố định thuộc đường tròn $(C).$

<!-- chunk:15 level:3 source:https://toanmath.com/2019/09/mot-so-ung-dung-cua-tich-vo-huong.html -->
## Ví dụ 4: Cho tam giác $ABC$ nội tiếp đường tròn $(O)$ bán kính $R.$ Giả sử $M$ là điểm di động trong đường tròn $(O).$ Nối $AM$, $BM$, $CM$ lần lượt cắt $(O)$ tại $A’$, $B’$, $C’.$ Tìm tập hợp điểm $M$ sao cho $\frac{{MA}}{{MA’}} + \frac{{MB}}{{MB’}} + \frac{{MC}}{{MC’}} = 3.$

<img link="data_for_rag/toan10/images/mot-so-ung-dung-cua-tich-vo-huong-10.png" alt="">

Ta có $\frac{{MA}}{{MA’}} + \frac{{MB}}{{MB’}} + \frac{{MC}}{{MC’}} = 3$ $\Leftrightarrow \frac{{M{A^2}}}{{MA’.MA}} + \frac{{M{B^2}}}{{MB’.MB}} + \frac{{M{C^2}}}{{MC’.MC}} = 3$ $\Leftrightarrow – \frac{{M{A^2}}}{{\overrightarrow {MA’} .\overrightarrow {MA} }} – \frac{{M{B^2}}}{{\overrightarrow {MB’} .\overrightarrow {MB} }} – \frac{{M{C^2}}}{{\overrightarrow {MC’} .\overrightarrow {MC} }} = 3$ $(*).$

Mặt khác:

${P_{M/(O)}} = \overrightarrow {MA’} .\overrightarrow {MA}$ $= \overrightarrow {MB’} .\overrightarrow {MB} = \overrightarrow {MC’} .\overrightarrow {MC}$ $= M{O^2} – {R^2}.$

Suy ra $(*) \Leftrightarrow M{A^2} + M{B^2} + M{C^2}$ $= – 3\left( {M{O^2} – {R^2}} \right)$ $(1).$

Gọi $G$ là trọng tâm tam giác $ABC$, $I$ là trung điểm $GO.$

Ta có:

$M{A^2} + M{B^2} + M{C^2}$ $= {(\overrightarrow {MG} + \overrightarrow {GA} )^2}$ $+ {(\overrightarrow {MG} + \overrightarrow {GB} )^2}$ $+ {(\overrightarrow {MG} + \overrightarrow {GC} )^2}$ $= 3M{G^2}$ $+ 2\overrightarrow {MG} (\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} )$ $+ G{A^2} + G{B^2} + G{C^2}$ $= 3M{G^2} + G{A^2} + G{B^2} + G{C^2}$ $(2).$

Từ $(1)$ và $(2)$ ta có $3M{G^2} + G{A^2} + G{B^2} + G{C^2}$ $= – 3\left( {M{O^2} – {R^2}} \right).$

$\Leftrightarrow M{G^2} + M{O^2}$ $= {R^2} – \frac{1}{3}\left( {G{A^2} + G{B^2} + G{C^2}} \right).$

$\Leftrightarrow {(\overrightarrow {MI} + \overrightarrow {IG} )^2} + {(\overrightarrow {MI} + \overrightarrow {IO} )^2}$ $= {R^2} – \frac{1}{3}\left( {G{A^2} + G{B^2} + G{C^2}} \right).$

$\Leftrightarrow 2M{I^2} + 2I{O^2}$ $= {R^2} – \frac{1}{3}\left( {G{A^2} + G{B^2} + G{C^2}} \right).$

$\Leftrightarrow M{I^2}$ $= \frac{1}{2}{R^2} – \frac{1}{6}\left( {G{A^2} + G{B^2} + G{C^2}} \right) – I{O^2}$ $\Leftrightarrow MI = k.$

Trong đó ${k^2}$ $= \frac{1}{2}{R^2} – \frac{1}{6}\left( {G{A^2} + G{B^2} + G{C^2}} \right) – I{O^2}.$

Vậy tập hợp điểm $M$ là đường tròn tâm $I$ bán kính $R = k.$

## Bài tập
## Bài 1: Trong đường tròn tâm $(O;R)$ cho hai dây cung $AA’$ và $BB’$ vuông góc với nhau tại $S.$ Gọi $M$ là trung điểm của $AB.$ Chứng minh rằng $SM \bot A’B’.$

## Bài 2: Cho hai đường tròn $(O)$ và $(O’)$, $AA’$, $BB’$ là các tiếp tuyến chung ngoài của chúng, đường thẳng $AB’$ theo thứ tự cắt $(O)$ và $(O’)$ tại $M$, $N.$ Chứng minh rằng $AM = B’N.$

## Bài 3: Cho tam giác $ABC$ không cân tại $A$, $AM$, $AD$ lần lượt là trung tuyến, phân giác của tam giác. Đường tròn ngoại tiếp tam giác $AMD$ cắt $AB$, $AC$ tại $E$, $F.$ Chứng minh rằng $BE = CF.$

## Bài 4: Cho đường tròn $(O)$ và hai điểm $A$, $B$ cố định. Một đường thẳng quay quanh $A$, cắt $(O)$ tại $M$ và $N.$ Chứng minh rằng tâm đường tròn ngoại tiếp tam giác $BMN$ thuộc một đường thẳng cố định.

## Bài 5: Cho đường tròn $(O;R)$ và điểm $P$ cố định nằm trong đường tròn. Giả sử $AB$ là dây cung thay đổi luôn đi qua $P.$ Tiếp tuyến của đường tròn $(O)$ tại $A$, $B$ cắt nhau tại $C.$ Tìm tập hợp điểm $C.$

## Bài 6: Cho đường tròn $(O)$ đường kính $AB$ và điểm $H$ cố định thuộc $AB.$ Từ điểm $K$ thay đổi trên tiếp tuyến tại $B$ của $(O)$, vẽ đường tròn $(K;KH)$ cắt $(O)$ tại $C$ và $D.$ Chứng minh rằng $CD$ luôn đi qua một điểm cố định.

## Bài 7: Cho đường tròn đường kính $AB$, $H$ là điểm nằm giữa $AB$ và đường thẳng $\Delta$ vuông góc với $AB$ tại $H.$ Gọi $E$, $F$ là giao điểm của đường tròn và $\Delta.$ Vẽ đường tròn tâm $A$, bán kính $AE$ và đường tròn $(C)$ bất kì qua $H$, $B.$ Giả sử hai đường tròn đó cắt nhau tại $M$ và $N$, chứng minh rằng $AM$ và $AN$ là hai tiếp tuyến của $(C).$

## Bài 8: Cho hai đường tròn đồng tâm $O$ là $\left( {{C_1}} \right)$ và $\left( {{C_2}} \right)$ ($\left( {{C_2}} \right)$ nằm trong $\left( {{C_1}} \right)$). Từ một điểm $A$ nằm trên $\left( {{C_1}} \right)$ kẻ tiếp tuyến $AB$ tới $\left( {{C_2}} \right).$ $AB$ giao $\left( {{C_1}} \right)$ lần thứ hai tại $C$, $D$ là trung điểm của $AB.$ Một đường thẳng qua $A$ cắt $\left( {{C_2}} \right)$ tại $E$, $F$ sao cho đường trung trực của đoạn $DF$ và $EC$ giao nhau tại điểm $M$ nằm trên $AC.$ Tính $\frac{{AM}}{{MC}}.$

## Bài 9: Cho đường tròn $(O;R)$ và hai điểm $P$, $Q$ cố định ($P$ nằm ngoài $(O)$, $Q$ nằm trong $(O)$). Dây cung $AB$ của $(O)$ luôn đi qua $Q.$ $PA$, $PB$ lần lượt giao $(O)$ lần thứ hai tại $D$, $C.$ Chứng minh rằng $CD$ luôn đi qua điểm cố định.

## Bài 10: Cho hai đường tròn không đồng tâm $\left( {{O_1};{R_1}} \right)$ và $\left( {{O_2};{R_2}} \right).$ Tìm tập hợp các điểm $M$ có phương tích đối với hai đường tròn bằng nhau.