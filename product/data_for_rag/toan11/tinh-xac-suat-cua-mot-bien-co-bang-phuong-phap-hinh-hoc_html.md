# Tính xác suất của một biến cố bằng phương pháp hình học

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
Như đã trình bày ở bài viết trước, ta nhận thấy rằng định nghĩa cổ điển về xác suất có hai hạn chế, thứ nhất là số kết quả của phép thử là hữu hạn, thứ hai các kết quả của phép thử phải đồng khả năng xuất hiện. Định nghĩa thống kê của xác suất khắc phục được hạn chế thứ hai. Để khắc phục hạn chế thứ nhất (đồng thời vẫn giả thiết các kết quả đồng khả năng), người ta đưa vào định nghĩa xác suất theo hình học.

Bài viết giới thiệu phương pháp, một số dạng toán và ví dụ minh họa cách tính xác suất của một biến cố bằng phương pháp hình học.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
Xét một phép thử có vô hạn kết cục đồng khả năng. Giả sử ta có thể biểu thị tập hợp mọi kết cục này bởi một miền hình học $G$ nào đó: một đoạn thẳng, một miền phẳng, một mảnh mặt cong hay một khối không gian … và những kết cục thích hợp cho sự kiện $A$ bởi các điểm thuộc miền cong $g ⊂ G.$

Với các giả thiết trên, xác suất của sự kiện $A$ được tính như sau: $P\left( A \right) = \frac{{{\rm{kích\:thước\:miền\:g}}}}{{{\rm{kích\:thước\:miền\:G}}}}.$

Tùy theo $G$ là đoạn thẳng, miền phẳng hay khối không gian mà kích thước được hiểu là độ dài, diện tích hay thể tích.

<!-- chunk:2 level:2 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Dạng toán 1. Bài toán tính xác suất tỉ số độ dài.
Phương pháp giải toán:

+ Xác định tập hợp kết cục đồng khả năng là miền độ dài $G$.

+ Xác định tập hợp kết cục thuận lợi cho biến cố $A$ là miền độ dài $g < G.$

