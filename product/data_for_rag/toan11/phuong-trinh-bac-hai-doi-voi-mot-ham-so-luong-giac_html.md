# Phương trình bậc hai đối với một hàm số lượng giác

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
Bài viết hướng dẫn phương pháp giải các phương trình bậc hai đối với một hàm số lượng giác.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Bài toán 1: Giải và biện luận phương trình: $a.{\sin ^2}x + b.\sin x + c = 0$ $(1).$
PHƯƠNG PHÁP CHUNG: Ta biện luận theo các bước sau:

Bước 1: Đặt $\sin x = t$, điều kiện $|t| \le 1$, khi đó phương trình có dạng:

$f(t) = a.{t^2} + b.t + c = 0$ $(2).$

Bước 2: Xét tuỳ theo yêu cầu của bài toán:

1. Nếu bài toán yêu cầu giải phương trình thì ta giải phương trình $(2)$ theo $t$ và chọn nghiệm ${t_0}$ thoả mãn điều kiện $|t| \le 1.$

2. Nếu bài toán yêu cầu giải và biện luận phương trình theo tham số thì ta giải và biện luận phương trình $(2)$ theo $t$, điều kiện $|t| \le 1$, cụ thể:

+ Ta tính các biểu thức: $\Delta$, $af(1)$, $af( -1)$, $\frac{S}{2} – 1$, $\frac{S}{2} + 1.$

+ Lập bảng tổng kết:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac-1.png" alt="">

3. Nếu bài toán yêu cầu tìm giá trị của tham số để phương trình có nghiệm.

+ Trường hợp 1: $a = 0$, thử vào phương trình $\Rightarrow$ kết luận.

+ Trường hợp 2: $a \ne 0.$

$\Leftrightarrow$ phương trình $(2)$ có nghiệm thoả mãn $|t| \le 1.$

