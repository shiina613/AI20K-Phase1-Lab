# Xác định thiết diện của hình đa diện khi cắt bởi mặt phẳng

<!-- chunk:0 level:0 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
Bài viết phân dạng và hướng dẫn phương pháp xác định thiết diện của hình đa diện khi cắt bởi mặt phẳng với các ví dụ minh họa có lời giải chi tiết.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 1: Thiết diện của hình đa diện với mặt phẳng $\left( \alpha \right)$ biết $\left( \alpha \right)$ đi qua ba điểm phân biệt không thẳng hàng.

Phương pháp:

+ Xác định giao tuyến của mặt phẳng $\left( \alpha \right)$ với từng mặt của hình đa diện.

+ Nối các đoạn giao tuyến lại ta được thiết diện cần tìm.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 1: Cho tứ diện $ABCD$. Gọi $I$ và $J$ lần lượt là trung điểm của $BC$ và $BD$; $E$ là một điểm thuộc cạnh $AD$ khác với $A$ và $D$. Xác định thiết diện của hình tứ diện khi cắt bởi mặt phẳng $\left( IJE \right)$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-1.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-1">

Ta có:

$\left( {IJE} \right) \cap \left( {BCD} \right) = IJ$ $\left( 1 \right).$

$\left( {IJE} \right) \cap \left( {ABD} \right) = EJ$ $\left( 2 \right).$

Tìm $\left( {IJE} \right) \cap \left( {ACD} \right)$:

$E \in \left( {IJE} \right) \cap \left( {ACD} \right).$

$IJ \subset \left( {IJE} \right)$, $CD \subset \left( {ACD} \right).$

Vì $IJ$ là đường trung bình của tam giác $BCD$ nên $IJ//CD$ $\Rightarrow \left( {IJE} \right) \cap \left( {ACD} \right) = Ex$ với $Ex$ là đường thẳng đi qua $E$ và song song với $IJ$ và $CD.$

Gọi $F = Ex \cap AC.$

Khi đó: $\left( {IJE} \right) \cap \left( {ACD} \right) = EF$ $\left( 3 \right).$

Ta có: $\left( {IJE} \right) \cap \left( {ABC} \right) = IF$ $\left( 4 \right).$

Từ $\left( 1 \right),\left( 2 \right),\left( 3 \right),\left( 4 \right)$ suy ra thiết diện của hình tứ diện $ABCD$ khi cắt bởi mặt phẳng $\left( IJE \right)$ là hình thang $IJEF.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 2: Cho hình lăng trụ $ABC.A’B’C’$. Gọi $M,N$ lần lượt là trung điểm của $A’B’$, $CC’$. Dựng thiết diện của hình lăng trụ với mặt phẳng $\left( {AMN} \right).$

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-2.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-2">

Ta có:

$\left( {AMN} \right) \cap \left( {ABB’A’} \right) = AM$ $\left( 1 \right).$

$\left( {AMN} \right) \cap \left( {ACC’A’} \right) = AN$ $\left( 2 \right).$

Tìm $\left( {AMN} \right) \cap \left( {A’B’C’} \right):$

$M \in \left( {AMN} \right) \cap \left( {A’B’C’} \right).$

Gọi $P = AN \cap A’C’$ $\Rightarrow P \in \left( {AMN} \right) \cap \left( {A’B’C’} \right).$

Suy ra $\left( {AMN} \right) \cap \left( {A’B’C’} \right)$ $= MP = MQ$ (với $Q = MP \cap B’C’$) $\left( 3 \right).$

Khi đó: $\left( {AMN} \right) \cap \left( {BCC’B’} \right) = NQ$ $\left( 4 \right).$

Từ $\left( 1 \right),\left( 2 \right),\left( 3 \right),\left( 4 \right)$ suy ra thiết diện là tứ giác $AMQN.$

