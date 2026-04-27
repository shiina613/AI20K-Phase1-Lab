# Phương pháp giải nhanh trắc nghiệm tính đơn điệu của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp giải nhanh bài tập trắc nghiệm tính đơn điệu của hàm số trong chương trình Giải tích 12.

<!-- chunk:1 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 1. Hàm số nào sau đây là hàm số đồng biến trên $R$?

A. $y = {\left( {{x^2} + 1} \right)^2} – 3x.$

B. $y = x\sqrt {{x^2} + 1} .$

C. $y = x – \frac{1}{x}.$

D. $y = – \cot x.$

Chọn B.
Lời giải tự luận 1: (Thực hiện từ trái qua phải): Ta lần lượt:

+ Với hàm số $y = {\left( {{x^2} + 1} \right)^2} – 3x$ xác định trên $R$ thì:

$y’ = 4x\left( {{x^2} + 1} \right) – 3$ $= 4{x^3} + 4x – 3.$

Hàm số không thể đồng biến trên $R$ bởi $y'(0) = – 3 < 0$, do đó đáp án A bị loại.

+ Với hàm số $y = x\sqrt {{x^2} + 1}$ xác định trên $R$ thì:

$y’ = \sqrt {{x^2} + 1} + \frac{{{x^2}}}{{\sqrt {{x^2} + 1} }} > 0$, $\forall x \in R.$

Do đó đáp án B là đúng, tới đây ta dừng lại.

Lời giải tự luận 2: (Thực hiện từ phải qua trái): Ta lần lượt:

+ Với hàm số $y = – \cot x$ xác định trên $R\backslash \{ k\pi ,k \in Z\}$ nên đáp án D bị loại.

+ Với hàm số $y = x – \frac{1}{x}$ xác định trên $R\backslash \{ 0\}$ nên đáp án C bị loại.

+ Với hàm số $y = x\sqrt {{x^2} + 1}$ xác định trên $R$ thì:

$y’ = \sqrt {{x^2} + 1} + \frac{{{x^2}}}{{\sqrt {{x^2} + 1} }} > 0$, $\forall x \in R.$

Do đó đáp án B là đúng, tới đây ta dừng lại.

Lựa chọn đáp án bằng phép thử: Ta lần lượt đánh giá:

+ Trước tiên, hàm số đồng biến trên $R$ thì phải xác định trên $R.$ Do đó, các đáp án C và D bị loại. Tới đây ta chỉ còn phải lựa chọn A và B.

+ Vì A là hàm số bậc bốn nên có đạo hàm là một đa thức bậc ba, và một đa thức bậc ba thì không thể luôn dương (do phương trình bậc ba luôn có ít nhất một nghiệm), suy ra đáp án A không thỏa mãn.

Do đó, việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta lần lượt thử từ trái qua phải cho các hàm số bằng việc thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Đánh giá $y’$ để xét tính đồng biến của nó trên $R.$ Tới hàm số trong B chúng ta thấy thỏa mãn nên dừng lại ở đó. Trong trường hợp trái lại, chúng ta sẽ tiếp tục hàm số ở C, tại đây nếu C thỏa mãn thì chúng ta lựa chọn đáp án C, còn không sẽ khẳng định D là đúng.

+ Trong cách giải tự luận 2 chúng ta lần lượt thử từ phải qua trái cho các hàm số.

+ Trong cách lựa chọn đáp án bằng phép thử chúng ta loại trừ dần bằng việc thực hiện theo hai bước:

Bước 1: Sử dụng điều kiện cần để hàm số đơn điệu trên $D$ là phải xác định trên $D$, chúng ta loại bỏ được các đáp án C và D bởi các hàm số này đều không xác định trên $R.$

Bước 2: Sử dụng tính chất nghiệm của phương trình bậc ba, để loại bỏ được đáp án A.

<!-- chunk:2 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 2. Hàm số nào sau đây là hàm số nghịch biến trên $R$?

A. $y = – {x^3} + 2{x^2} – x + 3.$

B. $y = – {x^4} + 2{x^2} + 1.$

C. $y = \cos 2x – 2x + 3.$

D. $y = \sqrt {1 – {x^2}} .$

Chọn C.

Lời giải tự luận 1: (Thực hiện từ trái qua phải): Ta lần lượt:

+ Với hàm số $y = – {x^3} + 2{x^2} – x + 3$ xác định trên $R$ thì:

