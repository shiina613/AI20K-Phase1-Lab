# Phương trình đối xứng đối với tanx và cotx

<!-- chunk:0 level:0 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
Bài viết hướng dẫn phương pháp giải và biện luận phương trình đối xứng đối với tanx và cotx.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài toán 1: Giải phương trình: $a\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ b(\tan x + \cot x) + c = 0$ $(1).$

PHƯƠNG PHÁP CHUNG:

Ta thực hiện theo các bước sau:

Bước 1: Đặt điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Bước 2: Đặt $\tan x + \cot x = t$, điều kiện $|t| \ge 2$ $\Rightarrow {\tan ^2}x + {\cot ^2}x = {t^2} – 2.$

Khi đó phương trình có dạng:

$a\left( {{t^2} – 2} \right) + bt + c = 0$ $\Leftrightarrow a{t^2} + bt + c – 2a = 0$ $(2).$

Bước 3: Giải phương trình $(2)$ theo $t$ và chọn nghiệm ${t_0}$ thoả mãn điều kiện $|t| \ge 2.$

Bước 4: Với $t = {t_0}$ $\Leftrightarrow \tan x + \cot x = {t_0}$, khi đó ta có thể lựa chọn một trong hai hướng biến đổi sau:

+ Hướng 1: Ta có:

$\tan x + \frac{1}{{\tan x}} = {t_0}$ $\Leftrightarrow {\tan ^2}x – {t_0}\tan x + 1 = 0.$

Đây là phương trình bậc hai theo $\tan x.$

+ Hướng 2: Ta có:

$\frac{{\sin x}}{{\cos x}} + \frac{{\cos x}}{{\sin x}} = {t_0}$ $\Leftrightarrow \frac{{{{\sin }^2}x + {{\cos }^2}x}}{{\sin x\cos x}} = {t_0}$ $\Leftrightarrow \sin 2x = \frac{1}{{2{t_0}}}.$

Đây là phương trình cơ bản của sin.

Chú ý: Cũng có thể lựa chọn phép đổi biến $t = \tan x$, tuy nhiên khi đó ta sẽ thu được một phương trình bậc cao.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Ví dụ 1: Giải phương trình:

$(\tan x + 7)\tan x$ $+ (\cot x + 7)\cot x + 14 = 0.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Biến đổi phương trình về dạng:

$\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ 7(\tan x + \cot x) + 14 = 0.$

Đặt $\tan x + \cot x = t$, điều kiện $|t| \ge 2$, suy ra ${\tan ^2}x + {\cot ^2}x = {t^2} – 2.$

Khi đó phương trình có dạng:

${t^2} – 2 + 7t + 14 = 0$ $\Leftrightarrow {t^2} + 7t + 12 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 3}\\
{t = – 4}
\end{array}} \right..
$$

+ Với $t=-3$ ta được:

$\tan x + \cot x = – 3$ $\Leftrightarrow \tan x + \frac{1}{{\tan x}} = – 3$ $\Leftrightarrow {\tan ^2}x + 3\tan x + 1 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = \frac{{ – 3 – \sqrt 5 }}{2} = \tan \alpha }\\
{\tan x = \frac{{ – 3 + \sqrt 5 }}{2} = \tan \beta }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \beta + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

+ Với $t = – 4$ ta được:

$\tan x + \cot x = – 4$ $\Leftrightarrow \frac{{\sin x}}{{\cos x}} + \frac{{\cos x}}{{\sin x}} = – 4$ $\Leftrightarrow \frac{{{{\sin }^2}x + {{\cos }^2}x}}{{\sin x\cos x}} = – 4.$

