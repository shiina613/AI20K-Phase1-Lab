# Công thức tính khoảng cách từ một điểm đến mặt phẳng và bài tập áp dụng

<!-- chunk:0 level:0 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
Bài viết trình bày công thức tính khoảng cách từ một điểm đến mặt phẳng, mở rộng đối với khoảng cách giữa hai mặt phẳng song song và hướng dẫn giải một số bài tập trắc nghiệm liên quan.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## A. CÁC KẾT QUẢ CẦN LƯU Ý

Cho $a$, $b$, $c$ là các số thực và ${a^2} + {b^2} + {c^2} > 0.$

<!-- chunk:2 level:2 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Dạng 1: Khoảng cách từ một điểm đến một mặt phẳng.

Phương pháp: Điểm ${M_0}\left( {{x_0};{y_0};{z_0}} \right)$ và mặt phẳng $(\alpha ):ax + by + cz + d = 0.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-1.png" alt="">

$d\left( {{M_0};(\alpha )} \right) = \frac{{\left| {a{x_0} + b{y_0} + c{z_0} + d} \right|}}{{\sqrt {{a^2} + {b^2} + {c^2}} }}.$

Hệ quả:

* ${M_0} \in (\alpha )$ $\Leftrightarrow d\left( {{M_0};(\alpha )} \right) = 0.$

