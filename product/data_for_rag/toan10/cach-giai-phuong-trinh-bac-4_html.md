# Cách giải phương trình bậc 4

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
Bài viết trình bày cách giải phương trình bậc 4 (phương trình bậc bốn), đây là dạng toán thường gặp trong chương trình Đại số 10 chương 3.

<!-- chunk:1 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 1. Phương trình bậc bốn dạng $a{x^4} + b{x^3} + c{x^2} + bkx + a{k^2} = 0.$

Ta có: $a{x^4} + b{x^3} + c{x^2} + bkx + a{k^2} = 0$ $\Leftrightarrow a\left( {{x^4} + 2{x^2}.k + {k^2}} \right)$ $+ bx\left( {{x^2} + k} \right) + \left( {c – 2ak} \right){x^2} = 0$ $\Leftrightarrow a{\left( {{x^2} + k} \right)^2} + bx\left( {{x^2} + k} \right)$ $+ \left( {c – 2ak} \right){x^2} = 0.$

Đến đây có hai hướng để giải quyết:

Cách 1: Đưa phương trình về dạng ${A^2} = {B^2}.$

Thêm bớt, biến đổi vế trái thành dạng hằng đẳng thức dạng bình phương của một tổng, chuyển các hạng tử chứa $x^2$ sang bên phải.

Cách 2: Đặt $y = {x^2} + k$ $\Rightarrow y \ge k.$

Phương trình $a{x^4} + b{x^3} + c{x^2} + bkx + a{k^2} = 0$ trở thành: $a{y^2} + bxy$ $+ \left( {c – 2ak} \right){x^2} = 0.$

Tính $x$ theo $y$ hoặc $y$ theo $x$ để đưa về phương trình bậc hai theo ẩn $x.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 1. Giải phương trình: ${x^4} – 8{x^3} + 21{x^2} – 24x + 9 = 0.$

Cách 1:

Phương trình $\Leftrightarrow \left( {{x^4} + 9 + 6{x^2}} \right) – 8\left( {{x^2} + 3} \right) + 16{x^2}$ $= 16{x^2} – 21{x^2} + 6{x^2}$ $\Leftrightarrow {\left( {{x^2} – 4x + 3} \right)^2} = {x^2}$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 4x + 3 = x\\
{x^2} – 4x + 3 = – x
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 5x + 3 = 0\\
{x^2} – 3x + 3 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{{5 – \sqrt {13} }}{2}\\
x = \frac{{5 + \sqrt {13} }}{2}
\end{array} \right.
$$

Cách 2:

Phương trình $\Leftrightarrow \left( {{x^4} + 6{x^2} + 9} \right)$ $– 8x\left( {{x^2} + 3} \right) + 15{x^2} = 0$ $\Leftrightarrow {\left( {{x^2} + 3} \right)^2} – 8x\left( {{x^2} + 3} \right) + 15{x^2} = 0.$

