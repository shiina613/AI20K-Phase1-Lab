# Khoảng cách giữa hai đường thẳng chéo nhau

<!-- chunk:0 level:0 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
Bài viết trình bày phương pháp tính khoảng cách giữa hai đường thẳng chéo nhau trong không gian, đây là dạng toán thường gặp trong chương trình hình Hình học 11 chương 3 – quan hệ vuông góc, kiến thức và các ví dụ trong bài viết được tham khảo từ chuyên mục hình học không gian đăng trên TOANMATH.com.

Để tính khoảng cách giữa hai đường thẳng chéo nhau $Δ$ và $Δ’$, ta sử dụng các phương pháp sau đây:

Phương pháp 1: Chọn mặt phẳng $(α)$ chứa đường thẳng $Δ$ và song song với $Δ’$. Khi đó $d(\Delta ,\Delta’) = d(\Delta’,(\alpha ))$.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-1.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-1">

<!-- chunk:1 level:3 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Ví dụ 1: Cho hình chóp $S.ABCD$ có $SA \bot \left( {ABCD} \right)$, đáy $ABCD$ là hình chữ nhật với $AC = a\sqrt 5$ và $BC = a\sqrt 2$. Tính khoảng cách giữa $SD$ và $BC.$

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-2.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-2">

Ta có $BC // (SAD).$

Suy ra $d\left( {BC;SD} \right) = d\left( {BC;\left( {SAD} \right)} \right)$ $= d\left( {B;\left( {SAD} \right)} \right).$

