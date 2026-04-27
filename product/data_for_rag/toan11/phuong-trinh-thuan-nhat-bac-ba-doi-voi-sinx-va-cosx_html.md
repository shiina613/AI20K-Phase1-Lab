# Phương trình thuần nhất bậc ba đối với sinx và cosx

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
Bài viết hướng dẫn phương pháp giải và biện luận phương trình thuần nhất bậc ba đối với sinx và cosx.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## I. PHƯƠNG PHÁP
Bài toán: Giải phương trình: $a{\sin ^3}x + b{\sin ^2}x\cos x$ $+ c\sin x{\cos ^2}x + d{\cos ^3}x = 0$ $(1).$

PHƯƠNG PHÁP CHUNG: Thực hiện theo các bước:

+ Bước 1: Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình $(1)$ có dạng $a = 0.$

+ Nếu $a = 0$ thì $(1)$ nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Nếu $a \ne 0$ thì $(1)$ không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Bước 2: Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$a{\tan ^3}x + b{\tan ^2}x + c\tan x + d = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$a{t^3} + b{t^2} + ct + d = 0$ $(2).$

+ Bước 3: Giải phương trình $(2)$ theo $t$ (tham khảo bài viết cách giải phương trình bậc 3 tổng quát).

Mở rộng: Phương pháp giải trên được mở rộng cho phương trình đẳng cấp bậc $n$ đối với sin và cos, đó là phương trình có dạng:

$\sum\limits_{k = 0}^n {{a_k}} {\sin ^{n – k}}x{\cos ^k}x = 0.$

Tuy nhiên để linh hoạt, các em học sinh cần nhớ rằng vì ${\sin ^2}x + {\cos ^2}x = 1$ nên với các nhân tử có bậc $k$ cũng được coi là có bậc $k + 2l$, do vậy chúng ta có dạng mở rộng của phương trình thuần nhất bậc ba như sau:

$a{\sin ^3}x + b{\sin ^2}x\cos x$ $+ c\sin x{\cos ^2}x + d{\cos ^3}x$ $+ (e\sin x + f\cos x) = 0.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 1: (ĐHNT – 1996): Giải phương trình sau: $4{\sin ^3}x + 3{\sin ^2}x\cos x – \sin x – {\cos ^3}x = 0.$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng:

$4{\sin ^3}\left( {\frac{\pi }{2} + k\pi } \right) – \sin \left( {\frac{\pi }{2} + k\pi } \right) = 0$ (mâu thuẫn).

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$4{\tan ^3}x + 3{\tan ^2}x$ $– \left( {1 + {{\tan }^2}x} \right)\tan x – 1 = 0$ $\Leftrightarrow 3{\tan ^3}x + 3{\tan ^2}x – \tan x – 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$3{t^3} + 3{t^2} – t – 1 = 0$ $\Leftrightarrow (t + 1)\left( {3{t^2} – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 1/\sqrt 3 }\\
{t = – 1/\sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – 1}\\
{\tan x = 1/\sqrt 3 }\\
{\tan x = – 1/\sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + k\pi }\\
{x = \frac{\pi }{6} + k\pi \quad }\\
{x = – \frac{\pi }{6} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 2: Giải phương trình sau:

${\sin ^4}x – 3{\sin ^2}x{\cos ^2}x$ $– 4\sin x{\cos ^3}x – 3{\cos ^4}x = 0.$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng ${\sin ^4}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ mâu thuẫn.

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^4}x \ne 0$, ta được:

${\tan ^4}x – 3{\tan ^2}x – 4\tan x – 3 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

${t^4} – 3{t^2} – 4t – 3 = 0$ $\Leftrightarrow \left( {{t^4} – 2{t^2} + 1} \right) – \left( {{t^2} + 4t + 4} \right) = 0$ $\Leftrightarrow \left( {{t^2} – t – 3} \right)\left( {{t^2} + t + 1} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t^2} – t – 3 = 0}\\
{{t^2} + t + 1 = 0\:{\rm{(vô\:nghiệm)}}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t_1} = \frac{{1 – \sqrt {13} }}{2}}\\
{{t_2} = \frac{{1 + \sqrt {13} }}{2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = \frac{{1 – \sqrt {13} }}{2} = \tan \alpha }\\
{\tan x = \frac{{1 + \sqrt {13} }}{2} = \tan \beta }
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \beta + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

***Chú ý***: Tồn tại những phương trình ở dạng ban đầu chưa phải là phương trình thuần nhất, khi đó cần thực hiện một vài phép biến đổi lượng giác thích hợp.

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 3: (ĐHNN I Khối B – 1999): Giải phương trình sau:

$(\tan x + 1){\sin ^2}x$ $= 3(\cos x – \sin x)\sin x + 3.$

Điều kiện: $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^2}x \ne 0$, ta được:

