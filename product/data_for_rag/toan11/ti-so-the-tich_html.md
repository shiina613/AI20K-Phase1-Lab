# Tỉ số thể tích

<!-- chunk:0 level:0 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
TOANMATH.com giới thiệu đến bạn đọc bài viết **tỉ số thể tích **nằm trong chủ đề Hình học không gian, nội dung bài viết được chia thành 3 phần: phương pháp giải toán, ví dụ minh họa và bài tập tự rèn luyện.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
1) Tỉ số về diện tích

Cho tam giác $ABC.$

+ Lấy các điểm $M$, $N$ lần lượt trên các đường thẳng $AB$, $AC$ thì: $\frac{{{S}_{AMN}}}{{{S}_{ABC}}}=\frac{AM}{AB}.\frac{AN}{AC}.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-1.png" alt="">

+ Nếu điểm $M$ nằm trong tam giác $ABC$, $AM$ cắt $BC$ tại ${A}’$ thì: $\frac{{{S}_{MBC}}}{{{S}_{ABC}}}=\frac{M{A}’}{MA}.$

+ Nếu điểm $M$ nằm trên cạnh $BC$ của tam giác $ABC$ thì: $\frac{{{S}_{BAM}}}{{{S}_{BAC}}}=\frac{BM}{BC}$, $\frac{{{S}_{CAM}}}{{{S}_{CAB}}}=\frac{CM}{CB}.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-2.png" alt="">

+ Nếu $G$ là trọng tâm tam giác $ABC$ thì: ${{S}_{GBC}}={{S}_{GCA}}={{S}_{GAB}}=\frac{1}{3}{{S}_{ABC}}.$

+ Nếu $M$ nằm trên đường trung bình ứng với cạnh $BC$ thì: $\frac{{{S}_{MBC}}}{{{S}_{ABC}}}=\frac{1}{2}.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-3.png" alt="">

+ Nếu $M$ nằm trên đường thẳng đi qua $A$ và song song với $BC$ thì: $\frac{{{S}_{MBC}}}{{{S}_{ABC}}}=1.$

**2) Tỉ số về khoảng cách**

<img link="data_for_rag/toan11/images/ti-so-the-tich-4.png" alt="">

+ Đường thẳng $AB$ cắt mặt phẳng $(P)$ ở điểm $M$ thì: $\frac{d(A,(P))}{d(B,(P))}=\frac{AM}{BM}.$

+ Đường thẳng $\Delta$ song song với một mặt phẳng $(P)$ thì khoảng cách từ mọi điểm thuộc đường thẳng $\Delta$ đến mặt phẳng $(P)$ bằng nhau.

3) Tỉ số về thể tích

Cho khối chóp tam giác $S.ABC.$

+ Trên ba đường thẳng $SA$, $SB$, $SC$ lần lượt lấy ba điểm ${A}’$, ${B}’$, ${C}’$ bất kỳ.

Ta có: $\frac{{{V}_{S.{A}'{B}'{C}’}}}{{{V}_{S.ABC}}}=\frac{S{A}’}{SA}.\frac{S{B}’}{SB}.\frac{S{C}’}{SC}.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-5.png" alt="">

+ Nếu $M$ nằm trên cạnh $SC$ thì: $\frac{{{V}_{S.ABM}}}{{{V}_{S.ABC}}}=\frac{SM}{SC}.$

+ Nếu $M$ nằm trong hình chóp và $SM$ cắt mặt phẳng $(ABC)$ tại điểm $S’$ thì: $\frac{{{V}_{M.ABC}}}{{{V}_{S.ABC}}}=\frac{M{S}’}{S{S}’}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 1. Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh $a$, $SA$ vuông góc với mặt phẳng $\left( ABC \right)$. Gọi $I$ là trung điểm của cạnh $BC$. Mặt phẳng $\left( P \right)$ qua $A$ và vuông góc với $SI$ cắt $SB$, $SC$ lần lượt tại $M$, $N$.Biết rằng ${{V}_{SAMN}}=\frac{1}{4}{{V}_{SABC}}$. Hãy tính ${{V}_{SABC}}.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-6.png" alt="">

$BC\bot AI$ (do $\Delta ABC$ đều) và $BC\bot SA.$

Suy ra: $BC\bot \left( SAI \right)$ $\Rightarrow BC\bot SI.$

