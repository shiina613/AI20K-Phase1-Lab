# Hàm số lượng giác và các vấn đề liên quan

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
Bài viết trình bày lí thuyết và phương pháp giải các dạng toán liên quan đến hàm số lượng giác trong chương trình Đại số và Giải tích 11.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## I. CÁC CÔNG THỨC LƯỢNG GIÁC

1. Các hằng đẳng thức:
${\sin ^2}\alpha + {\cos ^2}\alpha = 1$ với mọi $\alpha .$

$\tan \alpha .\cot \alpha = 1$ với mọi $\alpha \ne \frac{{k\pi }}{2}.$

$1 + {\tan ^2}\alpha = \frac{1}{{{{\cos }^2}\alpha }}$ với mọi $\alpha \ne k2\pi .$

$1 + {\cot ^2}\alpha = \frac{1}{{{{\sin }^2}\alpha }}$ với mọi $\alpha \ne k\pi .$

2. Hệ thức các cung đặc biệt:

a. Hai cung đối nhau: $\alpha$ và $– \alpha .$

$\cos ( – \alpha ) = \cos \alpha .$

$\sin ( – \alpha ) = – \sin \alpha .$

$\tan ( – \alpha ) = – \tan \alpha .$

$\cot ( – \alpha ) = – \cot \alpha .$

b. Hai cung phụ nhau: $\alpha$ và $\frac{\pi }{2} – \alpha .$

$\cos \left( {\frac{\pi }{2} – \alpha } \right) = \sin \alpha .$

$\sin \left( {\frac{\pi }{2} – \alpha } \right) = \cos \alpha .$

$\tan \left( {\frac{\pi }{2} – \alpha } \right) = \cot \alpha .$

$\cot \left( {\frac{\pi }{2} – \alpha } \right) = \tan \alpha .$

c. Hai cung bù nhau: $\alpha$ và $\pi – \alpha .$

$\sin (\pi – \alpha ) = \sin \alpha .$

$\cos (\pi – \alpha ) = – \cos \alpha .$

$\tan (\pi – \alpha ) = – \tan \alpha .$

$\cot (\pi – \alpha ) = – \cot \alpha .$

d. Hai cung hơn kém nhau $\pi$: $\alpha$ và $\pi + \alpha .$

$\sin (\pi + \alpha ) = – \sin \alpha .$

$\cos (\pi + \alpha ) = – \cos \alpha .$

$\tan (\pi + \alpha ) = \tan \alpha .$

$\cot (\pi + \alpha ) = \cot \alpha .$

3. Các công thức lượng giác:

a. Công thức cộng:
$\cos (a \pm b) = \cos a.\cos b \pm \sin a.\sin b.$
$\sin (a \pm b) = \sin a.\cos b \pm \cos a.\sin b.$
$\tan (a \pm b) = \frac{{\tan a \pm \tan b}}{{1 \pm \tan a.\tan b}}.$

b. Công thức nhân:
$\sin 2a = 2\sin a\cos a.$

$\cos 2a = {\cos ^2}a – {\sin ^2}a$ $= 1 – 2{\sin ^2}a = 2{\cos ^2}a – 1.$

$\sin 3a = 3\sin a – 4{\sin ^3}a.$

$\cos 3a = 4{\cos ^3}a – 3\cos a.$

c. Công thức hạ bậc:
${\sin ^2}a = \frac{{1 – \cos 2a}}{2}.$

${\cos ^2}a = \frac{{1 + \cos 2a}}{2}.$

${\tan ^2}a = \frac{{1 – \cos 2a}}{{1 + \cos 2a}}.$

d. Công thức biến đổi tích thành tổng:
$\cos a.\cos b = \frac{1}{2}[\cos (a – b) + \cos (a + b)].$

$\sin a.\sin b = \frac{1}{2}[\cos (a – b) – \cos (a + b)].$

$\sin a.\cos b = \frac{1}{2}[\sin (a – b) + \sin (a + b)].$

e. Công thức biến đổi tổng thành tích:
$\cos a + \cos b = 2\cos \frac{{a + b}}{2}.\cos \frac{{a – b}}{2}.$

$\cos a – \cos b = – 2\sin \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}.$

$\sin a + \sin b = 2\sin \frac{{a + b}}{2}.\cos \frac{{a – b}}{2}.$

$\sin a – \sin b = 2\cos \frac{{a + b}}{2}.\sin \frac{{a – b}}{2}.$

$\tan a + \tan b = \frac{{\sin (a + b)}}{{\cos a\cos b}}.$

$\tan a – \tan b = \frac{{\sin (a – b)}}{{\cos a\cos b}}.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## II. TÍNH TUẦN HOÀN CỦA HÀM SỐ

Định nghĩa: Hàm số $y = f(x)$ xác định trên tập $D$ được gọi là hàm số tuần hoàn nếu có số $T \ne 0$ sao cho với mọi $x \in D$ ta có: $x \pm T \in D$ và $f(x + T) = f(x)$. Nếu có số $T$ dương nhỏ nhất thỏa mãn các điều kiện trên thì hàm số đó được gọi là hàm số tuần hoàn với chu kì $T.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## III. CÁC HÀM SỐ LƯỢNG GIÁC

1. Hàm số $y = \sin x.$

Tập xác định: $D = R.$

Tập giá trị: $[ – 1;1]$, tức là $– 1 \le \sin x \le 1$, $\forall x \in R.$

Hàm số đồng biến trên mỗi khoảng $\left( { – \frac{\pi }{2} + k2\pi ;\frac{\pi }{2} + k2\pi } \right)$, nghịch biến trên mỗi khoảng $\left( {\frac{\pi }{2} + k2\pi ;\frac{{3\pi }}{2} + k2\pi } \right).$

Hàm số $y = \sin x$ là hàm số lẻ nên đồ thị hàm số nhận gốc tọa độ $O$ làm tâm đối xứng.

Hàm số $y = \sin x$ là hàm số tuần hoàn với chu kì $T = 2\pi .$

Đồ thị hàm số $y = \sin x.$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-1.png" alt="">

2. Hàm số $y = \cos x.$
Tập xác định: $D = R.$

Tập giá trị: $[ – 1;1]$, tức là $– 1 \le \cos x \le 1$, $\forall x \in R.$

Hàm số $y = \cos x$ nghịch biến trên mỗi khoảng $(k2\pi ;\pi + k2\pi )$, đồng biến trên mỗi khoảng $( – \pi + k2\pi ;k2\pi ).$

Hàm số $y = \cos x$ là hàm số chẵn nên đồ thị hàm số nhận trục $Oy$ làm trục đối xứng.

Hàm số $y = \cos x$ là hàm số tuần hoàn với chu kì $T = 2\pi .$

