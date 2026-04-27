# Tìm giao tuyến của hai mặt phẳng

<!-- chunk:0 level:0 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
Bài viết hướng dẫn phương pháp tìm giao tuyến của hai mặt phẳng thông qua các ví dụ minh họa có lời giải chi tiết.

**Phương pháp

**+ Giao tuyến là đường thẳng chung của hai mặt phẳng, có nghĩa giao tuyến là đường thẳng vừa thuộc mặt phẳng này vừa thuộc mặt phẳng kia.

+ Muốn tìm giao tuyến của hai mặt phẳng, ta tìm hai điểm chung thuộc cả hai mặt phẳng, nối hai điểm chung đó được giao tuyến cần tìm.

+ Về dạng toán này, điểm chung thứ nhất thường dễ tìm, điểm chung còn lại ta phải tìm hai đường thẳng lần lượt thuộc hai mặt phẳng, đồng thời cùng thuộc một mặt phẳng thứ ba mà chúng không song song với nhau, giao điểm của hai đường thẳng đó là điểm chung thứ hai.

Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 1: Cho tứ giác $ABCD$ sao cho các cạnh đối không song song với nhau. Lấy một điểm $S$ không thuộc mặt phẳng $(ABCD)$. Xác định giao tuyến của hai mặt phẳng:

a) Mặt phẳng $(SAC)$ và mặt phẳng $(SBD).$

b) Mặt phẳng $(SAB)$ và mặt phẳng $(SCD).$

c) Mặt phẳng $(SAD)$ và mặt phẳng $(SBC).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-1.png" alt="tim-giao-tuyen-cua-hai-mat-phang-1">

a) Ta có: $S \in \left( {SAC} \right) \cap \left( {SBD} \right)$ $(1).$

Trong mặt phẳng $(ABCD)$ gọi $O = AC \cap BD.$

Vì 
$$
\left\{ \begin{array}{l}
O \in AC,AC \subset \left( {SAC} \right)\\
O \in BD,BD \subset \left( {SBD} \right)
\end{array} \right.
$$
 $\Rightarrow O \in \left( {SAC} \right) \cap \left( {SBD} \right)$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\left( {SAC} \right) \cap \left( {SBD} \right) = SO.$

b) Ta có: $S \in \left( {SAB} \right) \cap \left( {SCD} \right)$ $(3).$

Trong mặt phẳng $(ABCD)$ gọi $E = AB \cap CD.$

Vì: 
$$
\left\{ \begin{array}{l}
E \in AB,AB \subset \left( {SAB} \right)\\
E \in CD,CD \subset \left( {SCD} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {SAB} \right) \cap \left( {SCD} \right)$ $(4).$

Từ $(3)$ và $(4)$ suy ra: $\left( {SAB} \right) \cap \left( {SCD} \right) = SE.$

c) Ta có: $S \in \left( {SAD} \right) \cap \left( {SBC} \right)$ $(5).$

Trong mặt phẳng $(ABCD)$ gọi $F = AD \cap BC.$

Vì 
$$
\left\{ \begin{array}{l}
F \in AD,AD \subset \left( {SAD} \right)\\
F \in BC,BC \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow F \in \left( {SAD} \right) \cap \left( {SBC} \right)$ $(6).$

Từ $(5)$ và $(6)$ suy ra: $\left( {SAD} \right) \cap \left( {SBC} \right) = SF.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 2: Cho tứ diện $ABCD$. Gọi $I, J$ lần lượt là trung điểm các cạnh $AD, BC.$

a) Tìm giao tuyến của hai mặt phẳng $(IBC)$ và mặt phẳng $(JAD).$

b) Lấy điểm $M$ thuộc cạnh $AB$, $N$ thuộc cạnh $AC$ sao cho $M,N$ không là trung điểm. Tìm giao tuyến của hai mặt phẳng $(IBC)$ và mặt phẳng $(DMN).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-2.png" alt="tim-giao-tuyen-cua-hai-mat-phang-2">

a) Tìm giao tuyến của $2$ mặt phẳng $(IBC)$ và $(JAD).$

Ta có:

$$
\left\{ \begin{array}{l}
I \in \left( {IBC} \right)\\
I \in AD,AD \subset \left( {JAD} \right)
\end{array} \right.
$$
 $\Rightarrow I \in \left( {IBC} \right) \cap \left( {JAD} \right)$ $(1).$

$$
\left\{ \begin{array}{l}
J \in \left( {JAD} \right)\\
J \in BC,BC \subset \left( {IBC} \right)
\end{array} \right.
$$
 $\Rightarrow J \in \left( {IBC} \right) \cap \left( {JAD} \right)$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\left( {IBC} \right) \cap \left( {JAD} \right) = IJ.$

b) Tìm giao tuyến của $2$ mặt phẳng $(IBC)$ và $(DMN)$.

Trong mặt phẳng $(ABD)$ gọi $E = BI \cap DM.$

Vì 
$$
\left\{ \begin{array}{l}
E \in BI,BI \subset \left( {IBC} \right)\\
E \in DM,DM \subset \left( {DMN} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {IBC} \right) \cap \left( {DMN} \right)$ $(3).$

Trong mặt phẳng $(ACD)$ gọi $F = CI \cap DN.$

Vì 
$$
\left\{ \begin{array}{l}
F \in CI,CI \subset \left( {IBC} \right)\\
F \in DN,DN \subset \left( {DMN} \right)
\end{array} \right.
$$
 $\Rightarrow F \in \left( {IBC} \right) \cap \left( {DMN} \right)$ $(4).$

Từ $(3)$ và $(4)$ suy ra: $\left( {IBC} \right) \cap \left( {DMN} \right) = EF.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 3: Cho tứ diện $ABCD$. Lấy điểm $M$ thuộc cạnh $AB$, $N$ thuộc cạnh $AC$ sao cho $MN$ cắt $BC$. Gọi $I$ là điểm bên trong tam giác $BCD.$ Tìm giao tuyến của hai mặt phẳng:

a) Mặt phẳng $(MNI)$ và mặt phẳng $(BCD).$

b) Mặt phẳng $(MNI)$ và mặt phẳng $(ABD).$

c) Mặt phẳng $(MNI)$ và mặt phẳng $(ACD).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-3.png" alt="tim-giao-tuyen-cua-hai-mat-phang-3">

a) Mặt phẳng $(MNI)$ và mặt phẳng $(BCD).$

Gọi $H = MN \cap BC$ $\left( {MN,BC \subset \left( {ABC} \right)} \right).$

Ta có:

$I \in \left( {IMN} \right) \cap \left( {BCD} \right)$ $(1).$

$$
\left\{ \begin{array}{l}
H \in MN,MN \subset \left( {IMN} \right)\\
H \in BC,BC \subset \left( {BCD} \right)
\end{array} \right.
$$
 $\Rightarrow H \in \left( {IMN} \right) \cap \left( {BCD} \right)$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\left( {IMN} \right) \cap \left( {BCD} \right) = HI.$

b) Mặt phẳng $(MNI)$ và mặt phẳng $(ABD).$

Trong mặt phẳng $(BCD)$, gọi $E$ và $F$ lần lượt là giao điểm của $HI$ với $BD$ và $CD.$

Ta có:

$$
\left\{ \begin{array}{l}
M \in \left( {MNI} \right)\\
M \in AB \subset \left( {ABD} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {MNI} \right) \cap \left( {ABD} \right)$ $(3).$

$$
\left\{ \begin{array}{l}
E \in HI \subset \left( {MNI} \right)\\
E \in BD \subset \left( {ABD} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {MNI} \right) \cap \left( {ABD} \right)$ $(4).$

Từ $(3)$ và $(4)$ suy ra: $\left( {MNI} \right) \cap \left( {ABD} \right) = ME.$

c) Mặt phẳng $(MNI)$ và mặt phẳng $(ACD).$

Ta có:

$$
\left\{ \begin{array}{l}
N \in \left( {MNI} \right)\\
N \in AC \subset \left( {ACD} \right)
\end{array} \right.
$$
 $\Rightarrow N \in \left( {MNI} \right) \cap \left( {ACD} \right)$ $(5).$

$$
\left\{ \begin{array}{l}
F \in HI \subset \left( {MNI} \right)\\
F \in CD \subset \left( {ACD} \right)
\end{array} \right.
$$
 $\Rightarrow F \in \left( {MNI} \right) \cap \left( {ACD} \right)$ $(6).$

Từ $(5)$ và $(6)$ suy ra: $\left( {MNI} \right) \cap \left( {ACD} \right) = NF.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 4: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang có $AB$ song song với $CD$. Gọi $I$ là giao điểm của $AD$ và $BC$. Lấy $M$ thuộc cạnh $SC$. Tìm giao tuyến của hai mặt phẳng:

a) Mặt phẳng $(SAC)$ và mặt phẳng $(SBD).$

b) Mặt phẳng $(SAD)$ và mặt phẳng $(SBC).$

c) Mặt phẳng $(ADM)$ và mặt phẳng $(SBC).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-4.png" alt="tim-giao-tuyen-cua-hai-mat-phang-4">

