# Ứng dụng tích phân tính thể tích vật thể

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
Bài viết hướng dẫn phương pháp ứng dụng tích phân để tính thể tích vật thể (gồm vật thể giới hạn bởi các mặt phẳng và vật thể tròn xoay) thông qua lý thuyết, công thức tính, các bước giải toán và ví dụ minh họa có lời giải chi tiết.

Kiến thức cần nắm:
1. Thể tích của vật thể
Giả sử vật thể $T$ được giới hạn bởi hai mặt phẳng song song $(\alpha )$, $(\beta )$. Ta chọn trục $Ox$ sao cho:

$$
\left\{ \begin{array}{l}
Ox \bot (\alpha ) \\
Ox \bot (\beta )
\end{array} \right.
$$
 và giả sử 
$$
\left\{ \begin{array}{l}
Ox \cap (\alpha ) = a\\
Ox \cap (\beta ) = b
\end{array} \right.
$$

Giả sử mặt phẳng $(\gamma ) \cap Ox$ và $(\gamma ) \cap Ox = x\left( {a \le x \le b} \right)$ cắt $T$ theo một thiết diện có diện tích $S\left( x \right)$ (là hàm số liên tục theo biến $x$). Khi đó, thể tích $V$ của vật thể $T$ được cho bởi công thức: $V = \int\limits_a^b {S(x)dx} .$

2. Thể tích của vật thể tròn xoay

a. Cho hàm số $y = f\left( x \right)$ liên tục và không âm trên đoạn $\left[ {a;b} \right]$. Thể tích của vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi $y = f\left( x \right)$, $x = a$, $x = b$, $y = 0$ quay quanh trục $Ox$ được cho bởi công thức: $V = \pi \int\limits_a^b {{y^2}dx}$ $= \pi \int\limits_a^b {{f^2}(x)dx} .$

b. Cho hàm số $x = f\left( y \right)$ liên tục và không âm trên đoạn $\left[ {a;b} \right]$. Tính thể tích vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi $x = f\left( y \right)$, $y = a$, $y = b$, $x = 0$ quay quanh trục $Oy$ được cho bởi công thức: $V = \pi \int\limits_a^b {{x^2}dy}$ $= \pi \int\limits_a^b {{f^2}(y)dy} .$

3. Thể tích khối nón và khối chóp, khối nón cụt và khối cầu

a. Thể tích khối nón (khối chóp) có diện tích đáy bằng $B$ và chiều cao $h$ được cho bởi $V = \frac{1}{3}Bh.$ Thể tích khối nón cụt (khối chóp cụt) có diện tích hai đáy là ${B_1}$, ${B_2}$ và chiều cao $h$ được cho bởi: $V = \frac{1}{3}({B_1} + {\rm{ }}{B_2} + \sqrt {{B_{1.}}.{B_2}} )h.$

b. Thể tích của khối cầu có bán kính $R$ được cho bởi: $V = \frac{4}{3}\pi {R^3}.$

<!-- chunk:1 level:2 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Dạng toán 1: Tính thể tích vật thể
Phương pháp: Thực hiện theo hai bước:

+ Bước 1: Xác định công thức tính diện tích thiết diện $S\left( x \right)$ (hoặc $S\left( y \right)$) thông thường chúng ta gặp thiết diện là các hình cơ bản.

+ Bước 2: Khi đó: $V = \int\limits_a^b {S(x)dx}$ (hoặc $V = \int\limits_a^b {S(y)dy}$).

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 1: Tính thể tích của vật thể:

a. Nằm giữa hai mặt phẳng $x = 0$ và $x = \frac{\pi }{2}$, biết rằng thiết diện của vật thể bị cắt bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ $\left( {0 \le x \le \frac{\pi }{2}} \right)$ là một hình vuông cạnh $\sqrt {{{\sin }^3}x} .$

b. Nằm giữa hai mặt phẳng $x = 1$ và $x = 4$, biết rằng thiết diện của vật thể bị cắt bởi mặt phẳng vuông góc với trục $Ox$ tại điểm có hoành độ $x$ $\left( {1 \le x \le 4} \right)$ là một tam giác đều cạnh là $\sqrt x – 1.$

a. Diện tích thiết diện $S\left( x \right)$ được cho bởi:

$S\left( x \right) = {\left( {\sqrt {{{\sin }^3}x} } \right)^2}$ $= {\rm{ }}si{n^3}x$ $= \frac{1}{4}\left( {3\sin x – \sin 3x} \right) .$

Khi đó, thể tích vật thể được cho bởi:

$V = \int\limits_{ – 1}^1 {S(x)dx}$ $= \frac{1}{4}\int\limits_0^{\pi /2} {\left( {3\sin x – \sin 3x} \right)dx}$ 
$$
= \frac{1}{4}\left( { – 3\cos x + \frac{1}{3}\cos 3x} \right)\left| \begin{array}{l}
\pi /2\\
0
\end{array} \right.
$$
 $= \frac{2}{3}.$

b. Diện tích thiết diện $S\left( x \right)$ được cho bởi:

$S\left( x \right) = \frac{{\sqrt 3 }}{4}{\left( {\sqrt x – 1} \right)^2}$ $= \frac{{\sqrt 3 }}{4}\left( {x – 2\sqrt x + 1} \right).$

Khi đó, thể tích vật thể được cho bởi:

$V = \int\limits_{ – 1}^1 {S(x)dx}$ $= \frac{{\sqrt 3 }}{4}\int\limits_1^4 {\left( {x – 2\sqrt x + 1} \right)dx}$ $= \frac{{\sqrt 3 }}{4}\left( {\frac{1}{2}{x^2} – \frac{4}{3}{x^{\frac{3}{2}}} + x} \right)\left| {_1^4} \right.$ $= \frac{{7\sqrt 3 }}{{24}}.$

Nhận xét: Như vậy, để tính các thể tích vật thể trên:

+ Ở câu 1.a vì thiết diện là hình vuông (giả sử cạnh bằng $a$) nên ta có ngay $S = {a^2}$.

+ Ở câu 1.b vì thiết diện là tam giác đều (giả sử cạnh bằng $a$) nên ta có ngay $S = \frac{{{a^2}\sqrt 3 }}{4}.$

[ads]

<!-- chunk:3 level:2 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Dạng toán 2: Tính thể tích vật thể tròn xoay dạng 1
Phương pháp: Ta có hai dạng sau:

+ Dạng 1: Công thức tính thể tích vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi $y = f\left( x \right)$, $x = a$, $x = b$, $y = 0$ khi quay quanh trục $Ox$: $V = \pi \int\limits_a^b {{y^2}dx}$ $= \pi \int\limits_a^b {{f^2}(x)dx} .$

+ Dạng 2: Công thức tính thể tích vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi $x = f\left( y \right)$, $y = a$, $y = b$, $x = 0$ khi quay quanh trục $Oy$: $V = \pi \int\limits_a^b {{x^2}dy}$ $= \pi \int\limits_a^b {{f^2}(y)dy} .$

Chú ý: Trong một số trường hợp chúng ta cần tìm cận $a$, $b$ thông qua việc thiết lập điều kiện không âm cho hàm số $f\left( x \right)$ (hoặc $f(y)$).

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 2: Tính thể tích khối tròn xoay tạo thành khi:

a. Quay quanh trục hoành một hình phẳng giới hạn bởi đồ thị hàm số $y = {e^x}$, trục hoành và hai đường thẳng $x = 0$, $x = 3.$

b. Quay quanh trục tung một hình phẳng giới hạn bởi đồ thị hàm số $y = 3 – {x^2}$, trục tung và đường thẳng $y = 1.$

a. Thể tích vật thể được cho bởi: $V = \pi \int\limits_0^3 {{y^2}dx}$ $= \pi \int\limits_0^3 {{e^{2x}}dx}$ $= \frac{\pi }{2}{e^{2x}}\left| {_0^3} \right.$ $= \frac{\pi }{2}({e^6} – 1).$

b. Biến đổi hàm số về dạng: $y = 3 – {x^2}$ $\Leftrightarrow {x^2} = 3 – y$ (cần có điều kiện $3 – y \ge 0$ $\Leftrightarrow y \le 3$).

Khi đó, thể tích vật thể được cho bởi: $V = \pi \int\limits_1^3 {{x^2}dy}$ $= \pi \int\limits_1^3 {(3 – y)dy}$ $= \pi \left( {3y – \frac{{{y^2}}}{2}} \right)\left| {_1^3} \right.$ $= 2\pi .$

Nhận xét: Như vậy, để tính các thể tích khối tròn xoay trên:

+ Ở câu 2.a chúng ta sử dụng ngay công thức trong dạng 1.

+ Ở câu 2.b chúng ta cần thực thêm công việc biến đổi hàm số về dạng $x = f\left( y \right)$ và ở đây nhờ điều kiện có nghĩa của $y$ chúng ta nhận được cận $y = 3.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 3: Tính thể tích của khối tròn xoay tạo nên khi ta quay hình $H$ quanh trục $Ox$, với:

a. $H = {\rm{\{ }}y = 0;y = \sqrt {1 + {{\cos }^4}x + {{\sin }^4}x} ;$ $x = \frac{\pi }{2};x = \pi {\rm{\} }}.$

b. $H = {\rm{\{ }}y = 0;y = \sqrt {{{\cos }^6}x + {{\sin }^6}x} ;$ $x = 0;x = \frac{\pi }{2}{\rm{\} }}.$

a. Thể tích vật tròn xoay cần tính được cho bởi:

$V = \pi \int\limits_{\pi /2}^\pi {(1 + {{\cos }^4}x + {{\sin }^4}x)} dx$ $= \pi \int\limits_{\pi /2}^\pi {(\frac{{7 – \cos 4x}}{4})dx}$ 
$$
= \pi \left( {\frac{7}{4}x – \frac{1}{{16}}\sin 4x} \right)\left| \begin{array}{l}
\pi \\
\pi /2
\end{array} \right.
$$
 $= \frac{7}{8}{\pi ^2}$ (đvtt).

b. Thể tích vật thể tròn xoay cần tính là:

$V = \pi \int\limits_0^{\pi /2} {({{\cos }^6}x} + {\sin ^6}x)dx$ $= \pi \int\limits_0^{\pi /2} {(1 – \frac{3}{4}{{\sin }^2}2x)dx}$ $= \pi \int\limits_0^{\pi /2} {(\frac{5}{8} + \frac{3}{8}\cos 4x)dx}$ 
$$
= \pi \left( {\frac{5}{8}x + \frac{3}{{32}}\sin 4x} \right)\left| \begin{array}{l}
\frac{\pi }{2}\\
0
\end{array} \right.
$$
 $= \frac{{5{\pi ^2}}}{{16}}$ (đvtt).

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 4: Tính thể tích của khối tròn xoay tạo nên khi ta quay hình $H$ quanh trục $Ox$, với:

a. $H = \left\{ {y = 3ax – {x^2}\left( {a > 0} \right),y = 0} \right\}.$

b. $H = \left\{ {y = xlnx;y = 0;x = 1;x = e} \right\}.$

a. Phương trình hoành độ giao điểm của $\left( P \right)$ và $Ox$ là:

$3ax – {x^2} = 0$ $\Leftrightarrow x = 0$ hoặc $x = 3a.$

Khi đó, thể tích cần xác định được cho bởi:

$V = \pi \int\limits_0^{3a} {{{(3ax – {x^2})}^2}dx}$ $= \pi \int\limits_0^{3a} {({x^4} – 6a{x^3} + 9{a^2}{x^2})dx}$ 
$$
= \pi \left( {\frac{1}{5}{x^5} – \frac{{3a}}{2}{x^4} + 3{a^2}{x^3}} \right)\left| \begin{array}{l}
3a\\
0
\end{array} \right.
$$
 $= \frac{{81{a^5}\pi }}{{10}}$ (đvtt).

b. Thể tích vật thể tròn xoay cần tính là:

$V = \pi \int\limits_1^e {{{(x\ln x)}^2}} dx$ $= \pi \int\limits_1^e {{x^2}{{\ln }^2}x} dx.$

Để tính tích phân trên ta sử dụng phương pháp tích phân từng phần, đặt:

$$
\left\{ \begin{array}{l}
u = {\ln ^2}x\\
dv = {x^2}dx
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
du = \frac{2}{x}\ln xdx\\
v = \frac{1}{3}{x^3}
\end{array} \right.
$$

Khi đó: 
$$
V = \pi \left( {\frac{1}{3}{x^3}{{\ln }^2}x} \right)\left| \begin{array}{l}
e\\
1
\end{array} \right.
$$
 $– \frac{{2\pi }}{3}\int\limits_1^e {{x^2}\ln x} dx$ $= \frac{{\pi {e^3}}}{3} – \frac{{2\pi }}{3}\underbrace {\int\limits_1^e {{x^2}\ln x} dx}_I$ $(1).$

Xét tích phân $I$, đặt:

$$
\left\{ \begin{array}{l}
u = \ln x\\
dv = {x^2}dx
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
du = \frac{1}{x}dx\\
v = \frac{1}{3}{x^3}
\end{array} \right.
$$

Khi đó: $I = \frac{1}{3}{x^3}lnx\left| {_1^e} \right. – \frac{1}{3} \int\limits_1^e {{x^2}dx}$ $= \frac{{{e^3}}}{3} – \frac{1}{9}{x^3}\left| {_1^e} \right.$ $= \frac{{2{e^3}}}{9} + \frac{1}{9}$ $(2).$

Thay $(2)$ vào $(1)$, ta được: $V = \frac{{\pi (5{e^3} – 2)}}{{27}}$ (đvtt).

<!-- chunk:7 level:2 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Dạng toán 3: Tính thể tích vật thể tròn xoay dạng 2

Phương pháp: Ta có hai dạng sau:

+ Dạng 1: Công thức tính thể tích vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi $y = f\left( x \right)$, $y = g\left( x \right)$, $x = a$, $x = b$ quay quanh trục $Ox$: $V = \pi \int\limits_a^b {\left| {{f^2}(x) – {g^2}(x)} \right|dx} .$

+ Dạng 2: Công thức tính thể tích vật thể tròn xoay sinh bởi miền $\left( D \right)$ giới hạn bởi  $x = f\left( y \right)$, $x = g\left( y \right)$, $y = a$, $y = b$ quay quanh trục $Oy$: $V = \pi \int\limits_a^b {\left| {{f^2}(y) – {g^2}(y)} \right|dy} .$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 5: Tính thể tích khối tròn xoay tạo thành khi:

a. Quay quanh trục hoành một hình phẳng giới hạn bởi đồ thị hai hàm số $y = {x^2}$ và $y = 2 – {x^2}.$

b. Quay quanh trục tung một hình phẳng giới hạn bởi đồ thị hai hàm số $y = x$ và $y = 2 – {x^2}.$

a. Hoành độ giao điểm là nghiệm của phương trình:

${x^2} = 2 – {x^2}$ $\Leftrightarrow {x^2} = 1$ $\Leftrightarrow x = \pm 1.$

Thể tích vật tròn xoay cần tính là:

$V = \pi \int\limits_{ – 1}^1 {\left| {{x^4} – {{(2 – {x^2})}^2}} \right|dx}$ $= \pi \int\limits_{ – 1}^1 {\left| {4{x^2} – 4} \right|dx}$ $= 4\pi \int\limits_{ – 1}^1 {(1 – {x^2})dx}$ $= 4\pi \left( {x – \frac{{{x^3}}}{3}} \right)\left| {_{ – 1}^1} \right.$ $= \frac{{16\pi }}{3}.$

b. Hoành độ giao điểm là nghiệm của phương trình:

$x = 2 – {x^2}$ $\Leftrightarrow {x^2} + x – 2 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 1  \Rightarrow  y = 1\\
x = -2  \Rightarrow  y = -2
\end{array} \right.
$$

Thể tích vật thể được cho bởi:

$V = \pi \int\limits_{ – 2}^1 {\left| {{y^2} – \left( {2 – y} \right)} \right|dy}$ $= \frac{9}{2}\pi .$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 6: Cho hình tròn $\left( C \right)$ tâm $I\left( {0;2} \right)$, bán kính $R = 1$. Tính thể tích khối tròn xoay tạo thành khi:

a. Quay $\left( C \right)$ quanh trục $Ox$.

b. Quay $\left( C \right)$ quanh trục $Oy$.

Đường tròn $(C)$ có phương trình: $\left( C \right):{x^2} + {(y – 2)^2} = 1.$

<img link="data_for_rag/toan12/images/ung-dung-tich-phan-tinh-the-tich-vat-the-1.png" alt="ung-dung-tich-phan-tinh-the-tich-vat-the-1">

a. Ta có:

Ta chia đường tròn $(C)$ thành $2$ đường cong như sau:

+ Nửa $\left( C \right)$ ở trên ứng với $2 \le y \le 3$ có phương trình: $y = {f_1}\left( x \right) = 2 + \sqrt {1 – {x^2}}$ với $x \in \left[ { – 1;{\rm{ }}1} \right]$.

+ Nửa $\left( C \right)$ ở dưới  ứng với $1 \le y \le 2$ có phương trình: $y = {f_2}\left( x \right) = 2 – \sqrt {1 – {x^2}}$ với $x \in \left[ { – 1;{\rm{ }}1} \right]$.

Khi đó, thể tích vật thể tròn xoay cần tính được sinh bởi hình tròn $(C)$ giới hạn bởi các đường: $y = {f_1}\left( x \right) = 2 + \sqrt {1 – {x^2}}$, $y = {f_2}\left( x \right) = 2 – \sqrt {1 – {x^2}}$, $x = -1$, $x = 1$ quay quanh $Ox$ được tính theo công thức: $V = \pi \int\limits_{ – 1}^1 {\left| {f_1^2\left( x \right) – f_2^2\left( x \right)} \right|} dx$ $= 8\pi \int\limits_{ – 1}^1 {\sqrt {1 – {x^2}} } dx$ $= 4{\pi ^2}.$

b. Khi quay $\left( C \right)$ quanh trục $Oy$ ta nhận được khối tròn xoay chính là hình cầu bán kính $R = 1$, do đó: $V = \frac{4}{3}\pi {R^3}$ $= \frac{4}{3}\pi .$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-the-tich-vat-the.html -->
## Ví dụ 7: Tính thể tích vật thể tạo bởi hình elip $\left( E \right):\frac{{{{\left( {x – 4} \right)}^2}}}{4} + \frac{{{y^2}}}{{16}} \le 1$ quay quanh trục $Oy.$

Elip $\left( E \right)$ có tâm $I\left( {4,0} \right)$, trục lớn có độ dài $2a = 8$, trục nhỏ có độ dài $2b = 4.$

<img link="data_for_rag/toan12/images/ung-dung-tich-phan-tinh-the-tich-vat-the-2.png" alt="ung-dung-tich-phan-tinh-the-tich-vat-the-2">

Ta chia đường biên của elip $(E)$ thành $2$ đường cong như sau:

+ Nửa biên $\left( E \right)$ ứng với $2 \le x \le 4$ có phương trình: $x = {f_1}\left( y \right) = 4 – 2\sqrt {1 – \frac{{{y^2}}}{{16}}}$ với $y \in \left[ { – 4;4} \right].$

+ Nửa biên $\left( E \right)$ ứng với $4 \le x \le 6$ có phương trình: $x = {f_2}\left( y \right) = 4 + 2\sqrt {1 – \frac{{{y^2}}}{{16}}}$ với $y \in \left[ { – 4;4} \right].$

Thể tích vật thể tròn xoay cần tính được sinh bởi miền $E$ giới hạn bởi các đường: $x = {f_1}\left( y \right) = 4 – 2\sqrt {1 – \frac{{{y^2}}}{{16}}}$, $x = {f_2}\left( y \right) = 4 + 2\sqrt {1 – \frac{{{y^2}}}{{16}}}$, $y = -4$, $y = 4$ quay quanh trục $Oy$ được tính theo công thức:

$V = \pi \int\limits_{ – 4}^4 {\left( {f_2^2(y) – f_1^2(y)} \right)} dy$ $= 32\pi \int\limits_{ – 4}^4 {\sqrt {1 – \frac{{{y^2}}}{{16}}} } dy$ $= 64{\pi ^2}.$