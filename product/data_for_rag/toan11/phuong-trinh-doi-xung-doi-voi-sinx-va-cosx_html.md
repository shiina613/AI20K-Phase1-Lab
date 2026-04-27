# Phương trình đối xứng đối với sinx và cosx

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
Bài viết hướng dẫn phương pháp giải và biện luận phương trình đối xứng đối với sinx và cosx.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài toán 1: Giải phương trình: $a(\sin x + \cos x) + b\sin x\cos x + c = 0$ $(1).$
PHƯƠNG PHÁP CHUNG:

Ta biện luận theo các bước sau:

+ Bước 1: Đặt $\sin x + \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$ $\Rightarrow \sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó phương trình có dạng:

$at + b\frac{{{t^2} – 1}}{2} + c = 0$ $\Leftrightarrow b{t^2} + 2at + 2c – b = 0$ $(2).$

+ Bước 2: Giải $(2)$ theo $t$ và chọn nghiệm ${t_0}$ thoả mãn điều kiện $|t| \le \sqrt 2 .$

Với $t = {t_0}$, ta được:

$\sin x + \cos x = {t_0}$ $\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = {t_0}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right) = \frac{{{t_0}}}{{\sqrt 2 }}.$

Đây là phương trình cơ bản của sin.

Chú ý: Ta có thể giải $(1)$ bằng cách đặt ẩn phụ $z = \frac{\pi }{4} – x$, khi đó ta có:

$\sin x + \cos x$ $= \sqrt 2 \cos \left( {\frac{\pi }{4} – x} \right)$ $= \sqrt 2 \cos z.$

$\sin x\cos x$ $= \frac{1}{2}\sin 2x$ $= \frac{1}{2}\sin 2\left( {\frac{\pi }{4} – z} \right)$ $= \frac{1}{2}\sin \left( {\frac{\pi }{2} – 2z} \right)$ $= \frac{1}{2}\cos 2z$ $= \frac{1}{2}\left( {2{{\cos }^2}z – 1} \right).$

Vậy ta chuyển phương trình ban đầu về dạng phương trình bậc $2$ đối với $\cos z.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 1: Giải phương trình:

$\sin x + \cos x$ $– 2\sin x\cos x + 1 = 0.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Đặt $\sin x + \cos x = t$, điều kiện $|t| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó phương trình có dạng:

$t – \left( {{t^2} – 1} \right) + 1 = 0$ $\Leftrightarrow {t^2} – t – 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 2\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow \sin x + \cos x = – 1$ $\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = – 1$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right) = – \frac{1}{{\sqrt 2 }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{2} + 2k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Đặt $z = \frac{\pi }{4} – x$. Khi đó phương trình có dạng:

$\sqrt 2 \cos \left( {\frac{\pi }{4} – x} \right) – \sin 2x + 1 = 0$ $\Leftrightarrow \sqrt 2 \cos z – \sin 2\left( {\frac{\pi }{4} – z} \right) + 1 = 0.$

$\Leftrightarrow \sqrt 2 \cos z – \sin \left( {\frac{\pi }{2} – 2z} \right) + 1 = 0$ $\Leftrightarrow \sqrt 2 \cos z – \cos 2z + 1 = 0.$

$\Leftrightarrow \sqrt 2 \cos z – \left( {2{{\cos }^2}z – 1} \right) + 1 = 0$ $\Leftrightarrow – 2{\cos ^2}z + \sqrt 2 \cos z + 2 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos z = \sqrt 2 \:{\rm{(loại)}}}\\
{\cos z = – \frac{{\sqrt 2 }}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{z = – \frac{{3\pi }}{4} + 2k\pi }\\
{z = \frac{{3\pi }}{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\frac{\pi }{4} – x = – \frac{{3\pi }}{4} + 2k\pi }\\
{\frac{\pi }{4} – x = \frac{{3\pi }}{4} + 2k\pi }
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{2} – 2k\pi }\\
{x = \pi – 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

**Chú ý**: Tồn tại những phương trình ở dạng ban đầu chưa phải là phương trình đối xứng, khi đó cần thực hiện một vài phép biến đổi lượng giác thích hợp.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 2: (ĐHMĐC – 1999): Giải phương trình: $1 + \tan x = 2\sqrt 2 \sin x.$

Điều kiện: $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$1 + \frac{{\sin x}}{{\cos x}} = 2\sqrt 2 \sin x$ $\Leftrightarrow \sin x + \cos x = 2\sqrt 2 \sin x\cos x.$

Đặt $\sin x + \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó phương trình có dạng:

$t = \sqrt 2 \left( {{t^2} – 1} \right)$ $\Leftrightarrow \sqrt 2 {t^2} – t – \sqrt 2 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – \frac{{\sqrt 2 }}{2}}\\
{t = \sqrt 2 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x + \cos x = – \frac{{\sqrt 2 }}{2}}\\
{\sin x + \cos x = \sqrt 2 }
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin \left( {x + \frac{\pi }{4}} \right) = – \frac{1}{2}}\\
{\sin \left( {x + \frac{\pi }{4}} \right) = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x + \frac{\pi }{4} = – \frac{\pi }{6} + 2k\pi }\\
{x + \frac{\pi }{4} = \frac{{7\pi }}{6} + 2k\pi }\\
{x + \frac{\pi }{4} = \frac{\pi }{2} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{{5\pi }}{{12}} + 2k\pi }\\
{x = \frac{{11\pi }}{{12}} + 2k\pi }\\
{x = \frac{\pi }{4} + 2k\pi }
\end{array}} \right.
$$
 $(k \in Z).$