$\left( P \right)\bot SI$ $\Rightarrow \left( P \right)\parallel BC.$

$$
\left\{ \begin{align}
& \left( P \right)\parallel BC \\
& \left( P \right)\cap \left( SBC \right)=MN \\
\end{align} \right.
$$
 $\Rightarrow MN\parallel BC$ $\Rightarrow \frac{SM}{SB}=\frac{SN}{SC}.$

Theo giả thiết ta có: $\frac{{{V}_{SAMN}}}{{{V}_{SABC}}}=\frac{SA}{SA}.\frac{SM}{SB}.\frac{SN}{SC}=\frac{1}{4}.$

$\Rightarrow \frac{SM}{SB}=\frac{SN}{SC}=\frac{1}{2}.$

Suy ra $M$, $N$ lần lượt là trung điểm của các cạnh $SB$, $SC.$

Trong tam giác $SBC$, $MN$ là đường trung bình của tam giác, gọi $H$ là giao điểm của $MN$ với $SI$ thì $H$ là trung điểm của $SI.$

Tam giác $SAI$ có trung tuyến $AI~\bot SI~$ (do $AI\subset \left( P \right)\bot SI$) nên là tam giác cân tại $A$, suy ra $SA=AI=\frac{a\sqrt{3}}{2}.$

Thể tích tứ diện $ABCD$: ${{V}_{SABC}}=\frac{1}{3}{{S}_{ABC}}.SA$ $=\frac{1}{3}.\frac{{{a}^{2}}\sqrt{3}}{4}.\frac{a\sqrt{3}}{2}$ $=\frac{{{a}^{3}}}{8}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 2.

1. Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $A$, $AB=a$, $AC=a\sqrt{3}$. Cạnh bên $SA$ vuông góc với đáy và $SA=2a$. Gọi $M$, $N$ là các điểm thuộc $SB$, $SC$ sao cho $\frac{SM}{SB}=\frac{2}{3}$, $\frac{SN}{SC}=x$.

a) Tính thể tích khối chóp $S.AMN$ theo $a$, $x.$

b) Tìm $x$ theo $a$ để mặt phẳng $(AMN)$ chia khối chóp thành hai phần có thể tích bằng nhau.

2. Cho khối chóp $S.ABC$ có đáy là tam giác vuông cân tại đỉnh $B$, $AB=a$, $SA=2a$ và $SA$ vuông góc với mặt phẳng đáy. Mặt phẳng qua $A$ vuông góc với $SC$ cắt các cạnh $SB$, $SC$ lần lượt tại $H$, $K.$ Tính thể tích khối chóp $S.AHK$ theo $a.$

1.

<img link="data_for_rag/toan11/images/ti-so-the-tich-7.png" alt="">

a. Ta có ${{V}_{S.ABC}}=\frac{1}{3}SA.{{S}_{\Delta ABC}}$ $=\frac{1}{6}SA.AB.AC=\frac{{{a}^{3}}\sqrt{3}}{3}.$

Áp dụng công thức tỉ số thể tích: $\frac{{{V}_{S.AMN}}}{{{V}_{S.ABC}}}=\frac{SA.AM.SN}{SA.SB.SC}$ $=\frac{SM}{SB}.\frac{SN}{SC}=\frac{2x}{3}.$

Do đó: ${{V}_{S.AMN}}=\frac{2x}{3}{{V}_{S.ABC}}$ $=\frac{2x{{a}^{3}}\sqrt{3}}{9}$.

b. Mặt phẳng $(AMN)$ chia khối chóp thành hai phần có thể tích bằng nhau $\Leftrightarrow \frac{{{V}_{S.AMN}}}{{{V}_{S.ABC}}}=\frac{1}{2}$ $\Leftrightarrow \frac{2x}{3}=\frac{1}{2}$ $\Leftrightarrow x=\frac{3}{4}$.

2.

<img link="data_for_rag/toan11/images/ti-so-the-tich-8.png" alt="">

Vì $(AHK)\bot SC$ $\Rightarrow AH\bot SC$, nhưng $BC\bot (SAB)$ $\Rightarrow AH\bot BC$ do đó ta có $AH\bot (SBC)$ $\Rightarrow AH\bot SB.$