$y’ = – 3{x^2} + 4x – 1.$

$y’ \le 0$ $\Leftrightarrow – 3{x^2} + 4x – 1 \le 0$ $\Leftrightarrow x \le \frac{1}{3}$ hoặc $x \ge 1.$

Do đó đáp án A bị loại.

+ Với hàm số $y = – {x^4} + 2{x^2} + 1$ xác định trên $R$ thì:

$y’ = – 4{x^3} + 4x.$

$y’ \le 0$ $\Leftrightarrow – 4{x^3} + 4x \le 0$ $\Leftrightarrow – 4x\left( {{x^2} – 1} \right) \le 0$ $\Leftrightarrow – 1 \le x \le 0$ hoặc $x \ge 1.$

Do đó đáp án B bị loại.

+ Với hàm số $y = \cos 2x – 2x + 3$ xác định trên $R$ thì:

$y’ = – 2\sin 2x – 2$ $= – 2(\sin 2x + 1) \le 0$, $\forall x \in R.$

Do đó đáp án C là đúng, tới đây chúng ta dừng lại.

Lời giải tự luận 2: (Thực hiện từ phải qua trái): Ta lần lượt:

+ Với hàm số $y = \sqrt {1 – {x^2}}$ xác định trên $[ – 1;1]$ nên đáp án D bị loại.

+ Với hàm số $y=\cos 2 x-2 x+3$ xác định trên $R$ thì:

$y’ = – 2\sin 2x – 2$ $= – 2(\sin 2x + 1) \le 0$, $\forall x \in R.$

Do đó đáp án C là đúng, tới đây chúng ta dừng lại.

Lựa chọn đáp án bằng phép thử: Ta lần lượt đánh giá:

+ Trước tiên, hàm số nghịch biến trên $R$ thì phải xác định trên $R.$ Do đó đáp án D bị loại. Tới đây ta chỉ còn phải lựa chọn A, B và C.

+ Vì B là hàm số bậc bốn nên có đạo hàm là một đa thức bậc ba, và một đa thức bậc ba thì không thể luôn âm (do phương trình bậc ba luôn có ít nhất một nghiệm), suy ra đáp án B không thỏa mãn.

+ Với hàm số $y = – {x^3} + 2{x^2} – x + 3$ xác định trên $R$ thì:

$y’ = – 3{x^2} + 4x – 1.$

$y’ \le 0$ $\Leftrightarrow – 3{x^2} + 4x – 1 \le 0$ $\Leftrightarrow x \le \frac{1}{3}$ hoặc $x \ge 1.$

Do đó đáp án A bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

<!-- chunk:3 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 3. Hàm số $y = \frac{1}{3}{x^3} – 2{x^2} + 3x + 1$ đồng biến trên các khoảng:

A. $( – \infty ;1)$ và $[3; + \infty ).$

B. $( – \infty ;1]$ và $[3; + \infty ).$

C. $( – \infty ;1]$ và $(3; + \infty ).$

D. $( – \infty ;1)$ và $(3; + \infty ).$

Chọn B.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D=R.$

+ Đạo hàm: $y’ = {x^2} – 4x + 3.$

+ Hàm số đồng biến khi: $y’ \ge 0$ $\Leftrightarrow {x^2} – 4x + 3 \ge 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x \ge 3}\\
{x \le 1}
\end{array}} \right..
$$

Vậy hàm số đồng biến trên các khoảng $( – \infty ;1]$ và $[3; + \infty ).$

Lựa chọn đáp án bằng phép thử: Nhận xét rằng hàm đồng biến khi $y’ \ge 0$ do đó sẽ có hai nửa đoạn (dấu ngoặc vuông) nên các đáp án A, C và D bị loại. Do đó, việc lựa chọn đáp án B là đúng đắn.

**Nhận xét**: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thiết lập điều kiện để hàm số đồng biến, từ đó rút ra được các khoảng cần tìm.

+ Trong cách lựa chọn đáp án bằng phép thử chúng ta loại trừ ngay được các đáp án A, C và D thông qua việc đánh giá về sự tồn tại của các dấu ngoặc vuông. Trong trường hợp các đáp án được cho dưới dạng khác, chúng ta có thể đánh giá thông qua tính chất của hàm đa thức bậc ba. Bài toán sau minh họa cho nhận xét này.

<!-- chunk:4 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 4. Hàm số $y = \frac{1}{3}{x^3} + \frac{1}{2}{x^2} + 2$ nghịch biến trên các khoảng:

A. $( – \infty ; – 1]$ và $[0; + \infty ).$

B. $( – \infty ;0]$ và $[1; + \infty ).$

C. $[ – 1;0].$

D. $(0;1).$

Chọn C.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D= R.$

+ Đạo hàm: $y’ = {x^2} + x.$

+ Hàm số nghịch biến khi: $y’ \le 0$ $\Leftrightarrow {x^2} + x \le 0$ $\Leftrightarrow – 1 \le x \le 0.$

Vậy hàm số nghịch biến trên $[ – 1;0].$

Lựa chọn đáp án bằng phép thử: Nhận xét rằng:

+ Hàm số nghịch biến khi $y’ \le 0$ do đó sẽ có hai nửa đoạn (dấu ngoặc vuông) nên đáp án D bị loại.

+ Hàm đa thức bậc ba với $a>0$ nghịch biến trên đoạn nằm giữa hai nghiệm của phương trình $y’ = 0$ nên các đáp án A và B bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

**Chú ý**: Như vậy, để lựa chọn được đáp án đúng bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất của hàm đa thức bậc ba và dấu tam thức bậc hai.

<!-- chunk:5 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 5. Hàm số $y = \frac{1}{4}{x^4} – \frac{1}{2}{x^2} – 1$ đồng biến trên các khoảng:

A. $( – \infty ;1]$ và $[1; + \infty ).$

B. $[ – 1;0]$ và $[1; + \infty ).$

C. $( – \infty ; – 1]$ và $[0;1].$

D. $[ – 1;1].$

Chọn B.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định $D=R.$

+ Đạo hàm: $y’ = {x^3} – x$, $y’ = 0$ $\Leftrightarrow {x^3} – x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so-1.png" alt="">

Từ đó suy ra hàm số đồng biến trên $[ – 1;0]$ và $[1; + \infty ).$

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định $D=R.$

+ Đạo hàm: $y’ = {x^3} – x$, $y’ \ge 0$ $\Leftrightarrow {x^3} – x \ge 0$ $\Leftrightarrow x \in [ – 1;0) \cup [1; + \infty ).$

Dựa trên việc xét dấu bằng cách vẽ trục số như sau:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so-2.png" alt="">

Từ đó, suy ra hàm số đồng biến trên $[ – 1;0]$ và $[1; + \infty ).$

Lựa chọn đáp án đúng bằng phép thử: Nhận xét rằng hàm đa thức bậc bốn dạng trùng phương với $a>0$ thì:

+ Có khoảng đồng biến chứa $+ \infty$ nên các đáp án C và D bị loại.

+ Có khoảng đồng biến chứa $– \infty$ nên các đáp án A bị loại.

Do đó việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy, để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thay vì thiết lập điều kiện $y’ \ge 0$ chúng ta đi giải phương trình $y’ = 0$ rồi lập bảng biến thiên cho trực quan (bởi việc giải bất phương trình bậc ba dễ gây nhầm dấu).

+ Trong cách giải tự luận 2 chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm của hàm số.

Bước 2: Thiết lập điều kiện $y’ \ge 0$ chúng ta đi xác định được nghiệm của bất phương trình bằng việc xét dấu ngay trên trục số (miền ngoài cùng dấu hệ số $a$ và sau đó đan dấu).

+ Trong cách lựa chọn đáp án bằng phép thử, các em học sinh cần nắm vững kiến thức về tính chất của hàm bậc bốn dạng trùng phương.

<!-- chunk:6 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 6. Hàm số $y = {x^4} – 2{x^2} – 5$ nghịch biến trên các khoảng:

A. $( – \infty ; – 1]$ và $[1; + \infty ).$

B. $( – \infty ; – 1]$ và $[0;1].$

C. $[ – 1;0]$ và $[1; + \infty ).$

D. $[ – 1;1].$

Chọn B.
Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định $D=R.$

+ Đạo hàm: $y’ = 4{x^3} – 4x$, $y’ = 0$ $\Leftrightarrow 4{x^3} – 4x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so-3.png" alt="">

Từ đó suy ra hàm số nghịch biến trên $( – \infty ; – 1]$ và $[0;1].$

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định $D=R.$

+ Đạo hàm: $y’ = {x^3} – x$, $y’ \le 0$ $\Leftrightarrow {x^3} – x \le 0$ $\Leftrightarrow x \in ( – \infty ; – 1] \cup [0;1].$