$$
\Leftrightarrow \left[ \begin{array}{l}
\left( 2 \right){\rm{\:có\:1\:nghiệm\:thuộc\:}}\left[ { – 1;1} \right]\\
\left( 2 \right){\rm{\:có\:2\:nghiệm\:thuộc\:}}\left[ { – 1;1} \right]
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
f( – 1)f(1) \le 0\\
\left\{ \begin{array}{l}
\Delta \ge 0\\
af( – 1) \ge 0\\
af(1) \ge 0\\
– 1 \le \frac{S}{2} \le 1
\end{array} \right.
\end{array} \right..
$$

4. Nếu bài toán yêu cầu tìm giá trị của tham số để phương trình có $k$ nghiệm thuộc $(\alpha ,\beta ).$

+ Trường hợp 1: Nếu $a = 0$, thử vào phương trình $\Rightarrow$ kết luận.

+ Trường hợp 2: Nếu $a \ne 0.$

Vì $x \in (\alpha ,\beta )$ $\Leftrightarrow t \in \left( {{\alpha _t},{\beta _t}} \right).$

Từ đó dựa vào tính chất nghiệm của phương trình $\sin x = \sin \gamma$ và đường tròn đơn vị biểu diễn khoảng $(\alpha ,\beta )$, ta có được điều kiện cần và đủ cho phương trình $(2).$

Chú ý:

1. Với các yêu cầu 3, 4 ta ưu tiên việc lựa chọn phương pháp hàm số để giải phương trình.

2. Phương pháp trên cũng được sử dụng để giải và biện luận phương trình: $a.{\cos ^2}x + b.\cos x + c = 0.$

3. Thông thường phương trình ban đầu chưa phải phương trình bậc hai theo một hàm số lượng giác, khi đó ta cần thực hiện một vài phép biến đổi lượng giác dựa trên nguyên tắc:

+ Nếu phương trình chứa nhiều hàm lượng giác khác nhau thì biến đổi tương đương về phương trình chỉ chứa một hàm

+ Nếu phương trình chứa các hàm lượng giác của nhiều cung khác nhau thì biến đổi tương đương về phương trình chỉ chứa các hàm lượng giác của một cung.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Ví dụ 1: (CĐSP Hà Nội – 1997): Giải phương trình: $\cos 2x + {\sin ^2}x + 2\cos x + 1 = 0.$

Biến đổi tương đương phương trình về dạng:

$2{\cos ^2}x – 1 + 1 – {\cos ^2}x + 2\cos x + 1 = 0$ $\Leftrightarrow {\cos ^2}x + 2\cos x + 1 = 0$ $\Leftrightarrow {(\cos x + 1)^2} = 0$ $\Leftrightarrow \cos x = – 1$ $\Leftrightarrow x = \pi + 2k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm $x = \pi + 2k\pi$, $k \in Z.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Ví dụ 2: Cho phương trình: $4{\sin ^2}2x + 8{\cos ^2}x – 5 + 3m = 0$ $(1).$

a. Giải phương trình với $m = – \frac{4}{3}.$

b. Tìm $m$ nguyên dương để phương trình có nghiệm.

Biến đổi phương trình về dạng:

$4\left( {1 – {{\cos }^2}2x} \right) + 4(1 + \cos 2x) – 5 + 3m = 0$ $\Leftrightarrow 4{\cos ^2}2x – 4\cos 2x – 3 – 3m = 0.$

Đặt $t = \cos 2x$, điều kiện $|t| \le 1.$

Khi đó, phương trình có dạng:

$4{t^2} – 4t – 3 – 3m = 0$ $\Leftrightarrow 4{t^2} – 4t – 3 = 3m$ $\left( 2 \right).$

a. Với $m = – \frac{4}{3}$, phương trình có dạng:

$4{t^2} – 4t + 1 = 0$ $\Leftrightarrow t = \frac{1}{2}$ $\Leftrightarrow \cos 2x = \frac{1}{2}$ $\Leftrightarrow 2x = \pm \frac{\pi }{3} + 2k\pi$ $\Leftrightarrow x = \pm \frac{\pi }{6} + 2k\pi$, $k \in Z.$

Vậy với $m = – \frac{4}{3}$, phương trình có hai họ nghiệm.

b. Ta lựa chọn một trong hai cách sau:

Cách 1: Phương trình $(1)$ có nghiệm $\Leftrightarrow (2)$ có nghiệm thuộc $[ – 1,1].$

$$
\Leftrightarrow \left[ \begin{array}{l}
\left( 2 \right){\rm{\:có\:1\:nghiệm\:thuộc\:}}\left[ { – 1;1} \right]\\
\left( 2 \right){\rm{\:có\:2\:nghiệm\:thuộc\:}}\left[ { – 1;1} \right]
\end{array} \right..
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
f( – 1).f(1) \le 0\\
\left\{ {\begin{array}{l}
{\Delta ‘ \ge 0}\\
{ af ( – 1) \ge 0}\\
{ af (1) \ge 0}\\
{ – 1 \le \frac{S}{2} \le 1}
\end{array}} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
(5 – 3m)( – 3 – 3m) \le 0\\
\left\{ {\begin{array}{l}
{16 + 12m \ge 0}\\
{5 – 3m \ge 0}\\
{ – 3 – 3m \ge 0}\\
{ – 1 \le \frac{1}{2} \le 1}
\end{array}} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
– 1 \le m \le 5/3\\
\left\{ {\begin{array}{l}
{m \ge – 4/3}\\
{m \le 5/3}\\
{m \le – 1}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow – \frac{4}{3} \le m \le \frac{5}{3}$ 
$$
\mathop \Leftrightarrow \limits^{m \in {Z^ + }} \left[ {\begin{array}{l}
{m = – 1}\\
{m = 0}\\
{m = 1}
\end{array}} \right..
$$

Vậy với $m = \pm 1$ hoặc $m = 0$ phương trình có nghiệm.

Cách 2: Phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = 3m$ cắt đồ thị hàm số $y = 4{t^2} – 4t – 3$ trên đoạn $[ – 1,1].$

Xét hàm số $y = 4{t^2} – 4t – 3$ trên đoạn $[ – 1,1].$

Đạo hàm:

$y’ = 8t – 4$, $y’ = 0$ $\Leftrightarrow 8t – 4 = 0$ $\Leftrightarrow t = \frac{1}{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac-2.png" alt="">

Dựa vào bảng biến thiên, ta được điều kiện là:

$– 4 \le 3m \le 5$ $\Leftrightarrow – \frac{4}{3} \le m \le \frac{5}{3}$ 
$$
\mathop \Leftrightarrow \limits^{m \in {Z^ + }} \left[ {\begin{array}{l}
{m = – 1}\\
{m = 0}\\
{m = 1}
\end{array}} \right..
$$

Vậy với $m = \pm 1$ hoặc $m =0$ phương trình có nghiệm.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Ví dụ 3: Cho phương trình: ${\sin ^2}3x + \left( {{m^2} – 3} \right)\sin 3x + {m^2} – 4 = 0$ $(1).$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình có đúng $4$ nghiệm thuộc $\left[ {\frac{{2\pi }}{3},\frac{{4\pi }}{3}} \right].$

Đặt $t = \sin 3x$, điều kiện $|t| \le 1.$

Khi đó phương trình có dạng:

${t^2} + \left( {{m^2} – 3} \right)t + {m^2} – 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 4 – {m^2}}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin 3x = – 1}\\
{\sin 3x = 4 – {m^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{6} + \frac{{2k\pi }}{3}}\\
{\sin 3x = 4 – {m^2}\:(2)}
\end{array}} \right.
$$
, $k \in Z.$

a. Với $m = 1$, phương trình $(2)$ có dạng: $\sin 3x = 3$ vô nghiệm.

Vậy với $m = 1$ phương trình có nghiệm $x = – \frac{\pi }{6} + \frac{{2k\pi }}{3}$, $k \in Z.$

b. Trước hết nghiệm: $x = – \frac{\pi }{6} + \frac{{2k\pi }}{3} \in \left[ {\frac{{2\pi }}{3};\frac{{4\pi }}{3}} \right]$ là ${x_1} = \frac{{7\pi }}{6}.$

Vậy để phương trình $(1)$ có đúng $4$ nghiệm thuộc $\left[ {\frac{{2\pi }}{3},\frac{{4\pi }}{3}} \right]$ điều kiện là phương trình $(2)$ có đúng $3$ nghiệm khác $\frac{{7\pi }}{6}$ thuộc $\left[ {\frac{{2\pi }}{3},\frac{{4\pi }}{3}} \right].$

Vì $x \in \left[ {\frac{{2\pi }}{3},\frac{{4\pi }}{3}} \right] \Leftrightarrow 3x \in [2\pi ,4\pi ]$, do đó điều kiện là:

$\sin 3x = 0$ $\Leftrightarrow 4 – {m^2} = 0$ $\Leftrightarrow m = \pm 2.$

Khi đó ta được các nghiệm $3x \in [2\pi ,3\pi ,4\pi ]$ $\Leftrightarrow x \in \left[ {\frac{{2\pi }}{3},\pi ,\frac{{4\pi }}{3}} \right].$

Vậy với $m = \pm 2$ phương trình $(1)$ có $4$ nghiệm thuộc $\left[ {\frac{{2\pi }}{3},\frac{{4\pi }}{3}} \right].$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Bài toán 2: Giải và biện luận phương trình: $a.{\tan ^2}x + b.\tan x + c = 0$ $(1).$

PHƯƠNG PHÁP CHUNG: Ta biện luận theo các bước sau:

Bước 1: Đặt điều kiện $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Bước 2: Đặt $\tan x = t$, khi đó phương trình có dạng:

$a.{t^2} + b.t + c = 0$ $\left( 2 \right).$

Bước 3: Giải và biện luận phương trình $(2)$ theo $t.$

Chú ý:

1. Phương pháp trên được sử dụng để giải và biện luận phương trình: $a.{\cot ^2}x + b. \cot x + c = 0$ với điều kiện $\sin x \ne 0 \Leftrightarrow x \ne k\pi$, $k \in Z.$

2. Ưu tiên lựa chọn phương pháp hàm số để giải.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Ví dụ 4: Giải phương trình: $\sqrt 3 {\cot ^2}x – 4 \cot x + \sqrt 3 = 0.$

Điều kiện: $\sin x \ne 0 \Leftrightarrow x \ne k\pi$, $k \in Z.$

Đặt $\cot x = t$, khi đó phương trình có dạng:

$\sqrt 3 {t^2} – 4t + \sqrt 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \sqrt 3 }\\
{t = \frac{1}{{\sqrt 3 }}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cot x = \sqrt 3 }\\
{\cot x = \frac{1}{{\sqrt 3 }}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{6} + k\pi }\\
{x = \frac{\pi }{3} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm $x = \pi + 2k\pi$, $k \in Z.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Ví dụ 5: Cho phương trình: $\frac{{{m^2} – 1}}{{{{\cos }^2}x}} – 2m\tan x – {m^2} + 2 = 0$ $(1).$

a. Giải phương trình với $m = 2.$

b. Tìm $m$ để phương trình có đúng ba nghiệm thuộc $\left( { – \pi ,\frac{\pi }{2}} \right).$

Điều kiện: $\cos x \ne 0 \Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$\left( {{m^2} – 1} \right)\left( {1 + {{\tan }^2}x} \right) – 2m\tan x – {m^2} + 2 = 0$ $\Leftrightarrow \left( {{m^2} – 1} \right){\tan ^2}x – 2m\tan x + 1 = 0.$

Đặt $\tan x = t$, khi đó phương trình có dạng:

$\left( {{m^2} – 1} \right){t^2} – 2mt + 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{(m – 1)t = 1}\\
{(m + 1)t = 1}
\end{array}} \right.
$$
 $(2).$

a. Với $m = 2$, ta được:

$$
\left[ {\begin{array}{l}
{t = 1}\\
{t = \frac{1}{3}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 1 = \tan \frac{\pi }{4}}\\
{\tan x = \frac{1}{3} = \tan \alpha }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{4} + k\pi }\\
{x = \alpha + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = 2$, phương trình có hai họ nghiệm.

b. Để phương trình có đúng ba nghiệm thuộc $\left( { – \pi ,\frac{\pi }{2}} \right)$ $\Leftrightarrow (2)$ có hai nghiệm trái dấu 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne \pm 1}\\
{\frac{1}{{m – 1}}.\frac{1}{{m + 1}} < 0}
\end{array}} \right.
$$
 $\Leftrightarrow {m^2} – 1 < 0$ $\Leftrightarrow |m| < 1.$

Vậy với $|m| < 1$ thoả mãn điều kiện đầu bài.

<!-- chunk:8 level:1 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: (ĐHCSND – 99): Tìm các nghiệm thoả mãn điều kiện $\cos x \ge 0$ của phương trình: $1 – 5\sin x + 2{\cos ^2}x = 0.$

Biến đổi phương trình về dạng:

$1 – 5\sin x + 2\left( {1 – {{\sin }^2}x} \right) = 0$ $\Leftrightarrow 2{\sin ^2}x + 5\sin x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x = 3{\rm{\:(loại)\:}}}\\
{\sin x = \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{6} + 2k\pi }\\
{x = \frac{{5\pi }}{6} + 2k\pi }
\end{array}} \right..
$$

<img link="data_for_rag/toan11/images/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac-3.png" alt="">

Bằng cách biểu diễn các họ nghiệm trên lên đường tròn đơn vị ta thấy nghiệm $x = \frac{\pi }{6} + 2k\pi$, $k \in Z$ thoả mãn điều kiện $\cos x \ge 0.$

Chú ý: Các em học sinh cũng có thể kiểm tra bằng phương pháp đại số như sau:

+ Với $x = \frac{\pi }{6} + 2k\pi$ $\Rightarrow \cos x = \cos \left( {\frac{\pi }{6} + 2k\pi } \right)$ $= \cos \frac{\pi }{6} = \frac{{\sqrt 3 }}{2} > 0$ thỏa mãn.

+ Với $x = \frac{{5\pi }}{6} + 2k\pi$ $\Rightarrow \cos x = \cos \left( {\frac{{5\pi }}{6} + 2k\pi } \right)$ $= \cos \frac{{5\pi }}{6} = – \frac{{\sqrt 3 }}{2} < 0$ loại.

Vậy họ nghiệm của phương trình thoả mãn điều kiện $\cos x \ge 0$ là $x = \frac{\pi }{6} + 2k\pi .$

## Bài 2: (ĐH Đà Nẵng – 96): Cho phương trình: ${\cos ^2}x – (2m + 1)\cos x + m + 1 = 0$ $(1).$

a. Giải phương trình với $m = \frac{3}{2}.$

b. Tìm $m$ để phương trình có nghiệm thuộc $\left[ {\frac{\pi }{2},\frac{{3\pi }}{2}} \right].$

Đặt $t = \cos x$, điều kiện $|t| \le 1.$

Khi đó phương trình có dạng:

${t^2} – (2m + 1)t + m + 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{1}{2}}\\
{t = m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos x = \frac{1}{2}}\\
{\cos x = m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \pm \frac{\pi }{3} + k\pi }\\
{\cos x = m\:\left( * \right)}
\end{array}} \right.
$$
, $k \in Z.$

a. Với $m = \frac{3}{2}$, phương trình $(*)$ vô nghiệm.

Vậy với $m = \frac{3}{2}$ phương trình có hai họ nghiệm $x = \pm \frac{\pi }{3} + 2k\pi$, $k \in Z.$

b. Với $x \in \left[ {\frac{\pi }{2},\frac{{3\pi }}{2}} \right]$ $\Rightarrow – 1 \le \cos x \le 0.$

Do đó, phương trình $(1)$ có nghiệm thuộc $\left[ {\frac{\pi }{2},\frac{{3\pi }}{2}} \right]$ $\Leftrightarrow – 1 \le m < 0.$

## Bài 3: (CĐCN IV TPHCM – 2000): Cho phương trình: ${\cos ^2}x + 2(1 – m)\cos x + 2m – 1 = 0$ $(1).$

a. Giải phương trình với $m = \frac{1}{2}.$

b. Tìm $m$ để phương trình có $4$ nghiệm thuộc $[0,2\pi ].$

a. Với $m = \frac{1}{2}$, phương trình có dạng:

${t^2} + t = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos x = 0}\\
{\cos x = – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{2} + k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

b. Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Phương trình $(1)$ có $4$ nghiệm thuộc $[0,2\pi ]$ $\Leftrightarrow$ phương trình $(2)$ có $2$ nghiệm thoả mãn $– 1 < {t_1} < {t_2} \le 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta’ > 0}\\
{ af ( – 1) > 0}\\
{ af (1) \ge 0}\\
{ – 1 < \frac{S}{2} < 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} – 4m + 2 > 0}\\
{4m – 2 > 0}\\
{2 \ge 0}\\
{ – 1 < m – 1 < 1}
\end{array}} \right.
$$
 $\Leftrightarrow \frac{1}{2} < m < 2 – \sqrt 2 .$