+ Tính $P\left( A \right) = \frac{{{\rm{độ\:dài\:miền\:g}}}}{{{\rm{độ\:dài\:miền\:G}}}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 1. Đường dây điện thoại ngầm nối hai trạm $A$, $B$ bỗng nhiên bị đứt. Dây dài $800$ mét chôn trong lòng đất đồng chất. Hãy tính xác suất của sự kiện: chỗ đứt cách $A$ không quá $100$ mét.

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-1.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-1">

Rõ ràng dây có đứt tại một điểm bất kỳ trên đoạn thẳng $AB$ (như hình vẽ) với cùng khả năng như nhau, do đó có thể biểu thị tập hợp mọi kết cục đồng khả năng của phép thử bởi đoạn thẳng $AB.$

Các kết cục thích hợp cho sự kiện chỗ đứt cách $A$ không quá $100$ mét được biểu thị bởi đoạn $AC.$

Do đó: $P = \frac{{100}}{{800}} = \frac{1}{8}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 2. Trên một vòng tròn bán kính $R$ có một điểm $A$ cố định. Chọn ngẫu nhiên trên vòng tròn đó một điểm. Tính xác suất để điểm này cách $A$ không quá $R.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-2.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-2">

Điểm $M$ có thể chọn tùy ý trên vòng tròn nên miền đồng khả năng là cả vòng tròn.

Muốn biến cố: “Điểm $M$ cách $A$ không quá $R$” xảy ra thì điểm M chỉ được nằm trên cung $IJ$ (như hình vẽ).

Vậy: $P\left( A \right) = \frac{{{\rm{độ\:dài\:IJ}}}}{{{\rm{độ\:dài\:}}\left( O \right)}} = \frac{1}{3}.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Dạng toán 2. Bài toán xác suất tỉ số diện tích.
Phương pháp giải toán:

+ Xác định tập hợp kết cục đồng khả năng là miền diện tích $G.$

+ Xác định tập hợp kết cục thuận lợi cho biến cố $A$ là miền diện tích $g ⊂ G.$

+ Tính $P\left( A \right) = \frac{{{\rm{diện\:tích\:miền\:g}}}}{{{\rm{diện\:tích\:miền\:G}}}} = \frac{{{S_g}}}{{{S_G}}}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 3. Trên đoạn thẳng $OA$ ta chọn ngẫu nhiên hai điểm $B$ và $C$ có độ dài tương ứng là $OB = x$, $OC = y$ $(y ≥ x)$. Tìm xác suất sao cho độ dài của đoạn $BC$ bé hơn độ dài của đoạn $OB.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-6.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-6">

Giả sử đoạn thẳng $OA$ có chiều dài bằng $l.$

Với mỗi cách chọn hai điểm $B$ và $C$ có độ dài tương ứng là $OB = x$, $OC = y$ $(y ≥ x)$ sẽ cho ta tương ứng một điểm $M(x;y)$ trên mặt phẳng tọa độ $Oxy.$

Vì: 
$$
\left\{ {\begin{array}{l}
{0 \le x \le l}\\
\begin{array}{l}
0 \le y \le l\\
y \ge x{\rm{ }}
\end{array}
\end{array}} \right.
$$
 suy ra miền biểu diễn điểm $M(x;y)$ là tam giác $OMP$ như hình vẽ bên dưới.

Để độ dài của đoạn $BC$ bé hơn độ dài của đoạn $OB$ thì $y-x<x$ $⇒y<2x.$

Do đó: Miền biểu diễn các kết cục thuận lợi là tam giác $ONP.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-7.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-7">

Vậy $P = \frac{{{S_{ONP}}}}{{{S_{OMP}}}} = \frac{1}{2}.$

Chú ý: Bạn đọc tham khảo bài viết: Bất phương trình và hệ bất phương trình bậc nhất hai ẩn để xem lại cách biểu diễn miền nghiệm của hệ bất phương trình bậc nhất hai ẩn trên hệ tọa độ $Oxy.$

[ads]

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 4. Xét hình vuông $(H)$ giới hạn bởi: $0 ≤ x ≤ 1$, $0 ≤ y ≤ 1$ và hai đường cong: $y = x^2$ và $y = \sqrt x$. Lấy ngẫu nhiên một điểm $M$ thuộc hình vuông $(H).$ Tìm xác suất để $M$ thuộc hình giới hạn bởi hai đường cong trên.

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-3.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-3">

Diện tích hình vuông $(H)$ bằng $S = 1.$

Hai đường cong $y = x^2$, $y = \sqrt x$ cắt nhau tại $O(0;0)$ và $A(1; 1)$ là hai đỉnh hình vuông $(H).$

Diện tích hình giới hạn bởi hai đường cong là: $S’ = \int_0^1 {\left( {\sqrt x – {x^2}} \right)} dx$ $= \left. {\left( {\frac{2}{3}{x^{\frac{3}{2}}} – \frac{1}{3}{x^3}} \right)} \right|_0^1 = \frac{1}{3}.$

Vậy xác suất cần tìm: $P = \frac{{S’}}{S} = \frac{1}{3} \approx 33\% .$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 5. Có một đoạn thẳng chiều dài $l$. Bẻ gẫy ngẫu nhiên thành $3$ đoạn. Tính xác suất để $3$ đoạn đó tạo thành được một tam giác.

Nếu ta xem đoạn thẳng như một trục số từ $O$ đến $l$, ta ký hiệu $x$ là tọa độ điểm chia thứ nhất và $y$ là tọa độ điểm chia thứ hai (trên trục $Ol$) thì đoạn thẳng được chia thành ba đoạn có độ dài tương ứng là: $x$, $y – x$ và $l – y.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-4.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-4">

Mỗi cách chia đoạn thẳng sẽ được biểu thị bằng một điểm $M(x; y)$ trên mặt phẳng tọa độ $Oxy.$

Ta nhận thấy $0 < x < y < l$ nên miền đồng khả năng là tam giác $OAB.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-5.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-5">

Gọi $X$ là biến cố ba đoạn tạo thành được một tam giác.

Muốn tạo tam giác thì tổng hai cạnh phải lớn hơn cạnh thứ ba, do đó: 
$$
\left\{ \begin{array}{l}
x + \left( {y – x} \right) > l – y\\
x + \left( {l – y} \right) > y – x\\
\left( {y – x} \right) + \left( {l – x} \right) > x
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
y > \frac{l}{2}\\
y < x + \frac{l}{2}\\
x < \frac{l}{2}
\end{array} \right.
$$

Suy ra miền thuận lợi cho $X$ chính là tam giác $ΔIJK.$

Vậy $P(A) = \frac{{{S_{\Delta IJK}}}}{{{S_{\Delta AOB}}}} = \frac{1}{4}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 6. Hai người $A$ và $B$ hẹn gặp nhau tại một địa điểm xác định trong vòng từ $0$ đến $1$ giờ. Người đến trước chờ người kia quá $20$ phút thì sẽ bỏ đi. Tính xác suất để họ gặp được nhau, biết rằng mỗi người có thể đến chỗ hẹn vào thời điểm bất kỳ trong khoảng thời gian trên.

Gọi $x$ là thời gian đến của $A$, $y$ là thời gian đến của $B$ (tính bằng phút).

Mọi kết cục đồng khả năng là mọi cặp số $(x; y)$ mà $0 ≤ x ≤ 60$, $0 ≤ y ≤ 60.$

Tập hợp này được biểu diễn bởi hình vuông $OIJK$ (như hình vẽ).

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-8.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-8">

Các kết cục thích hợp cho hai người gặp nhau là những cặp $(x;y)$ sao cho: $\left| {x – y} \right| \le 20$ $\Leftrightarrow x-20 \le y \le x+20.$

Trên hình vẽ, tập hợp này ứng với miền con của hình vuông $OIJK$, gồm phần nằm giữa các đường thẳng $y = x + 20$ và $y = x – 20.$

Vậy xác suất phải tìm bằng: $P = \frac{{{{60}^2} – {{40}^2}}}{{{{60}^2}}} = \frac{5}{9}.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc.html -->
## Ví dụ 7. Trên mặt phẳng kẻ sẵn các đường thẳng song song cách đều nhau một khoảng có độ dài $2a$, người ta gieo ngẫu nhiên một chiếc kim dài $2l$ $(l < a).$ Tính xác suất sao cho kim cắt một đường thẳng trong số những đường thẳng đó.

Gọi $x$ là khoảng cách từ trung điểm của kim đến đường thẳng song song gần nhất và $φ$ là góc mà kim tạo với các đường này.

Ta có: $0 ≤ x ≤ a$, $0 ≤ φ ≤ π.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-9.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-9">

Do đó có thể biểu diễn miền đồng khả năng bởi một hình chữ nhật có cạnh là $a$ và $π.$

<img link="data_for_rag/toan11/images/tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-10.png" alt="tinh-xac-suat-cua-mot-bien-co-bang-phuong-phap-hinh-hoc-10">

Ta thấy rằng để kim cắt đường thẳng song song, điều kiện cần và đủ là: $0 \le x \le l\sin \varphi .$

Từ các giả thiết của bài toán, suy ra xác suất phải tìm bằng tỷ số diện tích miền gạch chéo và diện tích hình chữ nhật: $P(H) = \frac{{\int\limits_0^\pi {l\sin \varphi d\varphi } }}{{a\pi }} = \frac{{2l}}{{a\pi }}.$