Tam giác vuông $SAB$ với đường cao $AH$ nên $\frac{SH}{SB}=\frac{SH.SB}{S{{B}^{2}}}$ $=\frac{S{{A}^{2}}}{S{{B}^{2}}}$ hay $\frac{SH}{SB}=\frac{S{{A}^{2}}}{S{{A}^{2}}+A{{B}^{2}}}=\frac{4}{5}.$

Tương tự ta có $\frac{SK}{SC}=\frac{S{{A}^{2}}}{S{{A}^{2}}+A{{B}^{2}}+C{{B}^{2}}}=\frac{2}{3}.$

Thể tích khối chóp $S.ABC$ là $V=\frac{{{a}^{3}}}{3}.$

Vì thế $\frac{{{V}_{S.AHK}}}{V}=\frac{SH}{SB}.\frac{SK}{SC}=\frac{8}{15}$ $\Rightarrow {{V}_{S.AHK}}=\frac{8}{45}{{a}^{3}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 3. Cho hình chóp $S.ABCD$ có $SA=AB=a$, $SA\bot (ABCD)$ và đáy là hình chữ nhật. Gọi $G$ là trọng tâm tam giác $SAC$, mặt phẳng $(ABG)$ cắt $SC$ tại $M$, cắt $SD$ tại $N.$ Đường thẳng $AN$ tạo với mặt phẳng đáy góc ${{30}^{0}}.$ Tính thể tích khối đa diện $MNABCD.$

<img link="data_for_rag/toan11/images/ti-so-the-tich-9.png" alt="">

Vì $G$ là trọng tâm tam giác $SAC$ nên $AG\cap SC=M$ là trung điểm của $SC.$

Mặt khác ta có $AB//CD$ nên $N$ là trung điểm của $SD.$

Do đó:

$\frac{{{V_{S.ABM}}}}{{{V_{S.ABC}}}} = \frac{{SM}}{{SC}} = \frac{1}{2}.$

$\frac{{{V_{S.ANM}}}}{{{V_{S.ADC}}}} = \frac{{SM}}{{SC}}.\frac{{SN}}{{SD}} = \frac{1}{4}.$

$\frac{{{V}_{S.ABMN}}}{{{V}_{S.ABCD}}}=\frac{{{V}_{S.ABM}}}{2{{V}_{S.ABC}}}+\frac{{{V}_{S.ANM}}}{2{{V}_{S.ADC}}}=\frac{3}{8}.$

Góc hợp bởi $AN$ và mặt phẳng đáy là $\widehat{NAD}={{30}^{0}}$, vì vậy:

$AD = SA.\cot {30^0} = a\sqrt 3$ $\Rightarrow {V_{S.ABCD}} = \frac{{\sqrt 3 }}{3}{a^3}.$

${V_{S.ABMN}} = \frac{{\sqrt 3 }}{8}{a^3}$ $\Rightarrow {V_{MNABCD}} = {V_{S.ABCD}} – {V_{S.ABMN}}$ $= \frac{{5\sqrt 3 }}{{24}}{a^3}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 4.

1. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật $AB=a$, $AD=2a$. Cạnh bên $SA$ vuông góc với đáy và $SA=a\sqrt{3}$. Gọi $H$, $K$ lần lượt là hình chiếu của $A$ lên $SB$, $SD$; $M$ là giao điểm của $SC$ với $(AHK)$. Chứng minh rằng $SC\bot AM$ và tính thể tích khối chóp $S.AHMK$.

2. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thoi cạnh $a$, $\widehat{BAD}={{60}^{0}}$, $SA=a$ và $SA$ vuông góc với mặt phẳng đáy. Gọi ${C}’$ là trung điểm của $SC.$ Mặt phẳng $(\alpha )$ qua $A{C}’$ và song song với $BD$ cắt $SB$, $SD$ lần lượt tại ${B}’$, ${D}’.$ Tính thể tích khối chóp $S.A{B}'{C}'{D}’.$

1.

<img link="data_for_rag/toan11/images/ti-so-the-tich-10.png" alt="">

Thể tích khối chóp $S.ABCD$ là: ${{V}_{S.ABCD}}=\frac{1}{3}SA.{{S}_{ABCD}}$ $=\frac{1}{3}SA.AB.AD=\frac{2{{a}^{3}}\sqrt{3}}{3}.$

${{V}_{S.ABC}}={{V}_{S.ACD}}$ $=\frac{1}{2}{{V}_{S.ABCD}}=\frac{{{a}^{3}}\sqrt{3}}{3}.$

Ta có 
$$
\left\{ \begin{align}
& BC\bot AB \\
& BC\bot SA \\
\end{align} \right.
$$
 $\Rightarrow BC\bot (SAB)$ $\Rightarrow BC\bot AH.$

Mặt khác $AH\bot SB$ nên suy ra $AH\bot (SBC)$ $\Rightarrow AH\bot SC.$

Hoàn toàn tương tự ta chứng minh được $AK\bot SC.$

Từ đó suy ra $SC\bot (AHK)$ nên $SC\bot AM$.

Áp dụng hệ thức lượng trong tam giác vuông ta có:

$\frac{SH}{SB}=\frac{S{{A}^{2}}}{S{{B}^{2}}}$ $=\frac{S{{A}^{2}}}{S{{A}^{2}}+A{{B}^{2}}}=\frac{3{{a}^{2}}}{4{{a}^{2}}}=\frac{3}{4}.$

$\frac{SK}{SD}=\frac{S{{A}^{2}}}{S{{A}^{2}}+A{{D}^{2}}}=\frac{3}{7}.$

$\frac{SM}{SC}=\frac{S{{A}^{2}}}{S{{A}^{2}}+A{{C}^{2}}}=\frac{3}{8}.$

Sử dụng công thức tỉ số thể tích ta có được:

$\frac{{{V}_{S.AHM}}}{{{V}_{S.ABC}}}=\frac{SH}{SB}.\frac{SM}{SC}=\frac{9}{32}$ $\Rightarrow {{V}_{S.AHM}}=\frac{9}{32}{{V}_{S.ABC}}=\frac{3{{a}^{3}}\sqrt{3}}{32}.$

$\frac{{{V}_{S.AKM}}}{{{V}_{S.ADC}}}=\frac{SK}{SD}.\frac{SM}{SC}=\frac{9}{56}$ $\Rightarrow {{V}_{S.AKM}}=\frac{9}{56}{{V}_{S.ABC}}=\frac{3{{a}^{3}}\sqrt{3}}{56}.$

Vậy ${{V}_{S.AHMK}}={{V}_{S.AHM}}+{{V}_{S.AKM}}=\frac{33{{a}^{3}}\sqrt{3}}{224}$.

Chú ý: Ta có thể tính thể tích khối chóp $S.AHMK$ theo cách sau: ${{V}_{S.AHMK}}=\frac{1}{3}SM.{{S}_{AHMK}}.$

2.

<img link="data_for_rag/toan11/images/ti-so-the-tich-11.png" alt="">

Gọi $O$ là giao của hai đường chéo của hình thoi và $I=SO\cap A{C}’.$

Khi đó ${B}'{D}’$ qua $I$ và song song với $BD.$

Ta có $\frac{S{B}’}{SB}=\frac{S{D}’}{SD}=\frac{SI}{SO}=\frac{2}{3}$ (vì $I$ là trọng tâm tam giác $SAC$).

Suy ra $\frac{{{V}_{S.A{B}'{C}’}}}{{{V}_{S.ABC}}}=\frac{S{B}’}{SB}.\frac{S{C}’}{SC}=\frac{1}{3}$ và $\frac{{{V}_{S.A{D}'{C}’}}}{{{V}_{S.ADC}}}=\frac{S{D}’}{SD}.\frac{S{C}’}{SC}=\frac{1}{3}.$

Vậy $\frac{{{V}_{S.A{B}'{C}'{D}’}}}{{{V}_{S.ABCD}}}$ $=\frac{{{V}_{S.A{D}'{C}’}}}{2{{V}_{S.ADC}}}+\frac{{{V}_{S.A{D}'{C}’}}}{2{{V}_{S.ADC}}}=\frac{1}{3}.$

Mà ${{V}_{S.ABCD}}=\frac{1}{3}SA.{{S}_{ABCD}}$ $=\frac{2}{3}SA.{{S}_{ABD}}=\frac{1}{3}a.a.a.\sin {{60}^{0}}$ $=\frac{\sqrt{3}}{6}{{a}^{3}}$ nên ${{V}_{S.A{B}'{C}'{D}’}}=\frac{1}{3}{{V}_{S.ABCD}}=\frac{\sqrt{3}}{18}{{a}^{3}}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 5. Cho hình lăng trụ tam giác $ABC.{A}'{B}'{C}’.$ Gọi $M$, $N$, $P$ nằm trên các cạnh ${A}'{B}’$, ${B}'{C}’$, $BC$ sao cho $\frac{B{M}’}{{A}'{B}’}=\frac{1}{2}$, $\frac{N{B}’}{{B}'{C}’}=\frac{2}{3}$, $\frac{PB}{BC}=\frac{1}{3}.$ Tính tỉ số thể tích hai phần khi chia lăng trụ bởi mặt phẳng $(MNP).$

<img link="data_for_rag/toan11/images/ti-so-the-tich-12.png" alt="">

$NP\cap {B}’B=E$, $EM\cap AB=Q.$

$\frac{EB}{E{B}’}=\frac{EQ}{EM}$ $=\frac{EP}{EN}=\frac{BP}{{B}’N}=\frac{1}{2}.$

Mặt phẳng $(MNP)$ chia khối lăng trụ thành hai phần, phần chứa điểm $B$ có thể tích là ${{V}_{1}}$, phần còn lại có thể tích là ${{V}_{2}}.$ Gọi thể tích của khối lăng trụ là $V.$

Ta có:

$d(E,(A’B’C’)) = 2.d(B,(A’B’C’)).$

$\frac{{{S_{B’MN}}}}{{{S_{A’B’C’}}}} = \frac{{B’M}}{{B’A’}}.\frac{{B’N}}{{B’C’}} = \frac{1}{3}.$

Nên ${{V}_{E.M{B}’N}}=\frac{1}{3}.2.d(B,({A}'{B}'{C}’)).\frac{1}{3}{{S}_{{A}'{B}'{C}’}}=\frac{2}{9}V.$

$\frac{{{V_{E.QBP}}}}{{{V_{E.MB’N}}}} = {\left( {\frac{{EB}}{{EB’}}} \right)^3} = \frac{1}{8}.$

$\Rightarrow {V_1} = {V_{E.MB’N}} – {V_{E.QBP}}$ $= \frac{7}{8}.\frac{2}{9}V = \frac{7}{{36}}V.$

$\Rightarrow {V_2} = V – {V_1} = \frac{{29}}{{36}}V$ $\Rightarrow \frac{{{V_1}}}{{{V_2}}} = \frac{7}{{29}}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 6. Cho hình lập phương $ABCD.{A}'{B}'{C}'{D}’$ có độ dài cạnh bằng $a.$ Gọi $M$ là trung điểm của cạnh $BC$, $I$ là tâm hình vuông $C{C}'{D}’D.$ Tính thể tích của các khối đa diện do mặt phẳng $(AMI)$ chia hình lập phương.

<img link="data_for_rag/toan11/images/ti-so-the-tich-13.png" alt="">

$AM\cap DC=N$, $NI$ cắt $C{C}’$, $D{D}’$ lần lượt tại $H$, $K.$

Mặt phẳng $(AMI)$ chia khối lập phương thành hai khối đa diện. Khối đa diện chứa điểm $D$ có thể tích là ${{V}_{1}}$, khối đa diện còn lại có thể tích là ${{V}_{2}}.$

Thể tích của khối lập phương là $V={{a}^{3}}.$

Ta có $\frac{HC}{KD}=\frac{NC}{ND}$ $=\frac{NM}{NA}=\frac{NH}{NK}$ $=\frac{MC}{AD}=\frac{1}{2}.$

Nên ${{V}_{N.ADK}}=\frac{1}{3}.ND.{{S}_{ADK}}.$

$\Rightarrow {{V}_{N.ADK}}=\frac{2}{9}{{a}^{3}}.$

$\frac{{{V}_{N.MCH}}}{{{V}_{N.ADK}}}={{\left( \frac{NC}{ND} \right)}^{3}}=\frac{1}{8}.$

Do đó: ${{V}_{1}}={{V}_{N.ADK}}-{{V}_{N.MCH}}$ $=\frac{7}{8}{{V}_{N.ADK}}=\frac{7}{36}{{a}^{3}}$, ${{V}_{2}}=\frac{29}{36}{{a}^{3}}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Ví dụ 7.

1. Cho $O$ là một điểm nằm trong tứ diện và cách đều các mặt của tứ diện một khoảng $r.$ Gọi ${{h}_{A}}$, ${{h}_{B}}$, ${{h}_{C}}$, ${{h}_{D}}$ lần lượt là khoảng cách từ các điểm $A$, $B$, $C$, $D$ đến các mặt đối diện. Chứng minh : $\frac{1}{r}=\frac{1}{{{h}_{A}}}+\frac{1}{{{h}_{B}}}+\frac{1}{{{h}_{C}}}+\frac{1}{{{h}_{D}}}.$

2. Hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Một mặt phẳng $(P)$ cắt $SA$, $SB$, $SC$, $SD$ theo thứ tự tại $K$, $L$, $M$, $N.$ Chứng minh rằng:$\frac{SA}{SK}+\frac{SC}{SM}=\frac{SB}{SL}+\frac{SD}{SN}.$

3. Cho tứ diện $ABCD.$ Các điểm $M$, $N$, $P$ lần lượt nằm trên các cạnh $CB$, $BD$, $AC$ sao cho $BC=4BM$, $AC=3AP$, $BD=2BN.$ Mặt phẳng $(MNP)$ cắt $AD$ tại $Q.$ Tính tỉ số $\frac{AQ}{AD}$ và tỉ số thể tích hai phần của khối tứ diện $ABCD$ được phân chia bởi mặt phẳng $(MNP).$

1.

<img link="data_for_rag/toan11/images/ti-so-the-tich-14.png" alt="">

Ta có: $\frac{{{V}_{O.BCD}}}{{{V}_{ABCD}}}=\frac{\frac{1}{3}r.{{S}_{BCD}}}{\frac{1}{3}{{h}_{A}}.{{S}_{BCD}}}=\frac{r}{{{h}_{A}}}$, $\frac{{{V}_{O.CAD}}}{{{V}_{ABCD}}}=\frac{r}{{{h}_{B}}}$, $\frac{{{V}_{O.ABD}}}{{{V}_{ABCD}}}=\frac{r}{{{h}_{C}}}$, $\frac{{{V}_{O.ABC}}}{{{V}_{ABCD}}}=\frac{r}{{{h}_{D}}}.$

Suy ra: $\frac{r}{{{h}_{A}}}+\frac{r}{{{h}_{B}}}+\frac{r}{{{h}_{C}}}+\frac{r}{{{h}_{D}}}$ $=\frac{{{V}_{O.ABC}}+{{V}_{O.ABD}}+{{V}_{O.ACD}}+{{V}_{O.BCD}}}{{{V}_{ABCD}}}$ $=1.$

Do đó: $\frac{1}{r}=\frac{1}{{{h}_{A}}}+\frac{1}{{{h}_{B}}}+\frac{1}{{{h}_{C}}}+\frac{1}{{{h}_{D}}}.$

2.

<img link="data_for_rag/toan11/images/ti-so-the-tich-15.png" alt="">

Ta có ${{V}_{S.KMN}}+{{V}_{S.KML}}={{V}_{S.NLM}}+{{V}_{S.NLK}}$ $(*).$

Vì $ABCD$ là hình bình hành nên ${{S}_{ACD}}={{S}_{ACB}}={{S}_{ABD}}$ $={{S}_{CBD}}=\frac{1}{2}{{S}_{ABCD}}.$

Do đó ${{V}_{S.}}_{ACD}={{V}_{S.}}_{ACB}={{V}_{S.}}_{ABD}$ $={{V}_{S.}}_{CBD}=\frac{1}{2}{{V}_{S.}}_{ABCD}.$

Vậy từ $(*)$ ta suy ra:

$\frac{{{V}_{S.KMN}}}{{{V}_{S.ACD}}}+\frac{{{V}_{S.KML}}}{{{V}_{S.ABC}}}$ $=\frac{{{V}_{S.NLM}}}{{{V}_{S.DBC}}}+\frac{{{V}_{S.NLK}}}{{{V}_{S.DBA}}}.$

$\Rightarrow \frac{SK.SM.SN}{SA.SC.SD}+\frac{SK.SM.SL}{SA.SB.SC}$ $=\frac{SN.SL.SM}{SD.SB.SC}+\frac{SN.SL.SK}{SD.SB.SA}.$

$\Leftrightarrow \frac{SK.SL.SM.SN}{SA.SB.SC.SD}\left( \frac{SB}{SL}+\frac{SD}{SN} \right)$ $=\frac{SK.SL.SM.SN}{SA.SB.SC.SD}\left( \frac{SA}{SK}+\frac{SC}{SM} \right).$

$\Leftrightarrow \frac{SA}{SK}+\frac{SC}{SM}$ $=\frac{SB}{SL}+\frac{SD}{SN}.$

3.

<img link="data_for_rag/toan11/images/ti-so-the-tich-16.png" alt="">

Gọi $E$ là giao điểm của $MN$ và $CD.$

Điểm $Q$ chính là giao điểm của $AD$ và $PE.$

Ta có $\frac{ED}{EC}=\frac{MB}{MC}.\frac{ND}{NB}=\frac{1}{3}$ nên $\frac{QA}{QD}=\frac{PA}{PC}.\frac{EC}{ED}=\frac{3}{2}$, do đó $\frac{AQ}{AD}=\frac{3}{5}.$

Gọi $V$, ${{V}_{1}}$, ${{V}_{2}}$ lần lượt là thể tích khối tứ diện $ABCD$, khối đa diện chứa điểm $A$ và khối đa diện chứa điểm $D$ khi chia khối tứ diện bởi mặt phẳng $(MNP)$ chia khối tứ diện.

Ta có ${{V}_{1}}={{V}_{ABMN}}+{{V}_{AMPN}}+{{V}_{APQN}}.$

Vì $\frac{{{S}_{BMN}}}{{{S}_{BCD}}}=\frac{BM.BN}{BC.BD}=\frac{1}{8}$ và $\frac{{{S}_{MNC}}}{{{S}_{BCD}}}=\frac{3}{8}$, $\frac{{{S}_{DNC}}}{{{S}_{BCD}}}=\frac{1}{2}$ nên ${{V}_{ABMN}}=\frac{1}{8}V$, ${{V}_{AMPN}}=\frac{1}{3}V.$

${{V}_{APQN}}=\frac{1}{3}.\frac{3}{5}{{V}_{ADNC}}=\frac{1}{10}V.$

${{V}_{1}}=\frac{7}{20}V$ $\Rightarrow {{V}_{1}}=\frac{7}{20}V.$

${{V}_{2}}=\frac{13}{20}V$ $\Rightarrow \frac{{{V}_{1}}}{{{V}_{2}}}=\frac{7}{13}.$

<!-- chunk:9 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 1.

1. Cho hình chóp đều $S.ABCD$ có $M$, $N$, $E$ lần lượt là trung điểm các cạnh $AB$, $AD$, $SC$. Tính tỷ số thể tích hai phần của hình chóp được cắt bởi mặt phẳng $\left( MNE \right)$.

2. Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M$, $N$, $E$ lần lượt là trung điểm các cạnh $AB$, $AD$, $SC.$ Tính tỉ số thể tích hai phần của khối chóp $S.ABCD$ khi cắt bởi mặt phẳng $(MNE).$

<!-- chunk:10 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 2.

Cho hình chóp $S.ABC$ có $SA\bot (ABC)$, $SA=a$, $AB=b$, $AC=c$, $\widehat{BAC}=\alpha .$ Gọi $M$, $N$ lần lượt là hình chiếu của điểm $A$ trên các đường thẳng $SB$, $SC.$

a) Chứng minh rằng ${{V}_{SAMN}}:{{V}_{SABC}}$ không phụ thuộc vào độ lớn $\alpha .$

b) Tính $a$ theo $b$, $c$ biết rằng mặt phẳng $(AMN)$ chia khối chóp thành hai khối đa diện có thể tích bằng nhau.