Vậy phương trình có ba họ nghiệm.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 3: Cho phương trình:

$m(\sin x + \cos x)$ $+ \sin 2x + m – 1 = 0$ $(1).$

a. Giải phương trình với $m = 2.$

b. Tìm $m$ để phương trình có nghiệm.

Đặt $\sin x + \cos x = t$, điều kiện $|t| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó phương trình có dạng:

$mt + \left( {{t^2} – 1} \right) + m – 1 = 0$ $\Leftrightarrow f(t) = {t^2} + mt + m – 2 = 0$ $(2).$

a. Với $m = 2$ phương trình $(2)$ có dạng:

${t^2} + 2t = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = – 2\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow \sin x + \cos x = 0$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$ $(k \in Z).$

Vậy với $m = 2$ phương trình có một họ nghiệm.

b. Ta có thể lựa chọn một trong hai cách:

Cách 1: Phương trình $(1)$ có nghiệm $\Leftrightarrow (2)$ có nghiệm thoả mãn $\left| t \right| \le \sqrt 2 .$

$$
\Leftrightarrow \left[ \begin{array}{l}
(2){\rm{\:có\:1\:nghiệm\:thuộc\:}}\left[ { – \sqrt 2 ;\sqrt 2 } \right]\\
(2){\rm{\:có\:2\:nghiệm\:thuộc\:}}\left[ { – \sqrt 2 ;\sqrt 2 } \right]
\end{array} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{f( – \sqrt 2 )f(\sqrt 2 ) \le 0}\\
{\left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{af(\sqrt 2 ) \ge 0}\\
{af( – \sqrt 2 ) \ge 0}\\
{ – \sqrt 2 \le \frac{S}{2} \le \sqrt 2 }
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
( – m\sqrt 2 + m)(m\sqrt 2 + m) \le 0\\
\left\{ {\begin{array}{l}
{{m^2} – 4m + 8 \ge 0}\\
{m\sqrt 2 + m \ge 0}\\
{ – m\sqrt 2 + m \ge 0}\\
{ – \sqrt 2 \le – \frac{m}{2} \le \sqrt 2 }
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow \forall m.$

Vậy với mọi $m$ phương trình luôn có nghiệm.

Cách 2: Viết lại $(2)$ dưới dạng:

$2 – {t^2} = m(t + 1)$ $\Leftrightarrow \frac{{2 – {t^2}}}{{t + 1}} = m$ (vì $t = – 1$ không là nghiệm).

Phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = m$ cắt đồ thị hàm số $y = \frac{{2 – {t^2}}}{{t + 1}}$ trên $D = ( – 1,1].$

Xét hàm số $y = \frac{{2 – {t^2}}}{{t + 1}}$ trên $D = ( – 1,1].$

Đạo hàm: $y’ = \frac{{ – {t^2} – 2t – 2}}{{t + 1}} < 0$, suy ra hàm số nghịch biến trên $D.$

Do đó đường thẳng $y = m$ luôn cắt đồ thị hàm số trên $D$ $\Leftrightarrow$ với mọi $m$ phương trình luôn có nghiệm.

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài toán 2: Giải phương trình: $a(\sin x – \cos x) + b\sin x\cos x + c = 0$ $(1).$
PHƯƠNG PHÁP CHUNG:

Ta biện luận theo các bước sau:

+ Bước 1: Đặt $\sin x – \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$ $\Rightarrow \sin x\cos x = \frac{{1 – {t^2}}}{2}.$

Khi đó phương trình có dạng:

$at + b\frac{{1 – {t^2}}}{2} + c = 0$ $\Leftrightarrow b{t^2} – 2at – 2c – b = 0$ $(2).$

+ Bước 2: Giải phương trình $(2)$ theo $t$ và chọn nghiệm ${t_0}$ thoả mãn điều kiện: $|t| \le \sqrt 2 .$

Với $t = {t_0}$, ta được:

$\sin x + \cos x = {t_0}$ $\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = {t_0}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right) = \frac{{{t_0}}}{{\sqrt 2 }}.$

Đây là phương trình cơ bản của sin.

Chú ý: Cũng như trong bài toán 1, ta có thể giải phương trình nửa đối xứng đối với $\sin x$ và $\cos x$ bằng cách đặt ẩn phụ $z = \frac{\pi }{4} – x.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 4: Giải phương trình:

$6(\sin x – \cos x) + \sin x\cos x + 6 = 0.$

Ta có thể lựa chọn một trong hai cách sau:

+ Cách 1: Đặt $\sin x – \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{1 – {t^2}}}{2}.$

Khi đó phương trình có dạng:

$6t – \frac{{1 – {t^2}}}{2} + 6 = 0$ $\Leftrightarrow {t^2} – 12t – 13 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 13\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow \sin x – \cos x = – 1.$

$\Leftrightarrow \sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right) = – 1$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = – \frac{1}{{\sqrt 2 }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{2} + 2k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

+ Cách 2: Đặt $z = \frac{\pi }{4} – x.$

Khi đó phương trình có dạng:

$6\sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right) + \frac{1}{2}\sin 2x + 6 = 0$ $\Leftrightarrow 12\sqrt 2 \sin ( – z)$ $+ \sin 2\left( {\frac{\pi }{4} – z} \right) + 12 = 0.$

$\Leftrightarrow – 12\sqrt 2 \sin z$ $+ \sin \left( {\frac{\pi }{2} – 2z} \right) + 12 = 0$ $\Leftrightarrow – 12\sqrt 2 \sin z + \cos 2z + 12 = 0.$

$\Leftrightarrow – 12\sqrt 2 \sin z$ $+ \left( {1 – 2{{\sin }^2}z} \right) + 12 = 0$ $\Leftrightarrow – 2{\sin ^2}z – 12\sqrt 2 \sin z + 13 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin z = – \frac{{13\sqrt 2 }}{2}\:{\rm{(loại)}}}\\
{\sin z = \frac{{\sqrt 2 }}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{z = \frac{\pi }{4} + 2k\pi }\\
{z = \frac{{3\pi }}{4} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\frac{\pi }{4} – x = \frac{\pi }{4} + 2k\pi }\\
{\frac{\pi }{4} – x = \frac{{3\pi }}{4} + 2k\pi }
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 2k\pi }\\
{x = – \frac{\pi }{2} – 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 5: Cho phương trình sau:

$4(\cos x – \sin x) + \sin 2x = m$ $(1).$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình vô nghiệm.

Biến đổi phương trình về dạng:

$4(\cos x – \sin x) + 2\sin x\cos x = m.$

Đặt $\cos x – \sin x = t$, điều kiện $|t| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{1 – {t^2}}}{2}.$