* $d\left( {{M_0};(\alpha )} \right) = {M_0}H$ với 
$$
\left\{ {\begin{array}{l}
{{M_0}H \bot (\alpha )}\\
{H \in (\alpha )}
\end{array}} \right..
$$

* Với mọi $M \in (\alpha ):$ $d\left( {{M_0};(\alpha )} \right) \le {M_0}M.$

<!-- chunk:3 level:2 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Dạng 2: Khoảng cách giữa hai mặt phẳng song song.

Phương pháp: Cho hai mặt phẳng song song $(\alpha )$ và $(\beta )$, với $(\alpha ):ax + by + cz + d = 0$ và $(\beta ):ax + by + cz + D = 0$ $(d \ne D).$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-2.png" alt="">

Lúc đó: $d((\alpha );(\beta ))$ $= d(A;(\beta ))$ $= \frac{{|d – D|}}{{\sqrt {{a^2} + {b^2} + {c^2}} }}$ với $A \in (\alpha ).$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 1: Trong không gian với hệ tọa độ $Oxyz$, tính khoảng cách $d$ từ $A(1;2;3)$ đến mặt phẳng $(Oxy).$

A. $d=1.$

B. $d=2.$

C. $d=3.$

D. $d = \sqrt 5 .$

Lời giải:

Mặt phẳng $(Oxy)$ có phương trình: $z = 0.$

$\Rightarrow d(A;(Oxy)) = \frac{{|3|}}{{\sqrt 1 }} = 3.$

> **Đáp án: C**

<!-- chunk:5 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 2: Trong không gian với hệ tọa độ $Oxyz$, gọi $A’$ là điểm đối xứng của điểm $A(1;2;3)$ qua mặt phẳng $(Oxy).$ Tính độ dài đoạn thẳng $AA’.$

A. $4.$

B. $2.$

C. $3.$

D. $6.$

Lời giải:

Mặt phẳng $(Oxy)$ có phương trình: $z = 0$ $\Rightarrow d(A;(Oxy)) = \frac{{|3|}}{{\sqrt 1 }} = 3.$

Suy ra: $AA’ = 2d(A;(Oxy)) = 6.$

> **Đáp án: D**

Kết quả lưu ý: Với $\left( {{x_0};{y_0};{z_0}} \right)$ ta có:

$d(M;(Oxy)) = \left| {{z_0}} \right|.$

$d(M;(Oyz)) = \left| {{x_0}} \right|.$

$d(M;(Oxz)) = \left| {{y_0}} \right|.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 3: Trong không gian với hệ tọa độ $Oxyz$, gọi $H$ là hình chiếu vuông góc của $A(1;2;-3)$ trên mặt phẳng $(Oxy).$ Tính diện tích $S$ tam giác $OHA.$

A. $S = \frac{{\sqrt {13} }}{2}.$

B. $S = \sqrt {10} .$

C. $S = \frac{{3\sqrt 5 }}{2}.$

D. $S = \frac{{5\sqrt {15} }}{2}.$

Lời giải:

Ta có: $OA = \sqrt {14}$, $AH = d(A;(Oxy)) = 3.$

Tam giác $OHA$ vuông tại $H$ suy ra: $OH = \sqrt {O{A^2} – A{H^2}} = \sqrt 5 .$

Vậy $S = \frac{1}{2}AH.OH = \frac{{3\sqrt 5 }}{2}.$

> **Đáp án: C**

<!-- chunk:7 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 4: Trong không gian với hệ tọa độ $Oxyz$, gọi $H$ là hình chiếu vuông góc của $A(1;2;-3)$ trên mặt phẳng $(Oxz).$ Tính diện tích $S$ tam giác $OHA.$

A. $S = \frac{{\sqrt {13} }}{2}.$

B. $S = \sqrt {10} .$

C. $S = \frac{{3\sqrt 5 }}{2}.$

D. $S = \frac{{5\sqrt {15} }}{2}.$

Lời giải:

Ta có: $OA = \sqrt {14}$, $AH = d(A;(Oyz)) = 2.$

Tam giác $OHA$ vuông tại $H$ suy ra: $OH = \sqrt {O{A^2} – A{H^2}} = \sqrt {10} .$

Vậy $S = \frac{1}{2}AH.OH = \sqrt {10} .$

> **Đáp án: B**

<!-- chunk:8 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 5: Trong không gian với hệ tọa độ $Oxyz$, tính khoảng cách $d$ từ $A(1;3;-2)$ đến mặt phẳng $(P):x + 2y – 2z + 1 = 0.$

A. $d=4.$

B. $d=2.$

C. $d=3.$

D. $d = \sqrt 5 .$

Lời giải:

Ta có: $d(A;(P)) = \frac{{|1 + 6 + 4 + 1|}}{{\sqrt {{1^2} + {2^2} + {{( – 2)}^2}} }} = 4.$

> **Đáp án: A**

<!-- chunk:9 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 6: Trong không gian với hệ tọa độ $Oxyz$, tính bán kính $R$ của mặt cầu tâm $A(1;3;2)$ và tiếp xúc với mặt phẳng $(P):x + 2y + 2z + 1 = 0.$

A. $d=4.$

B. $d=2.$

C. $d=3.$

D. $d = \sqrt 5 .$

Lời giải:

Do mặt cầu tâm $A$ tiếp xúc với mặt phẳng $(P):$

$\Leftrightarrow R = d(A;(P))$ $= \frac{{|1 + 6 + 4 + 1|}}{{\sqrt {{1^2} + {2^2} + {{( – 2)}^2}} }} = 4.$

> **Đáp án: A**

<!-- chunk:10 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 7: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(1;1;-2)$ và mặt phẳng $(P):2x+2y+z+1=0.$ Gọi $M$ là điểm bất kì thuộc $(P)$, tính độ dài nhỏ nhất của đoạn thẳng $AM.$

A. $2.$

B. $1.$

C. $\sqrt 2 .$

D. $\sqrt 3 .$

Lời giải:

Gọi $H$ là hình chiếu vuông góc của $A$ trên $(P).$

Ta có: $AM \ge AH$ $\Rightarrow A{M_{\min }} = AH = d(A;(P)) = 1.$

> **Đáp án: B**

<!-- chunk:11 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 8: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $K(1;1;0)$ và mặt phẳng $(\alpha ):x + y + z – 1 = 0.$ Gọi $(C)$ là đường tròn giao tuyến của mặt cầu tâm $K$, bán kính $R=2$ với mặt phẳng $(\alpha )$, tính diện tích $S$ của $(C).$

A. $S = \frac{{22\pi }}{3}.$

B. $S = \frac{{44\pi }}{3}.$

C. $S = \frac{{\sqrt {33} \pi }}{3}.$

D. $S = \frac{{11\pi }}{3}.$

Lời giải:

Ta có: $d(K;(\alpha )) = \frac{{\sqrt 3 }}{3}.$ Gọi $r$ là bán kính đường tròn $(C)$, ta có: $r = \sqrt {{R^2} – {{[d(K;(\alpha ))]}^2}} = \frac{{\sqrt {33} }}{3}.$

Vậy $S = \pi {r^2} = \frac{{11\pi }}{3}.$

> **Đáp án: D**

<!-- chunk:12 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 9: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $P(2;1;3).$ Gọi $(C)$ là đường tròn giao tuyến của mặt cầu tâm $P$, bán kính $R=5$ với mặt phẳng $(Oxy)$, tính diện tích $S$ của $(C).$

A. $S = 24\pi .$

B. $S = 64\pi .$

C. $S = 16\pi .$

D. $S = 21\pi .$

Lời giải:

Ta có: $d(P;(\alpha )) = 3.$

Gọi $r$ là bán kính đường tròn $(C)$, ta có:

$r = \sqrt {{R^2} – {{[d(P;(Oxy))]}^2}} = 4.$

Vậy $S = \pi {r^2} = 16\pi .$

> **Đáp án: C**

<!-- chunk:13 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 10: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $I( – 2;1;3).$ Gọi $(C)$ là đường tròn giao tuyến của mặt cầu tâm $I$, bán kính $R=5$ với mặt phẳng $(Oyz)$, tính diện tích $S$ của $(C).$

A. $S = 24\pi .$

B. $S = 64\pi .$

C. $S = 16\pi .$

D. $S = 21\pi .$

Lời giải:

Ta có: $d(I;(\alpha )) = 2.$ Gọi $r$ là bán kính đường tròn $(C)$, ta có:

$r = \sqrt {{R^2} – {{[d(I;(Oyz))]}^2}} = \sqrt {21} .$

Vậy $S = \pi {r^2} = 21\pi .$

> **Đáp án: D**

<!-- chunk:14 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 11: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $F(-2;-1;5).$ Gọi $(C)$ là đường tròn giao tuyến của mặt cầu tâm $F$, bán kính $R=5$ với mặt phẳng $(Oxz)$, tính diện tích $S$ của $(C).$

A. $S = 24\pi .$

B. $S = 64\pi .$

C. $S = 16\pi .$

D. $S = 21\pi .$

Lời giải:

Ta có: $d(F;(Oxz)) = 1.$ Gọi $r$ là bán kính đường tròn $(C)$, ta có:

$r = \sqrt {{R^2} – {{[d(F;(Oxz))]}^2}} = \sqrt {24} .$

Vậy $S = \pi {r^2} = 24\pi .$

> **Đáp án: A**

<!-- chunk:15 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 12: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $I( – 1;1;1)$ và $A(1;3;2).$ Gọi $H$ là hình chiếu vuông góc của $A$ trên mặt phẳng $(P):x + 2y – 2z + 1 = 0.$ Tính diện tích $S$ tam giác $IHA.$

A. $S=4.$

B. $S = \frac{{2\sqrt {65} }}{9}.$

C. $S=2.$

D. $S = \frac{{\sqrt {65} }}{9}.$

Lời giải:

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-3.png" alt="">

Ta có: $IA = 3$, $AH = d(A;(P)) = \frac{4}{3}$ và $I \in (P).$

Tam giác $IHA$ vuông tại $H$ suy ra:

$IH = \sqrt {I{A^2} – A{H^2}} = \frac{{\sqrt {65} }}{3}.$

Vậy $S = \frac{1}{2}AH.IH = \frac{{2\sqrt {65} }}{9}.$

> **Đáp án: B**

<!-- chunk:16 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 13: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $I(1;1;1)$ và mặt phẳng $(P):x – 2y – 2z + 4 = 0.$ Gọi $M$ là điểm thuộc trục $Ox$, có hoành độ bằng $a$ $(a>1)$ và có khoảng cách đến mặt phẳng $(P)$ bằng $2.$ Tính độ dài đoạn thẳng $IM.$

A. $\sqrt 3 .$

B. $\sqrt {123} .$

C. $3.$

D. $123.$

Lời giải:

Gọi $M(a;0;0) \in Ox$ $\Rightarrow d(M;(P)) = \frac{{|a + 4|}}{3}.$

Theo giả thiết: $d(M;(P)) = 2$ $\Leftrightarrow |a + 4| = 6$ $\Leftrightarrow a = 2$ hoặc $a = – 10.$

Do $a > 1$ $\Rightarrow M(2;0;0).$

Vậy $\overrightarrow {IM} = (1; – 1; – 1)$ $\Rightarrow IM = \sqrt 3 .$

> **Đáp án: A**
Nhận xét: Có học sinh thực hiện như sau: Do $M(a;0;0)$ $\Rightarrow \overrightarrow {IM} = (a – 1; – 1; – 1)$ $\Rightarrow IM = \sqrt {{a^2} – 2a + 3}$ và kiểm tra từ đáp án. Việc kiểm tra này có tối ưu và nhanh chóng hay không thì để độc giả tự đánh giá.

<!-- chunk:17 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 14: Trong không gian với hệ tọa độ $Oxyz$, cho điểm $I(0;1;1)$ và mặt phẳng $(P):x – 2y – 2z + 4 = 0.$ Gọi $M$ là điểm thuộc trục $Ox$, có hoành độ bằng $a$ $(a >1)$ và có khoảng cách đến mặt phẳng $(P)$ bằng $3.$ Tính độ dài đoạn thẳng $IM.$

A. $3\sqrt 3 .$

B. $3\sqrt {19} .$

C. $27.$

D. $171.$

Lời giải:

Gọi $M(a;0;0) \in Ox$ $\Rightarrow d(M;(P)) = \frac{{|a + 4|}}{3}.$

Theo giả thiết: $d(M;(P)) = 3$ $\Leftrightarrow |a + 4| = 9$ $\Leftrightarrow a = 5$ hoặc $a = – 13.$

Do $a > 1$ $\Rightarrow M(5;0;0).$

Vậy $\overrightarrow {IM} = (5; – 1; – 1)$ $\Rightarrow IM = 3\sqrt 3 .$

> **Đáp án: A**

<!-- chunk:18 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 15: Trong không gian với hệ tọa độ $Oxyz$, gọi $A$, $B$ là hai điểm phân biệt thuộc trục $Ox$ và có khoảng cách đến mặt phẳng $(\alpha ):x – 2y – 2z + 4 = 0$ bằng $2.$ Tính độ dài đoạn thẳng $AB.$

A. $12.$

B. $14.$

C. $10.$

D. $8.$

Lời giải:

Gọi $M(a;0;0) \in Ox$ $\Rightarrow d(M;(\alpha )) = \frac{{|a + 4|}}{3}.$

Theo giả thiết: $d(M;(\alpha )) = 2$ $\Leftrightarrow |a + 4| = 6$ $\Leftrightarrow a = 2$ hoặc $a = – 10.$ Không mất tính tổng quát, giả sử $A(2;0;0)$, $B( – 10;0;0)$ $\Rightarrow \overrightarrow {AB} = ( – 12;0;0).$ Vậy $AB = 12.$

> **Đáp án: A**

<!-- chunk:19 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 16: Trong không gian với hệ tọa độ $Oxyz$, cho hai mặt phẳng song song $(P):x + y + 3z + 1 = 0$ và $(Q):x + y + 3z + 5 = 0.$ Tính khoảng cách $d$ giữa hai mặt phẳng $(P)$ và $(Q).$

A. $d = \frac{{2\sqrt {11} }}{{11}}.$

B. $d = \frac{{4\sqrt {11} }}{{11}}.$

C. $d = 2\sqrt {11} .$

D. $d=11.$

Lời giải:

Chọn $M( – 1;0;0) \in (P)$ $\Rightarrow d = d((P);(Q))$ $= \frac{{| – 1 + 5|}}{{\sqrt {{1^2} + {1^2} + {3^2}} }}$ $= \frac{{4\sqrt {11} }}{{11}}.$

> **Đáp án: B**

Nhận xét: Có thể sử dụng kết quả ở mục A – dạng 2 để chọn nhanh đáp án.

<!-- chunk:20 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 17: Trong không gian với hệ tọa độ $Oxyz$, gọi $(S)$ là mặt cầu bất kì tiếp xúc với hai mặt phẳng $(P):x + 2y + 2z + 1 = 0$ và $(Q):x + 2y + 2z + 7 = 0.$ Tính bán kính $R$ của mặt cầu $(S).$

A. $R=6.$

B. $R=2.$

C. $R=1.$

D. $R=3.$

Lời giải:

Do $(P)//(Q)$ $\Rightarrow R = \frac{1}{2}d((P);(Q))$ $= \frac{1}{2}.\frac{{|1 – 7|}}{{\sqrt {{1^2} + {2^2} + {2^2}} }} = 1.$

> **Đáp án: C**

Nhận xét: Mọi mặt cầu $(S)$ tiếp xúc đồng thời với mặt phẳng song song $(P)$, $(Q)$ đều có bán kính $R$ bằng nhau và $R = \frac{1}{2}d((P);(Q)).$

<!-- chunk:21 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 18: Trong không gian với hệ tọa độ $Oxyz$, cho hai mặt phẳng song song $(\alpha ):2x + y + 2z + 1 = 0$ và $(\beta ):2x + y + 2z + 3 = 0.$ Tính tổng khoảng cách $d$ từ gốc tọa độ $O$ đến hai mặt phẳng $(\alpha )$ và $(\beta ).$

A. $d = \frac{2}{3}.$

B. $d = \frac{4}{3}.$

C. $d=2.$

D. $d = \frac{1}{3}.$

Lời giải:

Ta có: $d(O;(\alpha )) = \frac{{|1|}}{{\sqrt {{2^2} + {1^2} + {2^2}} }} = \frac{1}{3}$ và $d(O;(\beta )) = \frac{{|3|}}{{\sqrt {{2^2} + {1^2} + {2^2}} }} = 1$ suy ra:

$d = {d_1} + {d_2} = \frac{4}{3}.$

> **Đáp án: B**

<!-- chunk:22 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 19: Trong không gian với hệ tọa độ $Oxyz$, tìm tập hợp tất cả các giá trị thực của tham số $m$ sao cho khoảng cách giữa hai mặt phẳng $(P):x + 2y + 2z + 2 = 0$ và $(Q):x + 2y + 2z + 2m – 1 = 0$ bằng $1.$

A. $\{ 3\} .$

B. $\{ 3, – 3\} .$

C. $\{ 0,3\} .$

D. $\{ 0, – 3\} .$

Lời giải:

Chọn $M( – 2;0;0) \in (P)$ $\Rightarrow d((P);(Q))$ $= d(M;(Q))$ $= \frac{{|2m – 3|}}{3}.$

Theo giả thiết: $\frac{{|2m – 3|}}{3} = 1$ $\Leftrightarrow |2m – 3| = 3$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2m – 3 = 3}\\
{2m – 3 = – 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 3}\\
{m = 0}
\end{array}} \right..
$$