Dựa trên việc xét dấu bằng cách vẽ trục số như sau:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so-4.png" alt="">

Từ đó suy ra hàm số nghịch biến trên $( – \infty ; – 1]$ và $[0;1].$

Lựa chọn đáp án đúng bằng phép thử: Nhận xét rằng hàm đa thức bậc bốn dạng trùng phương với $a>0$ thì:

+ Có khoảng nghịch biến chứa $– \infty$ nên các đáp án C và D bị loại.

+ Có khoảng nghịch biến không chứa $+ \infty$ nên các đáp án A bị loại.

Do đó việc lựa chọn đáp án B là đúng đắn.

<!-- chunk:7 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 7. Hàm số $y = \frac{{2x}}{{x – 2}}$ nghịch biến trên khoảng:

A. $( – \infty ;1].$

B. $[1; + \infty ].$

C. $R\backslash \{ 1\} .$

D. $R.$

Chọn C.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{ – 2}}{{{{(x – 1)}^2}}} < 0$ suy ra hàm số nghịch biến trên $D.$

Vậy hàm số nghịch biến trên $R\backslash \{ 1\} .$

** Lựa chọn đáp án đúng bằng phép thử**: Nhận xét rằng hàm phân thức bậc nhất trên bậc nhất luôn đơn điệu (luôn đồng biến hoặc luôn nghịch biến) trên tập xác định của nó, do đó ta lựa chọn ngay đáp án C cho bài toán.

**Chú ý**: Như vậy, để lựa chọn được đáp án đúng bằng phép thử các em học sinh cần nắm vững kiến thức về tinh chất của hàm phân thức bậc nhất trên bậc nhất.

<!-- chunk:8 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 8. Hàm số $y = \frac{{x – 1}}{{x + 1}}$ đồng biến trên khoảng:

A. $( – \infty ; – 1].$

B. $[ – 1; + \infty ).$

C. $( – \infty ; – 1)$ và $( – 1; + \infty ).$

D. $R.$

Chọn C.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ – 1\} .$

+ Đạo hàm $y’ = \frac{2}{{{{(x + 1)}^2}}} > 0$, $\forall x \ne – 1$ suy ra hàm số đồng biến trên từng khoảng của tập xác định $D.$

Vậy hàm số đồng biến trên $( – \infty ; – 1)$ và $( – 1; + \infty ).$

**Lựa chọn đáp án bằng phép thử**: Nhận xét rằng hàm phân thức bậc nhất trên bậc nhất luôn đơn điệu (luôn đồng biến hoặc luôn nghịch biến) trên tập xác định của nó, do đó ta lựa chọn ngay đáp án C cho bài toán.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 9. Hàm số $y = \frac{{{x^2}}}{{x – 1}}$ nghịch biến trên các khoảng (nửa khoảng):

A. $( – \infty ;1)$ và $(1;2].$

B. $( – \infty ;1)$ và $[2; + \infty ).$

C. $(0;1)$ và $(1;2).$

D. $( – \infty ;1)$ và $(1; + \infty ).$

Chọn C.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm $y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}} > 0$, $\forall x \ne 1.$

+ Hàm số nghịch biến khi $y’ < 0$ $\Leftrightarrow {x^2} – 2x < 0$ $\Leftrightarrow 0 < x < 2.$

Vậy hàm số nghịch biến trên các nửa khoảng $(0;1)$ và $(1;2).$

Lựa chọn đáp án bằng phép thử 1: Ta lần lượt đánh giá:

+ Vì $D = R\backslash \{ 1\}$ và với hàm phân thức bậc hai trên bậc nhất thì $y’ = 0$ hoặc vô nghiệm hoặc có hai nghiệm phân biệt đối xứng qua điểm $I.$ Do đó, các đáp án A và B bị loại. Tới đây ta chỉ còn phải lựa chọn C hoặc D.

+ Lấy $x=2$ và $x=3$ suy ra $y(2) = 4$ và $y(3) = \frac{9}{2}$, tức là hàm số đồng biến trên $[2;3]$, suy ra đáp án D bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

Lựa chọn đáp án bằng phép thử 2: Với hàm phân thức bậc hai trên bậc nhất có $ad<0$ thì điều kiện $y’ \le 0$ tương đương với $A{x^2} + Bx + C \le 0$ (với $A>0$). Suy ra, chúng ta chỉ có thể nhận được $[a;b]$ (với $a+b =2$).

