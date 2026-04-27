# Các dạng toán phép đối xứng tâm

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
Bài viết trình bày lý thuyết và hướng dẫn giải các dạng toán phép đối xứng tâm trong chương trình Hình học 11 chương 1. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu phép dời hình và phép đồng dạng trong mặt phẳng xuất bản trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## A. KIẾN THỨC CẦN NẮM
1. Định nghĩa phép đối xứng tâm

• Cho điểm $I$. Phép biến hình biến điểm $I$ thành chính nó và biến mỗi điểm $M$ khác $I$ thành điểm $M’$ sao cho $I$ là trung điểm của $MM’$ được gọi là phép đối xứng tâm $I$, kí hiệu ${{Đ}_{I}}$.

• ${Đ_I}\left( M \right) = M’$ $\Leftrightarrow \overrightarrow {IM} + \overrightarrow {IM’} = \overrightarrow 0 .$

• Nếu ${Đ_I}\left( {\left( H \right)} \right) = \left( H \right)$ thì $I$ được gọi là tâm đối xứng của hình $\left( H \right)$.

2. Biểu thức tọa độ của phép đối xứng tâm
Trong mặt phẳng $Oxy$ cho $I\left( a;b \right)$, $M\left( x;y \right)$, gọi $M’\left( x’;y’ \right)$ là ảnh của $M$ qua phép đối xứng tâm $I$ thì 
$$
\left\{ \begin{align}
& x’=2a-x \\
& y’=2b-y \\
\end{align} \right.
$$

3. Tính chất phép đối xứng tâm

+ Bảo toàn khoảng cách giữa hai điểm bất kì.

+ Biến một đường thẳng thành đường thẳng song song hoặc trùng với đường thẳng đã cho.

+ Biến một đoạn thẳng thành đoạn thẳng bằng đoạn thẳng đã cho.

+ Biến một tam giác thành tam giác bằng tam giác đã cho.

+ Biến đường tròn thành đường tròn có cùng bán kính.

<!-- chunk:2 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## **B. CÁC DẠNG TOÁN PHÉP ĐỐI XỨNG TÂM

****Dạng toán 1. Xác định ảnh của một hình qua phép đối xứng tâm

****Phương pháp**: Sử dụng biểu thức tọa độ và các tính chất của phép đối xứng tâm.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 1. Cho điểm $I\left( 1;1 \right)$ và đường thẳng $d:x+2y+3=0$. Tìm ảnh của $d$ qua phép đối xứng tâm $I$.

Cách 1. Lấy điểm $M\left( {x;y} \right) \in d$ $\Rightarrow x + 2y + 3 = 0$ $\left( * \right).$

Gọi $M’\left( {x’;y’} \right) = {Đ_I}\left( M \right)$ thì 
$$
\left\{ \begin{array}{l}
x’ = 2 – x\\
y’ = 2 – y
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 2 – x’\\
y = 2 – y’
\end{array} \right.
$$

Thay vào $\left( * \right)$ ta được $\left( {2 – x’} \right) + 2\left( {2 – y’} \right) + 3 = 0$ $\Leftrightarrow x’ + 2y’ – 9 = 0.$

Vậy ảnh của $d$ là đường thẳng $d’:x+2y-9=0$.

Cách 2. Gọi $d’$ là ảnh của $d$ qua phép đối xứng tâm $I$, thì $d’$ song song hoặc trùng với $d$ nên phương trình $d’$ có dạng $x+2y+c=0$.

Lấy $N\left( -3;0 \right)\in d$, gọi $N’={{Đ}_{I}}\left( N \right)$ thì $N’\left( 5;2 \right)$.

Lại có $N’\in d’$ $\Rightarrow 5+2.2+c=0$ $\Leftrightarrow c=-9$.

Vậy $d’:x+2y-9=0$.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 2. Cho đường thẳng $d:x-2y+6=0$ và $d’:x-2y-10=0$. Tìm phép đối xứng tâm $I$ biến $d$ thành $d’$ và biến trục $Ox$ thành chính nó.

Tọa độ giao điểm của $d,d’$ với $Ox$ lần lượt là $A\left( -6;0 \right)$ và $B\left( 10;0 \right)$.

Do phép đối xứng tâm biến $d$ thành $d’$ và biến trục $Ox$ thành chính nó nên biến giao điểm $A$ của $d$ với $Ox$ thành giao điểm $A’$ của $d’$ với $Ox$, do đó tâm đối xứng là trung điểm của $AA’$.

Vậy tâm đối xứng là $I\left( 2;0 \right)$.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 3. Tìm tâm đối xứng của đường cong $\left( C \right)$ có phương trình $y={{x}^{3}}-3{{x}^{2}}+3$.

Lấy điểm $M\left( {x;y} \right) \in \left( C \right)$ $\Rightarrow y = {x^3} – 3{x^2} + 3$ $\left( 1 \right).$

Gọi $I\left( a;b \right)$ là tâm đối xứng của $\left( C \right)$ và $M’\left( x’;y’ \right)$ là ảnh của $M$ qua phép đối xứng tâm $I$.

Ta có: 
$$
\left\{ \begin{array}{l}
x’ = 2a – x\\
y’ = 2b – y
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 2a – x’\\
y = 2b – y’
\end{array} \right.
$$

Thay vào $\left( 1 \right)$ ta được $2b – y’$ $= {\left( {2a – x’} \right)^3} – 3{\left( {2a – x’} \right)^2} + 3$ $\Leftrightarrow y’ = {x’}^3 – 3{x’}^2 + 3 + (6 – 6a){x’}^2$ $+ \left( {12{a^2} – 12a} \right)x’ – 8{a^3} + 12{a^2} + 2b + 6$ $\left( 2 \right).$

Mặt khác $M’ \in \left( C \right)$ nên $y’ = {x’}^3 – 3{x’}^2 + 3$, do đó $\left( 2 \right)$ $\Leftrightarrow (6 – 6a){x’}^2 + \left( {12{a^2} – 12a} \right)x’$ $– 8{a^3} + 12{a^2} + 2b – 6{\rm{ }} = 0$, $\forall x’.$

$$
\Leftrightarrow \left\{ \begin{array}{l}
6 – 6a = 0\\
12{a^2} – 12a = 0\\
– 8{a^3} + 12{a^2} + 2b – 6 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = 1\\
b = 1
\end{array} \right.
$$

Vậy $I\left( 1;1 \right)$ là tâm đối xứng của $\left( C \right)$.

<!-- chunk:6 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Dạng toán 4. Sử dụng phép đối xứng tâm để giải các bài toán dựng hình
Phương pháp: Xem điểm cần dựng là giao của một đường có sẵn và ảnh của một đường khác qua phép quay ${{Đ}_{I}}$ nào đó.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 4. Cho hai đường thẳng ${{d}_{1}},{{d}_{2}}$ và hai điểm $A,G$ không thuộc ${{d}_{1}},{{d}_{2}}$. Hãy dựng tam giác $ABC$ có trọng tâm $G$ và hai đỉnh $B,C$ lần lượt thuộc ${{d}_{1}}$ và ${{d}_{2}}$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-tam-1.png" alt="cac-dang-toan-phep-doi-xung-tam-1">

Phân tích:

Giả sử đã dựng được tam giác $ABC$ thỏa mãn yêu cầu bài toán.

Gọi $I$ là trung điểm của $BC$ thì ${{Đ}_{I}}\left( C \right)=B$, mà $C\in {{d}_{2}}$ nên $B\in {{d}_{2}}’$ với ${{d}_{2}}’$ là ảnh của $d_2$ qua phép đối xứng tâm $I$.

Ta lại có $B\in {{d}_{1}}\Rightarrow B={{d}_{1}}\cap {{d}_{2}}’$.

Cách dựng:

+ Dựng điểm $I$ sao cho $\overrightarrow{AI}=\frac{3}{2}\overrightarrow{AG}.$

+ Dựng đường thẳng ${{d}_{2}}’$ ảnh của ${{d}_{2}}$ qua ${{Đ}_{I}}.$

+ Gọi $B={{d}_{1}}\cap {{d}_{2}}’.$

+ Dựng điểm $C={{Đ}_{I}}\left( B \right).$

Tam giác $ABC$ là tam giác phải dựng.

Chứng minh: Dựa vào cách dựng ta có $I$ là trung điểm của $BC$ và $\overrightarrow{AI}=\frac{3}{2}\overrightarrow{AG}$ nên $G$ là trọng tâm của tam giác $ABC$.

Nhận xét: Số nghiệm hình bằng số giao điểm của ${{d}_{1}}$ và ${{d}_{2}}’$.

[ads]

<!-- chunk:8 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 5. Cho hai đường tròn $\left( O \right)$ và $\left( O’ \right)$ cắt nhau tại hai điểm $A,B$ và số $a>0$. Dựng đường thẳng $d$ đi qua $A$ cắt hai đường tròn thành hai dây cung mà hiệu độ dài bằng $a$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-tam-2.png" alt="cac-dang-toan-phep-doi-xung-tam-2">

Phân tích:

Giả sử đã dựng được đường thẳng $d$ cắt $\left( O \right)$ và $\left( O’ \right)$ tại $M,M’$ sao cho $AM-AM’=a$.

Xét phép đối xứng ${Đ_A}.$

Gọi $N = {Đ_A}\left( M’ \right)$, $\left( {{O_1}} \right) = {Đ_A}\left( {\left( O’ \right)} \right)$, $H,K$ lần lượt là trung điểm của $AN$ và $AM$, khi đó $H{{O}_{1}}\bot AM$ và $OK\bot AM$.

Gọi $I$ là hình chiếu của $O$ trên ${{O}_{1}}H$, ta có: 
$$
\left\{ \begin{array}{l}
OI\parallel KH\\
OI = KH
\end{array} \right.
$$
, mặt khác $KH = KA – HA$ $= \frac{{AM – AN}}{2}$ $= \frac{{AM – AM’}}{2} = \frac{a}{2}$ nên $OI = \frac{a}{2}.$

Vậy điểm $I$ thuộc đường tròn tâm $O$ bán kính $r=\frac{a}{2}$.

Mặt khác $I$ thuộc đường tròn đường kính $O{{O}_{1}}$ nên $I$ là giao điểm của đường tròn đường kính $O{{O}_{1}}$ với đường tròn $\left( O;\frac{a}{2} \right)$ do đó $I$ xác định và $d$ là đường thẳng đi qua $A$ và song song với $OI$.

Cách dựng:

+ Dựng $\left( {{O}_{1}} \right)$ ảnh của $\left( O’ \right)$ qua ${{Đ}_{A}}$.

+ Dựng đường tròn đường kính $O{{O}_{1}}$.

+ Dựng đường tròn $\left( O;\frac{a}{2} \right)$, và dựng giao điểm $I$ của đường tròn đường kính $O{{O}_{1}}$ với đường tròn $\left( O;\frac{a}{2} \right)$.

+ Từ $A$ dựng đường thẳng $d\parallel OI$ cắt $\left( O \right)$ tại $M$ và cắt $\left( O’ \right)$ tại $M’$ thì $d$ là đường thẳng cần dựng.

Chứng minh:

Gọi $H,K$ lần lượt là trung điểm của $AN,AM$ ta có $KH=OI=\frac{a}{2}.$

Mà $KH=AK-AH$ $=\frac{AM}{2}-\frac{AN}{2}$ $=\frac{AM-AM’}{2}$ $\Rightarrow AM-AM’=a$.

Nhận xét: Số nghiệm hình bằng số giao điểm của đường tròn $\left( O;\frac{a}{2} \right)$ và đường tròn đường kính $O{{O}_{1}}$.

<!-- chunk:9 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 6. Cho tam giác $ABC$ và đường tròn $\left( O \right)$. Trên $AB$ lấy điểm $E$ sao cho $BE=2AE$, $F$ là trung điểm của $AC$ và $I$ là đỉnh thứ tư của hình bình hành $AEIF$. Với mỗi điểm $P$ trên đường tròn $\left( O \right)$, ta dựng điểm $Q$ sao cho $\overrightarrow{PA}+2\overrightarrow{PB}+3\overrightarrow{PC}=6\overrightarrow{IQ}$. Tìm tập hợp điểm $Q$ khi $P$ thay đổi trên $\left( O \right).$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-tam-3.png" alt="cac-dang-toan-phep-doi-xung-tam-3">

Gọi $K$ là điểm xác định bởi $\overrightarrow{KA}+2\overrightarrow{KB}+3\overrightarrow{KC}=\overrightarrow{0}$.

Khi đó: $\overrightarrow {KA} + 2\left( {\overrightarrow {KA} + \overrightarrow {AB} } \right)$ $+ 3\left( {\overrightarrow {KA} + \overrightarrow {AC} } \right) = \overrightarrow 0$ $\Leftrightarrow \overrightarrow {AK} = \frac{1}{3}\overrightarrow {AB} + \frac{1}{2}\overrightarrow {AC} .$

Mặt khác $AEIF$ là hình bình hành nên $\overrightarrow{AI}=\overrightarrow{AE}+\overrightarrow{AF}$ $=\frac{1}{3}\overrightarrow{AB}+\frac{1}{2}\overrightarrow{AC}$ nên $K\equiv I$.

Từ giả thiết suy ra $6\overrightarrow{PK}+\left( \overrightarrow{KA}+2\overrightarrow{KB}+3\overrightarrow{KC} \right)=6\overrightarrow{IQ}$ $\Leftrightarrow \overrightarrow{PK}=\overrightarrow{IQ}$, hay $\overrightarrow{PI}=\overrightarrow{IQ}$.

Vậy ${{Đ}_{I}}\left( P \right)=Q$ mà $P$ di động trên đường tròn $\left( O \right)$ nên $Q$ di động trên đường tròn $\left( O’ \right)$, ảnh của đường tròn $\left( O \right)$ qua phép đối xứng tâm $I$.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-tam.html -->
## Ví dụ 7. Cho đường tròn $\left( O \right)$ và dây cung $AB$ cố định, $M$ là một điểm di động trên $\left( O \right)$, $M$ không trùng với $A,B$. Hai đường tròn $\left( {{O}_{1}} \right),\left( {{O}_{2}} \right)$ cùng đi qua $M$ và tiếp xúc với $AB$ tại $A$ và $B$. Gọi $N$ là giao điểm thứ hai của $\left( {{O}_{1}} \right)$ và $\left( {{O}_{2}} \right)$. Tìm tập hợp điểm $N$ khi $M$ di động.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-tam-4.png" alt="cac-dang-toan-phep-doi-xung-tam-4">

Gọi $I=MN\cap AB$, ta có $I{{A}^{2}}=IM.IN.$

Tương tự $I{{B}^{2}}=IM.IN.$

Suy ra $IA=IB$ nên $I$ là trung điểm của $AB$.

Gọi $P$ là giao điểm thứ hai của $MN$ với đường tròn $\left( O \right)$.

Dễ thấy ${{P}_{I/\left( O \right)}}=-IM.IP$ $=-IA.IB=-I{{A}^{2}}.$

Do đó $-IM.IN=-IM.IP$ $\Rightarrow IN=IP$ vậy $I$ là trung điểm của $NP$ do đó ${{Đ}_{I}}\left( P \right)=N$, mà $P$ di động trên đường tròn $\left( O \right)$ nên $N$ di động trên đường tròn $\left( O’ \right)$ ảnh của đường tròn $\left( O \right)$ qua phép đối xứng tâm $I$.

Vậy tập hợp điểm $N$ là đường tròn $\left( O’ \right)$ ảnh của đường tròn $\left( O \right)$ qua phép đối xứng tâm $I$.