Đồ thị hàm số $y = \cos x$: Đồ thị hàm số $y = \cos x$ bằng cách tịnh tiến đồ thị hàm số $y = \sin x$ theo véctơ $\overrightarrow v = \left( { – \frac{\pi }{2};0} \right).$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-2.png" alt="">

3. Hàm số $y = \tan x.$

Tập xác định: $D = R\backslash \left\{ {\frac{\pi }{2} + k\pi ,k \in Z} \right\}.$

Tập giá trị: $R.$

Hàm số $y = \tan x$ là hàm số lẻ.

Hàm số $y = \tan x$ là hàm số tuần hoàn với chu kì $T = \pi .$

Hàm số $y = \tan x$ đồng biến trên mỗi khoảng $\left( { – \frac{\pi }{2} + k\pi ;\frac{\pi }{2} + k\pi } \right).$

Đồ thị nhận mỗi đường thẳng $x = \frac{\pi }{2} + k\pi$, $k \in Z$ làm một đường tiệm cận.

Đồ thị:

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-3.png" alt="">

4. Hàm số $y = \cot x.$
Tập xác định: $D = R\backslash \{ k\pi ,k \in Z\} .$

Tập giá trị: $R.$

Hàm số $y = \cot x$ là hàm số lẻ.

Hàm số $y = \cot x$ là hàm số tuần hoàn với chu kì $T = \pi .$

Hàm số $y = \cot x$ nghịch biến trên mỗi khoảng $(k\pi ;\pi + k\pi ).$

Đồ thị hàm số $y = \cot x$ nhận mỗi đường thẳng $x = k\pi$, $k \in Z$ làm một đường tiệm cận.

Đồ thị:

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-4.png" alt="">

<!-- chunk:4 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## I. PHƯƠNG PHÁP

Hàm số $y = \sqrt {f(x)}$ có nghĩa $\Leftrightarrow f(x) \ge 0$ và $f(x)$ tồn tại.

Hàm số $y = \frac{1}{{f(x)}}$ có nghĩa $\Leftrightarrow f(x) \ne 0$ và $f(x)$ tồn tại.

$\sin u(x) \ne 0 \Leftrightarrow u(x) \ne k\pi$, $k \in Z.$

$\cos u(x) \ne 0 \Leftrightarrow u(x) \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

$– 1 \le \sin x,\cos x \le 1.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 1. Tìm tập xác định của hàm số sau:

1. $y = \tan \left( {x – \frac{\pi }{6}} \right).$

2. $y = {\cot ^2}\left( {\frac{{2\pi }}{3} – 3x} \right).$

1. Điều kiện: $\cos \left( {x – \frac{\pi }{6}} \right) \ne 0$ $\Leftrightarrow x – \frac{\pi }{6} \ne \frac{\pi }{2} + k\pi$ $\Leftrightarrow x \ne \frac{{2\pi }}{3} + k\pi .$

Tập xác định: $D = R\backslash \left\{ {\frac{{2\pi }}{3} + k\pi ,k \in Z} \right\}.$

2. Điều kiện: $\sin \left( {\frac{{2\pi }}{3} – 3x} \right) \ne 0$ $\Leftrightarrow \frac{{2\pi }}{3} – 3x \ne k\pi$ $\Leftrightarrow x \ne \frac{{2\pi }}{9} – k\frac{\pi }{3}.$

Tập xác định: $D = R\backslash \left\{ {\frac{{2\pi }}{9} – k\frac{\pi }{3},k \in Z} \right\}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 2. Tìm tập xác định của hàm số sau:

1. $y = \frac{{\tan 2x}}{{\sin x + 1}} + \cot \left( {3x + \frac{\pi }{6}} \right).$

2. $y = \frac{{\tan 5x}}{{\sin 4x – \cos 3x}}.$

1. Điều kiện: 
$$
\left\{ {\begin{array}{l}
{\sin x \ne – 1}\\
{\sin \left( {3x + \frac{\pi }{6}} \right) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne – \frac{\pi }{2} + k2\pi }\\
{x \ne – \frac{\pi }{{18}} + \frac{{n\pi }}{3}}
\end{array}} \right..
$$

Vậy tập xác định: $D = R\backslash \left\{ { – \frac{\pi }{2} + k2\pi , – \frac{\pi }{{18}} + \frac{{n\pi }}{3}\:\left( {k,n \in Z} \right)} \right\}.$

2. Ta có: $\sin 4x – \cos 3x$ $= \sin 4x – \sin \left( {\frac{\pi }{2} – 3x} \right)$ $= 2\cos \left( {\frac{x}{2} + \frac{\pi }{4}} \right)\sin \left( {\frac{{7x}}{2} – \frac{\pi }{4}} \right).$

Điều kiện: 
$$
\left\{ {\begin{array}{l}
{\cos 5x \ne 0}\\
{\cos \left( {\frac{x}{2} + \frac{\pi }{4}} \right) \ne 0}\\
{\sin \left( {\frac{{7x}}{2} – \frac{\pi }{4}} \right) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{{10}} + k\frac{\pi }{5}}\\
{x \ne \frac{\pi }{2} + n2\pi }\\
{x \ne – \frac{\pi }{{14}} + \frac{{n2\pi }}{7}}
\end{array}} \right..
$$

Vậy tập xác định: $D = R\backslash \left\{ {\frac{\pi }{{10}} + \frac{{k\pi }}{5},\frac{\pi }{2} + n2\pi , – \frac{\pi }{{14}} + \frac{{2m\pi }}{7}\:\left( {k,n,m \in Z} \right)} \right\}.$

<!-- chunk:7 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP
## Bài 1. Tìm tập xác định của hàm số sau:

## Bài tập 1. $y = \frac{{1 – \sin 2x}}{{\cos 3x – 1}}.$

## Bài tập 2. $y = \sqrt {\frac{{1 + {{\cot }^2}x}}{{1 – \sin 3x}}} .$

1. Điều kiện: $\cos 3x – 1 \ne 0$ $\Leftrightarrow \cos 3x \ne 1$ $\Leftrightarrow x \ne k\frac{{2\pi }}{3}$, $k \in Z.$

Tập xác định: $D = R\backslash \left\{ {k\frac{{2\pi }}{3},k \in Z} \right\}.$

2. Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x \ne k\pi }\\
{\sin 3x \ne 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne k\pi }\\
{x \ne \frac{\pi }{6} + n\frac{{2\pi }}{3}}
\end{array}} \right..
$$

Vậy tập xác định: $D = R\backslash \left\{ {k\pi ,\frac{\pi }{6} + \frac{{n2\pi }}{3};k,n \in Z} \right\}.$