> **Đáp án: C**

<!-- chunk:23 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 20: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(1;1;1)$ và $B(2;1;-1).$ Viết phương trình mặt phẳng $(P)$ qua $A$ và cách $B$ một khoảng lớn nhất.

A. $x + y + z – 3 = 0.$

B. $3x + 5y + 10z – 18 = 0.$

C. $9x – 10y + 12z – 11 = 0.$

D. $x – 2z + 1 = 0.$

Lời giải:

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-4.png" alt="">

Gọi $H$ là hình chiếu vuông góc của $B$ trên mặt phẳng $(P)$, ta có: $d(B;(P)) = BH \le AB$ $\Rightarrow d{(B;(P))_{\max }} = AB.$

Vậy $(P)$ là mặt phẳng qua $A$ và có một vectơ pháp tuyến là $\overrightarrow {AB} = (1;0; – 2).$

Suy ra $(P):1(x – 1) + 0(y – 1) – 2(z – 1) = 0.$

$\Leftrightarrow x – 2z + 1 = 0.$

> **Đáp án: D**

<!-- chunk:24 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 21: Trong không gian với hệ tọa độ $Oxyz$, cho hai điểm $A(1;1;1)$ và $B(2;1;-1).$ Gọi $\vec n = (1;a;b)$, $(a;b \in R)$ là một vectơ pháp tuyến của mặt phẳng $(P)$ qua $A$ và cách $B$ một khoảng lớn nhất. Tính $a + b.$

