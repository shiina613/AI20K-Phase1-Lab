# Các quy tắc tính xác suất

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
Bài viết hướng dẫn phương pháp giải bài toán xác suất dựa vào hai quy tắc tính xác suất: quy tắc cộng xác suất và quy tắc nhân xác suất.

Các quy tắc tính xác suất:

1. Quy tắc cộng xác suất:

Biến cố hợp:

• Cho hai biến cố $A$ và $B$ cùng liên quan đến một phép thử $T$. Biến cố “$A$ hoặc $B$ xảy ra” được gọi là hợp của hai biến cố $A$ và $B$, kí hiệu $A \cup B.$

• Nếu gọi ${\Omega _A}$ là tập hợp mô tả các kết quả thuận lợi cho $A$, ${\Omega _B}$ là tập hợp mô tả các kết quả thuận lợi cho $B$, thì tập hợp các kết quả thuận lợi cho $A \cup B$ là ${\Omega _A} \cup {\Omega _B}.$

• Tổng quát: Cho $k$ biến cố ${A_1},{A_2},…,{A_k}$ cùng liên quan đến một phép thử $T$. Biến cố “Có ít nhất một trong các biến cố ${A_1},{A_2},…,{A_k}$ xảy ra” được gọi là hợp của $k$ biến cố ${A_1},{A_2},…,{A_k}$, kí hiệu ${A_1} \cup {A_2} \cup … \cup {A_k}.$

Biến cố xung khắc:

• Cho hai biến cố $A$ và $B$ cùng liên quan đến một phép thử $T$. Hai biến cố $A$ và $B$ được gọi là xung khắc nếu biến cố này xảy ra thì biến cố kia không xảy ra.

• Hai biến cố $A$ và $B$ là xung khắc khi và chỉ khi ${\Omega _A} \cap {\Omega _B} = \emptyset .$

Quy tắc cộng xác suất:

• Nếu hai biến cố $A$ và $B$ xung khắc thì xác suất để $A$ hoặc $B$ xảy ra là: $P(A \cup B) = P\left( A \right) + P\left( B \right).$

• Cho $k$ biến cố ${A_1},{A_2},…,{A_k}$ đôi một xung khắc, xác suất để ít nhất một trong các biến cố ${A_1},{A_2},…,{A_k}$ xảy ra là: $P({A_1} \cup {A_2} \cup … \cup {A_k})$ $= P\left( {{A_1}} \right) + P\left( {{A_2}} \right) + … + P\left( {{A_k}} \right).$

Biến cố đối:

• Cho biến cố $A$ khi đó biến cố “Không xảy ra $A$” được gọi là biến cố đối của $A$, kí hiệu $\overline A$.

• Hai biến cố đối nhau là hai biến cố xung khắc. Tuy nhiên hai biến cố xung khắc chưa chắc là hai biến cố đối nhau.

• Cho biến cố $A$. Xác suất của biến cố đối $\overline A$ là $P\left( {\overline A } \right) = 1 – P\left( A \right).$

2. Quy tắc nhân xác suất:

Biến cố giao:

• Cho hai biến cố $A$ và $B$ cùng liên quan đến một phép thử $T$. Biến cố “Cả $A$ và $B$ cùng xảy ra” được gọi là giao của hai biến cố $A$ và $B$, kí hiệu là $AB.$

• Nếu gọi ${\Omega _A}$ là tập hợp mô tả các kết quả thuận lợi cho $A$, ${\Omega _B}$ là tập hợp mô tả các kết quả thuận lợi cho $B$, thì tập hợp các kết quả thuận lợi cho $AB$ là $A \cap B.$

• Tổng quát: Cho $k$ biến cố ${A_1},{A_2},…,{A_k}$ cùng liên quan đến một phép thử $T$. Biến cố “Tất cả $k$ biến cố ${A_1},{A_2},…,{A_k}$ đều xảy ra” được gọi là giao của $k$ biến cố ${A_1},{A_2},…,{A_k}$, kí hiệu ${A_1}{A_2}…{A_k}$.

Biến cố độc lập:

• Cho hai biến cố $A$ và $B$ cùng liên quan đến một phép thử $T$. Hai biến cố $A$ và $B$ được gọi là độc lập với nhau nếu việc xảy ra hay không xảy ra của biến cố này không làm ảnh hưởng tới việc xảy ra hay không xảy ra của biến cố kia.

• Nếu hai biến cố $A$, $B$ độc lập với nhau thì $A$ và $\overline B$, $\overline A$ và $B$, $\overline A$ và $\overline B$ cũng độc lập với nhau.

• Tổng quát: Cho $k$ biến cố ${A_1},{A_2},…,{A_k}$ cùng liên quan đến một phép thử $T$. $k$ biến cố này được gọi là độc lập với nhau nếu việc xảy ra hay không xảy ra của mỗi biến cố không làm ảnh hưởng tới việc xảy ra hay không xảy ra của các biến cố còn lại.

Quy tắc nhân xác suất:

• Nếu hai biến cố $A$ và $B$ độc lập với nhau thì xác suất để $A$ và $B$ xảy ra là: $P\left( {AB} \right) = P\left( A \right).P\left( B \right).$

• Cho $k$ biến cố ${A_1},{A_2},…,{A_k}$ độc lập với nhau thì: $P\left( {{A_1}{A_2}…{A_k}} \right)$ $= P\left( {{A_1}} \right).P\left( {{A_2}} \right)…P\left( {{A_k}} \right).$

Các ví dụ minh họa:

<!-- chunk:1 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 1. Cho một con súc sắc không cân đối, biết rằng khi gieo, xác suất mặt bốn chấm xuất hiện nhiều gấp $3$ lần mặt khác, các mặt còn lại đồng khả năng xảy ra. Gieo con súc sắc đó $1$ lần, tìm xác suất để xuất hiện mặt có số chấm là số chẵn.

Gọi ${A_i}$ là biến cố: “Xuất hiện mặt $i$ chấm”, với $i = 1,2,3,4,5,6.$

Ta có: $P({A_1}) = P({A_2}) = P({A_3})$ $= P({A_5}) = P({A_6}) = \frac{1}{3}P({A_4}) = x.$

Do $P\left( {{A_1}} \right) + P\left( {{A_2}} \right) + P\left( {{A_3}} \right)$ $+ P\left( {{A_4}} \right) + P\left( {{A_5}} \right) + P\left( {{A_6}} \right) = 1$, suy ra ${ \Rightarrow 5x + 3x = 1}$ ${ \Rightarrow x = \frac{1}{8}}.$

Gọi $A$ là biến cố: “Xuất hiện mặt có số chấm là số chẵn”, suy ra $A = {A_2} \cup {A_4} \cup {A_6}.$

Vì các biến cố ${A_i}$ xung khắc, áp dụng quy tắc cộng xác suất, suy ra: $P(A) = P({A_2}) + P({A_4}) + P({A_6})$ $= \frac{1}{8} + \frac{3}{8} + \frac{1}{8} = \frac{5}{8}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 2. Gieo một con xúc sắc $4$ lần. Tìm xác suất của các biến cố:

1. $A:$ “Mặt $4$ chấm xuất hiện ít nhất một lần.”

2. $B:$ “Mặt $3$ chấm xuất hiện đúng một lần.”

1. Gọi ${A_i}$ là biến cố “Mặt $4$ chấm xuất hiện lần thứ $i$”, với $i = 1,2,3,4.$

Khi đó: $\overline {{A_i}}$ là biến cố: “Mặt $4$ chấm không xuất hiện lần thứ $i$.”

$P\left( {{A_i}} \right) = \frac{1}{6}$, $P\left( {\overline {{A_i}} } \right) = 1 – P({A_i})$ $= 1 – \frac{1}{6} = \frac{5}{6}.$

Ta có: $\overline A = \overline {{A_1}} .\overline {{A_2}} .\overline {{A_3}} .\overline {{A_4}} .$

Vì các biến cố $\overline {{A_i}}$ độc lập với nhau, áp dụng quy tắc nhân xác suất, suy ra: $P(\overline A )$ $= P\left( {\overline {{A_1}} } \right)P\left( {\overline {{A_2}} } \right)P\left( {\overline {{A_3}} } \right)P\left( {\overline {{A_4}} } \right)$ $= {\left( {\frac{5}{6}} \right)^4}.$

