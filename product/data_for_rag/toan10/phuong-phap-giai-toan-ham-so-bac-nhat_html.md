# Phương pháp giải toán hàm số bậc nhất

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
Bài viết hướng dẫn phương pháp giải các dạng toán hàm số bậc nhất trong chương trình Đại số 10 chương 2, trong mỗi dạng toán đều bao gồm phương pháp giải toán cùng các ví dụ minh họa điển hình có lời giải chi tiết.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## A. KIẾN THỨC TRỌNG TÂM HÀM SỐ BẬC NHẤT
1. Định nghĩa hàm số bậc nhất: Hàm số bậc nhất là hàm số có dạng $y = ax + b$ $(a \ne 0).$

2. Sự biến thiên của hàm số bậc nhất:

+ Tập xác định: $D = R.$

+ Hàm số $y = ax + b$ đồng biến khi $a > 0$ và nghịch biến khi $a < 0.$

+ Bảng biến thiên:

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-1.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-1">

3. Đồ thị hàm số bậc nhất: Đồ thị của hàm số $y=ax+b$ $(a\ne 0)$ là một đường thẳng có hệ số góc bằng $a,$ cắt trục hoành tại $A\left( -\frac{b}{a};0 \right)$ và cắt trục tung tại $B\left( 0;b \right).$

Lưu ý:

+ Nếu $a=0\Rightarrow y=b$ là hàm số hằng, đồ thị là đường thẳng song song hoặc trùng với trục hoành.

+ Cho đường thẳng $d$ có hệ số góc $k$, $d$ đi qua điểm $M\left( {{x}_{0}};{{y}_{0}} \right)$, khi đó phương trình của đường thẳng $d$ là: $y-{{y}_{0}}=a\left( x-{{x}_{0}} \right)$.

<!-- chunk:2 level:2 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Dạng toán 1. Xác định hàm số bậc nhất và sự tương giao giữa đồ thị các hàm số bậc nhất.
Phương pháp giải toán:

Để xác định hàm số bậc nhất ta thực hiện theo các bước sau:

+ Gọi hàm số cần tìm là $y=ax+b$, $a\ne 0$.

+ Dựa giả thiết bài toán để thiết lập hệ phương trình với ẩn $a,b.$

+ Giải hệ phương trình để tìm ẩn số $a$, $b$ và suy ra hàm số cần tìm.

Cho hai đường thẳng ${{d}_{1}}:y={{a}_{1}}x+{{b}_{1}}$ và ${{d}_{2}}:y={{a}_{2}}x+{{b}_{2}}.$ Khi đó:

a) ${{d}_{1}}$ và ${{d}_{2}}$ trùng nhau 
$$
\Leftrightarrow \left\{ \begin{align}
& {{a}_{1}}={{a}_{2}} \\
& {{b}_{1}}={{b}_{2}} \\
\end{align} \right.
$$

b) ${{d}_{1}}$ và ${{d}_{2}}$ song song nhau 
$$
\Leftrightarrow \left\{ \begin{align}
& {{a}_{1}}={{a}_{2}} \\
& {{b}_{1}}\ne {{b}_{2}} \\
\end{align} \right.
$$

c) ${{d}_{1}}$ và ${{d}_{2}}$ cắt nhau $\Leftrightarrow {{a}_{1}}\ne {{a}_{2}}$, tọa độ giao điểm là nghiệm của hệ phương trình 
$$
\left\{ \begin{matrix}
y={{a}_{1}}x+{{b}_{1}} \\
y={{a}_{2}}x+{{b}_{2}} \\
\end{matrix} \right.
$$

d) ${{d}_{1}}$ và ${{d}_{2}}$ vuông góc nhau $\Leftrightarrow {{a}_{1}}.{{a}_{2}}=-1.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 1. Cho hàm số bậc nhất có đồ thị là đường thẳng $d$, tìm hàm số đó biết:

a) $d$ đi qua $A(1;3)$, $B(2;-1).$

b) $d$ đi qua $C(3;-2)$ và song song với $\Delta: 3x-2y+1=0.$

c) $d$ đi qua $M(1;2)$ và cắt hai tia $Ox$, $Oy$ tại $P$, $Q$ sao cho ${{S}_{\Delta OPQ}}$ nhỏ nhất.

d) $d$ đi qua $N\left( 2;-1 \right)$ và $d\bot d’$ với $d’:y=4x+3.$

