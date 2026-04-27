# Phương trình thuần nhất bậc hai đối với sinx và cosx

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
Bài viết hướng dẫn phương pháp giải và biện luận phương trình thuần nhất bậc hai đối với sinx và cosx.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## I. KIẾN THỨC CƠ BẢN
Bài toán: Giải phương trình: $a{\sin ^2}x + b\sin x\cos x + c{\cos ^2}x = d$ $(1).$

PHƯƠNG PHÁP CHUNG: Ta lựa chọn một trong hai cách sau:

Cách 1: Thực hiện theo các bước:

+ Bước 1. Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình $(1)$ có dạng $a = d.$

+ Nếu $a = d$ thì $(1)$ nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Nếu $a \ne d$ thì $(1)$ không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Bước 2. Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^2}x \ne 0$ ta được:

$a{\tan ^2}x + b\tan x + c$ $= d\left( {1 + {{\tan }^2}x} \right).$

Đặt $t = \tan x$, phương trình có dạng:

$(a – d){t^2} + bt + c – d = 0$ $(2).$

+ Bước 3. Giải phương trình $(2)$ theo $t.$

Cách 2: Sử dụng các công thức:

${\sin ^2}x = \frac{{1 – \cos 2x}}{2}.$

${\cos ^2}x = \frac{{1 + \cos 2x}}{2}.$

$\sin x\cos x = \frac{1}{2}\sin 2x.$

Ta được: $b\sin 2x + (c – a)\cos 2x = d – c – a$ $(3).$

Đây là phương trình bậc nhất đối với sinx và cosx.

Nhận xét quan trọng:

1. Cách 1 thường được sử dụng với các bài toán yêu cầu giải phương trình và tìm điều kiện của tham số để phương trình có nghiệm thuộc tập $D.$

2. Cách 2 thường được sử dụng với các bài toán yêu cầu giải phương trình và tìm điều kiện của tham số để phương trình có nghiệm, vô nghiệm hoặc giải và biện luận phương trình theo tham số.

***Chú ý***: Nhiều phương trình ở dạng ban đầu không phải là phương trình đẳng cấp bậc hai, khi đó chúng ta cần đánh giá thông qua một hoặc nhiều phép biến đổi lượng giác. Cụ thể chúng ta đi xem xét ví dụ sau:

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Ví dụ 1: Giải phương trình: $2\sqrt 3 {\cos ^2}x + 6\sin x\cos x = 3 + \sqrt 3 .$

Cách 1: Biến đổi phương trình về dạng:

$\sqrt 3 (1 + \cos 2x) + 3\sin 2x = 3 + \sqrt 3$ $\Leftrightarrow \cos 2x + \sqrt 3 \sin 2x = \sqrt 3 .$