$(\tan x + 1){\tan ^2}x$ $= 3(1 – \tan x)\tan x + 3\left( {1 + {{\tan }^2}x} \right)$ $\Leftrightarrow {\tan ^3}x + {\tan ^2}x – 3\tan x – 3 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

${t^3} + {t^2} – 3t – 3 = 0$ $\Leftrightarrow (t + 1)\left( {{t^2} – 3} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = \sqrt 3 }\\
{t = – \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – 1}\\
{\tan x = \sqrt 3 }\\
{\tan x = – \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + k\pi }\\
{x = \pm \frac{\pi }{3} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

<!-- chunk:5 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 4: (ĐHQG TPHCM – 1998): Giải phương trình sau:

${\sin ^3}\left( {x – \frac{\pi }{4}} \right) = \sqrt 2 \sin x.$

Biến đổi phương trình về dạng:

$2\sqrt 2 {\sin ^3}\left( {x – \frac{\pi }{4}} \right) = 4\sin x$ $\Leftrightarrow {\left[ {\sqrt 2 \sin \left( {x – \frac{\pi }{4}} \right)} \right]^3} = 4\sin x$ $\Leftrightarrow {(\sin x – \cos x)^3} = 4\sin x.$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: ${\sin ^3}\left( {\frac{\pi }{2} + k\pi } \right) = 4\sin \left( {\frac{\pi }{2} + k\pi } \right)$ mâu thuẫn.

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

${(\tan x – 1)^3} = 4\left( {1 + {{\tan }^2}x} \right)\tan x$ $\Leftrightarrow 3{\tan ^3}x + 3{\tan ^2}x + \tan x – 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$3{t^3} + 3{t^2} + t – 1 = 0$ $\Leftrightarrow (t + 1)\left( {3{t^2} + 1} \right) = 0$ $\Leftrightarrow t = – 1$ $\Leftrightarrow x = – \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

Chú ý: Các em học sinh cũng cần nhớ rằng ngoài phương pháp chính quy để giải mọi phương trình đẳng cấp bậc $3$ thì trong một vài trường hợp riêng biệt cũng có thể giải nó bằng phương pháp phân tích thành phương trình tích. Cụ thể ta đi xem xét ví dụ sau:

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 5: (ĐHTS – 1996): Giải phương trình sau:

${\cos ^3}x + {\sin ^3}x = \sin x – \cos x$ $(1).$

Cách 1: Sử dụng phương pháp giải phương trình đẳng cấp bậc $3:$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: $\pm 1 = \pm 1.$

Vậy phương trình nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$1 + {\tan ^3}x$ $= \left( {1 + {{\tan }^2}x} \right)\tan x – \left( {1 + {{\tan }^2}x} \right)$ $\Leftrightarrow {\tan ^2}x – \tan x + 2 = 0$ vô nghiệm.

Vậy phương trình có một họ nghiệm.

Cách 2: Sử dụng phương pháp phân tích:

Biến đổi phương trình về dạng:

${\cos ^3}x + {\sin ^3}x$ $= (\sin x – \cos x)\left( {{{\cos }^2}x + {{\sin }^2}x} \right).$

$\Leftrightarrow 2{\cos ^3}x + \cos x{\sin ^2}x – \sin x{\cos ^2}x = 0.$

$\Leftrightarrow \left( {2{{\cos }^2}x + {{\sin }^2}x – \sin x\cos x} \right)\cos x = 0.$

$\Leftrightarrow \left( {1 + {{\cos }^2}x – \sin x\cos x} \right)\cos x = 0.$

$\Leftrightarrow \cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 6: Giải phương trình:

$\frac{{1 – \tan x}}{{1 + \tan x}} = 1 + \sin 2x.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\cos x \ne 0}\\
{\tan x \ne – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ne \frac{\pi }{2} + k\pi }\\
{x \ne – \frac{\pi }{4} + k\pi }
\end{array}} \right.
$$
, $k \in Z$ $(I).$