## Bài 2. Tìm tập xác định của hàm số sau:

## Bài tập 1. $y = \frac{1}{{\sin 2x – \cos 3x}}.$

## Bài tập 2. $y = \frac{{\cot x}}{{2\sin x – 1}}.$

1. Điều kiện: $\sin 2x – \cos 3x \ne 0$ $\Leftrightarrow \cos \frac{{5x}}{2}.\sin \frac{x}{2} \ne 0.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\cos \frac{{5x}}{2} \ne 0}\\
{\sin \frac{x}{2} \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{5x}}{2} \ne \frac{\pi }{2} + k2\pi }\\
{\frac{x}{2} \ne k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{5} + k\frac{{4\pi }}{5}}\\
{x \ne k2\pi }
\end{array}} \right..
$$

Tập xác định: $D = R\backslash \left\{ {\frac{\pi }{5} + k\frac{{4\pi }}{5},k2\pi ;k \in Z} \right\}.$

2. Điều kiện: 
$$
\left\{ {\begin{array}{l}
{x \ne k\pi }\\
{\sin x – \frac{1}{2} \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne k\pi }\\
{\sin x – \sin \frac{\pi }{6} \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne k\pi }\\
{2\cos \left( {\frac{x}{2} + \frac{\pi }{{12}}} \right)\sin \left( {\frac{x}{2} – \frac{\pi }{{12}}} \right) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne k\pi }\\
{x \ne \frac{\pi }{6} + k2\pi }\\
{x \ne \frac{{5\pi }}{6} + k2\pi }
\end{array}} \right..
$$

Tập xác định: $D = R\backslash \left\{ {k\pi ,\frac{\pi }{6} + k2\pi ,\frac{{5\pi }}{6} + k2\pi ;k \in Z} \right\}.$

## Bài 3. Tìm tập xác định của hàm số sau:

## Bài tập 1. $y = \frac{{\sin 3x}}{{\sin 8x – \sin 5x}}.$

## Bài tập 2. $y = \frac{{\tan 4x}}{{\cos 4x + \sin 3x}}.$

1. Điều kiện: $\sin 8x – \sin 5x \ne 0$ $\Leftrightarrow 2\cos \frac{{13x}}{2}\sin \frac{{3x}}{2} \ne 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{13x}}{2} \ne \frac{\pi }{2} + k\pi }\\
{\frac{{3x}}{2} \ne n\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{{13}} + k\frac{{2\pi }}{{13}}}\\
{x \ne \frac{{2n\pi }}{3}}
\end{array}} \right..
$$

Tập xác định: $D = R\backslash \left\{ {\frac{\pi }{{13}} + k\frac{{2\pi }}{{13}},\frac{{2n\pi }}{3};k,n \in Z} \right\}.$

2. Điều kiện: $\cos 4x + \sin 3x \ne 0$ $\Leftrightarrow \cos 4x + \cos \left( {\frac{\pi }{2} – 3x} \right) \ne 0$ $\Leftrightarrow 2\cos \left( {\frac{\pi }{4} + \frac{x}{2}} \right)\cos \left( {\frac{{7x}}{2} – \frac{\pi }{4}} \right) \ne 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{2} + k2\pi }\\
{x \ne \frac{{3\pi }}{{14}} + n\frac{{4\pi }}{7}}
\end{array}} \right..
$$

Tập xác định: $D = R\backslash \left\{ {\frac{\pi }{2} + k2\pi ,\frac{{3\pi }}{{14}} + n\frac{{4\pi }}{7};k,n \in Z} \right\}.$

<!-- chunk:8 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## I. PHƯƠNG PHÁP

Cho hàm số $y = f(x)$ tuần hoàn với chu kì $T.$

Để khảo sát sự biến thiên và vẽ đồ thị của hàm số, ta chỉ cần khảo sát và vẽ đồ thị hàm số trên một đoạn có độ dài bằng $T$ sau đó ta tịnh tiến theo các véc tơ $k.\overrightarrow v$ (với $\overrightarrow v = (T;0)$, $k \in Z$) ta được toàn bộ đồ thị của hàm số.

Số nghiệm của phương trình $f(x) = k$, (với $k$ là hằng số) chính bằng số giao điểm của hai đồ thị $y = f(x)$ và $y = k.$

Nghiệm của bất phương trình $f(x) \ge 0$ là miền $x$ mà đồ thị hàm số $y = f(x)$ nằm trên trục $Ox.$

Chú ý:

Hàm số $f(x) = a\sin ux + b\cos vx + c$ (với $u,v \in Z$) là hàm số tuần hoàn với chu kì $T = \frac{{2\pi }}{{|(u,v)|}}$ ($(u,v)$ là ước chung lớn nhất).

Hàm số $f(x) = a\tan ux + b\cot vx + c$ (với $u,v \in Z$) là hàm tuần hoàn với chu kì $T = \frac{\pi }{{|(u,v)|}}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 1. Xét tính tuần hoàn và tìm chu kì cơ sở của các hàm số $f(x) = \cos \frac{{3x}}{2}.\cos \frac{x}{2}.$

Ta có: $f(x) = \frac{1}{2}(\cos x + \cos 2x)$ suy ra hàm số tuần hoàn với chu kì cơ sở ${T_0} = 2\pi .$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 2. Xét tính tuần hoàn và tìm chu kì cơ sở (nếu có) của các hàm số sau.

## Bài tập 1. $f(x) = \cos x + \cos (\sqrt 3 x).$

## Bài tập 2. $f(x) = \sin {x^2}.$

## Bài tập 1. Giả sử hàm số đã cho tuần hoàn $\Rightarrow$ có số thực dương $T$ thỏa mãn:

$f(x + T) = f(x)$ $\Leftrightarrow \cos (x + T) + \cos \sqrt 3 (x + T)$ $= \cos x + \cos \sqrt 3 x.$

Cho $x = 0$ $\Rightarrow \cos T + \cos \sqrt 3 T = 2$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\cos T = 1}\\
{\cos \sqrt 3 T = 1}
\end{array}} \right..
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{T = 2n\pi }\\
{\sqrt 3 T = 2m\pi }
\end{array}} \right.
$$
 $\Rightarrow \sqrt 3 = \frac{m}{n}$ vô lí, do $m,n \in Z \Rightarrow \frac{m}{n}$ là số hữu tỉ.

Vậy hàm số đã cho không tuần hoàn.

## Bài tập 2. Giả sử hàm số đã cho là hàm số tuần hoàn.

$\Rightarrow \exists T > 0$: $f(x + T) = f(x)$ $\Leftrightarrow \sin {(x + T)^2} = \sin {x^2}$, $\forall x \in R.$

