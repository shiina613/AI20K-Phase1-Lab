# Phương pháp giải nhanh trắc nghiệm cực trị của hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
Bài viết hướng dẫn phương pháp giải nhanh một số bài toán trắc nghiệm cực trị của hàm số (Giải tích 12) bằng cách sử dụng phép thử và sự hỗ trợ của máy tính cầm tay Casio – Vinacal.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## A. KIẾN THỨC CẦN GHI NHỚ
1. Khái niệm cực trị của hàm số

Định nghĩa: Cho hàm số $y = f(x)$ xác định trên tập hợp $D$ $(D \subset R)$ và ${x_0} \in D.$

a) ${x_0}$ gọi là một điểm cực đại của hàm số $y = f(x)$ nếu tồn tại một khoảng $(a;b)$ chứa điểm ${x_0}$ sao cho $(a;b) \subset D$ và $f(x) < f\left( {{x_0}} \right)$, $\forall x \in (a;b)\backslash \left\{ {{x_0}} \right\}.$

Khi đó $f\left( {{x_0}} \right)$ được gọi là giá trị cực đại của hàm số $f(x).$

b) ${x_0}$ gọi là một điểm cực tiểu của hàm số $y = f(x)$ nếu tồn tại một khoảng $(a;b)$ chứa điểm ${x_0}$ sao cho $(a;b) \subset D$ và $f(x) > f\left( {{x_0}} \right)$, $\forall x \in (a;b)\backslash \left\{ {{x_0}} \right\}.$

Khi đó $f\left( {{x_0}} \right)$ được gọi là giá trị cực tiểu của hàm số $f(x).$

Giá trị cực đại và giá trị cực tiểu được gọi chung là cực trị.

2. Điều kiện cần để hàm số có cực trị

Xét hàm số $y = f(x)$ liên tục trên khoảng $(a;b)$ và ${x_0} \in (a;b).$

Định lí 1: Giả sử hàm số $y = f(x)$ đạt cực trị tại điểm ${x_0}.$ Khi đó, nếu $f(x)$ có đạo hàm tại điểm ${x_0}$ thì $f’\left( {{x_0}} \right) = 0.$

3. Điều kiện đủ để hàm số có cực trị

Định lí 2: Giả sử hàm số $y = f(x)$ liên tục trên khoảng $(a;b)$ chứa điểm ${x_0}$ và có đạo hàm trên các khoảng $\left( {a;{x_0}} \right)$ và $\left( {{x_0};b} \right).$ Khi đó:

a) Nếu $f’\left( {{x_0}} \right) < 0$ với mọi $x \in \left( {a;{x_0}} \right)$ và $f’\left( {{x_0}} \right) > 0$ với mọi $x \in \left( {{x_0};b} \right)$ thì hàm số $f(x)$ đạt cực tiểu tại điểm ${x_0}.$

b) Nếu $f’\left( {{x_0}} \right) > 0$ với mọi $x \in \left( {a;{x_0}} \right)$ và $f’\left( {{x_0}} \right) < 0$ với mọi $x \in \left( {{x_0};b} \right)$ thì hàm số $f(x)$ đạt cực đại tại điểm ${x_0}.$

Nói một cách vắn tắt: Nếu khi $x$ qua ${x_0}$, đạo hàm đổi dấu thì điểm ${x_0}$ là một điểm cực trị của hàm số.

Từ định lí 2 ta có quy tắc tìm cực trị sau đây:

Quy tắc 1: Để tìm cực trị của hàm số $y = f(x)$ ta thực hiện theo các bước:

+ Bước 1: Tính $f'(x).$

+ Bước 2: Tìm các điểm ${x_i}$ $(i = 1;2 \ldots )$ tại đó đạo hàm của hàm số bằng $0$ hoặc hàm số liên tục nhưng không có đạo hàm.

+ Bước 3: Xét dấu $f'(x).$ Nếu $f'(x)$ đổi dấu khi x qua điểm ${x_i}$ thì hàm số đạt cực trị tại ${x_i}.$

Định lí 3: Giả sử hàm số $y = f(x)$ có đạo hàm cấp một trên khoảng $(a;b)$ chứa điểm ${x_0}$, $f’\left( {{x_0}} \right) = 0$ và $f(x)$ có đạo hàm cấp hai khác $0$ tại điểm ${x_0}.$

a) $f”\left( {{x_0}} \right) < 0$ thì hàm số đạt cực đại tại điểm ${x_0}.$

b. Nếu $f”\left( {{x_0}} \right) > 0$ thì hàm số đạt cực tiểu tại điểm ${x_0}.$

Từ định lí 3 ta có quy tắc tìm cực trị sau đây:

Quy tắc 2: Để tìm cực trị của hàm số $y = f(x)$ ta thực hiện theo các bước:

+ Bước 1: Tính $f'(x).$

+ Bước 2: Tìm các nghiệm ${x_i}$ $(i = 1;2 \ldots .)$ của phương trình $f'(x) = 0.$

+ Bước 3: Với mỗi $i$ ta tính $f”\left( {{x_i}} \right)$, khi đó:

Nếu $f”\left( {{x_i}} \right) < 0$ thì hàm số đạt cực đại tại điểm ${x_i}.$

Nếu $f”\left( {{x_i}} \right) > 0$ thì hàm số đạt cực tiểu tại điểm ${x_i}.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Không có cực trị.

Chọn A.
Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 3{x^2} + 12x + 9.$

$y’ = 0$ $\Leftrightarrow 3{x^2} + 12x + 9 = 0$ $\Leftrightarrow x = – 1$ hoặc $x = – 3.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-1.png" alt="">

Vậy hàm số có một cực đại và một cực tiểu.

Lựa chọn đáp án bằng phép thử: Ta có đánh giá:

Hàm đa thức bậc ba chỉ có thể xảy ra một trong hai trường hợp:

+ Không có cực trị.

+ Một cực đại và một cực tiểu.

Suy ra các đáp án B và C bị loại.

Tính nhanh $y’$ nhận thấy phương trình $y’=0$ có hai nghiệm phân biệt.

Do đó, việc lựa chọn đáp án A là đúng đắn.

**Nhận xét**: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta sử dụng quy tắc 1 để giải.