Khi đó phương trình có dạng:

$4t + 1 – {t^2} = m$ $\Leftrightarrow – {t^2} + 4t + 1 – m = 0$ $(2).$

a. Với $m = 1$, ta được:

$– {t^2} + 4t = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = 4\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow \cos x – \sin x = 0$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

b. Ta có thể lựa chọn một trong hai cách sau:

+ Cách 1: Ta đi xét bài toán ngược “Tìm $m$ để phương trình có nghiệm”.

Phương trình $(1)$ có nghiệm $\Leftrightarrow (2)$ có nghiệm thoả mãn $\left| t \right| \le \sqrt 2 .$

$$
\Leftrightarrow \left[ \begin{array}{l}
(2){\rm{\:có\:1\:nghiệm\:thuộc\:}}\left[ { – \sqrt 2 ;\sqrt 2 } \right]\\
(2){\rm{\:có\:2\:nghiệm\:thuộc\:}}\left[ { – \sqrt 2 ;\sqrt 2 } \right]
\end{array} \right..
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
f\left( { – \sqrt 2 } \right)f\left( {\sqrt 2 } \right) \le 0\\
\left\{ {\begin{array}{l}
{\Delta ‘ \ge 0}\\
{af\left( {\sqrt 2 } \right) \ge 0}\\
{af\left( { – \sqrt 2 } \right) \ge 0}\\
{ – \sqrt 2 \le \frac{S}{2} \le \sqrt 2 }
\end{array}} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
( – 1 – 4\sqrt 2 – m)(1 + 4\sqrt 2 – m) \le 0\\
\left\{ {\begin{array}{l}
{5 – m \ge 0}\\
{1 + 4\sqrt 2 – m \ge 0}\\
{ – 1 – 4\sqrt 2 – m \ge 0}\\
{ – \sqrt 2 \le 2 \le \sqrt 2 }
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow |m| \le 4\sqrt 2 + 1.$

Vậy phương trình vô nghiệm khi $|m| > 4\sqrt 2 + 1.$

+ Cách 2: Viết lại $(2)$ dưới dạng:

$– {t^2} + 4t + 1 = m.$

Vậy phương trình vô nghiệm $\Leftrightarrow$ đường thẳng $y = m$ không cắt phần đồ thị hàm số $y = – {t^2} + 4t + 1$ trên $\left[ { – \sqrt 2 ,\sqrt 2 } \right].$

Xét hàm số $y = – {t^2} + 4t + 1$ trên $\left[ { – \sqrt 2 ,\sqrt 2 } \right].$

Đạo hàm:

$y’ = – 2t + 4 > 0$, $\forall t \in \left[ { – \sqrt 2 ,\sqrt 2 } \right]$, do đó hàm số đồng biến trên $\left[ { – \sqrt 2 ,\sqrt 2 } \right].$

Từ đó ta được điều kiện là:

$$
\left[ {\begin{array}{l}
{m < y( – \sqrt 2 )}\\
{m > y(\sqrt 2 )}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m < – 4\sqrt 2 – 1}\\
{m > 4\sqrt 2 + 1}
\end{array}} \right.
$$
 $\Leftrightarrow |m| > 4\sqrt 2 + 1.$

Vậy phương trình vô nghiệm khi $|m| > 4\sqrt 2 + 1.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Ví dụ 6: Cho phương trình sau:

${\sin ^3}x – {\cos ^3}x = m$ $(1).$

a. Giải phương trình với $m =1.$

b. Tìm $m$ để phương trình có đúng ba nghiệm thuộc $[0,\pi ].$

Biến đổi phương trình về dạng:

$(\sin x – \cos x)$ $+ 3\sin x\cos x(\sin x – \cos x) = m.$

Đặt $\sin x – \cos x = t$, điều kiện $|t| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{1 – {t^2}}}{2}.$

Khi đó phương trình có dạng:

${t^3} + 3t.\frac{{1 – {t^2}}}{2} = m$ $\Leftrightarrow – {t^3} + 3t = 2m$ $(2).$

a. Với $m = 1$ ta được:

${t^3} – 3t + 2 = 0$ $\Leftrightarrow (t – 1)\left( {{t^2} + t + 2} \right) = 0$ $\Leftrightarrow t = 1$ $\Leftrightarrow \sin x – \cos x = 1.$

$\Leftrightarrow \sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right) = 1$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{1}{{\sqrt 2 }}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{2} + 2k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

b. Ta có thể lựa chọn một trong hai cách sau:

+ Cách 1: Với $x \in [0,\pi ]$ $\Rightarrow t \in [ – 1,\sqrt 2 ].$

Ta có nhận xét sau:

+ Với mỗi ${t_0} \in ( – 1,1)$ hoặc ${t_0} = \sqrt 2$ thì phương trình: $\sin x – \cos x = {t_0}$ $\Leftrightarrow \sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right) = {t_0}$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{{{t_0}}}{{\sqrt 2 }}$ sẽ có đúng $1$ nghiệm $x \in [0,\pi ].$

+ Với mỗi ${t_0} \in [1,\sqrt 2 )$ thì phương trình: $\sin x – \cos x = {t_0}$ $\Leftrightarrow \sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right) = {t_0}$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{{{t_0}}}{{\sqrt 2 }}$ sẽ có đúng $2$ nghiệm $x \in [0,\pi ].$