Vậy $P\left( A \right) = 1 – P\left( {\overline A } \right)$ $= 1 – {\left( {\frac{5}{6}} \right)^4}.$

2. Gọi ${B_i}$ là biến cố “Mặt $3$ chấm xuất hiện lần thứ $i$”, với $i = 1,2,3,4.$

Khi đó: $\overline {{B_i}}$ là biến cố “Mặt $3$ chấm không xuất hiện lần thứ $i$.”

Ta có: $B = {B_1}.\overline {{B_2}} .\overline {{B_3}} .\overline {{B_4}}$ $\cup \overline {{B_1}} .{B_2}.\overline {{B_3}} .\overline {{B_4}}$ $\cup \overline {{B_1}} .\overline {{B_2}} .{B_3}.\overline {{B_4}}$ $\cup \overline {{B_1}} .\overline {{B_2}} .\overline {{B_3}} .{B_4}.$

Suy ra: $P\left( B \right) = P\left( {{B_1}} \right)P\left( {\overline {{B_2}} } \right)P\left( {\overline {{B_3}} } \right)P\left( {\overline {{B_4}} } \right)$ $+ P\left( {\overline {{B_1}} } \right)P\left( {{B_2}} \right)P\left( {\overline {{B_3}} } \right)P\left( {\overline {{B_4}} } \right)$ $+ P\left( {\overline {{B_1}} } \right)P\left( {\overline {{B_2}} } \right)P\left( {{B_3}} \right)P\left( {\overline {{B_4}} } \right)$ $+ P\left( {\overline {{B_1}} } \right)P\left( {\overline {{B_2}} } \right)P\left( {\overline {{B_3}} } \right)P\left( {{B_4}} \right).$

Mà $P\left( {{B_i}} \right) = \frac{1}{6}$, $P\left( {\overline {{B_i}} } \right) = \frac{5}{6}.$

