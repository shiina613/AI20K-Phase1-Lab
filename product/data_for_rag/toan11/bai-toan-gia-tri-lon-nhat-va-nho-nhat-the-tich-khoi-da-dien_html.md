# Bài toán giá trị lớn nhất và nhỏ nhất thể tích khối đa diện

<!-- chunk:0 level:0 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
Trong bài viết này, chúng ta sẽ cùng nhau đề cập đến một dạng toán nâng cao liên quan đến thể tích của khối đa diện, đó là dạng toán giá trị lớn nhất và nhỏ nhất thể tích khối đa diện, bài viết tập trung chủ yếu vào phần thể tích của khối chóp, các dạng khối đa diện khác, phương pháp tiếp cận bài toán cũng tương tự.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## A. MỘT SỐ KIẾN THỨC CẦN LƯU Ý
Phương pháp tìm giá trị lớn nhất, nhỏ nhất:

+ Nhóm bình phương và so sánh.

+ Dùng bất đẳng thức Côsi: với các số $a$, $b$, $c$ không âm thì:

$\frac{{a + b}}{2} \ge \sqrt {ab}$, dấu bằng xảy ra khi $a = b.$

$\frac{{a + b + c}}{3} \ge \sqrt[3]{{abc}}$, dấu bằng xảy ra khi $a = b = c.$

+ Dùng tam thức bậc hai.

+ Dùng đạo hàm, dựa vào tính chất đơn điệu hay lập bảng biến thiên để đánh giá.

Chú ý:

1) Hình chóp đều là chóp có các cạnh bên bằng nhau và có đáy là đa giác đều. Trong hình chóp đều thì hình chiếu của đỉnh chóp là tâm của đáy.

2) Thể tích của một khối chóp bằng một phần ba tích số của diện tích mặt đáy và chiều cao của khối chóp đó.

3) Tứ diện hay hình chóp tam giác có $4$ cách chọn đỉnh chóp.

<!-- chunk:2 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 1: Cho tứ diện $SABC$ có các góc phẳng ở đỉnh $S$ vuông. Biết rằng $SA = a$, $SB + SC = k.$ Đặt $SB = x.$ Tính thể tích tứ diện $SABC$ theo $a$, $k$, $x$ và xác định $SB$, $SC$ để thể tích tứ diện $SABC$ lớn nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-1.png" alt="">

Thể tích tứ diện:

${V_{SABC}} = \frac{1}{6}SA.SB.SC$ $= \frac{1}{6} ax (k – x)$ $\le \frac{1}{6}a{\left( {\frac{{x + k – x}}{2}} \right)^2} = \frac{{a{k^2}}}{{24}}.$

Dấu bằng xảy ra khi $x = k – x \Leftrightarrow x = \frac{k}{2}.$

<!-- chunk:3 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 2: Cho tam giác $ABC$, $AB = AC.$ Một điểm $M$ thay đổi trên đường thẳng vuông góc với mặt phẳng $(ABC)$ tại $A.$

a) Tìm quỹ tích trọng tâm $G$ của tam giác $MBC.$

b) Gọi $O$ là trực tâm của tam giác $ABC$, hãy xác định vị trí của $M$ để thể tích tứ diện $OHBC$ đạt giá trị lớn nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-2.png" alt="">

Gọi $D$ là trung điểm của $BC.$

Ta có: $MB = MC.$

Do đó $MD \bot BC$ và trọng tâm $G$ của tam giác $MBC$ nằm trên $MD$ thoả mãn hệ thức: $\overrightarrow {DG} = \frac{1}{2}\overrightarrow {DM} .$

Do đó $G$ là ảnh của $M$ trong phép vị tự tâm $D$, tỉ số vị tự $\frac{1}{3}.$

Vậy quỹ tích các trọng tâm $G$ của tam giác $MBC$ là đường $d’$ vuông góc với mặt phẳng $(ABC)$ tại trọng tâm $G’$ của tam giác $ABC.$