c) Tính thể tích của khối chóp $S.AMN.$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 3.

1. Cho hình hộp chữ nhật $ABCD.{A}'{B}'{C}'{D}’$ có $A{A}’=a$, $AB=b$, $AD=c.$ Mặt phẳng qua $A$, $C$ và trung điểm của ${A}'{B}’$ chia khối chữ nhật thành hai phần. Tính thể tích mỗi phần.

2. Cho khối lập phương $ABCD.{A}'{B}'{C}'{D}’$ cạnh $a.$ Gọi $M$ là trung điểm của $BC$, $N$ chia đoạn $CD$ theo tỉ số $-2.$ Mặt phẳng $({A}’MN)$ chia khối lập phương thành hai phần. Tính thể tích mỗi phần.

3. Cho khối hộp $ABCD.{A}'{B}'{C}'{D}’$ và $M$ là trung điểm ${B}'{C}’.$ Mặt phẳng $(\alpha )$ chứa $AM$ và song song với ${B}'{D}’$ chia khối hộp thành hai phần. Tính tỉ số thể tích của hai phần đó.

<!-- chunk:12 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 4.

1. Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $a$, $\widehat{ASC}={{90}^{0}}$, $SA$ lập với đáy góc $\alpha$ $({{0}^{0}}<\alpha <{{90}^{0}})$ và mặt phẳng $(SAC)$ vuông góc với mặt phẳng $(ABC).$ Tính khoảng cách từ $A$ đến $(SBC).$

2. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, cạnh bên $SA$ vuông góc với mặt phẳng đáy. Góc giữa cạnh $SC$ và mặt phẳng $(SAB)$ bằng $\varphi .$ Mặt phẳng $(\alpha )$ qua $A$ vuông góc cạnh $SC$ cắt các cạnh $SB$, $SC$, $SD$ lần lượt tại $M$, $N$, $P.$ Tính thể tích khối chóp $S.AMNP.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 5.

1. Cho hình lập phương $ABCD.{{A}_{1}}{{B}_{1}}{{C}_{1}}{{D}_{1}}$ cạnh $a.$ Các điểm $M\in B{{B}_{1}}$, $N\in D{{D}_{1}}$ sao cho $M{{B}_{1}}=N{{D}_{1}}=\frac{a}{3}$. Mặt phẳng $(AMN)$ chia hình lập phương thành hai phần. Tính thể tích mỗi phần và tỷ số thể tích hai phần đó.

2. Cho hình hộp đứng có đáy là hình thoi cạnh $a$ tam giác $ABD$ là tam giác đều. Gọi $M$, $N$ lần lượt là trung điểm của các cạnh $BC$, $C’D’$. Tính khoảng cách từ $D$ đến mặt phẳng $(AMN)$ biết rằng $MN\bot B’D$.

