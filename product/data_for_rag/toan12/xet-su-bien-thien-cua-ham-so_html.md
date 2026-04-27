# Xét sự biến thiên của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp giải bài toán tự luận và trắc nghiệm xét sự biến thiên của hàm số trong chương trình Giải tích 12.

1. PHƯƠNG PHÁP CHUNG

Để xét sự biến thiên của hàm số $y = f(x)$, ta thực hiện theo các bước:

+ Bước 1: Miền xác định.

+ Bước 2: Tính đạo hàm $y’$, rồi tìm các điểm tới hạn (thông thường là việc giải phương trình $y’ = 0$).

+ Bước 3: Tính các giới hạn (nếu cần).

+ Bước 4: Lập bảng biến thiên của hàm số.

## Bài tập

<!-- chunk:1 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 1. Hàm số nào sau đây là hàm số đồng biến trên $R$?

A. $y = {\left( {{x^2} – 1} \right)^2} – 3x + 2.$

B. $y = \frac{x}{{\sqrt {{x^2} + 1} }}.$

C. $y = \frac{x}{{x + 1}}.$

D. $y = \tan x.$

Đáp số trắc nghiệm B.

Lời giải tự luận:

Ta lần lượt:

+ Với hàm số $y = {\left( {{x^2} – 1} \right)^2} – 3x + 2$ xác định trên $R$ thì:

$y’ = 2x\left( {{x^2} – 1} \right) – 3$ $= 2{x^3} – 2x – 3.$

Hàm số trên không thể đồng biến trên $R$ bởi $y'(0) = – 3 < 0$, do đó đáp án A bị loại.

+ Với hàm số $y = \frac{x}{{\sqrt {{x^2} + 1} }}$ xác định trên $R$ thì:

$y’ = \frac{1}{{\sqrt {{{\left( {{x^2} + 1} \right)}^3}} }} > 0$ với mọi $x \in R.$

Do đó đáp án B là đúng, tới đây chúng ta dừng lại.

Lựa chọn đáp án bằng phép thử:
 Ta lần lượt đánh giá:

+ Trước tiên, hàm số đồng biến trên $R$ thì phải xác định trên $R.$ Do đó, các đáp án C và D bị loại. Tới đây ta chỉ còn phải lựa chọn A và B.

+ Vì A là hàm số bậc bốn nên có đạo hàm là một đa thức bậc ba, và một đa thức bậc ba thì không thể luôn dương (do phương trình bậc ba luôn có ít nhất một nghiệm), suy ra đáp án A không thỏa mãn.

Do đó việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta lần lượt thử cho các hàm số bằng việc thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Đánh giá $y’$ để xét tính đồng biến của nó trên $R.$

Tới hàm số trong B chúng ta thấy thỏa mãn nên dừng lại ở đó. Trong trường hợp trái lại chúng ta sẽ tiếp tục hàm số ở C, tại đây nếu C thỏa mãn thì chúng ta lựa chọn đáp án C, còn không sẽ khẳng định D là đúng.

+ Trong cách lựa chọn đáp án bằng phép thử chúng ta loại trừ dần bằng việc thực hiện theo hai bước:

Bước 1: Sử dụng điều kiện cần để hàm số đơn điệu trên D là phải xác định trên D, chúng ta loại bỏ được các đáp án C và D bởi các hàm số này đều không xác định trên R.

Bước 2: Sử dụng tính chất nghiệm của phương trình bậc ba, để loại bỏ được đáp án A.

<!-- chunk:2 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 2. Hàm số $y = {x^3} – 6{x^2} + 9x + 7$ đồng biến trên các khoảng:

A. $( – \infty ;1)$ và $[3; + \infty ).$

B. $( – \infty ;1]$ và $[3; + \infty ).$

C. $( – \infty ;1]$ và $(3; + \infty ).$

D. $( – \infty ;1)$ và $(3; + \infty ).$

Đáp số trắc nghiệm B.

Lời giải tự luận:

Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 3{x^2} – 12x + 9.$

+ Hàm số đồng biến khi: $y’ \ge 0$ $\Leftrightarrow 3{x^2} – 12x + 9 \ge 0$ $\Leftrightarrow {x^2} – 4x + 3 \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge 3}\\
{x \le 1}
\end{array}} \right..
$$

Vậy hàm số đồng biến trên các khoảng $( – \infty ;1]$ và $[3; + \infty ).$