Cho $x = 0$ $\Rightarrow \sin {T^2} = 0$ $\Leftrightarrow {T^2} = k\pi$ $\Rightarrow T = \sqrt {k\pi }$ $\Rightarrow f(x + \sqrt {k\pi } ) = f(x)$, $\forall x \in R.$

Cho $x = \sqrt {2k\pi }$ ta có: $f(\sqrt {2k\pi } ) = \sin {(\sqrt {k2\pi } )^2}$ $= \sin (k2\pi ) = 0.$

$f(x + \sqrt {k\pi } ) = \sin {(\sqrt {k2\pi } + \sqrt {k\pi } )^2}$ $= \sin (3k\pi + 2k\pi \sqrt 2 ) = \pm \sin (2k\pi \sqrt 2 )$ $\Rightarrow f(x + \sqrt {k\pi } ) \ne 0.$

Vậy hàm số đã cho không phải là hàm số tuần hoàn.

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 3. Cho $a$, $b$, $c$, $d$ là các số thực khác $0.$ Chứng minh rằng hàm số $f(x) = a\sin cx + b\cos dx$ là hàm số tuần hoàn khi và chỉ khi $\frac{c}{d}$ là số hữu tỉ.

Giả sử $f(x)$ là hàm số tuần hoàn $\Rightarrow \exists T > 0$: $f(x + T) = f(x)$, $\forall x.$

Cho $x = 0$, $x = – T$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{a\sin cT + b\cos dT = b}\\
{ – a\sin cT + b\cos dT = b}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\cos dT = 1}\\
{\sin cT = 0}
\end{array}} \right..
$$

