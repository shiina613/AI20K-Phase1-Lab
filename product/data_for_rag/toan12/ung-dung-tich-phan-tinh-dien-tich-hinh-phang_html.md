# Ứng dụng tích phân tính diện tích hình phẳng

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
Bài viết hướng dẫn ứng dụng tích phân tính diện tích hình phẳng thông qua tổng hợp lý thuyết, phân dạng, các bước giải toán và các ví dụ minh họa có lời giải chi tiết. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu nguyên hàm, tích phân và ứng dụng đăng tải trên TOANMATH.com.

Lý thuyết cần nắm:

1. Diện tích của hình tròn và của hình elíp

a. Hình tròn bán kính $R$ có diện tích $S = \pi {R^2}.$

b. Hình elíp $\left( E \right)$: $\frac{{{x^2}}}{{{a^2}}} + \frac{{{y^2}}}{{{b^2}}} = 1$ có diện tích $S = \pi ab.$

2. Tính diện tích hình phẳng giới hạn bởi các đường cong

a. Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f\left( x \right)$ ($f\left( x \right)$ liên tục trên đoạn $\left[ {a;b} \right]$), trục $Ox$ và hai đường thẳng $x = a$ và $x = b$ được cho bởi công thức: $S = \int\limits_a^b {\left| {f(x)} \right|dx} .$

b. Diện tích hình phẳng giới hạn bởi hai đường thẳng $x = a$, $x = b$ và đồ thị của hai hàm số $y = {f_1}\left( x \right)$ và $y = {f_2}\left( x \right)$ (${f_1}\left( x \right)$ và ${f_2}\left( x \right)$ liên tục trên đoạn $\left[ {a;b} \right]$) được cho bởi công thức: $S = \int\limits_a^b {\left| {{f_1}(x) – {f_2}(x)} \right|dx} .$

<!-- chunk:1 level:2 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Dạng 1: Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $y = f\left( x \right)$ (liên tục trên đoạn $\left[ {a;b} \right]$), trục hoành và hai đường thẳng $x = a$, $x = b$ và trục $Ox$
+ Bước 1: Gọi $S$ là diện tích cần xác định, ta có: $S = \int\limits_a^b {\left| {f(x)} \right|dx} .$

+ Bước 2: Xét dấu biểu thức $f\left( x \right)$ trên $\left[ {a;b} \right]$. Từ đó phân được đoạn $\left[ {a;b} \right]$ thành các đoạn nhỏ, giả sử: $\left[ {a;b} \right]$ $= \left[ {a;{c_1}} \right] \cup \left[ {{c_1};{c_2}} \right] \cup … \cup \left[ {{c_k};b} \right]$ mà trên mỗi đoạn $f\left( x \right)$ chỉ có một dấu.

+ Bước 3: Khi đó: $S = \int\limits_a^{{c_1}} {\left| {f(x)} \right|} dx + \int\limits_{{c_1}}^{{c_2}} {\left| {f(x)} \right|} dx$ $+ … + \int\limits_{{c_k}}^b {\left| {f(x)} \right|} dx.$

Chú ý: Nếu bài toán phát biểu dưới dạng: “Tính diện tích hình phẳng giới hạn bởi đồ thị hàm số $x = {\rm{ }}f\left( y \right)$ (liên tục trên đoạn $\left[ {a;b} \right]$) hai đường thẳng $y = a$, $y = b$ và trục $Oy$”, khi đó công thức tính diện tích là: $S = \int\limits_a^b {\left| {f(y)} \right|dy} .$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Ví dụ 1: Tính diện tích hình phẳng giới hạn bởi:

a. Đồ thị hàm số $y = cosx + 1$, trục hoành và hai đường thẳng $x = 0$ và $x = \frac{{2\pi }}{3}.$

b. Đồ thị hàm số $y = {x^3} – 1$, trục hoành, trục tung và đường thẳng $x = 2.$

a. Ta có: $S = \int\limits_0^{2\pi /3} {\left| {co{\mathop{\rm s}\nolimits} x + 1} \right|dx}$ $= \int\limits_0^{2\pi /3} {(co{\mathop{\rm s}\nolimits} x + 1)dx}$ $= \left( {\sin x + x} \right)\left| {_0^{2\pi /3}} \right.$ $= \frac{{\sqrt 3 }}{2} + \frac{{2\pi }}{3}.$

b. Ta có: $S = \int\limits_0^2 {\left| {{x^3} – 1} \right|dx} .$

Xét hàm số: $f\left( x \right) = {x^3} – 1$ trên đoạn $\left[ {0;2} \right]$, ta có: ${x^3} – 1 = 0$ $\Leftrightarrow (x – 1)\left( {{x^2} + {\rm{ }}x{\rm{ }} + {\rm{ }}1} \right) = 0$ $\Leftrightarrow x{\rm{ }} = {\rm{ }}1.$

Bảng xét dấu:

<img link="data_for_rag/toan12/images/ung-dung-tich-phan-tinh-dien-tich-hinh-phang-1.png" alt="ung-dung-tich-phan-tinh-dien-tich-hinh-phang-1">

Khi đó: $S = \int\limits_0^1 {\left| {{x^3} – 1} \right|dx} + \int\limits_1^2 {\left| {{x^3} – 1} \right|dx}$ $= \int\limits_0^1 {\left( {1 – {x^3}} \right)dx} + \int\limits_1^2 {\left( {{x^3} – 1} \right)dx}$ $= \left( {x – \frac{{{x^4}}}{4}} \right)\left| {_0^1} \right. + \left( {\frac{{{x^4}}}{4} – x} \right)\left| {_1^2} \right. = \frac{7}{2}.$

Nhận xét: Như vậy, để tính các diện tích hình phẳng trên:

+ Ở câu 1.a chúng ta chỉ việc sử dụng công thức cùng với nhận xét $cosx + 1 \ge 0$ để phá dấu trị tuyệt đối. Từ đó, nhận được giá trị của tích phân.

+ Ở câu 1.b chúng ta cần xét dấu đa thức ${x^3} – 1$ trên đoạn $\left[ {0;2} \right]$, để từ đó tách tích phân $S$ thành các tích phân nhỏ mà trên đó biểu thức ${x^3} – 1$ không âm hoặc không dương.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Ví dụ 2: Tính diện tích hình phẳng giới hạn bởi:

a. Đồ thị hàm số $y = – {x^2} + 3x – 2$ và trục hoành.

b. Đồ thị hàm số $y = {x^3} – 2{x^2} – x + 2$ và trục hoành.

a. Ta có hoành độ giao điểm của đồ thị hàm số $y = – {x^2} + 3x – 2$ và trục hoành là:

$– {x^2} + 3x – 2 = 0$ $\Leftrightarrow x = 1$ hoặc $x = 2.$

Khi đó: $S = \int\limits_1^2 {\left| { – {x^2} + 3x – 2} \right|dx}$ $= \int\limits_1^2 {\left( { – {x^2} + 3x – 2} \right)dx}$ $= \left. {\left( { – \frac{1}{3}{x^3} + \frac{3}{2}{x^2} – 2x} \right)} \right|_1^2$ $= \frac{1}{6}.$

b. Ta có hoành độ giao điểm của đồ thị hàm số $y = {x^2} – 2x$ và trục hoành là:

${x^3} – 2{x^2} – x + 2{\rm{ }} = 0$ $\Leftrightarrow (x – 1)({x^2} – x – 2) = 0$ $\Leftrightarrow x = \pm 1$ hoặc $x = 2.$

Khi đó: $S = \int\limits_{ – 1}^2 {\left| {{x^3} – 2{x^2} – x + 2} \right|dx}$ $= \int\limits_{ – 1}^1 {\left| {{x^3} – 2{x^2} – x + 2} \right|dx}$ $+ \int\limits_1^2 {\left| {{x^3} – 2{x^2} – x + 2} \right|dx}$

$= \int\limits_{ – 1}^1 {\left( {{x^3} – 2{x^2} – x + 2} \right)dx}$ $+ \int\limits_1^2 {\left( { – {x^3} + 2{x^2} + x – 2} \right)dx}$

$= \left. {\left( {\frac{1}{4}{x^4} – \frac{2}{3}{x^3} – \frac{1}{2}{x^2} + 2x} \right)} \right|_{ – 1}^1$ $+ \left. {\left( { – \frac{1}{4}{x^4} + \frac{2}{3}{x^3} + \frac{1}{2}{x^2} – 2x} \right)} \right|_1^2$ $= 3.$

Nhận xét: Như vậy, để tính các diện tích hình phẳng trên chúng ta đều cần tìm được hai cận $a$, $b$ của tích phân và:

+ Ở câu 2.a vì phương trình hoành độ chỉ có hai nghiệm nên hàm số dưới dấu tích phân chỉ có một dấu.

+ Ở câu 2.b vì phương trình hoành độ có ba nghiệm nên tích phân $S$ cần được tách thành hai tích phân nhỏ.

[ads]

<!-- chunk:4 level:2 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Dạng toán 2: Tính diện tích hình phẳng giới hạn bởi đồ thị hai hàm số $y = f\left( x \right)$, $y = g\left( x \right)$ (liên tục trên đoạn $\left[ {a;b} \right]$) hai đường thẳng $x = a$, $x = b$

+ Bước 1: Gọi $S$ là diện tích cần xác định, ta có: $S = \int\limits_a^b {\left| {f(x) – g(x)} \right|dx} .$

+ Bước 2: Xét dấu biểu thức $f\left( x \right) – g\left( x \right)$ trên $\left[ {a;b} \right]$. Từ đó phân được đoạn $\left[ {a,b} \right]$ thành các đoạn nhỏ, giả sử: $\left[ {a;b} \right]$ $= \left[ {a;{c_1}} \right] \cup \left[ {{c_1};{c_2}} \right] \cup … \cup \left[ {{c_k};b} \right]$ mà trên mỗi đoạn $f\left( x \right) – g\left( x \right)$ chỉ có một dấu.

