# Tìm điều kiện để phương trình f(x) = g(m) có n nghiệm

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm điều kiện để phương trình f(x) = g(m) có n nghiệm trong chương trình Giải tích 12: ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN

Để phương trình $f(x) = g(m)$ có $n$ nghiệm thực chất ta chuyển đổi về bài toán tường giao giữa đồ thị hàm số $y = f(x)$ với đường thẳng $g(m).$

Số giao điểm phân biệt của đồ thị hàm số $y = f(x)$ với đường thẳng $g(m)$ chính là số nghiệm phân biệt của phương trình $f(x) = g(m).$

Xét bài toán: Tìm $m$ để phương trình $f(x;m) = 0$ có nghiệm $x \in D.$

+ Bước 1: Thực hiện cô lập $m$ để đưa về dạng $f(x) = g(m).$

+ Bước 2: Khảo sát và vẽ bảng biến thiên hàm số $f(x)$ trên $D.$

+ Bước 3: Dựa vào bảng biến thiên để kết luận điều kiện cần tìm.

Chú ý:

+ Nếu tồn tại $\mathop {\max }\limits_D f(x)$, $\mathop {\min }\limits_D f(x)$ và yêu cầu bài toán chỉ là tìm $m$ để phương trình $f(x;m) = 0$ có nghiệm thì ta có thể sử dụng luôn điều kiện: Phương trình bài ra có nghiệm khi và chỉ khi $\mathop {\min }\limits_D f(x) \le m \le \mathop {\max }\limits_D f(x).$

+ Nếu bài toán yêu cầu, tìm điều kiện tham số để phương trình $f(x;m) = 0$ có $n$ nghiệm phân biệt thì ta chỉ cần tìm điều kiện tham số để đường thẳng $g(m)$ cắt đồ thị hàm số $y = f(x)$ tại $n$ điểm phân biệt.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 1. Tìm điều kiện của tham số $m$ để phương trình ${x^3} – 2{x^2} + x – m + 5 = 0$ có ba nghiệm phân biệt.

Ta có ${x^3} – 2{x^2} + x – m + 5 = 0$ $\Leftrightarrow {x^3} – 2{x^2} + x + 5 = m.$

Xét hàm số $f(x) = {x^3} – 2{x^2} + x + 5.$

Suy ra $f'(x) = 3{x^2} – 4x + x$, $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1}\\
{x = \frac{1}{3}}
\end{array}} \right..
$$

Ta có bảng biến thiên sau:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-1.png" alt="">

Từ bảng biến thiên suy ra: phương trình bài ra có ba nghiệm phân biệt khi $5 < m < \frac{{139}}{{27}}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 2. Cho phương trình ${x^4} – 2{x^2} – 2 – 3m = 0.$ Tìm giá trị của tham số $m$ để phương trình đã cho có nghiệm.

Ta có: ${x^4} – 2{x^2} – 2 – 3m = 0$ $\Leftrightarrow {x^4} – 2{x^2} – 2 = 3m.$

Xét hàm số $f(x) = {x^4} – 2{x^2} – 2$ có $f'(x) = 4{x^3} – 4x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

Ta có bảng biến thiên sau:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-2.png" alt="">

Từ bảng biến thiên, suy ra phương trình bài ra có nghiệm khi: $3m \ge – 3$ $\Leftrightarrow m \ge – 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 3. Cho phương trình ${x^3} – 3mx + 2 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có nghiệm trên khoảng $\left( {\frac{1}{2};2} \right).$

Ta có ${x^3} – 3mx + 2 = 0$ $\Leftrightarrow {x^3} + 2 = 3mx$ $\Leftrightarrow 3m = {x^2} + \frac{2}{x}.$

Xét hàm số $f(x) = {x^2} + \frac{2}{x}$ trên $\left( {\frac{1}{2};2} \right) \cdot$ Khi đó $f'(x) = 2x – \frac{2}{{{x^2}}} = 0$ $\Leftrightarrow x = 1.$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-3.png" alt="">

Từ bảng biến thiên, ta có phương trình bài ra có nghiệm trên khoảng $\left( {\frac{1}{2};2} \right)$ khi $3 \le 3m < 5$ $\Leftrightarrow 1 \le m < \frac{5}{3}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 4. Cho phương trình ${\sin ^2}x + m\sin x – 2m + 5 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có nghiệm.