Gọi hàm số cần tìm là $y=ax+b$, $a\ne 0.$

a) Vì $A\in d$ và $B\in d$ nên ta có hệ phương trình:

$$
\left\{ \begin{matrix}
3=a+b \\
-1=2a+b \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
a=-4 \\
b=7 \\
\end{matrix} \right.
$$

Vậy hàm số cần tìm là $y=-4x+7.$

b) Ta có $\Delta: y=\frac{3}{2}x+\frac{1}{2}$.

Vì $\text{d}//\Delta$ nên 
$$
\left\{ \begin{matrix}
a=\frac{3}{2} \\
b\ne \frac{1}{2} \\
\end{matrix} \right.
$$

Mặt khác $C\in d$ $\Rightarrow -2=3a+b.$

Suy ra 
$$
\left\{ \begin{matrix}
a=\frac{3}{2} \\
b=-\frac{13}{2} \\
\end{matrix} \right.
$$

Vậy hàm số cần tìm là $y=\frac{3}{2}x-\frac{13}{2}.$

c) Đường thẳng $d$ cắt trục $Ox$ tại $P\left( -\frac{b}{a};0 \right)$ và cắt $Oy$ tại $Q\left( 0;b \right)$ với $a<0$, $b>0.$

Suy ra ${S_{\Delta OPQ}} = \frac{1}{2}OP.OQ$ $= \frac{1}{2}.\left| { – \frac{b}{a}} \right|.\left| b \right|$ $= – \frac{{{b^2}}}{{2a}}.$

Ta có $M \in d$ $\Rightarrow 2 = a + b$ $\Rightarrow b = 2 – a.$

Do đó: ${S_{\Delta OPQ}} = – \frac{{{{\left( {2 – a} \right)}^2}}}{{2a}}$ $= – \frac{2}{a} – \frac{a}{2} + 2.$

Áp dụng bất đẳng thức Côsi, ta có: $– \frac{2}{a} – \frac{a}{2}$ $\ge 2\sqrt {\left( { – \frac{2}{a}} \right).\left( { – \frac{a}{2}} \right)}$ $= 2$ $\Rightarrow {S_{\Delta OPQ}} \ge 4.$

Đẳng thức xảy ra khi và chỉ khi 
$$
\left\{ {\begin{array}{c}
{ – \frac{2}{a} = – \frac{a}{2}}\\
{a < 0}
\end{array}} \right.
$$
 $\Leftrightarrow a = – 2$ $\Rightarrow b = 4.$

Vậy hàm số cần tìm là $y = – 2x + 4.$

d) Đường thẳng $d$ đi qua $N\left( 2;-1 \right)$ nên $-1=2a+b.$

Và $d\bot d’$ $\Rightarrow 4.a=-1$ $\Leftrightarrow a=-\frac{1}{4}.$

Do đó: $b=-\frac{1}{2}$.

Vậy hàm số cần tìm là $y=-\frac{1}{4}x-\frac{1}{2}$.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 2. Cho hai đường thẳng $d:y = x + 2m$ và $d’:y = 3x + 2$ ($m$ là tham số).

a) Chứng minh rằng hai đường thẳng $d$, $d’$ cắt nhau và tìm tọa độ giao điểm của chúng.

b) Tìm $m$ để ba đường thẳng $d$, $d’$ và $d”:y=-mx+2$ phân biệt đồng quy.

a) Ta có ${{a}_{d}}=1\ne {{a}_{d’}}=3$ suy ra hai đường thẳng $d$, $d’$cắt nhau.

Tọa độ giao điểm của hai đường thẳng $d$, $d’$ là nghiệm của hệ phương trình: 
$$
\left\{ {\begin{array}{c}
{y = x + 2m}\\
{y = 3x + 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{x = m – 1}\\
{y = 3m – 1}
\end{array}} \right.
$$

Suy ra $d$ và $d’$ cắt nhau tại điểm $M\left( m-1;3m-1 \right).$

b) Vì ba đường thẳng $d$, $d’$, $d”$ đồng quy nên $M\in d”$, do đó: $3m-1=-m\left( m-1 \right)+2$ $\Leftrightarrow {{m}^{2}}+2m-3=0$ 
$$
\Leftrightarrow \left[ \begin{matrix}
m=1 \\
m=-3 \\
\end{matrix} \right.
$$

+ Với $m=1$ ta có ba đường thẳng là $d:y=x+2$, $d’:y=3x+2$, $d”:y=-x+2$ phân biệt và đồng quy tại $M\left( 0;2 \right)$.

+ Với $m=-3$ ta có $d’\equiv d”$ suy ra $m=-3$ không thỏa mãn yêu cầu bài toán.

Vậy $m=1$ là giá trị cần tìm.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 3. Cho đường thẳng $d:y=\left( m-1 \right)x+m$ và $d’:y=\left( {{m}^{2}}-1 \right)x+6.$

a) Tìm $m$ để hai đường thẳng $d$, $d’$ song song với nhau.

b) Tìm $m$ để đường thẳng $d$ cắt trục tung tại $A$, $d’$ cắt trục hoành tại $B$ sao cho tam giác $OAB$ cân tại $O.$