Vậy để phương trình $(1)$ có đúng ba nghiệm thuộc $[0,\pi ]$ $\Leftrightarrow (2)$ có $2$ nghiệm ${t_1}$, ${t_2}$ thoả mãn $– 1 < {t_1} < 1 < {t_2} < \sqrt 2 .$

Xét hàm số $y = – {t^3} + 3t$ trên $[ – 1,\sqrt 2 ].$

Đạo hàm:

$y’ = – 3{t^2} + 3.$

$y’ = 0$ $\Leftrightarrow – 3{t^2} + 3 = 0$ $\Leftrightarrow t = \pm 1.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx-1.png" alt="">

Dựa vào bảng biến thiên, ta được điều kiện là:

$\sqrt 2 < 2m < 2$ $\Leftrightarrow \frac{{\sqrt 2 }}{2} < m < 1.$

+ Cách 2: Số nghiệm thuộc $[0,\pi ]$ của phương trình $(1)$ bằng số giao điểm của đồ thị hàm số $y = {\sin ^3}x – {\cos ^3}x$ trên $[0,\pi ]$ với đường thẳng $y = m.$

Xét hàm số $y = {\sin ^3}x – {\cos ^3}x$ trên $[0,\pi ].$

Đạo hàm:

$y’ = – 3\cos x{\sin ^2}x + 3\sin x{\cos ^2}x.$