3. Cho lăng trụ $ABC.A’B’C’$ có thể tích bằng thể tích khối lập phương cạnh $a$. Trên các cạnh $AA’$, $BB’$ lấy $M$, $N$ sao cho $\frac{AM}{AA’}=\frac{BN}{BB’}=\frac{1}{3}$. Gọi $E$, $F$ lần lượt là giao điểm của $CM$ với $C’A’$ và $CN$ với $C’B’$.

a) Mặt phẳng $(CMN)$ chia khối lăng trụ thành hai phần. Tính tỉ số thể tích hai phần đó.

b) Tính thể tích khối chóp $C’CEF$.

4. Cho hình lăng trụ tam giác $ABC.{A}'{B}'{C}’.$ Gọi $M$, $N$, $P$ lần lượt là trung điểm của các cạnh ${A}'{B}’$, $BC$, $C{C}’.$ Mặt phẳng $(MNP)$ chia khối chóp thành hai phần. Tính tỉ số thể tích của hai phần đó.

<!-- chunk:14 level:4 source:https://toanmath.com/2019/04/ti-so-the-tich.html -->
## Bài tập 6.

1. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang cân có đường chéo $BD$ vuông góc với cạnh bên $BC$, $BD$ là tia phân giác trong của góc $\widehat{ADC}$, $BC=3cm$, $SA=x$ $(x>0)$, $SA\bot (ABCD).$ Gọi $N$ là một điểm trên cạnh $SC$. Mặt phẳng $(\alpha )$ qua $A$, $N$ song song với $BD$ cắt các cạnh $SB$, $SD$ lần lượt tại $M$, $P.$

a) Tính thể tích khối chóp $S.AMNP$ biết $NC=3NS$.

b) Tìm vị trí của điểm $N$ trên cạnh $SC$ sao cho $(\alpha )$ chia khối chóp thành hai phần có thể tích bằng nhau.

2. Cho hình chóp tứ giác đều $S.ABCD$ có cạnh đáy bằng $a$, các mặt bên nghiêng đều trên đáy một góc $\varphi$. Mặt phẳng $(\alpha )$ qua $AC$ vuông góc với mặt phẳng $(SAB)$ chia khối chóp thành hai phần. Tính thể tích của mỗi phần theo $a$ và $\varphi .$