b) Hạ $CE \bot AB$, $CF \bot MB$ ta có $H = DM \cap CF$ là trực tâm của tam giác $MBC$, $O = DA \cap CE$ là trực tâm của tam giác $ABC.$

Gọi $HH’$ là chiều cao của tứ diện $OHBC$, ta có $H’$ thuộc $DO.$

Hình chóp này có đáy $OBC$ cố định nên ${V_{OHBC}}$ lớn nhất khi và chỉ khi $HH’$ lớn nhất. Điểm $H$ chạy trên đường tròn đường kính $OD$ nên $HH’$ lớn nhất khi $HH’ = \frac{1}{2}DO$ nghĩa là $DHH’$ là tam giác vuông cân tại $H’$, suy ra tam giác $DMA$ lúc đó vuông cân tại $A.$

Vậy tứ diện $OHBC$ có thể tích đạt giá trị lớn nhất, cần chọn $M$ trên $d$ (về hai phía của $A$) sao cho $AM = AD.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 3: Cho ba tia $Ox$, $Oy$, $Oz$ vuông góc với nhau từng đội một tạo tam diện $Oxyz.$ Điểm $M$ cố định nằm trong góc tam diện. Một mặt phẳng qua $M$ cắt $Ox$, $Oy$, $Oz$ lần lượt tại $A$, $B$, $C.$ Gọi khoảng cách từ $M$ đến các mặt phẳng $(OBC)$, $(OCA)$, $(OAB)$ lần lượt là $a$, $b$, $c.$

a) Chứng minh: $\frac{a}{{OA}} + \frac{b}{{OB}} + \frac{c}{{OC}} = 1.$

b) Tính $OA$, $OB$, $OC$ theo $a$, $b$, $c$ để tứ diện $OABC$ có thể tích nhỏ nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-3.png" alt="">

a) Ta có: ${V_{OABC}} = {V_{MOAB}} + {V_{MOBC}} + {V_{MOCA}}$ nên $\frac{1}{6}OA.OB.OC$ $= \frac{1}{6}OA.OB.c + \frac{1}{6}OB.OC.a + \frac{1}{6}OC.OA.b.$

Do đó: $1 = \frac{a}{{OA}} + \frac{b}{{OB}} + \frac{c}{{OC}}.$

b) Điểm $M$ cố định tức là các số $a$, $b$, $c$ không đổi.

Ta có: $V = \frac{1}{6}OA.OB.OC.$

Do đó $V$ nhỏ nhất $\Leftrightarrow OA.OB.OC$ nhỏ nhất.

Áp dụng bất đẳng thức Cô si:

$1 = \frac{a}{{OA}} + \frac{b}{{OB}} + \frac{c}{{OC}}$ $\ge 3\sqrt[3]{{\frac{{abc}}{{OA.OB.OC}}}}$ $\Leftrightarrow OA.OB.OC \ge 27abc.$

$OA.OB.OC$ nhỏ nhất $\Leftrightarrow \frac{a}{{OA}} = \frac{b}{{OB}} = \frac{c}{{OC}}.$

Vậy: $V$ nhỏ nhất khi và chỉ khi $OA = 3a$, $OB = 3b$, $OC = 3c.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 4: Khối chóp tam giác $S.ABC$ có đáy $ABC$ là tam giác vuông cân đỉnh $C$ $\left( {\widehat C = {{90}^0}} \right)$ và $SA \bot (ABC)$, $SC = a.$ Hãy tìm góc giữa hai mặt phẳng $(SCB)$ và $(ABC)$ để thể tích khối chóp lớn nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-4.png" alt="">

Ta có $BC \bot AC$ $\Rightarrow BC \bot SC.$

Mặt khác $BC \bot AC$ suy ra góc $SCA$ là góc giữa hai mặt phẳng $(SCB)$ và $(ABC).$

Đặt $\widehat {SCA} = x.$

Khi đó $SA = a\sin x$, $AC = a\cos x.$

