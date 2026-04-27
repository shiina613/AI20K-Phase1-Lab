# Phương pháp giải các dạng phương trình lượng giác thường gặp

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
Bài viết hướng dẫn phương pháp giải các dạng phương trình lượng giác thường gặp trong chương trình Đại số và Giải tích 11 chương 1.

1. Phương trình bậc hai đối với một hàm số lượng giác

• Dạng 1: $a{\sin ^2}x + b\sin x + c = 0$ $(a \ne 0; a, b, c \in R).$

Cách giải: Đặt $t = \sin x$, điều kiện $|t| \le 1$, đưa phương trình $a{\sin ^2}x + b\sin x + c = 0$ về phương trình bậc hai theo $t$, giải tìm $t$, chú ý kết hợp với điều kiện của $t$ rồi giải tìm $x.$

• Dạng 2: $a{\cos ^2}x + b\cos x + c = 0$ $(a \ne 0; a, b, c \in R).$

Cách giải: Đặt $t = \cos x$, điều kiện $|t| \le 1$, đưa phương trình $a{\cos ^2}x + b\cos x + c = 0$ về phương trình bậc hai theo $t$, giải tìm $t$, chú ý kết hợp với điều kiện của $t$ rồi giải tìm $x.$

• Dạng 3: $a{\tan ^2}x + b\tan x + c = 0$ $(a \ne 0; a, b, c \in R).$

Cách giải: Điều kiện $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$ $\left( {k \in Z} \right).$

Đặt $t = \tan x$ $\left( {t \in R} \right)$, đưa phương trình $a{\tan ^2}x + b\tan x + c = 0$ về phương trình bậc hai theo $t$, chú ý khi tìm được nghiệm $x$ cần thay vào điều kiện xem thoả mãn hay không.

• Dạng 4: $a{\cot ^2}x + b\cot x + c = 0$ $(a \ne 0; a, b, c \in R).$

Cách giải: Điều kiện $\sin x \ne 0$ $\Leftrightarrow x \ne k\pi$ $\left( {k \in Z} \right).$

Đặt $t = \cot x$ $(t \in R)$, đưa phương trình $a{\cot ^2}x + b\cot x + c = 0$ về phương trình bậc hai theo ẩn $t$, giải tìm $t$ rồi tìm $x$, chú ý khi tìm được nghiệm cần thay vào điều kiện xem thoả mãn hay không.

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 1: Giải phương trình $2{\cos ^2}x – 3\cos x + 1 = 0.$