$\Leftrightarrow \frac{1}{2}\cos 2x + \frac{{\sqrt 3 }}{2}\sin 2x = \frac{{\sqrt 3 }}{2}$ $\Leftrightarrow \cos \left( {2x – \frac{\pi }{3}} \right) = \frac{{\sqrt 3 }}{2}.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \frac{\pi }{3} = \frac{\pi }{6} + 2k\pi }\\
{2x – \frac{\pi }{3} = – \frac{\pi }{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{4} + k\pi }\\
{x = \frac{\pi }{{12}} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng:

$0 = 3 + \sqrt 3$ (mâu thuẫn).

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình cho ${\cos ^2}x \ne 0$, ta được:

$2\sqrt 3 + 6\tan x = (3 + \sqrt 3 )\left( {1 + {{\tan }^2}x} \right)$ $\Leftrightarrow (3 + \sqrt 3 ){\tan ^2}x – 6\tan x + 3 – \sqrt 3 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 1}\\
{\tan x = \frac{{3 – \sqrt 3 }}{{3 + \sqrt 3 }} = \tan \alpha }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{\pi }{4} + k\pi }\\
{x = \alpha + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Ví dụ 2: Cho phương trình: $m{\sin ^2}x – 3\sin x\cos x – m – 1 = 0$ $(1).$

a. Giải phương trình với $m = 1.$

b. Tìm $m$ để phương trình có đúng $3$ nghiệm thuộc $\left( {0,\frac{{3\pi }}{2}} \right).$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: $– 1 = 0$ (mâu thuẫn).

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình cho ${\cos ^2}x \ne 0$, ta được:

$m{\tan ^2}x – 3\tan x$ $– (m + 1)\left( {1 + {{\tan }^2}x} \right) = 0$ $\Leftrightarrow {\tan ^2}x + 3\tan x + m + 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$f(t) = {t^2} + 3t + m + 1 = 0$ $(2).$

a. Với $m = 1$, ta được:

${t^2} + 3t + 2 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = – 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – 1}\\
{\tan x = – 2 = \tan \alpha }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + k\pi }\\
{x = \alpha + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = 1$ phương trình có hai họ nghiệm.

b. Để phương trình có đúng $3$ nghiệm thuộc $\left( {0,\frac{{3\pi }}{2}} \right).$

$\Leftrightarrow (2)$ có $2$ nghiệm phân biệt thoả mãn ${t_1} < 0 < {t_2}.$

$\Leftrightarrow af(0) < 0$ $\Leftrightarrow m + 1 < 0$ $\Leftrightarrow m < – 1.$

Vậy với $m < -1$ thoả mãn điều kiện đầu bài.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Ví dụ 3: (ĐHTS – 2000): Cho phương trình:

$2{\sin ^2}x + \sin x\cos x – {\cos ^2}x + m = 0$ $(1).$

a. Giải phương trình với $m = 1.$

b. Giải và biện luận phương trình theo $m.$

Biến đổi phương trình về dạng:

$2.\frac{{1 – \cos 2x}}{2} + \frac{1}{2}\sin 2x$ $– \frac{{1 + \cos 2x}}{2} = – m.$

$\Leftrightarrow \sin 2x – 3\cos 2x = – 2m – 1$ $(2).$

a. Với $m = 1$, ta được:

$\sin 2x – 3\cos 2x = – 3.$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Biến đổi phương trình về dạng:

$\frac{1}{{\sqrt {10} }}\sin 2x – \frac{3}{{\sqrt {10} }}\cos 2x = – \frac{3}{{\sqrt {10} }}.$

Đặt $\frac{1}{{\sqrt {10} }} = \cos \alpha$ và $\frac{3}{{\sqrt {10} }} = \sin \alpha$, khi đó ta được:

$\sin 2x\cos \alpha – \cos 2x\sin \alpha = – \sin \alpha$ $\Leftrightarrow \sin (2x – \alpha ) = \sin ( – \alpha ).$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \alpha = – \alpha + 2k\pi }\\
{2x – \alpha = \pi + \alpha + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \frac{\pi }{2} + \alpha + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

Cách 2: Biến đổi phương trình về dạng:

$\sin 2x = 3(1 – \cos 2x)$ $\Leftrightarrow 2\sin x\cos x = 6{\sin ^2}x$ $\Leftrightarrow (\cos x – 3\sin x)\sin x = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cos x – 3\sin x = 0}\\
{\sin x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cot x = 3 = \cot \alpha }\\
{\sin x = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

b. Biến đổi phương trình về dạng:

$\frac{1}{{\sqrt {10} }}\sin 2x – \frac{3}{{\sqrt {10} }}\cos 2x = \frac{{ – 2m – 1}}{{\sqrt {10} }}$ $\Leftrightarrow \sin (2x – \alpha ) = \frac{{ – 2m – 1}}{{\sqrt {10} }}.$

+ Nếu $\left| {\frac{{ – 2m – 1}}{{\sqrt {10} }}} \right| > 1$ $\Leftrightarrow m > \frac{{ – 1 + \sqrt {10} }}{2}$ hoặc $m < \frac{{ – 1 – \sqrt {10} }}{2}$, phương trình vô nghiệm.

+ Nếu $\left| {\frac{{ – 2m – 1}}{{\sqrt {10} }}} \right| \le 1$ $\Leftrightarrow \frac{{ – 1 – \sqrt {10} }}{2} \le m \le \frac{{ – 1 + \sqrt {10} }}{2}$, đặt $\frac{{ – 2m – 1}}{{\sqrt {10} }} = \sin \beta$ ta được:

$\sin (2x – \alpha ) = \sin \beta$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x – \alpha = \beta + 2k\pi }\\
{2x – \alpha = \pi – \beta + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{{\alpha + \beta }}{2} + k\pi }\\
{x = \frac{{\pi + \alpha – \beta }}{2} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

***Chú ý***: Nhiều phương trình ở dạng ban đầu chưa phải là phương trình đẳng cấp bậc hai, khi đó tự các em học sinh cần biết đánh giá hoặc thực hiện một vài phép biến đổi lượng giác.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Ví dụ 4: Cho phương trình: $m\sin x + \cos x = \frac{1}{{\cos x}}$, với $m \ne 0$ $(1).$

a. (ĐHAN – 1998): Giải phương trình khi $m = \sqrt 3 .$

b. Xác định $m$ để phương trình có nghiệm.

c. Giả sử $m$ là giá trị làm cho phương trình có nghiệm ${x_1}$, ${x_2}$ thoả mãn: ${x_1} + {x_2} \ne \frac{\pi }{2} + k\pi .$ Tính $\cos 2\left( {{x_1} + {x_2}} \right)$ theo $m.$

Điều kiện: $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Cách 1: Biến đổi phương trình về dạng:

$m\sin x.\cos x + {\cos ^2}x = 1$ $\Leftrightarrow m\sin x\cos x = {\sin ^2}x.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\sin x = 0}\\
{m\cos x = \sin x}
\end{array}} \right.
$$
 
