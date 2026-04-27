# Giải phương trình lượng giác bằng cách đặt ẩn phụ

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
Bài viết hướng dẫn giải phương trình lượng giác bằng cách đặt ẩn phụ thông qua các ví dụ minh họa có lời giải chi tiết.

Phương pháp đặt ẩn phụ giải phương trình lượng giác: Để giải một phương trình lượng giác bằng phương pháp đặt ẩn phụ, ta sử dụng $2$ kỹ thuật đặt ẩn phụ thường gặp sau:

+ Chọn góc để đặt ẩn phụ, đưa phương trình lượng giác đã cho về một phương trình lượng giác đơn giản hơn (phương trình lượng giác cơ bản, phương trình lượng giác thường gặp, …).

+ Chọn biểu thức lượng giác để đặt ẩn phụ, đưa phương trình lượng giác đã cho về phương trình (hoặc hệ phương trình) đại số.

1. Chọn góc để đặt ẩn phụ

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
## Ví dụ 1. Giải các phương trình lượng giác sau:

a. $\sin \left( {\frac{{3\pi }}{{10}} – \frac{x}{2}} \right)$ $= \frac{1}{2}\sin \left( {\frac{\pi }{{10}} + \frac{{3x}}{2}} \right).$

b. $\cos x – 2\sin \left( {\frac{{3\pi }}{2} – \frac{x}{2}} \right) = 3.$

c. $\sin \left( {3x – \frac{\pi }{4}} \right)$ $= \sin 2x.\sin \left( {x + \frac{\pi }{4}} \right).$

d. $\sin \left( {\frac{{5x}}{2} – \frac{\pi }{4}} \right) – \cos \left( {\frac{x}{2} – \frac{\pi }{4}} \right)$ $= \sqrt 2 \cos \frac{{3x}}{2}.$

a. Nhận xét: Nhìn vào phương trình này ta nghĩ ngay đến việc dùng công thức biến đổi $sin$ của một tổng … nhưng đừng vội làm như thế, ta xem mối quan hệ giữa hai cung $\left( {\frac{{3\pi }}{{10}} – \frac{x}{2}} \right)$ và $\left( {\frac{\pi }{{10}} + \frac{{3x}}{2}} \right)$ có quan hệ với nhau như thế nào?

Thật vậy, nếu ta đặt $t = \frac{{3\pi }}{{10}} – \frac{x}{2}$ $\Rightarrow 3t = \frac{{9\pi }}{{10}} – \frac{{3x}}{2}$ $= \pi – \left( {\frac{\pi }{{10}} + \frac{{3x}}{2}} \right)$ thì khi đó sử dụng công thức góc nhân ba là biến đổi dễ dàng.

Đặt $t = \frac{{3\pi }}{{10}} – \frac{x}{2}$ $\Rightarrow \frac{\pi }{{10}} + \frac{{3x}}{2} = \pi – 3t.$

$PT \Leftrightarrow \sin t = \frac{1}{2}\sin \left( {\pi – 3t} \right)$ $\Leftrightarrow \sin t = \frac{1}{2}\sin 3t$