A. $2.$

B. $3.$

C. $-2.$

D. $-3.$

Lời giải:

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-5.png" alt="">

Gọi $H$ là hình chiếu vuông góc của $B$ trên mặt phẳng $(P)$, ta có:

$d(B;(P)) = BH \le AB$ $\Rightarrow d{(B;(P))_{\max }} = AB.$

Vậy $(P)$ là mặt phẳng qua $A$ và có một vectơ pháp tuyến là $\overrightarrow {AB} = (1;0; – 2).$

Suy ra $a = 0$ và $b = – 2$ $\Rightarrow a + b = – 2.$

> **Đáp án: C**

<!-- chunk:25 level:1 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## D. Vô số.

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} = – 4 \ne 0$ $\Rightarrow A$, $B$, $C$, $D$ không đồng phẳng.

Vậy tồn tại hai mặt phẳng chứa $B$, $C$ và cách đều hai điểm $A$, $D$ là:

+ Trường hợp 1: Mặt phẳng chứa $B$, $C$ và song song với đường thẳng $AD.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-6.png" alt="">

+ Trường hợp 2: Mặt phẳng chứa $B$, $C$ và đi qua trung điểm $I$ của đoạn thẳng $AD.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-7.png" alt="">

> **Đáp án: C**

<!-- chunk:26 level:1 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## D. Vô số.