Ta có: ${\sin ^2}x + m\sin x – 2m + 5 = 0$ $\Leftrightarrow {\sin ^2}x + 5 = m(2 – \sin x).$

Đặt $t = \sin x.$ Khi đó ta có $– 1 \le \sin x \le 1$ nên $t \in [ – 1;1].$

Do đó ta có phương trình: ${t^2} + 5 = m(2 – t)$ $\Leftrightarrow \frac{{{t^2} + 5}}{{2 – t}} = m.$

Xét hàm số $f(t) = \frac{{{t^2} + 5}}{{2 – t}}$ với $t \in [ – 1;1].$

Khi đó $f'(t) = \frac{{ – {t^2} + 4t + 5}}{{{{(2 – t)}^2}}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 5\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-4.png" alt="">

Từ bảng biến thiên, ta có phương trình bài ra có nghiệm khi $m \in [2;6].$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 5. Cho phương trình $\sin x + \cos x + 2m\sin x\cos x + 4m – 1 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có nghiệm.

Đặt $t = \sin x + \cos x$ $= \sqrt 2 .\sin \left( {x + \frac{\pi }{4}} \right).$ Khi đó ta có $– 1 \le \sin \left( {x + \frac{\pi }{4}} \right) \le 1$ nên $t \in [ – \sqrt 2 ;\sqrt 2 ].$

Khi đó ${t^2} = 1 + 2\sin x\cos x$ $\Leftrightarrow 2\sin x\cos x = {t^2} – 1.$

Do đó ta có phương trình: $t + m\left( {{t^2} – 1} \right) + 4m – 1 = 0$ $\Leftrightarrow \frac{{1 – t}}{{{t^2} + 3}} = m.$

Xét hàm số $f(t) = \frac{{1 – t}}{{{t^2} + 3}}$ với $t \in [ – \sqrt 2 ;\sqrt 2 ].$

