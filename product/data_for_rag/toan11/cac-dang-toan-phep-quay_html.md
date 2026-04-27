# Các dạng toán phép quay

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
Bài viết trình bày lý thuyết và hướng dẫn giải các dạng toán phép quay trong chương trình Hình học 11 chương 1. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu phép dời hình và phép đồng dạng trong mặt phẳng xuất bản trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## A. KIẾN THỨC CẦN NẮM

1. Định nghĩa phép quay
• Cho điểm $O$ và góc lượng giác $\alpha$. Phép biến hình biến $O$ thành chính nó và biến mỗi điểm $M$ khác $O$ thành điểm $M’$ sao cho $OM’=OM$ và góc lượng giác $\left( OM;OM’ \right)=\alpha$ được gọi là phép quay tâm $O$, $\alpha$ được gọi là góc quay.

• Phép quay tâm $O$ góc quay $\alpha$ được kí hiệu là ${{Q}_{\left( O;\alpha  \right)}}$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-1.png" alt="cac-dang-toan-phep-quay-1">

• Nhận xét:

+ Khi $\alpha = 2k\pi$, $k \in Z$ thì ${Q_{\left( {O;\alpha } \right)}}$ là phép đồng nhất.

+ Khi $\alpha = \left( {2k + 1} \right)\pi$, $k \in Z$ thì ${Q_{\left( {O;\alpha } \right)}}$ là phép đối xứng tâm $O.$