Lời giải:

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-8.png" alt="">

Ta có: $\overrightarrow {AC} = ( – 1;3; – 1)$, $\overrightarrow {AB} = (2; – 2;1)$, $\overrightarrow {CD} = (4; – 4;2)$ $\Rightarrow \overrightarrow {CD} = 2\overrightarrow {AB}$ và $\overrightarrow {AB}$, $\overrightarrow {AC}$ không cùng phương. Vậy $AB//CD$ $\Rightarrow$ có vô số mặt phẳng chứa $A$, $B$ và cách đều $C$, $D.$

> **Đáp án: D**

<!-- chunk:27 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 24: Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1;1;0)$, $B(3;1; – 2)$, $C(0;2;0)$ và $D( – 1;3;2).$ Biết rằng qua $B$, $C$ có hai mặt phẳng cách đều $A$, $D.$ Tính tổng khoảng cách từ $O$ đến hai mặt phẳng đó.

A. $\frac{{9\sqrt {10} + 5\sqrt 6 }}{5}.$

B. $\frac{{3\sqrt {10} + 5\sqrt 6 }}{{15}}.$

C. $\frac{{9\sqrt {10} + 5\sqrt 6 }}{{15}}.$

D. $\frac{{9\sqrt {10} + 7\sqrt 6 }}{{15}}.$

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} \ne 0$ $\Rightarrow A$, $B$, $C$, $D$ không đồng phẳng. Vậy tồn tại hai mặt phẳng chứa $B$, $C$ và cách đều hai điểm $A$, $D$ là:

+ Trường hợp 1: Mặt phẳng chứa $B$, $C$ và song song với đường thẳng $AD.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-9.png" alt="">

Mặt phẳng $(P)$ qua $C(0;2;0)$ và có một vectơ pháp tuyến là ${\vec n_p} = [\overrightarrow {BC} ,\overrightarrow {AD} ] = ( – 2;2; – 4)$, có phương trình:

$(P): – 2(x – 0) + 2(y – 2) – 4(z – 0) = 0$ $\Leftrightarrow x – y + 2z + 2 = 0.$

+ Trường hợp 2: Mặt phẳng chứa $B$, $C$ và đi qua trung điểm $I$ của đoạn thẳng $AD.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-10.png" alt="">

Trung điểm $I$ của $AD$ là $I(0;2;1).$ Mặt phẳng $(Q)$ qua $C(0;2;0)$ và có một vectơ pháp tuyến là ${\vec n_Q} = [\overrightarrow {BC} ,\overrightarrow {IB} ] = ( – 1; – 3;0)$, có phương trình:

$(Q): – 1(x – 0) – 3(y – 2) – 0(z – 0) = 0$ $\Leftrightarrow – x – 3y + 6 = 0.$

Vậy $d(O;(P)) + d(O;(Q))$ $= \frac{{9\sqrt {10} + 5\sqrt 6 }}{{15}}.$

