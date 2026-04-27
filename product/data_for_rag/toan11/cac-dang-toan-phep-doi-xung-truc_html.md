# Các dạng toán phép đối xứng trục

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
Bài viết trình bày lý thuyết và phương pháp giải các dạng toán phép đối xứng trục trong chương trình Hình học 11 chương 1. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu phép dời hình và phép đồng dạng trong mặt phẳng được chia sẻ trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## A. KIẾN THỨC CẦN NẮM
1. Định nghĩa phép đối xứng trục:
• Cho đường thẳng $d$. Phép biến hình biến mỗi điểm $M$ thuộc $d$ thành chính nó, biến mỗi điểm $M$ không thuộc $d$ thành điểm $M’$ sao cho $d$ là đường trung trực của đoạn thẳng $MM’$ được gọi là phép đối xứng qua đường thẳng $d$, hay còn gọi là phép đối xứng trục $d$, ký hiệu ${Đ_d}.$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-1.png" alt="cac-dang-toan-phep-doi-xung-truc-1">

• ${Đ_d}\left( M \right) = M’$ $\Leftrightarrow \overrightarrow {IM} = – \overrightarrow {IM’} .$

• Nếu ${Đ_d}\left[ {\left( H \right)} \right] = \left( H \right)$ thì $d$ được gọi là trục đối xứng của hình $\left( H \right)$.

2. Biểu thức tọa độ của phép đối xứng trục:

Trong mặt phẳng $Oxy$ với mỗi điểm $M\left( {x;y} \right)$, gọi $M’\left( {x’;y’} \right) = {Đ_d}\left( M \right).$