$\Leftrightarrow \sin 2x = – \frac{1}{2}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x = – \frac{\pi }{6} + 2k\pi }\\
{2x = \frac{{7\pi }}{6} + 2k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – \frac{\pi }{{12}} + k\pi }\\
{x = \frac{{7\pi }}{{12}} + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có bốn họ nghiệm.

Nhận xét: Qua việc lựa chọn hai phương pháp giải để tìm ra nghiệm $x$ khi biết ${t_0}$ các em hãy lựa chọn cho mình một phương pháp phù hợp.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Ví dụ 2: Cho phương trình:

${\tan ^2}x + {\cot ^2}x$ $+ m(\tan x + \cot x) + 2m = 0$ $(1).$

a. Giải phương trình với $m = – \frac{1}{2}.$

b. Tìm $m$ để phương trình có nghiệm.

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Đặt $\tan x + \cot x = t$ với $|t| \ge 2$, suy ra ${\tan ^2}x + {\cot ^2}x = {t^2} – 2.$

Khi đó phương trình có dạng:

${t^2} – 2 + mt + 2m = 0$ $\Leftrightarrow f(t) = {t^2} + mt + 2m – 2 = 0$ $(2).$

a. Với $m = – \frac{1}{2}$ ta được:

${t^2} – \frac{1}{2}t – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2}\\
{t = – 3/2\:{\rm{(loại)}}}
\end{array}} \right.
$$
 $\Leftrightarrow \tan x + \cot x = 2.$

$\Leftrightarrow \tan x = 1$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy với $m = – \frac{1}{2}$ phương trình có một họ nghiệm.

b. Để tìm $m$ sao cho phương trình có nghiệm ta lựa chọn một trong hai cách sau:

Cách 1: Phương trình $(1)$ có nghiệm $\Leftrightarrow$ phương trình $(2)$ có nghiệm $|t| \ge 2.$

Xét bài toán ngược: “Tìm điều kiện để phương trình đã cho vô nghiệm”.

Phương trình đã cho vô nghiệm:

$$
\Leftrightarrow \left[ \begin{array}{l}
(2){\rm{\:vô\:nghiệm}}\\
(2){\rm{\:có\:hai\:nghiệm\:thuộc\:}}( – 2,2)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\Delta < 0}\\
{\left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{af( – 2) > 0}\\
{af(2) > 0}\\
{ – 2 < \frac{S}{2} < 2}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ \begin{array}{l}
{m^2} – 8m – 8 < 0\\
\left\{ {\begin{array}{l}
{{m^2} – 8m – 8 \ge 0}\\
{2 > 0}\\
{4m + 2 > 0}\\
{ – 2 < – \frac{m}{2} < 2}
\end{array}} \right.
\end{array} \right..
$$

$\Leftrightarrow – \frac{1}{2} < m < 4 + 2\sqrt 2 .$

Vậy với $m \le – \frac{1}{2}$ hoặc $m \ge 4 + 2\sqrt 2$ phương trình đã cho có nghiệm.

Cách 2: Vì $t = – 2$ không phải là nghiệm của phương trình, nên viết lại $(2)$ dưới dạng:

$\frac{{ – {t^2} + 2}}{{t + 2}} = m.$

Vậy phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = m$ cắt phần đồ thị hàm số $y = \frac{{ – {t^2} + 2}}{{t + 2}}$ trên $( – \infty , – 2] \cup [2, + \infty ).$

Xét hàm số $y = \frac{{ – {t^2} + 2}}{{t + 2}}$ trên $(-\infty,-2] \cup[2,+\infty)$

Đạo hàm:

$y’ = \frac{{ – {t^2} – 4t – 2}}{{{{(t + 2)}^2}}}.$

$y’ = 0$ $\Leftrightarrow – {t^2} – 4t – 2 = 0$ $\Leftrightarrow t = – 2 \pm \sqrt 2 .$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx-1.png" alt="">

Dựa vào bảng biến thiên, ta được điều kiện là: $m \le – \frac{1}{2}$ hoặc $m \ge 4 + 2\sqrt 2 .$

Chú ý: Phương pháp được mở rộng tự nhiên cho các phương trình đối xứng bậc cao hơn $2.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Ví dụ 3: Cho phương trình:

$2\tan x + {\tan ^2}x + {\tan ^3}x$ $+ 2\cot x + {\cot ^2}x + {\cot ^3}x = m$ $(1).$

a. Giải phương trình với $m = 8.$

b. Tìm $m$ để phương trình có nghiệm.

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Đặt $\tan x + \cot x = t$, điều kiện $|t| \ge 2$, suy ra:

${\tan ^2}x + {\cot ^2}x = {t^2} – 2.$

${\tan ^3}x + {\cot ^3}x$ $= {(\tan x + \cot x)^3}$ $– 3\tan x\cot x(\tan x + \cot x)$ $= {t^3} – 3t.$

Khi đó phương trình có dạng:

$2t + {t^2} – 2 + {t^3} – 3t = m$ $\Leftrightarrow {t^3} + {t^2} – t – 2 = m$ $(2).$

a. Với $m = 8$ ta được:

${t^3} + {t^2} – t – 10 = 0$ $\Leftrightarrow (t – 2)\left( {{t^2} + 3t + 5} \right) = 0$ $\Leftrightarrow t = 2$ $\Leftrightarrow \tan x + \cot x = 2.$

$\Leftrightarrow \tan x = 1$ $\Leftrightarrow x = \frac{\pi }{4} + k\pi$, $k \in Z.$

Vậy với $m = 10$ phương trình có một họ nghiệm.

b. Phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = m$ cắt phần đồ thị hàm số $y = {t^3} + {t^2} – t – 2$ trên $(-\infty,-2] \cup[2,+\infty)$

Xét hàm số $y = {t^3} + {t^2} – t – 2$ trên $D = ( – \infty , – 2] \cup [2, + \infty ).$

Đạo hàm:

$y’ = 3{t^2} + 2t – 1 > 0$, $\forall t \in D$ $\Leftrightarrow$ hàm số đồng biến trên $D.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx-2.png" alt="">

Dựa vào bảng biến thiên ta được điều kiện là $m \le – 4$ hoặc $m \ge 8.$

<!-- chunk:5 level:2 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài toán 2: Giải phương trình: $a\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ b(\tan x – \cot x) + c = 0$ $(1).$

PHƯƠNG PHÁP CHUNG:

Ta thực hiện theo các bước sau:

Bước 1: Đặt điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Bước 2: Đặt $\tan x – \cot x = t$ $\Rightarrow {\tan ^2}x + {\cot ^2}x = {t^2} + 2.$

Khi đó phương trình có dạng:

$a\left( {{t^2} + 2} \right) + bt + c = 0$ $\Leftrightarrow a{t^2} + bt + c + 2a = 0$ $(2).$

Bước 3: Giải phương trình $(2)$ theo $t.$

Bước 4: Với $t = {t_0}$ $\Leftrightarrow \tan x – \cot x = {t_0}$, khi đó ta có thể lựa chọn một trong hai hướng biến đổi sau:

+ Hướng 1: Ta có:

$\tan x – \frac{1}{{\tan x}} = {t_0}$ $\Leftrightarrow {\tan ^2}x – {t_0}\tan x – 1 = 0.$

Đây là phương trình bậc hai theo $\tan x.$

+ Hướng 2: Ta có:

$\frac{{\sin x}}{{\cos x}} – \frac{{\cos x}}{{\sin x}} = {t_0}$ $\Leftrightarrow \frac{{{{\sin }^2}x – {{\cos }^2}x}}{{\sin x\cos x}} = {t_0}$ $\Leftrightarrow \frac{{ – 2\cos 2x}}{{\sin 2x}} = {t_0}$ $\Leftrightarrow \cot 2x = – \frac{{{t_0}}}{2}.$

Đây là phương trình cơ bản của cotan.

Chú ý: Cũng có thể lựa chọn phép đổi biến $t = \tan x$, tuy nhiên khi đó ta sẽ thu được một phương trình bậc cao.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Ví dụ 4: Giải phương trình:

$\sqrt 3 \left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ 2(\sqrt 3 – 1)(\tan x – \cot x)$ $– 4 – 2\sqrt 3 = 0.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Đặt $\tan x – \cot x = t$, suy ra ${\tan ^2}x + {\cot ^2}x = {t^2} + 2.$

Khi đó phương trình có dạng:

$\sqrt 3 \left( {{t^2} + 2} \right) + 2(\sqrt 3 – 1)t – 4 – 2\sqrt 3 = 0$ $\Leftrightarrow \sqrt 3 {t^2} + 2(\sqrt 3 – 1)t – 4 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 2}\\
{t = 2/\sqrt 3 }
\end{array}} \right..
$$