$y’ = 0$ $\Leftrightarrow 3\cos x{\sin ^2}x + 3\sin x{\cos ^2}x = 0$ $\Leftrightarrow \frac{3}{2}(\sin x + \cos x)\sin 2x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin 2x = 0}\\
{\sin x + \cos x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin 2x = 0}\\
{\sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x = k\pi }\\
{x + \frac{\pi }{4} = k\pi }
\end{array}} \right.
$$
 
$$
\mathop \Leftrightarrow \limits^{x \in \left[ {0;\pi } \right]} \left[ {\begin{array}{l}
{x = 0}\\
{x = \frac{\pi }{2}}\\
{x = \pi }\\
{x = \frac{{3\pi }}{4}}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx-2.png" alt="">

Dựa vào bảng biến thiên, ta được điều kiện là: $\frac{{\sqrt 2 }}{2} < m < 1.$

<!-- chunk:9 level:1 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: Giải phương trình:

$\cos x + \frac{1}{{\cos x}}$ $+ \sin x + \frac{1}{{\sin x}} = \frac{{10}}{3}.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Biến đổi phương trình về dạng:

$\sin x + \cos x$ $+ \frac{{\sin x + \cos x}}{{\sin x\cos x}} – \frac{{10}}{3} = 0.$

Đặt $\sin x + \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó phương trình có dạng:

$t + \frac{{2t}}{{{t^2} – 1}} – \frac{{10}}{3} = 0$ $\Leftrightarrow 3{t^3} – 10{t^2} + 3t + 10 = 0.$

$\Leftrightarrow (t – 2)\left( {3{t^2} – 4t – 5} \right) = 0$ $\mathop \Leftrightarrow \limits^{\left| t \right| \le \sqrt 2 } t = \frac{{2 – \sqrt {19} }}{3}$ $\Leftrightarrow \sin x + \cos x = \frac{{2 – \sqrt {19} }}{3}.$

$\Leftrightarrow \sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = \frac{{2 – \sqrt {19} }}{3}$ $\Leftrightarrow \sin \left( {x + \frac{\pi }{4}} \right) = \frac{{2 – \sqrt {19} }}{{3\sqrt 2 }} = \sin \alpha .$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + \alpha + 2k\pi }\\
{x = \frac{{5\pi }}{4} – \alpha + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

## Bài 2: (ĐHNT – 1998): Giải phương trình:

$\sin x + {\sin ^2}x + {\sin ^3}x + {\sin ^4}x$ $= \cos x + {\cos ^2}x + {\cos ^3}x + {\cos ^4}x.$

Ta có:

${\sin ^3}x – {\cos ^3}x$ $= (\sin x – \cos x)\left( {{{\sin }^2}x + {{\cos }^2}x + \sin x\cos x} \right).$

${\sin ^4}x – {\cos ^4}x$ $= \left( {{{\sin }^2}x – {{\cos }^2}x} \right)\left( {{{\sin }^2}x + {{\cos }^2}x} \right)$ $= – \cos 2x.$

Phương trình được viết lại dưới dạng:

$\sin x – \cos x$ $+ {\sin ^2}x – {\cos ^2}x$ $+ {\sin ^3}x – {\cos ^3}x$ $+ {\sin ^4}x – {\cos ^4}x = 0.$

$\Leftrightarrow \sin x – \cos x – \cos 2x$ $+ (\sin x – \cos x)(1 + \sin x\cos x)$ $– \cos 2x = 0.$

$\Leftrightarrow \sin x – \cos x – 2\cos 2x$ $+ (\sin x – \cos x)(1 + \sin x\cos x) = 0.$

$\Leftrightarrow (\sin x – \cos x)\left[ {1 + 2(\sin x + \cos x) + 1 + \sin x\cos x} \right] = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x – \cos x = 0\:\left( 1 \right)}\\
{2(\sin x + \cos x) + \sin x\cos x + 2 = 0\:\left( 2 \right)}
\end{array}} \right..
+ Giải $(1)$: Ta được $\tan x = 1$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