Cách 1: Biến đổi phương trình về dạng:

$\frac{{\cos x – \sin x}}{{\cos x + \sin x}} = {(\cos x + \sin x)^2}$ $\Leftrightarrow \cos x – \sin x = {(\cos x + \sin x)^3}.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$1 + {\tan ^2}x – \left( {1 + {{\tan }^2}x} \right)\tan x$ $= {(1 + \tan x)^3}$ $\Leftrightarrow {\tan ^3}x + {\tan ^2}x + 2\tan x = 0$ $\Leftrightarrow \left( {{{\tan }^2}x + \tan x + 2} \right)\tan x = 0$ $\Leftrightarrow \tan x = 0$ $\Leftrightarrow x = k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

Cách 2: Biến đổi phương trình về dạng:

$\frac{{\cos x – \sin x}}{{\cos x + \sin x}} = {(\cos x + \sin x)^2}$ $\Leftrightarrow \frac{{\cos \left( {x + \frac{\pi }{4}} \right)}}{{\sin \left( {x + \frac{\pi }{4}} \right)}} = 2{\sin ^2}\left( {x + \frac{\pi }{4}} \right)$ $\Leftrightarrow \cot \left( {x + \frac{\pi }{4}} \right) = \frac{2}{{1 + {{\cot }^2}\left( {x + \frac{\pi }{4}} \right)}}.$

Đặt $t = \cot \left( {x + \frac{\pi }{4}} \right)$, ta được:

$t = \frac{2}{{1 + {t^2}}}$ $\Leftrightarrow {t^3} + t – 2 = 0$ $\Leftrightarrow (t – 1)\left( {{t^2} + t + 2} \right) = 0$ $\Leftrightarrow t = 1.$

$\Leftrightarrow \cot \left( {x + \frac{\pi }{4}} \right) = 1$ $\Leftrightarrow x + \frac{\pi }{4} = \frac{\pi }{4} + k\pi$ $\Leftrightarrow x = k\pi$, $k \in Z.$

Vậy phương trình có một họ nghiệm.

<!-- chunk:8 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 7: Giải phương trình sau:

${(\sin x – 2\cos x)^4}$ $+ (\sin x – 2\cos x)\left( {5 – 7\sin 2x + 7{{\cos }^2}x} \right)\cos x$ $+ {\cos ^4}x = 0.$

Biến đổi phương trình về dạng:

${(\sin x – 2\cos x)^4}$ $+ (\sin x – 2\cos x)\left( {5{{\sin }^2}x – 14\sin x\cos x + 13{{\cos }^2}x} \right)\cos x$ $+ {\cos ^4}x = 0.$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: ${\sin ^4}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ mâu thuẫn.

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^4}x \ne 0$, ta được:

${(\tan x – 2)^4}$ $+ (\tan x – 2)\left( {5{{\tan }^2}x – 14\tan x + 13} \right)$ $+ 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

${(t – 2)^4}$ $+ (t – 2)\left( {5{t^2} – 14t + 13} \right)$ $+ 1 = 0$ $(1).$

Nhận xét rằng đây không phải là một phương trình hồi quy, tuy nhiên nếu đặt ẩn phụ thích hợp ta sẽ có một phương trình hồi quy.

Thật vậy, đặt $y = t – 2.$

$(1) \Leftrightarrow {y^4}$ $+ y\left[ {5{{(y + 2)}^2} – 14(y + 2) + 13} \right]$ $+ 1 = 0.$

$\Leftrightarrow {y^4} + 5{y^3} + 6{y^2} + 5y + 1 = 0$ $(2).$