Lựa chọn đáp án bằng phép thử:
 Nhận xét rằng hàm đồng biến khi $y’ \ge 0$ do đó sẽ có hai nửa đoạn (dấu ngoặc vuông) nên các đáp án A, C và D bị loại.

Do đó việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thiết lập điều kiện để hàm số đồng biến, từ đó rút ra được các khoảng cần tìm.

+ Trong cách lựa chọn đáp án bằng phép thử, chúng ta loại trừ ngay được các đáp án A, C và D thông qua việc đánh giá về sự tồn tại của các dấu ngoặc vuông. Trong trường hợp các đáp án được cho dưới dạng khác, chúng ta có thể đánh giá thông qua tính chất của hàm đa thức bậc ba. Bài toán sau đây minh họa cho nhận xét này.

<!-- chunk:3 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 3. Hàm số $y = 2{x^3} + 3{x^2} + 1$ nghịch biến trên các khoảng:

A. $( – \infty ; – 1]$ và $[0; + \infty ).$

B. $( – \infty ;0]$ và $[1; + \infty ).$

C. $[ – 1;0].$

D. $(0;1).$

Đáp số trắc nghiệm C.

Lời giải tự luận:
Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 6{x^2} + 6x.$

+ Hàm số nghịch biến khi: $y’ \le 0$ $\Leftrightarrow 6{x^2} + 6x \le 0$ $\Leftrightarrow – 1 \le x \le 0.$

Vậy hàm số nghịch biến trên $[ – 1;0].$

Lựa chọn đáp án bằng phép thử:
Nhận xét rằng:

+ Hàm số nghịch biến khi $y’ \ge 0$ do đó sẽ có hai nửa đoạn (dấu ngoặc vuông) nên đáp án D bị loại.

+ Hàm đa thức bậc ba với $a > 0$ nghịch biến trên đoạn nằm giữa hai nghiệm của phương trình $y’ = 0$ nên các đáp án A và B bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

Chú ý: Như vậy, để lựa chọn được đáp án đúng bằng phép thử, các em học sinh cần nắm vững kiến thức về tính chất của hàm đa thức bậc ba và dấu tam thức bậc hai.

<!-- chunk:4 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 4. Hàm số $y = {x^4} – 2{x^2} – 5$ đồng biến trên các khoảng:

A. $( – \infty ; – 1]$ và $[1; + \infty ).$

B. $[ – 1;0]$ và $[1; + \infty ).$

C. $( – \infty ; – 1]$ và $[0;1].$

D. $[ – 1;1].$

Đáp số trắc nghiệm B.

Lời giải tự luận 1:
Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 4{x^3} – 4x.$