+ Giải $(2)$: Đặt $\sin x + \cos x = t$ điều kiện $\left| t \right| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{{t^2} – 1}}{2}.$

Khi đó $(2)$ có dạng:

$2t + \frac{{{t^2} – 1}}{2} + 2 = 0$ $\Leftrightarrow {t^2} + 4t + 3 = 0$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = – 3\:{\rm{(loại)}}}
\end{array}} \right..
$\Leftrightarrow \sin x + \cos x = – 1$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{2} + 2k\pi }\\
{x = \pi + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

## Bài 3: (ĐHSP TP HCM – ĐHL TP HCM): Tìm $m$ để phương trình: $2\cos 2x$ $+ (\sin x\cos x – m)(\sin x + \cos x) = 0$ $(1)$ có nghiệm trong khoảng $\left[ {0,\frac{\pi }{2}} \right].$

Biến đổi phương trình về dạng:

$(\sin x + \cos x)\left[ {2(\cos x – \sin x) + \sin x\cos x – m} \right] = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x + \cos x = 0}\\
{2(\cos x – \sin x) + \sin x\cos x = m}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + k\pi }\\
{2(\cos x – \sin x) + \sin x\cos x = m}
\end{array}} \right..
$\Leftrightarrow 2(\cos x – \sin x) + \sin x\cos x – m = 0$ $(2).$

Đặt $t = \cos x – \sin x$, vì $x \in \left[ {0,\frac{\pi }{2}} \right]$ $\Leftrightarrow t \in [ – 1,1].$

Khi đó $\sin x\cos x = \frac{{1 – {t^2}}}{2}$, phương trình $(2)$ có dạng:

$– \frac{1}{2}{t^2} + 2t + \frac{1}{2} = m$ $(3).$

Vậy $(1)$ có nghiệm trong khoảng $\left[ {0,\frac{\pi }{2}} \right]$ $\Leftrightarrow (3)$ có nghiệm thuộc $[ – 1,1].$

Xét hàm số $f(t) = – \frac{1}{2}{t^2} + 2t + \frac{1}{2}.$

Miền xác định: $D = [ – 1,1].$

Đạo hàm:

$f'(t) = – t + 2.$

$f(t) = 0$ $\Leftrightarrow t = 2.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx-3.png" alt="">

Vậy phương trình có nghiệm thuộc $[ – 1,1]$ khi:

$f( – 1) \le m \le f(1)$ $\Leftrightarrow – 2 \le m \le 2.$

## Bài 4: Giải và biện luận phương trình:

$\frac{1}{{\cos x}} – \frac{1}{{\sin x}} = k.$

Điều kiện:
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Biến đổi phương trình về dạng:

$\frac{{\sin x – \cos x}}{{\sin x\cos x}} – k = 0$ $\Leftrightarrow \sin x – \cos x – k\sin x\cos x = 0$ $(1).$

Đặt $\sin x – \cos x = t$, điều kiện $\left| t \right| \le \sqrt 2$, suy ra $\sin x\cos x = \frac{{1 – {t^2}}}{2}.$

Khi đó phương trình có dạng:

$t – k.\frac{{1 – {t^2}}}{2} = 0$ $\Leftrightarrow f(t) = k{t^2} + 2t – k = 0$ $(2).$

1. Với $k = 0$ ta được:

$t = 0$ $\Leftrightarrow \sin x + \cos x = 0$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy với $k = 0$ phương trình có một họ nghiệm.

2. Với $k \ne 0$ ta có:

$\Delta = 1 + {k^2} > 0$, $\forall k$ suy ra phương trình $(2)$ có hai nghiệm là:

${t_1} = \frac{{ – 1 – \sqrt {1 + {k^2}} }}{k}.$

${t_2} = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{k}.$

Phương trình $(1)$ có nghiệm $\Rightarrow (2)$ có nghiệm thoả mãn $– \sqrt 2 \le t \le \sqrt 2 .$

Xét hai trường hợp:

+ Trường hợp 1: Phương trình $(2)$ có $1$ nghiệm thuộc $[ – \sqrt 2 ,\sqrt 2 ].$

$\Leftrightarrow f( – \sqrt 2 )f(\sqrt 2 ) \le 0$ $\Leftrightarrow (k – 2\sqrt 2 )(k + 2\sqrt 2 ) \le 0$ $\Leftrightarrow – 2\sqrt 2 \le k \le 2\sqrt 2 .$

Khi đó nghiệm thuộc $[ – \sqrt 2 ,\sqrt 2 ]$ là ${t_2} = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{k}.$

$\Leftrightarrow \sin x – \cos x = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{k}$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{{k\sqrt 2 }} = \sin \alpha .$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \frac{\pi }{4} = \alpha + 2k\pi }\\
{x – \frac{\pi }{4} = \pi – \alpha + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + \frac{\pi }{4} + 2k\pi }\\
{x = \frac{{5\pi }}{4} – \alpha + 2k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

+ Trường hợp 2: Phương trình $(2)$ có $2$ nghiệm thuộc $[ – \sqrt 2 ,\sqrt 2 ].$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{af(\sqrt 2 ) \ge 0}\\
{af( – \sqrt 2 ) \ge 0}\\
{ – \sqrt 2 \le \frac{S}{2} \le \sqrt 2 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{1 + {k^2} \ge 0}\\
{k(k + 2\sqrt 2 ) \ge 0}\\
{k(k – 2\sqrt 2 ) \ge 0}\\
{ – \sqrt 2 \le – \frac{1}{k} \le \sqrt 2 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k \ge 2\sqrt 2 }\\
{k \le – 2\sqrt 2 }
\end{array}} \right..
Khi đó:

+ Với ${t_1} = \frac{{ – 1 – \sqrt {1 + {k^2}} }}{k}.$

$\Leftrightarrow \sin x – \cos x = \frac{{ – 1 – \sqrt {1 + {k^2}} }}{k}$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{{ – 1 – \sqrt {1 + {k^2}} }}{{k\sqrt 2 }} = \sin \alpha .$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \frac{\pi }{4} = \alpha + 2k\pi }\\
{x – \frac{\pi }{4} = \pi – \alpha + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + \frac{\pi }{4} + 2k\pi }\\
{x = \frac{{5\pi }}{4} – \alpha + 2k\pi }
\end{array}} \right.
, $k \in Z.$

