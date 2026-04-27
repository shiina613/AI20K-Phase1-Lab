# Chứng minh phương trình có nghiệm dựa vào tính liên tục của hàm số %

<!-- chunk:0 level:0 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp chứng minh phương trình có nghiệm bằng cách sử dụng tính liên tục của hàm số. Kiến thức và các ví dụ minh học có trong bài viết được tham khảo từ các tài liệu chuyên đề giới hạn đăng tải trên TOANMATH.com.

Phương pháp:

Để chứng minh phương trình có nghiệm bằng cách sử dụng tính liên tục của hàm số, ta thực hiện theo các bước sau:

+ Bước 1: Biến đổi phương trình về dạng $f\left( x \right) = 0.$

+ Bước 2: Tìm hai số $a$ và $b$ $(a<b)$ sao cho $f\left( a \right).f\left( b \right) < 0.$

+ Bước 3: Chứng minh hàm số $f(x)$ liên tục trên đoạn $\left[ {a;b} \right].$

Từ đó suy ra phương trình $f\left( x \right) = 0$ có ít nhất một nghiệm thuộc $\left( {a;b} \right).$

Chú ý:

+ Nếu  $f\left( a \right).f\left( b \right) \le 0$ thì phương trình có ít nhất một nghiệm thuộc $\left[ {a;b} \right].$

+ Nếu hàm số $f(x)$ liên tục trên $\left[ {a; + \infty } \right)$ và có $f\left( a \right).\mathop {\lim }\limits_{x \to + \infty } f\left( x \right) < 0$ thì phương trình $f\left( x \right) = 0$ có ít nhất một nghiệm thuộc $\left( {a; + \infty } \right).$

+ Nếu hàm số $f(x)$ liên tục trên $\left( { – \infty ;a} \right]$ và có $f\left( a \right).\mathop {\lim }\limits_{x \to – \infty } f\left( x \right) < 0$ thì phương trình $f\left( x \right) = 0$ có ít nhất một nghiệm thuộc $\left( { – \infty ;a} \right).$

<!-- chunk:1 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 1: Chứng minh rằng phương trình $4{x^3} – 8{x^2} + 1 = 0$ có nghiệm trong khoảng $\left( { – 1;2} \right).$

Hàm số $f\left( x \right) = 4{x^3} – 8{x^2} + 1$ liên tục trên $R.$

Ta có: $f\left( { – 1} \right) = – 11$, $f\left( 2 \right) = 1$ nên $f\left( { – 1} \right).f\left( 2 \right) < 0.$

Do đó theo tính chất hàm số liên tục, phương trình đã cho có ít nhất một nghiệm thuộc khoảng $\left( { – 1;2} \right).$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 2: Chứng minh phương trình $4{x^4} + 2{x^2} – x – 3 = 0$ có ít nhất $2$ nghiệm thuộc khoảng $\left( { – 1;1} \right).$

Đặt $f\left( x \right) = 4{x^4} + 2{x^2} – x – 3$ thì $f\left( x \right)$ liên tục trên $R.$

Ta có:

$f\left( { – 1} \right) = 4 + 2 + 1 – 3 = 4.$

$f\left( 0 \right) = – 3.$

$f\left( 1 \right) = 2.$

