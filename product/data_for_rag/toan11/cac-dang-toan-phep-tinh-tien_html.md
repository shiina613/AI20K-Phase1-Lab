# Các dạng toán phép tịnh tiến

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
Bài viết trình bày lý thuyết và các dạng toán phép tịnh tiến trong chương trình Hình học 11 chương 1. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu phép dời hình và phép đồng dạng trong mặt phẳng được chia sẻ trên TOANMATH.com.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## A. KIẾN THỨC CẦN NẮM

1. Định nghĩa phép tịnh tiến

• Trong mặt phẳng cho vectơ $\overrightarrow v$. Phép biến hình biến mỗi điểm $M$ thành điểm $M’$ sao cho $\overrightarrow {MM’} = \overrightarrow v$ được gọi là phép tịnh tiến theo vectơ $\overrightarrow v$, ký hiệu ${T_{\overrightarrow v }}.$

• ${T_{\overrightarrow v }}\left( M \right) = M’$ $\Leftrightarrow \overrightarrow {MM’} = \overrightarrow v .$

2. Biểu thức tọa độ của phép tịnh tiến:Trong mặt phẳng tọa độ $Oxy$, cho điểm $M\left( {x;y} \right)$ và $\overrightarrow v = \left( {a;b} \right).$ Khi đó: $M’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( M \right)$ $\Leftrightarrow \overrightarrow {MM’} = \overrightarrow v$ 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x’ – x = a\\
y’ – y = b
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x’ = x + a\\
y’ = y + b
\end{array} \right.
$$

3. Các tính chất của phép tịnh tiến
• Phép tịnh tiến bảo toàn khoảng cách giữa hai điểm bất kỳ.

• Phép tịnh tiến biến đường thẳng thành đường thẳng song song hoặc trùng với đường thẳng đã cho.

• Phép tịnh tiến biến đoạn thẳng thành đoạn thẳng bằng đoạn thẳng đã cho.

• Phép tịnh tiến biến tam giác thành tam giác bằng tam giác đã cho.

• Phép tịnh tiến biến đường tròn thành đường tròn có cùng bán kính.

## B. CÁC DẠNG TOÁN PHÉP TỊNH TIẾN

**Dạng toán 1. Xác định ảnh của một hình qua phép tịnh tiến**

**Phương pháp**: Sử dụng định nghĩa và các tính chất hoặc biểu thức tọa độ của phép tịnh tiến.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 1. Cho tam giác $ABC$, dựng ảnh của tam giác $ABC$ qua phép tịnh tiến theo vectơ $\overrightarrow {BC} .$

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-tinh-tien-1.png" alt="cac-dang-toan-phep-tinh-tien-1">

Ta có: ${T_{\overrightarrow {BC} }}\left( B \right) = C.$

Để tìm ảnh của điểm $A$, ta dựng hình bình hành $ABCD.$

Do $\overrightarrow {AD} = \overrightarrow {BC}$ nên ${T_{\overrightarrow {BC} }}\left( A \right) = D.$

Gọi $E$ là điểm đối xứng với $B$ qua $C$, khi đó: $\overrightarrow {CE} = \overrightarrow {BC} .$

Suy ra ${T_{\overrightarrow {BC} }}\left( C \right) = E.$

Vậy ảnh của tam giác $ABC$ là tam giác $DCE$.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 2. Trong mặt phẳng tọa độ $Oxy$ , cho $\overrightarrow{v}=\left( -2;3 \right)$. Hãy tìm ảnh của điểm $A\left( 1;-1 \right)$ qua phép tịnh tiến theo vectơ $\overrightarrow{v}$.

Gọi $A’\left( {x’;y’} \right)$ là ảnh của điểm $A$ qua phép tịnh tiến theo vectơ $\overrightarrow{v}$.

