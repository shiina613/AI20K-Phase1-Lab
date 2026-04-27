# Chứng minh hai đường thẳng song song

<!-- chunk:0 level:0 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
Bài viết trình bày định nghĩa, phương pháp chứng hai đường thẳng song song trong không gian và một số ví dụ minh họa điển hình, đây là dạng toán thường gặp trong chương trình Hình học 11 chương 2: đường thẳng và mặt phẳng trong không gian, quan hệ song song.

**Định nghĩa**: Hai đường thẳng gọi là song song nếu chúng đồng phẳng và không có điểm chung.

**Phương pháp chứng minh hai đường thẳng song song**: Để chứng minh hai đường thẳng song song trong không gian, ta sử dụng một trong các cách sau đây:

+ **Cách 1**. Chứng minh chúng đồng phẳng rồi sử dụng các định lí đường trung bình, Thales đảo … quen thuộc trong hình học phẳng.

+ **Cách 2**. Chứng minh chúng cùng song song với đường thẳng thứ ba.

+ **Cách 3**. Dùng hệ quả: Nếu hai mặt phẳng cắt nhau lần lượt đi qua hai đường thẳng song song thì giao tuyến của chúng song song hoặc trùng với một trong hai đường thẳng đó.

Ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 1: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành.

a) Tìm giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD).$

b) Đường thẳng qua $D$ và song song $SC$ cắt mặt phẳng $(SAB)$ tại $I.$ Chứng minh $AI$ song song $SB.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-1.png" alt="chung-minh-hai-duong-thang-song-song-1">

a) Mặt phẳng $(SAB)$ chứa $AB$, mặt phẳng $(SCD)$ chứa $CD$ mà $AB // CD$ nên $St = mp (SCD) ∩ mp (SAB)$ với $St // AB // CD.$

b) Trong mặt phẳng $(SCD)$, đường thẳng qua $D$ và song song $SC$ cắt $St$ tại $I.$

Do $St ⊂ mp (SAB)$ $⇒I ∈ mp (SAB).$

Ta có $SI // CD$ và $SC // DI$ nên $SIDC$ là hình bình hành. Do đó: $SI // = CD.$

Mà $CD // = AB$ nên $SI // = AB.$

Tứ giác $SIAB$ là hình bình hành nên $AI // SB.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 2: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang với $AB$ song song $CD$ và $AB > CD.$ Gọi $M$, $N$ lần lượt là trung điểm $SA$, $SB.$

a) Chứng minh $MN$ song song $CD.$

b) Tìm giao điểm $J$ của $SC$ và mặt phẳng $(ADN).$

c) $AN$ và $DJ$ cắt nhau tại $I$. Chứng minh $SI // AB$ và $SA // IB.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-2.png" alt="chung-minh-hai-duong-thang-song-song-2">

a) Ta có $MN$ là đường trung bình của tam giác $SAB$ nên $MN // AB$, mà $AB // CD$ nên $MN // CD.$

b) Trong mặt phẳng $(ABCD)$, $AD$ cắt $BC$ tại $E.$

Trong mặt phẳng $(SBC)$, $NE$ cắt $SC$ tại $J.$

$J ∈ NE$ $⇒ J ∈ mp (ADN).$

Vậy $J$ là giao điểm $SC$ và $(ADN).$

c) Ta có:

$AB ⊂ mp (SAB).$

$CD ⊂ mp (SCD).$

$AB // CD.$

$SI$ là giao tuyến của mặt phẳng $(SAB)$ và mặt phẳng $(SCD).$

Vậy $SI // AB // CD.$

Ta có: $SI // MN$ (vì cùng song song với $AB$), mà $M$ là trung điểm $SA$ nên $MN$ là đường trung bình của tam giác $ASI.$

Do đó: $\overrightarrow {SI} = 2\overrightarrow {MN}$ mà $\overrightarrow {AB} = 2\overrightarrow {MN}$ nên $\overrightarrow {SI} = \overrightarrow {AB} .$

Vậy $ABIS$ là hình bình hành, suy ra $SA // IB.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 3: Cho tứ diện $ABCD.$ Gọi $A_1$, $B_1$, $C_1$, $D_1$ lần lượt là trọng tâm các $ΔBCD$, $ΔACD$, $ΔABD$, $ΔABC.$ Gọi $G$ là giao điểm $AA_1$ và $BB_1.$ Chứng minh:

a) $\frac{{AG}}{{A{A_1}}} = \frac{3}{4}.$