Khi đó $f'(t) = \frac{{{t^2} – 2t – 3}}{{{{\left( {{t^2} + 3} \right)}^2}}}$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = – 1}\\
{t = 3\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-5.png" alt="">

Từ bảng biến thiên, ta có phương trình bài ra có nghiệm khi $m \in \left[ {\frac{{1 – \sqrt 2 }}{5};\frac{1}{2}} \right].$

<!-- chunk:7 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 6. Cho phương trình ${x^2} + m(\sqrt {4 – {x^2}} + 1) – 7 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có nghiệm.

Xét phương trình: ${x^2} + m(\sqrt {4 – {x^2}} + 1) – 7 = 0.$

Đặt $t = \sqrt {4 – {x^2}} .$ Điều kiện $0 \le t \le 2.$ Khi đó ${t^2} = 4 – {x^2}$ $\Leftrightarrow {x^2} = 4 – {t^2}.$

Phương trình trở thành: $4 – {t^2} + m(t + 1) – 7 = 0$ $\Leftrightarrow m = \frac{{{t^2} + 3}}{{t + 1}}.$

Xét hàm số $f(t) = \frac{{{t^2} + 3}}{{t + 1}}$ với $t \in [0;2].$

Suy ra $f'(t) = \frac{{{t^2} + 2t – 3}}{{{{(t + 1)}^2}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = – 3\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-6.png" alt="">

Từ bảng biến thiên của hàm số thì để phương trình bài ra có nghiệm thì $2 \le m \le 3.$

<!-- chunk:8 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 7. Cho phương trình $m(\sqrt {x – 1} + \sqrt {4 – x} )$ $+ 2\sqrt { – {x^2} + 5x – 4} – 7 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có nghiệm.

Nhận xét: $– {x^2} + 5x – 4 = (x – 1)(4 – x).$

Đặt $t = \sqrt {x – 1} + \sqrt {4 – x} .$

Xét hàm số $t(x) = \sqrt {x – 1} + \sqrt {4 – x}$ với $x \in [1;4].$

Ta có $t'(x) = \frac{1}{{2\sqrt {x – 1} }} – \frac{1}{{2\sqrt {4 – x} }}$ $= \frac{{\sqrt {4 – x} – \sqrt {x – 1} }}{{2\sqrt {x – 1} .\sqrt {4 – x} }} = 0$ $\Leftrightarrow x = \frac{5}{2}.$

Bảng biến thiên hàm số $t(x):$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-7.png" alt="">

Do đó với $x \in [1;4]$ thì $t \in [\sqrt 3 ;\sqrt 6 ].$

Khi đó ta có $t = \sqrt {x – 1} + \sqrt {4 – x}$ $\Rightarrow {t^2} = 3 – 2\sqrt { – {x^2} + 5x – 4} .$

$\Rightarrow 2\sqrt { – {x^2} + 5x – 4} = 3 – {t^2}.$

Phương trình ban đầu trở thành: $mt + 3 – {t^2} – 7 = 0$ $\Leftrightarrow m = t + \frac{4}{t}.$

Xét hàm số $f(t) = t + \frac{4}{t}$ với $t \in [\sqrt 3 ;\sqrt 6 ].$

Suy ra $f'(t) = 1 – \frac{4}{{{t^2}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 2}\\
{t = – 2\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-8.png" alt="">

Từ bảng biến thiên của hàm số thì để phương trình bài ra có nghiệm thì $4 \le m \le \frac{{10}}{{\sqrt 6 }}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 8. Cho phương trình $2{x^3} – 3{x^2} + 2m – 1 = 0.$ Tìm tất cả các giá trị của $m$ để phương trình đã cho có ba nghiệm phân biệt trên đoạn $[-2;4].$

Ta có $2{x^3} – 3{x^2} + 2m – 1 = 0$ $\Leftrightarrow 2m = – 2{x^3} + 3{x^2} + 1.$

Xét hàm số $f(x) = – 2{x^3} + 3{x^2} + 1$ trên đoạn $[ – 2;4].$

Khi đó $f'(x) = – 6{x^2} + 6x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 1}
\end{array}} \right..
$$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-9.png" alt="">

Từ bảng biến thiên, ta có phương trình bài ra có ba nghiệm phân biệt khi $1 < 2m < 2$ $\Leftrightarrow \frac{1}{2} < m < 1.$

<!-- chunk:10 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 9. Cho phương trình $4{\sin ^2}x – (m + 4)\sin x – 2m + 1 = 0.$ Tìm điều kiện của tham số $m$ để phương trình đã cho có đúng bốn nghiệm phân biệt trên đoạn $[0;\pi ].$

Đặt $t = \sin x.$ Xét hàm số $t(x) = \sin x$ với $x \in [0;\pi ].$

Khi đó $t’ = \cos x$, $t’ = 0$ $\Leftrightarrow x = \frac{\pi }{2}.$

Ta có bảng biến thiên hàm số $t(x):$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-10.png" alt="">

Từ bảng biến thiên, ta thấy với $x \in [0;\pi ]$ thì $t \in [0;1].$ Và mỗi $t \in [0;1)$ thì cho ta hai nghiệm $x \in [0;\pi ].$

Phương trình bài ra trở thành:

${t^2} – (m + 4)t – 2m + 1 = 0$ $\Leftrightarrow 4{t^2} – 4t + 1 = m(2 + t)$ $\Leftrightarrow \frac{{4{t^2} – 4t + 1}}{{t + 2}} = m.$

Xét hàm số $f(t) = \frac{{4{t^2} – 4t + 1}}{{t + 2}}$ với $t \in [0;1].$

Suy ra: $f'(t) = \frac{{(2t – 1)(2t + 9)}}{{{{(t + 2)}^2}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{1}{2}}\\
{t = – \frac{9}{2}\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-11.png" alt="">

Từ bảng biến thiên ta có, phương trình bài ra có bốn nghiệm phân biệt khi phương trình $f(t) = m$ có hai nghiệm phân biệt $t \in [0;1).$ Do đó $0 < m < \frac{1}{3}.$

<!-- chunk:11 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## Ví dụ 10. Cho phương trình $– {m^3}{x^6} + {x^3} + 3(1 – m){x^2} + 6x + 4 = 0.$ Tìm các giá trị của tham số $m$ để phương trình đã cho có đúng hai nghiệm phân biệt trên đoạn $[-3;-1].$

Ta có $– {m^3}{x^6} + {x^3} + 3(1 – m){x^2} + 6x + 4 = 0$ $\Leftrightarrow {x^3} + 3{x^2} + 6x + 4 = {m^3}{x^6} + 3m{x^2}.$

$\Leftrightarrow {(x + 1)^3} + 3(x + 1) = {\left( {m{x^2}} \right)^3} + 3m{x^2}$ $(1).$

Xét hàm số đặc trưng cho phương trình: $f(t) = {t^3} + 3t$ với $t \in R.$

Ta có $f'(t) = 3{t^2} + 3 > 0$, $\forall t \in R.$

Do đó hàm số $f(t)$ liên tục và đồng biến trên $R.$

Từ phương trình $(1)$, ta có: $f(x + 1) = f\left( {m{x^2}} \right)$ $\Rightarrow x + 1 = m{x^2}$ $\Leftrightarrow m = \frac{{x + 1}}{{{x^2}}}.$

Xét hàm số $g(x) = \frac{{x + 1}}{{{x^2}}}$ với $[ – 3; – 1].$

Ta có $g'(x) = \frac{{ – {x^2} – 2x}}{{{x^4}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0\:\:{\rm{(loại)}}}\\
{x = – 2}
\end{array}} \right..
$$

Bảng biến thiên của hàm số $g(x):$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-12.png" alt="">

Từ bảng biến thiên suy ra phương trình bài ra có đúng hai nghiệm phân biệt trên $[-3;-1]$ khi $m \in \left[ { – \frac{1}{4}; – \frac{2}{9}} \right].$

<!-- chunk:12 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Cho phương trình ${x^3} – {x^2} – 5x – m + 1 = 0.$ Tìm điều kiện của tham số $m$ để phương trình bài ra có $3$ nghiệm phân biệt.

A. $m \in ( – 8; – 6).$

B. $m \in \left( { – 6;\frac{{ – 148}}{{27}}} \right).$

C. $m \in \left( {\frac{{ – 148}}{{27}};4} \right).$

D. $m \in (4;5).$

Ta có ${x^3} – {x^2} – 5x – m + 1 = 0$ $\Leftrightarrow m = {x^3} – {x^2} – 5x + 1.$

Xét hàm số $f(x) = {x^3} – {x^2} – 5x + 1.$

Suy ra: $f'(x) = 3{x^2} – 2x – 5 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = \frac{5}{3}}
\end{array}} \right..
$$