> **Đáp án: B**

<!-- chunk:28 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 25: Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1;1;0)$, $B(3;1; – 2)$, $C(0;2;0)$ và $D( – 1;3;2).$ Gọi $\vec n(1;b;0)$, $(b \in R)$ là một vectơ pháp tuyến của mặt phẳng qua $B$, $C$ và cách đều $A$, $D.$ Tính ${b^2}.$

A. $16.$

B. $1.$

C. $4.$

D. $9.$

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} \ne 0$ $\Rightarrow A$, $B$, $C$, $D$ không đồng phẳng. Vậy tồn tại hai mặt phẳng chứa $B$, $C$ và cách đều hai điểm $A$, $D$ là:

+ Trường hợp 1: Mặt phẳng chứa $B$, $C$ và song song với đường thẳng $AD.$

Mặt phẳng $(P)$ qua $C(0;2;0)$ và có một vectơ pháp tuyến là ${\vec n_P} = [\overrightarrow {BC} ,\overrightarrow {AD} ] = ( – 2;2; – 4).$

+ Trường hợp 2: Mặt phẳng chứa $B$, $C$ và đi qua trung điểm $I$ của đoạn thẳng $AD.$

Trung điểm $I$ của $AD$ là $I(0;2;1).$

Mặt phẳng $(Q)$ qua $C(0;2;0)$ và có một vectơ pháp tuyến là ${\vec n_Q} = [\overrightarrow {BC} ,\overrightarrow {IB} ] = ( – 1; – 3;0).$

Theo giả thiết $\vec n(1;b;0)$ $= {\vec n_Q} = ( – 1; – 3;0)$ $\Rightarrow b = 3.$

Vậy ${b^2} = 9.$

> **Đáp án: D**

<!-- chunk:29 level:1 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## D. Vô số.

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} = 7 \ne 0$ $\Rightarrow A$, $B$, $C$, $D$ không đồng phẳng. Vậy tồn tại hai mặt phẳng chứa $B$, $C$ thỏa mãn khoảng cách từ $A$ đến $(P)$ bằng hai lần khoảng cách từ $D$ đến $(P).$

+ Trường hợp 1: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $I$ sao cho $D$ là trung điểm $AI.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-11.png" alt="">

+ Trường hợp 2: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $K$ sao cho $\overrightarrow {AK} = \frac{2}{3}\overrightarrow {AD} .$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-12.png" alt="">

> **Đáp án: C**

<!-- chunk:30 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 27: Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1;1;2)$, $B(2;2;0)$, $C( – 1;2;3)$ và $D(3;1;1).$ Biết rằng qua $B$, $C$ có hai mặt phẳng sao cho khoảng cách từ $A$ đến $(P)$ bằng hai lần khoảng cách từ $D$ đến $(P).$ Tính tổng khoảng cách từ $O$ đến hai mặt phẳng đó.

A. $\frac{{12\sqrt {43} + 172\sqrt 3 }}{{129}}.$

B. $\frac{{48\sqrt {43} + 72\sqrt 3 }}{{129}}.$

C. $\frac{{16\sqrt {33} + 24\sqrt {11} }}{{33}}.$

D. $\frac{{344\sqrt {11} + 176\sqrt {43} }}{{473}}.$

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} \ne 0$ $\Rightarrow A$, $B$, $C$, $D$ không đồng phẳng. Vậy tồn tại hai mặt phẳng chứa $B$, $C$ thỏa mãn khoảng cách từ $A$ đến $(P)$ bằng hai lần khoảng cách từ $D$ đến $(P)$ là:

+ Trường hợp 1: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $I$ sao cho $D$ là trung điểm $AI.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-13.png" alt="">

Ta có: $D$ là trung điểm $AI$ $\Rightarrow I(5;1;0).$ Mặt phẳng $(P)$ qua $C( – 1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_p} = [\overrightarrow {BC} ,\overrightarrow {IC} ] = ( – 3; – 9; – 3)$, có phương trình:

$(P): – 3(x + 1) – 9(y – 2) – 3(z – 3) = 0$ $\Leftrightarrow x + 3y + z – 8 = 0.$