b) $AA_1$, $BB_1$, $CC_1$ đồng quy.

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-3.png" alt="chung-minh-hai-duong-thang-song-song-3">

a) Gọi $I$ là trung điểm $CD.$ Trên mặt phẳng $(IAB)$, ta có:

$\frac{{I{B_1}}}{{IA}} = \frac{{I{A_1}}}{{IB}} = \frac{1}{3}$ $\Rightarrow {A_1}{B_1}//AB$ và $\frac{{{A_1}{B_1}}}{{AB}} = \frac{1}{3}.$

$\Rightarrow \frac{{GA}}{{G{A_1}}} = \frac{{AB}}{{{A_1}{B_1}}} = 3$ $\Rightarrow \frac{{GA}}{{G{A_1} + GA}} = \frac{3}{{3 + 1}} = \frac{{AG}}{{A{A_1}}}$ $(1).$

b) Tương tự, gọi ${G’} = A{A_1} \cap D{D_1}$, ta có: $\frac{{G’A}}{{A{A_1}}} = \frac{3}{4}$ $(2).$

Tương tự, gọi $G” = A{A_1} \cap C{C_1}$, ta có: $\frac{{G”A}}{{A{A_1}}} = \frac{3}{4}$ $(3).$

Từ $(1)$, $(2)$ và $(3)$, suy ra: $\frac{{G’A}}{{A{A_1}}} = \frac{{G”A}}{{A{A_1}}} = \frac{{GA}}{{A{A_1}}}$ $\Rightarrow G \equiv G’ \equiv G”.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 4: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Lấy $M$, $N$, $P$, $Q$ lần lượt trên $BC$, $SC$, $SD$, $AD$ sao cho $MN // SB$, $NP // CD$, $MQ // AB.$

a) Chứng minh $PQ // SA.$

b) Gọi $K$ là giao điểm $MN$ và $PQ.$ Chứng minh $SK // AD // BC.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-4.png" alt="chung-minh-hai-duong-thang-song-song-4">

a) Do $MQ//AB \Rightarrow \frac{{DQ}}{{DA}} = \frac{{CM}}{{CB}}$ $(1).$

Do $MN//SB \Rightarrow \frac{{CM}}{{CB}} = \frac{{CN}}{{CS}}$ $(2).$

Do $NP//CD \Rightarrow \frac{{CN}}{{CS}} = \frac{{DP}}{{DS}}$ $(3).$

Từ $(1)$, $(2)$ và $(3)$, suy ra: $\frac{{DQ}}{{DA}} = \frac{{DP}}{{DS}}$ $\Rightarrow PQ///SA.$

b) Mặt phẳng $(SAD)$ và $(SBC)$ đã có chung điểm $S.$

$K \in NM \Rightarrow K \in (SBC).$

$K \in PQ \Rightarrow K \in (SAD).$

Vậy $SK = (SAD) \cap (SBC).$

Ta có $AD \subset (SAD)$, $BC \subset (SBC)$, mà $AD//BC.$

Vậy $SK = (SAD) \cap (SBC)$ thì $SK//AD//BC.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 5: Cho hình chóp $S.ABCD$ có $ABCD$ là hình bình hành tâm $O$. Gọi $M$ và $N$ lần lượt là trung điểm của $SC$ và $OB.$ Gọi $I$ là giao điểm của $SD$ và mặt phẳng $(AMN).$ Tính tỉ số $\frac{{SI}}{{ID}}.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-5.png" alt="chung-minh-hai-duong-thang-song-song-5">

Trong mặt phẳng $(ABCD)$, gọi $E$ và $F$ là giao điểm của $AN$ với $CD$ và $BC.$

Trong mặt phẳng $(SCD)$, gọi $I$ là giao điểm của $EM$ và $SD.$

$I ∈ ME$ $⇒ I ∈ mp (AMN).$

Vậy $I$ là giao điểm của $SD$ và mặt phẳng $(AMN).$

Ta có: $BF//AD$ $\Rightarrow \frac{{BF}}{{AD}} = \frac{{NB}}{{ND}}$ $= \frac{{\frac{1}{2}OB}}{{OD + \frac{1}{2}OB}} = \frac{{\frac{1}{2}OB}}{{\frac{3}{2}OB}} = \frac{1}{3}$ $\Rightarrow BF = \frac{1}{3}AD$ $\Rightarrow CF = \frac{2}{3}AD.$