$y’ = 0$ $\Leftrightarrow 4{x^3} – 4x = 0$ $\Leftrightarrow 4x\left( {{x^2} – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-1.png" alt="">

Từ đó suy ra hàm số đồng biến trên $[ – 1;0]$ và $[1; + \infty ).$

Lời giải tự luận 2:
Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 4{x^3} – 4x$, $y’ \ge 0$ $\Leftrightarrow 4{x^3} – 4x \ge 0$ $\Leftrightarrow x \in [ – 1;0] \cup [1; + \infty )$ dựa trên việc xét dấu bằng cách vẽ trục số như sau:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-2.png" alt="">

Từ đó suy ra hàm số đồng biến trên $[ – 1;0]$ và $[1; + \infty ).$

Lựa chọn đáp án bằng phép thử:
Nhận xét rằng hàm đa thức bậc bốn dạng trùng phương với $a > 0$ thì:

+ Có khoảng đồng biến chứa $+ \infty$ nên các đáp án C và D bị loại.

+ Có khoảng đồng biến không chứa $– \infty$ nên đáp án A bị loại.

Do đó việc lựa chọn đáp án $B$ là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1, chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thay vì thiết lập điều kiện $y’ \ge 0$ chúng ta đi giải phương trình $y’ = 0$ rồi lập bảng biến thiên cho trực quan (bởi việc giải bất phương trình bậc ba dễ gây nhầm dấu).

+ Trong cách giải tự luận 2, chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thiết lập điều kiện $y’ \ge 0$ chúng ta xác định được nghiệm của bất phương trình bằng việc xét dấu ngay trên trục số (miền ngoài cùng cùng dấu với hệ số $a$ và sau đó đan dấu).

+ Trong cách lựa chọn đáp án bằng phép thử, các em học sinh cần nắm vững kiến thức về tính chất của hàm đa thức bậc bốn dạng trùng phương.

<!-- chunk:5 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 5. Hàm số $y = \frac{x}{{x – 2}}$ nghịch biến trên khoảng:

A. $( – \infty ;2].$

B. $[2; + \infty ).$

C. $( – \infty ;2)$ và $(2; + \infty ).$

D. $R.$

Đáp số trắc nghiệm C.

Lời giải tự luận:

Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 2\} .$

+ Đạo hàm: $y’ = \frac{{ – 2}}{{{{(x – 2)}^2}}} < 0.$

Vậy hàm số nghịch biến trên $( – \infty ;2)$ và $(2; + \infty ).$

Lựa chọn đáp án bằng phép thử:

Nhận xét rằng hàm phân thức bậc nhất trên bậc nhất luôn đơn điệu (luôn đồng biến hoặc luôn nghịch biến) trên từng khoảng xác định của nó, do đó ta lựa chọn ngay đáp án C cho bài toán.

Chú ý: Như vậy, để lựa chọn được đáp án đúng bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất của hàm phân thức bậc nhất trên bậc nhất.

<!-- chunk:6 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 6. Hàm số $y = \frac{{{x^2}}}{{1 – x}}$ đồng biến trên các khoảng:

A. $( – \infty ;1)$ và $(1;2).$

B. $( – \infty ;1)$ và $(2; + \infty ).$

C. $(0;1)$ và $(1;2).$

D. $( – \infty ;1)$ và $(1; + \infty ).$

Đáp số trắc nghiệm C.

Lời giải tự luận:
Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{2x(1 – x) + {x^2}}}{{{{(1 – x)}^2}}}$ $= \frac{{ – {x^2} + 2x}}{{{{(1 – x)}^2}}}.$

+ Hàm số đồng biến khi $y’ \ge 0$ $\Leftrightarrow – {x^2} + 2x \ge 0$ $\Leftrightarrow 0 \le x \le 2.$

Vậy hàm số đồng biến trên các khoảng $(0;1)$ và $(1;2).$

Lựa chọn đáp án bằng phép thử 1:

Ta lần lượt đánh giá:

+ Vì $D = R\backslash \{ 1\}$ và với hàm phân thức bậc hai trên bậc nhất thì $y’ = 0$ hoặc vô nghiệm hoặc có hai nghiệm phân biệt đối xứng qua điểm $1.$ Do đó các đáp án A và B bị loại. Tới đây ta chỉ còn phải lựa chọn C và D.

+ Lấy $x = 2$ và $x = 3$ suy ra $y(2) = -4$ và $y(3) = – \frac{9}{2}$, tức là hàm số nghịch biến trên $(2;3)$, suy ra đáp án D bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

Lựa chọn đáp án bằng phép thử 2:
Với hàm phân thức bậc hai trên bậc nhất có $ad < 0$ thì điều kiện $y’ > 0$ tương đương với $A{x^2} + Bx + C > 0$ (với $A < 0$). Suy ra, chúng ta chỉ có thể nhận được $(\alpha ;\beta )$ (với $\alpha + \beta = 2$).

Do đó việc lựa chọn đáp án C là đúng đắn.

<!-- chunk:7 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 7. Hàm số $y = \sqrt {2 + x – {x^2}}$ nghịch biến trên khoảng:

A. $\left( {\frac{1}{2};2} \right).$

B. $\left( { – 1;\frac{1}{2}} \right).$

C. $(2; + \infty ).$

D. $( – 1;2).$

Đáp số trắc nghiệm A.

Lời giải tự luận:
Ta lần lượt có:

+ Tập xác định $D = [ – 1;2].$

+ Đạo hàm: $y’ = \frac{{1 – 2x}}{{2\sqrt {2 + x – {x^2}} }}$, $y’ < 0$ $\Leftrightarrow 1 – 2x < 0$ $\Leftrightarrow x > \frac{1}{2}.$

Vậy hàm số nghịch biến trên $\left( {\frac{1}{2};2} \right).$

Lựa chọn đáp án bằng phép thử 1:
Ta lần lượt đánh giá:

+ Tìm tập xác định của hàm số $D = [ – 1;2]$, suy ra các đáp án C và D là sai.