a)

+ Với $m=1$, ta có $d:y=1$, $d’:y=6$ do đó hai đường thẳng này song song với nhau.

+ Với $m=-1$, ta có $d:y=-2x-1$, $d’:y=6$ suy ra hai đường thẳng này cắt nhau tại $M\left( -\frac{7}{2};6 \right).$

+ Với $m\ne \pm 1$ khi đó hai đường thẳng trên là đồ thị của hàm số bậc nhất nên song song với nhau khi và chỉ khi 
$$
\left\{ \begin{matrix}
m-1={{m}^{2}}-1 \\
m\ne 6 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
\left[ \begin{matrix}
m=1 \\
m=0 \\
\end{matrix} \right. \\
m\ne 6 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{matrix}
m=1 \\
m=0 \\
\end{matrix} \right.
$$

Đối chiếu với điều kiện $m\ne \pm 1$ suy ra $m=0$.

Vậy $m=0$ và $m=1$ là giá trị cần tìm.

b) Ta có tọa độ điểm $A$ là nghiệm của hệ 
$$
\left\{ \begin{matrix}
y=\left( m-1 \right)x+m \\
x=0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
x=0 \\
y=m \\
\end{matrix} \right.
$$
 $\Rightarrow A\left( 0;m \right).$

Tọa độ điểm $B$ là nghiệm của hệ 
$$
\left\{ \begin{matrix}
y=\left( {{m}^{2}}-1 \right)x+6 \\
y=0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{matrix}
\left( {{m}^{2}}-1 \right)x+6=0 \\
y=0 \\
\end{matrix} \right.
$$
 $(*).$

Rõ ràng $m=\pm 1$ hệ phương trình $(*)$ vô nghiệm.

Với $m\ne \pm 1$, ta có $(*)$ 
$$
\Leftrightarrow \left\{ \begin{matrix}
x=\frac{6}{1-{{m}^{2}}} \\
y=0 \\
\end{matrix} \right.
$$
 $\Rightarrow B\left( \frac{6}{1-{{m}^{2}}};0 \right).$

Do đó tam giác $OAB$ cân tại $O$ $\Leftrightarrow \left| m \right|=\left| \frac{6}{1-{{m}^{2}}} \right|$ $\Leftrightarrow \left| m-{{m}^{3}} \right|=6$ 
$$
\Leftrightarrow \left[ \begin{matrix}
m-{{m}^{3}}=6 \\
m-{{m}^{3}}=-6 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{matrix}
{{m}^{3}}-m+6=0 \\
{{m}^{3}}-m-6=0 \\
\end{matrix} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{matrix}
m=-2 \\
m=2 \\
\end{matrix} \right.
$$
 (thỏa mãn).

Vậy $m=\pm 2$ là giá trị cần tìm.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 4. Lập bảng biến thiên và vẽ đồ thị của các hàm số sau:

a) $y = 3x + 6.$

b) $y = – \frac{1}{2}x + \frac{3}{2}.$

a) Tập xác định $D = R.$

Vì $a = 3 > 0$ suy ra hàm số đồng biến trên $R.$

Bảng biến thiên:

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-2.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-2">

Đồ thị hàm số $y = 3x + 6$ đi qua $A\left( { – 2;0} \right)$, $B\left( { – 1;3} \right).$

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-3.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-3">

b) Tập xác định $D = R.$

Vì $a = – \frac{1}{2} < 0$ suy ra hàm số nghịch biến trên $R.$

Bảng biến thiên:

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-4.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-4">

Đồ thị hàm số $y = – \frac{1}{2}x + \frac{3}{2}$ đi qua $A\left( {3;0} \right)$, $B\left( {0;\frac{3}{2}} \right).$

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-5.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-5">

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 5. Cho các hàm số $y = 2x – 3$, $y = – x – 3$, $y = – 2.$

a) Vẽ đồ thị các hàm số trên trong cùng một hệ trục tọa độ.