$$
\Rightarrow \left\{ {\begin{array}{l}
{dT = 2n\pi }\\
{cT = m\pi }
\end{array}} \right.
$$
 $\Rightarrow \frac{c}{d} = \frac{m}{{2n}} \in Q.$

Giả sử $\frac{c}{d} \in Q$ $\Rightarrow \exists k,l \in Z$: $\frac{c}{d} = \frac{k}{l}.$

Đặt $T = \frac{{2\pi k}}{c} = \frac{{2l\pi }}{d}.$

Ta có: $f(x + T) = f(x)$, $\forall x \in R \Rightarrow f(x)$ là hàm số tuần hoàn với chu kì $T = \frac{{2\pi k}}{c} = \frac{{2l\pi }}{d}.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 4. Cho hàm số $y = f(x)$ và $y = g(x)$ là hai hàm số tuần hoàn với chu kỳ lần lượt là ${T_1}$, ${T_2}.$ Chứng minh rằng nếu $\frac{{{T_1}}}{{{T_2}}}$ là số hữu tỉ thì các hàm số $f(x) \pm g(x)$, $f(x).g(x)$ là những hàm số tuần hoàn.

Vì $\frac{{{T_1}}}{{{T_2}}}$ là số hữu tỉ nên tồn tại hai số nguyên $m$, $n$, $n \ne 0$ sao cho:

$\frac{{{T_1}}}{{{T_2}}} = \frac{m}{n}$ $\Rightarrow n{T_1} = m{T_2} = T.$

Khi đó: $f(x + T) = f\left( {x + n{T_1}} \right) = f(x)$ và $g(x + T) = g\left( {x + m{T_2}} \right) = g(x).$

Suy ra: $f(x + T) \pm g(x + T)$ $= f(x) \pm g(x)$ và $f(x + T).g(x + T) = f(x).g(x)$, $\frac{{f(x + T)}}{{g(x + T)}} = \frac{{f(x)}}{{g(x)}}.$ Từ đó ta có điều phải chứng minh.

Nhận xét:

## Bài tập 1. Hàm số $f(x) = a\sin ux + b\cos vx + c$ (với $u,v \in Z$) là hàm số tuần hoàn với chu kì $T = \frac{{2\pi }}{{(u,v)}}$ ($(u,v)$ là ước chung lớn nhất).

## Bài tập 2. Hàm số $f(x) = a.\tan ux + b.\cot vx + c$ (với $u,v \in Z$) là hàm tuần hoàn với chu kì $T = \frac{\pi }{{(u,v)}}.$

<!-- chunk:13 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## III. CÁC BÀI TOÁN LUYỆN TẬP

Bài tập. Chứng minh rằng các hàm số sau là những hàm số tuần hoàn với chu kì cơ sở ${T_0}.$

## Bài tập 1. $f(x) = \sin x$, ${T_0} = 2\pi .$

## Bài tập 2. $f(x) = \tan 2x$, ${T_0} = \frac{\pi }{2}.$

1. Ta có: $f(x + 2\pi ) = \sin (x + 2\pi )$ $= \sin x = f(x)$, $\forall x \in R.$

Giả sử có số thực dương $T < 2\pi$ thỏa mãn $f(x + T) = f(x)$ $\Leftrightarrow \sin (x + T) = \sin x$, $\forall x \in R$ $(1).$

Cho $x = \frac{\pi }{2}$ $\Rightarrow VT(1) = \sin \left( {\frac{\pi }{2} + T} \right)$ $= \cos T < 1.$

$VP(1) = \sin \frac{\pi }{2} = 1$ $\Rightarrow (1)$ không xảy ra với mọi $x \in R.$

Vậy hàm số đã cho tuần hoàn với chu kì cơ sở ${T_0} = 2\pi .$

2. Ta có: $f\left( {x + \frac{\pi }{2}} \right)$ $= \tan 2\left( {x + \frac{\pi }{2}} \right)$ $= \tan (2x + \pi )$ $= \tan 2x = f(x).$

Giả sử có số thực dương $T < \frac{\pi }{2}$ thỏa mãn $f(x + T) = f(x)$ $\Leftrightarrow \tan (2x + 2T) = \tan 2x$ $\forall x \in R$ $(2).$

Cho $x = 0$ $\Rightarrow VT(2) = \tan 2T \ne 0$, còn $VP(2) = 0$ $\Rightarrow (2)$ không xảy ra với mọi $x \in R.$

Vậy hàm số đã cho tuần hoàn với chu kì cơ sở ${T_0} = \frac{\pi }{2}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 1. Xét sự biến thiên và vẽ đồ thị hàm số sau: $y = 2\sin x.$

Hàm số $y = 2\sin x.$

Tập xác định: $D = R.$

Hàm số $y = 2\sin x$ là hàm số lẻ.

Hàm số $y = 2\sin x$ là hàm tuần hoàn với chu kì $T = 2\pi .$

Hàm số đồng biến trên mỗi khoảng $\left( {k2\pi ;\frac{\pi }{2} + k2\pi } \right).$ Nghịch biến trên mỗi khoảng $\left( {\frac{\pi }{2} + k2\pi ;\pi + k2\pi } \right).$

Đồ thị hàm số đi qua các điểm $(k\pi ;0)$, $\left( {\frac{\pi }{2} + k2\pi ;2} \right).$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-5.png" alt="">

<!-- chunk:15 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 2. Xét sự biến thiên và vẽ đồ thị hàm số sau $y = \tan 2x.$

Hàm số $y = \tan 2x.$

Tập xác định: $D = R\backslash \left\{ {\frac{\pi }{4} + k\frac{\pi }{2},k \in Z} \right\}.$

Hàm số $y = \tan 2x$ là hàm số lẻ.

Hàm số $y = \tan 2x$ là hàm tuần hoàn với chu kì $T = \frac{\pi }{2}.$

Hàm số đồng biến trên mỗi khoảng $\left( {k\pi ;\frac{\pi }{4} + k\pi } \right).$

Các đường tiệm cận: $x = \frac{\pi }{4} + k\frac{\pi }{2}.$

Đồ thị hàm số đi qua các điểm $\left( {\frac{{k\pi }}{2};0} \right).$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-6.png" alt="">

<!-- chunk:16 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 3. Xét sự biến thiên và vẽ đồ thị hàm số sau: $y = 1 + 2{\cos ^2}x.$

Hàm số $y = 1 + 2{\cos ^2}x.$

Ta có: $y = 2 + \cos 2x.$

Tập xác định: $D=R.$

Hàm số $y = 2 + \cos 2x$ là hàm số chẵn.

Hàm số $y = 2 + \cos 2x$ là hàm tuần hoàn với chu kì $T = \pi .$

Hàm số đồng biến trên mỗi khoảng $\left( {\frac{\pi }{2} + k\pi ;\pi + k\pi } \right)$, nghịch biến trên mỗi khoảng $\left( {k\pi ;\frac{\pi }{2} + k\pi } \right).$

Đồ thị hàm số đi qua các điểm $\left( {\frac{{k\pi }}{2};1} \right)$, $(\pi + k\pi ;3).$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-7.png" alt="">

<!-- chunk:17 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## II. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Xét sự biến thiên và vẽ đồ thị các hàm số $y = \sin 2x.$

Đồ thị hàm số: $y = \sin 2x.$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-8.png" alt="">

## Bài 2. Xét sự biến thiên và vẽ đồ thị các hàm số: $y = 2|\cos x|.$

Đồ thị hàm số: $y = 2|\cos x|.$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-9.png" alt="">

<!-- chunk:18 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 1. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y = 4\sin x\cos x + 1.$

## Bài tập 2. $y = 4 – 3{\sin ^2}2x.$

1. Ta có: $y = 2\sin 2x + 1.$

Do $– 1 \le \sin 2x \le 1$ $\Rightarrow – 2 \le 2\sin 2x \le 2$ $\Rightarrow – 1 \le 2\sin 2x + 1 \le 3.$

$\Rightarrow – 1 \le y \le 3.$

Với $y = – 1$ $\Leftrightarrow \sin 2x = – 1$ $\Leftrightarrow 2x = – \frac{\pi }{2} + k2\pi$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi .$

Với $y = 3$ $\Leftrightarrow \sin 2x = 1$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi .$

Vậy giá trị lớn nhất của hàm số bằng $3$, giá trị nhỏ nhất bằng $-1.$

2. Ta có: $0 \le {\sin ^2}x \le 1$ $\Rightarrow 1 \le 4 – 3{\sin ^2}x \le 4.$

Với $y = 1$ $\Leftrightarrow {\sin ^2}x = 1$ $\Leftrightarrow \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi .$

Với $y = 4$ $\Leftrightarrow {\sin ^2}x = 0$ $\Leftrightarrow x = k\pi .$

Vậy giá trị lớn nhất của hàm số bằng $4$, giá trị nhỏ nhất bằng $1.$

<!-- chunk:19 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 2. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y = 6{\cos ^2}x + {\cos ^2}2x.$

## Bài tập 2. $y = {(4\sin x – 3\cos x)^2}$ $– 4(4\sin x – 3\cos x) + 1.$

1. Ta có: $y = 6{\cos ^2}x + {\left( {2{{\cos }^2}x – 1} \right)^2}$ $= 4{\cos ^4}x + 2{\cos ^2}x + 1.$

Đặt: $t = {\cos ^2}x \Rightarrow t \in [0;1].$ Khi đó: $y = 4{t^2} + 2t + 1 = f(t).$

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-10.png" alt="">

Vậy:

$\min y = 1$ đạt được khi $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi .$

$\max y = 7$ đạt được khi ${\cos ^2}x = 1$ $\Leftrightarrow x = k\pi .$

## Bài tập 2. Đặt $t = 4\sin x – 3\cos x$ $\Rightarrow – 5 \le t \le 5$, $\forall x \in R.$

Khi đó: $y = {t^2} – 4t + 1$ $= {(t – 2)^2} – 3.$

Vì $t \in [ – 5;5]$ $\Rightarrow – 7 \le t – 2 \le 3$ $\Rightarrow 0 \le {(t – 2)^2} \le 49.$

Do đó: $– 3 \le y \le 46.$

Vậy: $\min y = – 3$, $\max y = 46.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 3. Tìm tất cả các giá trị của tham số $m$ để hàm số sau chỉ nhận giá trị dương: $y = {(3\sin x – 4\cos x)^2}$ $– 6\sin x + 8\cos x + 2m – 1.$

Đặt $t = 3\sin x – 4\cos x$ $\Rightarrow – 5 \le t \le 5.$

Ta có: $y = {t^2} – 2t + 2m – 1$ $= {(t – 1)^2} + 2m – 2.$

Do: $– 5 \le t \le 5$ $\Rightarrow 0 \le {(t – 1)^2} \le 36$ $\Rightarrow y \ge 2m – 2$ $\Rightarrow \min y = 2m – 2.$

Hàm số chỉ nhận giá trị dương $\Leftrightarrow y > 0$, $\forall x \in R$ $\Leftrightarrow \min y > 0$ $\Leftrightarrow 2m – 2 > 0$ $\Leftrightarrow m > 1.$

Vậy $m >1$ là giá trị cần tìm.

<!-- chunk:21 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 4. Tìm $m$ để hàm số $y = \sqrt {2{{\sin }^2}x + 4\sin x\cos x – (3 + 2m){{\cos }^2}x + 2}$ xác định với mọi $x.$

Hàm số xác định với mọi $x$ $\Leftrightarrow 2{\sin ^2}x + 4\sin x\cos x$ $– (3 + 2m){\cos ^2}x + 2 \ge 0$, $\forall x \in R$ $(1).$

$\cos x = 0 \Rightarrow (1)$ đúng.

$\cos x \ne 0$ khi đó ta có:

$(1) \Leftrightarrow 2{\tan ^2}x + 4\tan x$ $– (3 + 2m) + 2\left( {1 + {{\tan }^2}x} \right) \ge 0.$

$\Leftrightarrow 4{\tan ^2}x + 4\tan x \ge 1 + 2m$, $\forall x \in R.$

$\Leftrightarrow {(2\tan x + 1)^2} \ge 2 + 2m$, $\forall x \in R$ $\Leftrightarrow 2 + 2m \le 0$ $\Leftrightarrow m \le – 1.$

<!-- chunk:22 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 5. Cho các góc nhọn $x$, $y$ thỏa mãn ${\sin ^2}x + {\sin ^2}y = \sin (x + y)$ $(*).$ Chứng minh rằng: $x + y = \frac{\pi }{2}.$

Ta có hàm số $y=\sin x, y=\cos x$, $y = \cos x$ đồng biến trên khoảng $\left( {0;\frac{\pi }{2}} \right).$

Và $x$, $y$, $\frac{\pi }{2} – x$, $\frac{\pi }{2} – y \in \left( {0;\frac{\pi }{2}} \right).$

Giả sử $x + y > \frac{\pi }{2}$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x > \frac{\pi }{2} – y}\\
{y > \frac{\pi }{2} – x}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\sin x > \sin \left( {\frac{\pi }{2} – y} \right) = \cos y}\\
{\sin y > \sin \left( {\frac{\pi }{2} – x} \right) = \cos x}
\end{array}} \right..
$$