+ Với $t = \frac{2}{{\sqrt 3 }}$ ta được:

$\tan x – \cot x = \frac{2}{{\sqrt 3 }}$ $\Leftrightarrow \frac{{\sin x}}{{\cos x}} – \frac{{\cos x}}{{\sin x}} = \frac{2}{{\sqrt 3 }}$ $\Leftrightarrow \frac{{{{\sin }^2}x – {{\cos }^2}x}}{{\sin x\cos x}} = \frac{2}{{\sqrt 3 }}.$

$\Leftrightarrow \cot 2x = – \frac{1}{{\sqrt 3 }}$ $\Leftrightarrow 2x = – \frac{\pi }{3} + k\pi$ $\Leftrightarrow x = – \frac{\pi }{6} + \frac{{k\pi }}{2}$, $k \in Z.$

+ Với $t =-2$ ta được:

$\tan x – \cot x = – 2$ $\Leftrightarrow \tan x – \frac{1}{{\tan x}} = – 2$ $\Leftrightarrow {\tan ^2}x + 2\tan x – 1 = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x = – 1 – \sqrt 2 = \tan \alpha }\\
{\tan x = – 1 + \sqrt 2 = \tan \beta }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + k\pi }\\
{x = \beta + k\pi }
\end{array}} \right.
$$
, $k \in Z.$

Vậy phương trình có ba họ nghiệm.

Nhận xét: Qua việc lựa chọn hai phương pháp giải để tìm ra nghiệm $x$ khi biết ${t_0}$, lời khuyên dành cho các em học sinh là hãy lựa chọn hướng 2 để giải, bởi ngay với $t=-2$, ta được:

$\tan x – \cot x = – 2$ $\Leftrightarrow \frac{{\sin x}}{{\cos x}} – \frac{{\cos x}}{{\sin x}} = – 2$ $\Leftrightarrow \frac{{{{\sin }^2}x – {{\cos }^2}x}}{{\sin x\cos x}} = – 2.$

$\Leftrightarrow \cot 2x = 1$ $\Leftrightarrow 2x = \frac{\pi }{4} + k\pi$ $\Leftrightarrow x = \frac{\pi }{8} + \frac{{k\pi }}{2}$, $k \in Z.$

Chú ý: Phương pháp được mở rộng tự nhiên cho các phương trình đối xứng bậc cao hơn $2.$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Ví dụ 5: Cho phương trình:

${\tan ^3}x – {\cot ^3}x$ $– 3\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $– 3(\tan x – \cot x)$ $+ m + 6 = 0$ $(1).$

a. Giải phương trình với $m = 4.$

b. Biện luận theo $m$ số nghiệm thuộc $\left( {0,\frac{\pi }{2}} \right)$ của phương trình.

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Đặt $\tan x – \cot x = t.$

Suy ra:

${\tan ^2}x + {\cot ^2}x = {t^2} + 2.$

${\tan ^3}x – {\cot ^3}x$ $= {(\tan x – \cot x)^3}$ $+ 3\tan x\cot x(\tan x – \cot x)$ $= {t^3} + 3t.$

Khi đó phương trình có dạng:

${t^3} + 3t – 3\left( {{t^2} + 2} \right) – 3t + m + 6 = 0$ $\Leftrightarrow {t^3} – 3{t^2} + m = 0$ $(2).$