b) Dựa vào đồ thị hãy xác định giao điểm của các đồ thị hàm số đó.

a) Đường thẳng $y = 2x – 3$ đi qua các điểm $A\left( {0; – 3} \right)$, $B\left( {\frac{3}{2};0} \right).$

Đường thẳng $y = – x – 3$ đi qua các điểm $A\left( {0; – 3} \right)$, $C\left( { – 3;0} \right).$

Đường thẳng $y = – 2$ song song với trục hoành và cắt trục tung tại điểm có tung độ bằng $-2.$

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-6.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-6">

b) Đường thẳng $y = 2x – 3$, $y = – x – 3$ cắt nhau tại $A\left( {0; – 3} \right).$

Đường thẳng $y = – x – 3$, $y = – 2$ cắt nhau tại $A’\left( { – 1; – 2} \right).$

Đường thẳng $y = 2x – 3$, $y = – 2$ cắt nhau tại $A\left( {\frac{1}{2}; – 2} \right).$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 6. Cho đồ thị hàm số có đồ thị $\left( C \right)$ như hình vẽ.

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-7.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-7">

a) Hãy lập bảng biến thiên của hàm số trên $\left[ -3;3 \right].$

b) Tìm giá trị lớn nhất và nhỏ nhất của hàm số trên $\left[ -4;2 \right].$

a) Bảng biến thiên của hàm số trên $\left[ { – 3;3} \right].$

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-8.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-8">

b) Dựa vào đồ thị hàm số đã cho ta có:

$\mathop {{\rm{max}}}\limits_{\left[ { – 4;2} \right]} = 3$ khi và chỉ khi $x = – 4.$

$\mathop {\min }\limits_{\left[ { – 4;2} \right]} = 0$ khi và chỉ khi $x = 2.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Dạng toán 3. Đồ thị của hàm số chứa dấu trị tuyệt đối $y = \left| {ax + b} \right|.$
Phương pháp giải toán: Vẽ đồ thị $\left( C \right)$ của hàm số $y=\left| ax+b \right|$ ta làm như sau:

+ Cách 1: Vẽ $\left( {{C}_{1}} \right)$ là đường thẳng $y=ax+b$ với phần đồ thị sao cho hoành độ $x$ thỏa mãn $ax+b≥0.$ Vẽ $\left( {{C}_{2}} \right)$ là đường thẳng $y=-ax-b$ lấy phần đồ thị sao cho $ax+b<0$. Khi đó $\left( C \right)$ là hợp của hai đồ thị $\left( {{C}_{1}} \right)$ và $\left( {{C}_{2}} \right)$.

+ Cách 2: Vẽ đường thẳng $y=ax+b$ và $y=-ax-b$ rồi xóa đi phần đường thẳng nằm dưới trục hoành, phần đường thẳng nằm trên trục hoành chính là $\left( C \right)$.

Chú ý:

Biết trước đồ thị $\left( C \right):y=f\left( x \right)$ khi đó đồ thị $\left( {{C}_{1}} \right):y=f\left( \left| x \right| \right)$ là gồm phần:

+ Giữ nguyên đồ thị $\left( C \right)$ ở bên phải trục tung.

+ Lấy đối xứng đồ thị $\left( C \right)$ ở bên trái trục tung qua trục tung.

Biết trước đồ thị $\left( C \right):y=f\left( x \right)$ khi đó đồ thị $\left( {{C}_{2}} \right):y=\left| f\left( x \right) \right|$ là gồm phần:

+ Giữ nguyên đồ thị $\left( C \right)$ ở phía trên trục hoành.

+ Lấy đối xứng đồ thị $\left( C \right)$ ở dưới trục hoành qua trục hoành.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 7. Vẽ đồ thị của các hàm số sau:

a) 
$$
y = \left\{ \begin{array}{l}
2x\: khi\:x \ge 0\\
– x\: khi\:x < 0
\end{array} \right.
$$

b) $y = \left| { – 3x + 3} \right|.$

a) Với $x\ge 0$ đồ thị hàm số $y=2x$ là phần đường thẳng đi qua hai điểm $O\left( 0;0 \right)$, $A\left( 1;2 \right)$ nằm bên phải của đường thẳng $x=0$.