Ta có bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-13.png" alt="">

Từ bảng biến thiên của hàm số, ta thấy phương trình bài ra có ba nghiệm phân biệt khi $\frac{{ – 148}}{{27}} < m < 4.$

> **Đáp án: C**

## Bài 2. Cho phương trình $\frac{1}{4}{x^4} – 2{x^2} + m – \frac{5}{4} = 0.$ Tìm tất cả các giá trị của tham số $m$ để phương trình bài ra có $4$ nghiệm phân biệt.

A. $\left( { – 3; – \frac{5}{4}} \right].$

B. $\left( { – \frac{5}{4}; + \infty } \right).$

C. $( – 4; – 3).$

D. $\left( {\frac{5}{4};3} \right).$

Ta có $\frac{1}{4}{x^4} – 2{x^2} + m – \frac{5}{4} = 0$ $\Leftrightarrow \frac{1}{4}{x^4} – 2{x^2} – \frac{5}{4} = – m.$

Xét hàm số $f(x) = \frac{1}{4}{x^4} – 2{x^2} – \frac{5}{4}.$

Suy ra $f'(x) = {x^3} – 4x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-14.png" alt="">

Từ bảng biến thiên của hàm số ta thấy phương trình bài ra có $4$ nghiệm phân biệt khi $– m \in \left( { – 3; – \frac{5}{4}} \right)$ $\Leftrightarrow m \in \left( {\frac{5}{4};3} \right).$

Chú ý: Bài toán này ta có thể đặt ẩn phụ $t = {x^2}$ đưa về biện luận dạng phương trình bậc hai: $\frac{1}{4}{t^2} – 2t + m – \frac{5}{4} = 0$ có hai nghiệm dương phân biệt thì kết quả đáp số thu được vẫn giống như trên.