Nhận xét rằng $y = 0$ không phải là nghiệm của phương trình. Chia cả hai vế của phương trình cho ${y^2} \ne 0$, ta được phương trình tương đương:

$\left( {{y^2} + \frac{1}{{{y^2}}}} \right) + 5\left( {y + \frac{1}{y}} \right) + 6 = 0.$

Đặt $u = y + \frac{1}{y}$, điều kiện $|u| \ge 2$, suy ra ${y^2} + \frac{1}{{{y^2}}} = {u^2} – 2.$

Khi đó phương trình trên có dạng:

${u^2} + 5u + 4 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = – 1\:{\rm{(loại)}}}\\
{u = – 4}
\end{array}} \right..
$$

+ Với $u = -4$, ta được:

$y + \frac{1}{y} = – 4$ $\Leftrightarrow {y^2} + 4y + 1 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{y_1} = – 2 – \sqrt 3 }\\
{{y_2} = – 2 + \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t_1} = – \sqrt 3 }\\
{{t_2} = \sqrt 3 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – \sqrt 3 }\\
{\tan x = \sqrt 3 }
\end{array}} \right.
$$
 $\Leftrightarrow x = \pm \frac{\pi }{3} + k\pi$, $k \in Z.$

Vậy phương trình có hai họ nghiệm.

<!-- chunk:9 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 8: Cho phương trình:

$2(m – 2){\sin ^3}x$ $– (5m – 2){\sin ^2}x\cos x$ $+ 2\sin x{\cos ^2}x$ $– (m + 1){\cos ^3}x = 0$ $(1).$

a. Giải phương trình với $m = 3.$

b. Xác định $m$ để phương trình có đúng một nghiệm $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right).$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng:

$2(m – 2){\sin ^3}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ $\Leftrightarrow m = 2.$

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$2(m – 2){\tan ^3}x$ $– (5m – 2){\tan ^2}x$ $+ 2\tan x – m – 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$2(m – 2){t^3} – (5m – 2){t^2} + 2t – m – 1 = 0$ $\Leftrightarrow (2t – 1)\left[ {(m – 2){t^2} – 2mt + m + 1} \right] = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{2t – 1 = 0}\\
{g(t) = (m – 2){t^2} – 2mt + m + 1 = 0\:(2)}
\end{array}} \right.
$$
 $(I).$

a. Với $m = 3$, ta được:

$$
(I) \Leftrightarrow \left[ {\begin{array}{l}
{2t – 1 = 0}\\
{{t^2} – 6t + 4 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{1}{2}}\\
{t = 3 – \sqrt 5 }\\
{t = 3 + \sqrt 5 }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = \frac{1}{2} = \tan \alpha }\\
{\tan x = 3 – \sqrt 5 = \tan \beta }\\
{\tan x = 3 + \sqrt 5 = \tan \gamma }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \beta + k\pi }\\
{x = \gamma + k\pi }
\end{array}} \right..
$$

Vậy phương trình có ba họ nghiệm.

b. Để phương trình có đúng một nghiệm $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right).$

$\Leftrightarrow (I)$ có duy nhất nghiệm $t = \frac{1}{2}.$

Trường hợp 1: Nếu $m – 2 = 0$ $\Leftrightarrow m = 2.$

Khi đó:

$(2) \Leftrightarrow – 4t + 3 = 0$ $\Leftrightarrow t = \frac{3}{4} \ne \frac{1}{2}.$

Suy ra $m = 2$ không thoả mãn.

Trường hợp 2: Nếu $m – 2 \ne 0$ $\Leftrightarrow m \ne 2.$