<!-- chunk:4 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 2: Thiết diện của một hình đa diện với mặt phẳng $\left( \alpha \right)$, biết $\left( \alpha \right)$ chứa $a$ và song song với đường thẳng $b.$

Phương pháp:

+ Chọn mặt phẳng $\left( \beta \right) \supset b.$

+ Tìm một điểm chung $M$ của hai mặt phẳng $\left( \alpha \right)$ và $\left( \beta \right).$

+ Tìm ${M_x} = \left( \alpha \right) \cap \left( \beta \right)$, khi đó ${M_x}\parallel a\parallel b.$

+ Xác định giao tuyến của mặt phẳng $\left( \alpha \right)$ với các mặt của hình đa diện.

+ Nối các đoạn giao tuyến lại ta được thiết diện cần tìm.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 3: Cho hình chóp $S.ABCD$ đáy là hình thang với các cạnh đáy là $AB$ và $CD$. Gọi $I,J$ lần lượt là trung điểm của $AD$ và $BC$. $G$ là trọng tâm của $\Delta SAB$. Xác định thiết diện của hình chóp với mặt phẳng $\left( IJG \right)$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-3.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-3">

Do $I,J$ lần lượt là trung điểm của $AD$ và $BC$ nên $IJ||AD||BC.$

Vậy $\left( {IJG} \right)$ là mặt phẳng có chứa một đường thẳng song song với một đường thẳng cho trước $\left( {AB} \right).$

Chọn mặt phẳng $\left( {SAB} \right) \supset AB.$

$G$ là điểm chung của hai mặt phẳng $\left( {SAB} \right)$ và $\left( {IJG} \right).$