> **Đáp án: D**

## Bài 3. Tìm tất cả điều kiện của tham số $m$ để phương trình $x + 3 = m\sqrt {{x^2} + 1}$ có hai nghiệm phân biệt.

A. $( – 2; – 1).$

B. $(1;\sqrt {10} ).$

C. $( – 1;1).$

D. $(3;5).$

Ta có $x + 3 = m\sqrt {{x^2} + 1}$ $\Leftrightarrow m = \frac{{x + 3}}{{\sqrt {{x^2} + 1} }}.$

Xét hàm số $f(x) = \frac{{x + 3}}{{\sqrt {{x^2} + 1} }}.$

Suy ra: $f'(x) = \frac{{1 – 3x}}{{\left( {{x^2} + 1} \right)\sqrt {{x^2} + 1} }} = 0$ $\Leftrightarrow x = \frac{1}{3}.$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-15.png" alt="">

Từ bảng biến thiên, ta có phương trình bài ra có hai nghiệm phân biệt khi $m \in (1;\sqrt {10} ).$

> **Đáp án: B**

## Bài 4. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $2{\sin ^2}x – (m + 3)\sin x + 2m – 1 = 0$ có nghiệm.

A. $4.$

B. $3.$

C. $2.$

D. $6.$

Đặt $t = \sin x$ với $t \in [ – 1;1].$

Ta có phương trình:

$2{t^2} – (m + 3)t + 2m – 1 = 0$ $\Leftrightarrow 2{t^2} – 3t – 1 = m(t – 2)$ $\Leftrightarrow \frac{{2{t^2} – 3t – 1}}{{t – 2}} = m.$

Xét hàm số $f(t) = \frac{{2{t^2} – 3t – 1}}{{t – 2}}$ với $t \in [ – 1;1].$

Suy ra: $f'(t) = \frac{{2{t^2} – 8t + 7}}{{{{(t – 2)}^2}}} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = \frac{{4 + \sqrt 2 }}{2}\:\:{\rm{(loại)}}}\\
{t = \frac{{4 – \sqrt 2 }}{2}\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-16.png" alt="">

Từ bảng biến thiên, suy ra phương trình có nghiệm khi $m \in \left[ { – \frac{4}{3};2} \right].$ Do đó có các giá trị nguyên của $m$ là: $-1$, $0$, $1$, $2.$ Có bốn giá trị thỏa mãn đề bài.

> **Đáp án: A**

## Bài 5. Tính tổng tất cả các giá trị nguyên của tham số $m$ để phương trình $m(\sqrt {x – 1} + \sqrt {2 – x} )$ $+ 2\sqrt { – {x^2} + 3x – 2} – 5 = 0$ có nghiệm.

A. $3.$

B. $12.$

C. $9.$

D. $7.$

Đặt $t = \sqrt {x – 1} + \sqrt {2 – x} .$

Xét hàm số $t(x) = \sqrt {x – 1} + \sqrt {2 – x}$ với $x \in [1;2].$

Ta có $t'(x) = \frac{1}{{2\sqrt {x – 1} }} – \frac{1}{{2\sqrt {2 – x} }}$, $t'(x) = 0$ $\Leftrightarrow x = \frac{3}{2}.$

Bảng biến thiên của hàm số $t(x):$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-17.png" alt="">

Từ bảng biến thiên của hàm số $t(x)$ ta có $t \in [1;\sqrt 2 ].$

Khi đó $t = \sqrt {x – 1} + \sqrt {2 – x}$ $\Rightarrow {t^2} = 1 + 2\sqrt { – {x^2} + 3x – 2}$ $\Leftrightarrow 2\sqrt { – {x^2} + 3x – 2} = {t^2} – 1.$

Phương trình trở thành: $mt + {t^2} – 1 – 5 = 0$ $\Leftrightarrow m = – t + \frac{6}{t}$ $(1).$

Xét hàm số $f(t) = – t + \frac{6}{t}$ với $t \in [1;\sqrt 2 ].$ Ta có $f'(t) = – 1 – \frac{6}{{{t^2}}} < 0$, $\forall t \in [1;\sqrt 2 ].$

Phương trình $(1)$ có nghiệm khi:

$\mathop {\min }\limits_{_{[1;\sqrt 2 ]}} f(t) \le m \le \mathop {\max }\limits_{_{[1;\sqrt 2 ]}} f(t)$ $\Leftrightarrow f(\sqrt 2 ) \le m \le f(1)$ $\Leftrightarrow 2\sqrt 2 \le m \le 5.$

Mà $m \in Z$ $\Rightarrow m \in \{ 3;4;5\} .$

Vậy tổng các giá trị $m$ nguyên cần tìm là $S = 3+4+5=12.$

> **Đáp án: B**

## Bài 6. Biết tất cả các giá trị của tham số $m$ để phương trình $2x + 2 = \sqrt {{x^2} + 2x + m}$ có nghiệm có dạng $S = [a; + \infty ).$ Hỏi giá trị $a$ thuộc khoảng nào sau đây?

A. $\left( {\frac{{ – 3}}{2};\frac{1}{2}} \right).$

B. $\left( {\frac{3}{2};\frac{5}{2}} \right).$

C. $\left( {\frac{5}{2};\frac{7}{2}} \right).$

D. $\left( {\frac{1}{2};\frac{3}{2}} \right).$

Ta có $2x + 2 = \sqrt {{x^2} + 2x + m}$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{{(2x + 2)}^2} = {x^2} + 2x + m\:\:(1)}\\
{x \ge – 1}
\end{array}} \right..
$$