a) Tìm giao tuyến của $2$ mặt phẳng $(SAC)$ và $(SBD).$

Ta có: $S \in \left( {SAC} \right) \cap \left( {SBD} \right)$ $\left( 1 \right).$

Trong mặt phẳng $(ABCD)$ gọi $H = AC \cap BD$, ta có:

$$
\left\{ \begin{array}{l}
H \in AC \subset \left( {SAC} \right)\\
H \in BD \subset \left( {SBD} \right)
\end{array} \right.
$$
 $\Rightarrow H \in \left( {SAC} \right) \cap \left( {SBD} \right)$ $\left( 2 \right).$

Từ $(1)$ và $(2)$ suy ra $\left( {SAC} \right) \cap \left( {SBD} \right) = SH.$

b) Tìm giao tuyến của $2$ mặt phẳng $(SAD)$ và $(SBC)$.

Ta có: $S \in \left( {SAD} \right) \cap \left( {SBC} \right)$ $\left( 3 \right).$

Trong mặt phẳng $\left( {ABCD} \right)$ gọi $I = AD \cap BC$, ta có:

$$
\left\{ \begin{array}{l}
I \in AD \subset \left( {SAD} \right)\\
I \in BC \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow I \in \left( {SAD} \right) \cap \left( {SBC} \right)$ $(4).$

Trong $(3)$ và $(4)$ suy ra: $\left( {SAD} \right) \cap \left( {SBC} \right) = SI.$

c) Tìm giao tuyến của $2$ mặt phẳng $\left( {ADM} \right)$ và $\left( {SBC} \right).$

Ta có:

$$
\left\{ \begin{array}{l}
M \in \left( {ADM} \right)\\
M \in SC,SC \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow M \in \left( {ADM} \right) \cap \left( {SBC} \right)$ $\left( 5 \right).$

$$
\left\{ \begin{array}{l}
I \in AD,AD \subset \left( {ADM} \right)\\
I \in BC,BC \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow I \in \left( {ADM} \right) \cap \left( {SBC} \right)$ $(6).$

Từ $(5)$ và $(6)$ suy ra: $\left( {ADM} \right) \cap \left( {SBC} \right) = MI.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 5: Cho hình chóp $S.ABCD$ đáy là hình bình hành tâm $O$. Gọi $M, N, P$ lần lượt là trung điểm các cạnh $BC, CD, SA$. Tìm giao tuyến của hai mặt phẳng:

a) Mặt phẳng $(MNP)$ và mặt phẳng $(SAB).$

b) Mặt phẳng $(MNP)$ và mặt phẳng $(SAD).$

c) Mặt phẳng $(MNP)$ và mặt phẳng $(SBC).$

d) Mặt phẳng $(MNP)$ và mặt phẳng $(SCD).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-5.png" alt="tim-giao-tuyen-cua-hai-mat-phang-5">

Gọi $F = MN \cap AB$, $E = MN \cap AD$ (vì $MN,AB,AD \subset \left( {ABCD} \right)$).

a) Mặt phẳng $(MNP)$ và mặt phẳng $(SAB).$

Ta có:

$$
\left\{ \begin{array}{l}
P \in \left( {MNP} \right)\\
P \in SA,SA \subset \left( {SAB} \right)
\end{array} \right.
$$
 $\Rightarrow P \in \left( {MNP} \right) \cap \left( {SAB} \right)$ $\left( 1 \right).$

$$
\left\{ \begin{array}{l}
F \in MN,MN \subset \left( {MNP} \right)\\
F \in AB,AB \subset \left( {SAB} \right)
\end{array} \right.
$$
 $\Rightarrow F \in \left( {MNP} \right) \cap \left( {SAB} \right)$ $\left( 2 \right).$

Từ $(1)$ và $(2)$ suy ra: $\left( {MNP} \right) \cap \left( {SAB} \right) = PF.$

b) Mặt phẳng $(MNP)$ và mặt phẳng $(SAD).$

Ta có:

$$
\left\{ \begin{array}{l}
P \in \left( {MNP} \right)\\
P \in SA,SA \subset \left( {SAD} \right)
\end{array} \right.
$$
 $\Rightarrow P \in \left( {MNP} \right) \cap \left( {SAD} \right)$ $\left( 3 \right).$

$$
\left\{ \begin{array}{l}
E \in MN,MN \subset \left( {MNP} \right)\\
E \in AD,AD \subset \left( {SAD} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {MNP} \right) \cap \left( {SAD} \right)$ $\left( 4 \right).$

Từ $(3)$ và $(4)$ suy ra $\left( {MNP} \right) \cap \left( {SAD} \right) = PE.$

c) Mặt phẳng $(MNP)$ và mặt phẳng $(SBC).$

Trong mặt phẳng $(SAB)$ gọi $K = PF \cap SB$, ta có:

$$
\left\{ \begin{array}{l}
K \in PF,PF \subset \left( {MNP} \right)\\
K \in SB,SB \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow K \in \left( {MNP} \right) \cap \left( {SBC} \right)$ $\left( 5 \right).$

$$
\left\{ \begin{array}{l}
M \in \left( {MNP} \right)\\
M \in BC,BC \subset \left( {SBC} \right)
\end{array} \right.
$$
 $\Rightarrow M \in \left( {MNP} \right) \cap \left( {SBC} \right)$ $\left( 6 \right).$

Từ $(5)$ và $(6)$ suy ra $\left( {MNP} \right) \cap \left( {SBC} \right) = MK.$

d) Mặt phẳng $(MNP)$ và mặt phẳng $(SCD).$

Gọi $H = PE \cap SD$ $\left( {PE,SD \subset \left( {SAD} \right)} \right)$, ta có:

$$
\left\{ \begin{array}{l}
H \in PE,PE \subset \left( {MNP} \right)\\
H \in SD,SD \subset \left( {SCD} \right)
\end{array} \right.
$$
 $\Rightarrow H \in \left( {MNP} \right) \cap \left( {SCD} \right)$ $\left( 7 \right).$

$$
\left\{ \begin{array}{l}
N \in \left( {MNP} \right)\\
N \in CD,CD \subset \left( {SCD} \right)
\end{array} \right.
$$
 $\Rightarrow N \in \left( {MNP} \right) \cap \left( {SCD} \right)$ $\left( 8 \right).$

Từ $(7)$ và $(8)$ suy ra: $\left( {MNP} \right) \cap \left( {SCD} \right) = NH.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 6: Cho tứ diện $S.ABC$. Lấy $M \in SB$, $N \in AC$, $I \in SC$ sao cho $MI$ không song song với $BC, NI$ không song song với $SA.$ Tìm giao tuyến của mặt phẳng $(MNI)$ với các mặt $(ABC)$ và $(SAB).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-6.png" alt="tim-giao-tuyen-cua-hai-mat-phang-6">

a) Tìm giao tuyến của $2$ mặt phẳng $(MNI)$ và $(ABC).$

Vì 
$$
\left\{ \begin{array}{l}
N \in \left( {MNI} \right)\\
N \in AC,AC \subset \left( {ABC} \right)
\end{array} \right.
$$
 $\Rightarrow N \in \left( {MNI} \right) \cap \left( {ABC} \right)$ $(1).$

Trong mặt phẳng $(SBC)$ gọi $K = MI \cap BC.$

Vì: 
$$
\left\{ \begin{array}{l}
K \in MI \subset \left( {MNI} \right)\\
K \in BC,BC \subset \left( {ABC} \right)
\end{array} \right.
$$
 $\Rightarrow K \in \left( {MNI} \right) \cap \left( {ABC} \right)$ $\left( 2 \right).$

Từ $(1)$ và $(2)$ suy ra: $\left( {MNI} \right) \cap \left( {ABC} \right) = NK.$

b) Tìm giao tuyến của $2$ mặt phẳng $(MNI)$ và $(SAB).$

Gọi $J = NI \cap SA$ $\left( {NI,SA \subset \left( {SAC} \right)} \right).$

Ta có:

$$
\left\{ \begin{array}{l}
M \in \left( {MNI} \right)\\
M \in SB,SB \subset \left( {SAB} \right)
\end{array} \right.
$$
 $\Rightarrow M \in \left( {MNI} \right) \cap \left( {SAB} \right)$ $\left( 3 \right).$

$$
\left\{ \begin{array}{l}
J \in NI \subset \left( {MNI} \right)\\
J \in SA,SA \subset \left( {SAB} \right)
\end{array} \right.
$$
 $\Rightarrow J \in \left( {MNI} \right) \cap \left( {SAB} \right)$ $\left( 4 \right).$

Từ $(3)$ và $(4)$ suy ra: $\left( {MNI} \right) \cap \left( {SAB} \right) = MJ.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 7: Cho tứ diện $ABCD$, $M$ là một điểm nằm bên trong tam giác $ABD$, $N$ là một điểm bên trong tam giác $ACD$. Tìm giao tuyến của hai mặt phẳng:

a) Mặt phẳng $(AMN)$ và mặt phẳng $(BCD).$

b) Mặt phẳng $(DMN)$ và mặt phẳng $(ABC).$

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-7.png" alt="tim-giao-tuyen-cua-hai-mat-phang-7">

a) Tìm giao tuyến của hai mặt phẳng $(AMN)$ và $(BCD).$

Trong mặt phẳng $(ABD)$, gọi $E = AM \cap BD$, ta có:

$$
\left\{ \begin{array}{l}
E \in AM,AM \subset \left( {AMN} \right)\\
E \in BD,BD \subset \left( {BCD} \right)
\end{array} \right.
$$
 $\Rightarrow E \in \left( {AMN} \right) \cap \left( {BCD} \right)$ $(1).$

Trong $(ACD)$ gọi $F = AN \cap CD$, ta có:

$$
\left\{ \begin{array}{l}
F \in AN,AN \subset \left( {AMN} \right)\\
F \in CD,CD \subset \left( {BCD} \right)
\end{array} \right.
$$
 $\Rightarrow F \in \left( {AMN} \right) \cap \left( {BCD} \right)$ $(2).$

Từ $(1)$ và $(2)$ suy ra: $\left( {AMN} \right) \cap \left( {BCD} \right) = EF.$

b) Tìm giao tuyến của hai mặt phẳng $(DMN)$ và $(ABC).$

Trong mặt phẳng $(ABD)$, gọi $P = DM \cap AB$, ta có:

$$
\left\{ \begin{array}{l}
P \in DM,DM \subset \left( {DMN} \right)\\
P \in AB,AB \subset \left( {ABC} \right)
\end{array} \right.
$$
 $\Rightarrow P \in \left( {DMN} \right) \cap \left( {ABC} \right)$ $(3).$

Trong $(ACD)$, gọi $Q = DN \cap AC$, ta có:

$$
\left\{ \begin{array}{l}
Q \in DN,DN \subset \left( {DMN} \right)\\
Q \in AC,AC \subset \left( {ABC} \right)
\end{array} \right.
$$
 $\Rightarrow Q \in \left( {DMN} \right) \cap \left( {ABC} \right)$ $\left( 4 \right).$

Từ $(3)$ và $(4)$ suy ra: $\left( {DMN} \right) \cap \left( {ABC} \right) = PQ.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/07/tim-giao-tuyen-cua-hai-mat-phang.html -->
## Ví dụ 8: Cho tứ diện $ABCD$. Lấy $I \in AB$, $J$ là điểm trong tam giác $BCD$, $K$ là điểm trong tam giác $ACD$. Tìm giao tuyến của mặt phẳng $(IJK)$ với các mặt của tứ diện.

<img link="data_for_rag/toan11/images/tim-giao-tuyen-cua-hai-mat-phang-8.png" alt="tim-giao-tuyen-cua-hai-mat-phang-8">

Gọi:

$M = DK \cap AC$ $\left( {DK,AC \subset \left( {ACD} \right)} \right).$

$N = DJ \cap BC$ $\left( {DJ,BC \subset \left( {BCD} \right)} \right).$

$H = MN \cap KJ$ $\left( {MN,KJ \subset \left( {DMN} \right)} \right).$

Vì $H \in MN$, $MN \subset \left( {ABC} \right)$ $\Rightarrow H \in \left( {ABC} \right).$

Gọi:

$P = HI \cap BC$ $\left( {HI,BC \subset \left( {ABC} \right)} \right).$

$Q = PJ \cap CD$ $\left( {PJ,CD \subset \left( {BCD} \right)} \right).$

$T = QK \cap AD$ $\left( {QK,AD \subset \left( {ACD} \right)} \right).$

Theo cách dựng điểm ở trên, ta có:

$\left( {IJK} \right) \cap \left( {ABC} \right) = IP.$

$\left( {IJK} \right) \cap \left( {BCD} \right) = PQ.$

$\left( {IJK} \right) \cap \left( {ACD} \right) = QT.$

$\left( {IJK} \right) \cap \left( {ABD} \right) = TI.$