a. Với $m = 4$ ta được:

${t^3} – 3{t^2} + 4 = 0$ $\Leftrightarrow (t + 1)\left( {{t^2} – 4t + 4} \right) = 0$ $\Leftrightarrow (t + 1){(t – 2)^2} = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x – \cot x = – 1}\\
{\tan x – \cot x = 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cot 2x = \frac{1}{2} = \cot 2\alpha }\\
{\cot 2x = – 1}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{2x = 2\alpha + k\pi }\\
{2x = – \frac{\pi }{4} + k\pi }
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \alpha + \frac{{k\pi }}{2}}\\
{x = – \frac{\pi }{8} + \frac{{k\pi }}{2}}
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = 4$ phương trình có hai họ nghiệm.

b. Với mỗi nghiệm ${t_0}$ của phương trình $(2)$ ta được:

$\tan x – \cot x = {t_0}$ $\Leftrightarrow \cot 2x = – \frac{{{t_0}}}{2}.$

Mặt khác vì $x \in \left( {0,\frac{\pi }{2}} \right)$ $\Leftrightarrow 2x \in (0,\pi ).$

Do đó với mỗi nghiệm ${t_0}$ của $(2)$ ta có được $1$ nghiệm ${x_0} \in \left( {0,\frac{\pi }{2}} \right)$ của $(1).$

Số nghiệm của $(2)$ bằng số giao điểm của đường thẳng $y = -m$ với đồ thị hàm số $y = {t^3} – 3{t^2}.$

Xét hàm số $y = {t^3} – 3{t^2}.$

Đạo hàm:

$y’ = 3{t^2} – 6t.$

$y’ = 0$ $\Leftrightarrow 3{t^2} – 6t = 0$ $\Leftrightarrow t = 0$ hoặc $t = 2.$

Bảng biến thiên:

<img link="data_for_rag/toan11/images/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx-3.png" alt="">

Dựa vào bảng biến thiên, ta có kết luận (bạn đọc tự đưa ra lời kết luận).

<!-- chunk:8 level:1 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## II. CÁC BÀI TOÁN THI

## Bài 1: Cho phương trình:

$\frac{3}{{{{\sin }^2}x}} + 3{\tan ^2}x$ $+ m(\tan x + \cot x) – 1 = 0$ $(1).$

Tìm $m$ để phương trình có nghiệm.

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Biến đổi phương trình về dạng:

$3\left( {1 + {{\cot }^2}x} \right) + 3{\tan ^2}x$ $+ m(\tan x + \cot x) – 1 = 0.$

$\Leftrightarrow 3\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ m(\tan x + \cot x) + 2 = 0.$

Đặt $\tan x + \cot x = t$, điều kiện $|t| \ge 2$, suy ra ${\tan ^2}x + {\cot ^2}x = {t^2} – 2.$

Khi đó phương trình có dạng:

$3\left( {{t^2} – 2} \right) + mt + 2 = 0$ $\Leftrightarrow f(t) = 3{t^2} + mt – 4 = 0$ $(2).$

Để tìm $m$ sao cho phương trình có nghiệm ta lựa chọn một trong hai cách sau:

Cách 1: Ta đi xét bài toán ngược: “Tìm $m$ để phương trình vô nghiệm”.