Ta có $CF//AD$ $\Rightarrow \frac{{EC}}{{ED}} = \frac{{CF}}{{AD}} = \frac{2}{3}.$

Trong mặt phẳng $(SCD)$ vẽ $CJ//SD$ $(J \in EI)$. Ta có $\frac{{JC}}{{ID}} = \frac{{EC}}{{ED}} = \frac{2}{3}$ $(1).$

$JC//SI$ $\Rightarrow \frac{{CJ}}{{SI}} = \frac{{MC}}{{MS}} = 1$ $\Rightarrow CJ = SI$ $(2).$

Từ $(1)$ và $(2)$ suy ra $\frac{{SI}}{{ID}} = \frac{2}{3}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 6: Cho hình lập phương $ABCD.A’B’C’D’$ cạnh $a.$ Gọi $M$, $N$, $P$, $Q$ lần lượt là trung điểm của $A’B’$, $C’B’$, $CC’$, $AA’.$

a) Chứng minh tứ giác $MNPQ$ là hình thang cân.

b) Tính chu vi và diện tích tứ giác $MNPQ$ theo $a.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-6.png" alt="chung-minh-hai-duong-thang-song-song-6">

a) Ta có $MN$ là đường trung bình của tam giác $A’B’C’$ nên $MN//A’C’$ $(1).$

Ta có $\overrightarrow {A’Q} = \frac{1}{2}\overrightarrow {A’A}$ và $\overrightarrow {C’P} = \frac{1}{2}\overrightarrow {C’C} .$

Mà $\overrightarrow {A’A} = \overrightarrow {C’C}$ nên $\overrightarrow {A’Q} = \overrightarrow {C’P} .$

Do đó $A’QPC’$ là hình bình hành nên $PQ // A’C’$ $(2).$

Từ $(1)$ và $(2)$ suy ra $PQ//MN.$

Ta có $\Delta A’MQ = \Delta C’PN$ (c.g.c) $\Rightarrow MQ = NP.$

Vẽ $MH$ và $NK$ vuông góc với $PQ.$

Ta có $\Delta MHQ = \Delta NKP$ nên $\widehat {MQH} = \widehat {NPK}.$

Do đó $MNPQ$ là hình thang cân.

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-7.png" alt="chung-minh-hai-duong-thang-song-song-7">

b) Ta có:

$MN = \frac{{A’C’}}{2} = \frac{{a\sqrt 2 }}{2}.$

$PQ = A’C’ = a\sqrt 2 .$

$NP = MQ = \frac{a}{2}\sqrt 2 .$

Do đó chu vi tứ giác $MNPQ$ là: $\frac{{a\sqrt 2 }}{2} + a\sqrt 2 + 2\left( {\frac{a}{2}\sqrt 2 } \right) = \frac{{5a\sqrt 2 }}{2}.$

Do $\Delta MQH = \Delta NKP$ nên $HQ = KP.$

Vậy $KP = QH = \frac{1}{2}(PQ – HK)$ $= \frac{1}{2}(PQ – MN)$ $= \frac{1}{2}\left( {a\sqrt 2 – \frac{{a\sqrt 2 }}{2}} \right) = \frac{{a\sqrt 2 }}{4}.$

Do tam giác $NPK$ vuông $\Rightarrow N{K^2} = N{P^2} – K{P^2}$ $= \frac{{{a^2}}}{2} – \frac{{{a^2}}}{8} = \frac{{6{a^2}}}{{16}}.$

Vậy diện tích tứ giác $MNPQ$ là: $\frac{1}{2}NK(MN + PQ)$ $= \frac{{a\sqrt 6 }}{8}\left( {\frac{{a\sqrt 2 }}{2} + a\sqrt 2 } \right) = \frac{{3{a^2}\sqrt 3 }}{8}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 7: Cho tam giác $ABC$ nằm trong mặt phẳng $(α).$ Gọi $Bx$, $Cy$ là hai nửa đường thẳng song song nằm về cùng phía đối với mặt phẳng $(α).$ Gọi $M$ và $N$ là hai điểm di động trên $Bx$, $Cy$ sao cho $CN = 2BM.$

a) Chứng minh $MN$ luôn qua một điểm cố định $I$ khi $M$, $N$ di động.

b) Lấy $E$ thuộc đoạn $AM$ với $EM = \frac{1}{3}AE$, $IE$ cắt $AN$ tại $F$, $BE$ cắt $CF$ tại $Q.$ Chứng minh $AQ$ song song $Bx$ và $Cy$, và mặt phẳng $(QMN)$ chứa một đường thẳng cố định khi $M$, $N$ di động.

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-8.png" alt="chung-minh-hai-duong-thang-song-song-8">