Ta có: 
$$
\left\{ \begin{array}{l}
AB \subset \left( {SAB} \right)\\
IJ \subset \left( {IJG} \right)\\
G \in \left( {SAB} \right) \cap \left( {IJG} \right)\\
AB\parallel IJ
\end{array} \right.
$$
 $\Rightarrow \left( {SAB} \right) \cap \left( {IJG} \right)$ $= {G_x}\left( {{G_x}\parallel AB\parallel IJ} \right).$

Giả sử ${G_x}$ cắt $SA$ tại $M$ và cắt $SB$ tại $N$, khi đó: $\left( {SAB} \right) \cap \left( {IJG} \right) = MN$, $\left( {SAD} \right) \cap \left( {IJG} \right) = MI$, $\left( {SBC} \right) \cap \left( {IJG} \right) = NJ$, $\left( {ABCD} \right) \cap \left( {IJG} \right) = IJ.$

Vậy thiết diện cần tìm là hình thang $MNIJ.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 4: Cho tứ diện $ABCD$. Gọi $I,J$ lần lượt là trung điểm của $AC$ và $BC$. Gọi $K$ là một điểm trên cạnh $BD$. Xác định thiết diện của tứ diện với mặt phẳng $\left( IJK \right)$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-4.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-4">

Do $I,J$ lần lượt là trung điểm của $AC$ và $BC.$ Nên suy ra $IJ\parallel AB.$

Vậy $\left( {IJK} \right)$ là mặt phẳng chứa một đường thẳng song song với một đường thẳng cho trước $\left( {AB} \right).$

Chọn mặt phẳng $\left( {ABC} \right) \supset AB.$

$$
\left\{ \begin{array}{l}
K \in BD\\
BD \subset \left( {ABD} \right)
\end{array} \right.
$$
 $\Rightarrow K \in \left( {ABD} \right)$, suy ra $K$ là điểm chung của hai mặt phẳng $\left( {IJK} \right)$ và $\left( {ABD} \right).$

Ta có: 
$$
\left\{ \begin{array}{l}
AB \subset \left( {ABD} \right)\\
IJ \subset \left( {IJK} \right)\\
AB\parallel IJ\\
K \in \left( {ABD} \right) \cap \left( {IJK} \right)
\end{array} \right.
$$
 $\Rightarrow \left( {ABD} \right) \cap \left( {IJK} \right) = {K_x}$ $\left( {{K_x}\parallel AB\parallel IJ} \right).$

Giả sử ${K_x}$ cắt $AD$ tại $H$, khi đó: $\left( {ABD} \right) \cap \left( {IJK} \right) = KH$, $\left( {CAD} \right) \cap \left( {IJK} \right) = IH$, $\left( {CDB} \right) \cap \left( {IJK} \right) = JK$, $\left( {CAB} \right) \cap \left( {IJK} \right) = IJ.$

Vậy thiết diện cần tìm là hình thang $IJKH.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 3: Thiết diện của hình đa diện với mặt phẳng $\left( \alpha \right)$, biết mặt phẳng $\left( \alpha \right)$ qua $M$ và song song với hai đường thẳng $a$ và $b.$

Phương pháp:

+ Qua $\left( \alpha \right)$ kẻ hai đường thẳng $\left( \alpha \right)$lần lượt song song với hai đường thẳng $\left( \alpha \right)$

+ Tìm điểm chung của $\left( \alpha \right)$với một mặt nào đó của hình đa diện

+ Mặt phẳng nào chứa điểm chung và chứa đường thẳng $\left( \alpha \right)$hoặc $\left( \alpha \right)$thì tiếp tục kẻ đường thẳng qua điểm chung và song song với đường thẳng $\left( \alpha \right)$hoặc $\left( \alpha \right)$cho đến khi thiết diện được hình thành.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 5: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $O$ là giao điểm của hai đường chéo hình bình hành. Một mặt phẳng $\left( \alpha  \right)$ qua $O$, song song với $SA,CD$. Tìm thiết diện tạo bởi $\left( \alpha  \right)$ và hình chóp.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-5.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-5">

Tìm $\left( \alpha \right) \cap \left( {ABCD} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
O \in \left( \alpha \right) \cap \left( {ABCD} \right)\\
CD\parallel \left( \alpha \right)\\
\left( {ABCD} \right) \supset CD
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {ABCD} \right) = MN$ $\left( 1 \right)$, với $MN$ là đoạn thẳng qua $O$ và song song với $CD$, $\left( {M \in BC,N \in AD} \right).$

Tìm $\left( \alpha \right) \cap \left( {SAD} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
N \in \left( \alpha \right) \cap \left( {SAD} \right)\\
SA\parallel \left( \alpha \right)\\
\left( {SAD} \right) \supset SA
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {SAD} \right) = NP$ $\left( 2 \right)$ với $NP\parallel SA$ $\left( {P \in SD} \right).$

Tìm $\left( \alpha \right) \cap \left( {SCD} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
P \in \left( \alpha \right) \cap \left( {SCD} \right)\\
CD\parallel \left( \alpha \right)\\
\left( {SCD} \right) \supset CD
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {SCD} \right) = MQ$ $\left( 3 \right)$ với $PQ\parallel CD$ $\left( {Q \in SC} \right).$

Ta có: $\left( \alpha \right) \cap \left( {SBC} \right) = MQ$ $\left( 4 \right).$

Từ $\left( 1 \right),\left( 2 \right),\left( 3 \right),\left( 4 \right)$ suy ra thiết diện cần tìm là tứ giác $MNPQ.$

Ta lại có: $MN\parallel CD\parallel QP.$ Vậy thiết diện cần tìm là hình thang $MNPQ.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 6: Cho hình chóp $S.ABCD$, đáy $ABCD$ là hình thang cân có $AD$ không song song với $BC$. Gọi $M$ là trung điểm của $AD$ và $\left( \alpha  \right)$ là mặt phẳng qua $M$, song song với $SA,BD$. Xác định thiết diện của hình chóp cắt bởi mặt phẳng $\left( \alpha \right).$

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-6.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-6">

Tìm $\left( \alpha \right) \cap \left( {ABCD} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
M \in \left( \alpha \right) \cap \left( {ABCD} \right)\\
BD\parallel \left( \alpha \right)\\
\left( {ABCD} \right) \supset BD
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {ABCD} \right) = MN$ $\left( 1 \right)$ với $MN\parallel BD$ $\left( {N \in AB} \right)$ ($N$ là trung điểm của $AB$).

Tìm $\left( \alpha \right) \cap \left( {SAD} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
M \in \left( \alpha \right) \cap \left( {SAD} \right)\\
SA\parallel \left( \alpha \right)\\
\left( {SAD} \right) \supset SA
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {SAD} \right) = MR$ $\left( 2 \right)$ với $MR\parallel SA$ $\left( {R \in SD} \right)$ ($R$ là trung điểm của $SD$).

Tìm $\left( \alpha \right) \cap \left( {SAB} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
N \in \left( \alpha \right) \cap \left( {SAB} \right)\\
SA\parallel \left( \alpha \right)\\
\left( {SAB} \right) \supset SA
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {SCD} \right) = NP$ $\left( 3 \right)$ với $NP\parallel SA$ $\left( {P \in SB} \right)$ ($P$ là trung điểm của $SB$).

Tìm $\left( \alpha \right) \cap SC$:

Gọi $I$ là giao điểm của $MN$ với $AC.$

Chọn mặt phẳng phụ $\left( {SAC} \right) \supset SC.$

Tìm $\left( \alpha \right) \cap \left( {SAC} \right)$:

Ta có: 
$$
\left\{ \begin{array}{l}
I \in \left( \alpha \right) \cap \left( {SAC} \right)\\
SA\parallel \left( \alpha \right)\\
\left( {SAC} \right) \supset SA
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right) \cap \left( {SAC} \right) = IQ$ với $IQ\parallel SA$ $\left( {Q \in SC} \right).$

Suy ra $\left( \alpha \right) \cap SC = Q.$

Do đó ta có:

$\left( \alpha \right) \cap \left( {SCD} \right) = RQ$ $\left( 4 \right).$

$\left( \alpha \right) \cap \left( {SCB} \right) = PQ$ $\left( 5 \right).$

Từ $\left( 1 \right),\left( 2 \right),\left( 3 \right),\left( 4 \right),\left( 5 \right)$ suy ra thiết diện cần tìm là ngũ giác $MNPQR.$

[ads]

<!-- chunk:10 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 4: Thiết diện của hình đa diện với mặt phẳng $(\alpha )$ biết $(\alpha )$ đi qua một điểm cho trước và song song với mặt phẳng $(\beta ).$

Phương pháp:

+ Chọn mặt phẳng $(\gamma )$ chứa điểm thuộc mặt phẳng $(\alpha )$ sao cho giao tuyến của $(\beta )$ và $(\gamma )$ là dễ tìm.

+ Xác định giao tuyến $d=(\beta )\cap \left( \gamma \right).$

+ Kết luận giao tuyến của $(\alpha )$ và $(\gamma )$ là đường thẳng qua điểm thuộc $(\alpha )$ và song song $d.$

+ Tiếp tục làm quá trình này cho đến khi thiết diện được hình thành.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 7: Cho tứ diện $ABCD$. Gọi $E$ là một điểm nằm trên cạnh $AB.$ Xác định thiết diện của tứ diện cắt bởi mặt phẳng $(\alpha )$ với $(\alpha )$ là mặt phẳng qua $E$ và $(\alpha )\parallel (BCD).$

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-7.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-7">

Tìm $(\alpha ) \cap (ABC)$:

Ta có: 
$$
\left\{ \begin{array}{l}
(ABC) \cap (BCD) = BC\\
(\alpha )\parallel (BCD)\\
E \in (\alpha ) \cap (ABC)
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (ABC) = EF$ $(1)$, với $EF$ là đoạn thẳng qua $E$ và song song với $BC.$

Tìm $(\alpha ) \cap (ABD)$:

Ta có: 
$$
\left\{ \begin{array}{l}
(ABD) \cap (BCD) = BD\\
(\alpha )\parallel (BCD)\\
E \in (\alpha ) \cap (ABD)
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (ABD) = EG$ $(2)$, với $EG$ là đoạn thẳng qua $E$ và song song $BD.$

Nối đoạn $FG$ ta có: $(\alpha ) \cap (ACD) = FG$ $(3).$

Từ $(1),(2),(3)$ suy ra thiết diện cần tìm là tam giác $EFG.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 8: Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang cạnh đáy $AD$, $AD<BC$. $(\alpha )$ là mặt phẳng qua $M$ trên cạnh $AB$ và song song với mặt phẳng $(SAD).$ Tìm thiết diện của hình chóp với $(\alpha ).$

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-8.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-8">

Tìm $(\alpha ) \cap (ABCD)$:

Ta có: 
$$
\left\{ \begin{array}{l}
(ABCD) \cap (SAD) = AD\\
(\alpha )\parallel (SAD)\\
M \in (\alpha ) \cap (ABCD)
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (ABCD) = MN$ $(1)$, với $MN$ là đoạn thẳng qua $M$ song song $AD.$

Tìm $(\alpha ) \cap (SAB)$:

Ta có: 
$$
\left\{ \begin{array}{l}
(SAB) \cap (SAD) = SA\\
(\alpha )\parallel (SAD)\\
M \in (\alpha ) \cap (SAB)
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (SAB) = MK$ $(2)$, với $MK$ là đoạn thẳng qua $M$ song song $SA.$

Tìm $(\alpha ) \cap (SCD)$:

Ta có: 
$$
\left\{ \begin{array}{l}
(SCD) \cap (SAD) = SD\\
(\alpha )\parallel (SAD)\\
N \in (\alpha ) \cap (SCD)
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (SCD) = NP$ $(3)$, với $NP$ là đoạn thẳng qua $N$ song song $SD.$

Nối đoạn $KP$ ta có: $(\alpha ) \cap (SBC) = KP$ $(4).$

Từ $(1),(2),(3),(4)$ suy ra thiết diện cần tìm là tứ giác $MNPK.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 5: Thiết diện của hình đa diện với mặt phẳng $(\alpha )$ biết $(\alpha )$ qua một điểm cho trước và vuông góc với một đường thẳng cho trước.

Phương pháp: Để tìm thiết diện của khối đa diện $S$ với mặt phẳng $\left( \alpha \right)$, biết $\left( \alpha \right)$ đi qua điểm $M$ cho trước và vuông góc với đường thẳng $d$ cho trước, làm như sau:

+ Tìm hai đường thẳng cắt nhau hay chéo nhau $a,b$ cùng vuông góc với $d$.

+ Xác định mặt phẳng $\left( \alpha \right)$ theo một trong bốn trường hợp:

$(I)$: 
$$
\left\{ {\begin{array}{c}
{a \subset \left( \alpha \right)}\\
{b \subset \left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

$(II)$: 
$$
\left\{ {\begin{array}{c}
{a//\left( \alpha \right)}\\
{b//\left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

$(III)$: 
$$
\left\{ {\begin{array}{c}
{a \subset \left( \alpha \right)}\\
{b//\left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

$(IV)$: 
$$
\left\{ {\begin{array}{c}
{a//\left( \alpha \right)}\\
{b \subset \left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 9: Cho hình tứ diện $SABC$ có $ABC$ là tam giác đều. $SA$ vuông góc với mặt phẳng $\left( ABC \right)$. Gọi $E$ là trung điểm của $AC$, $M$ là một điểm thuộc $AE$. Xác định thiết diện tạo bởi tứ diện $SABC$ và mặt phẳng $\left( \alpha \right)$, biết $\left( \alpha \right)$ là mặt phẳng qua điểm $M$ và vuông góc với $AC$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-9.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-9">

Tìm hai đường thẳng không song song cùng vuông góc với $AC.$

Ta có: 
$$
\left\{ {\begin{array}{c}
{SA \bot \left( {ABC} \right)}\\
{AC \subset \left( {ABC} \right)}
\end{array}} \right.
$$
 $\Rightarrow SA \bot AC.$

Xét tam giác đều $ABC$, ta có $E$ là trung điểm của $AC$ nên $BE$ sẽ vuông góc với $AC$.

Vậy ta có hai đường thẳng $SA$ và $BE$ là hai đường thẳng không song song cùng vuông góc với $AC$.

Xác định mặt phẳng $\left( \alpha \right)$:

Do $\left( \alpha  \right)$ qua $M$ và $M\notin SA$, $M\notin BE$ nên $\left( \alpha  \right)$ sẽ được xác định theo cách: 
$$
\left\{ {\begin{array}{c}
{SA||\left( \alpha \right)}\\
{BE||\left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

Khi đó:

Trong $\left( ABC \right)$ dựng $Mx||BE$ cắt $AB$ tại $N$ (ta được $MN\bot AC$).

Trong $\left( SAC \right)$ dựng $My||SA$ cắt $SC$ tại $P$ (ta được $MP\bot AC$).

Trong $\left( SAB \right)$ dựng $Nz||SA$ cắt $SB$ tại $Q$ (ta được $NQ\bot AC$).

Xác định thiết của $\left( \alpha \right)$ với tứ diện $SABC$:

Ta có:

$\left( SAB \right)\cap \left( \alpha \right)=NQ.$

$\left( SAC \right)\cap \left( \alpha \right)=NP.$

$\left( SBC \right)\cap \left( \alpha \right)=PQ.$

$\left( ABC \right)\cap \left( \alpha \right)=MN.$

Vậy thiết diện cần tìm là hình thang vuông $MNPQ$.

<!-- chunk:15 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 10: Cho hình tứ diện $SABC$ có $ABC$ là tam giác đều. $SA$ vuông góc với mặt phẳng $\left( ABC \right)$. Lấy một điểm $M$ bất kì trên cạnh $SC$, gọi $\left( \alpha \right)$ là mặt phẳng qua $M$ và vuông góc với $AB$. Hãy xác định thiết diện tạo bởi tứ diện $SABC$ và mặt phẳng $\left( \alpha \right)$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-10.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-10">

Tìm hai đường thẳng không song song cùng vuông góc với $AB.$

Ta có: 
$$
\left\{ {\begin{array}{c}
{SA \bot \left( {ABC} \right)}\\
{AB \subset \left( {ABC} \right)}
\end{array}} \right.
$$
 $\Rightarrow SA \bot AB.$

Xét tam giác đều $ABC$, ta có $I$ là trung điểm của $AB$nên $CI$ sẽ vuông góc với $AB$.

Vậy ta có hai đường thẳng $SA$ và $CI$ là hai đường thẳng không song song cùng vuông góc với $AB$.

Xác định mặt phẳng $\left( \alpha \right)$:

Do $\left( \alpha  \right)$ qua $M$và $M\notin SA$, $M\notin CI$ nên $\left( \alpha  \right)$ sẽ được xác định theo cách: 
$$
\left\{ {\begin{array}{c}
{SA//\left( \alpha \right)}\\
{CI//\left( \alpha \right)}\\
{M \in \left( \alpha \right)}
\end{array}} \right.
$$

Khi đó:

Trong $\left( SAC \right)$ dựng $Mx//SA$ cắt $AC$ tại $N$ (ta được $MN\bot AB$).

Trong $\left( ABC \right)$ dựng $Ny//CI$ cắt $AB$ tại $P$ (ta được $NP\bot AB$).

Trong $\left( SAB \right)$ dựng $Pz//SA$ cắt $SB$ tại $Q$ (ta được $PQ\bot AB$).

Xác định thiết của $\left( \alpha \right)$ với tứ diện $SABC$:

Ta có:

$\left( SAB \right)\cap \left( \alpha \right)=PQ.$

$\left( SAC \right)\cap \left( \alpha \right)=MN.$

$\left( SBC \right)\cap \left( \alpha \right)=QM.$

$\left( ABC \right)\cap \left( \alpha \right)=NP.$

Vậy thiết diện cần tìm là hình thang vuông $MNPQ$.

<!-- chunk:16 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 6: Thiết diện của hình đa diện với mặt phẳng $\left( \alpha  \right)$ biết $\left( \alpha  \right)$ chứa đường thẳng $d$ và vuông góc với mặt phẳng $\left( \beta  \right)$.

Phương pháp:

+ Từ một điểm $M\in d$ ta dựng đường thẳng $a$ qua $M$ và vuông góc với $(\beta )$. Khi đó: $\left( \alpha \right)=\left( d,a \right).$

+ Tìm giao tuyến của $\left( \alpha \right)$ với các mặt của hình đa diện.

<!-- chunk:17 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 11: Cho tứ diện $SABC$ có đáy $ABC$ là tam giác vuông tại $B$, $SA\bot \left( ABC \right)$. Gọi $E$ là trung điểm cạnh $SC$, $M$ là một điểm trên cạnh $AB$. Gọi $\left( \alpha \right)$ là mặt phẳng chứa $EM$ và vuông góc với $\left( SAB \right)$. Xác định thiết diện của $\left( \alpha \right)$ và tứ diện.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-11.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-11">

Ta có: 
$$
\left\{ \begin{array}{l}
BC \bot AB\\
BC \bot {\rm{S}}A
\end{array} \right.
$$
 $\Rightarrow BC \bot \left( {SAB} \right).$

Ta lại có: 
$$
\left\{ \begin{array}{l}
\left( \alpha \right) \bot \left( {SAB} \right)\\
BC \bot \left( {{\rm{S}}AB} \right)
\end{array} \right.
$$
 $\Rightarrow \left( \alpha \right)\parallel BC.$

Kẻ $MN\parallel BC$, ${\rm{EF}}\parallel BC.$

Nối $MF, NE$ ta được thiết diện cần tìm là hình thang $MNEF.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 12: Cho hình chóp $S.ABCD$, $ABCD$ là hình chữ nhật, $SA\bot (ABCD)$. Gọi $I,J$ lần lượt là trung điểm của $AB,CD$. Gọi $\left( P \right)$ là mặt phẳng qua $I$ và vuông góc với mặt $\left( SBC \right)$. Tìm thiết diện của hình chóp với mặt phẳng $\left( P \right)$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-12.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-12">

Ta có: 
$$
\left. \begin{array}{l}
IJ \bot AB\\
IJ \bot SA
\end{array} \right\}
$$
 $\Rightarrow IJ \bot \left( {SAB} \right)$ $\Rightarrow IJ \bot SB.$

Từ $I$ kẻ đường thẳng vuông góc với $SB$ tại $K.$

Do đó $\left( P \right) \equiv \left( {KIJ} \right).$

Ta có:

$\left( P \right) \cap \left( {SAB} \right) = KI.$

$\left( P \right) \cap \left( {ABCD} \right) = IJ.$

$\left( P \right) \supset IJ\parallel BC$ $\Rightarrow \left( P \right) \cap \left( {SBC} \right) = KN\parallel BC.$

$\left( P \right) \cap \left( {SCD} \right) = NI.$

Vậy thiết diện là hình thang $KNIJ.$

<!-- chunk:19 level:2 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Dạng 7: Thiết diện của hình đa diện với mặt phẳng $(\alpha )$ biết $(\alpha )$ chứa đường thẳng $d$ và tạo với mặt phẳng $(\beta )$ một góc $\varphi .$

Phương pháp: Sử dụng các công thức lượng giác, tính chất giao điểm và trung tuyến … từ đó xác định các đoạn giao tuyến và tìm được thiết diện.

<!-- chunk:20 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 13: Cho hình chóp tứ giác đều $S.ABCD$ có đáy là hình vuông cạnh $a$. Mặt bên hợp với đáy một góc ${{60}^{0}}$. Cho $\left( P \right)$ là mặt phẳng qua $CD$ và vuông góc với $\left( SAB \right)$, $\left( P \right)$ cắt $SA,SB$ lần lượt tại $M,N$. $\left( P \right)$ cắt hình chóp theo thiết diện là hình gì? Tính thiết diện theo $a$.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-13.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-13">

Gọi $K,I$ lần lượt là trung điểm của $AB,CD.$

Khi đó $KI$ đi qua tâm $O$ của hình vuông $ABCD.$

Ta có: 
$$
\left\{ \begin{array}{l}
SK \bot AB\\
OK \bot AB
\end{array} \right.
$$
 $\Rightarrow \widehat {SKO} = {60^0}$ (Vì $\widehat {SKO}$ là góc giữa mặt bên và mặt đáy hình chóp).

Suy ra $\Delta SKI$ là tam giác đều.

Hạ đường cao $IE$ của $\Delta SIK.$

Ta có: 
$$
\left\{ \begin{array}{l}
IE \bot SK\\
IE \bot AB
\end{array} \right.
$$
 $\Rightarrow IE \bot \left( {SAB} \right).$

Do đó mặt phẳng $\left( P \right)$ qua $CD$ và vuông góc $\left( SAB \right)$ là mặt phẳng $\left( CDE \right)$.

Vậy thiết diện cần tìm là tứ giác $CDMN.$

Ta có: 
$$
\left\{ \begin{array}{l}
MN\parallel AB\\
CD\parallel AB
\end{array} \right.
$$
 $\Rightarrow MN\parallel CD.$

Mặt khác $MN$ là đường trung bình của $\Delta SAB$, do đó $DM = CN.$

Vậy thiết diện $CDMN$ là hình thang cân.

Ta có: $MN = \frac{a}{2}$, $IE = \frac{{a\sqrt 3 }}{2}.$

Vậy diện tích thiết diện là ${S_{CDMN}} = \frac{{\left( {CD + MN} \right).IE}}{2}$ $= \frac{{3{a^2}\sqrt 3 }}{8}.$

<!-- chunk:21 level:3 source:https://toanmath.com/2018/07/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang.html -->
## Ví dụ 14: Cho hình chóp tứ giác đều $S.ABCD$ có đáy là hình vuông $ABCD$ cạnh $a$. Mặt bên tạo với đáy một góc ${{60}^{0}}.$ Mặt phẳng $(\alpha )$ qua $AB$ cắt $SC,SD$ lần lượt tại $M,N$. Cho biết góc tạo bởi mặt phẳng $(\alpha )$ với mặt đáy là ${{30}^{0}}.$ Hãy xác định thiết diện tạo bởi mặt phẳng $(\alpha )$ và hình chóp.

<img link="data_for_rag/toan11/images/xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-14.png" alt="xac-dinh-thiet-dien-cua-hinh-da-dien-khi-cat-boi-mat-phang-14">

Ta có: 
$$
\left\{ \begin{array}{l}
M \in (\alpha ) \cap (SCD)\\
CD\parallel AB\\
(SCD) \supset CD,(\alpha ) \supset AB
\end{array} \right.
$$
 $\Rightarrow (\alpha ) \cap (SCD) = MN$ $(MN\parallel AB).$

Ta có: $(SAB) \cap (\alpha ) = AB$, $(SAD) \cap (\alpha ) = AN$, $(SCD) \cap (\alpha ) = MN$, $(SBC) \cap (\alpha ) = MB.$

Vậy thiết diện cần tìm là hình thang $ABMN.$

Mặc khác $\Delta AND=\Delta BMC$ $\Rightarrow AN=BM.$

Vậy $ABMN$ là hình thang cân.