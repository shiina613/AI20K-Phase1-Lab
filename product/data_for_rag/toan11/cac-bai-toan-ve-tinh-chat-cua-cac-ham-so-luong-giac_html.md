# Các bài toán về tính chất của các hàm số lượng giác

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
Bài viết hướng dẫn giải một số bài toán về tính chất của các hàm số lượng giác trong chương trình Đại số và Giải tích 11 chương 1.

<!-- chunk:1 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 1. Xét tính chẵn, lẻ của các hàm số sau:

1) $f(x) = \sin 2x – \cos 3x.$

2) $f(x) = 5\cos x – 2.$

3) $f(x) = 4\sin 2x + 3.$

4) $f(x) = \sin x{\cos ^2}x + \tan x.$

1) Hàm số $f(x) = \sin 2x – \cos 3x$ xác định trên $R.$ Rõ ràng $R$ là tập đối xứng qua gốc $O.$

Mặt khác với mọi $x \in R$ ta có: $f( – x) = \sin ( – 2x) – \cos ( – 3x)$ $= – \sin 2x – \cos 3x.$

Từ đó suy ra ta không thể có: $f( – x) = f(x)$, $\forall x \in R$ cũng như $f( – x) = – f(x)$, $\forall x \in R.$ Ví dụ $f\left( {\frac{\pi }{3}} \right) = \sin \frac{{2\pi }}{3} – \cos \pi$ $= \frac{{\sqrt 3 }}{2} + 1$, $f\left( { – \frac{\pi }{3}} \right) = – \sin \frac{{2\pi }}{3} – \cos \pi$ $= – \frac{{\sqrt 3 }}{2} + 1.$

Vậy trên $R$ hàm số $f(x) = \sin 2x – \cos 3x$ không phải là hàm số chẵn, cũng không phải hàm số lẻ.

2) Hàm số $f(x) = 5\cos x – 2$ xác định trên $R.$

Với mọi $x \in R$ ta có:

$f( – x) = 5\cos ( – x) – 2$ $= 5\cos x – 2 = f(x).$

Vậy $f(x) = 5\cos x – 2$ là hàm số chẵn trên $R.$

3) Hàm số $f(x) = 4\sin 2x + 3$ xác định trên $R.$

Với mọi $x \in R$ ta có:

$f( – x) = 4\sin ( – 2x) + 3$ $= – 4\sin 2x + 3.$

Từ đó suy ra ta không thể có:

$f( – x) = f(x)$, $\forall x \in R.$

$f( – x) = – f(x)$, $\forall x \in R.$

Vậy $f(x) = 4\sin 2x + 3$ không phải là hàm số chẵn, cũng không phải là hàm số lẻ trên $R.$

4) Hàm số $f(x) = \sin x{\cos ^2}x + \tan x$ xác định với mọi $x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$ Rõ ràng tập xác định $D$ đó là miền đối xứng qua gốc $O.$

Với mọi $x \in D$ ta có:

$f( – x) = \sin ( – x){\cos ^2}( – x) + \tan ( – x)$ $= – \sin x{\cos ^2}x – \tan x = – f(x).$

Vậy $f(x)$ là hàm số lẻ trên miền xác định $D = \left\{ {x \in R:x \ne \frac{\pi }{2} + k\pi ,k \in R} \right\}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 2. Cho hàm số $f(x) = a\sin x + b\cos x$ thoả mãn điều kiện: $f\left( {{x_1}} \right) = f\left( {{x_2}} \right) = 0$ ở đây ${x_1} – {x_2} \ne k\pi$, $k \in Z.$ Chứng minh $f(x) = 0$ với mọi $x \in R.$

Ta có $f\left( {{x_1}} \right) = f\left( {{x_2}} \right) = 0$ nên ta có hệ sau:

$$
\left\{ {\begin{array}{l}
{a\sin {x_1} + b\cos {x_1} = 0}\\
{a\sin {x_2} + b\cos {x_2} = 0}
\end{array}} \right..
$$

Quan niệm hệ trên là hệ phương trình bậc nhất của các ẩn $a$, $b$ ta có:

$$
D = \left| {\begin{array}{l}
{\sin {x_1}}&{\cos {x_1}}\\
{\sin {x_2}}&{\cos {x_2}}
\end{array}} \right|
$$
 $= \sin {x_1}\cos {x_2} – \sin {x_2}\cos {x_1}$ $= \sin \left( {{x_1} – {x_2}} \right).$

Vì ${x_1} – {x_2} \ne k\pi$ nên suy ra $D \ne 0.$

Mặt khác:

$$
{D_a} = \left| {\begin{array}{c}
0&{\cos {x_1}}\\
0&{\cos {x_2}}
\end{array}} \right| = 0.
$$

$$
{D_b} = \left| {\begin{array}{l}
{\sin {x_1}}&0\\
{\sin {x_2}}&0
\end{array}} \right| = 0.
$$

Từ đó suy ra:

$a = \frac{{{D_a}}}{D} = 0.$

$b = \frac{{{D_b}}}{D} = 0.$

Vậy $f(x) = 0$, $\forall x \in R.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 3. Cho hàm số $f(x) = a\cos (\alpha + x) + b\cos (\beta + x).$ Giả sử $f(0) = f(\varphi ) = 0$ với $\varphi \ne k\pi$, $k \in Z.$ Chứng minh rằng $f(x) = 0$ với mọi $x \in R.$

Từ giả thiết $f(0) = f(\varphi ) = 0$ ta có:

$$
\left\{ {\begin{array}{l}
{a\cos \alpha + b\cos \beta = 0\:\:(1)}\\
{a\cos (\alpha + \varphi ) + b\cos (\beta + \varphi ) = 0\:\:(2)}
\end{array}.} \right.
$$

Từ $(2)$ ta có:

$a\cos \alpha \cos \varphi + b\cos \beta \cos \varphi$ $– a\sin \alpha \sin \varphi – b\sin \beta \sin \varphi = 0.$

$\Rightarrow \cos \varphi (a\cos \alpha + b\cos \beta )$ $– \sin \varphi (a\sin \alpha + b\sin \beta ) = 0$ $(3).$

Từ $(1)$ và $(3)$ đi đến: $\sin \varphi (a\sin \alpha + b\sin \beta ) = 0$ $(4).$

Vì $\varphi \ne k\pi$, $k \in Z$ nên $\sin \varphi \ne 0.$ Vì thế từ $(4)$ suy ra:

$a\sin \alpha + b\sin \beta = 0$ $(5).$

Bây giờ ta biến đổi $f(x)$ về dạng sau:

$f(x) = a\cos (x + \alpha ) + b\cos (x + \beta )$ $= \cos x(a\cos \alpha + b\cos \beta )$ $– \sin x(a\sin \alpha + b\sin \beta )$ $(6).$

Từ $(1)$, $(5)$ và $(6)$ đi đến: $f(x) = 0$, $\forall x \in R.$

Đó là điều phải chứng minh.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 4. Cho hàm số $f(x) = a\cos x + b\cos 2x + c\cos 3x.$ Biết rằng $f(x) = 0$, $\forall x \in R.$ Chứng minh rằng $a = b = c = 0.$

Vì $f(x) = a\cos x + b\cos 2x + c\cos 3x = 0$, $\forall x \in R$ nên nói riêng ta có:

$$
\left\{ {\begin{array}{l}
{f\left( {\frac{\pi }{2}} \right) = 0}\\
{f\left( {\frac{\pi }{6}} \right) = 0}\\
{f(0) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a\cos \frac{\pi }{2} + b\cos \pi + c\cos \frac{{3\pi }}{2} = 0}\\
{a\cos \frac{\pi }{6} + b\cos \frac{\pi }{3} + c\cos \frac{\pi }{2} = 0}\\
{a\cos 0 + b\cos 0 + c\cos 0 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – b = 0\:\:(1)}\\
{\frac{{\sqrt 3 }}{2}a + \frac{b}{2} = 0\:\:(2)}\\
{a + b + c = 0\:\:(3)}
\end{array}} \right..
$$

Từ $(1)$ suy ra $b = 0.$ Thay vào $(2)$ ta có $a = 0$, rồi thay $a = b = 0$ vào $(3)$ ta được $c = 0.$

Vậy $a = b = c = 0.$ Suy ra điều phải chứng minh.

Nhận xét: Nếu bài toán ra dưới dạng:

Tìm tất cả các hàm số có dạng $f(x) = a\cos x + b\cos 2x + c\cos 3x$ sao cho $f(x) = 0$, $\forall x \in R.$

Khi đó ta giải như sau:

1. Điều kiện cần: Giả sử $f(x) = a\cos x + b\cos 2x + c\cos 3x = 0$, $\forall x \in R.$

Theo ví dụ trên suy ra $a = b = c = 0.$

2. Điều kiện đủ: Đảo lại nếu $a = b = c = 0$ thì hiển nhiên ta có:

$f(x) = 0$, $\forall x \in R.$

Vậy $f(x) = 0$ là hàm số duy nhất cần tìm.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 5. Cho các hàm số sau:

$y = – {\sin ^2}x.$

$y = 3{\tan ^2}x + 1.$

$y = \sin x\cos x.$

$y = \sin x\cos x + \frac{{\sqrt 3 }}{2}\cos 2x.$

Chứng minh rằng với mỗi hàm $y = f(x)$ đó đều có tính chất $f(x + k\pi ) = f(x)$, $k \in Z$, $x$ thuộc tập xác định của hàm số.

Các hàm số $y = – {\sin ^2}x$, $y = \sin x\cos x = \frac{1}{2}\sin 2x$, $y = \sin x\cos x + \frac{{\sqrt 3 }}{2}\cos 2x$ $= \frac{1}{2}\sin 2x + \frac{{\sqrt 3 }}{2}\cos 2x$ đều xác định với mọi $x \in R.$

Để ý rằng:

$\sin (x + \pi ) = – \sin x$ $\Rightarrow {\sin ^2}(x + \pi ) = {\sin ^2}x.$

$\sin [2(x + \pi )]$ $= \sin (2x + 2\pi )$ $= \sin 2x.$

$\cos [2(x + \pi )]$ $= \cos (2x + 2\pi )$ $= \cos 2x.$

Vì thế với các hàm số trên ta luôn có $f(x + \pi ) = f(x)$, $\forall x \in R.$

Hàm số $y = 3{\tan ^2}x + 1$ xác định trên miền: $D = \left\{ {x:x \ne \frac{\pi }{2} + k\pi ,k \in Z} \right\}.$

Từ đó suy ra nếu $x \in D$ $\Rightarrow x + \pi \in D.$

Mặt khác $\tan (x + \pi ) = \tan x$, $\forall x \in D$ $\Rightarrow f(x + \pi ) = f(x)$, $\forall x \in D$, ở đây $f(x) = 3{\tan ^2}x + 1.$

Đó là điều phải chứng minh.

Nhận xét: Ta có thể thấy ứng với $k = 1$ thì:

$f(x + \pi ) = f(x)$, $\forall x \in D$ $(1).$

Ở đây $D$ là miền xác định của các hàm số trên. Ngoài ra, dễ thấy $\pi$ là số dương bé nhất thoả mãn $(1).$ Vậy ta có thể nói rằng các hàm số trên là các hàm số tuần hoàn với chu kì cơ sở là $\pi .$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 6. Chứng minh rằng hàm số $f(x) = \cos x + \cos (\sqrt 2 x)$ không phải là hàm số tuần hoàn.

Giả thiết phản chứng $f(x)$ là hàm số tuần hoàn với chu kì $T > 0.$

Khi đó ta có $f(x + T) = f(x)$, $\forall x \in R$ $(1).$

Từ $(1)$ suy ra $f(T) = f(0).$

$\Rightarrow \cos T + \cos (\sqrt 2 T) = 2.$

Vì $\cos T \le 1$, $\cos (\sqrt 2 T) \le 1$ nên từ $(2)$ suy ra hệ sau:

$$
\left\{ {\begin{array}{l}
{\cos T = 1\:\:(3)}\\
{\cos (\sqrt 2 T) = 1\:\:(4)}
\end{array}} \right..
$$

Từ $(3)$ ta có $T = 2k\pi$, $k \in Z.$

Từ $(4)$ ta có $\sqrt 2 T = 2n\pi$, $n \in Z.$

Từ đó suy ra $\sqrt 2 = \frac{n}{k}$ $(5).$

Hệ thức $(5)$ là điều vô lí, vì $\sqrt 2$ là số vô tỉ.

Vậy giả thiết phản chứng là sai, suy ra điều phải chứng minh.

<!-- chunk:7 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 7. Chứng minh rằng hàm số $f(x) = \cos \left( {{x^2}} \right)$ không phải là hàm số tuần hoàn.

Giả thiết phản chứng $f(x)$ là hàm tuần hoàn với chu kì $T > 0.$

Khi đó ta có $f(x + T) = f(x)$, $\forall x \in R$ $(1).$

Vì $(1)$ đúng với mọi $x \in R$ nên trong $(1)$ lần lượt cho $x = 0$, $x = \sqrt {2\pi }$, $x = \sqrt {4\pi }$ ta có:

$$
\left\{ {\begin{array}{l}
{f(T) = f(0)\:\:(2)}\\
{f(\sqrt {2\pi } + T) = f(\sqrt {2\pi } )\:\:(3)}\\
{f(\sqrt {4\pi } + T) = f(\sqrt {4\pi } )\:\:(4)}
\end{array}} \right..
$$

Ta có:

$(2) \Leftrightarrow \cos {T^2} = 1$ $\Leftrightarrow {T^2} = 2k\pi$, $k \in N*.$

$(3) \Leftrightarrow \cos {(\sqrt {2\pi } + T)^2} = \cos 2\pi = 1$ $\Leftrightarrow {(\sqrt {2\pi } + T)^2} = 2m\pi$, $m \in N*.$

$(4) \Leftrightarrow \cos {(\sqrt {4\pi } + T)^2} = \cos 4\pi = 1$ $\Leftrightarrow {(\sqrt {4\pi } + T)^2} = 2n\pi$, $n \in N*.$

Vậy ta có hệ sau: 
$$
\left\{ {\begin{array}{l}
{{T^2} = 2k\pi ,k \in N*\:\:(5)}\\
{{{(\sqrt {2\pi } + T)}^2} = 2m\pi ,m \in N*\:\:(6)}\\
{{{(\sqrt {4\pi } + T)}^2} = 2n\pi ,n \in N*\:\:(7)}
\end{array}} \right..
$$

Ở đây $N*$ là tập hợp tất cả các số nguyên dương.

Trừ từng vế $(7)$ và $(6)$ ta có:

$2\pi + 2T\sqrt \pi (2 – \sqrt 2 )$ $= 2(n – m)\pi$ $\Rightarrow T\sqrt \pi (2 – \sqrt 2 ) = (n – m – 1)\pi .$

$\Rightarrow \pi {T^2}{(2 – \sqrt 2 )^2} = {(n – m – 1)^2}{\pi ^2}$ $\Rightarrow {T^2}{(2 – \sqrt 2 )^2} = {(n – m – 1)^2}\pi$ $(8).$

Thay $(5)$ vào $(8)$ ta có:

$2k{(2 – \sqrt 2 )^2} = {(n – m – 1)^2}$ $\Rightarrow {(2 – \sqrt 2 )^2} = \frac{{{{(n – m – 1)}^2}}}{{2k}}.$

$\Rightarrow 6 – 4\sqrt 2 = \frac{{{{(n – m – 1)}^2}}}{{2k}}$ $(9).$

Hệ thức $(9)$ là điều vô lí vì $\sqrt 2$ là số vô tỉ.

Như vậy giả thiết phản chứng là sai. Từ đó suy ra điều phải chứng minh.

<!-- chunk:8 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 8. Cho $f(x)$ và $g(x)$ là hai hàm tuần hoàn có cùng miền xác định. Giả sử ${T_1}$, ${T_2}$ lần lượt là các chu kì của các hàm số $f(x)$ và $g(x)$, ngoài ra $\frac{{{T_1}}}{{{T_2}}}$ là số hữu tỉ. Chứng minh rằng các hàm số $f(x) + g(x)$ và $f(x).g(x)$ cũng là các hàm số tuần hoàn.

Vì $\frac{{{T_1}}}{{{T_2}}}$ là số hữu tỉ, nên theo định nghĩa số hữu tỉ, ta có: $\frac{{{T_1}}}{{{T_2}}} = \frac{m}{n}$ ở đây $m$, $n$ nguyên dương và phân số $\frac{m}{n}$ là tối giản.

Từ đó ta có $n{T_1} = m{T_2}$ $(1).$

Đặt $T = n{T_1} = m{T_2}.$

Giả sử $D$ là miền xác định của $f(x)$ và $g(x).$ Khi đó với mọi $x \in D$ ta có:

$f(x + T) + g(x + T)$ $= f\left( {x + n{T_1}} \right) + g\left( {x + m{T_2}} \right)$ $(2).$

Vì $f(x)$ là hàm tuần hoàn với chu kì ${T_1}$ và do $n$ nguyên dương, nên ta có:

$f\left( {x + n{T_1}} \right)$ $= f\left[ {x + (n – 1){T_1}} \right]$ $= f\left[ {x + (n – 2){T_1}} \right]$ $= \ldots = f\left( {x + {T_1}} \right)$ $= f(x)$ $(3).$

Hoàn toàn tương tự, ta có: $g\left( {x + m{T_2}} \right) = g(x)$ $(4).$

Từ $(2)$ $(3)$ $(4)$ suy ra:

$f(x + T) + g(x + T)$ $= f(x) + g(x)$, $\forall x \in D.$

Vậy $f(x) + g(x)$ là hàm tuần hoàn với chu kì $T.$

Tương tự $f(x).g(x)$ cũng là hàm tuần hoàn với chu kì $T.$

Suy ra điều phải chứng minh.

Nhận xét:

1. Từ ví dụ trên ta suy ra kết quả sau:

Các hàm số:

$f(x) = a\sin \alpha x + b\cos \beta x.$

$g(x) = a\cos \alpha x + b\cos \beta x.$

$h(x) = a\sin \alpha x + b\sin \beta x.$

trong đó $\frac{\alpha }{\beta }$ là số hữu tỉ đều là hàm tuần hoàn $(\alpha ,\beta > 0).$

Thật vậy xét ví dụ hàm số $f(x) = a\sin \alpha x + b\cos \beta x.$

Hàm số $a\sin \alpha x$ và $b\cos \beta x$ cùng xác định trên toàn $R$ và lần lượt có chu kì là ${T_1} = \frac{{2\pi }}{\alpha }$, ${T_2} = \frac{{2\pi }}{\beta }.$

Do $\frac{{{T_1}}}{{{T_2}}} = \frac{\beta }{\alpha }$ là số hữu tỉ.

Từ đó suy ra điều phải chứng minh.

2. Nếu $\frac{{{T_1}}}{{{T_2}}}$ là số vô tỉ, thì kết luận của ví dụ 1 chưa chắc đúng. Ví dụ 6 là một minh chứng cho điều này.

Hàm số $f(x) = \cos x + \cos (\sqrt 2 x)$ không phải là hàm tuần hoàn, ở đây $\cos x$ có chu kì $2\pi$, $\cos (\sqrt 2 x)$ có chu kì $\sqrt 2 \pi$ và $\frac{{{T_1}}}{{{T_2}}} = \frac{1}{{\sqrt 2 }}$ không phải là số hữu tỉ.

<!-- chunk:9 level:3 source:https://toanmath.com/2019/09/cac-bai-toan-ve-tinh-chat-cua-cac-ham-so-luong-giac.html -->
## Ví dụ 9. Cho hàm số $f(x)$ và một số $a > 0$ sao cho nếu $f(x)$ xác định thì $f(x + a)$ cũng xác định. Giả sử với mọi $x \in D$, $D$ là miền xác định của $f(x)$ ta luôn có:

$f(x + a) = \frac{{f(x) – 1}}{{f(x) + 1}}.$

Chứng minh rằng $f(x)$ là hàm tuần hoàn. Hãy đưa ra một hàm lượng giác có tính chất trên.

Từ giả thiết, ta có $\forall x \in D$ thì:

$f(x + a) = \frac{{f(x) – 1}}{{f(x) + 1}}$ $(1).$

Từ $(1)$ suy ra $\forall x \in D$ thì:

$f(x + 2a)$ $= f[(x + a) + a]$ $= \frac{{f(x + a) – 1}}{{f(x + a) + 1}}$ $= \frac{{\frac{{f(x) – 1}}{{f(x) + 1}} – 1}}{{\frac{{f(x) – 1}}{{f(x) + 1}} + 1}}$ $= – \frac{1}{{f(x)}}$ $(2).$

Vì $(2)$ đúng với mọi $x \in D$ nên ta có:

$f(x + 4a)$ $= f[(x + 2a) + 2a]$ $= – \frac{1}{{f(x + 2a)}}$ $= – \frac{1}{{ – \frac{1}{{f(x)}}}}$ $= f(x).$

Như vậy với mọi $x \in D$ thì $f(x + 4a) = f(x).$

Hệ thức trên chứng tỏ rằng $f(x)$ là hàm tuần hoàn.

Xét hàm số lượng giác $f(x) = \cot x$ và lấy $a = \frac{\pi }{4}.$

Rõ ràng nếu $x \in \overline D$ $= \{ x \in R:x \ne k\pi \}$ ($\overline D$ là miền xác định của hàm số $f(x)$) thì $x + \frac{\pi }{4} \in \overline D .$

Mặt khác với mọi $x \in \overline D$ ta có:

$f\left( {x + \frac{\pi }{4}} \right)$ $= \cot \left( {x + \frac{\pi }{4}} \right)$ $= \frac{1}{{\tan \left( {x + \frac{\pi }{4}} \right)}}$ $= \frac{1}{{\frac{{1 + \tan x}}{{1 – \tan x}}}}$ $= \frac{{1 – \tan x}}{{1 + \tan x}}$ $= \frac{{1 – \frac{1}{{\cot x}}}}{{1 + \frac{1}{{\cot x}}}}$ $= \frac{{\cot x – 1}}{{\cot x + 1}}$ $= \frac{{f(x) – 1}}{{f(x) + 1}}.$

Vậy hàm số $f(x)$ thoả mãn đầy đủ các tính chất của ví dụ trên.

Rõ ràng $f(x) = \cot x$ là hàm tuần hoàn với chu kì $\pi .$

Ví dụ này chứng tỏ lớp hàm thoả mãn yêu cầu đầu bài là một tập hợp không rỗng.