$2{\cos ^2}x – 3\cos x + 1 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\cos x = 1\\
\cos x = \frac{1}{2}
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = k2\pi \\
x = \pm \frac{\pi }{3} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình có 3 họ nghiệm 
$$
\left[ \begin{array}{l}
x = k2\pi \\
x = \pm \frac{\pi }{3} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 2: Giải phương trình $\cot x – \tan x + 4\sin 2x = \frac{2}{{\sin 2x}}.$

Điều kiện: $\sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$ $\left( {k \in Z} \right).$

Ta có: $\cot x – \tan x + 4\sin 2x = \frac{2}{{\sin 2x}}$ $\Leftrightarrow \frac{{\cos x}}{{\sin x}} – \frac{{\sin x}}{{\cos x}} + 4\sin 2x = \frac{2}{{\sin 2x}}$

$\Leftrightarrow \frac{{{{\cos }^2}x – {{\sin }^2}x}}{{\sin x.\cos x}} + 4\sin 2x = \frac{2}{{\sin 2x}}$  $\Leftrightarrow \frac{{2\cos 2x}}{{\sin 2x}} + 4\sin 2x = \frac{2}{{\sin 2x}}$

$\Leftrightarrow \cos 2x + 2{\sin ^2}2x = 1$ $\Leftrightarrow 2{\cos ^2}2x – \cos 2x – 1 = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\cos 2x = 1\\
\cos 2x = – \frac{1}{2}
\end{array} \right.
$$

Ta thấy $\cos 2x = 1$ không thoả mãn điều kiện. Do đó:

PT $\Leftrightarrow \cos 2x = – \frac{1}{2}$ $\Leftrightarrow 2x = ± \frac{{2\pi }}{3} + k2\pi$ $\Leftrightarrow x = \pm \frac{\pi }{3} + k\pi$ $\left( {k \in Z} \right).$

Vậy phương trình có 2 họ nghiệm $\Leftrightarrow x = \pm \frac{\pi }{3} + k\pi$ $\left( {k \in Z} \right).$

2. Phương trình bậc nhất đối với $\sin x$ và $\cos x$
Phương trình lượng giác dạng $a\sin x + b\cos x = c$, trong đó $a, b, c \in R$ và ${a^2} + {b^2} \ne 0$ được gọi là phương trình bậc nhất đối với $\sin x$ và $\cos x$.

Cách giải: Ta có thể lựa chọn 1 trong 2 cách sau:

Cách 1: Thực hiện theo các bước:

• Bước 1: Kiểm tra:

+ Nếu ${a^2} + {b^2} < {c^2}$ thì phương trình vô nghiệm.

+ Nếu ${a^2} + {b^2} \ge {c^2}$ khi đó để tìm nghiệm của phương trình ta thực hiện tiếp bước 2.

• Bước 2: Chia cả 2 vế phương trình $a\sin x + b\cos x = c$ cho $\sqrt {{a^2} + {b^2}}$, ta được:

$\frac{a}{{\sqrt {{a^2} + {b^2}} }}\sin x + \frac{b}{{\sqrt {{a^2} + {b^2}} }}\cos x$ $= \frac{c}{{\sqrt {{a^2} + {b^2}} }}.$

Vì ${\left( {\frac{a}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} + {\left( {\frac{b}{{\sqrt {{a^2} + {b^2}} }}} \right)^2} = 1$ nên tồn tại góc $\alpha$ sao cho $\frac{a}{{\sqrt {{a^2} + {b^2}} }} = \cos \alpha$ và $\frac{b}{{\sqrt {{a^2} + {b^2}} }} = \sin \alpha .$

Khi đó phương trình $a\sin x + b\cos x = c$ có dạng $\sin x.\cos \alpha + \sin \alpha .\cos x = \frac{c}{{\sqrt {{a^2} + {b^2}} }}$ $\Leftrightarrow \sin (x + \alpha ) = \frac{c}{{\sqrt {{a^2} + {b^2}} }}.$

Đây là phương trình lượng giác cơ bản của $sin$ mà ta đã biết cách giải.

Cách 2: Thực hiện theo các bước:

• Bước 1: Với $\cos \frac{x}{2} = 0$ $\Leftrightarrow x = \pi + k2\pi$ $(k \in Z).$ thử vào phương trình $a\sin x + b\cos x = c$ xem có là nghiệm hay không?

• Bước 2: Với $\cos \frac{x}{2} \ne 0$ $\Leftrightarrow x \ne \pi + k2\pi$ $(k \in Z).$

Đặt $t = \tan \frac{x}{2}$ suy ra $\sin x = \frac{{2t}}{{1 + {t^2}}}$, $\cos x = \frac{{1 – {t^2}}}{{1 + {t^2}}}.$

Khi đó phương trình $a\sin x + b\cos x = c$ có dạng: $a\frac{{2t}}{{1 + {t^2}}} + b\frac{{1 – {t^2}}}{{1 + {t^2}}} = c$ $\Leftrightarrow (c + b){t^2} – 2at + c – b = 0.$

• Bước 3: Giải phương trình bậc hai ẩn $t$ sau đó giải tìm $x.$

Dạng đặc biệt:

• $\sin x + \cos x = 0$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$ $(k \in Z).$

• $\sin x – \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$ $(k \in Z).$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 3: Giải phương trình $(1 + \sqrt 3 )\sin x + (1 – \sqrt 3 )\cos x = 2.$

Cách 1: Thực hiện phép biến đổi:

PT $\Leftrightarrow (\frac{{1 + \sqrt 3 }}{{2\sqrt 2 }})\sin x + (\frac{{1 – \sqrt 3 }}{{2\sqrt 2 }})\cos x = \frac{1}{{\sqrt 2 }}.$

Đặt $\frac{{1 + \sqrt 3 }}{{2\sqrt 2 }} = \cos \alpha$, $\frac{{1 – \sqrt 3 }}{{2\sqrt 2 }} = \sin \alpha .$

Phương trình đã cho sẽ được viết thành $\sin x.\cos \alpha + \sin \alpha .\cos x = \frac{1}{{\sqrt 2 }}$ $\Leftrightarrow \sin (x + \alpha ) = \sin \frac{\pi }{4}$

$$
\Leftrightarrow \left[ \begin{array}{l}
x + \alpha = \frac{\pi }{4} + k2\pi \\
x + \alpha = \pi – \frac{\pi }{4} + k2\pi
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{4} – \alpha + k2\pi \\
x = \frac{{3\pi }}{4} – \alpha + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{4} – \alpha + k2\pi \\
x = \frac{{3\pi }}{4} – \alpha + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Cách 2: Biến đổi phương trình về dạng:

$(\sin x + \cos x) + \sqrt 3 (\sin x – \cos x) = 2$ $\Leftrightarrow \sqrt 2 \sin (x + \frac{\pi }{4}) – \sqrt 6 \cos (x + \frac{\pi }{4}) = 2$

$\Leftrightarrow \frac{1}{2}\sin (x + \frac{\pi }{4}) – \frac{{\sqrt 3 }}{2}\cos (x + \frac{\pi }{4}) = \frac{1}{{\sqrt 2 }}$ $\Leftrightarrow \sin (x + \frac{\pi }{4})\cos \frac{\pi }{3} – \cos (x + \frac{\pi }{4})\sin \frac{\pi }{3} = \frac{1}{{\sqrt 2 }}$

$\Leftrightarrow \sin (x + \frac{\pi }{4} – \frac{\pi }{3}) = \sin \frac{\pi }{4}$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x – \frac{\pi }{{12}} = \frac{\pi }{4} + k2\pi \\
x – \frac{\pi }{{12}} = \pi – \frac{\pi }{4} + k2\pi
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{3} + k2\pi \\
x = \frac{{5\pi }}{6} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{3} + k2\pi \\
x = \frac{{5\pi }}{6} + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Chú ý: Đối với phương trình dạng $a\sin P(x) + b\cos Q(x)$ $= c\sin Q(x) + d\cos P(x)$ trong đó $a, b, c, d ∈ R$ thoả mãn ${a^2} + {b^2} = {c^2} + {d^2} > 0$ và $P(x)$, $Q(x)$ không đồng thời là các hàm hằng số. Bằng phép chia cho $\sqrt {{a^2} + {b^2}}$ ta có: PT $\Leftrightarrow \sin \left[ {P(x) + \alpha } \right] = \sin \left[ {Q(x) + \beta } \right]$ (hoặc $\cos \left[ {P(x) + \alpha } \right] = \cos \left[ {Q(x) + \beta } \right]$).

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 4: Giải phương trình: $\cos 7x – \sin 5x = \sqrt 3 (\cos 5x – \sin 7x).$

PT ⇔ $\cos 7x + \sqrt 3 \sin 7x = \sqrt 3 \cos 5x + \sin 5x$

$\Leftrightarrow \frac{1}{2}\cos 7x + \frac{{\sqrt 3 }}{2}\sin 7x$ $= \frac{{\sqrt 3 }}{2}\cos 5x + \frac{1}{2}\sin 5x$

$\Leftrightarrow \cos \frac{\pi }{3}\cos 7x + \sin \frac{\pi }{3}\sin 7x$ $= \cos \frac{\pi }{6}\cos 5x + \sin \frac{\pi }{6}\sin 5x$

$\Leftrightarrow \cos (7x – \frac{\pi }{3}) = \cos (5x – \frac{\pi }{6})$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{{12}} + k\pi \\
x = \frac{\pi }{{24}} + \frac{{k\pi }}{6}
\end{array} \right.
$$
 $(k ∈ Z).$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{{12}} + k\pi \\
x = \frac{\pi }{{24}} + \frac{{k\pi }}{6}
\end{array} \right.
$$
 $(k ∈ Z).$

[ads]

3. Phương trình thuần nhất bậc hai đối với $\sin x$ và $\cos x$

Phương trình thuần nhất bậc hai đối với $\sin x$ và $\cos x$ là phương trình có dạng $a{\sin ^2}x + b\sin x.\cos x + c{\cos ^2}x = d$, trong đó $a, b,  c, d ∈ R.$

Cách giải:

Cách 1: Chia từng vế của phương trình cho một trong ba hạng tử ${\sin ^2}x$, ${\cos ^2}x$ hoặc $\sin x.\cos x$. Chẳng hạn nếu chia cho ${\cos ^2}x$ ta làm theo các bước sau:

• Bước 1: Kiểm tra: $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$ $\left( {k \in Z} \right)$ xem nó có phải là nghiệm của phương trình $a{\sin ^2}x + b\sin x.\cos x + c{\cos ^2}x = d$ hay không?

• Bước 2: Với $\cos x \ne 0$, chia cả hai vế cho ${\cos ^2}x$ lúc đó phương trình $a{\sin ^2}x + b\sin x.\cos x + c{\cos ^2}x = d$ trở thành: $a{\tan ^2}x + b\tan x + c = d(1 + {\tan ^2}x)$ $\Leftrightarrow (a – d){\tan ^2}x + b\tan x + c – d = 0.$

Đây là phương trình bậc hai theo $tan$ đã trình bày cách giải ở phần 1.

Cách 2: Dùng công thức hạ bậc ${\sin ^2}x = \frac{{1 – \cos 2x}}{2}$, ${\cos ^2}x = \frac{{1 + \cos 2x}}{2}$, $\sin x.\cos x = \frac{{\sin 2x}}{2}$ đưa phương trình $a{\sin ^2}x + b\sin x.\cos x + c{\cos ^2}x = d$ về phương trình $b\sin 2x + (c – a)\cos 2x = d – c – a.$

Đây là phương trình bậc nhất đối với $sin$ và $cos$ đã trình bày cách giải ở phần 2.

Mở rộng: Đối với phương trình đẳng cấp bậc $n (n ≥ 3)$ với dạng tổng quát: $A({\sin ^n}x, {\cos ^n}x, {\sin ^k}x{\cos ^h}x) = 0$ trong đó $k + h = n$, $k, h, n \in N$, khi đó ta cũng làm theo 2 bước:

• Bước 1: Kiểm tra xem $\cos x = 0$ có phải là nghiệm của phương trình hay không?

• Bước 2: Nếu $\cos x \ne 0$, chia cả hai vế của phương trình trên cho ${\cos ^n}x$ ta sẽ được phương trình bậc $n$ theo $\tan$. Giải phương trình này ta được nghiệm của phương trình ban đầu.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 5: Giải phương trình $2\sqrt 3 {\cos ^2}x + 6\sin x.\cos x = 3 + \sqrt 3 .$

Cách 1:

+ Thử với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k2\pi$ $\left( {k \in Z} \right)$ vào phương trình đã cho, ta có: $0 = 3 + \sqrt 3$ (vô lý). Vậy $x = \frac{\pi }{2} + k2\pi$ $\left( {k \in Z} \right)$ không là nghiệm của phương trình.

+ Với $\cos x \ne 0$, chia cả hai vế của phương trình cho ${\cos ^2}x$, ta được: $2\sqrt 3 + 6\tan x = (3 + \sqrt 3 )(1 + {\tan ^2}x)$ $\Leftrightarrow (3 + \sqrt 3 ){\tan ^2}x – 6\tan x + 3 – \sqrt 3 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
\tan x = 1\\
\tan x = \frac{{3 – \sqrt 3 }}{{3 + \sqrt 3 }} = \tan \alpha
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{4} + k\pi \\
x = \alpha + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{4} + k\pi \\
x = \alpha + k\pi
\end{array} \right.\left( {k \in Z} \right).
$$

Cách 2:

PT $\Leftrightarrow \sqrt 3 (1 + \cos 2x) + 3\sin 2x = 3 + \sqrt 3$ $\Leftrightarrow \cos 2x + \sqrt 3 \sin 2x = \sqrt 3$

$\Leftrightarrow \frac{1}{2}\cos 2x + \frac{{\sqrt 3 }}{2}\sin 2x = \frac{{\sqrt 3 }}{2}$ $\Leftrightarrow \cos (2x – \frac{\pi }{3}) = \frac{{\sqrt 3 }}{2}$

$$
\Leftrightarrow \left[ \begin{array}{l}
2x – \frac{\pi }{3} = \frac{\pi }{6} + k2\pi \\
2x – \frac{\pi }{3} = – \frac{\pi }{6} + k2\pi
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \frac{\pi }{4} + k\pi \\
x = \frac{\pi }{{12}} + k\pi
\end{array} \right. \left( {k \in Z} \right).
$$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \frac{\pi }{4} + k\pi \\
x = \frac{\pi }{{12}} + k\pi
\end{array} \right.\left( {k \in Z} \right).
$$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 6: Giải phương trình $\frac{{1 – \tan x}}{{1 + \tan x}} = 1 + \sin 2x .$

Điều kiện 
$$
\left\{ \begin{array}{l}
\cos x \ne 0\\
\tan x = – 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x \ne \frac{\pi }{2} + k\pi \\
x \ne – \frac{\pi }{4} + k\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Biến đổi phương trình $\frac{{1 – \tan x}}{{1 + \tan x}} = 1 + \sin 2x$ về dạng:

$\frac{{\cos x – \sin x}}{{\cos x + \sin x}} = {\left( {\cos x + \sin x} \right)^2}$

$\Leftrightarrow \cos x – \sin x = {\left( {\cos x + \sin x} \right)^3}$

Chia cả hai vế của phương trình $\cos x – \sin x = {\left( {_{}\cos x + \sin x} \right)^3}$ cho ${\cos ^3}x \ne 0$, ta được: $1 + {\tan ^2}x – \left( {1 + {{\tan }^2}x} \right)\tan x$ $= {\left( {1 + \tan x} \right)^3}$

$\Leftrightarrow {\tan ^3}x + {\tan ^2}x + 2\tan x = 0$ $\Leftrightarrow \left( {{{\tan }^2}x + \tan x + 2} \right)\tan x = 0$ $\Leftrightarrow \tan x = 0$ $\Leftrightarrow x = k\pi$ $\left( {k \in Z} \right)$ (phương trình ${\tan ^2}x + \tan x + 2 = 0$ vô nghiệm).

Vậy phương trình có một họ nghiệm $x = k\pi$ $\left( {k \in Z} \right).$

4. Phương trình đối xứng đối với $\sin x$ và $\cos x$

Phương trình đối xứng đối với $\sin x$ và $\cos x$ là phương trình dạng $a(\sin x + \cos x) + b\sin x\cos x + c = 0$, trong đó $a, b, c \in R.$

Cách giải:

Cách 1: Do ${(\sin x + cosx)^2} = 1 + 2\sin x\cos x$ nên ta đặt: $t = \sin x + \cos x$ $= \sqrt 2 \sin (x + \frac{\pi }{4})$ $= \sqrt 2 \cos (\frac{\pi }{4} – x)$, điều kiện $|t| \le \sqrt 2 .$

Suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}$ và phương trình $a(\sin x + \cos x) + b\sin x\cos x + c = 0$ được viết lại: $b{t^2} + 2at – (b + 2c) = 0.$

Cách 2: Đặt $t = \frac{\pi }{4} – x$, ta có:

$\sin x + \cos x = \sqrt 2 \cos (\frac{\pi }{4} – x)$ $= \sqrt 2 \cos t.$

$\sin x\cos x = \frac{1}{2}\sin 2x$ $= \frac{1}{2}\cos (\frac{\pi }{2} – 2x)$ $= \frac{1}{2}\cos 2t = {\cos ^2}t – \frac{1}{2}.$

Phương trình $a(\sin x + \cos x) + b\sin x\cos x + c = 0$ trở thành $b{\cos ^2}x + \sqrt 2 \cos x – \frac{b}{2} + c = 0$. Đây là phương trình bậc hai theo $cos$ đã trình bày cách giải ở phần 1.

Chú ý: Phương trình lượng giác dạng $a(\sin x – \cos x) + b\sin x\cos x + c = 0$ được giải tương tự bằng cách đặt $t = \sin x – \cos x.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 7: Giải phương trình $\sin x + \cos x – 2\sin x\cos x + 1 = 0.$

Đặt $\sin x + \cos x = t$, điều kiện $|t| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Phương trình đã cho trở thành: $t – 2(\frac{{{t^2} – 1}}{2}) + 1 = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
t = – 1\\
t = 2
\end{array} \right.
$$
 (loại $t = 2$ vì không thỏa mãn điều kiện).

Với $t = – 1$ $⇔ \sin x + \cos x = – 1$ $\Leftrightarrow \sqrt 2 \sin (x + \frac{\pi }{4}) = – 1$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = – \frac{\pi }{2} + k2\pi \\
x = \pi + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

Vậy phương trình có 2 họ nghiệm 
$$
\left[ \begin{array}{l}
x = – \frac{\pi }{2} + k2\pi \\
x = \pi + k2\pi
\end{array} \right.
$$
 $\left( {k \in Z} \right).$

5. Phương trình lượng giác hỗn hợp chứa các biểu thức đối xứng $\tan x$ và $cotx$
Phương trình lượng giác hỗn hợp chứa các biểu thức đối xứng $\tan x$ và $cotx$ là phương trình có dạng ${p_k}\sum\limits_{k = 1}^n {({{\tan }^k}x + {\alpha ^k}{{\cot }^k}x)}$ $+ q(\tan x \pm \alpha \cot x) + r = 0$ $(\alpha > 0; k \ge 2).$

Cách giải:

• Bước 1: Đặt ẩn phụ 
$$
\left[ \begin{array}{l}
t = \tan x + \alpha \cot x \left( {|t| \le 2\sqrt 2 } \right)\\
t = \tan x – \alpha \cot x \left( {t \in R} \right)
\end{array} \right.
$$
 đưa phương trình đã cho về dạng đại số $F(t) = 0.$

• Bước 2: Giải phương trình $F(t) = 0$ và loại những nghiệm không thoả mãn điều kiện của bài toán.

• Bước 3: Với nghiệm $t$ tìm được ở bước 2 thế vào bước 1 để tìm $x.$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-cac-dang-phuong-trinh-luong-giac-thuong-gap.html -->
## Ví dụ 8: Giải phương trình: ${\tan ^3}x – {\cot ^3}x – 3({\tan ^2}x + {\cot ^2}x)$ $– 3(\tan x – \cot x) + 10 = 0.$

Phương trình $\Leftrightarrow {\tan ^3}x – {\cot ^3}x – 3\tan x.\cot x(tanx – cotx)$ $– 3({\tan ^2}x + {\cot ^2}x – 2) + 4 = 0$

$\Leftrightarrow {(\tan x – \cot x)^3}$ $– 3(\tan x – \cot x) + 4 = 0$

$$
\Leftrightarrow \left[ \begin{array}{l}
\tan x – \cot x = – 1\\
\tan x – \cot x = 2
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
\cot 2x = \frac{1}{2} = \cot 2\alpha \\
\cot 2x = – 1
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
x = \alpha + k\frac{\pi }{2}\\
x = – \frac{\pi }{8} + k\frac{\pi }{2}
\end{array} \right. \left( {k \in Z} \right).
$$

Vậy phương trình có hai họ nghiệm 
$$
\left[ \begin{array}{l}
x = \alpha + k\frac{\pi }{2}\\
x = – \frac{\pi }{8} + k\frac{\pi }{2}
\end{array} \right. \left( {k \in Z} \right)
$$
 với $\cot 2\alpha = \frac{1}{2}.$