Vậy với $\frac{1}{2} < m < 2 – \sqrt 2$ phương trình $(1)$ có $4$ nghiệm thuộc $[0,2\pi ].$

Cách 2: Biến đổi $(2)$ về dạng:

${t^2} + 2t – 1 = 2m(t – 1)$ $\Leftrightarrow \frac{{{t^2} + 2t – 1}}{{t – 1}} = 2m$ ($t=1$ không là nghiệm).

Phương trình $(1)$ có $4$ nghiệm thuộc $[0,2\pi ] \Leftrightarrow$ đường thẳng $y = 2m$ cắt đồ thị hàm số $y = \frac{{{t^2} + 2t – 1}}{{t – 1}}$ trên $( – 1,1)$ tại $2$ điểm phân biệt.

Xét hàm số $y = \frac{{{t^2} + 2t – 1}}{{t – 1}}$ trên $( – 1,1).$

Đạo hàm: $y’ = \frac{{{t^2} – 2t – 1}}{{{{(t – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {t^2} – 2t – 1 = 0$ $\Leftrightarrow t = 1 \pm \sqrt 2 .$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac-4.png" alt="">

Dựa vào bảng biến thiên, ta được điều kiện là:

$1 < 2m < 4 – 2\sqrt 2$ $\Leftrightarrow \frac{1}{2} < m < 2 – \sqrt 2 .$

Vậy với $\frac{1}{2} < m < 2 – \sqrt 2$ phương trình $(1)$ có $4$ nghiệm thuộc $[0,2\pi ].$

## Bài 4: (HVKTQS – 2001): Giải phương trình: $3 {\cot ^2}x + 2\sqrt 2 {\sin ^2}x = (2 + 3\sqrt 2 )\cos x$ $(1).$

Biến đổi phương trình về dạng:

$\left( {3 {{\cot }^2}x – 3\sqrt 2 \cos x} \right) + \left( {2\sqrt 2 {{\sin }^2}x – 2\cos x} \right) = 0.$

$\Leftrightarrow 3\left( {\frac{{\cos x}}{{{{\sin }^2}x}} – \sqrt 2 } \right)\cos x + 2\left( {\sqrt 2 {{\sin }^2}x – \cos x} \right) = 0.$

$\Leftrightarrow 3\left( {\cos x – \sqrt 2 {{\sin }^2}x} \right)\cos x$ $+ 2\left( {\sqrt 2 {{\sin }^2}x – \cos x} \right){\sin ^2}x = 0.$

$\Leftrightarrow \left( {\cos x – \sqrt 2 {{\sin }^2}x} \right)\left( {3\cos x – 2{{\sin }^2}x} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sqrt 2 {{\cos }^2}x + \cos x – \sqrt 2 = 0}\\
{2{{\cos }^2}x + 3\cos x – 2 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos x = \frac{{\sqrt 2 }}{2}}\\
{\cos x = \frac{1}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \pm \frac{\pi }{4} + 2k\pi }\\
{x = \pm \frac{\pi }{3} + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có bốn họ nghiệm.

## Bài 5: Giải và biện luận phương trình: $(m – 1){\sin ^2}x – 2(m + 1)\cos x + 2m – 1 = 0$ $(1).$

Biến đổi phương trình về dạng:

$(m – 1)\left( {1 – {{\cos }^2}x} \right) – 2(m + 1)\cos x + 2m – 1 = 0.$

$\Leftrightarrow (m – 1){\cos ^2}x + 2(m + 1)\cos x – 3m + 2 = 0.$

Đặt $t = \cos x$, điều kiện $|t| \le 1.$

Khi đó phương trình có dạng:

$(m – 1){t^2} + 2(m + 1)t – 3m + 2 = 0$ $(2).$

Ta đi xác định các giá trị:

$\Delta ‘ = {(m + 1)^2} + (3m – 2)(m – 1)$ $= 4{m^2} – 3m + 3.$

$af( – 1) = (m – 1)( – 4m – 1).$

$af (1) = 3(m – 1).$

$\frac{S}{2} – 1 = – \frac{{m + 1}}{{m – 1}} – 1 = – \frac{{2m}}{{m – 1}}.$

$\frac{S}{2} + 1 = – \frac{{m + 1}}{{m – 1}} + 1 = – \frac{2}{{m – 1}}.$

Ta có bảng tổng kết sau:

<img link="data_for_rag/toan11/images/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac-5.png" alt="">

Vậy:

+ Với $m < – \frac{1}{4}$, phương trình vô nghiệm.

+ Với $m = – \frac{1}{4}$, phương trình có nghiệm: ${t_1} = – 1 \Leftrightarrow x = \pi + 2k\pi$, $k \in Z.$

+ Với $– \frac{1}{4} < m < 1$, phương trình có nghiệm: ${t_1} = \frac{{ – m – 1 – \sqrt {4{m^2} – 3m + 3} }}{{m – 1}}$ $\Leftrightarrow \cos x = {t_1} = \cos \alpha$ $\Leftrightarrow x = \pm \alpha + 2k\pi$, $k \in Z.$

+ Với $m = 1$, phương trình có nghiệm:

$t = \frac{1}{4} \Leftrightarrow \cos x = \frac{1}{4} = \cos \beta$ $\Leftrightarrow x = \pm \beta + 2k\pi$, $k \in Z.$

+ Với $m> 1$, phương trình có nghiệm: ${t_2} = \frac{{ – m – 1 + \sqrt {4{m^2} – 3m + 3} }}{{m – 1}}$ $\Leftrightarrow \cos x = {t_2} = \cos \gamma$ $\Leftrightarrow x = \pm \gamma + 2k\pi$, $k \in Z.$

<!-- chunk:9 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Bài tập 1: Cho phương trình: $5 – 4{\sin ^2}x – 8{\cos ^2}\frac{x}{2} = 3m.$

a. Giải phương trình với $m = – \frac{4}{3}.$

b. Tìm $m$ nguyên dương để phương trình có nghiệm.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Bài tập 2: Cho phương trình: $\cos 2x + 5\sin x + m = 0.$

a. (ĐHNN Hà Nội – 1997): Giải phương trình với $m = 2.$

b. Tìm $m$ nguyên dương để phương trình có nghiệm.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/08/phuong-trinh-bac-hai-doi-voi-mot-ham-so-luong-giac.html -->
## Bài tập 3: Cho phương trình: $4{\cos ^2}x – 2(m – 1)\cos x – m = 0.$

a. Giải phương trình với $m = \sqrt 3 .$

b. Tìm $m$ nguyên dương để phương trình có nghiệm.