Vì $f\left( { – 1} \right).f\left( 0 \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( { – 1;0} \right).$

Vì $f\left( 1 \right).f\left( 0 \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( {0;1} \right).$

Mà hai khoảng $\left( { – 1;0} \right)$, $\left( {0;1} \right)$ không giao nhau. Từ đó suy ra phương trình đã cho có ít nhất $2$ nghiệm thuộc khoảng $\left( { – 1;1} \right).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 3: Chứng minh phương trình ${x^5} – 5{x^3} + 4x – 1 = 0$ có đúng năm nghiệm.

Đặt $f\left( x \right) = {x^5} – 5{x^3} + 4x – 1$ thì $f\left( x \right)$ liên tục trên $R.$

Ta có $f\left( x \right) = x\left( {{x^4} – 5{x^2} + 4} \right) – 1$ $= \left( {x – 2} \right)\left( {x – 1} \right)x\left( {x + 1} \right)\left( {x + 2} \right) – 1.$

$f\left( { – 2} \right) = – 1.$

$f\left( { – \frac{3}{2}} \right) = \frac{{105}}{{32}} – 1 > 0.$

$f\left( { – 1} \right) = – 1 < 0.$

$f\left( {\frac{1}{2}} \right) = \frac{{45}}{{32}} – 1 > 0.$

$f\left( 1 \right) = – 1 < 0.$

$f\left( 3 \right) = 120 – 1 = 119 > 0.$

Vì $f\left( { – 2} \right).f\left( { – \frac{3}{2}} \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( { – 2; – \frac{3}{2}} \right).$

Vì $f\left( { – \frac{3}{2}} \right).f\left( { – 1} \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( { – \frac{3}{2}; – 1} \right).$

Vì $f\left( { – 1} \right).f\left( {\frac{1}{2}} \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( { – 1;\frac{1}{2}} \right).$

Vì $f\left( {\frac{1}{2}} \right).f\left( 1 \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( {\frac{1}{2};1} \right).$

Vì $f\left( 1 \right).f\left( 3 \right) < 0$ nên phương trình có nghiệm thuộc khoảng $\left( {1;3} \right).$

Do các khoảng $\left( { – 2; – \frac{3}{2}} \right)$, $\left( { – \frac{3}{2}; – 1} \right)$, $\left( { – 1;\frac{1}{2}} \right)$, $\left( {\frac{1}{2};1} \right)$, $\left( {1;3} \right)$ không giao nhau nên phương trình có ít nhất $5$ nghiệm.

Mà phương trình bậc $5$ có không quá $5$ nghiệm suy ra phương trình đã cho có đúng $5$ nghiệm.

[ads]

<!-- chunk:4 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 4: Chứng minh rằng nếu $2a + 3b + 6c = 0$ thì phương trình $a{\tan ^2}x + b\tan x + c = 0$ có ít nhất một nghiệm thuộc khoảng $\left( {k\pi ;\frac{\pi }{4} + k\pi } \right)$, $k \in Z.$

Đặt $t = \tan x$, vì $x \in \left( {k\pi ;\frac{\pi }{4} + k\pi } \right)$ nên $t \in \left( {0;1} \right)$, phương trình đã cho trở thành: $a{t^2} + bt + c = 0$ $\left( * \right)$ với $t \in \left( {0;1} \right).$

Đặt $f\left( t \right) = a{t^2} + bt + c$ thì $f\left( t \right)$ liên tục trên $R.$

Ta sẽ chứng minh phương trình $\left( * \right)$ luôn có nghiệm $t \in \left( {0;1} \right).$

• Cách 1:

Ta có: $f\left( 0 \right).f\left( {\frac{2}{3}} \right)$ $= \frac{c}{9}\left( {4a + 6b + 9c} \right)$ $= \frac{c}{9}\left[ {2\left( {2a + 3b + 6c} \right) – 3c} \right]$ $= – \frac{{{c^2}}}{3}.$

+ Nếu $c = 0$ thì $f\left( {\frac{2}{3}} \right) = 0$ do đó phương trình $\left( * \right)$ có nghiệm $t = \frac{2}{3} \in \left( {0;1} \right).$

+ Nếu $c \ne 0$ thì $f\left( 0 \right).f\left( {\frac{2}{3}} \right) < 0$ suy ra phương trình $\left( * \right)$ có nghiệm $t \in \left( {0;\frac{2}{3}\pi } \right)$, do đó phương trình $\left( * \right)$ có nghiệm $t \in \left( {0;1} \right).$

Vậy phương trình $a{\tan ^2}x + b\tan x + c = 0$ có ít nhất một nghiệm thuộc khoảng $\left( {k\pi ;\frac{\pi }{4} + k\pi } \right)$, $k \in Z.$

• Cách 2:

Ta có: $f\left( 0 \right) + 4f\left( {\frac{1}{2}} \right) + f\left( 1 \right)$ $= c + 4\left( {\frac{1}{4}a + \frac{1}{2}b + c} \right)$ $+ a + b + c$ $= 2a + 3b + 6c = 0$ $\left( { * * } \right).$

+ Nếu $a = 0$, từ giả thiết suy ra $3b + 6c = 0$, do đó phương trình $\left( * \right)$ có nghiệm $t = \frac{1}{2} \in \left( {0;1} \right).$

+ Nếu $a \ne 0$ thì $f\left( 0 \right)$, $f\left( {\frac{1}{2}} \right)$, $f\left( 1 \right)$ không thể đồng thời bằng $0$ (vì phương trình bậc hai không có quá hai nghiệm).

Khi đó, từ $\left( { * * } \right)$ suy ra trong ba số $f\left( 0 \right)$, $f\left( {\frac{1}{2}} \right)$, $f\left( 1 \right)$ phải có hai giá trị trái dấu nhau (Vì nếu cả ba giá trị đó cùng âm hoặc cùng dương thì tổng của chúng không thể bằng $0$).

Mà hai giá trị nào trong chúng trái dấu thì theo tính chất hàm liên tục ta đều suy ra phương trình $\left( * \right)$ có ít nhất một nghiệm $t \in \left( {0;1} \right).$

Vậy phương trình $a{\tan ^2}x + b\tan x + c = 0$ có ít nhất một nghiệm thuộc khoảng $\left( {k\pi ;\frac{\pi }{4} + k\pi } \right)$, $k \in Z.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 5: Cho hàm số $y = f(x) = {x^3} – \frac{3}{2}{m^2}{x^2} + 32$ (với $m$ là tham số). Chứng minh rằng với $m < – 2$ hoặc $m > 2$ thì phương trình $f(x)=0$ có đúng ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ và thỏa điều kiện ${x_1} < 0 < {x_2} < {x_3}.$

Ta có: $f(0) = 32$, $f\left( {{m^2}} \right) = \frac{1}{2}\left( {64 – {m^6}} \right)$, khi $m < – 2$ hoặc $m > 2$ thì $\frac{1}{2}\left( {64 – {m^6}} \right) < 0$ và ${m^2} > 0.$

Mà:

$\mathop {\lim }\limits_{x \to – \infty } f\left( x \right)$ $= \mathop {\lim }\limits_{x \to – \infty } \left( {{x^3} – \frac{3}{2}{m^2}{x^2} + 32} \right) = – \infty$ $\Rightarrow \exists \alpha < 0$ sao cho $f\left( \alpha \right) < 0.$

$\mathop {\lim }\limits_{x \to + \infty } f\left( x \right)$ $= \mathop {\lim }\limits_{x \to + \infty } \left( {{x^3} – \frac{3}{2}{m^2}{x^2} + 32} \right) = + \infty$ $\Rightarrow \exists \beta > {m^2}$ sao cho $f\left( \beta \right) > 0.$

Do đó ta có 
$$
\left\{ \begin{array}{l}
f\left( \alpha \right).f\left( 0 \right) < 0\\
f\left( 0 \right).f\left( {{m^2}} \right) < 0\\
f\left( {{m^2}} \right).f\left( \beta \right) < 0
\end{array} \right. .
$$
 Vì hàm số $f(x)$ xác định và liên tục trên $R$ nên liên tục trên các đoạn $\left[ {\alpha ;0} \right]$, $\left[ {0;{m^2}} \right]$, $\left[ {{m^2};\beta } \right]$ nên phương trình $f(x)=0$ có ít nhất ba nghiệm lần lượt thuộc các khoảng $\left( {\alpha ;0} \right)$, $\left( {0;{m^2}} \right)$, $\left( {{m^2};\beta } \right).$ Vì $f(x)$ là hàm bậc ba nên nhiều nhất chỉ có ba nghiệm.

Vậy với $m < – 2$ hoặc $m > 2$ thì phương trình $f(x)={x^3} – \frac{3}{2}{m^2}{x^2} + 32=0$ có đúng ba nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3}$ thỏa mãn điều kiện ${x_1} < 0 < {x_2} < {x_3}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/08/chung-minh-phuong-trinh-co-nghiem-dua-vao-tinh-lien-tuc-cua-ham-so.html -->
## Ví dụ 6: Chứng minh rằng phương trình $\left( {{m^2} – m + 3} \right){x^{2n}} – 2x – 4 = 0$ với $n \in {N^*}$ luôn có ít nhất một nghiệm âm với mọi giá trị của tham số m.

Đặt $f\left( x \right) = \left( {{m^2} – m + 3} \right){x^{2n}} – 2x – 4.$

Ta có:

$f\left( { – 2} \right)$ $= \left( {{m^2} – m + 3} \right){\left( { – 2} \right)^{2n}} – 2\left( { – 2} \right) – 4$ $= \left( {{m^2} – m + 3} \right){2^{2n}} > 0$, $\forall m \in R.$

$f\left( 0 \right) = – 4 < 0$, $\forall m \in R.$

Từ đó có: $f\left( { – 2} \right).f\left( 0 \right) < 0$, $\forall m \in R.$

Ngoài ra hàm số $f(x)$ xác định và liên tục trên $R$ nên hàm số liên tục trên đoạn $\left[ { – 2;0} \right].$

Vậy phương trình $f(x) = 0$ luôn có ít nhất một nghiệm âm với mọi giá trị tham số $m.$