+ Trong cách lựa chọn đáp án bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất cực trị của hàm đa thức bậc ba.

<!-- chunk:3 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Một cực đại và một cực tiểu.

Chọn A.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 4{x^3} – 16x$, $y’ = 0$ $\Leftrightarrow 4{x^3} – 16x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 2}
\end{array}} \right..
$$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-2.png" alt="">

Vậy hàm số có một cực đại và hai cực tiểu.

Lựa chọn đáp án bằng phép thử: Nhận xét rằng hàm trùng phương với $a>0$ chỉ có thể xảy ra một trong hai trường hợp:

+ Một cực tiểu.

+ Một cực đại và hai cực tiểu.

Do đó việc lựa chọn đáp án A là đúng đắn.

Nhận xét: Như vậy để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta sử dụng quy tắc 1 để giải. Chú ý rằng, để nhanh chóng lựa chọn được đáp án đúng chúng ta thường thực hiện trích lược tự luận, tức là không cần thiết phải tính các giá trị cực trị mà chỉ cần dựa vào bảng xét dấu của $y’$ để chỉ ra được đáp án đúng.

+ Trong cách lựa chọn đáp án bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất cực trị của hàm đa thức bậc bốn dạng trùng phương.

<!-- chunk:4 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Một cực tiểu và không có cực đại.

Chọn D.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = 4{x^3} + 4x$, $y’ = 0$ $\Leftrightarrow x\left( {{x^2} + 1} \right) = 0$ $\Leftrightarrow x = 0.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-3.png" alt="">

Vậy hàm số có một cực tiểu và không có cực đại.

Lựa chọn đáp án bằng phép thử: Nhận xét rằng hàm trùng phương với $a>0$ chỉ có thể xảy ra một trong hai trường hợp:

+ Một cực tiểu.

+ Một cực đại và hai cực tiểu.

Suy ra các đáp án B và C bị loại.

Ta có $y’ = 4{x^3} + 4x$, $y’ = 0$ $\Leftrightarrow x\left( {{x^2} + 1} \right) = 0$ $\Leftrightarrow x = 0.$

Tức là hàm số chỉ có một cực trị nên đáp án A bị loại.

Do đó việc lựa chọn đáp án D là đúng đắn.

<!-- chunk:5 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Không có cực trị.

Chọn D.

Lời giải tự luận:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = – \frac{2}{{{{(x – 1)}^2}}} < 0$, $\forall x \in D$ $\Rightarrow$ Hàm số không có cực trị.

**Lựa chọn đáp án bằng phép thử**: Nhận xét rằng hàm phân thức bậc nhất trên bậc nhất không có cực trị nên ta thấy ngay việc lựa chọn đáp án D là đúng đắn.

**Nhận xét**: Như vậy để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta sử dụng quy tắc 1 để giải.

+ Trong cách lựa chọn đáp án bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất cực trị của hàm phân thức bậc nhất trên bậc nhất.

<!-- chunk:6 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Không có cực trị.

Chọn C.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 0\} .$