Do đó: $P\left( B \right) = 4.\frac{1}{6}.{\left( {\frac{5}{6}} \right)^3} = \frac{{125}}{{324}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 3. Một hộp đựng $4$ viên bi xanh, $3$ viên bi đỏ và $2$ viên bi vàng. Chọn ngẫu nhiên $2$ viên bi:

1. Tính xác suất để chọn được $2$ viên bi cùng màu.

2. Tính xác suất để chọn được $2$ viên bi khác màu.

1. Gọi:

$A$ là biến cố “Chọn được $2$ viên bi xanh”.

$B$ là biến cố “Chọn được $2$ viên bi đỏ”.

$C$ là biến cố “Chọn được $2$ viên bi vàng”.

$X$ là biến cố “Chọn được $2$ viên bi cùng màu”.

Ta có: $X = A \cup B \cup C$ và các biến cố $A,B,C$ đôi một xung khắc.

Do đó: $P(X) = P(A) + P(B) + P(C).$

Mà: $P(A) = \frac{{C_4^2}}{{C_9^2}} = \frac{1}{6}$, $P(B) = \frac{{C_3^2}}{{C_9^2}} = \frac{1}{{12}}$, $P(C) = \frac{{C_2^2}}{{C_9^2}} = \frac{1}{{36}}.$

Vậy $P(X) = \frac{1}{6} + \frac{1}{{12}} + \frac{1}{{36}} = \frac{5}{{18}}.$

2. Biến cố “Chọn được $2$ viên bi khác màu” chính là biến cố $\overline X .$

Suy ra: $P(\overline X ) = 1 – P(X) = \frac{{13}}{{18}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 4. Một cặp vợ chồng mong muốn sinh con trai. Nếu sinh con gái, họ sẽ sinh tiếp cho đến khi sinh được một đứa con trai thì dừng lại. Biết rằng xác suất sinh được con trai trong mỗi lần sinh là $0,51$. Tìm xác suất sao cho cặp vợ chồng đó sinh được con trai ở lần sinh thứ $2$.

Gọi:

$A$ là biến cố: “Sinh con gái ở lần thứ nhất.”

$B$ là biến cố: “Sinh con trai ở lần thứ hai.”

Ta có: $P(A) = 1 – 0,51 = 0,49,$ $P(B) = 0,51.$

Gọi $C$ là biến cố: “Sinh con gái ở lần thứ nhất và sinh con trai ở lần thứ hai.”

Khi đó: $C = AB$, mà $A$ và $B$ độc lập, do đó, theo quy tắc nhân xác suất ta suy ra: $P(C) = P(AB)$ $= P(A).P(B) = 0,2499.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 5. Xác suất bắn trúng mục tiêu của một vận động viên khi bắn một viên đạn là $0,6.$ Vận động viên đó bắn hai viên đạn một cách độc lập. Tính xác suất để một viên đạn trúng mục tiêu và một viên đạn trượt mục tiêu.

Gọi:

${A_1}$ là biến cố “Viên đạn thứ nhất trúng mục tiêu.”

${A_2}$ là biến cố “Viên đạn thứ hai trúng mục tiêu.”

$X$ là biến cố “Một viên đạn trúng mục tiêu và một viên đạn không trúng mục tiêu.”

Khi đó: $X = {A_1}\overline {{A_2}} \cup \overline {{A_1}} {A_2}.$

Suy ra: $P\left( X \right) = P\left( {{A_1}} \right)P\left( {\overline {{A_2}} } \right) + P\left( {\overline {{A_1}} } \right)P\left( {{A_2}} \right)$ $= 0,6.0.4 + 0,4.0,6 = 0,48.$

[ads]

<!-- chunk:6 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 6. Việt và Nam chơi cờ tướng cùng nhau. Trong một ván cờ, xác suất để Việt thắng Nam là $0,3$ và xác suất để Nam thắng Việt là $0,4$. Hai bạn dừng chơi cờ khi có người thắng, người thua. Tính xác suất để hai bạn dừng chơi sau hai ván cờ.

Gọi:

$A$ là biến cố: “Ván thứ nhất Việt và Nam hòa nhau.”

$B$ là biến cố: “Ván thứ hai Việt thắng Nam.”

$C$ là biến cố: “Ván thứ hai Nam thắng Việt.”

$D$ là biến cố: “Hai bạn Việt và Nam dừng chơi sau hai ván cờ.”

Khi đó: $D = AB \cup AC.$

Ta có: $P(A) = 1 – 0,3 – 0,4 = 0,3$, $P(B) = 0,3$, $P(C) = 0,4.$

Suy ra: $P\left( D \right) = P\left( A \right)P\left( B \right) + P\left( A \right)P\left( C \right)$ $=0,21.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 7. Cho ba hộp đựng bút giống nhau, mỗi hộp đựng $7$ cây bút chỉ khác nhau về màu sắc.

Hộp thứ nhất: Có $3$ cây bút màu đỏ, $2$ cây bút màu xanh, $2$ cây bút màu đen.

Hộp thứ hai: Có $2$ cây bút màu đỏ, $2$ cây bút màu xanh, $3$ cây bút màu đen.

Hộp thứ ba: Có $5$ cây bút màu đỏ, $1$ cây bút màu xanh, $1$ cây bút màu đen.

Lấy ngẫu nhiên một hộp, rút ngẫu nhiên từ hộp đó ra $2$ cây bút. Tính xác suất của các biến cố:

1. $A$: “Lấy được $2$ cây bút màu xanh.”

2. $B$: “Lấy được $2$ cây bút không có màu đen.”

1. Gọi ${X_i}$ là biến cố: “Rút được hộp thứ $i$”, $i = 1,2,3$. Ta có: $P\left( {{X_i}} \right) = \frac{1}{3}.$

Gọi ${A_i}$ là biến cố: “Lấy được $2$ cây bút màu xanh ở hộp thứ $i$”, $i = 1,2,3.$ Ta có: $P\left( {{A_1}} \right) = P\left( {{A_2}} \right) = \frac{1}{{C_7^2}}$, $P\left( {{A_3}} \right) = 0.$

Khi đó: $A = {X_1}{A_1} \cup {X_2}{A_2} \cup {X_3}{A_3}.$

Suy ra: $P\left( A \right) = P\left( {{X_1}} \right)P\left( {{A_1}} \right)$ $+ P\left( {{X_2}} \right)P\left( {{A_2}} \right) + P\left( {{X_3}} \right)P\left( {{A_3}} \right)$ $=\frac{1}{3}.\frac{1}{{C_7^2}} + \frac{1}{3}.\frac{1}{{C_7^2}} + \frac{1}{3}.0$ $= \frac{2}{{63}}.$

2. Gọi ${B_i}$ là biến cố: “Rút $2$ bút ở hộp thứ $i$ không có màu đen.”

Ta có: $P\left( {{B_1}} \right) = \frac{{C_5^2}}{{C_7^2}}$, $P\left( {{B_2}} \right) = \frac{{C_4^2}}{{C_7^2}}$, $P\left( {{B_3}} \right) = \frac{{C_6^2}}{{C_7^2}}.$

Khi đó: $B = {X_1}{B_1} \cup {X_2}{B_2} \cup {X_3}{B_3}.$

Suy ra: $P\left( B \right) = P\left( {{X_1}} \right)P\left( {{B_1}} \right)$ $+ P\left( {{X_2}} \right)P\left( {{B_2}} \right) + P\left( {{X_3}} \right)P\left( {{B_3}} \right)$ = $\frac{{31}}{{63}}.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 8. Một mạch điện gồm $4$ linh kiện như hình vẽ, trong đó xác suất hỏng của từng linh kiện trong một khoảng thời gian $t$ nào đó tương ứng là $0,2$; $0,1$; $0,05$ và $0,02.$ Biết rằng các linh kiện làm việc độc lập với nhau và các dây dẫn điện luôn tốt. Tính xác suất để mạng điện hoạt động tốt trong khoảng thời gian $t.$

<img link="data_for_rag/toan11/images/cac-quy-tac-tinh-xac-suat-1.png" alt="cac-quy-tac-tinh-xac-suat-1">

Mạng điện hoạt động tốt khi một trong các trường hợp sau xảy ra:

+ Trường hợp 1: Linh kiện $1, 2, 4$ hoạt động tốt, linh kiện $3$ bị hỏng.

Xác suất là: ${P_1} = \left( {1 – 0,2} \right).\left( {1 – 0,1} \right).0,005.\left( {1 – 0,02} \right).$

+ Trường hợp 2: Linh kiện $1, 3, 4$ hoạt động tốt, linh kiện $2$ bị hỏng.

Xác suất là: ${P_2} = \left( {1 – 0,2} \right).0,1.\left( {1 – 0,005} \right).\left( {1 – 0,02} \right).$

+ Trường hợp 3: Tất cả các linh kiện $1, 2, 3, 4$ đều hoạt động tốt.

Xác suất là: ${P_3} = \left( {1 – 0,2} \right).\left( {1 – 0,1} \right).\left( {1 – 0,005} \right).\left( {1 – 0,02} \right).$

Vậy xác suất để mạng điện hoạt động tốt trong khoảng thời gian $t$ là: $P = {P_1} + {P_2} + {P_3} = 0,78008.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 9. Ba cầu thủ sút phạt đền 11m, mỗi người đá một lần với xác suất làm bàn tương ứng là $x$, $y$ và $0,6.$ (với $x > y$). Biết rằng xác suất để ít nhất một trong ba cầu thủ ghi bàn là $0,976$ và xác suất để cả ba cầu thủ đều ghi bàn là $0,336.$ Tính xác suất để có đúng hai cầu thủ ghi bàn.

Gọi ${A_i}$ là biến cố “Cầu thủ thứ $i$ ghi bàn”, với $i = 1,2,3.$

Các biến cố ${A_i}$ độc lập với nhau và: $P\left( {{A_1}} \right) = x$, $P\left( {{A_2}} \right) = y$, $P\left( {{A_3}} \right) = 0,6.$

Gọi:

$A$ là biến cố: “Có ít nhất một trong ba cầu thủ ghi bàn.”

$B$ là biến cố: “Cả ba cầu thủ đều ghi bàn.”

$C$ là biến cố: “Có đúng hai cầu thủ ghi bàn.”

Ta có: $\overline A = \overline {{A_1}} .\overline {{A_2}} .\overline {{A_3}}$ $\Rightarrow P\left( {\overline A } \right) = P\left( {\overline {{A_1}} } \right).P\left( {\overline {{A_2}} } \right).P\left( {\overline {{A_3}} } \right)$ $= 0,4(1 – x)(1 – y).$

Nên $P(A) = 1 – P\left( {\overline A } \right)$ $= 1 – 0,4(1 – x)(1 – y) = 0,976.$

Suy ra $(1 – x)(1 – y) = \frac{3}{{50}}$ $\Leftrightarrow xy – x – y = – \frac{{47}}{{50}}$ $(1).$

Tương tự: $B = {A_1}{A_2}{A_3}$, suy ra: $P\left( B \right) = P\left( {{A_1}} \right).P\left( {{A_2}} \right).P\left( {{A_3}} \right)$ $= 0,6xy = 0,336$ $\Leftrightarrow xy = \frac{{14}}{{25}}$ $(2).$

Từ $(1)$ và $(2)$ ta thu được hệ phương trình: 
$$
\left\{ \begin{array}{l}
xy – x – y = – \frac{{47}}{{50}}\\
xy = \frac{{14}}{{25}}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 0,8\\
y = 0,7
\end{array} \right.
$$

Ta có: $C = \overline {{A_1}} {A_2}{A_3} + {A_1}\overline {{A_2}} {A_3} + {A_1}{A_2}\overline {{A_3}} .$

Suy ra: $P\left( C \right) = P\left( {\overline {{A_1}} } \right)P\left( {{A_2}} \right)P\left( {{A_3}} \right)$ $+ P\left( {{A_1}} \right)P\left( {\overline {{A_2}} } \right)P\left( {{A_3}} \right)$ $+ P\left( {{A_1}} \right)P\left( {{A_2}} \right)P\left( {\overline {{A_3}} } \right)$ $= (1 – x)y.0,6$ $+ x(1 – y).0,6$ $+ xy.0,4$ $= 0,452.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/08/cac-quy-tac-tinh-xac-suat.html -->
## Ví dụ 10. Một đề thi trắc nghiệm gồm $10$ câu hỏi, mỗi câu hỏi có $4$ phương án lựa chọn trả lời trong đó chỉ có $1$ phương án đúng. Giả sử mỗi câu trả lời đúng được $4$ điểm và mỗi câu trả lời sai bị trừ đi $2$ điểm. Một học sinh không học bài nên lựa chọn đáp án một cách ngẫu nhiên. Tìm xác suất để học sinh này nhận điểm dưới $1.$

Ta có: Xác suất để học sinh trả lời câu đúng một câu hỏi là $\frac{1}{4}$, xác suất trả lời câu sai một câu hỏi là $\frac{3}{4}.$

Gọi $x$ $\left( {x \in N,0 \le x \le 10} \right)$ là số câu trả lời đúng, khi đó số câu trả lời sai là $10 – x.$

Số điểm học sinh này đạt được là: $4x – 2(10 – x) = 6x – 20.$

Học sinh này nhận điểm dưới $1$ khi $6x – 20 < 1$ $\Leftrightarrow x < \frac{{21}}{6}.$

Suy ra $x$ nhận các giá trị: $0,1,2,3.$

Gọi ${A_i}$ $\left( {i = 0,1,2,3} \right)$ là biến cố: “Học sinh trả lời đúng $i$ câu hỏi.”

$A$ là biến cố: “Học sinh nhận điểm dưới $1$.”

Khi đó: $A = {A_0} \cup {A_1} \cup {A_2} \cup {A_3}.$

Suy ra: $P(A) = P({A_0}) + P({A_1}) + P({A_2}) + P({A_3}).$

Mà: $P({A_i}) = C_{10}^i.{\left( {\frac{1}{4}} \right)^i}{\left( {\frac{3}{4}} \right)^{10 – i}}.$

Vậy: $P(A) = 0,7759.$