${V_{S.ABC}} = \frac{{a\sin x}}{3}.\frac{{{a^2}{{\cos }^2}x}}{2}$ $= \frac{{{a^3}}}{6}\sin x.{\cos ^2}x.$

Xét hàm số $y = \sin x{\cos ^2}x$ với $0 < x < \frac{\pi }{2}.$

Ta có $y’ = {\cos ^3}x – 2\cos x{\sin ^2}x$ $= \cos x\left( {{{\cos }^2}x – 2 + 2{{\cos }^3}x} \right)$ $= \cos x\left( {3{{\cos }^2}x – 2} \right)$ $= 3\cos x\left( {\cos x – \sqrt {\frac{2}{3}} } \right)\left( {\cos x + \sqrt {\frac{2}{3}} } \right).$

$y’ = 0 \Leftrightarrow \cos x = \sqrt {\frac{2}{3}} = \cos \alpha$ với $0 < \alpha < \frac{\pi }{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-5.png" alt="">

Vậy ${S_{S.ABC}}$ đạt giá trị lớn nhất khi $x = \alpha$, $0 < \alpha < \frac{\pi }{2}$ và $\cos \alpha = \sqrt {\frac{2}{3}} .$

<!-- chunk:6 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 5: Cho khối chóp tứ giác đều $S.ABCD$ mà khoảng cách từ đỉnh $A$ đến mặt phẳng $(SBC)$ bằng $2a.$ Với giá trị nào của góc giữa mặt bên và mặt đáy của khối chóp thì thể tích của khối chóp nhỏ nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-6.png" alt="">

Hạ $SO \bot (ABCD)$ thì $O$ là tâm hình vuông $ABCD.$

Gọi $EH$ là đường trung bình của hình vuông $ABCD.$

Vì $AD//BC \Rightarrow AD//(SBC).$

$\Rightarrow d(A,(SBC)) = d(E,(SBC)).$

Hạ $EK \bot SH$, ta có: $EK \bot (SBC).$

$\Rightarrow EK = d(A,(SBC)) = 2a.$

Ta có $BC \bot SH$, $SB \bot OH.$

$\Rightarrow \widehat {SHO}$ là góc giữa mặt bên $(SBC)$ và mặt phẳng đáy.

Đặt $\widehat {SHO} = x.$

Khi đó: $EH = \frac{{2a}}{{\sin x}}$, $OH = \frac{a}{{\sin x}}$, $SO = \frac{a}{{\sin x}}\tan x = \frac{a}{{\cos x}}.$

Vậy ${V_{S.ABCD}} = \frac{1}{3}{S_{ABCD}}.SO = \frac{{4{a^3}}}{{3\cos x{{\sin }^2}x}}.$

Do đó ${V_{S.ABCD}}$ nhỏ nhất $\Leftrightarrow y = \cos x.{\sin ^2}x$ đạt giá trị lớn nhất.

Ta có: $y’ = – {\sin ^3}x + 2\sin x{\cos ^2}x$ $= \sin x\left( {2{{\cos }^2}x – {{\sin }^2}x} \right)$ $= \sin x\left( {2 – 3{{\sin }^2}x} \right)$ $= 3\sin x\left( {\sqrt {\frac{2}{3}} – \sin x} \right)\left( {\sqrt {\frac{2}{3}} + \sin x} \right).$

$y’ = 0 \Leftrightarrow \sin x = \sqrt {\frac{2}{3}} .$

Xét giá trị $\alpha$ sao cho: $\sin \alpha = \sqrt {\frac{2}{3}}$, $0 < \alpha < \frac{\pi }{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-7.png" alt="">

Vậy ${V_{S.ABCD}}$ đạt giá trị nhỏ nhất $\Leftrightarrow x = \alpha$, $0 < \alpha < \frac{\pi }{2}$ và $\sin \alpha = \sqrt {\frac{2}{3}} .$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 6: Trên cạnh $AD$ của hình vuông $ABCD$ có độ dài cạnh là $a$, lấy điểm $M$ sao cho: $AM = x$ $(0 \le x \le a).$ Trên nửa đường thẳng $Az$ vuông góc với mặt phẳng chứa hình vuông tại điểm $A$, lấy điểm $S$ sao cho $SA = y$ $(y > 0).$

a) Chứng minh rằng $(SAB) \bot (SBC)$ và tính khoảng cách từ điểm $M$ đến mặt phẳng $(SAC).$

b) Tính thể tích khối chóp $S.ABCM$ theo $a$, $y$ và $x$. Giả sử ${x^2} + {y^2} = {a^2}$ tìm giá trị lớn nhất của thể tích khối chóp $S.ABCM.$

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-8.png" alt="">