Áp dụng biểu thức tọa độ của phép tịnh tiến 
$$
\left\{ \begin{array}{l}
x’ = x + a\\
y’ = y + b
\end{array} \right.
$$

Ta có: $A’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( A \right)$ 
$$
\Rightarrow \left\{ \begin{array}{l}
x’ = 1 + ( – 2)\\
y’ = – 1 + 3
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x’ = – 1\\
y’ = 2
\end{array} \right.
$$
 $\Rightarrow A’\left( { – 1;2} \right).$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 3. Trong mặt phẳng tọa độ $Oxy$, cho $\overrightarrow v = \left( {1; – 3} \right)$ và đường thẳng $d$ có phương trình $2x – 3y + 5 = 0.$ Viết phương trình đường thẳng $d’$ là ảnh của $d$ qua phép tịnh tiến ${T_{\overrightarrow v }}.$

Cách 1.

Lấy điểm $M\left( {x;y} \right)$ tùy ý thuộc $d$, ta có: $2x – 3y + 5 = 0$ $\left( * \right).$

Gọi $M’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( M \right)$ 
$$
\Rightarrow \left\{ \begin{array}{l}
x’ = x + 1\\
y’ = y – 3
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = x’ – 1\\
y = y’ + 3
\end{array} \right.
$$

Thay vào $(*)$ ta được phương trình $2\left( {x’ – 1} \right) – 3\left( {y’ + 3} \right) + 5 = 0$ $\Leftrightarrow 2x’ – 3y’ – 6 = 0.$

Vậy ảnh của $d$ là đường thẳng $d’:2x – 3y – 6 = 0.$

Cách 2.

Do $d’ = {T_{\overrightarrow v }}\left( d \right)$ nên $d’$ song song hoặc trùng với $d$, vì vậy phương trình đường thẳng $d’$ có dạng $2x – 3y + c = 0.$

Lấy điểm $M\left( { – 1;1} \right) \in d.$ Khi đó $M’ = {T_{\overrightarrow v }}\left( M \right)$ $= \left( { – 1 + 1;1 – 3} \right) = \left( {0; – 2} \right).$

Do $M’ \in d’$ $\Rightarrow 2.0 – 3.\left( { – 2} \right) + c = 0$ $\Leftrightarrow c = – 6.$

Vậy ảnh của $d$ là đường thẳng: $d’:2x – 3y – 6 = 0.$

Cách 3.

Lấy $M\left( { – 1;1} \right)$, $N\left( {2;3} \right)$ thuộc $d$, ảnh của $M$, $N$ qua phép tịnh tiến ${T_{\overrightarrow v }}$ tương ứng là $M’\left( {0; – 2} \right)$, $N’\left( {3;0} \right).$

Vì $d’$ đi qua hai điểm $M’, N’$ nên $d’$ có phương trình $\frac{{x – 0}}{3} = \frac{{y + 2}}{2}$ $\Leftrightarrow 2x – 3y – 6 = 0.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 4. Trong mặt phẳng tọa độ $Oxy$, cho đường tròn $\left( C \right)$ có phương trình ${x^2} + {y^2} + 2x – 4y – 4 = 0.$ Tìm ảnh của $\left( C \right)$ qua phép tịnh tiến theo vectơ $\overrightarrow v = \left( {2; – 3} \right).$

Cách 1.

Lấy điểm $M\left( {x;y} \right)$ tùy ý thuộc đường tròn $\left( C \right)$, ta có: ${x^2} + {y^2} + 2x – 4y – 4 = 0$ $\left( * \right).$

Gọi $M’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( M \right)$ 
$$
\Rightarrow \left\{ \begin{array}{l}
x’ = x + 2\\
y’ = y – 3
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = x’ – 2\\
y = y’ + 3
\end{array} \right.
$$

Thay vào phương trình $(*)$ ta được: ${\left( {x’ – 2} \right)^2} + {\left( {y’ + 3} \right)^2}$ $+ 2\left( {x’ – 2} \right) – 4\left( {y’ + 3} \right) – 4 = 0$ $\Leftrightarrow x{‘^2} + y{‘^2} – 2x’ + 2y’ – 7 = 0.$

Vậy ảnh của $\left( C \right)$ là đường tròn $\left( {C’} \right)$: ${x^2} + {y^2} – 2x + 2y – 7 = 0.$

Cách 2.

Ta có: $\left( C \right)$ có tâm $I\left( { – 1;2} \right)$ và bán kính $r = 3.$

Gọi $\left( {C’} \right) = {T_{\overrightarrow v }}\left( {\left( C \right)} \right)$ và $I’\left( {x’;y’} \right)$, $r’$ là tâm và bán kính của $(C’).$

Ta có: 
$$
\left\{ \begin{array}{l}
x’ = – 1 + 2 = 1\\
y’ = 2 – 3 = – 1
\end{array} \right.
$$
 $\Rightarrow I’\left( {1; – 1} \right)$ và $r’ = r = 3$ nên phương trình của đường tròn $\left( {C’} \right)$ là: ${\left( {x – 1} \right)^2} + {\left( {y + 1} \right)^2} = 9.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Dạng toán 2. Xác định phép tịnh tiến khi biết ảnh và tạo ảnh
Phương pháp: Xác định phép tịnh tiến tức là tìm tọa độ của $\overrightarrow{v}$. Để tìm tọa độ của $\overrightarrow{v}$ ta có thể giả sử $\overrightarrow{v}=\left( a;b \right)$, sử dụng các dữ kiện trong giả thiết của bài toán để thiết lập hệ phương trình hai ẩn $a,b$ và giải hệ tìm $a,b$.

[ads]

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 5. Trong mặt phẳng tọa độ $Oxy$, cho đường thẳng $d:3x+y-9=0$. Tìm phép tịnh tiến theo vectơ $\overrightarrow{v}$ có giá song song với $Oy$ biến $d$ thành $d’$ đi qua điểm $A\left( 1;1 \right)$.

Vì $\overrightarrow v$ có giá song song với $Oy$ nên $\overrightarrow v = \left( {0;k} \right)$ $\left( {k \ne 0} \right).$

Lấy $M\left( {x;y} \right) \in d$ $\Rightarrow 3x + y – 9 = 0$ $\left( * \right).$

Gọi $M’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( M \right)$ 
$$
\Rightarrow \left\{ \begin{array}{l}
x’ = x\\
y’ = y + k
\end{array} \right.
$$

Thay vào $\left( * \right)$, ta được: $3x’ + y’ – k – 9 = 0.$

Do đó: ${T_{\overrightarrow v }}\left( d \right) = d’:$ $3x + y – k – 9 = 0.$

Mà: $A\left( {1;1} \right)$ thuộc $d$, suy ra: $k = – 5.$

Vậy $\overrightarrow v = \left( {0; – 5} \right).$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 6. Trong mặt phẳng tọa độ $Oxy$, cho hai đường thẳng $d:2x – 3y + 3 = 0$ và $d’:2x – 3y – 5 = 0.$ Tìm tọa độ $\overrightarrow v$ có phương vuông góc với $d$ để ${T_{\overrightarrow v }}\left( d \right) = d’.$

Đặt $\overrightarrow v = \left( {a;b} \right).$

Lấy điểm $M\left( {x;y} \right)$ tùy ý thuộc $d$, ta có: $d:2x – 3y + 3 = 0$ $\left( * \right).$

Gọi $M’\left( {x’;y’} \right) = {T_{\overrightarrow v }}\left( M \right).$ Ta có 
$$
\left\{ \begin{array}{l}
x’ = x + a\\
y’ = y + b
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = x’ – a\\
y = y’ – b
\end{array} \right.
$$
, thay vào $(*)$ ta được phương trình: $2x’ – 3y’ – 2a + 3b + 3 = 0.$

Từ giả thiết suy ra $– 2a + 3b + 3 = – 5$ $\Leftrightarrow 2a – 3b = – 8.$

Vectơ pháp tuyến của đường thẳng $d$ là $\overrightarrow n = \left( {2; – 3} \right)$, suy ra vectơ chỉ phương của $d$ là $\overrightarrow u = \left( {3;2} \right).$

Do $\overrightarrow v \bot \overrightarrow u$ $\Rightarrow \overrightarrow v .\overrightarrow u = 3a + 2b = 0.$

Ta có hệ phương trình 
$$
\left\{ \begin{array}{l}
2a – 3b = – 8\\
3a + 2b = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
a = – \frac{{16}}{{13}}\\
b = \frac{{24}}{{13}}
\end{array} \right.
$$

Vậy $\overrightarrow v = \left( { – \frac{{16}}{{13}};\frac{{24}}{{13}}} \right).$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Dạng toán 3. Dùng phép tịnh tiến để giải các bài toán dựng hình
Phương pháp:

• Để dựng một điểm $M$ ta tìm cách xem nó là ảnh của một điểm đã biết qua một phép tịnh tiến, hoặc xem $M$ là giao điểm của hai đường trong đó một đường cố định còn một đường là ảnh của một đường đã biết qua phép tịnh tiến.

• Sử dụng kết quả: Nếu ${T_{\overrightarrow v }}\left( N \right) = M$ và $N \in \left( H \right)$ thì $M \in \left( {H’} \right)$, trong đó $\left( {H’} \right) = {T_{\overrightarrow v }}\left( {\left( H \right)} \right)$ và kết hợp với $M$ thuộc hình $\left( K \right)$ (theo giả thiết) để suy ra $M \in \left( {H’} \right) \cap \left( K \right).$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 7. Cho đường tròn tâm $O$, bán kính $R$ và hai điểm phân biệt $C,D$ nằm ngoài $\left( O \right)$. Hãy dựng dây cung $AB$ của đường tròn $\left( O \right)$ sao cho $ABCD$ là hình bình hành.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-tinh-tien-2.png" alt="cac-dang-toan-phep-tinh-tien-2">

Phân tích: Giả sử đã dựng được dây cung $AB$ thỏa mãn yêu cầu bài toán.

Do $ABCD$ là hình bình hành nên $\overrightarrow {AB} = \overrightarrow {DC}$ $\Rightarrow {T_{\overrightarrow {CD} }}\left( A \right) = B.$

Nhưng $A \in \left( O \right)$ $\Rightarrow B \in \left( {O’} \right) = {T_{\overrightarrow {DC} }}\left( {\left( O \right)} \right).$ Vậy $B$ vừa thuộc $\left( O \right)$ và $\left( {O’} \right)$ nên $B$ chính là giao điểm của $\left( O \right)$ và $\left( {O’} \right).$

Cách dựng:

+ Dựng đường tròn $\left( {O’} \right)$ là ảnh của đường tròn $\left( O \right)$ qua ${T_{\overrightarrow {DC} }}.$

+ Dựng giao điểm $B$ của $\left( O \right)$ và $\left( {O’} \right).$

+ Dựng đường thẳng qua $B$ và song song với $CD$ cắt $\left( O \right)$ tại $A.$

Dây cung $AB$ là dây cung thỏa yêu cầu bài toán.

Chứng minh: Từ cách dựng ta có ${T_{\overrightarrow {DC} }}\left( A \right) = B$ $\Rightarrow \overrightarrow {AB} = \overrightarrow {DC}$ $\Rightarrow ABCD$ là hình bình hành.

Nhận xét:

+ Nếu $CD>2R$ thì bài toán vô nghiệm .

+ Nếu $CD=2R$ thì có một nghiệm .

+ Nếu $CD<2R$ thì có hai nghiệm.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 8. Cho tam giác $ABC$. Dựng đường thẳng $d$ song song với $BC$, cắt hai cạnh $AB, AC$ lần lượt tại $M, N$ sao cho $AM=CN$.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-tinh-tien-3.png" alt="cac-dang-toan-phep-tinh-tien-3">

Phân tích: Giả sử đã dựng được đường thẳng $d$ thỏa mãn bài toán. Từ $M$ dựng đường thẳng song song với $AC$ cắt $BC$ tại $P$, khi đó $MNCP$ là hình bình hành nên $CN=PM$. Ta lại có $AM=CN$ suy ra $MP=MA$, từ đó ta có $AP$ là phân giác trong của góc $A.$

Cách dựng:

+ Dựng phân giác trong $AP$ của góc $A.$

+ Dựng đường thẳng đi qua $P$ song song với $AC$ cắt $AB$ tại $M.$

+ Dựng ảnh $N={{T}_{\overrightarrow{PM}}}\left( C \right)$.

Đường thẳng $MN$ chính là đường thẳng thỏa yêu cầu bài toán.

Chứng minh: Từ cách dựng ta có $MNCP$ là hình bình hành, suy ra $MN\parallel BC$ và $CN = PM$, ta có $\widehat {MAP}{\rm{ = }}\widehat {CAP} = \widehat {APM}$ $\Rightarrow \Delta MAP$ cân tại $M$ $\Rightarrow AM = MP.$ Vậy $AM = CN.$

Nhận xét: Bài toán có một nghiệm hình.

<!-- chunk:12 level:2 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Dạng toán 4. Sử dụng phép tịnh tiến để giải các bài toán tìm tập hợp điểm
Phương pháp: Nếu ${{T}_{\overrightarrow{v}}}\left( M \right)=M’$ và đểm $M$ di động trên hình $\left( H \right)$ thì điểm $M’$ thuộc hình $\left( H’ \right)$, trong đó $\left( H’ \right)$ là ảnh của hình $\left( H \right)$ qua ${{T}_{\overrightarrow{v}}}$.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 9. Cho hai điểm phân biệt $B,C$ cố định trên đường tròn $\left( O \right)$tâm $O$. Điểm $A$ di động trên $\left( O \right)$. Chứng minh khi $A$ di động trên $\left( O \right)$ thì trực tâm của tam giác $ABC$ di động trên một đường tròn.

<img link="data_for_rag/toan11/images/cac-dang-toan-phep-tinh-tien-4.png" alt="cac-dang-toan-phep-tinh-tien-4">

Gọi $H$ là trực tâm của tam giác $ABC$ và $M$ là trung điểm của $BC$. Tia $BO$ cắt đường tròn $(O)$ tại $D$.

Vì $\widehat{BCD}={{90}^{0}}$, nên $DC\parallel AH$. Tương tự $AD\parallel CH.$

Do đó $ADCH$ là hình bình hành.

Suy ra $\overrightarrow{AH}=\overrightarrow{DC}=2\overrightarrow{OM}$ không đổi.

$\Rightarrow {{T}_{2\overrightarrow{OM}}}\left( A \right)=H$.

Vì vậy khi $A$ di động trên đường tròn $\left( O \right)$ thì $H$ di động trên đường tròn $\left( O’ \right)={{T}_{2\overrightarrow{OM}}}\left( \left( O \right) \right)$.

<!-- chunk:14 level:3 source:https://toanmath.com/2018/08/cac-dang-toan-phep-tinh-tien.html -->
## Ví dụ 10. Cho tam giác $ABC$ có đỉnh $A$ cố định, $\widehat{BAC}=\alpha$ không đổi và $\overrightarrow{BC}=\overrightarrow{v}$ không đổi. Tìm tập hợp các điểm $B,C$.

Gọi $O$ là tâm đường tròn ngoại tiếp tam giác $ABC.$

Khi đó theo định lí sin ta có $\frac{BC}{\sin \alpha }=2R$ không đổi (do $\overrightarrow{BC}=\overrightarrow{v}$ không đổi).

Vậy $OA = R = \frac{{BC}}{{2\sin \alpha }}$, nên $O$ di động trên đường tròn tâm $A$ bán kính $AO = \frac{{BC}}{{2\sin \alpha }}.$

Ta có $OB = OC = R$ không đổi và $\widehat {BOC} = 2\alpha$ không đổi suy ra $\widehat {OBC} = \widehat {OCB}$ $= \frac{{{{180}^0} – 2\alpha }}{2}$ không đổi.

Mặt khác $\overrightarrow {BC}$ có phương không đổi nên $\overrightarrow {OB} ,\overrightarrow {OC}$ cũng có phương không đổi.

Đặt $\overrightarrow {OB} = \overrightarrow {{v_1}}$, $\overrightarrow {OC} = \overrightarrow {{v_2}}$ không đổi, thì ${T_{\overrightarrow {{v_1}} }}\left( O \right) = B$, ${T_{\overrightarrow {{v_2}} }}\left( O \right) = C.$

Vậy tập hợp điểm $B$ là đường tròn $\left( {{A_1};\frac{{BC}}{{2\sin \alpha }}} \right)$ ảnh của $\left( {A,\frac{{BC}}{{2\sin \alpha }}} \right)$ qua ${T_{\overrightarrow {{v_1}} }}$ và tập hợp điểm $C$ là đường tròn $\left( {{A_2};\frac{{BC}}{{2\sin \alpha }}} \right)$ ảnh của $\left( {A,\frac{{BC}}{{2\sin \alpha }}} \right)$ qua ${T_{\overrightarrow {{v_2}} }}.$