+ Bước 3: Khi đó: $S = I = \int\limits_a^{{c_1}} {\left| {f(x) – g(x)} \right|} dx +$ $… + \int\limits_{{c_k}}^b {\left| {f(x) – g(x)} \right|} dx .$

Chú ý: Nếu bài toán phát biểu dưới dạng: “Tính diện tích hình phẳng giới hạn bởi  đồ thị hai hàm số $x = {f_1}\left( y \right)$ và $x = {f_2}\left( y \right)$ (liên tục trên đoạn $\left[ {a;b} \right]$) và hai đường thẳng $y = a$, $y = b$ và trục $Oy$”, khi đó công thức tính diện tích là: $S = \int\limits_a^b {\left| {{f_1}(y) – {f_2}(y)} \right|dy} .$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Ví dụ 3: Tính diện tích hình phẳng giới hạn bởi:

a. Đồ thị các hàm số $y = 4-{x^2}$, $y = -x + 2.$

b. Đồ thị các hàm số $y = lnx$, $y = -lnx$ và $x = e.$

a. Hoành độ giao điểm của hai đồ thị là nghiệm của phương trình:

$4–{x^2} = –x + 2$ $\Leftrightarrow {x^2} – x – 2 = 0$ $\Leftrightarrow x = – 1$ hoặc $x = 2.$

Khi đó: $S = \int\limits_{ – 1}^2 {\left| {{x^2} – x – 2} \right|dx}$ $= – \int\limits_{ – 1}^2 {\left( {{x^2} – x – 2} \right)dx}$ $= – \left. {\left( {\frac{1}{3}{x^3} – \frac{1}{2}{x^2} – 2x} \right)} \right|_{ – 1}^2$ $= \frac{{27}}{6}.$

b. Hoành độ giao điểm của hai đồ thị là nghiệm của phương trình:

$lnx = -lnx$ $\Leftrightarrow 2lnx = 0$ $\Leftrightarrow lnx = 0$ $\Leftrightarrow x = 1.$

Khi đó: $S = \int\limits_1^e {\left| {\ln x + \ln x} \right|dx}$ $= 2\int\limits_1^e {\ln x.dx} .$

Đặt: 
$$
\left\{ \begin{array}{l}
u = \ln x\\
dv = dx
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
du = \frac{{dx}}{x}\\
v = x
\end{array} \right.
$$
 $\Rightarrow S = 2\left( {\left. {x.\ln x} \right|_1^e – \int\limits_1^e {dx} } \right)$ $= 2\left( {e – \left. x \right|_1^e} \right)$ $= 2.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/ung-dung-tich-phan-tinh-dien-tich-hinh-phang.html -->
## Ví dụ 4: Cho hàm số: $\left( C \right)$: $y = \frac{{{x^2}}}{{{x^2} + 1}}$. Tìm $b$ sao cho diện tích hình phẳng giới hạn bởi $\left( C \right)$ và các đường thẳng $y = 1$, $x = 0$, $x = b$ bằng $\frac{\pi }{4}.$

Gọi $S$ là diện tích cần xác định, ta có:

$S = \int\limits_0^b | \frac{{{{\rm{x}}^{\rm{2}}}}}{{{{\rm{x}}^{\rm{2}}} + 1}} – 1|dx$ $= \frac{\pi }{4}$ $\Leftrightarrow \int\limits_{\rm{0}}^b | \frac{{{\rm{x}}{{\rm{ }}^{\rm{2}}} – {x^2} – 1}}{{{\rm{x}}{{\rm{ }}^{\rm{2}}} + 1}}|dx$ $= \frac{\pi }{4}$ $\Leftrightarrow \left| {\int\limits_0^b {\frac{{dx}}{{{{\rm{x}}^{\rm{2}}} + 1}}} } \right|$ $= \frac{\pi }{4}$ $(1).$

Đặt $x = tant$, $– \frac{\pi }{2} < t < \frac{\pi }{2}$ $\Rightarrow dx = \frac{{dt}}{{{{\cos }^2}t}}$ $= \left( {1 + ta{n^2}t} \right)dt .$

Đổi cận: Với $x = 0$ thì $t = 0$, với $x = b$ thì $t = \alpha$ (với $tan\alpha = b$ và $– \frac{\pi }{2} < \alpha < \frac{\pi }{2}$).

Khi đó: $(1) \Leftrightarrow \left| {\int\limits_0^\alpha {dt} } \right|$ $= \frac{\pi }{4}$ 
$$
\Leftrightarrow \left| t \right|\left| \begin{array}{l}
\alpha \\
0
\end{array} \right.
$$
 $= \frac{\pi }{4}$ $\Leftrightarrow \left| \alpha \right| = \frac{\pi }{4}$ $\Leftrightarrow b = \pm 1.$