2. Biểu thức tọa độ của phép quay
• Trong mặt phẳng $Oxy$, giả sử $M\left( x;y \right)$ và $M’\left( x’;y’ \right)={{Q}_{\left( O,\alpha  \right)}}\left( M \right)$ thì 
$$
\left\{ \begin{array}{l}
x’ = x\cos \alpha – y\sin \alpha \\
y’ = x\sin \alpha + y\cos \alpha
\end{array} \right.
$$

• Trong mặt phẳng $Oxy$, giả sử $M\left( x;y \right)$, $I\left( a;b \right)$ và $M’\left( x’;y’ \right)={{Q}_{\left( I,\alpha  \right)}}\left( M \right)$ thì 
$$
\left\{ \begin{array}{l}
x’ = a + \left( {x – a} \right)\cos \alpha – \left( {y – b} \right)\sin \alpha \\
y’ = b + \left( {x – a} \right)\sin \alpha + \left( {y – b} \right)\cos \alpha
\end{array} \right.
$$

3. Tính chất của phép quay

• Các tính chất của phép quay:

+ Bảo toàn khoảng cách giữa hai điểm bất kì.

+ Biến một đường thẳng thành đường thẳng.

+ Biến một đoạn thẳng thành đoạn thẳng bằng đoạn đã cho.

+ Biến một tam giác thành tam giác bằng tam giác đã cho.

+ Biến đường tròn thành đường tròn có cùng bán kính.

• Lưu ý: Giả sử phép quay tâm $I$ góc quay $\alpha$ biến đường thẳng $d$ thành đường thẳng $d’$, khi đó:

+ Nếu $0<\alpha \le \frac{\pi }{2}$ thì góc giữa hai đường thẳng $d$ và $d’$ bằng $\alpha .$

+ Nếu $\frac{\pi }{2}<\alpha <\pi$ thì góc giữa hai đường thẳng $d$ và $d’$ bằng $\pi -\alpha .$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-2.png" alt="cac-dang-toan-phep-quay-2">

<!-- chunk:2 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## **B. CÁC DẠNG TOÁN PHÉP QUAY

****Dạng toán 1. Xác định ảnh của một hình qua phép quay

****Phương pháp**: Sử dụng định nghĩa phép quay, biểu thức tọa độ của phép quay và các tính chất của phép quay.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 1. Cho $M\left( 3;4 \right)$. Tìm ảnh của điểm $M$ qua phép quay tâm $O$ góc quay ${{30}^{0}}$.

Gọi $M’\left( {x’;y’} \right) = {Q_{\left( {O;{{30}^0}} \right)}}.$ Áp dụng biểu thức tọa độ của phép quay 
$$
\left\{ \begin{array}{l}
x’ = x\cos \alpha – y\sin \alpha \\
y’ = x\sin \alpha + y\cos \alpha
\end{array} \right.
$$
, ta có: 
$$
\left\{ \begin{array}{l}
x’ = 3\cos {30^0} – 4\sin {30^0} = \frac{{3\sqrt 3 }}{2} – 2\\
y’ = 3\sin {30^0} + 4\cos {30^0} = \frac{3}{2} + 2\sqrt 3
\end{array} \right.
$$
 $\Rightarrow M’\left( {\frac{{3\sqrt 3 }}{2} – 2;\frac{3}{2} + 2\sqrt 3 } \right).$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 2. Cho $I\left( 2;1 \right)$ và đường thẳng $d:2x+3y+4=0$. Tìm ảnh của $d$ qua ${{Q}_{\left( I;{{45}^{0}} \right)}}$.

Lấy hai điểm $M\left( { – 2;0} \right)$, $N\left( {1; – 2} \right)$ thuộc $d.$

Gọi $M’\left( {{x_1};{y_1}} \right)$, $N’\left( {{x_2};{y_2}} \right)$ là ảnh của $M,N$ qua ${Q_{\left( {I;{{45}^0}} \right)}}.$

Ta có 
$$
\left\{ \begin{array}{l}
{x_1} = 2 + \left( { – 2 – 2} \right)\cos {45^0} – \left( {0 – 1} \right)\sin {45^0}\\
{y_1} = 1 + \left( { – 2 – 2} \right)\sin {45^0} + \left( {0 – 1} \right)\cos {45^0}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_1} = 2 – \frac{{3\sqrt 2 }}{2}\\
{y_1} = 1 – \frac{{5\sqrt 2 }}{2}
\end{array} \right.
$$
 $\Rightarrow M’\left( {2 – \frac{{3\sqrt 2 }}{2};1 – \frac{{5\sqrt 2 }}{2}} \right).$

Tương tự: 
$$
\left\{ \begin{array}{l}
{x_2} = 2 + \left( {1 – 2} \right)\cos {45^0} – \left( { – 2 – 1} \right)\sin {45^0}\\
{y_2} = 1 + \left( {1 – 2} \right)\sin {45^0} + \left( { – 2 – 1} \right)\cos {45^0}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_2} = 2 + \sqrt 2 \\
{y_2} = 1 – 2\sqrt 2
\end{array} \right.
$$
 $\Rightarrow N’\left( {2 + \sqrt 2 ;1 – 2\sqrt 2 } \right).$

Ta có $\overrightarrow {M’N’} = \left( {\frac{{5\sqrt 2 }}{2};\frac{{\sqrt 2 }}{2}} \right)$ $= \frac{{\sqrt 2 }}{2}\left( {5;1} \right).$

Gọi $d’ = {Q_{\left( {I;{{45}^0}} \right)}}\left( d \right)$ thì $d’$ có vectơ chỉ phương $\overrightarrow u = \overrightarrow {M’N’} = \left( {5;1} \right)$, suy ra vectơ pháp tuyến $\overrightarrow n = \left( { – 1;5} \right).$

Phương trình đường thẳng $d’$ là: $– \left( {x – 2 – \sqrt 2 } \right) + 5\left( {y – 1 + 2\sqrt 2 } \right) = 0$ $\Leftrightarrow – x + 5y – 3 + 10\sqrt 2 = 0.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 3. Cho hình vuông $ABCD$ tâm $O$, $M$ là trung điểm của $AB$, $N$ là trung điểm của $OA$. Tìm ảnh của tam giác $AMN$ qua phép quay tâm $O$ góc quay ${{90}^{0}}$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-3.png" alt="cac-dang-toan-phep-quay-3">

Phép quay ${{Q}_{\left( O;{{90}^{0}} \right)}}$ biến $A$ thành $D$, biến $M$ thành $M’$ là trung điểm của $AD$, biến $N$ thành $N’$ là trung điểm của $OD$. Do đó nó biến tam giác $AMN$ thành tam giác $DM’N’$.

<!-- chunk:6 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Dạng toán 2. Sử dụng phép quay để giải các bài toán dựng hình
Phương pháp: Xem điểm cần dựng là giao của một đường có sẵn và ảnh của một đường khác qua phép quay ${{Q}_{\left( I;\alpha  \right)}}$ nào đó.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 4. Cho điểm $A$ và hai đường thẳng ${{d}_{1}}$, ${{d}_{2}}$. Dựng tam giác $ABC$ vuông cân tại $A$ sao cho $B\in {{d}_{1}}$, $C\in {{d}_{2}}$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-4.png" alt="cac-dang-toan-phep-quay-4">

Phân tích:

Giả sử đã dựng được tam giác $ABC$ thỏa mãn yêu cầu bài toán.

Ta có thể giả sử $\left( AB,AC \right)={{90}^{0}}$, khi đó ${{Q}_{\left( A;-{{90}^{0}} \right)}}\left( C \right)=B$, mà $C\in {{d}_{2}}$ nên $B\in {{d}_{2}}’$ với ${{d}_{2}}’={{Q}_{\left( A;-{{90}^{0}} \right)}}\left( {{d}_{2}} \right)$.

Ta lại có $B\in {{d}_{1}}$ nên $B={{d}_{1}}\cap {{d}_{2}}’$.

Cách dựng:

+ Dựng đường thẳng ${{d}_{2}}’$ là ảnh của ${{d}_{2}}$ qua ${{Q}_{\left( A;-{{90}^{0}} \right)}}$.

+ Dựng giao điểm $B={{d}_{1}}\cap {{d}_{2}}’$.

+ Dựng đường thẳng qua $A$ vuông góc với $AB$ cắt ${{d}_{2}}$ tại $C$.

Tam giác $ABC$ là tam giác cần dựng.

Chứng minh:

Từ cách dựng suy ra ${{Q}_{\left( A;{{90}^{0}} \right)}}\left( B \right)=C$ nên $AB=AC$ và $\widehat{BAC}={{90}^{0}}$ do đó tam giác $ABC$ vuông cân tại $A$.

Nhận xét:

+ Nếu ${{d}_{1}},{{d}_{2}}$ không vuông góc thì bài toán có một nghiệm hình.

+ Nếu ${{d}_{1}}\bot {{d}_{2}}$ và $A$ nằm trên đường phân giác của một trong các góc tạo bởi ${{d}_{1}},{{d}_{2}}$ thì bài toán có vô số nghiệm hình.

+ Nếu ${{d}_{1}}\bot {{d}_{2}}$ và $A$ không nằm trên đường phân giác của một trong các góc tạo bởi ${{d}_{1}},{{d}_{2}}$ thì bài toán vô nghiệm hình.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 5. Cho tam giác $ABC$ có $\left( AB,AC \right)=\alpha$ $\left( {{0}^{0}}<\alpha <{{90}^{0}} \right)$ và một điểm $M$ nằm trên cạnh $AB$. Dựng trên các đường thẳng $CB$, $CA$ các điểm $N$, $P$ sao cho $MN=MP$ và đường tròn $\left( AMP \right)$ tiếp xúc với $MN$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-5.png" alt="cac-dang-toan-phep-quay-5">

Phân tích:

Giả sử đã dựng được các điểm $N$, $P$ với $N\in BC$, $P\in AC$ sao cho $MN=MP$ và đường tròn $\left( AMP \right)$ tiếp xúc với $MN$.

Khi đó do $MN$ tiếp xúc với đường tròn $\left( AMP \right)$ nên $\widehat{PMN}=\widehat{A}=\alpha$.

Từ đó $\left( MP;MN \right)=-\alpha$, ta lại có $MP=MN$ nên ${{Q}_{\left( M,-\alpha \right)}}\left( P \right)=N$.

Giả sử $O={{Q}_{\left( M,-\alpha \right)}}\left( A \right)$ và $I=ON\cap AC$.

Theo tính chất phép quay ta có $\widehat{NIC}=\widehat{\left( ON,AP \right)}=\alpha$ $\Rightarrow \widehat{NIC}=\widehat{BAC}\Rightarrow IN\parallel AB$.

Cách dựng:

+ Dựng điểm $O = {Q_{\left( {M, – \alpha } \right)}}\left( A \right).$

+ Dựng đường thẳng qua $O$ song song với $AB$ cắt $BC$ tại $N.$

+ Dựng tia $MP$ cắt $AC$ tại $P$ sao cho $\widehat{NMP}=\alpha .$

Như vây các điểm $N$, $P$ là các điểm cần dựng.

Chứng minh:

Vì $ON\parallel AB$ nên $\widehat{AMO}=\widehat{MON}=\alpha$ $\Rightarrow \widehat{PMN}=\widehat{MAP}=\alpha$ suy ra đường tròn $\left( AMN \right)$ tiếp xúc với $MN$. Ta có ${{Q}_{\left( M;-\alpha \right)}}: MP\to MN$ nên $MP=MN$.

Nhận xét: Bài toán có một nghiệm hình duy nhất.

[ads]

<!-- chunk:9 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Dạng toán 3. Sử dụng phép quay để giải các bài toán tập hợp điểm
Phương pháp: Xem điểm cần dựng là giao của một đường có sẵn và ảnh của một đường khác qua phép quay ${{Q}_{\left( I;\alpha  \right)}}$ nào đó. Để tìm tập hợp điểm $M’$ ta đi tìm tập hợp điểm $M$ mà ${{Q}_{\left( I;\alpha  \right)}}$ nào đó biến điểm $M$ thành điểm $M’$, khi đó nếu $M\in \left( H \right)$ thì $M’\in \left( H’ \right)={{Q}_{\left( I;\alpha  \right)}}\left( \left( H \right) \right)$.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 6. Cho đường thẳng $d$ và một điểm $G$ không nằm trên $d$. Với mỗi điểm $A$ nằm trên $d$ ta dựng tam giác đều $ABC$ có tâm $G$. Tìm quỹ tích các điểm $B$, $C$ khi $A$ di động trên $d$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-6.png" alt="cac-dang-toan-phep-quay-6">

Do tam giác $ABC$ đều và có tâm $G$ nên phép quay tâm $G$ góc quay ${{120}^{0}}$ biến $A$ thành $B$ hoặc $C$ và phép quay tâm $G$ góc quay ${{240}^{0}}$ biến $A$ thành $B$ hoặc $C$.

Mà $A\in d$ nên $B$, $C$ thuộc các đường thẳng là ảnh của $d$ trong hai phép quay nói trên.

Vậy quỹ tích các điểm $B$, $C$ là các đường thẳng ảnh của $d$ trong hai phép quay tâm $G$ góc quay ${{120}^{0}}$ và ${{240}^{0}}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 7. Cho tam giác đều $ABC$. Tìm tập hợp điểm $M$ nằm trong tam giác $ABC$ sao cho $M{{A}^{2}}+M{{B}^{2}}=M{{C}^{2}}.$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-7.png" alt="cac-dang-toan-phep-quay-7">

Xét phép quay ${{Q}_{\left( B;-{{60}^{0}} \right)}}$ thì $A$ biến thành $C$, giả sử điểm $M$ biến thành $M’$.

Khi đó $MA=M’C$, $MB=MM’$ nên $M{{A}^{2}}+M{{B}^{2}}=M{{C}^{2}}$ $\Leftrightarrow M'{{C}^{2}}+MM{{‘}^{2}}=M{{C}^{2}}$.

Do đó tam giác $M’MC$ vuông tại $M’$, suy ra $\widehat{BM’C}={{150}^{0}}$.

Ta lại có $AM=CM’$, $BM=BM’$ và $AB=BC\Rightarrow$ $\Delta AMB=\Delta CM’B\Rightarrow \widehat{AMB}=\widehat{CM’B}={{150}^{0}}$.

Vậy $M$ thuộc cung chứa góc ${{150}^{0}}$ với dây cung $AB$ nằm trong tam giác $ABC$.

Đảo lại lấy điểm $M$ thuộc cung $\overset\frown{AB}={{150}^{0}}$ trong tam giác $ABC$, gọi $M’={{Q}_{\left( B;-{{60}^{0}} \right)}}\left( M \right)$.

Do ${{Q}_{\left( B;-{{60}^{0}} \right)}}:\overset\frown{AMB}\to \overset\frown{CM’B}$ nên $\overset\frown{CM’B}={{150}^{0}}$.

Mặt khác tam giác $BMM’$ đều nên $\widehat{BM’M}={{60}^{0}}$ $\Rightarrow \widehat{CM’M}={{150}^{0}}-{{60}^{0}}={{90}^{0}}$.

Vì vậy $\Delta M’MC$ vuông tại $M’$ $\Rightarrow M'{{B}^{2}}+M'{{C}^{2}}=M{{C}^{2}}$ .

Mà $MA=M’C$, $MB=MM’\Rightarrow M{{A}^{2}}+M{{B}^{2}}=M{{C}^{2}}$.

Vậy tập hợp điểm $M$ thỏa yêu cầu bài toán là cung $\overset\frown{AB}={{150}^{0}}$ trong tam giác $ABC$ nhận $AB$ làm dây cung.

<!-- chunk:12 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 8. Cho tam giác $ABC$. Vẽ các tam giác đều $ABB’$ và $ACC’$ nằm phía ngoài tam giác $ABC$. Gọi $I,J$ lần lượt là trung điểm của $CB’$ và $BC’$. Chứng minh các điểm $A,I,J$ hoặc trùng nhau hoặc tạo thành một tam giác đều.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-8.png" alt="cac-dang-toan-phep-quay-8">

Giả sử góc lượng giác $\left( AB,AC \right)>0$.

Xét phép quay ${{Q}_{\left( A;{{60}^{0}} \right)}}$.

Ta có ${{Q}_{\left( A;{{60}^{0}} \right)}}:B’\mapsto B$, $C\mapsto C’$, do đó ${{Q}_{\left( A;{{60}^{0}} \right)}}:B’C\mapsto BC’.$

Mà $I,J$ lần lượt là trung điểm của $B’C$ và $BC’$ nên ${{Q}_{\left( A;{{60}^{0}} \right)}}\left( I \right)=J$.

Vậy nếu $I,J$ không trùng $A$ thì $\Delta AIJ$ đều.

Khi $\widehat{BAC}={{120}^{0}}$ thì $I\equiv J\equiv A$.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-quay.html -->
## Ví dụ 9. Cho hai đường tròn bằng nhau $\left( O;R \right)$ và $\left( O’;R \right)$ cắt nhau tại hai điểm $A,B$ sao cho $\widehat{OAO’}={{120}^{0}}$. Đường thẳng $d$ đi qua $B$ cắt hai đường tròn $\left( O \right)$ và $\left( O’ \right)$ theo thứ tự tại $M,M’$ sao cho $M$ nằm ngoài $\left( O’ \right)$ còn $M’$ nằm ngoài $\left( O \right)$. Gọi $S$ là giao điểm của các tiếp tuyến với hai đường tròn tại $M$ và $M’$. Xác định vị trí của $M,M’$ sao cho bán kính đường tròn ngoại tiếp tam giác $SMM’$ lớn nhất.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-quay-9.png" alt="cac-dang-toan-phep-quay-9">

Giả sử góc lượng giác $\left( AO’,AO \right)={{120}^{0}}.$

Xét phép quay ${{Q}_{\left( A;-{{120}^{0}} \right)}}$.

Gọi $B’={{Q}_{\left( A;-{{120}^{0}} \right)}}\left( B \right)$ thì $\widehat{BAB’}={{120}^{0}}$.

Dễ thấy $\widehat{OAB}={{60}^{0}}$ suy ra $\widehat{OAB}+\widehat{BAB’}={{180}^{0}}$ nên $O,A,B’$ thẳng hàng.

Ta có $\widehat{MBA}+\widehat{ABM’}={{180}^{0}}$, $\widehat{ABM’}+\widehat{AB’M’}={{180}^{0}}\Rightarrow \widehat{MBA}=\widehat{AB’M’}$.

Mà $\left( O;R \right)$ và $\left( O’;R’ \right)$ bằng nhau nên $AM=AM’\left( 1 \right)$.

Từ đó ta có $\Delta OAM=\Delta O’AM’\Rightarrow \widehat{OAM}=\widehat{O’AM’}$$\Rightarrow \widehat{O’AM}+\widehat{O’AM}=\widehat{OAM}+\widehat{O’AM}={{120}^{0}}$ hay $\widehat{MAM’}={{120}^{0}}\left( 2 \right)$.

Từ $\left( 1 \right);\left( 2 \right)$ suy ra ${{Q}_{\left( A;-{{120}^{0}} \right)}}\left( M \right)=M’$.

Do đó trong phép quay này tiếp tuyến $MS$ biến thành tiếp tuyến $M’S$ nên góc tù giữa hai đường thẳng $MS$ và $M’S$ bằng ${{120}^{0}}$, do đó $\widehat{MSM’}={{60}^{0}}$.

Áp dụng định lí sin cho tam giác $SMM’$ ta có $R=\frac{MM’}{2\sin {{60}^{0}}}=\frac{MM’}{\sqrt{3}}$ $\Rightarrow R$ lớn nhất khi $MM’$ lớn nhất.

Gọi $H,K$ lần lượt là hình chiếu của $O,O’$ trên $MM’$ thì ta có $MM’=2HK\le 2OO’$, đẳng thức xảy ra khi $MM’\parallel OO’$.

Vậy bán kính đường tròn ngoại tiếp tam giác $SMM’$ lớn nhất khi $M,M’$ là các giao điểm thứ hai của đường thẳng $d$ đi qua $B$ và song song với $OO’$ với hai đường tròn.