+ Xuất phát từ tính chất của hàm số $y = a{x^2} + bx + c$ (với $a < 0$) nghịch biến trên $\left( { – \frac{b}{{2a}}; + \infty } \right)$, suy ra đáp án B không thỏa mãn.

Do đó việc lựa chọn đáp án A là đúng đắn.

Lựa chọn đáp án bằng phép thử 2:

Xuất phát từ tính chất của hàm số: $y = – {x^2} + x + 2$ nghịch biến trên $\left( {\frac{1}{2}; + \infty } \right)$, suy ra các đáp án B, C, D không thỏa mãn.

Do đó việc lựa chọn đáp án A là đúng đắn.

<!-- chunk:8 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 8. Hàm số $y = x – \sqrt x$ đồng biến trên khoảng:

A. $\left( { – \infty ;\frac{1}{4}} \right).$

B. $\left( {\frac{1}{4}; + \infty } \right).$

C. $\left( {0;\frac{1}{4}} \right).$

D. $( – \infty ;0).$

Đáp số trắc nghiệm B.

Lời giải tự luận:

+ Ta có điều kiện: $x \ge 0$ $\Rightarrow D = [0; + \infty ).$

+ Đạo hàm $y’ = 1 – \frac{1}{{2\sqrt x }}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{2\sqrt x }} = 0$ $\Leftrightarrow x = \frac{1}{4}.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-3.png" alt="">

Vậy hàm số đồng biến trên $\left( {\frac{1}{4}; + \infty } \right).$

Lựa chọn đáp án bằng phép thử:

Ta lần lượt đánh giá:

+ Vì $D = [0; + \infty )$ nên các đáp án A và D bị loại. Tới đây ta chỉ còn phải lựa chọn B và C.

+ Lấy $x = \frac{1}{4}$ và $x = 1$ suy ra $y\left( {\frac{1}{4}} \right) = – \frac{1}{4}$ và $y(1) = 0$, tức là hàm số đồng biến trên $\left( {\frac{1}{4};1} \right).$ Suy ra đáp án C bị loại.

Do đó việc lựa chọn đáp án B là đúng đắn.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 9. Cho hàm số: $y = 2{x^2} – 3x + 1.$

a. Khảo sát sự biến thiên của hàm số.

b. Biện luận theo $m$ số nghiệm của phương trình $2{x^2} – 3x + 2m = 0.$

a. Miền xác định $D = R.$

Đạo hàm: $y’ = 4x – 3$, $y’ = 0$ $\Leftrightarrow 4x – 3 = 0$ $\Leftrightarrow x = \frac{3}{4}$ và $f\left( {\frac{3}{4}} \right) = – \frac{1}{8}.$

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y$ $= \mathop {\lim }\limits_{x \to \pm \infty } {x^2}\left( {2 – \frac{3}{x} + \frac{1}{{{x^2}}}} \right)$ $= + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-4.png" alt="">

b. Viết lại phương trình dưới dạng: $2{x^2} – 3x + 1 = 1 – 2m.$

Số nghiệm của phương trình bằng số giao điểm của đồ thị hàm số với đường thẳng $(d):y = 1 – 2m.$

Dựa vào bảng biến thiên ta nhận được kết luận:

+ Với $1 – 2m < – \frac{1}{8}$ $\Leftrightarrow m > \frac{9}{{16}}$ phương trình vô nghiệm.

+ Với $1 – 2m = – \frac{1}{8}$ $\Leftrightarrow m = \frac{9}{{16}}$ phương trình có nghiệm kép $x = \frac{3}{4}.$

+ Với $1 – 2m > – \frac{1}{8}$ $\Leftrightarrow m < \frac{9}{{16}}$ phương trình có hai nghiệm phân biệt.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 10. Cho hàm số: $y = {x^3} – 3{x^2} + 4x – 2.$

a. Khảo sát sự biến thiên của hàm số.

b. Chứng tỏ rằng với mọi $m$ phương trình ${x^3} – 3{x^2} + 4x – m = 0$ luôn có nghiệm duy nhất.

a. Miền xác định $D = R.$