+ Trường hợp 2: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $K$ sao cho $\overrightarrow {AK} = \frac{2}{3}\overrightarrow {AD} .$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-14.png" alt="">

Từ $\overrightarrow {AK} = \frac{2}{3}\overrightarrow {AD}$ $\Rightarrow K\left( {\frac{7}{3};1;\frac{4}{3}} \right).$ Mặt phẳng $(Q)$ qua $C( – 1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_Q} = [\overrightarrow {BC} ,\overrightarrow {KC} ] = ( – 3; – 5; – 3)$, có phương trình:

$(Q): – 3(x + 1) – 5(y – 2) – 3(z – 3) = 0$ $\Leftrightarrow 3x + 5y + 3z – 16 = 0.$

Vậy $d(O;(P)) + d(O;(Q))$ $= \frac{{16\sqrt {33} + 24\sqrt {11} }}{{33}}.$

> **Đáp án: D**

<!-- chunk:31 level:3 source:https://toanmath.com/2020/02/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung.html -->
## Ví dụ 28: Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A(1;1;2)$, $B(2;2;0)$, $C( – 1;2;3)$ và $D(3;1;1).$ Biết rằng qua $B$, $C$ có hai mặt phẳng sao cho khoảng cách từ $A$ đến $(P)$ bằng hai lần khoảng cách từ $D$ đến $(P).$ Gọi $\alpha$ là góc giữa hai mặt phẳng đó, khẳng định nào sau đây đúng?

A. $\cos \alpha = – \frac{{\sqrt {418} }}{{19}}.$

B. $\cos \alpha = \frac{{\sqrt {418} }}{{19}}.$

C. $\cos \alpha = \frac{{\sqrt {317} }}{{19}}.$

D. $\cos \alpha = \frac{{21\sqrt {473} }}{{473}}.$

Lời giải:

Kiểm tra được: $[\overrightarrow {AB} ,\overrightarrow {AC} ].\overrightarrow {AD} \ne 0$ $\Rightarrow A$, $B$, $C$, $D.$ không đồng phẳng. Vậy tồn tại hai mặt phẳng chứa $B$, $C$ thỏa mãn khoảng cách từ $A$ đến $(P)$ bằng hai lần khoảng cách từ $D$ đến $(P)$ là:

+ Trường hợp 1: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $I$ sao cho $D$ là trung điểm $AI.$

Ta có: $D$ là trung điểm $AI$ $\Rightarrow I(5;1;0).$ Mặt phẳng $(P)$ qua $C(-1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_p} = [\overrightarrow {BC} ,\overrightarrow {IC} ] = ( – 3; – 9; – 3)$, có phương trình:

$(P): – 3(x + 1) – 9(y – 2) – 3(z – 3) = 0$ $\Leftrightarrow x + 3y + z – 8 = 0.$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-15.png" alt="">

+ Trường hợp 2: Mặt phẳng $(P)$ chứa $B$, $C$ và $(P)$ qua điểm $K$ sao cho $\overrightarrow {AK} = \frac{2}{3}\overrightarrow {AD} .$

<img link="data_for_rag/toan12/images/cong-thuc-tinh-khoang-cach-tu-mot-diem-den-mat-phang-va-bai-tap-ap-dung-16.png" alt="">

Từ $\overrightarrow {AK} = \frac{2}{3}\overrightarrow {AD}$ $\Rightarrow K\left( {\frac{7}{3};1;\frac{4}{3}} \right).$ Mặt phẳng $(Q)$ qua $C(-1;2;3)$ và có một vectơ pháp tuyến là ${\vec n_Q} = [\overrightarrow {BC} ,\overrightarrow {KC} ]$ $= ( – 3; – 5; – 3)$, có phương trình:

$(Q): – 3(x + 1) – 5(y – 2) – 3(z – 3) = 0$ $\Leftrightarrow 3x + 5y + 3z – 16 = 0.$

Vậy $\cos \alpha = \frac{{\left| {{{\vec n}_p}.{{\vec n}_Q}} \right|}}{{\left| {{{\vec n}_p}} \right|.\left| {{{\vec n}_Q}} \right|}} = \frac{{\sqrt {418} }}{{19}}.$

> **Đáp án: D**