Do đó việc lựa chọn đáp án C là đúng đắn.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 10. Hàm số $y = x – \frac{2}{x}$ đồng biến trên:

A. $[2;3].$

B. $[2;3]\backslash \{ 0\} .$

C. $R\backslash ( – 2;2).$

D. $( – \infty ;0)$ và $(0; + \infty ).$

Chọn D.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 0\} .$

+ Đạo hàm $y’ = 1 + \frac{2}{{{x^2}}} > 0$, $\forall x \ne 0$, suy ra hàm số đồng biến trên từng khoảng của tập xác định.

Vậy hàm số đồng biến trên $( – \infty ;0)$ và $(0; + \infty ).$

Lựa chọn đáp án bằng phép thử: Ta lần lượt đánh giá:

+ Vì $D = R\backslash \{ 0\}$ và với hàm phân thức bậc hai trên bậc nhất thì $y’ = 0$ hoặc vô nghiệm hoặc có hai nghiệm phân biệt đối xứng qua điểm $0.$ Do đó, các đáp án A và B bị loại. Tới đây ta chỉ còn phải lựa chọn C hoặc D.

+ Lấy $x=1$ và $x=2$ suy ra $y(1) = – 1$ và $y(2) = 1$, tức là hàm số đồng biến trên $[1;2]$, suy ra đáp án C bị loại.

Do đó, việc lựa chọn đáp án D là đúng đắn.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 11. Hàm số $y = \sqrt {2 + x – {x^2}}$ nghịch biến trên:

A. $\left[ {\frac{1}{2};2} \right].$

B. $\left[ { – 1;\frac{1}{2}} \right].$

C. $[2; + \infty ).$

D. $[ – 1;2].$

Chọn A.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = [ – 1;2].$

+ Đạo hàm $y’ = \frac{{1 – 2x}}{{2\sqrt {2 + x – {x^2}} }}$, $\forall x \in ( – 1;2).$

+ Hàm số nghịch biến khi $y’ \le 0$ $\Leftrightarrow 1 – 2x \le 0$ $\Leftrightarrow x \ge \frac{1}{2}.$

Vậy hàm số nghịch biến trên $\left[ {\frac{1}{2};2} \right].$

Lựa chọn đáp án bằng phép thử 1: Ta lần lượt đánh giá:

+ Tìm tập xác định của hàm số được $D = [ – 1;2]$, suy ra các đáp án C và D là sai.

+ Xuất phát từ tính chất của hàm số $y = a{x^2} + bx + c$ (với $a<0$) nghịch biến trên $\left[ { – \frac{b}{{2a}}; + \infty } \right)$, suy ra đáp án B không thỏa mãn.

Do đó, việc lựa chọn đáp án A là đúng đắn.

Lựa chọn đáp án bằng phép thử 2: Xuất phát từ tính chất của hàm số $y = – {x^2} + x + 2$ nghịch biến trên $\left[ {\frac{1}{2}; + \infty } \right).$ Suy ra các đáp án B, C, D không thỏa mãn.

Do đó, việc lựa chọn đáp án A là đúng đắn.

<!-- chunk:12 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 12. Hàm số $y = x – \sqrt x$ đồng biến trên:

A. $\left( { – \infty ;\frac{1}{4}} \right].$

B. $\left[ {\frac{1}{4}; + \infty } \right).$

C. $\left[ {0;\frac{1}{4}} \right].$

D. $( – \infty ;0].$

Chọn B.

Lời giải tự luận: Ta có điều kiện $x \ge 0$ $\Rightarrow D = [0; + \infty ).$

+ Đạo hàm $y’ = 1 – \frac{1}{{2\sqrt x }}$, $\forall x \ne 0$; $y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{2\sqrt x }} = 0$ $\Leftrightarrow x = \frac{1}{4}.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so-5.png" alt="">

Vậy hàm số đồng biến trên $\left[ {\frac{1}{4}; + \infty } \right).$

Lựa chọn đáp án bằng phép thử: Ta lần lượt đánh giá:

+ Vì tập xác định $D = [0; + \infty )$ nên các đáp án A và D bị loại. Tới đây ta chỉ còn phải lựa chọn B hoặc C.

+ Lấy $x = \frac{1}{4}$ và $x=1$ suy ra $y\left( {\frac{1}{4}} \right) = – \frac{1}{4}$ và $y(1) = 0$, tức là hàm số đồng biến trên $\left( {\frac{1}{4};1} \right)$, suy ra đáp án C bị loại.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 13. Cho hàm số $y = \frac{1}{3}{x^3} + a{x^2} + 4x + 3.$ Hàm số đồng biến trên $R$ khi và chỉ khi:

A. $|a| \le 1.$

B. $|a| \ge 1.$

C. $|a| \le 2.$

D. $|a| \le 2.$

Chọn D.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm $y’ = {x^2} + 2ax + 4.$

+ Để hàm số đồng biến trên $R$ điều kiện là:

$y’ \ge 0$, $\forall x \in R$ $\Leftrightarrow f(x) = {x^2} + 2ax + 4 \ge 0$, $\forall x \in R$ $\Leftrightarrow {a^2} – 4 \le 0$ $\Leftrightarrow |a| \le 2.$

Vậy với $|a| \le 2$ thỏa mãn điều kiện đề bài.

Lựa chọn đáp án bằng phép thử kết hợp tự luận: Ta có:

+ Tập xác định $D = R.$

+ Đạo hàm $y’ = {x^2} + 2ax + 4.$

Khi đó:

+ Với $a=-2$ thì $y’ = {x^2} – 4x + 4$ $= {(x – 2)^2} \ge 0$, $\forall x \in R$, do đó các đáp án A và B bị loại (vì chúng không chứa giá trị $a=-2$).

+ Với $a=-3$ thì $y’ = {x^2} – 6x + 4$ không thể không âm với mọi $x \in R$, do đó đáp án C bị loại.

Do đó việc lựa chọn đáp án D là đúng đắn.

<!-- chunk:14 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 14. Cho hàm số $y = ax – {x^3}.$ Hàm số nghịch biến trên $R$ khi và chỉ khi:

A. $a \le 0.$

B. $a \ge 1.$

C. $a \le 2.$

D. $0 \le a \le 2.$

Chọn A.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm $y’ = a – 3{x^2}.$

+ Để hàm số nghịch biến trên $R$ điều kiện là:

$y’ \le 0$, $\forall x \in R$ $\Leftrightarrow a – 3{x^2} \le 0$, $\forall x \in R$ $\Leftrightarrow a \le 3{x^2}$ $\Leftrightarrow a \le 0.$

Vậy với $a \le 0$ thỏa mãn điều kiện đề bài.

Lựa chọn đáp án bằng phép thử: Ta có với $a=1$ thì $y’ = 1 – 3{x^2}$ không thể không dương với mọi $x \in R$ do đó các đáp án B, C và D bị loại (vì chúng chứa giá trị $a=1$).

Do đó việc lựa chọn đáp án A là đúng đắn.

<!-- chunk:15 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-tinh-don-dieu-cua-ham-so.html -->
## Bài tập 15. Cho hàm số $y = \frac{{mx – 2}}{{x – 1}}.$ Hàm số nghịch biến trên từng khoảng của tập xác định của nó khi và chỉ khi:

A. $m \le 4.$

B. $m > 2.$

C. $m \ge 2.$

D. $m < 4.$

Chọn B.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm $y’ = \frac{{2 – m}}{{{{(x – 1)}^2}}}$, $\forall x \ne 1.$

+ Để hàm số nghịch biến trên từng khoảng của tập xác định điều kiện là: $y’ \le 0$, $\forall x \in R\backslash \{ 1\}$ và dấu đẳng thức chỉ xảy ra tại một số hữu hạn điểm.

$\Leftrightarrow 2 – m < 0$ $\Leftrightarrow m > 2.$

Vậy với $m>2$ thỏa mãn điều kiện đề bài.

Lựa chọn đáp án bằng phép thử kết hợp tự luận: Ta có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm $y’ = \frac{{2 – m}}{{{{(x – 1)}^2}}}$, $\forall x \ne 1.$

Khi đó:

+ Với $m=0$ thì $y’ = \frac{2}{{{{(x – 1)}^2}}} > 0$, suy ra hàm số đồng biến trên từng khoảng của tập xác định.

Suy ra các đáp án A và D bị loại (vì nó chứa giá trị $m=0$).

+ Với $m=2$ thì $y’ = 0$, suy ra hàm số là hàm hằng, nên đáp án C bị loại.

Do đó, việc lựa chọn đáp án B là đúng đắn.

Chú ý: Rất nhiều học sinh khi thực hiện bài toán trên dưới dạng tự luận đã đưa ra kết luận $m \ge 2.$