+ Với ${t_2} = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{k}.$

$\Leftrightarrow \sin x – \cos x = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{k}$ $\Leftrightarrow \sin \left( {x – \frac{\pi }{4}} \right) = \frac{{ – 1 + \sqrt {1 + {k^2}} }}{{k\sqrt 2 }} = \sin \beta .$
\Leftrightarrow \left[ {\begin{array}{l}
{x – \frac{\pi }{4} = \beta + 2k\pi }\\
{x – \frac{\pi }{4} = \pi – \beta + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \beta + \frac{\pi }{4} + 2k\pi }\\
{x = \frac{{5\pi }}{4} – \beta + 2k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có bốn họ nghiệm.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 1. Giải các phương trình sau:

a. $3(\sin x + \cos x) – 4\sin x\cos x = 0.$

b. $12(\sin x – \cos x) – 2\sin x\cos x – 12 = 0.$

c. $(1 + \cos x)(1 + \sin x) = 2.$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 2. Giải các phương trình sau:

a. $|\sin x – \cos x| + 4\sin 2x = 1.$

b. $|\sin x + \cos x| – \sin 2x = 0.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 3. (ĐHQG Hà Nội Khối B – 1997): Giải phương trình:

$2\sqrt 2 \sin \left( {x + \frac{\pi }{4}} \right) = \frac{1}{{\sin x}} + \frac{1}{{\cos x}}.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 5. Cho phương trình: $(1 – \cos x)(1 – \sin x) = m.$

a. Giải phương trình với $m = 2.$

b. Tìm $m$ để phương trình có đúng $1$ nghiệm thuộc $\left[ {0,\frac{\pi }{2}} \right].$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 6. Cho phương trình: $2{\sin ^3}x + \cos 2x + \cos x = m.$

a. Giải phương trình với $m = 0.$

b. Tìm $m$ để phương trình có nghiệm.

<!-- chunk:15 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 7. Cho phương trình: $m(\sin x + \cos x) + \sin x\cos x + 1 = 0.$

a. Giải phương trình với $m = – \sqrt 2 .$

b. Tìm $m$ để phương trình có nghiệm.

c. Tìm $m$ để phương trình có đúng $1$ nghiệm thuộc $\left[ { – \frac{\pi }{2},0} \right].$

<!-- chunk:16 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 8. Cho phương trình:

$m(\sin x + \cos x) + \sin 2x = 0.$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình vô nghiệm.

c. Tìm $m$ để phương trình có đúng $2$ nghiệm thuộc $[0,\pi ].$

<!-- chunk:17 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 9. Giải và biện luận theo $k$ phương trình:

$\frac{1}{{\cos x}} + \frac{1}{{\sin x}} = k.$

<!-- chunk:18 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 10. Cho phương trình:

$m(\sin x – \cos x) + 2\sin x\cos x = m.$

a. Giải phương trình với $m = 1 + \sqrt 2 .$

b. Tìm $m$ để phương trình có đúng $2$ nghiệm thuộc $[0,\pi ].$

<!-- chunk:19 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 11. Cho phương trình:

$m + {\sin ^3}x + {\cos ^3}x – 3\sin x\cos x = 0.$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình có đúng $3$ nghiệm thuộc $[0,\pi ].$

c. Tìm $m$ để phương trình có đúng $4$ nghiệm thuộc $[0,\pi ].$

<!-- chunk:20 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-sinx-va-cosx.html -->
## Bài tập 13. Tìm $m$ để phương trình sau có nghiệm:

$\sin 2x + 4(\cos x – \sin x) = m.$