Phương trình $(1)$ vô nghiệm 
$$
\Leftrightarrow \left[ \begin{array}{l}
(2){\rm{\:vô\:nghiệm\:}}\\
(2){\rm{\:có\:2\:nghiệm\:thuộc\:}}\left( { – 2,2} \right)
\end{array} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\Delta < 0}\\
{\left\{ {\begin{array}{l}
{\Delta \ge 0}\\
{af(2) > 0}\\
{af( – 2) > 0}\\
{ – 2 < S/2 < 2}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow – 4 < m < 4.$

Vậy phương trình có nghiệm khi $m \in R\backslash ( – 4,4).$

Cách 2: Viết lại $(2)$ dưới dạng:

$\frac{{ – 3{t^2} + 4}}{t} = m.$

Vậy phương trình $(1)$ có nghiệm $\Leftrightarrow$ đường thẳng $y = m$ cắt phần đồ thị hàm số $y = \frac{{ – 3{t^2} + 4}}{t}$ trên $D = ( – \infty , – 2] \cup [2, + \infty ).$

Xét hàm số $y = \frac{{ – 3{t^2} + 4}}{t}$ trên $D = ( – \infty , – 2] \cup [2, + \infty ).$

Đạo hàm: $y’ = \frac{{ – 3{t^2} – 4}}{{{t^2}}} < 0$, $\forall t \in D.$ Do đó hàm số nghịch biến trên $D.$

Từ đó ta được điều kiện là:

$$
\left[ {\begin{array}{l}
{m \le y(2)}\\
{m \ge y( – 2)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m \le – 4}\\
{m \ge 4}
\end{array}} \right..
$$

Vậy phương trình có nghiệm khi $|m| \ge 4.$

## Bài 2: Cho phương trình:

${\tan ^3}x – {\cot ^3}x$ $– 3\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $– 12(\tan x – \cot x)$ $+ m + 6 = 0$ $(1).$

a. Giải phương trình với $m = 2.$

b. Tìm $m$ để $(1)$ có $3$ nghiệm phân biệt ${x_1}$, ${x_2}$, ${x_3} \in \left( {0,\frac{\pi }{2}} \right)$ và thoả mãn:

$\frac{{\sin 2\left( {{x_1} – {x_2}} \right)}}{{\sin 2{x_1}}} – \frac{{\sin 2\left( {{x_2} – {x_3}} \right)}}{{\sin 2{x_3}}} = 0.$

Điều kiện:

$$
\left\{ {\begin{array}{l}
{\sin x \ne 0}\\
{\cos x \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow \sin 2x \ne 0$ $\Leftrightarrow x \ne \frac{{k\pi }}{2}$, $k \in Z.$

Đặt $\tan x – \cot x = t$.

Suy ra:

${\tan ^2}x + {\cot ^2}x = {t^2} + 2.$

${\tan ^3}x – {\cot ^3}x$ $= {(\tan x – \cot x)^3}$ $+ 3\tan x\cot x(\tan x – \cot x)$ $= {t^3} + 3t.$

Khi đó phương trình có dạng:

${t^3} + 3t – 3\left( {{t^2} + 2} \right)$ $– 12t + m + 6 = 0$ $\Leftrightarrow {t^3} – 3{t^2} – 9t + m = 0$ $(2).$

a. Với $m = 2$ ta được:

${t^3} – 3{t^2} – 9t + 2 = 0$ $\Leftrightarrow (t + 2)\left( {{t^2} – 5t + 1} \right) = 0.$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{{5 \pm \sqrt {21} }}{2}}\\
{t = – 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{\tan x – \cot x = \frac{{5 \pm \sqrt {21} }}{2}}\\
{\tan x – \cot x = – 2}
\end{array}} \right..
$$

$$
\Leftrightarrow \left[ {\begin{array}{l}
{\cot 2x = – \frac{{5 \pm \sqrt {21} }}{2} = \cot 2{\alpha _{1,2}}}\\
{\cot 2x = 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = {\alpha _{1,2}} + \frac{{k\pi }}{2}}\\
{x = \frac{\pi }{8} + \frac{{k\pi }}{2}}
\end{array}} \right.
$$
, $k \in Z.$

Vậy với $m = 2$ phương trình có ba họ nghiệm.

b. Với mỗi nghiệm ${t_0}$ của phương trình $(2)$ ta được:

$\tan x – \cot x = {t_0}$ $\Leftrightarrow \cot 2x = – \frac{{{t_0}}}{2}.$

Mặt khác vì $x \in \left( {0,\frac{\pi }{2}} \right)$ $\Leftrightarrow 2x \in (0,\pi ).$

Do đó với mỗi nghiệm ${t_0}$ của $(2)$ ta có được $1$ nghiệm ${x_0} \in \left( {0,\frac{\pi }{2}} \right)$ của $(1).$

Từ biểu thức điều kiện, ta được:

$\frac{{\sin 2\left( {{x_1} – {x_2}} \right)}}{{\sin 2{x_1}}} = \frac{{\sin 2\left( {{x_2} – {x_3}} \right)}}{{\sin 2{x_3}}}$ $\Leftrightarrow \frac{{\sin 2\left( {{x_1} – {x_2}} \right)}}{{\sin 2{x_1}\sin 2{x_2}}} = \frac{{\sin 2\left( {{x_2} – {x_3}} \right)}}{{\sin 2{x_2}\sin 2{x_3}}}.$

$\Leftrightarrow \cot 2{x_1} – \cot 2{x_2}$ $= \cot 2{x_2} – \cot 2{x_3}$ $\Leftrightarrow \cot 2{x_1} + \cot 2{x_3} = 2\cot 2{x_2}.$

$\Leftrightarrow – \frac{{{t_1}}}{2} – \frac{{{t_3}}}{2} = – 2\frac{{{t_2}}}{2}$ $\Leftrightarrow {t_1} + {t_3} = 2{t_2}.$

$\Leftrightarrow (2)$ có ba nghiệm phân biệt lập thành cấp số cộng.

Để phương trình có ba nghiệm phân biệt với hoành độ lập thành cấp số cộng thì điểm uốn $U(1, – 11)$ của đồ thị hàm số $y = {t^3} – 3{t^2} – 9t$ thuộc đường thẳng $y =-m.$

$\Leftrightarrow – m = – 11$ $\Leftrightarrow m = 11.$

Thử lại: với $m = 11$ phương trình $(2)$ có dạng:

${t^3} – 3{t^2} – 9t + 11 = 0$ $\Leftrightarrow (t – 1)\left( {{t^2} – 2t – 11} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{t_1} = 1 – 2\sqrt 3 }\\
{{t_2} = 1}\\
{{t_3} = 1 + 2\sqrt 3 }
\end{array}} \right.
$$
 (thoả mãn).

Vậy với $m = 11$ thoả mãn điều kiện đầu bài.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 1. Giải các phương trình:

a. $\cot x – \tan x = \sin x – \cos x.$

b. $\tan x + {\tan ^2}x + \cot x + {\cot ^2}x = 6.$

<!-- chunk:10 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 2. Cho phương trình:

$3\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $+ 4(\tan x + \cot x) + m = 0.$

a. (CĐHQ – 2000): Giải phương trình với $m = 2.$

b. Tìm $m$ để phương trình có nghiệm.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 3. Cho phương trình:

$\tan x + {\tan ^2}x + {\tan ^3}x$ $+ \cot x + {\cot ^2}x + {\cot ^3}x = m.$

a. Giải phương trình với $m = 6.$

b. Tìm $m$ để phương trình có nghiệm.

<!-- chunk:12 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 4. Cho phương trình:

$\frac{1}{{{{\cos }^2}x}} + {\cot ^2}x$ $+ m(\tan x + \cot x) + 2 = 0.$

a. Giải phương trình khi $m = \frac{5}{2}.$

b. Xác định $m$ để phương trình có nghiệm.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 5. Với giá trị nào của $m$ thì phương trình sau đây có nghiệm:

$\frac{3}{{{{\sin }^2}x}} + {\tan ^3}x$ $+ m(\tan x + \cot x) – 1 = 0.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/08/phuong-trinh-doi-xung-doi-voi-tanx-va-cotx.html -->
## Bài tập 6. Giải và biện luận phương trình:

$(m – 2)\left( {{{\tan }^2}x + {{\cot }^2}x} \right)$ $– 2m(\tan x – \cot x) – m + 5 = 0.$