a) Ta có $BC \bot AB$, $BC \bot SA$ nên $BC \bot (SAB).$

Do đó $(SAB) \bot (SBC).$

Vì $(SAC) \bot (ABCD)$ theo giao tuyến $AC$ nên hạ $MH \bot AC$ thì $MH \bot (SAC).$

Vậy $MH$ là khoảng cách từ $M$ tới mặt phẳng $(SAC).$

Trong tam giác vuông $AMH$ có:

$MH = x.\sin {45^0} = \frac{{\sqrt 2 x}}{2}.$

b) Hình chóp $S.ABCM$ có đường cao $SA = y$ và có đáy là hình thang vuông nên diện tích đáy là $S = \frac{1}{2}a(a + x).$

Do đó thể tích khối chóp $S.ABCM$ là:

$V = \frac{1}{3}y.\frac{1}{2}a(a + x) = \frac{1}{6}ya(a + x).$

Theo giả thiết ${x^2} + {y^2} = {a^2} \Rightarrow {y^2} = {a^2} – {x^2}$ nên:

${V^2} = \frac{1}{{36}}{a^2}\left( {{a^2} – {x^2}} \right){(x + a)^2}$ $= \frac{1}{{36}}{a^2}(a – x){(a + x)^3}.$

Đặt $f(x) = {V^2}$ với $0 \le x \le a$, ta có:

$f'(x) = – \frac{{{a^2}}}{{36}}{(a + x)^3} + \frac{{{a^3}}}{{36}}3(a – x){(a + x)^2}$ $= \frac{{{a^2}{{(a + x)}^2}(2a – 4x)}}{{36}}.$

$f'(x) = 0 \Leftrightarrow x = \frac{a}{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-9.png" alt="">

Vậy $f(x)$ đạt giá trị lớn nhất tại $x = \frac{a}{2}$, khi đó thể tích của khối chóp $S.ABCM$ đạt giá trị lớn nhất là: $V = \sqrt {f{{(x)}_{\max }}} = \frac{{{a^3}\sqrt 3 }}{8}.$

<!-- chunk:8 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 7: Cho hình chóp $S.ABCD$ có bảy cạnh bằng $1$ và cạnh bên $SC = x.$ Định $x$ để thể tích khối chóp là lớn nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-10.png" alt="">

Đáy $ABCD$ có $4$ cạnh bằng $1$ nên đáy là một hình thoi $\Rightarrow AC \bot BC.$

Ba tam giác $ABD$, $CBD$, $BSD$ có chung cạnh $BD$, các cạnh còn lại bằng nhau và bằng $1$ nên bằng nhau, các trung tuyến $AO$, $SO$ và $CO$ bằng nhau.

Suy ra tam giác $ASC$ vuông tại $S$, ta được $AC = \sqrt {{x^2} + 1} .$

Gọi $H$ là hình chiếu đỉnh $S$ trên đáy $(ABCD).$

Do $SA = SB = SD = 1$ nên $HA = HB = HD$, suy ra $H$ là tâm đường tròn ngoại tiếp tam giác $ABD$ $\Rightarrow H \in AC$ $\Rightarrow SH$ là đường cao của tam giác vuông $ASC.$