Suy ra: ${\sin ^2}x + {\sin ^2}y$ $= \sin x.\sin x + \sin y.\sin y$ $> \sin x\cos y + \sin y\cos x$ $= \sin (x + y)$ (mâu thuẫn với $(*)$).

Giả sử $x + y < \frac{\pi }{2}$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{x < \frac{\pi }{2} – y}\\
{y < \frac{\pi }{2} – x}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\sin x < \sin \left( {\frac{\pi }{2} – y} \right) = \cos y}\\
{\sin y < \sin \left( {\frac{\pi }{2} – x} \right) = \cos x}
\end{array}} \right..
$$

Suy ra: ${\sin ^2}x + {\sin ^2}y$ $= \sin x.\sin x + \sin y.\sin y$ $< \sin x\cos y + \sin y\cos x$ $= \sin (x + y)$ (mâu thuẫn với $(*)$).

Nếu $x + y = \frac{\pi }{2}$ $\Rightarrow (*)$ đúng.

Vậy $(*) \Leftrightarrow x + y = \frac{\pi }{2}.$

<!-- chunk:23 level:3 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## Ví dụ 6. Tìm GTLN và GTNN của các hàm sau:

## Bài tập 1. $y = 3\sin x + 4\cos x + 5.$

## Bài tập 2. $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}.$

## Bài tập 1. Xét phương trình: $y = 3\sin x + 4\cos x + 5.$

$\Leftrightarrow 3\sin x + 4\cos x + 5 – y = 0$ $\Rightarrow$ phương trình có nghiệm $\Leftrightarrow {3^2} + {4^2} \ge {(5 – y)^2}$ $\Leftrightarrow {y^2} – 10y \le 0$ $\Leftrightarrow 0 \le y \le 10.$

Vậy $\min y = 0$, $\max y = 10.$

## Bài tập 2. Do $\sin x + \cos x + 2 > 0$, $\forall x \in R$ $\Rightarrow$ hàm số xác định với $\forall x \in R.$

Xét phương trình: $y = \frac{{\sin x + 2\cos x + 1}}{{\sin x + \cos x + 2}}.$

$\Leftrightarrow (1 – y)\sin x + (2 – y)\cos x$ $+ 1 – 2y = 0.$

Phương trình có nghiệm $\Leftrightarrow {(1 – y)^2} + {(2 – y)^2} \ge {(1 – 2y)^2}.$

$\Leftrightarrow {y^2} + y – 2 \le 0$ $\Leftrightarrow – 2 \le y \le 1.$

Vậy $\min y = – 2$, $\max y = 1.$

<!-- chunk:24 level:1 source:https://toanmath.com/2019/08/ham-so-luong-giac-va-cac-van-de-lien-quan.html -->
## II. CÁC BÀI TOÁN LUYỆN TẬP

## Bài 1. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y = \sqrt {2\sin x + 3} .$

## Bài tập 2. $y = \frac{4}{{1 + 2{{\sin }^2}x}}.$

1. Ta có: $1 \le 2\sin x + 3 \le 5$ $\Rightarrow 1 \le y \le \sqrt 5 .$

Vậy:

Giá trị lớn nhất của hàm số bằng $\sqrt 5$, đạt được khi $\sin x = 1$ $\Leftrightarrow x = \frac{\pi }{2} + k2\pi .$

Giá trị nhỏ nhất bằng $1$, đạt được khi $x = – \frac{\pi }{2} + k2\pi .$

2. Ta có: $0 \le {\sin ^2}x \le 1$ $\Rightarrow \frac{4}{3} \le y \le 4.$

$y = \frac{4}{3}$ $\Leftrightarrow {\sin ^2}x = 1$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$ $\Rightarrow \min y = \frac{4}{3}.$

$y = 4$ $\Leftrightarrow {\sin ^2}x = 0$ $\Leftrightarrow x = k\pi$ $\Rightarrow \max y = 4.$

## Bài 2. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y = 2{\sin ^2}x + {\cos ^2}2x.$

## Bài tập 2. $y = 3\sin x + 4\cos x + 1.$

## Bài tập 1. Đặt $t = {\sin ^2}x$, $0 \le t \le 1$ $\Rightarrow \cos 2x = 1 – 2t.$

$\Rightarrow y = 2t + {(1 – 2t)^2}$ $= 4{t^2} – 2t + 1$ $= {\left( {2t – \frac{1}{2}} \right)^2} + \frac{3}{4}.$

Do $0 \le t \le 1$ $\Rightarrow – \frac{1}{2} \le 2t – \frac{1}{2} \le \frac{3}{2}$ $\Rightarrow 0 \le {\left( {2t – \frac{1}{2}} \right)^2} \le \frac{9}{4}$ $\Rightarrow \frac{3}{4} \le y \le 3.$

Vậy:

$\max y = 3$ đạt được khi $x = \frac{\pi }{2} + k\pi .$

$\min y = \frac{3}{4}$ đạt được khi ${\sin ^2}x = \frac{1}{4}.$