Mà 
$$
\left\{ \begin{array}{l}
AB \bot AD\\
AB \bot SA
\end{array} \right. \Rightarrow AB \bot \left( {SAD} \right)
$$
 $\Rightarrow d\left( {B;\left( {SAD} \right)} \right) = AB.$

Ta có $AB = \sqrt {A{C^2} – B{C^2}}$ $= \sqrt {5{a^2} – 2{a^2}} = \sqrt 3 a.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Ví dụ 2: Cho hình lăng trụ đứng $ABC.A’B’C’$ có đáy là tam giác vuông tại $B$, $AB = BC = a$, cạnh bên ${\rm{AA}}’ = \sqrt 2.$ Gọi $M$ là trung điểm của $BC$. Tính $d\left( {AM;B’C} \right)$.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-3.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-3">

Trước hết ta đi dựng $1$ mặt phẳng chứa đường này và song song với đường kia để chuyển về khoảng cách từ $1$ điểm đến mặt phẳng. Lấy $E$ là trung điểm $BB’.$

$\Rightarrow ME//CB’ \Rightarrow CB’//(AME).$

$\Rightarrow d(AM;B’C) = d(B’C;(AME))$ $= d(C;(AME)) = d(B;(AME)).$

Mà tứ diện $BAME$ vuông ở $B$ nên:

$\frac{1}{{{d^2}(B;(AME))}}$ $= \frac{1}{{B{M^2}}} + \frac{1}{{B{E^2}}} + \frac{1}{{B{A^2}}}$ $= \frac{1}{{{{\left( {\frac{a}{2}} \right)}^2}}} + \frac{1}{{{{\left( {\frac{{a\sqrt 2 }}{2}} \right)}^2}}} + \frac{1}{{{a^2}}}$ $= \frac{4}{{{a^2}}} + \frac{4}{{2{a^2}}} + \frac{1}{{{a^2}}} = \frac{7}{{{a^2}}}.$

$\Rightarrow d(B;(AME)) = \frac{a}{{\sqrt 7 }}$ $= d(AM;B’C).$

**Phương pháp 2:** Dựng hai mặt phẳng song song và lần lượt chứa hai đường thẳng. Khoảng cách giữa hai mặt phẳng đó là khoảng cách cần tìm.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-4.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-4">

Ta có $d(Δ,Δ’) = d((α),(β)).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Ví dụ 3: Hình hộp chữ nhật $ABCD.A’B’C’D’$ có $AB = 3$, $AD = 4$, $AA’ = 5$. Khoảng cách giữa hai đường thẳng $AC$ và $B’D’$ bằng bao nhiêu?

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-10.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-10">

Ta có:

$(ABCD) // (A’B’C’D’).$

$AC ⊂ (ABCD)$ và $B’D’ ⊂ (A’B’C’D’).$

Nên $d(AC,B’D’) = d((ABCD),(A’B’C’D’)$ $= AA’ = 5.$

[ads]

Phương pháp 3: Dựng đoạn vuông góc chung và tính độ dài đoạn đó. Ta xét 2 trường hợp sau:

1. Trường hợp 1: $Δ$ và $Δ’$ vừa chéo nhau vừa vuông góc với nhau

+ Bước 1: Chọn mặt phẳng $(α)$ chứa $Δ’$ và vuông góc với $Δ$ tại $I.$

+ Bước 2: Trong mặt phẳng $(α)$ kẻ $IJ \bot \Delta’$.

Khi đó $IJ$ là đoạn vuông góc chung của hai đường thẳng $Δ$ và $Δ’$, và $d(\Delta ,\Delta’) = IJ$.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-5.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-5">

<!-- chunk:4 level:3 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Ví dụ 4: Cho hình lập phương $ABCD.A’B’C’D’$ cạnh bằng $a$. Xác định đoạn vuông góc chung và tính khoảng cách giữa hai đường thẳng $AD’$ và $A’B’$ bằng bao nhiêu?

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-6.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-6">

Ta có $A’B’ \bot \left( {ADD’A’} \right).$

Gọi $H$ là giao điểm của $AD’$ với $A’D$. Vì $ADD’A’$ là hình vuông nên $A’H \bot AD’.$

Ta có 
$$
\left\{ \begin{array}{l}
A’H \bot AD’\\
A’H \bot A’B’
\end{array} \right.
$$
, suy ra $A’H$ là đoạn vuông góc chung của hai đường thẳng $AD’$ và $A’B’.$

$d\left( {A’B’;AD’} \right) = A’H = \frac{{a\sqrt 2 }}{2}.$

2. Trường hợp 2: $Δ$ và $Δ’$ chéo nhau mà KHÔNG vuông góc với nhau

Ta dựng đoạn vuông góc chung của hai đường thẳng $Δ$ và $Δ’$ theo một trong hai cách sau đây:

Cách 1:

+ Bước 1: Chọn mặt phẳng $(α)$ chứa $Δ’$ và song song với $Δ.$

+ Bước 2: Dựng $d$ là hình chiếu vuông góc của $Δ$ xuống $(α)$ bằng cách lấy điểm $M \in \Delta$ dựng đoạn $MN \bot \left( \alpha \right)$, lúc đó $d$ là đường thẳng đi qua $N$ và và song song với $Δ.$

+ Bước 3: Gọi $H = d \cap \Delta’$, dựng $HK\parallel MN$.

Khi đó $HK$ là đoạn vuông góc chung của $Δ$ và $Δ’$, và $d(\Delta ,\Delta’) = HK = MN$.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-7.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-7">

Cách 2:

+ Bước 1: Chọn mặt phẳng $(α) ⊥ Δ$ tại $I.$

+ Bước 2: Tìm hình chiếu $d$ của $Δ’$ xuống mặt phẳng $(α).$

+ Bước 3: Trong mặt phẳng $(α)$, dựng $IJ \bot d$, từ $J$ dựng đường thẳng song song với $Δ$ cắt $Δ’$ tại $H$, từ $H$ dựng $HM\parallel IJ$.

Khi đó $HM$ là đoạn vuông góc chung của hai đường thẳng $Δ$ và $Δ’$, và $d(\Delta ,\Delta ‘) = HM = IJ$.

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-8.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-8">

<!-- chunk:5 level:3 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Ví dụ 5: Cho hình chóp $SABC$ có $SA = 2a$ và vuông góc với mặt phẳng $(ABC)$, đáy $ABC$ là tam giác vuông cân tại $B$ với $AB = a$. Gọi $M$ là trung điểm của $AC.$

1. Hãy dựng đoạn vuông góc chung của $SM$ và $BC.$

2. Tính độ dài đoạn vuông góc chung của $SM$ và $BC.$

<img link="data_for_rag/toan11/images/khoang-cach-giua-hai-duong-thang-cheo-nhau-9.png" alt="khoang-cach-giua-hai-duong-thang-cheo-nhau-9">

1. Để dựng đoạn vuông góc chung của $SM$ và $BC$ ta có thể lựa chọn 1 trong 2 cách sau:

Cách 1: Gọi $N$ là trung điểm của $AB$, suy ra: $BC//MN \Rightarrow BC//\left( {SMN} \right).$

Ta có: 
$$
\left\{ \begin{array}{l}
MN \bot AB\\
MN \bot SA
\end{array} \right. \Rightarrow MN \bot \left( {SAB} \right)
$$
 $\Rightarrow \left( {SMN} \right) \bot \left( {SAB} \right).$

$\left( {SMN} \right) \cap \left( {SAB} \right) = SN.$

Hạ $BH \bot SN \Rightarrow BH \bot \left( {SMN} \right).$

Từ $H$ dựng $Hx$ song song với $BC$ và cắt $SM$ tại $E$. Từ $E$ dựng $Ey$ song song với $BH$ và cắt $BC$ tại $F$. Đoạn $EF$ là đoạn vuông góc chung của $SM$ và $BC.$

Cách 2: Nhận xét rằng: 
$$
\left\{ \begin{array}{l}
BC \bot AB\\
BC \bot SA
\end{array} \right. \Rightarrow BC \bot \left( {SAB} \right).
$$

Do đó $(SAB)$ chính là mặt phẳng qua $B$ thuộc $BC$ và vuông góc với $BC.$

Gọi $N$ là trung điểm của $AB$ suy ra: $MN//BC \Rightarrow MN \bot \left( {SAB} \right)$.

Suy ra $MN$ là hình chiếu vuông góc của $SM$ trên $(SAB).$

Hạ $BH \bot SN \Rightarrow BH \bot \left( {SMN} \right)$.

Từ $H$ dựng $Hx$ song song với $BC$ và cắt $SM$ tại $E$. Từ $E$ dựng $Ey$ song song với $BH$ và cắt $BC$ tại $F.$

Đoạn $EF$ là đoạn vuông góc chung của $SM$ và $BC.$

2. Nhận xét rằng tam giác $SAN$ và tam giác $BHN$ là $2$ tam giác vuông có $2$ góc nhọn đối đỉnh nên chúng đồng dạng, suy ra:

$\frac{{BH}}{{SA}} = \frac{{BN}}{{SN}} \Rightarrow BH = \frac{{SA.BN}}{{SN}}.$

Trong đó: $BN = \frac{1}{2}AB = \frac{a}{2}.$

$S{N^2} = S{A^2} + A{N^2}$ $= {\left( {2a} \right)^2} + {\left( {\frac{a}{2}} \right)^2} = \frac{{17{a^2}}}{4}$ $\Rightarrow SN = \frac{{a\sqrt {17} }}{2}.$

Suy ra: $BH = \frac{{2a.\frac{a}{2}}}{{\frac{{a\sqrt {17} }}{2}}} = \frac{{2a\sqrt {17} }}{{17}}.$

Vậy khoảng cách giữa $SM$ và $BC$ bằng $\frac{{2a\sqrt {17} }}{{17}}$.

<!-- chunk:6 level:2 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Bài toán 1: Cho tứ diện $ABCD$ có $AB = x$, $CD = b$, các cạnh còn lại đều bằng $a.$ Gọi

$E$ và $F$ lần lượt là trung điểm $AB$ và $CD.$

a) Chứng minh $AB \bot CD$ và $EF$ là đường vuông góc chung của $AB$ và $CD.$ Tính $EF$ theo $a$, $b$, $x$.

b) Tìm $x$ để hai mặt phẳng $(ACD)$ và $(BCD)$ vuông góc.

<!-- chunk:7 level:2 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Bài toán 2: Cho hình vuông $ABCD.$ Gọi $I$ là trung điểm $AB.$ Vẽ $SI \bot (ABCD)$ với $SI = \frac{{a\sqrt 3 }}{2}$. Gọi $M$, $N$, $K$ lần lượt là trung điểm $BC$, $SD$, $SB.$ Dựng và tính đoạn vuông góc chung của:

a) $NK$ và $AC.$

b) $MN$ và $AK.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Bài toán 3: Cho hình lập phương $ABCD.A’B’C’D’$ cạnh $a.$

a) Tính theo $a$ khoảng cách giữa hai đường thẳng $A’B$ và $DB’.$

b) Gọi $M$, $N$, $P$ lần lượt là trung điểm $BB’$, $CD$, $A’D’.$ Tính góc của hai đường thẳng $MP$ và $C’N.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/02/khoang-cach-giua-hai-duong-thang-cheo-nhau.html -->
## Bài toán 5: Cho hai hình chữ nhật $ABCD$, $ABEF$ không cùng thuộc một mặt phẳng và $AB = a$, $AD = AF = a\sqrt 2$, $AC$ vuông góc $BF.$

a) Gọi $I$ là giao điểm của $DF$ với mặt phẳng chứa $AC$ và song song $BF.$ Tính $\frac{{DI}}{{DF}}.$

b) Tính khoảng cách giữa $AC$ và $BF.$