Với $x<0$ đồ thị hàm số $y=-x$ là phần đường thẳng đi qua hai điểm $B\left( -1;1 \right)$, $C\left( -2;2 \right)$ nằm bên trái của đường thẳng $x=0$.

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-9.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-9">

b) Vẽ hai đường thẳng $y=-3x+3$ và $y=3x-3$ và lấy phần đường thẳng nằm trên trục hoành.

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-10.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-10">

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 8. Vẽ đồ thị của các hàm số sau:

a) $y = \left| x \right| – 2.$

b) $y = \left| {\left| x \right| – 2} \right|.$

a)

Cách 1: Ta có 
$$
y = \left\{ {\begin{array}{c}
{x – 2\:khi\:x \ge 0}\\
{ – x – 2\:khi\:x < 0}
\end{array}} \right.
$$

Vẽ đường thẳng $y=x-2$ đi qua hai điểm $\text{A}\left( 0;-2 \right)$, $B\left( 2;0 \right)$ và lấy phần đường thẳng bên phải của trục tung.

Vẽ đường thẳng $y=-x-2$ đi qua hai điểm $A\left( 0;-2 \right)$, $C\left( -2;0 \right)$ và lấy phần đường thẳng bên trái của trục tung.

Cách 2: Đường thẳng $d:y=x-2$ đi qua $\text{A}\left( 0;-2 \right)$, $B\left( 2;0 \right)$. Khi đó đồ thị của hàm số $y=\left| x \right|-2$ là phần đường thẳng $d$ nằm bên phải của trục tung và phần đối xứng của nó qua trục tung.

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-11.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-11">

b) Đồ thị $y=\left| \left| x \right|-2 \right|$ là gồm phần:

+ Giữ nguyên đồ thị hàm số $y=\left| x \right|-2$ ở phía trên trục hoành.

+ Lấy đối xứng phần đồ thị hàm số $y=\left| x \right|-2$ ở phía dưới trục hoành và lấy đối xứng qua trục hoành.

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-12.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-12">

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 9. Cho đồ thị $(C):$ $y = 3\left| {x – 2} \right| – \left| {2x – 6} \right|.$

a) Vẽ đồ thị $(C).$

b) Tìm giá trị lớn nhất và nhỏ nhất của hàm số trên với $x \in \left[ { – 3;4} \right].$

a) Ta có 
$$
y = \left\{ \begin{array}{l}
x\:khi\:x \ge 3\\
5x – 12\:khi\:2 < x < 3\\
– x\:khi\:x \le 2
\end{array} \right.
$$

Vẽ đường thẳng $y=x$ đi qua hai điểm $O\left( 0;0 \right)$, $A\left( 1;1 \right)$ và lấy phần đường thẳng bên phải của đường thẳng $x=3.$

Vẽ đường thẳng $y=5x-12$ đi qua hai điểm $B\left( 3;3 \right)$, $C\left( 2;-2 \right)$ và lấy phần đường thẳng nằm giữa của hai đường thẳng $x=2$, $x=3$.

Vẽ đường thẳng $y=-x$ đi qua hai điểm $O\left( 0;0 \right)$, $D\left( -1;-1 \right)$ và lấy phần đường thẳng bên trái của đường thẳng $x=2.$

<img link="data_for_rag/toan10/images/phuong-phap-giai-toan-ham-so-bac-nhat-13.png" alt="phuong-phap-giai-toan-ham-so-bac-nhat-13">

b) Dựa vào đồ thị hàm số ta có:

$\underset{\left[ -3;4 \right]}{\mathop{\text{max}}}y=4$ khi và chỉ khi $x=4.$

$\underset{\left[ -3;4 \right]}{\mathop{\min y}}=-2$ khi và chỉ khi $x=2.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Dạng toán 4. Ứng dụng của hàm số bậc nhất trong chứng minh bất đẳng thức và tìm giá trị nhỏ nhất, lớn nhất.
Phương pháp giải toán: Cho hàm số $f\left( x \right)=ax+b$  và đoạn $\left[ \alpha ;\beta  \right]\subset R$ . Khi đó, đồ thị của hàm số $y = f(x)$ trên $[\alpha ;\beta ]$  là một đoạn thẳng nên ta có một số tính chất:

$\mathop {\max }\limits_{\left[ {\alpha ,\beta } \right]} f\left( x \right) = max\{ f(a);f(b)\} .$