Khi đó ta có $(1) \Leftrightarrow m = 3{x^2} + 6x + 4.$

Xét hàm số $f(x) = 3{x^2} + 6x + 4$ với $x \ge – 1.$

Suy ra: $f'(x) = 6x + 6 \ge 0$, $\forall x \in [ – 1; + \infty ).$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-18.png" alt="">

Từ bảng biến thiên của hàm số, suy ra phương trình bài ra có nghiệm khi $m \in [1; + \infty ).$ Do đó $a = 1 \in \left( {\frac{1}{2};\frac{3}{2}} \right).$

> **Đáp án: D**

## Bài 7. Biết tất cả các giá trị của tham số $m$ để phương trình ${x^4} – 4{x^3} + 4{x^2} – m + 5 = 0$ có đúng $4$ nghiệm phân biệttrên đoạn $[-2;3]$ là $S = (a;b).$ Tính tổng $T = a+b.$

A. $T = 74.$

B. $T = 19.$

C. $T =11.$

D. $T =20.$

Ta có ${x^4} – 4{x^3} + 4{x^2} – m + 5 = 0$ $\Leftrightarrow {x^4} – 4{x^3} + 4{x^2} + 5 = m.$

Xét hàm số $f(x) = {x^4} – 4{x^3} + 4{x^2} + 5$ với $x \in [ – 2;3].$

Ta có $f'(x) = 4{x^3} – 12{x^2} + 8x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 1}\\
{x = 2}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-19.png" alt="">

Từ bảng biến thiên, suy ra phương trình bài ra có đúng bốn nghiệm phân biệt khi $m \in (5;6).$ Do đó $T = 5 + 6 = 11.$

> **Đáp án: C**

## Bài 8. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $x + 2\sqrt {1 – {x^2}} = m$ có hai nghiệm phân biệt.

A. $0.$

B. $2.$

C. $1.$

D. $3.$

Ta có $x + 2\sqrt {1 – {x^2}} = m$, điều kiện $x \in [ – 1;1].$

Xét hàm số $f(x) = x + 2\sqrt {1 – {x^2}}$ với $x \in [ – 1;1].$ Suy ra: $f'(x) = 1 – \frac{{2x}}{{\sqrt {1 – {x^2}} }}.$