Khi đó điều kiện:

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\Delta {‘_g} < 0}\\
{\left\{ {\begin{array}{l}
{\Delta {‘_g} = 0}\\
{g\left( {\frac{1}{2}} \right) = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
m + 2 < 0\\
\left\{ {\begin{array}{l}
{m + 2 = 0}\\
{m + 2 = 0}
\end{array}} \right.
\end{array} \right.
$$
 $\Leftrightarrow m \le – 2.$

Vậy với $m \le – 2$ phương trình có nghiệm duy nhất.

<!-- chunk:10 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 9: Cho phương trình:

${\sin ^3}x – 3m{\sin ^2}x\cos x$ $+ 3\left( {{m^2} – 1} \right)\sin x{\cos ^2}x$ $– \left( {{m^2} – 1} \right){\cos ^3}x = 0$ $(1).$

a. Giải phương trình với $m = 1.$

b. Xác định $m$ để phương trình có đúng ba nghiệm $x \in \left( {0,\frac{\pi }{2}} \right).$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: ${\sin ^3}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ mâu thuẫn.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

${\tan ^3}x – 3m{\tan ^2}x$ $+ 3\left( {{m^2} – 1} \right)\tan x – {m^2} + 1 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

${t^3} – 3m{t^2} + 3\left( {{m^2} – 1} \right)t – {m^2} + 1 = 0$ $(2).$

a. Với $m = 1$, ta được:

$(2) \Leftrightarrow {t^3} – 3{t^2} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 0}\\
{\tan x = 3 = \tan \alpha }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \alpha + k\pi }
\end{array}} \right..
$$

Vậy phương trình có hai họ nghiệm.

b. Để phương trình có đúng ba nghiệm $x \in \left( {0,\frac{\pi }{2}} \right)$ $\Leftrightarrow (2)$ có ba nghiệm phân biệt dương.

Xét hàm số $y = {t^3} – 3m{t^2} + 3\left( {{m^2} – 1} \right)t – {m^2} + 1.$

Ta có:

$y’ = 3{t^2} – 6mt + 3\left( {{m^2} – 1} \right).$

$y’ = 0$ $\Leftrightarrow 3{t^2} – 6mt + 3\left( {{m^2} – 1} \right) = 0$ $\Leftrightarrow {x^2} – 2mx + {m^2} – 1 = 0$ $(3).$

Ta có:

$\Delta’ = {m^2} – {m^2} + 1 = 1 > 0$, $\forall m.$

Khi đó $(3)$ luôn có $2$ nghiệm phân biệt ${t_1} = m – 1$ và ${t_2} = m + 1$ với mọi $m.$

Trước hết điều kiện để đồ thị hàm số cắt $Ot$ tại ba điểm phân biệt $\Leftrightarrow$ hàm số có cực đại, cực tiểu và ${y_{CĐ}}.{y_{CT}} < 0$ $\Leftrightarrow y\left( {{t_1}} \right)y\left( {{t_2}} \right) < 0$ $(4).$

Khi đó để giải bất phương trình $(4)$ trước hết đi tính $y\left( {{t_1}} \right)$, $y\left( {{t_2}} \right)$ bằng cách:

Thực hiện phép chia $y$ cho $y’$ ta được:

$y = \frac{1}{3}y'(t – m)t$ $– 2t + {m^3} – {m^2} – m + 1.$

Khi đó:

$y\left( {{t_1}} \right) = (m – 1)\left( {{m^2} – 3} \right)$ và $y\left( {{t_2}} \right) = (m + 1)\left( {{m^2} – 2m – 1} \right).$

Suy ra:

$(4) \Leftrightarrow$ $(m – 1)\left( {{m^2} – 3} \right)(m + 1)\left( {{m^2} – 2m – 1} \right) < 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – \sqrt 3 < m < – 1}\\
{1 – \sqrt 2 < m < 1}\\
{\sqrt 3 < m < 1 + \sqrt 2 }
\end{array}} \right.
$$
 $(I).$

Đồ thị hàm số cắt $Ot$ tại ba điểm phân biệt có hoành độ dương là:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{t_1} > 0}\\
{{t_2} > 0}\\
{y(0) < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m – 1 > 0}\\
{m + 1 > 0}\\
{ – \left( {{m^2} – 1} \right) < 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > 1$ $(II).$

Kết hợp $(I)$ và $(II)$ được $\sqrt 3 < m < 1 + \sqrt 2 .$

Vậy với $\sqrt 3 < m < 1 + \sqrt 2$ thoả mãn điều kiện đầu bài.

<!-- chunk:11 level:3 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Ví dụ 10: Cho phương trình:

$m{\cos ^4}x$ $+ \cos 2x(\sin x + 3\cos x)(\sin x + 5\cos x)$ $= 0$ $(1).$

a. Giải phương trình với $m = 9.$

b. Xác định $m$ để phương trình có đúng bốn nghiệm $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right).$