## Bài tập 2. Áp dụng bất đẳng thức: ${(ac + bd)^2} \le \left( {{c^2} + {d^2}} \right)\left( {{a^2} + {b^2}} \right).$

Đẳng thức xảy ra khi: $\frac{a}{c} = \frac{b}{d}.$

Ta có: ${(3\sin x + 4\cos x)^2}$ $\le \left( {{3^2} + {4^2}} \right)\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $= 25.$

$\Rightarrow – 5 \le 3\sin x + 4\cos x \le 5$ $\Rightarrow – 4 \le y \le 6.$

Vậy:

$\max y = 6$ đạt được khi $\tan x=\frac{3}{4}$

$\min y = – 4$ đạt được khi $\tan x=-\frac{3}{4}$

Chú ý: Với cách làm tương tự ta có được kết quả tổng quát sau:

$\max (a\sin x + b\cos x) = \sqrt {{a^2} + {b^2}} .$

$\min (a\sin x + b\cos x) = – \sqrt {{a^2} + {b^2}} .$

Tức là: $– \sqrt {{a^2} + {b^2}}$ $\le a\sin x + b\cos x$ $\le \sqrt {{a^2} + {b^2}} .$

## Bài 3. Chứng minh đẳng thức sau: $a\sin x + b\cos x$ $= \sqrt {{a^2} + {b^2}} \sin (x + \alpha ).$ Trong đó $\alpha \in [0;2\pi ]$ và $a$, $b$ không đồng thời bằng $0.$

Do $a$, $b$ không đồng thời bằng $0$ nên $\sqrt {{a^2} + {b^2}} \ne 0.$

Suy ra: $a\sin x + b\cos x$ $= \sqrt {{a^2} + {b^2}}\left( {\frac{a}{{\sqrt {{a^2} + {b^2}} }}\sin x + \frac{b}{{\sqrt {{a^2} + {b^2}} }}\cos x} \right).$