+ Đạo hàm: $y’ = 1 – \frac{1}{{{x^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{{x^2}}} = 0$ $\Leftrightarrow x = \pm 1.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-4.png" alt="">

Vậy hàm số có một cực đại và một cực tiểu.

Lựa chọn đáp án bằng phép thử: Nhận xét rằng hàm phân thức bậc hai trên bậc nhất chỉ có thể xảy ra một trong hai trường hợp:

+ Không có cực trị.

+ Một cực đại và một cực tiểu (hai cực trị).

Suy ra các đáp án A và B bị loại.

Ta có: $y’ = 1 – \frac{1}{{{x^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{{x^2}}} = 0$ $\Leftrightarrow x = \pm 1.$

Tức là hàm số có hai cực trị nên đáp án D bị loại.

Do đó việc lựa chọn đáp án C là đúng đắn.

Nhận xét: Như vậy để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta sử dụng quy tắc 1 để giải. Chú ý rằng, để nhanh chóng lựa chọn được đáp án đúng chúng ta thường thực hiện trích lược tự luận kết hợp với tính chất của hàm phân thức bậc hai trên bậc nhất, tức là không cần thiết phải lập bảng biến thiên mà chỉ cần dựa vào số nghiệm của $y’$ để chỉ ra được đáp án đúng.

+  Trong cách lựa chọn đáp án bằng phép thử các em học sinh cần nắm vững kiến thức về tính chất cực trị của hàm phân thức bậc hai trên bậc nhất.

<!-- chunk:7 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Hai cực trị và hoành độ cực tiểu lớn hơn hoành độ cực đại.

Chọn C.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-5.png" alt="">

Vậy hàm số có hai cực trị và hoành độ cực tiểu lớn hơn hoành độ cực đại.

Lựa chọn đáp án bằng phép đánh giá: Ta có:

$y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right.
$$
 $\Rightarrow$ Hàm số có hai cực trị.

Mặt khác: $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$ $\Rightarrow$ Hàm số đạt cực tiểu tại $x=2$ (đạt cực đại tại $x=0$).

Do đó việc lựa chọn đáp án C là đúng đắn.

Nhận xét: Như vậy để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta sử dụng quy tắc 1 để giải.

+ Trong cách lựa chọn đáp án bằng pháp đánh giá một vài em học sinh nếu cảm thấy khó hiểu thì hãy xem cách giải thích như sau:

Chúng ta thực hiện theo hai bước:

Bước 1: Tính đạo hàm để khẳng định hàm số có cực trị.

Bước 2: Nhận xét rằng: $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

Suy ra qua $x=2$ hàm số có hướng đi lên, tức là có dáng:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-6.png" alt="">

Hàm số đạt cực tiểu tại $x=2$ (đạt cực đại tại $x=0$).

Do đó việc lựa chọn đáp án C là đúng đắn.

<!-- chunk:8 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Một cực tiểu và không có cực đại.

Chọn A.

Lời giải tự luận: Ta lần lượt có:

+ Ta có điều kiện: $4 – {x^2} \ge 0$ $\Leftrightarrow |x| \le 2$ $\Rightarrow$ Tập xác định $D = [ – 2;2].$

+ Đạo hàm: $y’ = \frac{{4 – 2{x^2}}}{{\sqrt {4 – {x^2}} }}$ $y’ = 0$ $\Leftrightarrow 4 – 2{x^2} = 0$ $\Leftrightarrow x = \pm \sqrt 2 \in D.$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-7.png" alt="">

Từ đó suy ra hàm số có một cực đại và một cực tiểu.

Lời giải tự luận nhanh: Ta lần lượt có:

+ Điều kiện: $4 – {x^2} \ge 0$ $\Leftrightarrow |x| \le 2$ $\Rightarrow D = [ – 2;2].$

+ Đạo hàm: $y’ = \frac{{4 – 2{x^2}}}{{\sqrt {4 – {x^2}} }}.$

Từ đó suy ra phương trình $y’= 0$ (có dạng ${4 – 2{x^2} = 0}$) luôn có hai nghiệm phân biệt thuộc tập $D$ và đổi dấu qua chúng. Suy ra, hàm số có một cực đại và một cực tiểu.

Do đó việc lựa chọn đáp án A là đúng đắn.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 8. Cho hàm số $y = \frac{1}{3}{x^3} + \frac{1}{2}{x^2} + 5.$ Tổng các hoành độ cực đại và cực tiểu của hàm số bằng:

A. $-2.$

B. $-1.$

C. $0.$

D. $\frac{1}{2}.$

Chọn B.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = {x^2} + x$, $y’ = 0$ $\Leftrightarrow {x^2} + x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = 0}\\
{{x_2} = – 1}
\end{array}} \right.
$$
 $\Rightarrow {x_1} + {x_2} = – 1.$

Do đó việc lựa chọn đáp án B là đúng đắn.

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = {x^2} + x$, $y’ = 0$ $\Leftrightarrow {x^2} + x = 0$ $\Rightarrow {x_1} + {x_2} = – \frac{b}{a} = – 1.$

Do đó việc lựa chọn đáp án B là đúng đắn.

Lời giải tự luận dựa trên tính chất: Ta lần lượt có:

+ Tập xác định $D = R.$

+ Đạo hàm: $y’ = {x^2} + x$, $y” = 2x + 1.$

$y” = 0$ $\Leftrightarrow 2x + 1 = 0$ $\Leftrightarrow {x_0} = – \frac{1}{2}$ $\Rightarrow {x_1} + {x_2} = 2{x_0} = – 1.$

Do đó việc lựa chọn đáp án B là đúng đắn.

Lời giải trích lược tự luận dựa trên tính chất: Ta lần lượt có:

+ Hàm đa thức bậc ba $y = a{x^3} + b{x^2} + cx + d$ có hoành độ điểm uốn là:

${x_0} = – \frac{b}{{3a}}$ $\Rightarrow {x_0} = – \frac{1}{2}.$

+ Khi đó, tổng các hoành độ cực đại và cực tiểu của hàm số là: ${x_1} + {x_2} = 2{x_0} = – 1.$

Do đó việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy để lựa chọn đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta tìm hai nghiệm của phương trình $y’ = 0$ rồi tính tổng hai nghiệm đó.

+ Trong cách giải tự luận 2 chúng ta tìm tổng hai nghiệm của phương trình $y’=0$ bằng định lí Vi-ét và cách giải này tỏ ra hiệu quả hơn trong trường hợp hai nghiệm của phương trình $y’= 0$ lẻ.

+ Trong cách giải tự luận dựa trên tinh chất, các em học sinh cần biết được tính chất đối xứng của các điểm cực đại và cực tiểu (nếu có) của hàm đa thức bậc ba qua điểm uốn. Như vậy, nếu bài toán yêu cầu “Tính tổng các giá trị cực đại và cực tiểu của hàm số” thì ngoài cách giải tự luận thông thường chúng ta có thể thực hiện như sau:

Tập xác định: $D= R.$

Đạo hàm: $y’ = {x^2} + x$, $y” = 2x + 1$, $y” = 0$ $\Leftrightarrow 2x + 1 = 0$ $\Leftrightarrow {x_U} = – \frac{1}{2}.$

$\Rightarrow {y_{CD}} + {y_{CT}}$ $= 2{y_U}$ $= 2y\left( { – \frac{1}{2}} \right)$ $= \frac{{61}}{{12}}.$

+ Trong cách giải trích lược tự luận dựa trên tính chất các em học sinh cần biết được mọi hàm đa thức bậc ba $y = a{x^3} + b{x^2} + cx + d$ luôn có hoành độ điểm uốn là ${x_U} = – \frac{b}{{3a}}$ và tính chất đối xứng của các điểm cực đại và cực tiểu (nếu có) của hàm số qua điểm uốn.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 9. Cho hàm số $y = x – 1 + \frac{2}{x}.$ Tổng các hoành độ cực đại và cực tiểu của hàm số bằng:

A. $– \frac{3}{2}.$

B. $-1.$

C. $0.$

D. $\frac{3}{2}.$

Chọn C.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 0\} .$

+ Đạo hàm: $y’ = 1 – \frac{2}{{{x^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{2}{{{x^2}}} = 0$ $\Leftrightarrow {x^2} – 2 = 0$ $\Leftrightarrow {x_{1,2}} = \pm \sqrt 2$ $\Rightarrow {x_1} + {x_2} = 0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 0\} .$

+ Đạo hàm: $y’ = 1 – \frac{2}{{{x^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{2}{{{x^2}}} = 0$ $\Leftrightarrow {x^2} – 2 = 0$ $\Rightarrow {x_1} + {x_2} = 0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Lời giải tự luận dựa trên tính chất: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 0\} .$

+ Tiệm cận đứng $x=0$, suy ra ${x_1} + {x_2} = 2.0 = 0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Lựa chọn đáp án bằng trích lược tự luận dựa trên tính chất: Ta có hoành độ tâm đối xứng:

${x_I} = 0$ $\Rightarrow {x_1} + {x_2} = 2{x_I} = 0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta tìm hai nghiệm của phương trình $y’=0$ rồi tính tổng hai nghiệm đó.

+ Trong cách giải tự luận 2 chúng ta tìm tổng hai nghiệm của phương trình $y’=0$ bằng định lí Vi-ét và cách giải này tỏ ra hiệu quả hơn trong trường hợp hai nghiệm của phương trình $y’ = 0$ lẻ.

+ Trong cách giải tự luận dựa trên tính chất các em học sinh cần biết được tính chất đối xứng của các điểm cực đại và cực tiểu (nếu có) của hàm phân thức bậc hai trên bậc nhất qua tâm đối xứng (là giao điểm của hai đường tiệm cận). Như vậy, nếu bài toán yêu cầu “Tính tổng các giá trị cực địa và cực tiểu của hàm số” thì ngoài cách giải tự luận thông thường chúng ta có thể thực hiện như sau:

Tập xác định: $D = R\backslash \{ 0\} .$

Tiệm cận đứng $x=0$; tiệm cận xiên $y=x+1$, suy ra tâm đối xứng $I(0;1)$, từ đó ta được ${y_{CĐ}} + {y_{CT}} = 2.1 = 2.$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 10. Cho hàm số $y = \frac{{{x^2} – 2x + 1}}{{x – 2}}.$ Hàm số có hai điểm cực trị ${x_1}$, ${x_2}$, tích ${x_1}.{x_2}$ bằng:

A. $-3.$

B. $-2.$

C. $2.$

D. $3.$

Chọn D.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 2\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 4x + 3}}{{{{(x – 2)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 4x + 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = 1}\\
{{x_2} = 3}
\end{array}} \right.
$$
 $\Rightarrow {x_1}{x_2} = 1.3 = 3.$

Do đó việc lựa chọn đáp án D là đúng đắn.

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 2\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 4x + 3}}{{{{(x – 2)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 4x + 3 = 0$ $\Rightarrow {x_1}.{x_2} = \frac{c}{a} = 3.$

Do đó việc lựa chọn đáp án D là đúng đắn.

Nhận xét: Để tăng độ khó cho dạng toán này thông thường người ta đặt ra yêu cầu tính một biểu thức đối xứng phức tạp hơn giữa các nghiệm ${x_1}$ và ${x_2}.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 11. Cho hàm số $y = {x^4} – 8{x^2} + 3.$ Hàm số có ba điểm cực trị ${x_1}$, ${x_2}$, ${x_3}.$ Tích ${x_1}{x_2}{x_3}$ bằng:

A. $-2.$

B. $-1.$

C. $0.$

D. $1.$

Chọn C.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = 4{x^3} – 16x$, $y’ = 0$ $\Leftrightarrow 4{x^3} – 16x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = 0}\\
{{x_{2,3}} = \pm 2}
\end{array}} \right.
$$
 $\Rightarrow {x_1}{x_2}{x_3} = 0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = 4{x^3} – 16x$, $y’ = 0$ $\Leftrightarrow 4{x^3} – 16x = 0$ $(1).$

Vì ${x_1}$, ${x_2}$, ${x_3}$ là nghiệm của phương trình $(1)$ nên theo định lí Vi-ét ta có:

${x_1}{x_2}{x_3} = – \frac{d}{a} = 0.$

Vậy ta luôn có ${x_1}{x_2}{x_3} = 0.$

Lựa chọn đáp án bằng phép thử: Nhận xét rằng hàm trùng phương (là hàm số chẵn) luôn có một hoành độ cực trị bằng $0$, nên tích các hoành độ cực trị luôn bằng $0.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta tìm ba nghiệm của phương trình $y’ = 0$ rồi tính tích các nghiệm đó.

+ Trong cách giải tự luận 2 chúng ta tìm tích ba nghiệm của phương trình $y’=0$ bằng định lí Vi-ét.

+ Trong cách giải lựa chọn đáp án bằng phép thử các em học sinh cần nhớ rằng với hàm trùng phương $y = a{x^4} + b{x^2} + c$ $(a \ne 0)$ luôn có một điểm cực trị là $(0;c)$, do đó ${x_1}{x_2}{x_3} = 0.$ Ngoài ra, ta cũng luôn có ${x_1} + {x_2} + {x_3}$ $= {x_1} + {x_3} = 0$, ${x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1}$ $= {x_3}{x_1} = – \frac{{3b}}{{4a}}.$

<!-- chunk:13 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 12. Cho hàm số $y = {x^3} – 3{x^2} – 24x + 1.$ Tích các giá trị cực đại và cực tiểu của hàm số bằng:

A. $-2921.$

B. $-2291.$

C. $-2912.$

D. $-2192.$

Chọn B.

Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = 3{x^2} – 6x – 24$, $y’ = 0$ $\Leftrightarrow 3{x^2} – 6x – 24 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 4}\\
{x = – 2}
\end{array}} \right..
$$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số bằng:

${y_{CĐ}}.{y_{CT}}$ $= y(4).y( – 2)$ $= – 2291.$

Do đó việc lựa chọn đáp án C là đúng đắn.

Lời giải tự luận kết hợp với máy tính CASIO fx – 570MS: Ta có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = 3{x^2} – 6x – 24$, $y’ = 0$ $\Leftrightarrow 3{x^2} – 6x – 24 = 0.$

+ Giải nhanh phương trình $y’=0$ bằng cách ấn:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-8.png" alt="">

+ Nhập hàm số ta ấn:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-9.png" alt="">

+ Khi đó, ta lần lượt với các giá trị $x=4$ và $x=-2:$

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-10.png" alt="">

Do đó, việc lựa chọn đáp án B là đúng đắn.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên chúng ta chỉ có thể sử dụng cách giải tự luận. Việc tận dụng thêm các chức năng của máy tính CASIO fx – 570MS trong trường hợp nghiệm của phương trình $y’ = 0$ lẻ hoặc hàm số có hệ số lớn sẽ đảm bảo độ chính xác cho các kết quả.

<!-- chunk:14 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 13. Cho hàm số $y = \frac{1}{4}{x^4} – \frac{1}{2}{x^2} + \frac{1}{2}.$ Tích các giá trị cực đại và cực tiểu của hàm số bằng:

A. $– \frac{1}{{32}}.$

B. $-1.$

C. $1.$

D. $\frac{1}{{32}}.$

Chọn D.

Lời giải tự luận: Ta lần lượt có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = {x^3} – x$, $y’ = 0$ $\Leftrightarrow {x^3} – x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số bằng:

$P = y(1).y(0).y( – 1) = \frac{1}{{32}}.$

Lời giải tự luận kết hợp với máy tính CASIO fx -570MS: Ta có:

+ Tập xác định: $D= R.$

+ Đạo hàm: $y’ = {x^3} – x$, $y’ = 0$ $\Leftrightarrow {x^3} – x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = \pm 1}
\end{array}} \right..
$$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số là $P = \frac{1}{{32}}$ được tính nhanh bằng cách ấn:

+ Nhập hàm số $y = \frac{1}{4}{x^4} – \frac{1}{2}{x^2} + \frac{1}{2}$ ta ấn:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-11.png" alt="">

+ Khi đó, ta lần lượt với các giá trị $x=0$, $x=-1$ và $x=1:$

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-12.png" alt="">

<!-- chunk:15 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 14. Cho hàm số $y = \frac{{{x^2} – x + 4}}{{x – 1}}.$ Tích các giá trị cực đại và cực tiểu của hàm số bằng:

A. $-15.$

B. $-10.$

C. $-5.$

D. $0.$

Chọn D.
Lời giải tự luận 1: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = 1 – \frac{4}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{4}{{{{(x – 1)}^2}}} = 0$ $\Leftrightarrow {(x – 1)^2} = 4$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = – 1}\\
{{x_2} = 3}
\end{array}} \right..
$$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số bằng:

$P = y( – 1).y(3)$ $= \frac{{{{( – 1)}^2} + 1 + 4}}{{ – 1 – 1}}.\frac{{{3^2} – 3 + 4}}{{3 – 1}}$ $= – 15.$

Lời giải tự luận 1 kết hợp với máy tính CASIO fx-570MS: Ta có:

+ Tập xác định: $D = R\backslash \{ 1\} .$

+ Đạo hàm $y’ = 1 – \frac{4}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow 1 – \frac{4}{{{{(x – 1)}^2}}} = 0$ $\Leftrightarrow {(x – 1)^2} = 4$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = – 1}\\
{{x_2} = 3}
\end{array}} \right..
$$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số là $P = -15$ được tính nhanh bằng cách ấn:

+ Nhập hàm số $y = \frac{{{x^2} – x + 4}}{{x – 1}}$ ta ấn:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-13.png" alt="">

+ Khi đó, ta lần lượt với các giá trị $x=-1$ và $x=3$:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-14.png" alt="">

Lời giải tự luận 2: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 2x – 3}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Khi đó:

$\frac{{u’}}{{v’}} = 2x – 1$ $\Rightarrow P = y(0).y(2)$ $= [2( – 1) – 1](2.3 – 1)$ $= – 15.$

Lời giải tự luận 2 kết hợp với máy tính CASIO fx – 570MS: Ta có:

+ Tập xác định: $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 2x – 3}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Ta có: $\frac{{u’}}{{v’}} = 2x – 1.$

Khi đó, tích các giá trị cực đại và cực tiểu của hàm số là $P=-15$ được tính nhanh bằng cách ấn:

+ Nhập hàm số $y= 2x-1$ ta ấn:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-15.png" alt="">

+ Khi đó, ta lần lượt với các giá trị $x=-1$ và $x=3$:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-16.png" alt="">

Lời giải tự luận 3: Ta lần lượt có:

+ Tập xác định: $D = R\backslash \{ 1\} .$

+ Đạo hàm: $y’ = \frac{{{x^2} – 2x – 3}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} – 2x – 3 = 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x_1} + {x_2} = 2}\\
{{x_1}{x_2} = – 3}
\end{array}} \right..
$$

Khi đó: $\frac{{u’}}{{v’}} = 2x – 1$ $\Rightarrow P = y\left( {{x_1}} \right).y\left( {{x_2}} \right)$ $= \left( {2{x_1} – 1} \right)\left( {2{x_2} – 1} \right).$

$= 4{x_1}{x_2} – 2\left( {{x_1} + {x_2}} \right) + 1$ $= 4.( – 3) – 2.2 + 1$ $= – 15.$

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận 1 chúng ta tìm hai nghiệm của phương trình $y’ = 0$ rồi tính tích các giá trị của hàm số tại các nghiệm đó.

+ Cách giải tự luận 1 kết hợp với máy tính CASIO fx-570MS chỉ có tính minh họa, bởi nó chỉ tỏ ra hiệu quả trong trường hợp nghiệm của phương trình $y’ = 0$ lẻ hoặc hàm số có hệ số lớn.

+ Trong cách giải tự luận 2 chúng ta sử dụng kết quả: “Với hàm phân thức $y = \frac{u}{v}$, giá trị cực đại cực tiểu được tính bằng cách thay hoành độ của chúng vào $\frac{{u’}}{{v’}}$”.

+ Trong cách giải tự luận 3 chúng ta sử dụng kết quả được giới thiệu trong lời giải tự luận 2 và định lí Vi-ét.

<!-- chunk:16 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 15. Cho hàm số $y = |x|(x + 4).$ Tọa độ điểm cực đại của đồ thị hàm số là:

A. $(1;3).$

B. $(-2;4).$

C. $(0;2).$

D. $(0;0).$

Chọn B.
Lời giải tự luận sử dụng quy tắc 1: Ta lần lượt có:

+ Tập xác định: $D= R.$

+ Viết lại hàm số dưới dạng:

$$
y = \left\{ {\begin{array}{l}
{ – x(x + 4)\:\:{\rm{với}}\:\:x \le 0}\\
{x(x + 4)\:\:{\rm{với}}\:\:x > 0}
\end{array}} \right.
$$
 
$$
\Rightarrow y’ = \left\{ {\begin{array}{l}
{ – 2x – 4\:\:{\rm{với}}\:\:x \le 0}\\
{2x + 4\:\:{\rm{với}}\:\:x > 0}
\end{array}} \right..
$$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so-17.png" alt="">

Vậy tọa độ điểm cực đại của đồ thị hàm số là $( – 2;4).$

Lời giải tự luận sử dụng quy tắc 2: Ta lần lượt có:

+ Tập xác định: $D = R.$

+ Viết lại hàm số dưới dạng:

$$
y = \left\{ {\begin{array}{l}
{ – x(x + 4)\:\:{\rm{khi}}\:\:x \le 0}\\
{x(x + 4)\:\:{\rm{khi}}\:\:x > 0}
\end{array}} \right..
$$

$$
y’ = \left\{ {\begin{array}{l}
{ – 2x – 4\:\:{\rm{khi}}\:\:x \le 0}\\
{2x + 4\:\:{\rm{khi}}\:\:x > 0}
\end{array}} \right.
$$
 và 
$$
y” = \left\{ {\begin{array}{l}
{ – 2\:\:{\rm{khi}}\:\:x \le 0}\\
{2\:\:{\rm{khi}}\:\:x > 0}
\end{array}} \right..
$$

$y’ = 0$ $\Leftrightarrow x = – 2$ $\Rightarrow y”( – 2) = – 4 < 0.$

Vậy tọa độ của điểm cực đại của hàm số là $\left( { – 2;y – 2} \right) = \left( { – 2;4} \right).$

**Nhận xét**: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên chúng ta chỉ có thể sử dụng cách giải tự luận. Tuy nhiên, người ta thường không lựa chọn quy tắc II cho các hàm số chứa dấu giá trị tuyệt đối, cụ thể, quy tắc II không thể kiểm tra được đâu là điểm cực tiểu của đồ thị hàm số, thêm vào đó với cách cho đáp án như vậy chúng ta chỉ có thể loại trừ được đáp án C bằng phép thẻ thông thường.

<!-- chunk:17 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 16. Cho hàm số $y = \sin 2x – x – 2.$ Hàm số đạt cực tiểu tại các điểm:

A. $x = – \frac{\pi }{3} + k\pi$, $k \in Z.$

B. $x = \frac{\pi }{3} + k\pi$, $k \in Z.$

C. $x = – \frac{\pi }{6} + k\pi$, $k \in Z.$

D. $x = \frac{\pi }{3} + k\pi$, $k \in Z.$

Chọn C.
Phương pháp tự luận:

TXÐ: $D = R.$

Ta có $y’ = 2\cos 2x – 1$. Giải $y’ = 0$ $\Leftrightarrow x = \pm \frac{\pi }{6} + k\pi$, $k \in Z.$

$y” = – 4\sin 2x$ $\Rightarrow y”\left( { – \frac{\pi }{6} + k\pi } \right)$ $= – 4\sin \left( { – \frac{\pi }{3} + k2\pi } \right)$ $= 2\sqrt 3 > 0.$

Do đó, hàm số đạt cực tiểu tại $x = – \frac{\pi }{6} + k\pi$, $k \in Z.$

Lựa chọn đáp án bằng phép thử:

Chọn $k=0$, ta lần lượt tính các giá trị của hàm số tại $x = – \frac{\pi }{3}$, $x = \frac{\pi }{3}$, $x = – \frac{\pi }{6}$, $x = \frac{\pi }{6}$ ta có:

$y\left( { – \frac{\pi }{3}} \right) = – \frac{{\sqrt 3 }}{2} + \frac{\pi }{3} – 2.$

$y\left( {\frac{\pi }{3}} \right) = \frac{{\sqrt 3 }}{2} – \frac{\pi }{3} – 2.$

$y\left( { – \frac{\pi }{6}} \right) = – \frac{{\sqrt 3 }}{2} + \frac{\pi }{6} – 2$ (nhỏ nhất).

$y\left( {\frac{\pi }{6}} \right) = \frac{{\sqrt 3 }}{2} – \frac{\pi }{6} – 2.$

Nhận xét: Cho dù hàm số đã cho không tuần hoàn nhưng chúng ta vẫn có thể sử dụng phương pháp lựa chọn đáp án đúng bằng phương pháp thử bởi với mọi $k$ giá trị của hàm số chỉ hơn kém nhau $k\pi .$

<!-- chunk:18 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## B. Hàm số luôn có cực trị.

C. $\mathop {\lim }\limits_{x \to \infty } f\left( x \right) = \infty .$

<!-- chunk:19 level:1 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## D. Đồ thị hàm số luôn có tâm đối xứng.

Chọn B.
Phương pháp tự luận:

TXÐ: $D=R.$

Ta có $y’ = 3a{x^2} + 2bx + c.$ Giải $3a{x^2} + 2bx + c = 0$ $(1).$

Khi phương trình $(1)$ vô nghiệm thì hàm số không có cực trị. Do đó khẳng định B là sai.

Nhận xét: Như vậy, để lựa chọn được đáp án đúng cho bài toán trên cần nắm vững tính chất của hàm đa thức bậc $3$, cụ thể:

+ Đồ thị của hàm đa thức bậc $3$ (các hàm đa thức bậc lẻ) luôn cắt trục hoành (do nó là hàm số liên tục và các giới hạn của hàm số ở hai đầu $– \infty$ và $+ \infty$ trái dấu).

+ Hàm số luôn có cực trị là khẳng định sai (đã được giải thích ở trên).

+ Giới hạn tại vô cực bằng $\infty$ là đúng (tính chất này đúng với mọi hàm đa thức).

+ Đồ thị hàm số luôn có tâm đối xứng bởi phương trình $y” = 0$ có dạng $6ax + 2b = 0$ luôn có nghiệm $x = – \frac{b}{{3a}}$ với $a \ne 0.$

<!-- chunk:20 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 18. Hàm số $f\left( x \right) = a{x^3} + b{x^2} + cx + d$ đạt cực tiểu tại điểm $x = 0$, $f\left( 0 \right) = 0$ và đạt cực đại tại $x = 1$, $f\left( 1 \right) = 1.$ Các hệ số $a$, $b$, $c$, $d$ bằng?

A. $a = – 2$, $b = 3$, $c = 0$, $d = 1.$

B. $a = – 2$, $b = 3$, $c = 1$, $d = 0.$

C. $a = – 1$, $b = 1$, $c = 1$, $d = 0.$

D. $a = – 2$, $b = 3$, $c = d = 0.$

Phương pháp tự luận:

TXÐ: $D=R.$

Ta có $f’\left( x \right) = 3a{x^2} + 2bx + c$, $f”\left( x \right) = 6ax + 2b.$

Để hàm số đạt cực tiểu tại điểm $x = 0$, $f\left( 0 \right) = 0$ và đạt cực đại tại $x = 1$, $f\left( 1 \right) = 1$ thì điều kiện là:

$$
\left\{ {\begin{array}{l}
{f\left( 0 \right) = 0\:\:{\rm{và}}\:\:f\left( 1 \right) = 1}\\
{f’\left( 0 \right) = 0\:\:{\rm{và}}\:\:f’\left( 1 \right) = 0}\\
{f”\left( 0 \right) > 0\:\:{\rm{và}}\:\:f”\left( 1 \right) < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{d = 0}\\
{a + b + c + d = 1}\\
{c = 0}\\
{3a + 2b + c = 0}\\
{2b > 0\:\:{\rm{va}}\:\:6a + 2b < 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = – 2}\\
{b = 3}\\
{c = 0}\\
{d = 0}
\end{array}} \right..
$$

Lựa chọn đáp án bằng phép thử:

Hàm số đi qua $O\left( {0;0} \right)$ nên $d=0$, suy ra đáp án A bị loại.

Hàm số đi qua $A\left( {1;1} \right)$ nên $a+b+c+d=1$ suy ra đáp án B bị loại.

Vì $f’\left( 0 \right) = 0$ nên $c=0$ suy ra đáp án C bị loại.

<!-- chunk:21 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 19. Hàm số $f\left( x \right) = {x^3} + a{x^2} + bx + c$ đạt cực trị bằng $0$ tại điểm $x = -2$ và đồ thị của hàm số đi qua điểm $A\left( {1;0} \right).$ Các hệ số $a$, $b$, $c$ bằng?

A. $a = 2$, $b = 0$, $c = – 4.$

B. $a = 3$, $b = 0$, $c = – 4.$

C. $a = 1$, $b = 1$, $c = – 3.$

D. $a = 5$, $b = 1$, $c = – 2.$

Chọn B.
Phương pháp tự luận:

TXĐ: $D=R.$

Ta có $f’\left( x \right) = 3a{x^2} + 2bx + c$, $f”\left( x \right) = 6ax + 2b.$

Để hàm số đạt cực trị tại điểm $x = – 2$, $f\left( 0 \right) = 0$ và đồ thị của hàm số đi qua điểm $A\left( {1;0} \right)$ thì điều kiện là:

$$
\left\{ {\begin{array}{l}
{f\left( { – 2} \right) = 0}\\
{f’\left( { – 2} \right) = 0}\\
{f\left( 1 \right) = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – 8 + 4a + 2b + c = 0}\\
{12 – 4a + b = 0}\\
{1 + a + b + c = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a = 3}\\
{b = 0}\\
{c = – 4}
\end{array}} \right..
$$

Lựa chọn đáp án bằng phép thử:

Hàm số đi qua $A\left( {1;0} \right)$ nên $a+b+c+d=1$, suy ra đáp án A, D bị loại.

Hàm số đi qua $B\left( { – 2;0} \right)$ nên $4a – 2b + c – 8 = 0$ suy ra đáp án C bị loại.

<!-- chunk:22 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 20. Hàm số $y = \frac{{{x^2} – m\left( {m + 1} \right)x + {m^3} + 1}}{{x – m}}$ có cực đại và cực tiểu khi:

A. $m = 1.$

B. $m = 2.$

C. $m = 4.$

D. $\forall m.$

Chọn D.
Phương pháp tự luận:

TXÐ: $D = R\backslash \left\{ m \right\}.$

Ta có $y’ = 1 – \frac{1}{{{{\left( {x – m} \right)}^2}}}.$ Giải $y’ = 0$ $\Leftrightarrow {\left( {x – m} \right)^2} – 1 = 0$ $\Leftrightarrow x = m \pm 1 \in D.$

Tức là $y’=0$ có hai nghiệm phân biệt thuộc $D$ và đổi dẩu qua hai nghiệm này, do đó hàm số luôn có cực đại và cực tiểu.

Lựa chọn đáp án bằng phép thử:

Lấy $m = 0$, hàm số có dạng $y = \frac{{{x^2} + 1}}{x}$ $\Rightarrow y’ = 1 – \frac{1}{{{x^2}}}.$

Giải $y’ = 0$ $\Leftrightarrow x = \pm 1 \in D.$

Tức là $y’=0$ có hai nghiệm phân biệt thuộc $D$ và đổi dấu qua hai nghiệm này, do đó hàm số luôn có cực đại và cực tiểu tại $m=0$ (chỉ có ở đáp án D).

<!-- chunk:23 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 21. Cho hàm số $y = {x^3} – 3{x^2} – 9x.$ Đường thẳng đi qua các điểm cực đại, cực tiểu của đồ thị hàm số có phương trình:

A. $8x – y + 3 = 0.$

B. $x – 8y + 3 = 0.$

C. $8x + y + 3 = 0.$

D. $– x + 8y + 3 = 0.$

Chọn C.
Phương pháp tự luận:

TXÐ: $D=R.$

Ta có $y’ = 3{x^2} – 6x – 9.$ Giải $y’ = 0$ $\Leftrightarrow 3{x^2} – 6x – 9 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Đồ thị hàm số có các điểm cực trị $A\left( { – 1;5} \right)$, $B\left( {3; – 27} \right).$ Do đó phương trình đường thẳng đi qua hai điểm $A$, $B$ là $\frac{{x + 1}}{{3 + 1}} = \frac{{y – 5}}{{ – 27 – 5}}$ $\Leftrightarrow 8x + y + 3 = 0.$

Phương pháp tự luận kết hợp tính chất:

TXÐ: $D=R.$

Ta có $y’ = 3{x^2} – 6x – 9.$

Thực hiện phép chia $y$ cho $y’$ ta được $y = \left( {3{x^2} – 6x – 9} \right)\left( {\frac{1}{3}x – \frac{1}{3}} \right) – 8x – 3.$

Tọa độ các điểm cực đại và cực tiểu cùng thỏa mãn $y = – 8{\rm{ }}x – 3.$

Lựa chọn đáp án bằng phép thử:

TXÐ: $D=R.$

Ta có $y’ = 3{x^2} – 6x – 9.$ Giải $y’ = 0$ $\Leftrightarrow 3{x^2} – 6x – 9 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3}
\end{array}} \right..
$$

Đồ thị hàm số có các điểm cực trị $A\left( { – 1;5} \right)$, $B\left( {3; – 27} \right).$ Dùng phương pháp thử tọa độ của hai điểm $A$, $B$ vào từng phương trình.

Lựa chọn đáp án bằng pháp đánh giá 1 kết hợp tự luận: Hàm số bậc ba khi có cực tiểu, cực đại thì phương trình đường thẳng đi qua hai điểm này phải đi qua điểm uốn của đồ thị. Lấy tọa độ điểm uốn thử từng phương trình.

Lưu ý: Cách tìm điểm uốn:

+ Cách 1: $y’ = 3{x^2} – 6x – 9$, $y” = 6x – 6.$ Giải $y” = 0$ $\Leftrightarrow x = 1$ $\Rightarrow y = – 11.$ Suy ra $U\left( {1; – 11} \right).$

+ Cách 2: Điểm uốn là trung điểm của đoạn thẳng nối hai điểm cực trị $A$ và $B$ $\Rightarrow U\left( {1; – 11} \right).$

Lựa chọn đáp án bằng phép đánh giá 2:

Hàm số bậc ba với hệ số $a>0$ khi có cực tiểu, cực đại thì phương trình đường thẳng đi qua hai điểm này có hướng đi xuống nên hệ số của $x$ và $y$ trong phương trình đường thẳng là cùng dấu.

**Nhận xét**: Để lựa chọn được đáp án đúng cho bài toán trên thì:

+ Trong cách giải tự luận chúng ta cần nhớ phương pháp lập phương trình đường thẳng đi qua hai điểm.

+ Trong cách giải tự luận kết hợp phép thử chúng ta tránh được việc phải nhớ phương pháp lập phương trình đường thẳng đi qua hai điểm nhưng cần cẩn thận trong khi thử và tốt hơn là hãy kết hợp với máy tính để thực hiện tốt công đoạn này.

+ Trong cách giải tự luận kết hợp tính chất luôn là lựa chọn tốt nhất khi chúng ta không nhớ phương pháp lập phương trình đường thẳng đi qua hai điểm hoặc tọa độ hai điểm cực trị của đồ thị hàm số rất lẻ.

+ Trong cách lựa chọn đáp án bằng pháp đánh giá 1 chúng ta sử dụng tính chất thẳng hàng của cực đại, cực tiểu và điểm uốn đối với hàm số đa thức bậc ba.

+ Trong cách lựa chọn đáp án bằng phép đánh giá 2 chúng ta cần nhớ được các dạng đồ thị của hàm đa thức bậc ba, từ đó xác định được hướng của đường thẳng đi qua hai điểm cực trị của đồ thị hàm số.

<!-- chunk:24 level:4 source:https://toanmath.com/2019/12/phuong-phap-giai-nhanh-trac-nghiem-cuc-tri-cua-ham-so.html -->
## Bài tập 22. Cho hàm số $y = \frac{{ – {x^2} + x – 1}}{{x – 1}}.$ Đường thẳng đi qua các điểm cực đại, cực tiểu của đồ thị hàm số có phương trình:

A. $2x+y-1=0.$

B. $2x+y+1=0.$

C. $x-2y-3=0.$

D. $x – 2y + 1 = 0.$

Chọn A.
Phương pháp tự luận:

TXĐ: $D = R\backslash \left\{ 1 \right\}.$

Ta có $y’ = \frac{{ – {x^2} + 2x}}{{{{\left( {x – 1} \right)}^2}}}.$

Giải $y’ = 0$ $\Leftrightarrow – {x^2} + 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Đồ thị hàm số có các điểm cực trị $A\left( {0;1} \right)$, $B\left( {2;3} \right).$ Do đó phương trình đường thẳng đi qua hai điểm $A$ và $B$ là $2x+y−1=0.$

Lựa chọn đáp án bằng phép thử:

Ta có $y’ = \frac{{ – {x^2} + 2x}}{{{{\left( {x – 1} \right)}^2}}}.$ Giải $y’ = 0$ $\Leftrightarrow – {x^2} + 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}.} \right.
$$

Đồ thị hàm số có các điểm cực trị $A\left( {0;1} \right)$, $B\left( {2;3} \right).$ Dùng phương pháp thử tọa độ của hai điểm $A$, $B$ vào từng phương trình.

Phương pháp tự luận kết hợp tính chất:

TXÐ: $D = R\backslash \left\{ 1 \right\}.$

Ta có $y’ = \frac{{ – {x^2} + 2x}}{{{{\left( {x – 1} \right)}^2}}}.$

Giải $y’ = 0$ $\Leftrightarrow – {x^2} + 2x = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{x = 2}
\end{array}} \right..
$$

Phương trình đường thẳng đi qua hai điểm cực trị của hàm phân thức bậc hai trên bậc nhất luôn có dạng $y = \frac{{\left( { – {x^2} + x – 1} \right)’}}{{\left( {x – 1} \right)’}}$ $\Leftrightarrow y = – 2x + 1.$

Lựa chọn đáp án bằng phép đánh giá 1:

+ Phương trình đường thẳng đi qua hai điểm điểm cực trị của hàm số phân thức bậc hai trên bậc nhất phải đi qua điểm tâm đối xứng của đồ thị, tức là đi qua điểm $I\left( {1; – 1} \right).$ Loại được đáp án B và D.

+ Hàm phân thức bậc hai trên bậc nhất với $ad <0$ khi có cực đại, cực tiểu thì phương trình đường thẳng đi qua hai điểm này có hướng đi xuống nên hệ số của $x$ và $y$ trong phương trình đường thẳng phải cùng dấu. Loại C.

Lựa chọn đáp án bằng phép đánh giá 2:

+ Hàm phân thức bậc hai trên bậc nhất với $ad<0$ khi có cực đại, cực tiểu thì phương trình đường thẳng đi qua hai điểm này có hướng đi xuống nên hệ số của $x$ và $y$ trong phương trình đường thẳng phải cùng dấu. Loại C và D.

+ Phương trình đường thẳng đi qua hai điểm điểm cực trị của hàm số phân thức bậc hai trên bậc nhất phải đi qua điểm tâm đối xứng của đồ thị, tức là đi qua điểm $I\left( {1; – 1} \right).$ Loại được đáp án B.