Biến đổi phương trình về dạng:

$m{\cos ^4}x$ $– (\sin x – \cos x)(\sin x + \cos x)(\sin x + 3\cos x)(\sin x + 5\cos x)$ $= 0$ $(2).$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: $– {\sin ^4}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ mâu thuẫn.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(2)$ cho ${\cos ^4}x \ne 0$, ta được:

$m –$ $(\tan x – 1)(\tan x + 1)(\tan x + 3)(\tan x + 5)$ $= 0.$

Đặt $u = \tan x$, phương trình có dạng:

$m – (u – 1)(u + 1)(u + 3)(u + 5) = 0$ $\Leftrightarrow \left( {{u^2} + 4u – 5} \right)\left( {{u^2} + 4u + 3} \right) = m.$

Đặt $t = {u^2} + 4u – 5$, điều kiện $t \ge – 9.$

Suy ra ${u^2} + 4u + 3 = t + 8.$

Khi đó phương trình trên có dạng:

$t(t + 8) = m$ $\Leftrightarrow f(t) = {t^2} + 8t – m = 0$ $(3).$

a. Với $m = 9$, ta được:

$(3) \Leftrightarrow {t^2} + 8t – 9 = 0$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = – 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{u^2} + 4u – 5 = 1}\\
{{u^2} + 4u – 5 = – 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{u = 2 – \sqrt 8 }\\
{u = 2 + \sqrt 8 }\\
{u = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 2 – \sqrt 8 = \tan \alpha }\\
{\tan x = 2 + \sqrt 8 = \tan \beta }\\
{\tan x = 2 = \tan \gamma }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \beta + k\pi }\\
{x = \gamma + k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

b. Phương trình $(1)$ có $4$ nghiệm $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right)$ $\Leftrightarrow (3)$ có nghiệm $– 9 < {t_1} < {t_2}.$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta ‘ > 0}\\
{f( – 9) > 0}\\
{S/2 > – 9}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{16 + m > 0}\\
{9 – m > 0}\\
{ – 4 > – 9}
\end{array}} \right.
$\Leftrightarrow – 16 < m < 9.$

Vậy với $– 16 < m < 9$ phương trình có bốn nghiệm phân biệt $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right).$

<!-- chunk:12 level:1 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: (HVKTQS – 1996): Giải phương trình sau: $\sin 3x = 2{\cos ^3}x.$

Biến đổi phương trình về dạng:

$3\sin x – 4{\sin ^3}x = 2{\cos ^3}x$ $\Leftrightarrow 4{\sin ^3}x – 3\sin x + 2{\cos ^3}x = 0.$

Bạn đọc tự giải tiếp.

## Bài 2: (ĐHQG – 1996): Giải phương trình sau: $1 + 3\sin 2x = 2\tan x.$

Điều kiện: $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Biến đổi phương trình về dạng:

$\cos x + 6\sin x{\cos ^2}x = 2\sin x.$

Bạn đọc tự giải tiếp.

## Bài 3: (ĐHQG – 1998): Giải phương trình: $8{\cos ^3}\left( {x + \frac{\pi }{3}} \right) = \cos 3x.$

Biến đổi phương trình về dạng:

$8{\left( {\frac{1}{2}\cos x – \frac{{\sqrt 3 }}{2}\sin x} \right)^3}$ $= 4{\cos ^3}x – 3\cos x.$

$\Leftrightarrow {(\cos x – \sqrt 3 \sin x)^3}$ $= 4{\cos ^3}x – 3\cos x$ $(1).$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z.$

Khi đó phương trình có dạng: ${\left[ { – \sqrt 3 \sin \left( {\frac{\pi }{2} + k\pi } \right)} \right]^3} = 0$ mâu thuẫn.