Đạo hàm: $y’ = 3{x^2} – 6x + 4$ $= 3{(x – 1)^2} + 1 > 0$, $x \in R$ $\Rightarrow$ Hàm số luôn đồng biến.

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y$ $= \mathop {\lim }\limits_{x \to \pm \infty } \left[ {{x^3}\left( {1 – \frac{3}{x} + \frac{4}{{{x^2}}} – \frac{2}{{{x^3}}}} \right)} \right]$ 
$$
= \left[ {\begin{array}{c}
{ + \infty {\rm{\:khi\:}}x \to + \infty }\\
{ – \infty {\rm{\:khi\:}}x \to – \infty }
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-5.png" alt="">

b. Viết lại phương trình dưới dạng: ${x^3} – 3{x^2} + 4x – 2 = m – 2.$

Khi đó số nghiệm của phương trình bằng số giao điểm của $(C)$ với đường thẳng $(d): y = m – 2.$

Do đó dựa vào bảng biến thiên ta kết luận phương trình luôn có nghiệm duy nhất.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 11. Cho hàm số: $(C):y = – \frac{1}{2}{x^4} – {x^2} + \frac{3}{2}.$

a. Khảo sát sự biến thiên của hàm số.

b. Tìm $m$ để phương trình ${x^4} + 2{x^2} + m = 0$ có nghiệm duy nhất.

a. Miền xác định $D = R.$

Đạo hàm: $y’ = – 2{x^3} – 2x.$

$y’ = 0$ $\Leftrightarrow – 2{x^3} – 2x = 0$ $\Leftrightarrow – 2x\left( {{x^2} + 1} \right) = 0$ $\Leftrightarrow x = 0.$

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y$ $= \mathop {\lim }\limits_{x \to \pm \infty } \left[ { – {x^4}\left( {\frac{1}{2} + \frac{1}{{{x^2}}} – \frac{3}{{2{x^4}}}} \right)} \right]$ $= – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-6.png" alt="">

b. Viết lại phương trình dưới dạng: $– \frac{1}{2}{x^4} – {x^2} + \frac{3}{2} = \frac{m}{2} + \frac{3}{2}.$

Khi đó số nghiệm của phương trình bằng số giao điểm của $(C)$ với đường thẳng $(d):y = \frac{m}{2} + \frac{3}{2}$ nên phương trình có nghiệm duy nhất khi: $\frac{m}{2} + \frac{3}{2} = \frac{3}{2}$ $\Leftrightarrow m = 0.$

Vậy với $m = 0$ thoả mãn điều kiện đầu bài.

<!-- chunk:12 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 12. Cho hàm số: $y = \frac{{x – 2}}{{x + 2}}.$

a. Khảo sát sự biến thiên của hàm số.

b. Biện luận theo $m$ số nghiệm và dấu các nghiệm của phương trình: $(m – 1)x + 2m + 2 = 0.$

a. Miền xác định $D = R\backslash \{ – 2\} .$

Đạo hàm: $y’ = \frac{4}{{{{(x + 2)}^2}}} > 0$, $x \in D$, suy ra hàm số luôn đồng biến trên các khoảng xác định.

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = \mathop {\lim }\limits_{x \to + \infty } y = 1$ và $\mathop {\lim }\limits_{x \to – {2^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to – {2^ + }} y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-7.png" alt="">

b. Viết lại phương trình dưới dạng: $m(x + 2) = x – 2$ $\Leftrightarrow \frac{{x – 2}}{{x + 2}} = m$ (vì $x = – 2$ không phải là nghiệm của phương trình).

Số nghiệm của phương trình bằng số giao điểm của $(C)$ với đường thẳng $(d): y = m.$

Dựa vào bảng biến thiên ta nhận được kết luận:

+ Với $m < 1$ phương trình có một nghiệm lớn hơn $-2.$

+ Với $m > 1$ phương trình có một nghiệm nhỏ hơn $-2.$

+ Với $m = 1$ phương trình vô nghiệm.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 13. Cho hàm số: $y = \frac{{{x^2} – x + 2}}{{2 – x}}.$

a. Khảo sát sự biến thiên của hàm số.

b. Biện luận theo $m$ số nghiệm và dấu các nghiệm của phương trình: ${x^2} + (m – 1)x + 2 – 2m = 0.$

a. Miền xác định $D = R\backslash \{ 2\} .$

Đạo hàm: $y’ = \frac{{ – {x^2} + 4x}}{{{{(2 – x)}^2}}}$, $y’ = 0$ $\Leftrightarrow 4x – {x^2} = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 4}
\end{array}} \right..
$$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = – \infty$ và $\mathop {\lim }\limits_{x \to {2^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to {2^ + }} y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-8.png" alt="">

b. Viết lại phương trình dưới dạng: ${x^2} – x + 2 = (2 – x)m$ $\Leftrightarrow \frac{{{x^2} – x + 2}}{{2 – x}} = m$ (vì $x = 2$ không phải là nghiệm của phương trình).

Số nghiệm của phương trình bằng số giao điểm của $(C)$ với đường thẳng $(d): y = m.$

Dựa vào bảng biến thiên ta nhận được kết luận:

+ Với $m < -7$ phương trình có hai nghiệm phân biệt $2 < {x_1} < 4 < {x_2}.$

+ Với $m = -7$ phương trình có nghiệm kép ${x_0} = 4.$

+ Với $-7 < m < 1$ phương trình vô nghiệm.

+ Với $m = 1$ phương trình có nghiệm kép ${x_0} = 0.$

+ Với $m > 1$ phương trình có hai nghiệm phân biệt ${x_1} < 0 < {x_2} < 2.$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 14. Cho hàm số $y = \frac{x}{{{x^2} + 1}}.$

a. Khảo sát sự biến thiên của hàm số.

b. Biện luận theo $m$ số nghiệm của phương trình $m{x^2} – x + m = 0.$

a. Miền xác định $D = R.$

Đạo hàm: $y’ = \frac{{1 – {x^2}}}{{{{\left( {{x^2} + 1} \right)}^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – {x^2} = 0$ $\Leftrightarrow x = \pm 1.$

Giới hạn $\mathop {\lim }\limits_{x \to \pm \infty } y = 0.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-9.png" alt="">

b. Viết lại phương trình dưới dạng: $m\left( {{x^2} + 1} \right) = x$ $\Leftrightarrow \frac{x}{{{x^2} + 1}} = m.$

Số nghiệm của phương trình bằng số giao điểm của $(C)$ với đường thẳng $(d): y = m.$

Dựa vào bảng biến thiên ta nhận được kết luận:

+ Với $|m| > \frac{1}{2}$ hoặc $m = 0$ phương trình vô nghiệm.

+ Với $m = – \frac{1}{2}$ phương trình có nghiệm kép ${x_0} = – 1.$

+ Với $m = \frac{1}{2}$ phương trình có nghiệm kép ${x_0} = 1.$

+ Với $– \frac{1}{2} < m < 0$ phương trình có hai nghiệm phân biệt ${x_1} < – 1 < {x_2} < 0.$

+ Với $0 < m < \frac{1}{2}$ phương trình có hai nghiệm phân biệt $0 < {x_1} < 1 < {x_2}.$

<!-- chunk:15 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 15. Khảo sát sự biến thiên của các hàm số:

a. $y = \sqrt {4x – {x^2}} .$

b. $y = \sqrt[3]{{{x^3} – 3x}}.$

a. Miền xác định $D = [0;4].$

Đạo hàm: $y’ = \frac{{2 – x}}{{\sqrt {4x – {x^2}} }}$, $y’ = 0$ $\Leftrightarrow 2 – x = 0$ $\Leftrightarrow x = 2.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-10.png" alt="">

b. Miền xác định $D = R.$

Đạo hàm: $y’ = \frac{{{x^2} – 1}}{{\sqrt[3]{{{{\left( {{x^3} – 3x} \right)}^2}}}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 1 = 0$ $\Leftrightarrow x = \pm 1.$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-11.png" alt="">

<!-- chunk:16 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 16. Khảo sát sự biến thiên của các hàm số:

a. $y = x + \sqrt {4{x^2} + 2x + 1} .$

b. $y = 2x – 1 – \sqrt {4{x^2} – 4x} .$

a. Miền xác định $D = R.$

Đạo hàm: $y’ = 1 + \frac{{4x + 1}}{{\sqrt {4{x^2} + 2x + 1} }}.$

$y’ = 0$ $\Leftrightarrow 1 + \frac{{4x + 1}}{{\sqrt {4{x^2} + 2x + 1} }} = 0$ $\Leftrightarrow \sqrt {4{x^2} + 2x + 1} = – 4x – 1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 4x – 1 \ge 0}\\
{4{x^2} + 2x + 1 = {{( – 4x – 1)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x \le – \frac{1}{4}}\\
{12{x^2} + 6x = 0}
\end{array}} \right.
$$
 $\Leftrightarrow x = – \frac{1}{2}.$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-12.png" alt="">

b. Miền xác định $D = ( – \infty ;0] \cup [1; + \infty ).$

Đạo hàm: $y’ = 2 – \frac{{2x – 1}}{{\sqrt {{x^2} – x} }}.$

$y’ = 0$ $\Leftrightarrow 2 – \frac{{2x – 1}}{{\sqrt {{x^2} – x} }} = 0$ $\Leftrightarrow 2\sqrt {{x^2} – x} = 2x – 1$ vô nghiệm.

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y$ $= \mathop {\lim }\limits_{x \to \pm \infty } (2x – 1 – \sqrt {4{x^2} – 4x} )$ $= \mathop {\lim }\limits_{x \to \pm \infty } \frac{1}{{2x – 1 + \sqrt {4{x^2} – 4x} }} = 0.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-13.png" alt="">

<!-- chunk:17 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 17.Khảo sát sự biến thiên của các hàm số:

a. $y = \frac{{{x^2}}}{{\sqrt {{x^2} – 4} }}.$

b. $y = \sqrt {\frac{{x + 1}}{{x – 1}}} .$

a. Ta có điều kiện: ${x^2} – 4 > 0$ $\Leftrightarrow |x| > 2$ $\Rightarrow D = ( – \infty ; – 2) \cup (2; + \infty ).$

Đạo hàm: $y’ = \frac{{{x^3} – 8x}}{{\left( {{x^2} – 4} \right)\sqrt {{x^2} – 4} }}.$

$y’ = 0$ $\Leftrightarrow {x^3} – 8x = 0$ $\Leftrightarrow x = 0$ hoặc $x = \pm \sqrt 8 .$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = \mathop {\lim }\limits_{x \to + \infty } y$ $= \mathop {\lim }\limits_{x \to – {2^ – }} y = \mathop {\lim }\limits_{x \to {2^ + }} y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-14.png" alt="">

b. Ta có điều kiện: $\frac{{x + 1}}{{x – 1}} \ge 0$ $\Leftrightarrow x > 1$ hoặc $x \le – 1$ $\Rightarrow D = ( – \infty ; – 1] \cup (1; + \infty ).$

Đạo hàm: $y’ = \frac{{ – 1}}{{{{(x – 1)}^2}\sqrt {\frac{{x + 1}}{{x – 1}}} }} < 0$ $\Rightarrow$ hàm số nghịch biến trên từng khoảng xác định.

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = \mathop {\lim }\limits_{x \to + \infty } y = 1$ $\mathop {\lim }\limits_{x \to {1^ + }} y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-15.png" alt="">

<!-- chunk:18 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 18. Tuỳ theo $m$, khảo sát sự biến thiên của các hàm số:

a. $y = {x^3} + 3{x^2} + mx + m.$

b. $y = \frac{1}{4}{x^4} – \frac{1}{3}(m + 2){x^3} + m{x^2} + 8.$

a. Miền xác định $D = R.$

Đạo hàm: $y’ = 3{x^2} + 6x + m$, $y’ = 0$ $\Leftrightarrow 3{x^2} + 6x + m = 0$ $(1).$

Ta có $\Delta ‘ = 9 – 3m$ nên đi xét hai trường hợp:

Trường hợp 1: Nếu $\Delta ‘ \le 0$ $\Leftrightarrow 9 – 3m \le 0$ $\Leftrightarrow m \ge 3.$

Khi đó $y’ \ge 0$ nên hàm số đồng biến trên $D.$

Giới hạn $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$ và $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-16.png" alt="">

Trường hợp 2: Nếu $\Delta ‘ > 0$ $\Leftrightarrow 9 – 3m > 0$ $\Leftrightarrow m < 3.$

Khi đó $(1)$ có hai nghiệm phân biệt $x = \frac{{ – 3 \pm \sqrt {9 – 3m} }}{3}.$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$ và $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-17.png" alt="">

b. Miền xác định $D = R.$

Đạo hàm: $y’ = {x^3} – (m + 2){x^2} + 2mx.$

$y’ = 0$ $\Leftrightarrow {x^3} – (m + 2){x^2} + 2mx = 0$ $\Leftrightarrow x\left[ {{x^2} – (m + 2)x + 2m} \right] = 0.$

$\Leftrightarrow x = 0$ hoặc $x = 2$ hoặc $x = m.$

Ta xét các trường hợp:

Trường hợp 1: Nếu $m < 0$ ta có:

Giới hạn $\mathop {\lim }\limits_{x \to \pm \infty } y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-18.png" alt="">

Trường hợp 2: Nếu $m = 0$ khi đó:

$y’ = {x^2}(x – 2)$, do đó dấu của $y’$ chỉ phụ thuộc vào dấu của $x – 2.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-19.png" alt="">

Trường hợp 3: Nếu $0 < m < 2$ ta có:

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-20.png" alt="">

Trường hợp 4: Nếu $m = 2$ khi đó:

$y’ = x{(x – 2)^2}$, do đó dấu của $y’$ chỉ phụ thuộc vào dấu của $x.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-21.png" alt="">

Trường hợp 5: Nếu $m > 2$ ta có bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-22.png" alt="">

<!-- chunk:19 level:4 source:https://toanmath.com/2019/09/xet-su-bien-thien-cua-ham-so.html -->
## Bài tập 19. Tuỳ theo $m$, khảo sát sự biến thiên của các hàm số:

a. $y = \frac{{(m – 2)x – \left( {{m^2} – 2m + 4} \right)}}{{x – m}}.$

b. $y = \frac{{(3m + 1)x – {m^2} + m}}{{x + m}}.$

c. $y = \frac{{{x^2} + mx – m + 8}}{{x – 1}}.$

d. $y = \frac{{{x^2} + mx – 1}}{{x – 1}}.$

a. Miền xác định $D = R\backslash \{ m\} .$

Đạo hàm: $y’ = \frac{4}{{{{(x – m)}^2}}} > 0$ $\Rightarrow$ Hàm số đồng biến trên các khoảng xác định.

Giới hạn $\mathop {\lim }\limits_{x \to \pm \infty } y = m – 2$ và $\mathop {\lim }\limits_{x \to {m^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to {m^ + }} y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-23.png" alt="">

b. Miền xác định $D = R\backslash \{ – m\} .$

Đạo hàm: $y’ = \frac{{4{m^2}}}{{{{(x + m)}^2}}}.$

Ta xét các trường hợp:

Trường hợp 1: Nếu $m = 0$ thì $y’ = 0$ $\Leftrightarrow$ Hàm số là hàm hằng.

Trường hợp 2: Nếu $m \ne 0$ thì $y’ > 0$ $\Leftrightarrow$ Hàm số đồng biến trên các khoảng xác định.

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y = 3m + 1$ và $\mathop {\lim }\limits_{x \to – {m^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to – {m^ + }} y = – \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-24.png" alt="">

c. Miền xác định $D = R\backslash \{ 1\} .$

Đạo hàm: $y’ = \frac{{{x^2} – 2x – 8}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x – 8 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 4}\\
{x = – 2}
\end{array}} \right..
$$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$ và $\mathop {\lim }\limits_{x \to {1^ – }} y = – \infty$, $\mathop {\lim }\limits_{x \to {1^ + }} y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-25.png" alt="">

Trong đó $f(-2) = m – 4$ và $f(4) = m + 8.$

d. Miền xác định $D = R\backslash \{ 1\} .$

Đạo hàm: $y’ = \frac{{{x^2} – 2x – m + 1}}{{{{(x – 1)}^2}}}.$

$y’ = 0$ $\Leftrightarrow {x^2} – 2x – m + 1 = 0$ $(1).$

Ta có $\Delta ‘ = 1 + m – 1 = m$ đi xét hai trường hợp:

Trường hợp 1: Nếu $\Delta \le 0$ $\Leftrightarrow m \le 0.$

Suy ra $y’ \ge 0$, $\forall x \in D$ $\Leftrightarrow$ Hàm số luôn đồng biến.

Trường hợp 2: Nếu $\Delta > 0$ $\Leftrightarrow m > 1.$

Suy ra phương trình $(1)$ có hai nghiệm là $x = 1 \pm \sqrt m .$

Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$ và $\mathop {\lim }\limits_{x \to {1^ – }} y = – \infty$, $\mathop {\lim }\limits_{x \to {1^ + }} y = + \infty .$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/xet-su-bien-thien-cua-ham-so-26.png" alt="">

Trong đó $f\left( {{x_1}} \right) = 2 + 2\sqrt m + m$ và $f\left( {{x_2}} \right) = 2 – 2\sqrt m + m.$