Khi đó: $f'(x) = 0$ $\Leftrightarrow \sqrt {1 – {x^2}} = 2x$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \ge 0}\\
{1 – {x^2} = 4{x^2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = \frac{1}{{\sqrt 5 }}.$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-20.png" alt="">

Từ bảng biến thiên của hàm số, suy ra phương trình bài ra có hai nghiệm phân biệt khi $m \in (1;\sqrt 5 ).$ Mà $m \in Z$ $\Rightarrow m = 2.$

> **Đáp án: C**

## Bài 9. Tìm tất cả các giá trị của tham số $m$ để phương trình ${x^6} + 6{x^4} – {m^3}{x^3}$ $+ \left( {15 – 3{m^2}} \right){x^2} – 6mx + 10 = 0$ có đúng hai nghiệm phân biệt thuộc $\left[ {\frac{1}{2};2} \right].$

A. $\frac{7}{5} \le m < 3.$

B. $0 < m < \frac{9}{4}.$

C. $2 < m \le \frac{5}{2}.$

D. $\frac{{11}}{5} < m < 4.$

Ta có ${x^6} + 6{x^4} – {m^3}{x^3}$ $+ \left( {15 – 3{m^2}} \right){x^2} – 6mx + 10 = 0.$

$\Leftrightarrow {\left( {{x^2} + 2} \right)^3} + 3\left( {{x^2} + 2} \right)$ $= {(mx + 1)^3} + 3(mx + 1)$ $(1).$

Xét hàm số đặc trưng cho phương trình: $f(t) = {t^3} + 3t.$

Ta có $f'(t) = 3{t^2} + 3 > 0$, $\forall t \in R$ nên hàm số $f(t)$ liên tục và đồng biến trên $R.$

$(1) \Leftrightarrow f\left( {{x^2} + 2} \right) = f(mx + 1)$ $\Leftrightarrow {x^2} + 2 = mx + 1$ $\Leftrightarrow {x^2} – mx + 1 = 0$ $\Leftrightarrow m = \frac{{{x^2} + 1}}{x}.$

Xét hàm số $g(x) = \frac{{{x^2} + 1}}{x}$ trên $\left[ {\frac{1}{2};2} \right].$ Ta có $g'(x) = 1 – \frac{1}{{{x^2}}}$ $\Rightarrow g'(x) = 0$ $\Leftrightarrow x = 1.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-21.png" alt="">

Dựa vào bảng biến thiên suy ra phương trình đã cho có đúng hai nghiệm phân biệt thuộc $\left[ {\frac{1}{2};2} \right]$ khi và chỉ khi $2 < m \le \frac{5}{2}.$

> **Đáp án: C**

## Bài 10. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $\sqrt[3]{{m + 3\sqrt[3]{{m + 3\sin x}}}} = \sin x$ có nghiệm thực?

A. $5.$

B. $2.$

C. $4.$

D. $3.$

Ta có $\sqrt[3]{{m + 3\sqrt[3]{{m + 3\sin x}}}} = \sin x$ $\Leftrightarrow m + 3\sqrt[3]{{m + 3\sin x}} = {\sin ^3}x.$

$\Leftrightarrow (m + 3\sin x) + 3\sqrt[3]{{m + 3\sin x}}$ $= {\sin ^3}x + 3\sin x$ $(1).$

Xét hàm số đặc trưng cho phương trình $(1)$, ta có:

$f(t) = {t^3} + 3t$ với $t \in R$, $f'(t) = 3{t^2} + 3 > 0$ với mọi $t \in R.$

Do đó hàm số $f(t)$ liên tục và đồng biến trên $R.$

Ta có $(1) \Leftrightarrow f(\sqrt[3]{{m + 3\sin x}}) = f(\sin x)$ $\Leftrightarrow \sqrt[3]{{m + 3\sin x}} = \sin x.$

$\Leftrightarrow m + 3\sin x = {\sin ^3}x$ $\Leftrightarrow m = {\sin ^3}x – 3\sin x.$

Đặt $u = \sin x$, ta có $g(u) = {u^3} – 3u$, với $u \in [ – 1;1].$

$g'(u) = 3{u^2} – 3 = 0$ $\Leftrightarrow u = \pm 1.$

Khi đó: $g(1) = – 2$, $g( – 1) = 2.$

Phương trình bài ra có nghiệm khi $\mathop {\min }\limits_{_{[ – 1;1]}} g(u) \le m \le \mathop {\max }\limits_{_{[ – 1;1]}} g(u)$ $\Leftrightarrow – 2 \le m \le 2.$

Mà $m \in Z$ $\Rightarrow m \in \{ – 2; – 1;0;1;2\} .$

Vậy có $5$ giá trị nguyên cần tìm.

> **Đáp án: A**

<!-- chunk:13 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Tìm điều kiện của tham số $m$ để phương trình ${x^4} – 2{x^2} – 3m + 1 = 0$ có đúng ba nghiệm phân biệt.

A. $m = \frac{1}{3}.$

B. $m \in (1;3).$

C. $m \in ( – 2;0).$

D. $m = 1.$

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để phương trình ${x^3} – 3x + m – 4 = 0$ có nghiệm $x \in [0;3].$

A. $[ – 6;14].$

B. $[ – 14;6].$

C. $[ – 6; – 4].$

D. $[ – 4; + \infty ).$

## Bài 3. Tìm tất cả các giá trị của tham số $m$ để phương trình ${x^3} + 3{x^2} – m + 3 = 0$ có nghiệm $x \in [ – 3; – 1].$

A. $[3;5].$

B. $[3;7].$

C. $(3; + \infty ).$

D. $[5;7].$

## Bài 4. Biết tập tất cả các giá trị thực của tham số $m$ để phương trình ${x^4} – 2{x^2} + 5 – 2m = 0$ có bốn nghiệm phân biệt là $S = (a;b).$ Tính $T = a+b.$

A. $T = \frac{{ – 1}}{2}.$

B. $T = \frac{3}{2}.$

C. $T = \frac{7}{2}.$

D. $T = \frac{9}{2}.$

## Bài 5. Tính tổng tất cả các giá trị nguyên của tham số $m$ sao cho phương trình $2{x^3} – (m + 1)x + 4 = 0$ có hai nghiệm phân biệt trên khoảng $(0;3).$

A. $22.$

B. $171.$

C. $156.$

D. $161.$

## Bài 6. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình ${x^2} – 2x + (m + 2)\sqrt {2x – {x^2}} – 2m + 1 = 0$ có hai nghiệm phân biệt?

A. $1.$

B. $2.$

C. $3.$

D. $0.$

## Bài 7. Biết tập tất cả các giá trị của tham số $m$ để phương trình ${\sin ^2}x + (2 – m)\cos x + 3m = 0$ có $2$ nghiệm phân biệt trên đoạn $[ – \pi ;\pi ]$ là $S = [a;b).$ Tính $T = a + b.$

A. $T = – \frac{1}{2}.$

B. $T = \frac{3}{2}.$

C. $T = – \frac{2}{3}.$

D. $T = \frac{7}{3}.$

## Bài 8. Cho phương trình $\sqrt x + \sqrt {4 – x} = \sqrt {4x – {x^2} + m} .$ Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình đã cho có hai nghiệm phân biệt.

A. $1.$

B. $2.$

C. $4.$

D. $7.$

## Bài 9. Cho phương trình:

${\sin ^3}x\left( {{{\sin }^6}x + 3} \right) – {m^3} – 3m$ $= 27{\sin ^3}x + 27m{\sin ^2}x + 9\left( {1 + {m^2}} \right)\sin x.$

Tính tổng tất cả các giá trị nguyên của tham số $m$ để phương trình đã cho có nghiệm thuộc đoạn $\left[ { – \frac{\pi }{6};\frac{\pi }{2}} \right].$

A. $2.$

B. $-1.$

C. $-2.$

D. $0.$

## Bài 10. Cho phương trình ${x^3} + 3{x^2} + 6x – 2\sqrt {x + m}$ $= (x + m + 1)\sqrt {x + m} – 4.$ Biết tập hợp tất cả các giá trị của tham số $m$ để phương trình đã cho có hai nghiệm phân biệt là $S =(a;b].$ Tính tổng $T = 4a + b.$

A. $T =-3.$

B. $T =4.$

C. $T =-2.$

D. $T = 7.$

<!-- chunk:14 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem.html -->
## V. BẢNG ĐÁP ÁN BÀI TẬP TỰ LUYỆN
 1. $A.$

2. $B.$

3. $B.$

4. $D.$

5. $C.$

6. $A.$

7. $A.$

8. $A.$

9. $C.$

10. $B.$