Vì ${\left( {\frac{a}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} + {\left( {\frac{b}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} = 1$ nên tồn tại số thực $\alpha \in [0;2\pi ]$ sao cho: $\frac{a}{{\sqrt {{a^2} + {b^2}} }} = \cos \alpha$, $\frac{b}{{\sqrt {{a^2} + {b^2}} }} = \sin \alpha .$

Khi đó: $a\sin x + b\cos x$ $= \sqrt {{a^2} + {b^2}} (\sin x\cos \alpha + \cos x\sin \alpha )$ $= \sqrt {{a^2} + {b^2}} \sin (x + \alpha ).$

Nhận xét: Từ kết quả trên, ta có:

Giá trị nhỏ nhất của hàm số $y = a\sin x + b\cos x$ bằng $– \sqrt {{a^2} + {b^2}} .$

Giá trị lớn nhất của hàm số $y = a\sin x + b\cos x$ bằng $\sqrt {{a^2} + {b^2}} .$

$– \sqrt {{a^2} + {b^2}}$ $\le a\sin x + b\cos x$ $\le \sqrt {{a^2} + {b^2}}$, $\forall x \in R.$

## Bài 4. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y=\sin x+\sqrt{2-\sin ^{2} x}$

## Bài tập 2. $y = {\tan ^2}x + {\cot ^2}x$ $+ 3(\tan x + \cot x) – 1.$

Ta có: $y \ge 0$, $\forall x$ và ${y^2} = 2 + 2\sin x\sqrt {2 – {{\sin }^2}x} .$

Mà $2\left| {\sin x\sqrt {2 – {{\sin }^2}x} } \right|$ $\le {\sin ^2}x + 2 – {\sin ^2}x = 2.$

Suy ra: $0 \le {y^2} \le 4$ $\Rightarrow 0 \le y \le 2.$

$\min y = 0$ đạt được khi $x = – \frac{\pi }{2} + k2\pi .$

$\max y = 2$ đạt được khi $x = \frac{\pi }{2} + k2\pi .$

2. Ta có: $y = {(\tan x + \cot x)^2}$ $+ 3(\tan x + \cot x) – 3.$

Đặt $t = \tan x + \cot x$ $= \frac{2}{{\sin 2x}}$ $\Rightarrow |t| \ge 2.$

Suy ra $y = {t^2} + 3t – 3 = f(t).$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/ham-so-luong-giac-va-cac-van-de-lien-quan-11.png" alt="">

Vậy $\min y = – 5$ đạt được khi $x = – \frac{\pi }{4} + k\pi .$

Không tồn tại $\max y.$

## Bài 5. Tìm $m$ để hàm số $y = \sqrt {5\sin 4x – 6\cos 4x + 2m – 1}$ xác định với mọi $x.$

Hàm số xác định với mọi $x$ $\Leftrightarrow 5\sin 4x – 6\cos 4x \ge 1 – 2m$, $\forall x.$

Do $\min (5\sin 4x – 6\cos 4x) = – \sqrt {61}$ $\Rightarrow – \sqrt {61} \ge 1 – 2m$ $\Leftrightarrow m \ge \frac{{\sqrt {61} + 1}}{2}.$

## Bài 6. Tìm tập giá trị lớn nhất, giá trị nhỏ nhất của các hàm số sau:

## Bài tập 1. $y = \frac{{\sin 2x + 2\cos 2x + 3}}{{2\sin 2x – \cos 2x + 4}}.$

## Bài tập 2. $y = \frac{{2{{\sin }^2}3x + 4\sin 3x\cos 3x + 1}}{{\sin 6x + 4\cos 6x + 10}}.$

## Bài tập 3. $y = \frac{{{{\sin }^2}2x + 3\sin 4x}}{{2{{\cos }^2}2x – \sin 4x + 2}}.$

## Bài tập 4. $y = 3{(3\sin x + 4\cos x)^2}$ $+ 4(3\sin x + 4\cos x) + 1.$

1. Ta có: $2\sin 2x – \cos 2x + 4$ $\ge 4 – \sqrt 5 > 0$, $\forall x \in R.$

$y = \frac{{\sin 2x + 2\cos 2x + 3}}{{2\sin 2x – \cos 2x + 4}}$ $\Leftrightarrow (2y – 1)\sin 2x$ $– (y + 2)\cos 2x = 3 – 4y.$

$\Rightarrow {(2y – 1)^2} + {(y + 2)^2}$ $\ge {(3 – 4y)^2}$ $\Leftrightarrow 11{y^2} – 24y + 4 \le 0$ $\Leftrightarrow \frac{2}{{11}} \le y \le 2.$

Suy ra: $\min y = \frac{2}{{11}}$, $\max y = 2.$

2. Ta có: $\sin 6x + 4\cos 6x + 10$ $\ge 10 – \sqrt {17} > 0$, $\forall x \in R.$

$y = \frac{{2\sin 6x – \cos 6x + 2}}{{\sin 6x + 4\cos 6x + 10}}$ $\Leftrightarrow (y – 2)\sin 6x + (4y + 1)\cos 6x$ $= 2 – 10y.$

$\Rightarrow {(y – 2)^2} + {(4y + 1)^2}$ $\ge {(2 – 10y)^2}$ $\Leftrightarrow 83{y^2} – 44y – 1 \le 0.$

$\Leftrightarrow \frac{{22 – 9\sqrt 7 }}{{83}} \le y \le \frac{{22 + 9\sqrt 7 }}{{83}}.$

Suy ra: $\min y = \frac{{22 – 9\sqrt 7 }}{{83}}$, $\max y = \frac{{22 + 9\sqrt 7 }}{{83}}.$

3. Ta có: $y = \frac{{6\sin 4x – \cos 4x + 1}}{{2\cos 4x – 2\sin 4x + 6}}$ (do $\cos 4x – \sin 4x + 3 > 0$, $\forall x \in R$).

$\Leftrightarrow (6 + 2y)\sin 4x – (1 + 2y)\cos 4x$ $= 6y – 1.$

$\Rightarrow {(6 + 2y)^2} + {(1 + 2y)^2}$ $\ge {(6y – 1)^2}$ $\Leftrightarrow 8{y^2} – 10y – 9 \le 0$ $\Leftrightarrow \frac{{5 – \sqrt {97} }}{8} \le y \le \frac{{5 + \sqrt {97} }}{8}.$

Vậy $\min y = \frac{{5 – \sqrt {97} }}{8}$, $\max y = \frac{{5 + \sqrt {97} }}{8}.$

## Bài tập 4. Đặt $t = 3\sin x + 4\cos x$ $\Rightarrow t \in [ – 5;5].$

Khi đó: $y = 3{t^2} + 4t + 1 = f(t)$ với $t \in [ – 5;5].$

Do đó: $\min y = f\left( { – \frac{2}{3}} \right) = – \frac{1}{3}$, $\max y = f(5) = 96.$

## Bài 7. Tìm $m$ để các bất phương trình sau đúng với mọi $x \in R.$

## Bài tập 1. $\frac{{3\sin 2x + \cos 2x}}{{\sin 2x + 4{{\cos }^2}x + 1}} \le m + 1.$

## Bài tập 2. $\frac{{4\sin 2x + \cos 2x + 17}}{{3\cos 2x + \sin 2x + m + 1}} \ge 2.$

## Bài tập 1. Đặt $y = \frac{{3\sin 2x + \cos 2x}}{{\sin 2x + 2\cos 2x + 3}}.$

Do $\sin 2x + 2\cos 2x + 3 > 0$, $\forall x$ $\Rightarrow$ hàm số xác định trên $R$).

$\Leftrightarrow (3 – y)\sin 2x + (1 – 2y)\cos 2x = 3y.$

Suy ra: ${(3 – y)^2} + {(1 – 2y)^2} \ge 9{y^2}$ $\Leftrightarrow 2{y^2} + 5y – 5 \le 0.$

$\Leftrightarrow \frac{{ – 5 – 3\sqrt 5 }}{4} \le y \le \frac{{ – 5 + 3\sqrt 5 }}{4}$ $\Rightarrow \max y = \frac{{ – 5 + 3\sqrt 5 }}{4}.$

Yêu cầu bài toán $\Leftrightarrow \frac{{ – 5 + 3\sqrt 5 }}{4} \le m + 1$ $\Leftrightarrow m \ge \frac{{3\sqrt 5 – 9}}{4}.$

## Bài tập 2. Trước hết ta có: $3\cos 2x + \sin 2x + m + 1 \ne 0$, $\forall x \in R.$

$\Leftrightarrow {3^2} + {1^2} < {(m + 1)^2}$ $\Leftrightarrow {m^2} + 2m – 9 > 0$
\Leftrightarrow \left[ {\begin{array}{l}
{m < – 1 – \sqrt {10} }\\
{m > – 1 + \sqrt {10} }
\end{array}} \right.
$$
 $(*).$

Với $m > – 1 + \sqrt {10}$ $\Rightarrow 3\cos 2x + \sin 2x + \mathop m\limits^. + 1 > 0$, $\forall x \in R.$

Nên $\frac{{4\sin 2x + \cos 2x + 17}}{{3\cos 2x + \sin 2x + m + 1}} \ge 2$ $\Leftrightarrow 2\sin 2x – 5\cos 2x \ge 2m – 15$ $\Leftrightarrow – \sqrt {29} \ge 2m – 15$ $\Leftrightarrow m \le \frac{{15 – \sqrt {29} }}{2}.$

Suy ra: $\sqrt {10} – 1 < m \le \frac{{15 – \sqrt {29} }}{2}.$

Với $m < – 1 – \sqrt {10}$ $\Rightarrow 3\cos 2x + \sin 2x + m + 1 < 0$, $\forall x \in R.$

Nên $\frac{{4\sin 2x + \cos 2x + 17}}{{3\cos 2x + \sin 2x + m + 1}} \ge 2$ $\Leftrightarrow 2\sin 2x – 5\cos 2x \le 2m – 15$ $\Leftrightarrow \sqrt {29} \le 2m – 15$ $\Leftrightarrow m \ge \frac{{15 + \sqrt {29} }}{2}$ (loại).

Vậy $\sqrt {10} – 1 < m \le \frac{{15 – \sqrt {29} }}{2}$ là những giá trị cần tìm.

## Bài 8. Cho $x,y \in \left( {0;\frac{\pi }{2}} \right)$ thỏa mãn $\cos 2x + \cos 2y + 2\sin (x + y) = 2.$ Tìm giá trị nhỏ nhất của $P = \frac{{{{\sin }^4}x}}{y} + \frac{{{{\cos }^4}y}}{x}.$

Ta có: $\cos 2x + \cos 2y + 2\sin (x + y) = 2$ $\Leftrightarrow {\sin ^2}x + {\sin ^2}y = \sin (x + y).$

Suy ra: $x+y=\frac{\pi}{2}.$

Áp dụng bất đẳng thức: $\frac{{{a^2}}}{m} + \frac{{{b^2}}}{n} \ge \frac{{{{(a + b)}^2}}}{{m + n}}.$

Suy ra: $P \ge \frac{{{{\left( {{{\sin }^2}x + {{\sin }^2}y} \right)}^2}}}{{x + y}} = \frac{2}{\pi }.$

Đẳng thức xảy ra $\Leftrightarrow x = y = \frac{\pi }{4}.$

Do đó: $\min P = \frac{2}{\pi }.$