$$
\mathop \Leftrightarrow \limits^{\cos x \ne 0} \left[ {\begin{array}{l}
{\sin x = 0}\\
{\tan x = m}
\end{array}} \right.
$$
 $(I).$

a. Với $m = \sqrt 3$, ta được:

$$
(I) \Leftrightarrow \left[ {\begin{array}{l}
{\sin x = 0}\\
{\tan x = \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \frac{\pi }{3} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = \sqrt 3$ phương trình có hai họ nghiệm.

b. Từ $(I)$ ta có ngay nhận xét phương trình $(1)$ có nghiệm với mọi $m.$

c. Vì ${x_1} + {x_2} \ne \frac{\pi }{2} + k\pi$, do đó có thể coi:

${x_1}$ là nghiệm của phương trình $\sin x = 0$ $\Rightarrow \tan {x_1} = 0.$

${x_2}$ là nghiệm của phương trình $\tan x = m$ $\Rightarrow \tan {x_2} = m.$

Suy ra:

$\cos 2\left( {{x_1} + {x_2}} \right)$ $= \cos 2{x_1}\cos 2{x_2} – \sin 2{x_1}\sin 2{x_2}$ $= \frac{{1 – {{\tan }^2}{x_1}}}{{1 + {{\tan }^2}{x_1}}}.\frac{{1 – {{\tan }^2}{x_2}}}{{1 + {{\tan }^2}{x_2}}}$ $– \frac{{2\tan {x_1}}}{{1 + {{\tan }^2}{x_1}}}.\frac{{2\tan {x_2}}}{{1 + {{\tan }^2}{x_2}}}$ $= \frac{{1 – {m^2}}}{{1 + {m^2}}}.$

Cách 2: Chia hai vế của phương trình $(1)$ cho $\cos x \ne 0$, ta được:

$m\tan x + 1 = 1 + {\tan ^2}x$ $\Leftrightarrow {\tan ^2}x – m\tan x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 0}\\
{\tan x = m}
\end{array}} \right.
$$
 $(I).$

a. Với $m = \sqrt 3$, ta được:

$$
(I) \Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 0}\\
{\tan x = \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \frac{\pi }{3} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = \sqrt 3$ phương trình có hai họ nghiệm.

b. Từ $(I)$ ta có ngay nhận xét phương trình $(1)$ có nghiệm với mọi $m.$

c. Vì ${x_1} + {x_2} \ne \frac{\pi }{2} + k\pi$, do đó có thể coi:

${x_1}$ là nghiệm của phương trình $\tan x = 0$ $\Rightarrow \tan {x_1} = 0.$

${x_2}$ là nghiệm của phương trình $\tan x = m$ $\Rightarrow \tan {x_2} = m.$

Suy ra: $\cos 2\left( {{x_1} + {x_2}} \right) = \frac{{1 – {m^2}}}{{1 + {m^2}}}.$

<!-- chunk:6 level:1 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: (ĐHKTCN TP HCM – 1998): Cho phương trình:

${\sin ^2}x + 2(m – 1)\sin x\cos x$ $– (m + 1){\cos ^2}x = m$ $(1).$

a. Giải phương trình với $m = -2.$

b. Tìm $m$ để phương trình có nghiệm.

Biến đổi phương trình về dạng:

$\frac{{1 – \cos 2x}}{2} + (m – 1)\sin 2x$ $– (m + 1)\frac{{1 + \cos 2x}}{2} = m.$

$\Leftrightarrow 2(m – 1)\sin 2x$ $– (m + 2)\cos 2x = 3m$ $(2).$

a. Với $m = – 2$, ta được:

$\sin 2x = 1$ $\Leftrightarrow 2x = \frac{\pi }{2} + 2k\pi$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy với $m = – 2$ phương trình có một họ nghiệm.

b. Phương trình $(1)$ có nghiệm $\Leftrightarrow (2)$ có nghiệm:

$\Leftrightarrow {a^2} + {b^2} \ge {c^2}$ $\Leftrightarrow 4{(m – 1)^2} + {(m + 2)^2} \ge 9{m^2}$ $\Leftrightarrow {m^2} + m – 2 \le 0$ $\Leftrightarrow – 2 \le m \le 1.$

Vậy với $– 2 \le m \le 1$ phương trình có nghiệm.

## Bài 2: (ĐHGTVT – 1999): Tìm $m$ để phương trình sau có nghiệm $x \in \left( {0,\frac{\pi }{4}} \right):$

$m{\cos ^2}x – 4\sin x\cos x + m – 2 = 0$ $(1).$

Với $x \in \left( {0,\frac{\pi }{4}} \right)$ $\Rightarrow \cos x \ne 0$, chia hai vế của phương trình cho ${\cos ^2}x \ne 0$, ta được:

$m – 4\tan x + (m – 2)\left( {1 + {{\tan }^2}x} \right) = 0$ $\Leftrightarrow (m – 2){\tan ^2}x – 4\tan x + 2m – 2 = 0$ $(2).$

Đặt $t = \tan x$, vì $x \in \left( {0,\frac{\pi }{4}} \right)$ nên $t \in (0,1)$, ta được:

$(m – 2){t^2} – 4t + 2m – 2 = 0$ $(3).$

Khi đó $(1)$ có nghiệm $x \in \left( {0,\frac{\pi }{4}} \right)$ $\Leftrightarrow (3)$ có nghiệm $t \in (0,1).$

Ta có thể lựa chọn một trong hai cách sau:

Cách 1: Đại số:

+ Với $m – 2 = 0$ $\Leftrightarrow m = 2$, khi đó $(3)$ có dạng:

$– 4t + 2 = 0$ $\Leftrightarrow t = \frac{1}{2} \in (0,1).$

Vậy $m = 2$ thoả mãn điều kiện đầu bài.

+ Với $m – 2 \ne 0$ $\Leftrightarrow m \ne 2$, khi đó $(3)$ có nghiệm $t \in (0,1).$

$$
\Leftrightarrow \left[ \begin{array}{l}
\left( 3 \right){\rm{\:có\:1\:nghiệm\:thuộc\:}}(0,1)\\
\left( 3 \right){\rm{\:có\:2\:nghiệm\:thuộc\:}}(0,1)
\end{array} \right..
$$

$$
\Leftrightarrow \left[ \begin{array}{l}
f(1)f(0) < 0\\
\left\{ {\begin{array}{l}
{\Delta ‘ \ge 0}\\
{af(1) > 0}\\
{af(0) > 0}\\
{0 < \frac{S}{2} < 1}
\end{array}} \right.
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
(3m – 8)(2m – 2) < 0\\
\left\{ {\begin{array}{l}
{ – 2{m^2} + 6m \ge 0}\\
{(m – 2)(3m – 8) > 0}\\
{(m – 2)(2m – 2) > 0}\\
{0 < \frac{2}{{m – 2}} < 1}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow 1 < m < \frac{8}{3}.$

Vậy với $1 < m < \frac{8}{3}$ phương trình có nghiệm $x \in \left( {0,\frac{\pi }{4}} \right).$

Cách 2: Viết lại phương trình dưới dạng:

$\frac{{2{t^2} + 4t + 2}}{{{t^2} + 2}} = m.$

Phương trình $(1)$ có nghiệm $x \in \left( {0,\frac{\pi }{4}} \right)$ $\Leftrightarrow$ đường thẳng $y = m$ cắt đồ thị hàm số $y = \frac{{2{t^2} + 4t + 2}}{{{t^2} + 2}}$ trên $(0,1).$

Xét hàm số $(C):y = \frac{{2{t^2} + 4t + 2}}{{{t^2} + 2}}$ trên khoảng $(0,1).$

Đạo hàm: $y’ = \frac{{ – 4{t^2} + 4t + 8}}{{{{\left( {{t^2} + 2} \right)}^2}}}$ $= \frac{{ – 4(t + 1)(t – 2)}}{{{{\left( {{t^2} + 2} \right)}^2}}} > 0$ với mọi $t \in (0,1)$, tức là hàm số đồng biến trên $(0,1).$

Do đó đường thẳng $y = m$ cắt đồ thị hàm số $(C)$ trên khoảng $(0,1).$

$\Leftrightarrow y(0) < m < y(1)$ $\Leftrightarrow 1 < m < \frac{8}{3}.$

Vậy với $1 < m < \frac{8}{3}$ phương trình có nghiệm $x \in \left( {0,\frac{\pi }{4}} \right).$

<!-- chunk:7 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 1. Giải các phương trình:

a. $4{\sin ^2}x + 3\sqrt 3 \sin 2x – 2{\cos ^2}x = 4.$

b. $2{\sin ^2}x + 3{\cos ^2}x = 5\sin x\cos x.$

<!-- chunk:8 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 2. Giải các phương trình:

a. ${\sin ^2}x – 3\sin x\cos x = 1.$

b. $4\sin x + 6\cos x = \frac{1}{{\cos x}}.$

<!-- chunk:9 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 3. Cho phương trình: $3{\sin ^2}x + m\sin 2x + 4{\cos ^2}x = 0.$

a. Giải phương trình khi $m = 4.$

b. Xác định $m$ để phương trình có nghiệm.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 4. Cho phương trình: $(m + 1){\sin ^2}x – 2\sin x\cos x$ $+ \cos 2x = 0.$

a. Giải phương trình khi $m = 0.$

b. Xác định $m$ để phương trình có đúng hai nghiệm thuộc $\left( {0,\frac{\pi }{2}} \right).$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 5. Cho phương trình: $2{\sin ^2}x + (5m – 2)\sin 2x$ $– 3(m + 1){\cos ^2}x = 3m.$

a. Giải phương trình khi $m = \frac{2}{3}.$

b. Xác định $m$ để phương trình đúng ba nghiệm thuộc $\left( { – \frac{\pi }{2},\pi } \right).$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-hai-doi-voi-sinx-va-cosx.html -->
## Bài tập 6. Cho phương trình: $m\sin x + (m + 1)\cos x = \frac{m}{{\cos x}}.$

a. Giải phương trình khi $m = \frac{1}{2}.$

b. Xác định $m$ để phương trình có nghiệm.

c. Giả sử $m$ là giá trị làm cho phương trình có nghiệm ${x_1}$, ${x_2}$ thoả mãn: ${x_1} + {x_2} \ne \frac{\pi }{2} + k\pi .$ Tính $\cos 2\left( {{x_1} + {x_2}} \right)$ theo $m.$