a) Trong mặt phẳng $(Bx, Cy)$, gọi $I$ là giao điểm của $MN$ và $BC.$

Do $MB // NC$ nên $\frac{{IB}}{{IC}} = \frac{{MB}}{{NC}} = \frac{1}{2}$ $\Rightarrow IB = 2IC$, suy ra $B$ là trung điểm $IC.$

Vậy $MN$ di động luôn qua $I$ cố định.

b) Ta có:

$Q \in BE \Rightarrow Q \in mp(ABM).$

$Q \in CF \Rightarrow Q \in mp(ANC).$

Vậy $AQ = mp (ABM) ∩ mp (ANC).$

Mà hai mặt phẳng $(ABM)$ và mặt phẳng $(ANC)$ lần lượt chứa hai đường thẳng song song $BM$ và $NC.$

Do đó: $AQ // BM // NC.$

Ta có: $MB // AQ$ $\Rightarrow \frac{{MB}}{{AQ}} = \frac{{EM}}{{EA}} = \frac{1}{3}.$

Gọi $K$ là giao điểm của $MQ$ và $BA$ ta có: $\frac{{KB}}{{KA}} = \frac{{MB}}{{AQ}} = \frac{1}{3}$ $\Rightarrow KB = \frac{1}{3}KA.$

Vậy $K$ cố định.

Ta có:

$K ∈ MQ ⇒ K ∈ mp (MNQ).$

$I ∈ MN ⇒ I∈ mp (MNQ).$

Do đó: mặt phẳng $(QMN)$ di động nhưng luôn chứa đường thẳng cố định $IK.$

[ads]

<!-- chunk:8 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 8: Cho tam giác $ABC.$ Từ $A$, $B$, $C$ vẽ các nửa đường thẳng song song cùng chiều $Ax$, $By$, $Cz$ không nằm trong mặt phẳng $(ABC).$ Trên $Ax$, $By$, $Cz$ lần lượt lấy đoạn $AA’ = a$, $BB’ = b$, $CC’ = c.$ Gọi $I$, $J$, $K$ lần lượt là giao điểm $B’C’$, $A’C’$, $A’B’$ với mặt phẳng $(ABC).$ Gọi $G$, $G’$ là trọng tâm tam giác $ABC$ và tam giác $A’B’C’.$

a) Chứng minh $\frac{{IB}}{{IC}} \cdot \frac{{JC}}{{JA}} \cdot \frac{{KA}}{{KB}} = 1.$

b) Chứng minh $GG’ // AA’.$ Tính $GG’$ theo $a$, $b$, $c.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-9.png" alt="chung-minh-hai-duong-thang-song-song-9">

Ta có:

$CC’//BB’ \Rightarrow \frac{{IB}}{{IC}} = \frac{{BB’}}{{CC’}} = \frac{b}{c}.$

$CC’//AA’ \Rightarrow \frac{{JC}}{{JA}} = \frac{{CC’}}{{AA’}} = \frac{c}{a}.$

$AA’//BB’ \Rightarrow \frac{{KA}}{{KB}} = \frac{{AA’}}{{BB’}} = \frac{a}{b}.$

Do đó: $\frac{{IB}}{{IC}} \cdot \frac{{JC}}{{JA}} \cdot \frac{{KA}}{{KB}} = \frac{b}{c} \cdot \frac{c}{a} \cdot \frac{a}{b} = 1.$

b) Gọi $H$, $H’$ là trung điểm $CB$ và $C’B’.$

$HH’$ là đường trung bình của hình thang $CC’B’B$ nên $HH’//BB’//AA’//CC’$ $(1).$

$G$ là trọng tâm tam giác $ABC$ $\Rightarrow \frac{{AG}}{{AH}} = \frac{2}{3}.$

$G’$ là trọng tâm tam giác $A’B’C’$ $\Rightarrow \frac{{A’G’}}{{A’H’}} = \frac{2}{3}.$

Vậy $\frac{{AG}}{{AH}} = \frac{{A’G’}}{{A’H’}} \Rightarrow GG’//HH’$ $(2).$

Từ $(1)$ và $(2)$ suy ra $GG’//AA’.$

Gọi $M$ là giao điểm $AH’$ và $GG’.$