Đặt $y = {x^2} + 3$, phương trình trở thành: ${y^2} – 8xy + 15{x^2} = 0$ $\Leftrightarrow \left( {y – 3x} \right)\left( {y – 5x} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
y = 3x\\
y = 5x
\end{array} \right.
$$

Với $y = 3x$, ta có: $x^2+3=3x$, phương trình vô nghiệm.

Với $y = 5x$, ta có: ${x^2} + 3 = 5x$ $\Leftrightarrow {x^2} – 5x + 3 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{{5 – \sqrt {13} }}{2}\\
x = \frac{{5 + \sqrt {13} }}{2}
\end{array} \right.
$$

Nhận xét: Mỗi cách giải có ưu điểm riêng, với cách giải 1, ta sẽ tính được trực tiếp mà không phải thông qua ẩn phụ, với cách giải 2, ta sẽ có những tính toán đơn giản hơn và ít bị nhầm lẫn.

<!-- chunk:3 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 2. Phương trình bậc bốn dạng $\left( {x + a} \right)\left( {x + b} \right)\left( {x + c} \right)\left( {x + d} \right) = e{x^2}$ với $ad=bc=m.$

Cách 1: Đưa về dạng $A^2 = B^2.$

$\left( {x + a} \right)\left( {x + b} \right)\left( {x + c} \right)\left( {x + d} \right) = e{x^2}$ $\Leftrightarrow \left( {{x^2} + px + m} \right)\left( {{x^2} + nx + m} \right) = e{x^2}$ $\Leftrightarrow \left( {{x^2} + \frac{{p + n}}{2}x + m – \frac{{n – p}}{2}x} \right)\left( {{x^2} + \frac{{p + n}}{2}x + m + \frac{{n – p}}{2}x} \right)$ $= e{x^2}$ $\Leftrightarrow {\left( {{x^2} + \frac{{p + n}}{2}x + m} \right)^2}$ $= \left[ {{{\left( {\frac{{n – p}}{2}} \right)}^2} + e} \right]{x^2}$, với $ad = bc = m$, $p = a + d$, $n = b + c.$

Cách 2: Xét xem $x=0$ có phải là nghiệm của phương trình hay không.

Trường hợp $x≠0$, ta có: $\left( {x + a} \right)\left( {x + b} \right)\left( {x + c} \right)\left( {x + d} \right) = e{x^2}$ $\left( {x + \frac{m}{x} + p} \right)\left( {x + \frac{m}{x} + n} \right) = e.$

Đặt $u = x + \frac{m}{x}$, điều kiện $\left| u \right| \ge 2\sqrt {\left| m \right|}$, phương trình trở thành $(u+p)(u+n)=e$, đến đây giải phương trình bậc hai theo $u$ để tìm $x.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 2. Giải phương trình: $\left( {x + 4} \right)\left( {x + 6} \right)\left( {x – 2} \right)\left( {x – 12} \right) = 25{x^2}.$

Cách 1:

$\left( {x + 4} \right)\left( {x + 6} \right)\left( {x – 2} \right)\left( {x – 12} \right) = 25{x^2}$ $\Leftrightarrow \left( {{x^2} – 2x + 24 + 12x} \right)\left( {{x^2} – 2x + 24 – 12x} \right) = 25{x^2}$ $\Leftrightarrow {\left( {{x^2} – 2x + 24} \right)^2} = 169{x^2}$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 2x + 24 = 13x\\
{x^2} – 2x + 24 = – 13x
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 15x + 24 = 0\\
{x^2} + 11x + 24 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 8\\
x = – 3\\
x = \frac{{15 \pm \sqrt {129} }}{2}
\end{array} \right.
$$

Cách 2:

$\left( {x + 4} \right)\left( {x + 6} \right)\left( {x – 2} \right)\left( {x – 12} \right) = 25{x^2}$ $\left( {{x^2} + 10x + 24} \right)\left( {{x^2} – 14x + 24} \right) = 25{x^2}.$

Nhận thấy $x = 0$ không phải là nghiệm của phương trình.

Với $x≠0$, ta có: phương trình $\Leftrightarrow \left( {x + \frac{{24}}{x} + 10} \right)\left( {x + \frac{{24}}{x} – 14} \right) = 25.$

Đặt $y = x + \frac{{24}}{x}$ $\Rightarrow \left| y \right| \ge 4\sqrt 6$, ta được: $\left( {y + 10} \right)\left( {y – 14} \right) = 25$ $\Leftrightarrow \left( {y + 11} \right)\left( {y – 15} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
y = – 11\\
y = 15
\end{array} \right.
$$

Với $y=-11$, ta có phương trình: $x + \frac{{24}}{x} = – 11$ $\Leftrightarrow {x^2} + 11x + 24 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – 3\\
x = – 8
\end{array} \right.
$$

Với $y=15$, ta có phương trình: $x + \frac{{24}}{x} = 15$ $\Leftrightarrow {x^2} – 15x + 24 = 0$ $\Leftrightarrow x = \frac{{15 \pm \sqrt {129} }}{2}$

Vậy phương trình đã cho có tập nghiệm $S = \left\{ { – 3; – 8;\frac{{15 – \sqrt {129} }}{2};\frac{{15 + \sqrt {129} }}{2}} \right\}.$

Nhận xét: Trong cách giải 2, có thể ta không cần xét $x≠0$ rồi chia mà có thể đặt ẩn phụ $y=x^2+m$ để thu được phương trình bậc hai ẩn $x$, tham số $y$ hoặc ngược lại.

<!-- chunk:5 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 3. Phương trình bậc bốn dạng $\left( {x + a} \right)\left( {x + b} \right)\left( {x + c} \right)\left( {x + d} \right) = m$ với $a+b=c+d=p.$

Ta có: $\left( {x + a} \right)\left( {x + b} \right)\left( {x + c} \right)\left( {x + d} \right) = m$ $\Leftrightarrow \left( {{x^2} + px + ab} \right)\left( {{x^2} + px + cd} \right) = m.$

Cách 1:

$\left( {{x^2} + px + ab} \right)\left( {{x^2} + px + cd} \right) = m$ $\Leftrightarrow \left( {{x^2} + px + \frac{{ab + cd}}{2} + \frac{{ab – cd}}{2}} \right)\left( {{x^2} + px + \frac{{ab + cd}}{2} – \frac{{ab – cd}}{2}} \right) = m$ $\Leftrightarrow {\left( {{x^2} + px + \frac{{ab + cd}}{2}} \right)^2}$ $= m + {\left( {\frac{{ab – cd}}{2}} \right)^2}.$

Bài toán quy về giải hai phương trình bậc hai theo biến $x.$

Cách 2:

Đặt $y=x^2+px$, điều kiện $y \ge – \frac{{{p^2}}}{4}$, phương trình trở thành: $\left( {y + ab} \right)\left( {y + cd} \right) = m.$

Giải phương trình bậc hai ẩn $y$ để tìm $x.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 3. Giải phương trình: $x\left( {x + 1} \right)\left( {x + 2} \right)\left( {x + 3} \right) = 8.$

Cách 1:

Ta có: $x\left( {x + 1} \right)\left( {x + 2} \right)\left( {x + 3} \right) = 8$ $\Leftrightarrow \left( {{x^2} + 3x} \right)\left( {{x^2} + 3x + 2} \right) = 8$ $\Leftrightarrow \left( {{x^2} + 3x + 1 – 1} \right)\left( {{x^2} + 3x + 1 + 1} \right) = 8$ $\Leftrightarrow {\left( {{x^2} + 3x + 1} \right)^2} = 9$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + 3x + 1 = 3\\
{x^2} + 3x + 1 = – 3
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + 3x – 2 = 0\\
{x^2} + 3x + 4 = 0
\end{array} \right.
$$
 $\Leftrightarrow x = \frac{{ – 3 \pm \sqrt {17} }}{2}.$

Cách 2:

$x\left( {x + 1} \right)\left( {x + 2} \right)\left( {x + 3} \right) = 8$ $\Leftrightarrow \left( {{x^2} + 3x} \right)\left( {{x^2} + 3x + 2} \right) = 8.$

Đặt $y = {x^2} + 3x$ $\Rightarrow y \ge – \frac{9}{4}$, ta được: $y\left( {y + 2} \right) = 8$ $\Leftrightarrow {y^2} + 2y – 8 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
y = 2\\
y = – 4\:(loại)
\end{array} \right.
$$
 $\Leftrightarrow y = 2.$

Với $y=2$, ta có phương trình: ${x^2} + 3x – 2 = 0$ $\Leftrightarrow x = \frac{{ – 3 \pm \sqrt {17} }}{2}.$

Vậy phương trình đã cho có tập nghiệm $S = \left\{ {\frac{{ – 3 + \sqrt {17} }}{2};\frac{{ – 3 – \sqrt {17} }}{2}} \right\}.$

Nhận xét: Ngoài cách đặt ẩn phụ như đã nêu, ta có thể đặt một trong các dạng ẩn phụ sau:

Đặt $y = {x^2} + px + ab.$

Đặt $y = {x^2} + px + cd.$

Đặt $y = {\left( {x + \frac{p}{2}} \right)^2}.$

Đặt $y = {x^2} + px + \frac{{ab + cd}}{2}.$

<!-- chunk:7 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 4. Phương trình bậc bốn dạng ${\left( {x + a} \right)^4} + {\left( {x + b} \right)^4} = c$ với $(c<0).$

Đặt $x = y – \frac{{a + b}}{2}$, phương trình trở thành: ${\left( {y + \frac{{a – b}}{2}} \right)^4} + {\left( {y – \frac{{a – b}}{2}} \right)^4} = c.$

Sử dụng khai triển nhị thức bậc $4$, ta thu được phương trình: $2{y^4} + 3{\left( {a – b} \right)^2}{y^2} + 2{\left( {\frac{{a – b}}{2}} \right)^4} = c.$

Giải phương trình trùng phương ẩn $y$ để tìm $x.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 4. Giải phương trình: ${\left( {x + 2} \right)^4} + {\left( {x + 4} \right)^4} = 82.$

Đặt $y=x+3$, phương trình trở thành: ${\left( {y + 1} \right)^4} + {\left( {y – 1} \right)^4} = 82$ $\Leftrightarrow \left( {{y^4} + 4{y^3} + 6{y^2} + 4y + 1} \right)\left( {{y^4} – 4{y^3} + 6{y^2} – 4y + 1} \right) = 82$ $\Leftrightarrow 2{y^4} + 12{y^2} – 80 = 0$ $\Leftrightarrow \left( {{y^2} – 4} \right)\left( {{y^2} + 10} \right) = 0$ $\Leftrightarrow {y^2} = 4$ $\Leftrightarrow y = \pm 2.$

Với $y=2$, ta được $x=-1.$

Với $y=-2$, ta được $x=-5.$

Vậy phương trình có tập nghiệm $S = \left\{ { – 1; – 5} \right\}.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 5. Phương trình bậc bốn dạng ${x^4} = a{x^2} + bx + c.$

Đưa phương trình về dạng $A^2 = B^2$ như sau: ${x^4} = a{x^2} + bx + c$ $\Leftrightarrow {\left( {{x^2} + m} \right)^2} = \left( {2m + a} \right){x^2} + bx + c + {m^2}$, trong đó $m$ là một số cần tìm.

Tìm $m$ để $f\left( x \right) = \left( {2m + a} \right){x^2} + bx + c + {m^2}$ có $Δ=0$. Khi đó $f(x)$ có dạng bình phương của một biểu thức:

Nếu $2m+a<0$, phương trình $\Leftrightarrow {\left( {{x^2} + m} \right)^2} + {g^2}\left( x \right) = 0$ (với $f\left( x \right) = – {g^2}\left( x \right)$)
\Leftrightarrow \left\{ \begin{array}{l}
{x^2} + m = 0\\
g\left( x \right) = 0
\end{array} \right.
Nếu $2m+a>0$, phương trình $\Leftrightarrow {\left( {{x^2} + m} \right)^2} = {g^2}\left( x \right)$ (với $f\left( x \right) = {g^2}\left( x \right)$)
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + m = g\left( x \right)\\
{x^2} + m = – g\left( x \right)
\end{array} \right.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 5. Giải phương trình: ${x^4} + {x^2} – 6x + 1 = 0.$

Ta có: ${x^4} + {x^2} – 6x + 1 = 0$ $\Leftrightarrow {x^4} + 4{x^2} + 4 = 3{x^2} + 6x + 3$ $\Leftrightarrow {\left( {{x^2} + 2} \right)^2} = 3{\left( {x + 1} \right)^2}$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} + 2 = \sqrt 3 \left( {x + 1} \right)\\
{x^2} + 2 = – \sqrt 3 \left( {x + 1} \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – \sqrt 3 x + 2 – \sqrt 3 = 0\\
{x^2} + \sqrt 3 x + 2 + \sqrt 3 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{{\sqrt 3 – \sqrt {4\sqrt 3 – 5} }}{2}\\
x = \frac{{\sqrt 3 + \sqrt {4\sqrt 3 – 5} }}{2}
\end{array} \right.
Vậy phương trình đã cho có tập nghiệm: $S = \left\{ {\frac{{\sqrt 3 – \sqrt {4\sqrt 3 – 5} }}{2};\frac{{\sqrt 3 + \sqrt {4\sqrt 3 – 5} }}{2}} \right\}.$

Nhận xét:

Phương trình dạng $x^4 = ax+b$ được giải theo cách tương tự.

Phương trình $Δ=0$ là phương trình bậc ba với cách giải đã được trình bày ở bài viết trước: Cách giải phương trình bậc 3 tổng quát. Phương trình này có thể cho $3$ nghiệm $m$, cần lựa chọn $m$ sao cho việc tính toán là thuận lợi nhất. Tuy nhiên, dù dùng nghiệm $m$ nào thì cũng cho cùng một kết quả.

<!-- chunk:11 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng toán 6. Phương trình bậc bốn dạng $a{f^2}\left( x \right) + bf\left( x \right)g\left( x \right) + c{g^2}\left( x \right) = 0.$

Cách 1:

Xét $g(x) = 0$, giải tìm nghiệm và thử lại vào phương trình ban đầu.

Trường hợp $g(x) ≠ 0$, phương trình $\Leftrightarrow a{\left[ {\frac{{f\left( x \right)}}{{g\left( x \right)}}} \right]^2} + b\frac{{f\left( x \right)}}{{g\left( x \right)}} + c = 0.$

Đặt $y = \frac{{f\left( x \right)}}{{g\left( x \right)}}$, giải phương trình bậc hai $a{y^2} + by + c = 0$ rồi tìm $x.$

Cách 2: Đặt $u = f\left( x \right)$, $v = g\left( x \right)$, phương trình trở thành: $a{u^2} + buv + c{v^2} = 0$, xem phương trình này là phương trình bậc hai theo ẩn $u$, tham số $v$, từ đó tính $u$ theo $v.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 6. Giải phương trình: $20{\left( {x – 2} \right)^2} – 5{\left( {x + 1} \right)^2}$ $+ 48\left( {x – 2} \right)\left( {x + 1} \right) = 0.$

Đặt $u=x-2$, $v=x+1$, phương trình trở thành: $20{u^2} + 48uv – 5{v^2} = 0$ $\Leftrightarrow \left( {10u – v} \right)\left( {2u + 5v} \right) = 0$
\Leftrightarrow \left[ \begin{array}{l}
10u = v\\
2u = – 5v
\end{array} \right.
Với $10u=v$, ta có: $10\left( {x – 2} \right) = x + 1$ $\Leftrightarrow x = \frac{7}{3}.$

Với $2u=-5v$, ta có: $2\left( {x – 2} \right) = – 5\left( {x + 1} \right)$ $\Leftrightarrow x = – \frac{1}{7}.$

Vậy phương trình đã cho có tập nghiệm: $S = \left\{ {\frac{7}{3}; – \frac{1}{7}} \right\}.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Dạng 7. Phương trình bậc bốn tổng quát $a{x^4} + b{x^3} + c{x^2} + dx + e = 0.$

Phân tích các hạng tử bậc $4$, $3$, $2$ thành bình phương đúng, các hạng tử còn lại chuyển sang về phải: $a{x^4} + b{x^3} + c{x^2} + dx + e = 0$ $\Leftrightarrow 4{a^2}{x^4} + 4ba{x^3} + 4ca{x^2} + 4dax + 4ae = 0$ $\Leftrightarrow {\left( {2a{x^2} + bx} \right)^2}$ $= \left( {{b^2} – 4ac} \right){x^2} – 4adx – 4ae.$

Thêm vào hai vế một biểu thức $2\left( {2a{x^2} + bx} \right)y + {y^2}$ ($y$ là hằng số) để về trái thành bình phương đúng, còn vế phải là tam thức bậc hai theo $x$: $f\left( x \right) = \left( {{b^2} – 4ac – 4ay} \right){x^2}$ $+ 2\left( {by – 2ad} \right)x – 4ae + {y^2}.$

Tính $y$ sao cho vế phải là một bình phương đúng, khi đó $Δ$ của vế phải bằng $0$, như vậy ta phải giải phương trình $Δ= 0$, từ đó ta có dạng phương trình $A^2=B^2$ quen thuộc.

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/cach-giai-phuong-trinh-bac-4.html -->
## Ví dụ 7. Giải phương trình: ${x^4} – 16{x^3} + 66{x^2} – 16x – 55 = 0.$

Ta có: ${x^4} – 16{x^3} + 66{x^2} – 16x – 55 = 0$ $\Leftrightarrow {x^4} – 16{x^3} + 64{x^2}$ $= – 2{x^2} + 16x + 55$ $\Leftrightarrow {\left( {{x^2} – 8x} \right)^2} + 2y\left( {{x^2} – 8x} \right) + {y^2}$ $= \left( {2y – 2} \right){x^2} + \left( {16 – 16y} \right)x + 55 + {y^2}.$

Giải phương trình $\Delta = 0$ $\Leftrightarrow {\left( {8 – 8y} \right)^2} – \left( {55 + {y^2}} \right)\left( {2y – 2} \right) = 0$ tìm được $y=1$, $y= 3$, $y=29.$

Trong các giá trị này, ta thấy giá trị $y=3$ là thuận lợi nhất cho việc tính toán.

Như vậy chọn $y=3$, ta có phương trình: ${\left( {{x^2} – 8x + 3} \right)^2} = 4{\left( {x – 4} \right)^2}$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 8x + 3 = 2\left( {x – 4} \right)\\
{x^2} – 8x + 3 = – 2\left( {x – 4} \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{x^2} – 10x + 11 = 0\\
{x^2} – 6x – 5 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = 3 \pm \sqrt {14} \\
x = 5 \pm \sqrt {14}
\end{array} \right.
$$

Vậy phương trình đã cho có tập nghiệm $S = \left\{ {3 + \sqrt {14} ;3 – \sqrt {14} ;5 + \sqrt {14} ;5 – \sqrt {14} } \right\}.$

Nhận xét:

Ví dụ trên cho ta thấy phương trình $Δ= 0$ có nhiều nghiệm, có thể chọn $y=1$ nhưng từ đó ta có phương trình ${\left( {{x^2} – 8x + 1} \right)^2} = 56$ thì không thuận lợi lắm cho việc tính toán, tuy nhiên, kết quả vẫn như nhau.

Một cách giải khác là từ phương trình ${x^4} + a{x^3} + b{x^2} + cx + d = 0$, đặt $x = t – \frac{a}{4}$ ta sẽ thu được phương trình khuyết bậc ba theo $t$, nghĩa là bài toán quy về giải phương trình ${t^4} = a{t^2} + bt + c$ đã trình bày ở dạng 5.