Vậy phương trình không nhận $x = \frac{\pi }{2} + k\pi$ làm nghiệm.

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

${\left[ {1 – \sqrt 3 \left( {1 + {{\tan }^2}x} \right)\tan x} \right]^3}$ $= 4 – 3\left( {1 + {{\tan }^2}x} \right).$

$\Leftrightarrow \sqrt 3 {\tan ^3}x – 4{\tan ^2}x + \sqrt 3 \tan x = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$\sqrt 3 {t^3} – 4{t^2} + \sqrt 3 t = 0$ $\Leftrightarrow t\left( {\sqrt 3 {t^2} – 4t + \sqrt 3 } \right) = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 0}\\
{t = \sqrt 3 }\\
{t = \frac{1}{{\sqrt 3 }}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = 0}\\
{\tan x = \sqrt 3 }\\
{\tan x = \frac{1}{{\sqrt 3 }}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = k\pi }\\
{x = \frac{\pi }{3} + k\pi }\\
{x = \frac{\pi }{6} + k\pi }
\end{array}} \right.
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

## Bài 4: Cho phương trình:

$m{\sin ^3}x$ $+ (3m – 4){\sin ^2}x\cos x$ $+ (3m – 7)\sin x{\cos ^2}x$ $+ (m – 3){\cos ^3}x = 0$ $(1).$

a. Giải phương trình với $m = 3.$

b. Xác định $m$ để phương trình có $3$ nghiệm phân biệt thuộc $\left( { – \frac{\pi }{2},0} \right].$

Xét hai trường hợp:

+ Với $\cos x = 0$ $\Leftrightarrow x = \frac{\pi }{2} + k\pi$, $k \in Z$ ta được:

$m{\sin ^3}\left( {\frac{\pi }{2} + k\pi } \right) = 0$ $\Leftrightarrow m = 0.$

+ Với $\cos x \ne 0$ $\Leftrightarrow x \ne \frac{\pi }{2} + k\pi$, $k \in Z.$

Chia hai vế của phương trình $(1)$ cho ${\cos ^3}x \ne 0$, ta được:

$m{\tan ^3}x + (3m – 4){\tan ^2}x$ $+ (3m – 7)\tan x + m – 3 = 0.$

Đặt $t = \tan x$, phương trình có dạng:

$m{t^3} + (3m – 4){t^2}$ $+ (3m – 7)t + m – 3 = 0.$

$\Leftrightarrow (t + 1)\left[ {m{t^2} + 2(m – 2)t + m – 3} \right] = 0.$
\Leftrightarrow \left[ {\begin{array}{l}
{t + 1 = 0}\\
{g(t) = m{t^2} + 2(m – 2)t + m – 3 = 0\:(2)}
\end{array}} \right.
$(I).$

a. Với $m = 3$, ta được:
(I) \Leftrightarrow \left[ {\begin{array}{l}
{t + 1 = 0}\\
{3{t^2} + 2t = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 0}\\
{t = – 2/3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – 1}\\
{\tan x = 0}\\
{\tan x = – 2/3 = \tan \alpha }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{4} + k\pi }\\
{x = k\pi }\\
{x = \alpha + k\pi }
\end{array}} \right..
Vậy với $m = 3$ phương trình có ba họ nghiệm.

b. Để phương trình có $3$ nghiệm phân biệt thuộc $\left( { – \frac{\pi }{2},0} \right]$ $\Leftrightarrow (2)$ có $2$ nghiệm phân biệt không dương $\left( {{t_1} < {t_2} \le 0} \right)$ khác $– 1.$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \ne 0}\\
{\Delta {‘_g} > 0}\\
{ag(0) \ge 0}\\
{\frac{S}{2} < 0}\\
{g( – 1) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{4 – m > 0}\\
{m(m – 3) \ge 0}\\
{ – \frac{{m – 2}}{m} < 0}\\
{1 \ne 0}
\end{array}} \right.
$\Leftrightarrow 3 \le m < 4.$

Vậy với $m \in [3,4)$ phương trình có ba nghiệm phân biệt không dương.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 1. Giải các phương trình sau:

a. (ĐH Đà Nẵng – 1999): ${\cos ^3}x – {\sin ^3}x = \cos x – \sin x.$

b. (ĐHL – 1996): $4{\sin ^3}x – {\sin ^2}x\cos x$ $– 3\sin x + 3{\cos ^3}x = 0.$

c. ${\sin ^3}x – 5{\sin ^2}x\cos x$ $+ 7\sin x{\cos ^2}x – 2{\cos ^3}x = 0.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 2. Giải các phương trình sau:

a. $5(\sin x + \cos x)$ $+ \sin 3x – \cos 3x$ $= 2\sqrt 2 (2 + \sin 2x).$

b. ${\sin ^3}x – 5{\sin ^2}x\cos x$ $– 3\sin x{\cos ^2}x + 3{\cos ^3}x = 0.$

<!-- chunk:15 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 3. Giải các phương trình sau:

a. ${\sin ^3}x – 3\sin x{\cos ^2}x – {\cos ^3}x = 0.$

b. ${\sin ^3}x + \sin x{\cos ^2}x – {\cos ^3}x = 0.$

<!-- chunk:16 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 4. Giải các phương trình sau:

a. (HVNH TPHCM – 2000): $\sin 3x + \cos 3x + 2\cos x = 0.$

b. (ĐHY Hà Nội – 1999): $4{\sin ^3}x – \sin x – \cos x = 0.$

<!-- chunk:17 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 5. Tìm tất cả các nghiệm $x \in \left[ {0,\frac{\pi }{4}} \right]$ của các phương trình:

a. $\sin x\left( {2{{\sin }^2}x – {{\cos }^2}x} \right)\left( {8{{\sin }^4}x – 8{{\sin }^2}x{{\cos }^2}x + {{\cos }^4}x} \right)$ $= 0.$

b. $64{\sin ^6}x – 96{\sin ^4}x{\cos ^2}x$ $+ 36{\sin ^2}x{\cos ^4}x – 3{\cos ^6}x = 0.$

<!-- chunk:18 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 6. Cho phương trình:

${\sin ^3}x – 3(m + 1){\sin ^2}x\cos x$ $+ 2\left( {{m^2} + 4m + 1} \right)\sin x{\cos ^2}x$ $– 4m(m + 1){\cos ^3}x = 0.$

a. Giải phương trình với $m =-1.$

b. Xác định $m$ để phương trình có ba nghiệm phân biệt thuộc $\left( {\frac{\pi }{4},\frac{\pi }{2}} \right).$

<!-- chunk:19 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 7. Cho phương trình:

${\sin ^3}x – 3{\sin ^2}x\cos x$ $+ 2(m – 1)\sin x{\cos ^2}x$ $+ (m – 3){\cos ^3}x = 0.$

a. Giải phương trình với $m = 1.$

b. Xác định $m$ để phương trình có ba nghiệm ${x_1}$, ${x_2}$, ${x_3}$ thoả mãn:

$– \frac{\pi }{2} < {x_1} < – \frac{\pi }{4} < {x_2} < {x_3} < \frac{\pi }{2}.$

<!-- chunk:20 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 8. Cho phương trình:

$2(2 – 3m){\sin ^3}x$ $+ 3(2m – 1)\sin x$ $+ 2(m – 2){\sin ^2}x\cos x$ $– (4m – 3)\cos x = 0.$

a. Giải phương trình khi $m = 2.$

b. Tìm $m$ để $\left[ {0,\frac{\pi }{4}} \right]$ chứa đúng $1$ nghiệm của phương trình.

<!-- chunk:21 level:4 source:https://toanmath.com/2019/08/phuong-trinh-thuan-nhat-bac-ba-doi-voi-sinx-va-cosx.html -->
## Bài tập 9. Xác định $m \ne 0$ để phương trình:

${m^2}{\sin ^3}x$ $– 3m{\sin ^2}x\cos x$ $+ \left( {{m^2} + 2} \right)\sin x{\cos ^2}x$ $– m{\cos ^3}x = 0$ có đúng ba nghiệm $x \in \left( { – \frac{\pi }{2},\frac{\pi }{2}} \right).$