Ta có $G’M//AA’ \Rightarrow \frac{{G’M}}{{AA’}} = \frac{{H’G’}}{{H’A’}} = \frac{1}{3}$ $\Rightarrow G’M’ = \frac{a}{3}.$

Ta có $MG//HH’ \Rightarrow \frac{{MG}}{{HH’}} = \frac{{AG}}{{AH}} = \frac{2}{3}$ $\Rightarrow MG = \frac{2}{3}HH’$ $= \frac{2}{3}\frac{{BB’ + CC’}}{2} = \frac{{b + c}}{3}.$

Do đó $GG’ = MG’ + MG = \frac{{a + b + c}}{3}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Ví dụ 9: Cho hình chóp $S.ABCD$ có đáy là hình thang $ABCD$ với đáy $AD$ và $BC$ có $AD = a$, $BC = b$ với $a > b.$ Gọi $I$ và $J$ lần lượt là trọng tâm $ΔSAD$, $ΔSBC$, $SB$ và $SC$ cắt mặt phẳng $(ADJ)$ tại $M$, $N$, $SA$, $SD$ cắt mặt phẳng $(BCI)$ tại $P$, $Q.$

a) Chứng minh $MN$ song song $PQ.$

b) Giả sử $AM$ cắt $BP$ tại $E$, $CQ$ cắt $DN$ tại $F.$ Chứng minh $EF$ song song $MN$ và $PQ.$ Tính $EF$ theo $a$ và $b.$

<img link="data_for_rag/toan11/images/chung-minh-hai-duong-thang-song-song-10.png" alt="chung-minh-hai-duong-thang-song-song-10">

a) Ta có: $I \in (IBC) \cap (SAD).$

Ta có: 
$$
\left. {\begin{array}{l}
{AD//BC}\\
{AD \subset (SAD)}\\
{BC \subset (IBC)}
\end{array}} \right\}
$$
 $\Rightarrow (SAD) \cap (IBC) = PQ.$

Với $I∈PQ$ và $PQ//AD//BC.$

Tương tự $J \in (JAD) \cap (SBC).$

$$
\left. {\begin{array}{l}
{AD//BC}\\
{AD \subset (JAD)}\\
{BC \subset (SBC)}
\end{array}} \right\}
$$
 $\Rightarrow (JAD) \cap (SBC) = MN.$

Với $J \in MN$ và $MN//AD//BC.$

Do đó $MN//PQ.$

b) Ta có: 
$$
\left. {\begin{array}{l}
{\mathop E\limits^. \in AM \Rightarrow E \in (AMND)}\\
{E \in PQ \Rightarrow E \in (BPCQ)}
\end{array}} \right\}
$$
 $\Rightarrow E \in (AMND) \cap (BPCQ).$

Ta có: 
$$
\left. {\begin{array}{l}
{F \in DN \Rightarrow F \in (AMND)}\\
{F \in CQ \Rightarrow E \in (BPCQ)}
\end{array}} \right\}
$$
 $\Rightarrow F \in (AMND) \cap (BPCQ).$

Vậy $EF = (AMND) \cap (BPCQ).$

Ta có: 
$$
\left. {\begin{array}{l}
{MN \subset (AMND)}\\
{PQ \subset (BPCQ)}\\
{MN//PQ}
\end{array}} \right\}
$$
 $\Rightarrow EF//PQ//MN.$

Gọi $K$ là giao điểm $EF$ và $PC.$

Ta có $EK//BC$ $\Rightarrow \frac{{KE}}{{BC}} = \frac{{PE}}{{PB}}.$

Do $I$ là trọng tâm tam giác $SAD$ và $PI//AD$ $\Rightarrow \frac{{SP}}{{AS}} = \frac{2}{3}.$

Do $J$ là trọng tâm tam giác $SBC$ và $MJ//BC$ $\Rightarrow \frac{{SM}}{{SB}} = \frac{2}{3}.$

Do đó $\frac{{SP}}{{SA}} = \frac{{SM}}{{SB}} = \frac{2}{3}$ $\Rightarrow PM//AB$ $\Rightarrow \frac{{PE}}{{EB}} = \frac{{PM}}{{AB}}.$

Mà $\frac{{PM}}{{AB}} = \frac{{SP}}{{SA}} = \frac{2}{3}.$

Do đó $\frac{{PE}}{{EB}} = \frac{2}{3}$ $\Rightarrow \frac{{EK}}{{BC}} = \frac{{PE}}{{PB}} = \frac{{PE}}{{PE + EB}}$ $= \frac{1}{{1 + \frac{{EB}}{{PE}}}} = \frac{1}{{1 + \frac{3}{2}}} = \frac{2}{5}$ $\Rightarrow EK = \frac{2}{5}BC = \frac{2}{5}b.$