• Nếu $d$ là trục $Ox$ thì 
$$
\left\{ \begin{array}{l}
x’ = x\\
y’ = – y
\end{array} \right.
$$

• Nếu $d$ là trục $Oy$ thì 
$$
\left\{ \begin{array}{l}
x’ = – x\\
y’ = y
\end{array} \right.
$$

3. Tính chất phép đối xứng trục:

• Bảo toàn khoảng cách giữa hai điểm bất kì.

• Biến một đường thẳng thành đường thẳng.

• Biến một đoạn thẳng thành đoạn thẳng bằng đoạn thẳng đã cho.

• Biến một tam giác thành tam giác bằng tam giác đã cho.

• Biến đường tròn thành đường tròn có cùng bán kính.

<!-- chunk:2 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Dạng toán 1. Xác định ảnh của một hình qua phép đối xứng trục
Phương pháp: Để xác định ảnh $\left( H’ \right)$ của hình $\left( H \right)$ qua phép đối xứng trục ta có thể dùng một trong các cách sau:

• Dùng định nghĩa phép đối xứng trục.

• Dùng biểu thức tọa độ của phép đối xứng trục mà trục đối xứng là các trục tọa độ $Ox$, $Oy.$

• Dùng biểu thức vectơ của phép đối xứng trục.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 1. Trong mặt phẳng $Oxy$, cho điểm $M\left( {1;5} \right)$, đường thẳng $d:x + 2y + 4 = 0$ và đường tròn $\left( C \right):{x^2} + {y^2} + 2x – 4y – 4 = 0.$

a. Tìm ảnh của $M$, $d$ và $\left( C \right)$ qua  phép đối xứng trục $Ox.$

b. Tìm ảnh của $M$ qua phép đối xứng qua đường thẳng $d.$

a. Gọi $M’$, $d’$, $\left( {C’} \right)$ theo thứ tự là ảnh của $M$, $d$, $\left( C \right)$ qua phép đối xứng trục ${Đ_{Ox}}.$

• Áp dụng biểu thức tọa độ của phép đối xứng trục $Ox$, suy ra: $M’\left( {1; – 5} \right).$

• Tìm ảnh của đường thẳng $d$:

Lấy $N\left( {x;y} \right) \in d$ $\Rightarrow x + 2y + 4 = 0$ $(1).$

Gọi $N’\left( {x’;y’} \right)$ là ảnh của $N$ qua phép đối xứng ${Đ_{Ox}}.$

Ta có: 
$$
\left\{ \begin{array}{l}
x’ = x\\
y’ = – y
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = x’\\
y = – y’
\end{array} \right.
$$

Thay vào $\left( 1 \right)$ ta được: $x’ – 2y’ + 4 = 0.$

Vậy $d’:x – 2y + 4 = 0.$

• Tìm ảnh của đường tròn $\left( C \right):$

Cách 1:

Đường tròn $\left( C \right)$ có tâm $I\left( { – 1;2} \right)$ và bán kính $R = 3.$

Gọi $I’,R’$ là tâm và bán kính của $\left( {C’} \right)$ thì $I’\left( { – 1; – 2} \right)$ và $R’ = R = 3$.

Do đó $\left( {C’} \right): {\left( {x + 1} \right)^2} + {\left( {y + 2} \right)^2} = 9.$

Cách 2:

Lấy $P\left( {x;y} \right) \in \left( C \right)$ $\Rightarrow {x^2} + {y^2} + 2x – 4y – 4 = 0$ $\left( 2 \right).$

Gọi $P’\left( {x’;y’} \right)$ là ảnh của $P$ qua phép đối xứng ${Đ_{Ox}}.$

Ta có: 
$$
\left\{ \begin{array}{l}
x’ = x\\
y’ = – y
\end{array} \right.
$$
 
$$
\Rightarrow \left\{ \begin{array}{l}
x = x’\\
y = – y’
\end{array} \right.
$$

Thay vào $\left( 2 \right)$, ta được: $x{‘^2} + y{‘^2} + 2x’ + 4y’ – 4 = 0.$

Vậy $\left( {C’} \right):{x^2} + {y^2} + 2x + 4y – 4 = 0.$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-2.png" alt="cac-dang-toan-phep-doi-xung-truc-2">

b. Đường thẳng ${d_1}$ đi qua $M$ vuông góc với $d$ có phương trình $2x – y + 3 = 0.$

Gọi $I = d \cap {d_1}$ thì tọa độ điểm $I$ là nghiệm của hệ phương trình 
$$
\left\{ \begin{array}{l}
x + 2y + 4 = 0\\
2x – y + 3 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = – 2\\
y = – 1
\end{array} \right.
$$
 $\Rightarrow I\left( { – 2; – 1} \right).$

Gọi $M’$ đối xứng với $M$ qua $d$ thì $I$ là trung điểm của $MM’$.

Ta có 
$$
\left\{ \begin{array}{l}
{x_I} = \frac{{{x_M} + {x_{M’}}}}{2}\\
{y_I} = \frac{{{y_M} + {y_{M’}}}}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
{x_{M’}} = 2{x_I} – {x_M} = – 5\\
{y_{M’}} = 2{y_I} – {y_M} = – 7
\end{array} \right.
$$
 $\Rightarrow M’\left( { – 5; – 7} \right).$

Vậy ảnh của $M$ qua phép đối xứng đường thẳng $d$ là điểm $M’\left( { – 5; – 7} \right).$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 2. Cho hai đường thẳng $d:x + y – 2 = 0$, ${d_1}:x + 2y – 3 = 0$ và đường tròn $\left( C \right):{\left( {x – 1} \right)^2} + {\left( {y + 1} \right)^2} = 4.$ Tìm ảnh của ${d_1}$, $\left( C \right)$ qua phép đối xứng trục $d.$

• Tìm ảnh của ${d_1}:$

Ta có: ${d_1} \cap d = I\left( {1;1} \right)$ nên ${Đ_d}\left( I \right) = I.$

Lấy $M\left( {3;0} \right) \in {d_1}$.

Đường thẳng ${d_2}$ đi qua $M$ vuông góc với $d$ có phương trình $x – y – 3 = 0.$

Gọi ${M_0} = d \cap {d_2}$, thì tọa độ của ${M_0}$ là nghiệm của hệ 
$$
\left\{ \begin{array}{l}
x + y – 2 = 0\\
x – y – 3 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = \frac{5}{2}\\
y = – \frac{1}{2}
\end{array} \right.
$$
 $\Rightarrow {M_0}\left( {\frac{5}{2}; – \frac{1}{2}} \right).$

Gọi $M’$ là ảnh của $M$ qua ${Đ_d}$ thì ${M_0}$ là trung điểm của $MM’$ nên $M’\left( {2; – 1} \right).$

Gọi ${d_1}’ = {Đ_d}\left( {{d_1}} \right)$ thì ${d_1}’$ đi qua $I$ và $M’$ nên có phương trình $\frac{{x – 1}}{1} = \frac{{y – 1}}{{ – 2}}$ $\Leftrightarrow 2x + y – 3 = 0.$

Vậy ${d_1}’:2x + y – 3 = 0.$

• Tìm ảnh của $\left( C \right):$

Đường tròn $\left( C \right)$ có tâm $J\left( {1; – 1} \right)$ và bán kính $R = 2.$

Đường thẳng ${d_3}$ đi qua $J$ và vuông góc với $d$ có phương trình $x – y – 2 = 0.$

Gọi ${J_0} = {d_3} \cap d$ thì tọa độ của điểm ${J_0}$ là nghiệm của hệ:

$$
\left\{ \begin{array}{l}
x + y – 2 = 0\\
x – y – 2 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 2\\
y = 0
\end{array} \right.
$$
 $\Rightarrow {J_0}\left( {2;0} \right).$

Gọi $J’ = {Đ_d}\left( J \right)$ thì ${J_0}$ là trung điểm của $JJ’$ nên $J’\left( {3;1} \right).$

Gọi $\left( {C’} \right) = {Đ_d}\left( {\left( C \right)} \right)$ thì $J’$ là tâm của $\left( {C’} \right)$ và bán kính của $\left( {C’} \right)$ là $R’ = R = 2.$

Vậy $\left( {C’} \right):{\left( {x – 3} \right)^2} + {\left( {y – 1} \right)^2} = 4.$

[ads]

<!-- chunk:5 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Dạng toán 2. Dùng phép đối xứng trục để giải các bài toán dựng hình
Phương pháp: Để dựng một điểm $M$ ta tìm cách xác định nó như là ảnh của một điểm đã biết qua một phép đối xứng trục, hoặc xem $M$ như là giao điểm của một đường cố định và một với ảnh của một đường đã biết qua phép đối xứng trục.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 3. Dựng hình vuông $ABCD$ biết hai đỉnh $A$ và $C$ nằm trên đường thẳng ${{d}_{1}}$ và hai đỉnh $B, D$ lần lượt thuộc hai đường thẳng ${{d}_{2}},{{d}_{3}}$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-3.png" alt="cac-dang-toan-phep-doi-xung-truc-3">

Phân tích:

Giả sử đã dựng được hình vuông $ABCD$ thỏa điều kiện của bài toán.

Do $A,C \in {d_1}$ và $AC$ là trục đối xứng của hình vuông $ABCD$, mặc khác $B \in {d_2}$ nên $D \in {d_2}’$, trong đó ${d_2}’$ là đường thẳng đối xứng với ${d_2}$ qua ${d_1}.$ Suy ra: $D = {d_2}’ \cap {d_3}.$

Hai điểm $B,D$ đối xứng qua đường thẳng ${d_1}$ nên ${Đ_{{d_1}}}\left( D \right) = B.$

Cách dựng:

+ Dựng ${d_2}’ = {Đ_{{d_1}}}\left( {{d_2}} \right)$, gọi $D = {d_3} \cap {d_2}’.$

+ Dựng đường thẳng qua $D$ vuông góc với ${d_1}$ tại $O$ và cắt ${d_2}$ tại $B.$

+ Dựng  đường tròn tâm $O$ đường kính $BD$ cắt ${d_1}$ tại $A,C$ ($A,C$ theo thứ tự để tạo thành tứ giác $ABCD$).

Chứng minh: Từ cách dựng suy ra $ABCD$ là hình vuông.

Nhận xét:

Trường hợp 1: ${d_2}$ cắt ${d_3}$, khi đó:

+ Nếu ${d_2}’ \cap {d_3}$ thì bài toán có một nghiệm hình.

+ Nếu ${d_2}’\parallel {d_3}$ thì bài toán vô nghiệm hình.

Trường hợp 2: ${d_2}\parallel {d_3}$, khi đó:

+ Nếu ${{d}_{1}}$ song song và cách đều ${{d}_{2}}$ và ${{d}_{3}}$ thì bài toán có vô số nghiệm hình.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-4.png" alt="cac-dang-toan-phep-doi-xung-truc-4">

+ Nếu ${{d}_{1}}$ hợp với ${{d}_{2}},{{d}_{3}}$ một góc $45{}^\circ$ thì bài toán có một nghiệm hình.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-5.png" alt="cac-dang-toan-phep-doi-xung-truc-5">

+ Nếu ${{d}_{1}}$ song song và không cách đều ${{d}_{2}},{{d}_{3}}$ hoặc ${{d}_{1}}$ không hợp ${{d}_{2}},{{d}_{3}}$ một góc $45{}^\circ$ thì ví dụ đã cho vô nghiệm hình.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 4. Cho hai đường tròn $\left( C \right),\left( C’ \right)$ có bán kính khác nhau và đường thẳng $d$. Hãy dựng hình vuông $ABCD$ có hai đỉnh $A,C$ lần lượt nằm trên $\left( C \right),\left( C’ \right)$ và hai đỉnh còn lại nằm trên $d$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-6.png" alt="cac-dang-toan-phep-doi-xung-truc-6">

Phân tích:

Giả sử đã dựng được hình vuông $ABCD$.

Ta thấy hai đỉnh $B,D \in d$ nên hình vuông hoàn toàn xác định khi biết $C$.

Ta có $A,C$ đối xứng qua $d$ nên $C$ thuộc đường tròn $\left( {{C_1}} \right)$ là ảnh của đường tròn $\left( C \right)$ qua ${Đ_d}.$

Mặt khác $C \in \left( {C’} \right)$ $\Rightarrow C \in \left( {{C_1}} \right) \cap \left( {C’} \right).$

Cách dựng:

+ Dựng đường tròn $\left( {{C_1}} \right)$ là ảnh của $\left( C \right)$ qua ${Đ_d}.$

+ Gọi $C$ là giao điểm của $\left( {{C_1}} \right)$ và $\left( {C’} \right).$

+ Dựng điểm $A$ đối xứng với $C$ qua $d.$

+ Gọi $I = AC \cap d.$ Lấy trên $d$ hai điểm $BD$ sao cho $IB = ID = IA.$

Khi đó $ABCD$ là hình vuông cần dựng.

Chứng minh:

Dễ thấy $ABCD$ là hình vuông có $B,D \in d$, $C \in \left( {C’} \right).$

Mặt khác $A,C$ đối xứng qua $d$ mà $C \in \left( {C’} \right)$ $\Rightarrow A \in {Đ_d}\left[ {\left( {C’} \right)} \right] = \left( C \right)$ hay $A$ thuộc $\left( C \right).$

Nhận xét: Số nghiệm hình bằng số giao điểm của $\left( {{C}_{1}} \right)$ và $\left( C’ \right)$.

<!-- chunk:8 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Dạng toán 3. Dùng phép đối xứng trục để giải các bài tập hợp điểm
Phương pháp: Nếu $M’ = {Đ_d}\left( M \right)$ với $M$ di động trên hình $\left( H \right)$ thì $M’$ di động trên hình $\left( H’ \right)$ là ảnh của hình $\left( H \right)$ qua phép đối xứng trục $d$.

<!-- chunk:9 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 5. Trên đường tròn $\left( O,R \right)$ cho hai điểm cố định $A,B$. Đường tròn $\left( O’;R’ \right)$ tiếp xúc ngoài với $\left( O \right)$ tại $A$. Một điểm $M$ di động trên $\left( O \right)$. $MA$ cắt $\left( O’ \right)$ tại điểm thứ hai $A’$. Qua $A’$ kẻ đường thẳng song song với $AB$ cắt $MB$ tại $B’$. Tìm quỹ tích điểm $B’.$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-7.png" alt="cac-dang-toan-phep-doi-xung-truc-7">

Gọi $C = A’B’ \cap \left( {O’} \right).$ Vẽ tiếp tuyến chung của $\left( O \right)$ và $\left( {O’} \right)$ tại điểm $A.$

Ta có: $\widehat {A’CA} = \widehat {xAM}$ $= \widehat {ABM} = \widehat {BB’A’}$ do đó $ABB’C$ là hình thang cân.

Gọi $d$ là trục đối xứng của hình thang này thì ${Đ_d}\left( C \right) = B’$ mà $C$ di động trên đường tròn $\left( {O’} \right)$ nên $B’$ di động trên đường tròn $\left( {O”} \right)$ là ảnh của $\left( {O’} \right)$ qua ${Đ_d}.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-doi-xung-truc.html -->
## Ví dụ 6. Cho tam giác $ABC$ có tâm đường tròn nội tiếp $I$, $P$ là một điểm nằm trong tam giác. Gọi $A’,B’,C’$ là các điểm đối xứng với $P$ lần lượt đối xứng qua $IA,IB,IC$. Chứng minh các đường thẳng $AA’,BB’,CC’$ đồng quy.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-doi-xung-truc-8.png" alt="cac-dang-toan-phep-doi-xung-truc-8">

Giả sử điểm $P$ nằm trong tam giác $IAB$. Gọi ${{P}_{1}},{{P}_{2}},{{P}_{3}}$ lần lượt đối xứng với $P$ qua các cạnh $BC,CA,AB$. Ta sẽ chứng minh $AA’,BB’,CC’$ đồng quy tại tâm đường tròn ngoại tiếp tam giác ${{P}_{1}}{{P}_{2}}{{P}_{3}}$.

Hiển nhiên ta có $A{{P}_{2}}=A{{P}_{3}}$ vậy để chứng minh $AA’$ là trung trực của ${{P}_{2}}{{P}_{3}}$ ta cần chứng minh $\widehat{{{P}_{2}}AA’}=\widehat{{{P}_{3}}AA’}$.

Ta có: $\widehat {{P_3}AA’}$ $= \widehat {{P_3}AP} + \widehat {PAA’}$ $= 2\alpha + 2\beta .$

Tương tự $\widehat {{P_2}AA’}$ $= \widehat {{P_2}AC} + \widehat {CAA’}$ $= \widehat {CAP} + \widehat {CAA’}$ $= 2\alpha + 2\beta .$

Vậy $\widehat {{P_2}AA’} = \widehat {{P_3}AA’}$ nên $AA’$ là trung trực của ${P_2}{P_3}.$

Tương tự $BB’,CC’$ lần lượt là trung trực của ${{P}_{1}}{{P}_{3}}$ và ${{P}_{1}}{{P}_{2}}$ nên chúng đồng quy tại tâm đường tròn ngoại tiếp tam giác ${{P}_{1}}{{P}_{2}}{{P}_{3}}$.