$\Leftrightarrow \sin t = \frac{1}{2}\left( {3\sin t – 4{{\sin }^3}t} \right)$ $\Leftrightarrow \sin t\left( {1 – 4{{\sin }^2}t} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\sin t = 0\\
\sin t = \frac{1}{2}\\
\sin t = – \frac{1}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = k\pi \\
t = \frac{\pi }{6} + k2\pi \\
t = \frac{{5\pi }}{6} + k2\pi \\
t = \frac{{ – \pi }}{6} + k2\pi \\
t = \frac{{7\pi }}{6} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Thay $x = \frac{{3\pi }}{5} – 2t$, suy ra phương trình đã cho có nghiệm: $x = \frac{{3\pi }}{5} – k2\pi$, $x = \frac{{4\pi }}{{15}} – k4\pi$, $x = \frac{{ – 16\pi }}{{15}} – k4\pi$, $x = \frac{{14\pi }}{{15}} – k4\pi$, $x = \frac{{ – 26\pi }}{{15}} – k4\pi$ $\left( {k \in Z} \right).$

b. Đặt $t = \frac{{3\pi }}{2} – \frac{x}{2}$ $\Rightarrow x = 3\pi – 2t.$

$PT \Leftrightarrow \cos \left( {3\pi – 2t} \right)$ $– 2\sin t = 3$ $\Leftrightarrow – \cos 2t – 2\sin t = 3$

$\Leftrightarrow 2{\sin ^2}t – 1 – 2\sin t = 3$ $\Leftrightarrow {\sin ^2}t – \sin t – 2 = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\sin t = – 1\\
\sin t = 2 (loại)
\end{array} \right.
$$
 $\Leftrightarrow t = \frac{{ – \pi }}{2} + k2\pi$ $\left( {k \in Z} \right).$

Thay $x = 3\pi – 2t$, suy ra phương trình đã cho có nghiệm: $x = 4\pi + k4\pi$ $\left( {k \in Z} \right)$, hay có thể viết gọn $x = l4\pi$ $\left( {l \in Z} \right).$

c. Đặt $t = x + \frac{\pi }{4}$ $\Rightarrow x = t – \frac{\pi }{4}$ $\Rightarrow 3x – \frac{\pi }{4} = 3t – \pi .$

$PT \Leftrightarrow \sin \left( {3t – \pi } \right)$ $= \sin \left( {2t – \frac{\pi }{2}} \right).\sin t$ $\Leftrightarrow – \sin 3t = – \cos 2t.\sin t$

$\Leftrightarrow \sin 3t = \frac{1}{2}\sin 3t + \frac{1}{2}\sin \left( { – t} \right)$ $\Leftrightarrow \sin 3t = \sin \left( { – t} \right)$

$$
\Leftrightarrow \left[ \begin{array}{l}
3t = – t + k2\pi \\
3t = \pi + t + k2\pi
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = k\frac{\pi }{2}\\
t = \frac{\pi }{2} + k\pi
\end{array} \right.
$$
 $\Leftrightarrow t = k\frac{\pi }{2}\left( {k \in Z} \right).$

Thay $x = t – \frac{\pi }{4}$, suy ra phương trình đã cho có nghiệm: $x = \frac{{ – \pi }}{4} + k\frac{\pi }{2}$ $\left( {k \in Z} \right).$

d. Đặt $t = \frac{x}{2} – \frac{\pi }{4}$ $\Rightarrow x = 2t + \frac{\pi }{2}$ $\Rightarrow \frac{{3x}}{2} = 3t + \frac{{3\pi }}{4}$, $\frac{{5x}}{2} – \frac{\pi }{4} = 5t + \pi .$

$PT \Leftrightarrow \sin \left( {5t + \pi } \right) – \cos t$ $= \sqrt 2 \cos \left( {3t + \frac{{3\pi }}{4}} \right)$ $\Leftrightarrow \sin 5t + \cos t$ $= \cos 3t + \sin 3t$

$\Leftrightarrow \sin 5t – \sin 3t$ $= \cos 3t – \cos t$ $\Leftrightarrow 2\cos 4t\sin t$ $= – 2\sin 2t\sin t$

$\Leftrightarrow \cos 4t\sin t + \sin 2t\sin t = 0$ $\Leftrightarrow \sin t\left( {\cos 4t + \sin 2t} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\sin t = 0\\
\cos 4t + \sin 2t = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
\sin t = 0\\
\sin \left( {\frac{\pi }{2} – 4t} \right) – \sin \left( { – 2t} \right) = 0
\end{array} \right.
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
\sin t = 0\\
\sin \left( {\frac{\pi }{2} – 4t} \right) = \sin \left( { – 2t} \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = k\pi \\
t = \frac{\pi }{4} – k\pi \\
t = \frac{{ – \pi }}{{12}} – k\frac{\pi }{3}
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Thay $x = 2t + \frac{\pi }{2}$, suy ra phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{2} + k2\pi \\
x = \pi – k2\pi \\
x = \frac{\pi }{3} – k\frac{{2\pi }}{3}
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
## Ví dụ 2. Giải các phương trình lượng giác sau:

a. $8{\cos ^3}\left( {x + \frac{\pi }{3}} \right) = \cos 3x.$

b. ${\tan ^3}\left( {x – \frac{\pi }{4}} \right) = \tan x – 1.$

a. Đặt $t = x + \frac{\pi }{3}$ $\Rightarrow x = t – \frac{\pi }{3}$ $\Rightarrow 3x = 3t – \pi .$

$PT \Leftrightarrow 8{\cos ^3}t = \cos \left( {3t – \pi } \right)$ $\Leftrightarrow 8{\cos ^3}t = – \cos 3t$

$\Leftrightarrow 8{\cos ^3}t = 3\cos t – 4{\cos ^3}t$ $\Leftrightarrow \cos t\left( {12{{\cos }^2}t – 3} \right) = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\cos t = 0\\
\cos t = \frac{1}{2}\\
\cos t = \frac{{ – 1}}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = \frac{\pi }{2} + k\pi \\
t = \frac{\pi }{3} + k2\pi \\
t = \frac{{ – \pi }}{3} + k2\pi \\
t = \frac{{2\pi }}{3} + k2\pi \\
t = \frac{{ – 2\pi }}{3} + k2\pi
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = \frac{\pi }{2} + k\pi \\
t = \frac{\pi }{3} + k\pi \\
t = \frac{{2\pi }}{3} + k\pi
\end{array} \right.
$$
 $(k∈Z).$

Thay $x = t – \frac{\pi }{3}$, suy ra phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{6} + k\pi \\
x = k\pi \\
x = \frac{\pi }{3} + k\pi
\end{array} \right.
$$
 $(k∈Z).$

b. Điều kiện: 
$$
\left\{ \begin{array}{l}
\cos \left( {x – \frac{\pi }{4}} \right) \ne 0\\
\cos x \ne 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \ne \frac{{3\pi }}{4} + k\pi \\
x \ne \frac{\pi }{2} + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Đặt $t = x – \frac{\pi }{4}$ $\Rightarrow x = t + \frac{\pi }{4}.$

$PT \Leftrightarrow {\tan ^3}t$ $= \tan \left( {t + \frac{\pi }{4}} \right) – 1$ $\Leftrightarrow {\tan ^3}t = \frac{{\tan t + 1}}{{1 – \tan t}} – 1$

$\Leftrightarrow {\tan ^3}t = \frac{{2\tan t}}{{1 – \tan t}}$ $\Leftrightarrow {\tan ^3}t\left( {1 – \tan t} \right) – 2\tan t = 0$

$\Leftrightarrow \tan t\left( {{{\tan }^2}t – {{\tan }^3}t – 2} \right) = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\tan t = 0\\
\tan t = – 1
\end{array} \right.
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
t = k\pi \\
t = \frac{{ – \pi }}{4} + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Thay $x = t + \frac{\pi }{4}$, suy ra phương trình đã cho có nghiệm 
$$
\left[ \begin{array}{l}
x = k\pi \\
x = \frac{\pi }{4} + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

[ads]

2. Chọn biểu thức lượng giác để đặt ẩn phụ

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
## Ví dụ 3. Giải các phương trình lượng giác sau:

a. $3\sin x + 4\cos x$ $+ \frac{6}{{3\sin x + 4\cos x + 1}} = 6.$

b. $\sin x + \sqrt 3 \cos x$ $+ \sqrt {\sin x + \sqrt 3 \cos x} = 2.$

c. ${\cos ^2}x + \frac{1}{{{{\cos }^2}x}}$ $= \cos x + \frac{1}{{\cos x}}.$

d. $2{\cos ^2}2x + \cos 2x$ $= 4{\sin ^2}2x{\cos ^2}x.$

e. $1 + 3\tan x = 2\sin 2x.$

a. Nhận xét: Nhận thấy biểu thức $3\sin x+4\cos x$ xuất hiện $2$ lần, ta đặt $t=3\sin x+4\cos x+1$ vừa giúp chuyển phương trình đã cho về phương trình ẩn $t$, vừa làm gọn mẫu số.

Điều kiện: $3\sin x+4\cos x+1\ne 0.$

Đặt $t=3\sin x+4\cos x+1$ $\left( t\ne 0 \right).$

$PT \Leftrightarrow t – 1 + \frac{6}{t} = 6$ $\Leftrightarrow {t^2} – 7t + 6 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = 1\\
t = 6
\end{array} \right.
$$

+ Với $t = 1$, ta có: $3\sin x + 4\cos x = 0$ $\Leftrightarrow \frac{3}{5}\sin x + \frac{4}{5}\cos x = 0.$

Gọi $\alpha$ là giá trị thỏa mãn: 
$$
\left\{ \begin{array}{l}
\cos \alpha = \frac{3}{5}\\
\sin \alpha = \frac{4}{5}
\end{array} \right.
$$

$\frac{3}{5}\sin x + \frac{4}{5}\cos x = 0$ $\Leftrightarrow \cos \alpha .\sin x + \sin \alpha .\cos x = 0$

$\Leftrightarrow \sin \left( {x + \alpha } \right) = 0$ $\Leftrightarrow x = – \alpha + k\pi$ $\left( {k \in Z} \right).$

+ Với $t = 6$, ta có: $3\sin x + 4\cos x = 5$ $\Leftrightarrow \frac{3}{5}\sin x + \frac{4}{5}\cos x = 1$

$\Leftrightarrow \cos \alpha .\sin x + \sin \alpha .\cos x = 1$ $\Leftrightarrow \sin \left( {x + \alpha } \right) = 1$ $\Leftrightarrow x = \frac{\pi }{2} – \alpha + k2\pi$ $\left( {k \in Z} \right).$

Vậy phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = – \alpha + k\pi \\
x = \frac{\pi }{2} – \alpha + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

b. Điều kiện: $\sin x + \sqrt 3 \cos x \ge 0.$

Đặt $t = \sqrt {\sin x + \sqrt 3 \cos x}$ $\left( {t \ge 0} \right).$

$PT \Leftrightarrow {t^2} + t = 2$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = 1\\
t = – 2 \left( {loại} \right)
\end{array} \right.
$$

Với $t = 1$, ta có: $\sin x + \sqrt 3 \cos x = 1$ $\Leftrightarrow \frac{1}{2}\sin x + \frac{{\sqrt 3 }}{2}\cos x = \frac{1}{2}$

$\Leftrightarrow \sin \left( {x + \frac{\pi }{3}} \right) = \frac{1}{2}$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{{ – \pi }}{6} + k2\pi \\
x = \frac{\pi }{2} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = \frac{{ – \pi }}{6} + k2\pi \\
x = \frac{\pi }{2} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

c. Điều kiện: $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$ $\left( {k \in Z} \right).$

Đặt $t = \cos x + \frac{1}{{\cos x}}$ $\Rightarrow {t^2} = {\cos ^2}x + \frac{1}{{{{\cos }^2}x}} + 2.$

$PT \Leftrightarrow {t^2} – 2 = t$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = – 1\\
t = 2
\end{array} \right.
$$

+ Với $t = – 1$, ta có: $\cos x + \frac{1}{{\cos x}} = – 1$ $\Leftrightarrow {\cos ^2}x + \cos x + 1 = 0$ $(PTVN).$

+ Với $t = 2$, ta có: $\cos x + \frac{1}{{\cos x}} = 2$ $\Leftrightarrow {\cos ^2}x – 2\cos x + 1 = 0$ $\Leftrightarrow \cos x = 1$ $\Leftrightarrow x = k2\pi$ $\left( {k \in Z} \right).$

Vậy phương trình đã cho có nghiệm: $\Leftrightarrow x = k2\pi$ $\left( {k \in Z} \right).$

d. $PT \Leftrightarrow 2{\cos ^2}2x + \cos 2x$ $= 2\left( {1 – {{\cos }^2}2x} \right)\left( {1 + \cos 2x} \right).$

Đặt $t = \cos 2x$, $\left| t \right| \le 1.$

$PT \Leftrightarrow 2{t^2} + t$ $= 2\left( {1 – {t^2}} \right)\left( {1 + t} \right)$ $\Leftrightarrow 2{t^3} + 4{t^2} – t – 2 = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
t = – 2 \left( {loại} \right)\\
t = \frac{{\sqrt 2 }}{2}\\
t = \frac{{ – \sqrt 2 }}{2}
\end{array} \right.
$$

Thay $t = \cos 2x$, suy ra phương trình đã cho có nghiệm: 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{8} + k\pi \\
x = \frac{{ – \pi }}{8} + k\pi \\
x = \frac{{3\pi }}{8} + k\pi \\
x = \frac{{ – 3\pi }}{8} + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

e. Điều kiện: $\cos x \ne 0.$

Đặt $t = \tan x$ $\Rightarrow \sin 2x = \frac{{2t}}{{1 + {t^2}}}.$

$PT \Leftrightarrow 1 + 3t = \frac{{4t}}{{1 + {t^2}}}$ $\Leftrightarrow \left( {1 + 3t} \right)\left( {1 + {t^2}} \right) = 4t$

$\Leftrightarrow 3{t^3} + {t^2} – t + 1 = 0$ $\Leftrightarrow t = – 1.$

Thay $t = \tan x$, suy ra phương trình đã cho có nghiệm $x = \frac{{ – \pi }}{4} + k\pi$ $\left( {k \in Z} \right).$

**Lưu ý**: Một số phương trình lượng giác được giải bằng cách **đặt ẩn phụ không hoàn toàn**, tức là sau khi đặt ẩn phụ, ẩn cũ và ẩn mới cùng tồn tại trong phương trình (biểu thức chứa ẩn cũ còn lại ấy được xem là tham số của phương trình). Ta xét một số ví dụ sau đây:

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
## Ví dụ 4. Giải phương trình lượng giác sau: $(\sin x + 3){\sin ^4}\frac{x}{2}$ $– (\sin x + 3){\sin ^2}\frac{x}{2} + 1 = 0.$

Đặt ${\sin ^2}\frac{x}{2} = t$ $(0 \le t \le 1)$, phương trình đã cho trở thành: $\left( {\sin x + 3} \right){t^2}$ $– (\sin x + 3)t + 1 = 0$ $(*).$

Do $\sin x + 3 > 0$ với mọi $x∈R$ nên ta xem phương trình $(*)$ là phương trình bậc hai ẩn $t.$

Ta có: $\Delta = {(\sin + 3)^2} – 4(\sin x + 3)$ $= (\sin x – 1)(\sin x + 3).$

Vì 
$$
\left\{ \begin{array}{l}
\sin x – 1 \le 0\\
\sin x + 3 > 0
\end{array} \right.
$$
 nên $Δ≤0, ∀x∈R.$

Do đó phương trình 
$$
\left( * \right) \Leftrightarrow \left\{ \begin{array}{l}
\Delta = 0\\
t = – \frac{b}{{2a}}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\sin x = 1\\
{\sin ^2}\frac{x}{2} = \frac{1}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\sin x = 1\\
\frac{{1 – \cos 2x}}{2} = \frac{1}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
\sin x = 1\\
\cos x = 0
\end{array} \right.
$$
 $\Leftrightarrow x = \frac{\pi }{2} + k2\pi$ $(k∈Z).$

Vậy phương trình đã cho có nghiệm $x = \frac{\pi }{2} + k2\pi$ $(k∈Z).$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/giai-phuong-trinh-luong-giac-bang-cach-dat-an-phu.html -->
## Ví dụ 5. Giải phương trình lượng giác sau: $\frac{9}{{{{81}^{{{\sin }^2}x}}}}$ $+ 2(\cos 2x – 2)\frac{3}{{{9^{{{\sin }^2}x}}}}$ $+ 4{\cos ^2}x – 3 = 0.$

Đặt $t = \frac{3}{{{9^{{{\sin }^2}x}}}}$, $\left( {t > 0} \right).$

Ta có: $t = \frac{3}{{{9^{{{\sin }^2}x}}}}$ $= {3^{1 – 2{{\sin }^2}x}} = {3^{\cos 2x}}.$

Phương trình đã cho trở thành: ${t^2} + 2(\cos 2x – 2)t$ $+ 4{\cos ^2}x – 3 = 0$ $\Leftrightarrow {t^2} + 2(\cos 2x – 2)t$ $+ 2\cos 2x – 5 = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
t = – 1\left( {loại} \right)\\
t = 5 – 2\cos 2x
\end{array} \right.
$$

Với $t = 5 – 2\cos 2x$, ta có: ${3^{\cos 2x}} = 5 – 2\cos 2x$ $\Leftrightarrow {3^{\cos 2x}} + 2\cos 2x = 5$ $(*).$

Đặt $y = \cos 2x$, $\left| y \right| \le 1$ thì phương trình $(*)$ trở thành: ${3^y} + 2y = 5.$

Vì hàm số $f(y) = {3^y} + 2y$ luôn đồng biến trên $R$ nên phương trình $f(y)=5$ có nghiệm duy nhất. Mặc khác $f(1) = 5$, suy ra $y=1$ là nghiệm duy nhất của phương trình $f(y)=5.$

Với $y=1$, suy ra phương trình đã cho có nghiệm $x = k\pi$ $(k∈Z).$