Tương tự $KF = \frac{2}{5}a.$

Vậy $EF = EK + KF = \frac{2}{5}(a + b).$

Bài tập tự luyện:

<!-- chunk:10 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 1: Cho tứ diện $ABCD.$ Gọi $M$, $N$, $P$, $Q$, $R$, $S$ lần lượt là trung điểm của $AB$, $CD$, $BC$, $AD$, $AC$, $BD.$

a) Chứng minh $MNPQ$ là hình bình hành.

b) Chứng minh $MN$, $PQ$, $RS$ cắt nhau tại trung điểm của mỗi đường.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 2: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang có cạnh bên $AD$, $BC.$

a) Xác định giao tuyến $d$ của $(SAB)$ và $(SCD).$

b) Gọi $M$, $N$ lần lượt là trọng tâm của tam giác $SAD$ và $SBC.$ Chứng minh $d // MN.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 3: Cho hai hình bình hành $ABCD$, $ABEF$ không cùng nằm trên một mặt phẳng.

a) Chứng minh $CE // DF.$

b) Gọi $M$, $N$ là hai điểm trên $AC$, $AD$ sao cho $\frac{{AM}}{{AC}} = \frac{{AN}}{{AD}} = m.$ Gọi $H$, $K$ là hai điểm trên $BF$ và $AF$ sao cho $\frac{{FK}}{{FA}} = \frac{{FL}}{{FB}} = n$ với $m,n \in (0;1)$. Chứng minh $MN // KL.$

c) Cho $m = \frac{2}{5}$ và $n = \frac{3}{5}$. Chứng minh $NK // DF.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 4: Cho tứ diện $ABCD.$ Gọi $P$, $Q$ lần lượt là trung điểm của $AC$, $BC.$ Gọi $R$ là điểm trên $BD$ sao cho $BR = 2RD.$

a) Xác định $E$, $F$ là giao điểm của $(RPQ)$ với $CD$, $AD.$

b) Tìm giao tuyến của $(PQR)$ và $(ABE).$

c) Chứng minh $R$, $F$ lần lượt là trọng tâm của tam giác $BCE$ và $ACE.$

d) Chứng minh $FR // PQ.$

e) Tính tỉ số diện tích mà mặt phẳng $(PQR)$ chia cắt tam giác $ACD.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 5: Cho hình chóp $S.ABCD$ có $ABCD$ là hình bình hành tâm $O.$ Gọi $M$, $N$ lần lượt là trung điểm của $SC$, $OB.$

a) Tìm giao điểm $I$ của $SD$ và $(AMN).$

b) Tính $\frac{{SI}}{{ID}}.$

<!-- chunk:15 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 6: Cho hình chóp $S.ABCD$ có đáy là tứ giác lồi, $O$ là giao điểm của $AC$ và $BD.$ Gọi $M$, $N$, $E$, $F$ lần lượt là trung điểm của $SA$, $SB$, $SC$, $SD.$ Chứng minh:

a) $ME // AC$ và $NF // BD.$

b) Ba đường thẳng $EM$, $NF$, $SO$ đồng quy.

c) Bốn điểm $M$, $N$, $E$, $F$ đồng phẳng.

<!-- chunk:16 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 7: Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật. Gọi $M$, $N$, $E$, $F$ lần lượt là trọng tâm của tam giác $SAB$, $SBC$, $SCD$ và $SDA.$

a) Chứng minh tứ giác $MNEF$ là hình thoi.

b) Gọi $O$ là giao điểm của $AC$ và $BD.$ Chứng minh $ME$, $NF$ và $SO$ đồng quy.

<!-- chunk:17 level:4 source:https://toanmath.com/2019/02/chung-minh-hai-duong-thang-song-song.html -->
## Bài tập 8: Cho tứ diện $ABCD.$ Gọi $I$, $J$ lần lượt là trung điểm của $BC$ và $BD.$ Lấy $E$ trên $AD$ $(E ≠ A, D).$

a) Xác định mặt cắt của tứ diện và $(IJE).$

b) Tìm vị trí của điểm $E$ trên $AD$ sao cho thiết diện là hình bình hành.

c) Tìm điều kiện của $A.BCD$ và vị trí $E$ trên $AD$ sao cho thiết diện là hình thoi.