Ta có $SH.AC = SA.SC$ $\Rightarrow SH = \frac{x}{{\sqrt {{x^2} + 1} }}.$

$O{B^2} = A{B^2} – O{A^2}$ $= 1 – {\left( {\frac{{\sqrt {{x^2} + 1} }}{2}} \right)^2} = \frac{{3 – {x^2}}}{4}$ $\Rightarrow OB = \frac{1}{2}\sqrt {3 – {x^2}} .$

Điều kiện ${x^2} < 3 \Leftrightarrow 0 < x < \sqrt 3 .$

Ta có ${S_{ABCD}} = AC.OB$ $= \frac{1}{2}\sqrt {{x^2} + 1} .\sqrt {3 – {x^2}}$ $= \frac{1}{2}\sqrt {\left( {{x^2} + 1} \right)\left( {3 – {x^2}} \right)} .$

Vậy ${V_{SABCD}} = \frac{1}{3}{S_{ABCD}}.SH = \frac{1}{6}x\sqrt {3 – {x^2}} .$

Ta có thể dùng đạo hàm hay bất đẳng thức Côsi:

$V = \frac{1}{6}\sqrt {{x^2}\left( {3 – {x^2}} \right)}$ $\le \frac{1}{6}.\frac{{{x^2} + 3 – {x^2}}}{2} = \frac{1}{4}.$

Dấu bằng khi ${x^2} = 3 – {x^2}$ $\Leftrightarrow 2{x^2} = 3$ $\Leftrightarrow x = \frac{{\sqrt 6 }}{2}.$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/04/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien.html -->
## Bài toán 8: Cho hình chóp $S.ABC$ có đáy là tam giác $ABC$ vuông cân tại đỉnh $B$, $BA = BC = 2a$, hình chiếu vuông góc của $S$ trên mặt phẳng đáy $(ABC)$ là trung điểm $E$ của $AB$ và $SE = 2a.$ Gọi $I$, $J$ lần lượt là trung điểm của $EC$, $SC$, $M$ là điểm di động trên tia đối của tia $BA$ sao cho $\widehat {ECM} = \alpha$ $\left( {\alpha < {{90}^0}} \right)$ và $H$ là hình chiếu vuông góc của $S$ trên $MC.$ Tính thể tích của khối tứ diện $EHIJ$ theo $a$, $\alpha$ và tìm $\alpha$ để thể tích đó lớn nhất.

<img link="data_for_rag/toan11/images/bai-toan-gia-tri-lon-nhat-va-nho-nhat-the-tich-khoi-da-dien-11.png" alt="">

Vì $SE \bot (ABC)$, $SH \bot CM$ nên $EH \bot CM.$

$CE = \sqrt {B{C^2} + B{E^2}}$ $= \sqrt {4{a^2} + {a^2}} = a\sqrt 5 .$

Mà $IJ$ là đường trung bình trong tam giác $SCE$ nên $IJ = \frac{{SE}}{2} = a.$

Hơn nữa $IJ//SE \Rightarrow IJ \bot (ABC).$

Trong tam giác vuông $CEH$ với góc $\widehat {ECH} = \alpha$ và trung tuyến $HI$ ta có:

${S_{EHI}} = \frac{1}{2}{S_{ECH}} = \frac{1}{4}EH.CH$ $= \frac{1}{4}CE.\sin \alpha .CE.\cos \alpha$ $= \frac{5}{8}{a^2}\sin 2\alpha .$

Thể tích của khối tứ diện $EHIJ$ là:

${V_{EHIJ}} = \frac{1}{3}IJ.{S_{EHI}}$ $= \frac{a}{3}.\frac{{5{a^2}}}{8}.\sin 2\alpha = \frac{5}{{24}}{a^3}\sin 2\alpha .$

Thể tích tứ diện $EHIJ$ lớn nhất khi và chỉ khi: $\sin 2\alpha = 1 \Leftrightarrow \alpha = {45^0}.$