$\mathop {\min }\limits_{\left[ {\alpha ,\beta } \right]} f\left( x \right) = min\{ f(a);f(b)\} .$

$\mathop {\max }\limits_{\left[ {\alpha ,\beta } \right]} \left| {f(x)} \right| = \max \left\{ {\left| {f(\alpha )} \right|;\left| {f(\beta )} \right|} \right\}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 10. Cho hàm số $f\left( x \right)=\left| 2x-m \right|$. Tìm $m$ để giá trị lớn nhất của $f\left( x \right)$ trên $\left[ 1;2 \right]$ đạt giá trị nhỏ nhất.

Dựa vào các nhận xét trên ta thấy $\mathop {\max }\limits_{[1;2]} f(x)$ chỉ có thể đạt được tại $x=1$ hoặc $x=2.$

Như vậy nếu đặt $M = \mathop {\max }\limits_{[1;2]} f(x)$ thì $M \ge f\left( 1 \right) = \left| {2 – m} \right|$ và $M \ge f\left( 2 \right) = \left| {4 – m} \right|.$

Ta có: $M \ge \frac{{f(1) + f(2)}}{2}$ $= \frac{{\left| {2 – m} \right| + \left| {4 – m} \right|}}{2}$ $\ge \frac{{\left| {(2 – m) + (m – 4)} \right|}}{2} = 1.$

Đẳng thức xảy ra khi và chỉ khi 
$$
\left\{ \begin{array}{l}
\left| {2 – m} \right| = \left| {4 – m} \right|\\
(2 – m)(m – 4) \ge 0
\end{array} \right.
$$
 $\Leftrightarrow m = 3.$

Vậy giá trị nhỏ nhất của $M$ là $1$, đạt được chỉ khi $m = 3.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 11. Cho hàm số $y = \left| {\sqrt {2x – {x^2}} – 3m + 4} \right|.$ Tìm $m$ để giá trị lớn nhất của hàm số $y$ là nhỏ nhất.

Gọi $A = \max y.$ Ta đặt $t = \sqrt {2x – {x^2}}$ $\Rightarrow t = \sqrt {1 – {{\left( {x – 1} \right)}^2}}$, do đó $0 \le t \le 1.$

Khi đó hàm số được viết lại là $y = \left| {t – 3m + 4} \right|$ với $t \in \left[ {0;1} \right]$, suy ra:

$A = \mathop {\max }\limits_{[0,1]} \left| {t – 3m + 4} \right|$ $= \max \left\{ {\left| { – 3m + 4} \right|,\left| {5 – 3m + } \right|} \right\}$ $\ge \frac{{\left| { – 3m + 4} \right| + \left| {5 – 3m} \right|}}{2}.$

Áp dụng bất đẳng thức giá trị tuyệt đối ta có: $\left| { – 3m + 4} \right| + \left| {5 – 3m} \right|$ $= \left| {3m – 4} \right| + \left| {5 – 3m} \right| \ge 1.$

Do đó $A\ge \frac{1}{2}$, đẳng thức xảy ra khi $m=\frac{3}{2}$.

Vậy giá trị cần tìm là $m=\frac{3}{2}$.

<!-- chunk:16 level:3 source:https://toanmath.com/2018/09/phuong-phap-giai-toan-ham-so-bac-nhat.html -->
## Ví dụ 12. Cho $a,b,c$ thuộc $\left[ {0;2} \right]$. Chứng minh rằng: $2\left( {a + b + c} \right) – \left( {ab + bc + ca} \right) \le 4.$

Viết bất đẳng thức lại thành $\left( {2 – b – c} \right)a + 2\left( {b + c} \right) – bc – 4 \le 0.$

Xét hàm số bậc nhất: $f\left( a \right) = \left( {2 – b – c} \right)a + 2\left( {b + c} \right) – bc – 4$ với ẩn $a \in \left[ {0;2} \right].$

Ta có: $f\left( 0 \right) = 2\left( {b + c} \right) – bc – 4$ $= – \left( {2 – b} \right)\left( {2 – c} \right) \le 0.$

$f\left( 2 \right) = \left( {2 – b – c} \right)2$ $+ 2\left( {b + c} \right) – bc – 4$ $= – bc \le 0.$

Suy ra $f\left( a \right) \le max\left\{ {f\left( 0 \right);f\left( 2 \right)} \right\} \le 0.$