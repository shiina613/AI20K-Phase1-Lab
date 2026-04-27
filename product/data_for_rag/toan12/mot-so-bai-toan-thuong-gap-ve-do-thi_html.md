# Một số bài toán thường gặp về đồ thị

<!-- chunk:0 level:0 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
Tài liệu hướng dẫn phương pháp giải một số bài toán thường gặp về đồ thị trong chương trình Giải tích 12 chương 1.

<!-- chunk:1 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 1: Sự tương giao của hai đồ thị.
1. PHƯƠNG PHÁP

a. Giao điểm của hai đồ thị

Cho hai đồ thị $(C): y = f(x)$ và $(C’): y = g(x).$

Ta có: $(C)$ và $(C’)$ cắt nhau tại 
$$
M\left( {{x_0};{y_0}} \right) \Leftrightarrow \left\{ {\begin{array}{l}
{{y_0} = f\left( {{x_0}} \right)}\\
{{y_0} = g\left( {{x_0}} \right)}
\end{array}} \right..
$$

Tức là $\left( {{x_0};{y_0}} \right)$ là một nghiệm của hệ: 
$$
\left\{ {\begin{array}{l}
{y = f(x)}\\
{y = g(x)}
\end{array}} \right..
$$

Như vậy hoành độ giao điểm của $(C)$ và $(C’)$ là nghiệm của phương trình: $f(x) = g(x)$ $(1).$

Số nghiệm của phương trình $(1)$ bằng số giao điểm của $(C)$ và $(C’).$

b. Phương pháp biện luận số giao điểm của hai đồ thị

Cho hai đồ thị $(C): y = f(x)$ và $(C’): y = g(x).$

Để biện luận số giao điểm của $(C)$ và $(C’)$ ta thực hiện như sau:

+ Viết phương trình hoành độ giao điểm của $(C)$ và $(C’)$: $f(x) = g(x)$ $(1).$

+ Số nghiệm của $(1)$ chính là số giao điểm của $(C)$ và $(C’).$

+ Tùy theo số nghiệm của $(1)$ ta suy ra số giao điểm của $(C)$ và $(C’).$

2. CÁC VÍ DỤ

<!-- chunk:2 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1: Biện luận số giao điểm của hai đường: $(C):y = \frac{{{x^2} + x – 1}}{{x – 1}}$ và đường thẳng $(d): y = -3x + m.$

Phương trình hoành độ giao điểm của hai đường $(C)$ và $(d)$ là:

$\frac{{{x^2} + x – 1}}{{x – 1}} = – 3x + m$ $(1).$

$\Leftrightarrow {x^2} + x – 1 = (x – 1)( – 3x + m)$ $(x \ne 1).$

$\Leftrightarrow g(x) = 4{x^2} – (2 + m)x – 1 + m = 0$ $(2).$

Ta có: $\Delta = {(2 + m)^2} – 4.4( – 1 + m)$ $= {m^2} – 12m + 20.$

Vì $g(1) = 1 \ne 0$, $\forall m$ nên nếu $(2)$ có nghiệm thì nghiệm đó luôn khác $1$ nên nó là nghiệm của $(1).$

Do đó ta có:

$\Delta < 0 \Leftrightarrow 2 < m < 10$: $(1)$ vô nghiệm nên $(C)$ và $(d)$ không có giao điểm.

$\Delta = 0 \Leftrightarrow m = 2$ hay $m = 10$: $(1)$ có một nghiệm nên $(C)$ và $(d)$ có một giao điểm.

$\Delta > 0 \Leftrightarrow m < 2$ hay $m > 10$: $(1)$ có hai nghiệm nên $(C)$ và $(d)$ có hai giao điểm.

Kết luận:

$2 < m < 10$: $(C)$ và $(d)$ không có giao điểm.

$m = 2$ hay $m = 10$: $(C)$ và $(d)$ có một giao điểm.

$m< 2$ hay $m > 10$: $(C)$ và $(d)$ có hai giao điểm phân biệt.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Cho hàm số $y = \frac{{2x + 2}}{{x – 3}}$ có đồ thị $(C).$ Chứng minh rằng với mọi $m$, đường thẳng $(d): y = x + m$ luôn cắt $(C)$ tại hai điểm lần lượt thuộc hai nhánh của $(C).$

Phương trình hoành độ giao điểm của $(C)$ và $(d)$ là:

$\frac{{2x + 2}}{{x – 3}} = x + m$ $\Leftrightarrow {x^2} + (m – 5)x – 3m – 2 = 0$ (vì $x = 1$ không là nghiệm của phương trình).

Đặt $t = x – 3.$

Phương trình $(1)$ trở thành:

${(t + 3)^2} + (m – 5)(t + 3) – 3m – 2 = 0.$

$\Leftrightarrow {t^2} + (m + 1)t – 8 = 0$ $(2).$

Ta thấy: $(2)$ có $P = -8 < 0$ nên phương trình $(2)$ luôn có $2$ nghiệm ${t_1}$, ${t_2}$ sao cho ${t_1} < 0 < {t_2}.$

$\Leftrightarrow (1)$ luôn có $2$ nghiệm ${x_1}$, ${x_2}$ sao cho ${x_1} < 3 < {x_2}.$

$\Leftrightarrow (C)$ luôn cắt $(d)$ tại hai điểm lần lượt thuộc hai nhánh của $(C).$

## Bài tập

## Bài tập 1. Cho hàm số $y = \frac{{2x + 1}}{{x + 1}}.$

a. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số đã cho.

b. Tìm $k$ để đường thẳng $(d):y = kx + 2k + 1$ cắt đồ thị $(C)$ tại hai điểm phân biệt $A$, $B$ sao cho khoảng cách từ $A$ và $B$ đến trục hoành bằng nhau.

## Bài tập 2. Cho hàm số $y = \frac{{2x + 1}}{{x + 1}}.$

a. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số đã cho.

b. Tìm $m$ để đường thẳng $(d): y = -2x + m$ cắt đồ thị $(C)$ tại hai điểm phân biệt $A$, $B$ sao cho tam giác $OAB$ có diện tích bằng $\sqrt 3$ ($O$ là gốc tọa độ).

3.

a. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số: $y = \frac{{{x^2} + x + 1}}{{x + 1}}.$

b. Với các giá trị nào của $m$, đường thẳng $y = m + \frac{3}{4}x$ cắt $(C)$ tại hai điểm phân biệt.

## Bài tập 4. Tìm $m$ để $\left( {{C_m}} \right)$: $y = {x^3} + m{x^2} – (2m – 1)x + m – 2$ cắt trục hoành tại $3$ điểm có hoành độ dương.

## Bài tập 5. Định $m$ để $\left( {{C_m}} \right)$: $y = 4{x^3} – 3(2m + 4){x^2}$ $+ 2\left( {{m^2} + 8m + 4} \right)x – 2m(2m + 4)$ cắt $Ox$ tại $3$ điểm phân biệt có hoành độ lớn hơn $1.$

## Bài tập 6. Cho hàm số $y = – {x^4} + m{x^2} – m + 1$ $\left( {{C_m}} \right).$

a. Biện luận theo $m$ số cực trị của hàm số.

b. Định $m$ để $\left( {{C_m}} \right)$ cắt $Ox$ tại $4$ điểm có hoành độ lập thành cấp số cộng. Xác định các số hạng của cấp số cộng này.

## Bài tập 7. Cho $(C):y = \frac{{{x^2} – 2x + 2}}{{x – 1}}.$ Viết phương trình đường thẳng $(d)$ qua $A(3;0)$ và có hệ số góc $m.$ Định $m$ để $(d)$ và $(C)$ có $2$ giao điểm phân biệt.

## Bài tập 8. Cho $(C):y = {(x – 1)^2}(4 – x).$

a. Gọi $I$ là giao điểm của $(C)$ với trục $Oy.$ Viết phương trình đường thẳng $(d)$ qua $I$ và có hệ số góc $k.$

b. Định $k$ để $(d)$ cắt $(C)$ tại $3$ điểm phân biệt.

## Bài tập 9. Cho hàm số $y = \frac{{{x^2} + 5x + 7}}{{2 – x}}.$

a. Khảo sát hàm số. Gọi $(C)$ là đồ thị hàm số.

b. Tìm trên $(C)$ những điểm cách đều hai trục toạ độ.

c. Biện luận theo $m$ vị trí tương đối của $(C)$ và đường thẳng $(d): y = 3x + m.$

<!-- chunk:4 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 2: Điều kiện tiếp xúc của hai đường.

1. PHƯƠNG PHÁP

Định nghĩa:

Cho hai hàm số $f$ và $g$ có đạo hàm tại điểm ${x_0}.$

Ta nói rằng hai đường cong $(C): y = f(x)$ và $(C’): y = g(x)$ tiếp xúc nhau tại điểm $M\left( {{x_0};{y_0}} \right)$ nếu $M$ là một điểm chung của chúng và hai đường cong đó có tiếp tuyến chung tại $M.$

Điểm $M$ được gọi là tiếp điểm của hai đường cong đã cho.

Điều kiện tiếp xúc:

Hai đường cong $(C): y = f(x)$ và $(C’): y = g(x)$ tiếp xúc nhau $\Leftrightarrow$ hệ phương trình 
$$
\left\{ {\begin{array}{l}
{f(x) = g(x)}\\
{f'(x) = g'(x)}
\end{array}} \right.
$$
 có nghiệm.

Nghiệm của hệ phương trình là hoành độ tiếp điểm của hai đường cong đó.

2. CÁC VÍ DỤ

<!-- chunk:5 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1: Chứng minh rằng đường cong $(C):y = {x^3} – 2{x^2}$ tiếp xúc với parabol $(P):y = – {x^2} + x – 1.$ Tìm tiếp điểm và viết phương trình tiếp tuyến chung của chúng tại điểm đó.

Xét hệ phương trình: 
$$
\left\{ {\begin{array}{l}
{{x^3} – 2{x^2} = – {x^2} + x – 1}\\
{3{x^2} – 4x = – 2x + 1}
\end{array}} \right.
$$
 $(1).$

Ta có 
$$
(1) \Leftrightarrow \left\{ {\begin{array}{l}
{(x – 1)\left( {{x^2} – 1} \right) = 0}\\
{3{x^2} – 2x – 1 = 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 1{\rm{\: hay \:}}x = – 1}\\
{x = 1{\rm{\: hay \:}}x = – \frac{1}{2}}
\end{array}} \right.
$$
 $\Leftrightarrow x = 1.$

Vậy hệ $(1)$ có một nghiệm là $x = 1.$

Suy ra $(C)$ và $(P)$ tiếp xúc nhau.

Hoành độ của tiếp điểm là $x = 1 \Rightarrow y = – 1.$ Do đó tiếp điểm là $M(1;-1).$

Phương trình tiếp tuyến chung $(d)$ của $(C)$ và $(P)$ tại $M$ chính là phương trình tiếp tuyến của $(P)$ tại $M.$

Do đó $(d):y + 1 = y'(1)(x – 1)$ $= – 1(x – 1)$ $\Leftrightarrow (d):y = – x.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Định $m$ để $(C):y = \frac{{2x – 1}}{{x + 1}}$ và $(d): y = 3x + m$ tiếp xúc nhau.

$(C)$ và $(d)$ tiếp xúc nhau 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{y_C} = {y_d}}\\
{y{‘_C} = y{‘_d}}
\end{array}} \right.
$$
 có nghiệm.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\frac{{2x – 1}}{{x + 1}} = 3x + m}\\
{\frac{3}{{{{(x + 1)}^2}}} = 3}
\end{array}} \right.
$$
 có nghiệm 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m = \frac{{2x – 1}}{{x + 1}} – 3x}\\
{{{(x + 1)}^2} = 1}
\end{array}} \right.
$$
 có nghiệm.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = 0}\\
{m = – 1}
\end{array}} \right.
$$
 hay 
$$
\left\{ {\begin{array}{l}
{x = – 2}\\
{m = 11}
\end{array}} \right..
$$

Vậy $m$ thỏa mãn yêu cầu bài toán $\Leftrightarrow$ $m = -1$ hay $m = 11.$

## Bài tập

## Bài tập 1. Chứng minh rằng đồ thị của các hàm số $f(x) = – 3{x^2} + 4x + 4$, $g(x) = {x^3} – 3{x^2} + x + 2$ và $h(x) = – {x^2} + 8x + 6$ tiếp xúc nhau tại điểm $A(-1; -3).$

## Bài tập 2. Cho hàm số $y = \frac{{{x^2} – 3x + 3}}{{x – 2}}.$

a. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Tìm $m$ để đường thẳng $(d): y = -3x + m$ tiếp xúc $(C)$, hãy tìm toạ độ tiếp điểm.

## Bài tập 3. Cho hàm số $y = \frac{{(m – 1)x + m}}{{x – m}}$ $(m \ne 0).$

a. Chứng minh khi $m$ thay đổi đồ thị $\left( {{C_m}} \right)$ của hàm số luôn tiếp xúc nhau tại một điểm cố định.

b. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số khi $m = 2.$

## Bài tập 4. Định $m$ để đồ thị $(C)$ của hàm số:

a. $y = \frac{{3x – 3}}{{x + 2}}$ tiếp xúc với đường thẳng $(d): y = x + m.$

b. $y = 4{x^3} + (m – 3)x + 1$ tiếp xúc với đường thẳng $(d): y = m(2x – 1) + 2.$

c. $y = \frac{{{x^2} – mx + 1}}{{x + 1}}$ tiếp xúc trục $Ox.$

d. $y = {x^3} – 3{x^2} + mx – 4 + m$ tiếp xúc với $(d): y = 5x-3.$

<!-- chunk:7 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 3: Viết phương trình tiếp tuyến của đồ thị $(C): y = f(x).$

1. PHƯƠNG PHÁP

## Bài tập 1. Một số kiến thức cơ bản cần nắm vững

Cho hàm số $y = f(x)$ có đồ thị $(C)$, $f(x)$ có đạo hàm tại ${x_0}.$

Khi đó:

a. $f’\left( {{x_0}} \right)$ chính là hệ số góc của tiếp tuyến của $(C)$ tại $M\left( {{x_0};f\left( {{x_0}} \right)} \right).$

b. Phương trình tiếp tuyến của $(C)$ tại $M\left( {{x_0};{y_0}} \right)$ có dạng: $y – {y_0} = f’\left( {{x_0}} \right)\left( {x – {x_0}} \right).$

c. Điều kiện để đường thẳng $(d): y = kx + b$ tiếp xúc $(C)$ là hệ phương trình sau có nghiệm: 
$$
\left\{ {\begin{array}{l}
{f(x) = kx + b}\\
{f'(x) = k}
\end{array}} \right.
$$

## Bài tập 2. Các bài toán thường gặp về lập phương trình tiếp tuyến

<!-- chunk:8 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Bài toán 1: Lập phương trình tiếp tuyến của $(C)$ tại điểm $M.$

+ Tìm ${x_0} = {x_M}$, ${y_0} = {y_M}.$

+ $y’ \Rightarrow y’\left( {{x_0}} \right) = ?.$

+ Suy ra phương trình tiếp tuyến cần tìm là: $y – {y_0} = y’\left( {{x_0}} \right)\left( {x – {x_0}} \right).$

<!-- chunk:9 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Bài toán 2: Lập phương trình của tiếp tuyến khi biết hệ số góc $k.$

Cách 1:

+ Gọi ${x_0}$ là hoành độ tiếp điểm. Ta có $f’\left( {{x_0}} \right) = k$ $(1).$

+ Giải phương trình $(1)$ ta được ${x_0}$, thay vào $y$ ta được ${y_0}.$

Khi đó: Phương trình tiếp tuyến cần tìm có dạng: $y – {y_0} = k\left( {x – {x_0}} \right).$

Cách 2:

+ Vì tiếp tuyến $(d)$ có hệ số góc $k$ $\Rightarrow (d):y = kx + b.$

+ Từ điều kiện tiếp xúc suy ra $b.$

Từ đó ta có phương trình tiếp tuyến $(d): y = kx + b.$

Chú ý: Có thể xác định hệ số góc $k$ của tiếp tuyến dựa vào các nhận xét sau:

+ $(d)//(D) \Leftrightarrow {k_d} = {k_D}.$

+ $(d) \bot (D) \Leftrightarrow {k_d}{k_D} = – 1.$

+ Nếu $(D):y = ax + b$ thì ${k_D} = a.$

+ ${k_d} = \tan (Ox,d).$

<!-- chunk:10 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Bài toán 3: Phương trình tiếp tuyến của $(C)$ đi qua điểm $A$ cho trước.

Cách 1:

+ Gọi $(d)$ là đường thẳng qua $A$ và có hệ số góc là $k.$

$\Rightarrow (d):y – {y_A} = k\left( {x – {x_A}} \right)$ $(*).$

+ Bằng cách cho $(d)$ tiếp xúc $(C)$ ta tìm được $k.$

Thay $k$ vào $(*)$ ta thu được phương trình tiếp tuyến cần tìm. Cách 2:

+ Gọi $M\left( {{x_0};{y_0}} \right)$ là tiếp điểm của tiếp tuyến $(d)$ và $(C).$

$\Rightarrow (d):y – {y_0} = f\left( {{x_0}} \right)\left( {x – {x_0}} \right)$ $(a).$

+ Vì $(d)$ qua $A$ $\Rightarrow {y_A} – {y_0} = f’\left( {{x_0}} \right)\left( {{x_A} – {x_0}} \right)$ $(b).$

+ Giải $(b)$ ta được ${x_0}$ và ${y_0}.$ Thay vào $(a)$ ta được phương trình tiếp tuyến cần lập.

2. CÁC VÍ DỤ

<!-- chunk:11 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1: Lập phương trình tiếp tuyến của đồ thị $(C):y = \frac{{{x^2} – x + 1}}{{x – 1}}.$

a. Tại điểm có hoành độ ${x_0} = 3.$

b. Biết tiếp tuyến vuông góc với đường thẳng $(D):x – 3y + 1 = 0.$

a. Ta có ${x_0} = 3 \Rightarrow {y_0} = \frac{7}{2}.$

$y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}}$ $\Rightarrow y'(3) = \frac{3}{4}.$

Suy ra phương trình tiếp tuyến cần tìm là:

$(d):y – \frac{7}{2} = \frac{3}{4}(x – 3)$ $\Leftrightarrow (d):y = \frac{3}{4}x + \frac{5}{4}.$

b. $(D):x – 3y + 1 = 0$ $\Leftrightarrow y = \frac{1}{3}x + \frac{1}{3}.$ Do đó hệ số góc của $(D)$ là ${k_D} = \frac{1}{3}.$

Tiếp tuyến $(d)$ vuông góc với $(D)$ nên ${k_d}{k_D} = – 1 \Rightarrow {k_d} = – 3.$

Gọi ${x_0}$ là hoành độ tiếp điểm của $(d)$ và $(C)$, ta có:

$y’\left( {{x_0}} \right) = {k_d} = – 3$ $\Leftrightarrow \frac{{x_0^2 – 2{x_0}}}{{{{\left( {{x_0} – 1} \right)}^2}}} = – 3.$

$\Leftrightarrow 4x_0^2 – 8{x_0} + 3 = 0$ $\Leftrightarrow {x_0} = \frac{1}{2}$ hay ${x_0} = \frac{3}{2}.$

Với ${x_0} = \frac{1}{2}$ $\Rightarrow {y_0} = – \frac{3}{2}$ $\Rightarrow (d):y = – 3\left( {x – \frac{1}{2}} \right) – \frac{3}{2} = – 3x.$

Với ${x_0} = \frac{3}{2}$ $\Rightarrow {y_0} = \frac{7}{2}$ $\Rightarrow (d):y = – 3\left( {x – \frac{3}{2}} \right) + \frac{7}{2}$ $= – 3x + 8.$

Vậy có hai tiếp tuyến thỏa mãn bài toán là ${d_1}:y = – 3x$ và ${d_2}:y = – 3x + 8.$

<!-- chunk:12 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Cho đồ thị $(C):y = {x^3} – 3{x^2} + 2.$

a. Viết phương trình tiếp tuyến của $(C)$ biết tiếp tuyến qua $A(2;-2).$

b. Viết phương trình tiếp tuyến của $(C)$ biết tiếp tuyến song song với đường thẳng $(\Delta ):y = 9x + 2.$

a. Gọi $(d)$ là tiếp tuyến của $(C)$ qua $A$ và có hệ số góc $k.$

$\Rightarrow (d)$: $y = k(x – 2) – 2$ $= kx – 2k – 2.$

$(d)$ tiếp xúc $(C)$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{x^3} – 3{x^2} + 2 = kx – 2k – 2\:\left( 1 \right)}\\
{3{x^2} – 6x = k\:\left( 2 \right)}
\end{array}} \right.
$$
 có nghiệm.

Thay $(2)$ vào $(1)$ ta được:

${x^3} – 3{x^2} + 2$ $= x\left( {3{x^2} – 6x} \right) – 2\left( {3{x^2} – 6x} \right) – 2.$

$\Leftrightarrow 2{x^3} – 9{x^2} + 12x – 4 = 0$ $\Leftrightarrow (x – 2)\left( {2{x^2} – 5x + 2} \right) = 0$ $\Leftrightarrow x = 2$ hay $x = \frac{1}{2}.$

Khi $x = 2$ thì $(2) \Rightarrow k = 0$ $\Rightarrow (d):y = – 2.$

Khi $x = \frac{1}{2}$ thì $(2) \Rightarrow k = – \frac{9}{4}$ $\Rightarrow (d):y = – \frac{9}{4}x + \frac{5}{2}.$

Vậy có hai tiếp tuyến thỏa mãn yêu cầu bài toán.

## Bài tập
## Bài tập 1. Chứng minh rằng các đồ thị của hai hàm số $f(x) = {x^2} + 3x$ và $g(x) = \frac{{6x}}{{x + 2}}$ tiếp xúc với nhau. Xác định tiếp điểm của hai đường cong trên và viết phương trình tiếp tuyến chung của chúng tại điểm đó.

## Bài tập 2. Cho hàm số $y = f(x) = 2{x^3} – 3{x^2} + 1.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Tìm giao điểm của $(C)$ và parabol $(P)$: $y = g(x) = {x^2} + 1.$

c) Viết phương trình tiếp tuyến của $(C)$ và $(P)$ tại mỗi giao điểm của chúng.

## Bài tập 3. Cho $(C):y = \frac{{3x – 2}}{{x – 1}}.$ Viết phương trình tiếp tuyến của $(C)$ biết tiếp tuyến song song với đường thẳng $(\Delta ):4x + y – 3 = 0.$

4.

a) Khảo sát hàm số $y = 2{x^3} – 3{x^2} – 2$, gọi $(C)$ là đồ thị hàm số.

b) Viết phương trình tiếp tuyến của $(C)$ vẽ từ điểm $A(0;-2).$

## Bài tập 5. Cho $(C):y = \frac{{x – 2}}{{x – 3}}.$ Lập phương trình tiếp tuyến của $(C)$:

a) Tại điểm có hoành độ bằng $4.$

b) Tại điểm có tung độ bằng $\frac{1}{2}.$

c) Biết tiếp tuyến song song với đường thẳng $(\Delta ):y = – 4x + 5.$

d) Biết tiếp tuyến đi qua $A(-2;1).$

## Bài tập 6. Cho $(C):y = {x^3} – 3{x^2} – 9x + 20.$ Lập phương trình tiếp tuyến của $(C)$ biết tiếp tuyến:

a) Vuông góc với đường thẳng $(\Delta ):x – 9y – 1 = 0.$

b) Phát xuất từ điểm $A(3, -7).$

## Bài tập 7. Viết phương trình tiếp tuyến của $(C):y = \frac{{{x^2} + 3x + 3}}{{x + 2}}$ vuông góc với đường thẳng $(d): 3y – x + 6 = 0.$

## Bài tập 8. Cho $(C):y = \frac{{{x^2} + 2x + 2}}{{x + 1}}.$

a) $A \in (C)$ có ${x_A} = a$. Viết phương trình tiếp tuyến của $(C)$ tại $A.$

b) Tìm $a$ để tiếp tuyến qua $B(1;0).$ Chứng minh có hai giá trị $a$ thỏa mãn điều kiện và hai tiếp tuyến tương ứng vuông góc nhau.

## Bài tập 9. Cho $(C):y = \frac{{x + 2}}{{x – 2}}.$ Viết phương trình tiếp tuyến của $(C)$:

a) Tại điểm có tung độ bằng $5.$

b) Biết tiếp tuyến vuông góc với đường thẳng $y = x + 2.$

c) Biết tiếp tuyến đi qua điểm $A(0; 1).$

## Bài tập 10. Cho $(C):y = {x^4} – 2{x^2} + 2.$ Viết phương trình tiếp tuyến của $(C)$ đi qua $M(0; 1).$

## Bài tập 11. Cho $(C):y = \frac{{{x^2}}}{{x + 1}}.$ Chứng minh rằng qua điểm $A(1;-2)$ có thể kẻ được hai tiếp tuyến đến $(C)$ và hai tiếp tuyến này vuông góc với nhau.

## Bài tập 12. Viết phương trình tiếp tuyến của $(C):y = {x^3} + 3{x^2} – x + 1$ kẻ từ $A(1; 4).$

## Bài tập 13. Chứng minh rằng qua điểm $A(0; 2)$ ta luôn vẽ được ba tiếp tuyến đến đồ thị $(C):y = {x^4} – 3{x^2} + 2.$

## Bài tập 14. Cho hàm số $y = \frac{{{x^2} – 2mx + m}}{{x + m}}$ $({C_m}).$

a) Chứng minh nếu $({C_m})$ cắt $Ox$ tại điểm có hoành độ ${x_0}$ thì hệ số góc của tiếp tuyến tại điểm đó là $k = \frac{{2{x_0} – 2m}}{{{x_0} + m}}.$

b) Định $m$ để $\left( {{C_m}} \right)$ cắt $Ox$ tại hai điểm $A$, $B$ sao cho tiếp tuyến tại $A$, $B$ vuông góc nhau.

## Bài tập 15. Cho $\left( {{C_m}} \right):y = \frac{{x – {m^2} + m}}{{x + m}}$ $(m \ne 0).$ Tìm $m$ để tiếp tuyến với $\left( {{C_m}} \right)$ tại giao điểm của $\left( {{C_m}} \right)$ và trục hoành song song với đường thẳng $y = x.$ Viết phương trình tiếp tuyến nói trên.

## Bài tập 16. Cho hàm số $y = \frac{{ – x + 1}}{{2x – 1}}.$

a. Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b. Chứng minh rằng với mọi $m$, đường thẳng $(d):y = x + m$ luôn cắt $(C)$ tại hai điểm phân biệt $A$, $B.$ Gọi ${k_1}$, ${k_2}$ lần lượt là hệ số góc của các tiếp tuyến của $(C)$ tại $A$ và $B.$ Tìm $m$ để tổng ${k_1} + {k_2}$ đạt giá trị lớn nhất.

<!-- chunk:13 level:1 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## I. PHƯƠNG PHÁP

Các lưu ý:
 a) Định nghĩa giá trị tuyệt đối:

$$
\left| {f(x)} \right| = \left\{ {\begin{array}{l}
{f(x){\rm{\:khi\:}}f(x) \ge 0}\\
{ – f(x){\rm{\:khi\:}}f(x) < 0}
\end{array}} \right..
$$

b) Tính chất đồ thị của hàm số chẵn, hàm số lẻ:

+ Đồ thị của hàm số chẵn nhận trục $Oy$ làm trục đối xứng.

+ Đồ thị của hàm số lẻ nhận gốc tọa độ $O$ làm tâm đối xứng.

c) Cho hai hàm số $y = g(x)$ và $y = f(x)$ cùng có tập xác định là $D$ và có đồ thị lần lượt là $(G)$ và $(F).$ Khi đó:

+ Nếu $g(x) = f(x)$, $\forall x \in D$ thì $(G) \equiv (F).$

+ Nếu $g(x) = -f(x)$, $\forall x \in D$ thì $(G)$ và $(F)$ đối xứng nhau qua trục $Ox.$

<!-- chunk:14 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Dạng 1: Từ đồ thị $(C): y = f(x)$ hãy suy ra đồ thị $\left( {{C_1}} \right):y = \left| {f(x)} \right|.$

a. Cách giải:

Ta có $\left( {{C_1}} \right):y = \left| {f(x)} \right|$ 
$$
= \left\{ {\begin{array}{l}
{f(x){\rm{\:khi\:}}f(x) \ge 0}\\
{ – f(x){\rm{\:khi\:}}f(x) < 0}
\end{array}} \right..
$$

Do đó đồ thị $\left( {{C_1}} \right)$ gồm hai phần:

+ Phần 1 là phần không nằm phía dưới trục hoành của đồ thị $(C).$

+ Phần 2 là phần đối xứng của phần phía dưới trục hoành của $(C)$ qua trục $Ox.$

b. Ví dụ:

Cho hàm số $y = f(x) = {x^3} – 3{x^2} + 4.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $(C’)$ của hàm số $y = g(x) = \left| {{x^3} – 3{x^2} + 4} \right|.$

c) Định $m$ để phương trình: $\left| {{x^3} – 3{x^2} + 4} \right| = m$ có $4$ nghiệm phân biệt.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

## Bài tập 1. Tập xác định: $D= R.$

## Bài tập 2. Sự biến thiên:

Giới hạn: $\mathop {\lim }\limits_{x \to \pm \infty } y = \pm \infty .$

$y’ = 3{x^2} – 6x$, 
$$
y’ = 0 \Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \Rightarrow y = 4}\\
{x = 2 \Rightarrow y = 0}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-1.png" alt="">

Hàm số tăng trong $( – \infty ;0)$ và $(2; + \infty ).$

Hàm số giảm trong $(0;2).$

Hàm số đạt cực đại tại $x = 0$, ${y_{CĐ}} = 4$ và đạt cực tiểu tại $x = 2$, ${y_{CT}} = 0.$

3. Điểm uốn:

$y” = 6x – 6.$

$y” = 0$ $\Leftrightarrow x = 1 \Rightarrow y = 2.$

Suy ra điểm uốn $I(1; 2).$

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-2.png" alt="">

Nhận xét: Đồ thị nhận điểm uốn $I(1;2)$ làm tâm đối xứng.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $(C’)$ của hàm số $y = g(x) = \left| {{x^3} – 3{x^2} + 4} \right|.$

Ta có $\left( {{C_1}} \right):y = g(x) = \left| {f(x)} \right|$ 
$$
= \left\{ \begin{array}{l}
f(x){\rm{\:khi\:}}f(x) \ge 0\\
– f(x){\rm{\:khi\:}}f(x) < 0
\end{array} \right..
$$

Do đó đồ thị $\left( {{C_1}} \right)$ gồm hai phần:

+ Phần 1 là phần không nằm phía dưới trục hoành của đồ thị $(C).$

+ Phần 2 là phần đối xứng của phần phía dưới trục hoành của $(C)$ qua trục $Ox.$

Ta có đồ thị $\left( {{C_1}} \right)$ như sau:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-3.png" alt="">

c) Định $m$ để phương trình: $\left| {{x^3} – 3{x^2} – 6} \right| = m$ $(1)$ có $4$ nghiệm phân biệt.

Ta có phương trình $(1)$ là phương trình hoành độ giao điểm của đồ thị $({C_1})$ và đường thẳng $(d):y = m.$

Do đó số nghiệm của $(1)$ bằng số giao điểm của đồ thị $\left( {{C_1}} \right)$ và đường thẳng $(d).$

Dựa vào đồ thị $\left( {{C_1}} \right)$ ta suy ra:

$(1)$ có $4$ nghiệm phân biệt.

$\Leftrightarrow \left( {{C_1}} \right)$ và $(d)$ có $4$ giao điểm phân biệt $\Leftrightarrow 0 < m < 4.$

c. Bài tập:
1.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = {x^3} – 3x + 2.$

b) Từ đồ thị $(C)$ suy ra đồ thị $(C’)$ của hàm số $y = \left| {{x^3} – 3x + 2} \right|.$

2.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = f(x) = \frac{{{x^2} + 3x + 3}}{{x + 2}}.$

b) Dựa vào đồ thị $(C)$ suy ra đồ thị $\left( {{C_1}} \right)$ của hàm số $y = g(x) = \left| {\frac{{{x^2} + 3x + 3}}{{x + 2}}} \right|.$

## Bài tập 3. Cho hàm số $y = \frac{{x – 2}}{{x + 1}}.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $(C’)$: $y = \left| {\frac{{x – 2}}{{x + 1}}} \right|.$

<!-- chunk:15 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Dạng 2: Từ đồ thị $(C): y = f(x)$ hãy suy ra đồ thị $\left( {{C_1}} \right):y = g(x) = f\left( {\left| x \right|} \right).$
a. Cách giải:
Ta có: $g( – x) = f(| – x|) = f(|x|) = g(x)$ nên hàm số $y = g(x)$ là hàm số chẵn.

Suy ra $\left( {{C_1}} \right)$ nhận $Oy$ làm trục đối xứng.

Mặt khác khi $x \ge 0$ thì $g(x) = f(|x|) = f(x)$ nên $({C_1}) \equiv (C).$

Do đó $({C_1})$ gồm hai phần:

+ Phần 1 là phần của đồ thị $(C)$ nằm bên phải của $Oy.$

+ Phần 2 là phần đối xứng của phần 1 qua $Oy.$

b. Ví dụ:

Cho hàm số $y = f(x) = \frac{{{x^2} – 4x + 5}}{{x – 2}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $\left( {C’} \right):y = \frac{{{x^2} – 4|x| + 5}}{{|x| – 2}}.$

a) Ta có $y = \frac{{{x^2} – 4x + 5}}{{x – 2}}$ $= x – 2 + \frac{1}{{x – 2}}.$

Tập xác định: $D = R\backslash \{ 1\} .$

Giới hạn và tiệm cận:

$$
\left\{ {\begin{array}{l}
{\mathop {\lim }\limits_{x \to {2^ – }} y = \mathop {\lim }\limits_{x \to {2^ – }} \frac{{{x^2} – 4x + 5}}{{x – 2}} = – \infty }\\
{\mathop {\lim }\limits_{x \to {2^ + }} y = \mathop {\lim }\limits_{x \to {2^ + }} \frac{{{x^2} – 4x + 5}}{{x – 2}} = + \infty }
\end{array}} \right.
$$
 $\Rightarrow x = 2$ là tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to \pm \infty } [y – (x – 2)]$ $= \mathop {\lim }\limits_{x \to \pm \infty } \frac{1}{{x – 2}} = 0$ $\Rightarrow y = x – 2$ là tiệm cận xiên của đồ thị.

Sự biến thiên:

$y’ = \frac{{{x^2} – 4x + 3}}{{{{(x – 2)}^2}}}$, $y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1 \Rightarrow y = – 2}\\
{x = 3 \Rightarrow y = 2}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-4.png" alt="">

Hàm số đồng biến trong $( – \infty ;1)$ và $(3; + \infty ).$

Hàm số nghịch biến trong $(1;2)$ và $(2;3).$

Hàm số đạt cực đại tại $x = 1$ và ${y_{CĐ}} = – 2.$

Hàm số đạt cực tiểu tại $x = 3$ và ${y_{CT}} = 2.$

Giá trị đặc biệt:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-5.png" alt="">

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-6.png" alt="">

Nhận xét: Đồ thị nhận giao điểm $I(2; 0)$ của hai tiệm cận làm tâm đối xứng.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $\left( {C’} \right):y = g(x) = \frac{{{x^2} – 4|x| + 5}}{{|x| – 2}}.$

Tập xác định của $g(x)$ là: ${D_g} = R\backslash \{ \pm 2\} .$

Ta có: $\forall x \in {D_g} \Rightarrow – x \in {D_g}$ và $g( – x) = f(| – x|) = f(|x|) = g(x).$

Do đó $g(x)$ là hàm số chẵn.

Suy ra $(C’)$ nhận trục $Oy$ làm trục đối xứng.

Khi $x \ge 0$ thì $g(x) = f(x)$ nên $\left( {C’} \right) \equiv (C).$

Do đó đồ thị $(C’)$ gồm hai phần sau:

+ Phần 1 là phần của đồ thị $(C)$ ứng với $x \ge 0.$

+ Phần 2 là phần đối xứng của phần 1 qua trục $Oy.$

Ta có đồ thị $(C’)$ như sau:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-7.png" alt="">

c. Bài tập:

## Bài tập 1. Cho hàm số $y = {x^3} – 6{x^2} + 9x.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $\left( {{C_1}} \right)$ của hàm số $y = |x{|^3} – 6{x^2} + 9|x|.$

c) Định $m$ để phương trình $|x{|^3} – 6{x^2} + 9|x| – 3 + m = 0$ có $5$ nghiệm $x$ thuộc đoạn $[-2; 4].$

## Bài tập 2. Cho hàm số $y = \frac{{ – {x^2} + x – 2}}{{x + 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Dựa vào đồ thị $(C)$ suy ra đồ thị $\left( {{C_1}} \right)$ của hàm số $y = \frac{{ – {x^2} + |x| – 2}}{{|x| + 1}}.$

3.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = f(x) = 2{x^3} – 9{x^2} + 12x – 4.$

b) Tìm $m$ để phương trình $2|x{|^3} – 9{x^2} + 12|x| = m$ có $6$ nghiệm phân biệt.

<!-- chunk:16 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Dạng 3: Từ đồ thị $(C):y = u(x).v(x)$ hãy suy ra đồ thị $\left( {{C_1}} \right):y = |u(x)|.v(x).$
a. Cách giải:
Vì $y = |u(x)|.v(x)$ 
$$
= \left\{ {\begin{array}{c}
{u(x).v(x){\rm{\:khi\:}}u(x) \ge 0}\\
{ – u(x).v(x){\rm{\:khi\:}}u(x) < 0}
\end{array}} \right..
$$

Nên $\left( {{C_1}} \right)$ gồm hai phần sau:

+ Phần đồ thị $(C)$ ứng với $u(x) \ge 0.$

+ Phần đối xứng qua $Ox$ của phần đồ thị $(C)$ ứng với $u(x) < 0.$

b. Ví dụ:

Cho hàm số $y = f(x) = \frac{{2x – 4}}{{x – 1}}.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị của $(C’)$ của hàm số $y = \frac{{|2x – 4|}}{{x – 1}}.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

Tập xác định: $D = R\backslash \{ 1\} .$

Giới hạn và tiệm cận: 
$$
\left\{ {\begin{array}{l}
{\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{2x – 4}}{{x – 1}} = + \infty }\\
{\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{2x – 4}}{{x – 1}} = – \infty }
\end{array}} \right..
$$

Suy ra $x = 1$ là tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to \pm \infty } y = \mathop {\lim }\limits_{x \to \pm \infty } \frac{{2x – 4}}{{x – 1}} = 2$ $\Rightarrow y = 2$ là tiệm cận ngang của đồ thị hàm số.

Sự biến thiên: $y’ = \frac{2}{{{{(x – 1)}^2}}} > 0$, $\forall x \in D.$

Suy ra hàm số nghịch biến trên các khoảng xác định. Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-8.png" alt="">

Hàm số không có cực trị.

Giá trị đặc biệt :

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-9.png" alt="">

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-10.png" alt="">

Nhận xét: Đồ thị $(C)$ nhận giao điểm $I(1;2)$ của hai tiệm cận làm tâm đối xứng.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị của $(C’)$ của hàm số $y = g(x) = \frac{{|2x – 4|}}{{x – 1}}.$

Ta có 
$$
g(x) = \left\{ {\begin{array}{c}
{f(x){\rm{\:khi\:}}x \ge 2}\\
{ – f(x){\rm{\:khi\:}}x < 2}
\end{array}} \right..
$$

Do đó đồ thị $(C’)$ gồm hai phần sau:

+ Phần 1 là phần của đồ thị $(C)$ ứng với $x \ge 2.$

+ Phần 2 là phần đối xứng qua trục $Ox$ của phần đồ thị $(C)$ ứng với $x < 2.$

Ta có đồ thị $(C’)$ có dạng sau:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-11.png" alt="">

c. Bài tập:

## Bài tập 1. Cho hàm số $y = 2{x^4} – 4{x^2}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Với giá trị nào của $m$ thì phương trình ${x^2}\left| {{x^2} – 2} \right| = m$ có đúng $6$ nghiệm phân biệt.

## Bài tập 2. Cho hàm số $y = f(x) = {x^3} – 6{x^2} + 9x – 2.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $(C’)$ của hàm số.

## Bài tập 3. Cho hàm số: $y = \frac{{3x – 3}}{{x – 2}}.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Từ đồ thị $(C)$ hãy suy ra đồ thị $(C’)$ của hàm số $y = \frac{{3x – 3}}{{|x – 2|}}.$

## Bài tập 4. Cho hàm số $y = \frac{{{x^2} + x – 3}}{{x + 2}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Dựa vào đồ thị $(C)$ suy ra đồ thị $(C’)$ của hàm số $y = \frac{{{x^2} + x – 3}}{{|x + 2|}}.$

<!-- chunk:17 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 5: Biện luận số nghiệm của phương trình bằng đồ thị.

1. PHƯƠNG PHÁP

Cho đồ thị $(C): y = f(x).$ Dựa vào đồ thị $(C)$, hãy biện luận theo $m$ số nghiệm phương trình: $f(x) = m$ $(1).$

Ta có:

Phương trình $(1)$ là phương trình hoành độ giao điểm của đường $(C): y = f(x)$ và đường thẳng $(d): y = m.$

Do đó số nghiệm của $(1)$ bằng số điểm chung của $(C)$ và $(d).$

Dựa vào đồ thị $(C)$, kết luận số điểm chung của $(C)$ và $(d).$ Suy ra số nghiệm của $(1).$

Chú ý: Nếu bài toán yêu cầu biện luận số nghiệm $x$ thuộc tập $K$, thì ta chỉ dựa vào phần đồ thị $(C)$ ứng với $x \in K.$

2. CÁC VÍ DỤ

Ví dụ: Cho hàm số $y = {x^3} – 3x + 2.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Dùng đồ thị $(C)$ biện luận số nghiệm của phương trình: ${x^3} – 3x + 2 – m = 0.$

c) Định $m$ để phương trình sau có đúng một nghiệm dương: ${x^3} – 3x + 2m – 2 = 0.$

a) Bạn đọc tự giải.

Ta có đồ thị $(C)$ như sau:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-12.png" alt="">

b) Ta có ${x^3} – 3x + 2 – m = 0$ $\Leftrightarrow {x^3} – 3x + 2 = m$ $(1).$

Do đó $(1)$ là phương trình hoành độ giao điểm của đường thẳng $(d): y = m$ và đồ thị $(C).$

Suy ra số nghiệm của $(1)$ chính bằng số giao điểm của $(C)$ và $(d).$

Dựa vào đồ thị $(C)$ ta có:

$m < 0$ hay $m > 4$: $(1)$ có một nghiệm.

$m = 0$ hay $m = 4$: $(1)$ có hai nghiệm phân biệt.

$0< m < 4$: $(1)$ có ba nghiệm phân biệt.

c) Ta có ${x^3} – 3x + 2m – 2 = 0$ $\Leftrightarrow {x^3} – 3x + 2 = – 2m + 4$ $(2).$

Do đó $(2)$ là phương trình hoành độ giao điểm của đường thẳng $(d): y = -2m+4$ và đồ thị $(C).$

Suy ra số nghiệm dương của $(2)$ bằng số giao điểm của $(d)$ và phần đồ thị $(C)$ ứng với $x>0.$

Dựa vào đồ thị $(C)$ ta có: $(2)$ có đúng một nghiệm dương 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – 2m + 4 = 0}\\
{ – 2m + 4 > 2}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 2}\\
{m < 1}
\end{array}} \right..
$$

## Bài tập

## Bài tập 1. Cho hàm số $y = {x^3} – 4{x^2} + 4x.$

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số.

b) Dựa vào đồ thị $(C)$, biện luận theo $m$ số nghiệm phương trình: ${x^3} – 4{x^2} + 4x – m = 0.$

2.

a) Khảo sát sự biến thiên và vẽ đồ thị $(C)$ của hàm số: $y = \frac{{2{x^2} + 5x + 4}}{{x + 2}}.$

b) Biện luận theo $m$ số nghiệm phương trình: $\frac{{2{x^2} + 5x + 4}}{{x + 2}} + m = 0.$

3.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = {x^3} – 6{x^2} + 9x – 1.$

b) Dùng đồ thị $(C)$ biện luận theo $m$ số nghiệm của phương trình: ${x^3} – 6{x^2} + 9x – m – 1 = 0$ và ${x^3} – 6{x^2} + 9x + m = 0.$

4.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = 2{x^3} – 9{x^2} + 12x – 4.$

b) Dùng đồ thị $(C)$ biện luận theo $m$ số nghiệm của phương trình $2{x^3} – 9{x^2} + 12x – 4 – m = 0.$

5.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = \frac{{{x^2} + x – 1}}{{x – 1}}.$

b) Dùng đồ thị $(C)$ biện luận theo $m$ số nghiệm $t \in \left[ { – \frac{\pi }{2};\frac{\pi }{2}} \right]$ của phương trình: ${\sin ^2}t + (1 – m)\sin t + m – 1 = 0.$

6.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = – {x^3} + 6{x^2} – 9x.$

b) Dùng đồ thị $(C)$ biện luận theo $k$ số nghiệm của phương trình ${x^3} – 6{x^2} + 9x + m = 0.$

c) Định $m$ để phương trình sau có $3$ nghiệm phân biệt: ${x^3} – 6{x^2} + 9x – {k^3} + 6{k^2} – 9k = 0.$

7.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = \frac{{{{(x – 1)}^2}}}{{x + 2}}.$

b) Biện luận theo $m$ số nghiệm phương trình $\frac{{{{(x – 1)}^2}}}{{|x – 2|}} = m.$

8.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = {x^4} – 2{x^2} – 1.$

b) Với giá trị nào của $m$ thì phương trình $\left| {{x^4} – 2{x^2} – 1} \right| = 2m – 5$ có sáu nghiệm phân biệt.

<!-- chunk:18 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 6: Viết phương trình đường thẳng qua các điểm đặc biệt.

1. PHƯƠNG PHÁP

## Bài tập 1. Đường lối chung:

Để viết phương trình đường thẳng đi qua các điểm đặc biệt của đồ thị $(C)$ của hàm số $y = f(x)$ ta thực hiện các việc sau:

+ Gọi $M(x;y)$ là điểm đặc biệt của đồ thị hàm số.

+ Lập một hệ phương trình mà tọa độ $M$ phải thỏa mãn.

+ Từ hệ trên rút ra một phương trình hệ quả bậc nhất $y = ax + b.$

+ Suy ra đường thẳng $(d): y = ax + b$ là đường thẳng đi qua các điểm đặc biệt $M.$

## Bài tập 2. Hai trường hợp thường gặp:

Lập phương trình đường thẳng qua điểm cực trị của đồ thị hàm bậc ba $y = f(x)$:

+ Tính $y’.$

+ Chia $y$ cho $y’$ và viết được $y = y’.g(x) + r(x)$ với $r(x) = Ax + B.$

+ Gọi $M(x;y)$ là điểm cực trị của đồ thị hàm số $f(x)$ thì tọa độ của $M$ phải thỏa mãn hệ: 
$$
\left\{ {\begin{array}{l}
{f'(x) = 0}\\
{y = f'(x).g(x) + r(x)}
\end{array}} \right.
$$
 $\Rightarrow y = r(x).$

+ Vậy $y = r(x) = Ax + B$ là phương trình của đường thẳng đi qua các điểm cực trị của đồ thị hàm số.

Cách viết phương trình đường thẳng đi qua các điểm cực trị của đồ thị hàm số $y = \frac{{u(x)}}{{v(x)}}$:

+ Gọi $M(x;y)$ là điểm cực trị của đồ thị hàm số thì tọa độ $M$ thỏa mãn hệ phương trình: 
$$
\left\{ {\begin{array}{l}
{y = \frac{{u(x)}}{{v(x)}}}\\
{y = \frac{{u'(x)}}{{v'(x)}}}
\end{array}} \right..
$$
 Suy ra $y = ax + b.$

+ Vậy $y = ax + b$ là phương trình của đường thẳng đi qua các điểm cực đại và cực tiểu của đồ thị hàm số.

2. CÁC VÍ DỤ

<!-- chunk:19 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1: Chứng minh hàm số sau có cực đại, cực tiểu và viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số: $y = 2{x^3} – m{x^2} + mx + 1.$

Tập xác định: $D = R.$

$y’ = 6{x^2} – 2mx + m.$

$y’ = 0 \Leftrightarrow 6{x^2} – 2mx + m = 0$ $(1).$

Hàm số có cực trị $\Leftrightarrow (1)$ có hai nghiệm phân biệt.

$\Leftrightarrow \Delta’ = {m^2} – 6m > 0$ $\Leftrightarrow m < 0$ hay $m > 6.$

Chia $y$ cho $y’$ ta viết được:

$y = \left( {\frac{x}{3} – \frac{m}{{18}}} \right)y’ + \left( {\frac{{2m}}{3} – \frac{{{m^2}}}{9}} \right)x + \frac{{{m^2}}}{{18}} + 1.$

Tọa độ điểm cực trị của đồ thị hàm số thỏa mãn hệ:

$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y = \left( {\frac{x}{3} – \frac{m}{{18}}} \right)y’ + \left( {\frac{{2m}}{3} – \frac{{{m^2}}}{9}} \right)x + \frac{{{m^2}}}{{18}} + 1}
\end{array}} \right.
$$
 $\Rightarrow y = \left( {\frac{{2m}}{3} – \frac{{{m^2}}}{9}} \right)x + \frac{{{m^2}}}{{18}} + 1.$

Vậy phương trình đường thẳng qua các điểm cực trị của đồ thị hàm số là: $y = \left( {\frac{{2m}}{3} – \frac{{{m^2}}}{9}} \right)x + \frac{{{m^2}}}{{18}} + 1.$

<!-- chunk:20 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Chứng minh các hàm số sau có cực đại, cực tiểu và viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số: $y = \frac{{2{x^2} – (2m + 1)x + 4m – 4}}{{x – 2}}.$

Tập xác định: $D = R\backslash \left\{ 2 \right\}.$

$y’ = \frac{{2{x^2} – 8x + 6}}{{{{(x – 2)}^2}}}.$

$y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1 \Rightarrow y = – 2m + 3}\\
{x = 3 \Rightarrow y = – 2m + 12}
\end{array}} \right..
$$

Suy ra hai điểm cực trị của đồ thị hàm số là $A(1;-2m+3)$ và $B(3;-2m+11).$

Ta có: $\overrightarrow {AB} = (2;8) = 2(1;4).$

Do đó đường thẳng $AB$ có hệ số góc $k = 4.$

Suy ra phương trình của $AB$ là: $y = 4(x – 1) – 2m + 3$ $= 4x – 2m – 1.$

Vậy phương trình đường thẳng qua hai điểm cực trị là $y = 4x – 2m – 1.$

<!-- chunk:21 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 3: Định $m$ để hàm số $y = \frac{{2{x^2} – 3mx + 5m}}{{x – 2}}$ có cực đại, cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số.

Tập xác định: $D = R\backslash \{ 2\} .$

$y’ = \frac{{2{x^2} – 8x + m}}{{{{(x – 2)}^2}}}.$

$y’ = 0$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{g(x) = 2{x^2} – 8x + m = 0}\\
{x \ne 2}
\end{array}} \right..
$$

Hàm số có cực đại, cực tiểu.

$\Leftrightarrow y’ = 0$ có hai nghiệm phân biệt khác $2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\Delta’ = 16 – 2m > 0}\\
{g(2) = m – 8 \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m < 8.$

Đặt $y = \frac{{2{x^2} – 3mx + 5m}}{{x – 2}} = \frac{u}{v}.$

Ta có tọa độ các điểm cực trị thỏa mãn hệ:

$$
\left\{ {\begin{array}{l}
{y’ = \frac{{u’v – uv’}}{{{v^2}}}}\\
{y = \frac{u}{v}}
\end{array}} \right.
$$
 
$$
\Rightarrow \left\{ {\begin{array}{l}
{u’v = uv’}\\
{y = \frac{u}{v}}
\end{array}} \right.
$$
 $\Rightarrow y = \frac{u}{v} = \frac{{u’}}{{v’}}$ $= \frac{{4x – 3m}}{1} = 4x – 3m.$

Vậy các điểm cực trị của đồ thị hàm số thuộc đường thẳng $(d): y = 4x – 3m.$

Suy ra phương trình đường thẳng qua các điểm cực trị của đồ thị hàm số là $y = 4x – 3m.$

## Bài tập

## Bài tập 1. Chứng minh hàm số $y = {x^3} – 3{x^2} – 9x + m + 6$ luôn có cực đại và cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số.

## Bài tập 2. Cho họ đường cong $\left( {{C_m}} \right):$ $y = (3 – m){x^3} + 3(m – 3){x^2} + (6m – 1)x – m + 1.$

a) Chứng minh $\left( {{C_m}} \right)$ luôn đi qua $3$ điểm cố định.

b) Chứng minh $3$ điểm cố định trên cùng thuộc một đường thẳng $(d).$

## Bài tập 3. Cho hàm số $y = 3{x^3} – 9{x^2} + 3(2m – 1)x + 9m – 12.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 0.$

b) Định $m$ để hàm số có cực đại, cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số.

## Bài tập 4. Cho hàm số $y = \frac{{{x^2} + x + m}}{{{x^2} – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = -1.$

b) Định $m$ để hàm số có cực đại, cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số.

## Bài tập 5. Cho $\left( {{C_m}} \right):y = \frac{{{x^2} + mx – 6}}{{x – m}}.$

a) Tìm những điểm trong mặt phẳng mà mọi đường $\left( {{C_m}} \right)$ đều đi qua.

b) Định $m$ để $\left( {{C_m}} \right)$ có hai cực trị. Chứng tỏ rằng khi đó hai giá trị cực trị cùng dấu.

c) Viết phương trình đường thẳng qua hai điểm cực trị của đồ thị hàm số.

## Bài tập 6. Cho $\left( {{C_m}} \right):y = \frac{{x + m}}{{{x^2} + 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 0.$

b) Chứng minh nếu $\left( {{C_m}} \right)$ có $3$ điểm uốn thì $3$ điểm uốn thẳng hàng. Viết phương trình đường thẳng qua $3$ điểm uốn đó.

## Bài tập 7. Cho $\left( {{C_m}} \right):$ $y = {x^3} + (m – 1){x^2} – (m + 3)x – 1.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 1.$

b) Chứng minh với mọi $m$ hàm số có cực đại, cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị.

c) Tìm những cặp điểm nguyên trên $(C)$ đối xứng nhau qua đường thẳng $y = x$ và không nằm trên đường thẳng đó.

## Bài tập 8. Cho hàm số $y = \frac{{2x – 1}}{{{x^2}}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Cho $M(0;m).$ Hãy biện luận theo $m$ số tiếp tuyến của $(C)$ vẽ từ $M.$

c) Khi qua $M$ vẽ được hai tiếp tuyến đến $(C)$, hãy lập phương trình đường thẳng $(d)$ qua hai tiếp điểm.

## Bài tập 9. Cho họ đường cong $\left( {{C_m}} \right):$ $y = \frac{{ – {x^2} + mx – {m^2}}}{{x – m}}.$

a) Định $m$ để hàm số có cực đại, cực tiểu. Viết phương trình đường thẳng đi qua điểm cực đại và cực tiểu của đồ thị hàm số.

b) Tìm các điểm trong mặt phẳng sao cho có đúng hai đường của họ $\left( {{C_m}} \right)$ đi qua.

## Bài tập 10. Cho họ đường cong $\left( {{C_m}} \right):$ $y = 2{x^3} + 3(m – 1){x^2} + 6(m – 2)x – 1.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 2.$

b) Viết phương trình tiếp tuyến của $(C)$ đi qua $A(0;-1).$

c) Định $m$ để hàm số có cực đại, cực tiểu và đường thẳng đi qua điểm cực đại, cực tiểu vuông góc với đường thẳng $y = x.$

## Bài tập 11. Cho hàm số $y = m{x^3} – 3m{x^2} + (2m + 1)x + 3 – m$ $(Cm).$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 2.$

b) Định $m$ để hàm số có cực đại, cực tiểu. Chứng minh đường thẳng đi qua điểm cực đại và cực tiểu của $\left( {{C_m}} \right)$ luôn đi qua một điểm cố định.

<!-- chunk:22 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 7: Một số bài toán liên hệ khoảng cách.

1. PHƯƠNG PHÁP

Khoảng cách giữa hai điểm $A$ và $B:$ $AB = \sqrt {{{\left( {{x_B} – {x_A}} \right)}^2} + {{\left( {{y_B} – {y_A}} \right)}^2}} .$

Khoảng cách từ điểm $M$ đến đường thẳng $(\Delta ):Ax + By + C = 0$ là: $d\left( {M,\Delta } \right) = \frac{{\left| {A{x_M} + B{y_M} + C} \right|}}{{\sqrt {{A^2} + {B^2}} }}.$

Đặc biệt: $d\left( {M;Ox} \right) = \left| {{y_M}} \right|$, $d\left( {M;Oy} \right) = \left| {{x_M}} \right|.$

2. CÁC VÍ DỤ

<!-- chunk:23 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1:

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = \frac{{x + 2}}{{x – 1}}.$

b) Tìm trên $(C)$ điểm $M$ cách đều hai trục tọa độ.

a) Tập xác định: $D = R\backslash \left\{ 1 \right\}.$

Giới hạn và tiệm cận:

$$
\left\{ {\begin{array}{l}
{\mathop {\lim }\limits_{x \to {2^ – }} y = – \infty }\\
{\mathop {\lim }\limits_{x \to {2^ + }} y = + \infty }
\end{array}} \right.
$$
 $\Rightarrow x = 1$ là tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to \pm \infty } y = \mathop {\lim }\limits_{x \to \pm \infty } \frac{{x + 2}}{{x – 1}} = 1$ $\Rightarrow y = 1$ là tiệm cận ngang của đồ thị hàm số.

Sự biến thiên:

$y’ = \frac{{ – 3}}{{{{(x – 1)}^2}}} < 0$, $\forall x \in D.$

Suy ra hàm số nghịch biến trên các khoảng xác định.

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-13.png" alt="">

Hàm số không có cực trị.

Giá trị đặc biệt:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-14.png" alt="">

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-15.png" alt="">

Nhận xét: Đồ thị $(C)$ nhận giao điểm $I(1;1)$ của hai tiệm cận làm tâm đối xứng.

b) Gọi $M(x;y) \in (C)$ $\Leftrightarrow y = \frac{{x + 2}}{{x – 1}}.$

$M$ cách đều hai trục tọa độ 
$$
\Leftrightarrow |y| = |x| \Leftrightarrow \left[ {\begin{array}{l}
{y = x}\\
{y = – x}
\end{array}} \right..
$$

Với $y = x$ ta có: $x = \frac{{x + 2}}{{x – 1}}$ $\Leftrightarrow {x^2} – 2x – 2 = 0$ $\Leftrightarrow x = 1 \pm \sqrt 3 .$

Với $y = -x$ ta có: $– x = \frac{{x + 2}}{{x – 1}}$ $\Leftrightarrow {x^2} + 2 = 0$ $\Leftrightarrow x \in \emptyset .$

Vậy $M(1 \pm \sqrt 3 ;1 \pm \sqrt 3 )$ thỏa mãn yêu cầu bài toán.

<!-- chunk:24 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Cho $(C):y = 2{x^4} – 3{x^2} + 2x + 1$ và $(d):y = 2x – 3.$

a) Chứng minh $(C)$ và $(d)$ không có điểm chung.

b) Tìm trên $(C)$ điểm $A$ sao cho $d(A,d)$ nhỏ nhất.

a) Phương trình hoành độ giao điểm của $(C)$ và $(d)$ là:

$2{x^4} – 4{x^2} + 2x + 1 = 2x – 3$ $\Leftrightarrow 2{x^4} – 4{x^2} + 4 = 0$ $(1).$

Vì $(1)$ vô nghiệm nên $(C)$ và $(d)$ không có giao điểm.

b) Gọi $A(x;y) \in (C)$ $\Rightarrow y = 2{x^4} – 4{x^2} + 2x + 1.$

Ta có $(d): 2x – y – 3 = 0$ nên $d(A;d) = \frac{{|2x – y – 3|}}{{\sqrt {{2^2} + {1^2}} }}$ $= \frac{{\left| {2x – 3 – \left( {2{x^4} – 4{x^2} + 2x + 1} \right)} \right|}}{{\sqrt 5 }}$ $= \frac{1}{{\sqrt 5 }}\left| {2{x^4} – 4{x^2} + 4} \right|$ $= \frac{1}{{\sqrt 5 }}\left| {2{{\left( {{x^2} – 1} \right)}^2} + 2} \right|$ $\ge \frac{{2\sqrt 5 }}{5}.$

Dấu bằng xảy ra $\Leftrightarrow {x^2} = 1 \Leftrightarrow x = \pm 1.$

Vậy khi $A( – 1; – 3)$ hay $A(1;1)$ thì $d(A;d)$ nhỏ nhất.

Khi đó $\min d(A;d) = \frac{{2\sqrt 5 }}{5}.$

<!-- chunk:25 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 3: Cho hàm số $y = f(x) = \frac{{{x^2} – x + 1}}{{x – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Tìm điểm $M$ thuộc $(C)$ sao cho tổng các khoảng cách từ $M$ đến $2$ tiệm cận là nhỏ nhất.

c) Xác định hai điểm $A$, $B$ lần lượt ở trên hai nhánh của $(C)$ sao cho độ dài đoạn $AB$ ngắn nhất.

a) Ta có $y = \frac{{{x^2} – x + 1}}{{x – 1}} = x + \frac{1}{{x – 1}}.$

Tập xác định: $D = R\backslash \left\{ 1 \right\}.$

Giới hạn và tiệm cận:

$$
\left\{ {\begin{array}{l}
{\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{{x^2} – x + 1}}{{x – 1}} = – \infty }\\
{\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{{x^2} – x + 1}}{{x – 1}} = + \infty }
\end{array}} \right.
$$
 $\Rightarrow x = 1$ là tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to \pm \infty } [y – x] = \mathop {\lim }\limits_{x \to \pm \infty } \frac{1}{{x – 1}} = 0$ $\Rightarrow y = x$ là tiệm cận xiên của đồ thị.

Sự biến thiên:

$y’ = \frac{{{x^2} – 2x}}{{{{(x – 1)}^2}}}.$

$$
y’ = 0 \Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \Rightarrow y = – 1}\\
{x = 2 \Rightarrow y = 3}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-16.png" alt="">

Hàm số đồng biến trong $( – \infty ;0)$ và $(2; + \infty ).$

Hàm số nghịch biến trong $(0;1)$ và $(1;2).$

Hàm số đạt cực đại tại $x = 0$ và ${y_{CĐ}} = – 1.$

Hàm số đạt cực tiểu tại $x = 2$ và ${y_{CT}} = 3.$

Giá trị đặc biệt:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-17.png" alt="">

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-18.png" alt="">

Nhận xét: Đồ thị nhận giao điểm $I(1;1)$ của hai tiệm cận làm tâm đối xứng.

b) Tìm điểm $M$ thuộc $(C)$ sao cho tổng các khoảng cách từ $M$ đến hai tiệm cận là nhỏ nhất.

$M(x;y) \in (C)$ $\Leftrightarrow y = x + \frac{1}{{x – 1}}.$

$(C)$ có tiệm cận đứng là $x – 1 = 0$ $\Rightarrow {d_1} = d(M;TCĐ) = |x – 1|.$

$(C)$ có tiệm cận xiên là $y = x \Leftrightarrow x – y = 0.$

$\Rightarrow {d_2} = d(M;TCX)$ $= \frac{{|x – y|}}{{\sqrt 2 }} = \frac{1}{{\sqrt 2 |x – 1|}}.$

Ta có ${d_1} + {d_2} \ge 2\sqrt {{d_1}{d_2}} = 2\sqrt {\frac{1}{{\sqrt 2 }}} = \frac{2}{{\sqrt[4]{2}}}.$

Dấu bằng xảy ra $\Leftrightarrow {d_1} = {d_2}$ $\Leftrightarrow x = 1 \pm \frac{1}{{\sqrt[4]{2}}}$ $\Rightarrow y = 1 \pm \frac{1}{{\sqrt[4]{2}}} \pm \sqrt[4]{2}.$

Vậy khi $M\left( {1 + \frac{1}{{\sqrt[4]{2}}};1 + \frac{1}{{\sqrt[4]{2}}} + \sqrt[4]{2}} \right)$ hay $M\left( {1 – \frac{1}{{\sqrt[4]{2}}};1 – \frac{1}{{\sqrt[4]{2}}} – \sqrt[4]{2}} \right)$ thì ${d_1} + {d_2}$ đạt giá trị nhỏ nhất.

c) Xác định hai điểm $A$, $B$ lần lượt ở trên hai nhánh của $(C)$ sao cho $AB$ ngắn nhất.

Vì $A$, $B$ lần lượt thuộc hai nhánh của $(C)$ nên ta có thể giả thiết ${x_A} < 1 < {x_B}.$

Do đó có thể đặt: ${x_A} = 1 – a$, ${x_B} = 1 + b$ trong đó $a>0$ và $b > 0.$

Khi đó: ${y_A} = 1 – a – \frac{1}{a}$ và ${y_B} = 1 + b + \frac{1}{b}.$

Ta có $A{B^2} = {\left( {{x_B} – {x_A}} \right)^2} + {\left( {{y_B} – {y_A}} \right)^2}$ $= {(b + a)^2} + {\left( {b + a + \frac{1}{b} + \frac{1}{a}} \right)^2}$ $= {(b + a)^2}\left[ {1 + {{\left( {1 + \frac{1}{{ab}}} \right)}^2}} \right]$ $= {(a + b)^2}\left( {2 + \frac{1}{{{a^2}{b^2}}} + \frac{2}{{ab}}} \right)$ $\ge {\left( {2\sqrt {ab} } \right)^2}\left( {2\sqrt {\frac{2}{{{a^2}{b^2}}}} + \frac{2}{{ab}}} \right)$ $= 8(\sqrt 2 + 1).$

Dấu bằng xảy ra $\Leftrightarrow a = b = \frac{1}{{\sqrt[4]{2}}}.$

Vậy khi $A\left( {1 – \frac{1}{{\sqrt[4]{2}}};1 – \frac{1}{{\sqrt[4]{2}}} – \sqrt[4]{2}} \right)$, $B\left( {1 + \frac{1}{{\sqrt[4]{2}}};1 + \frac{1}{{\sqrt[4]{2}}} + \sqrt[4]{2}} \right)$ thì $AB$ ngắn nhất và $\min AB = 2\sqrt {2(\sqrt 2 + 1)} .$

## Bài tập

## Bài tập 1. Cho hàm số $y = f(x) = \frac{{x + 1}}{{x – 1}}$ và $(d):2x – y + m = 0.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Chứng minh $(d)$ luôn cắt $(H)$ tại hai điểm phân biệt $A$, $B$ ở trên hai nhánh khác nhau.

c) Định $m$ để độ dài $AB$ ngắn nhất.

## Bài tập 2. Cho hàm số $y = f(x) = \frac{{{x^2} + mx – m}}{{x – 1}}$ có đồ thị $\left( {{C_m}} \right).$

a) Định $m$ để $A(1;2)$ là tâm đối xứng của $\left( {{C_m}} \right).$

b) Khảo sát và vẽ đồ thị $(C)$ của hàm số với $m$ vừa tìm được.

c) Định $k$ để đường thẳng $(d): y = k$ cắt đồ thị $(C)$ tại hai điểm $A$, $B$ sao cho $AB = \sqrt 5 .$

## Bài tập 3. Cho hàm số $y = f(x) = \frac{{{x^2} + 3x + 3}}{{x + 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Xác định hai điểm $A$, $B$ lần lượt ở trên hai nhánh của $(C)$ sao cho $AB$ ngắn nhất.

c) Tìm tọa độ điểm $M$ thuộc $(C)$ sao cho $M$ cách đều hai trục tọa độ.

## Bài tập 4. Cho hàm số $y = f(x) = \frac{{{x^2}\cos \alpha + 2x\sin \alpha + 1}}{{x + 2}}$ có đồ thị là $\left( {{C_\alpha }} \right).$

a) Khảo sát và vẽ đồ thị $\left( {{C_0}} \right)$ của hàm số khi $\alpha = 0.$

b) Tìm $\alpha$ để đường tròn tâm $O$ và tiếp xúc với tiệm cận xiên của $\left( {{C_\alpha }} \right)$ có bán kính lớn nhất.

## Bài tập 5. Cho hàm số $y = f(x)$ $= \frac{{m{x^2} + \left( {{m^2} + 1} \right)x + 4{m^2} + m}}{{x + m}}$ có đồ thị $\left( {{C_m}} \right).$

a) Khi $m = -1$, hãy khảo sát và vẽ đồ thị $(C)$ của hàm số và tìm trên mỗi nhánh của $(C)$ một điểm sao cho khoảng cách giữa chúng nhỏ nhất.

b) Định $m$ để $\left( {{C_m}} \right)$ có một cực trị thuộc góc phần tư $(II)$ và một cực trị thuộc góc phần tư $(IV).$

## Bài tập 6. Cho hàm số $y = f(x) = \frac{{{x^2} + (m + 1)x – m + 1}}{{x – m}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 2.$

b) Chứng minh tích các khoảng cách từ điểm $M$ tùy ý thuộc $(C)$ đến hai tiệm cận là một hằng số.

c) Với giá trị nào của $m$ thì hàm số có cực đại, cực tiểu và hai giá trị cực đại, cực tiểu cùng dấu.

## Bài tập 7. Cho hàm số $y = x + 1 + \frac{1}{{x – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Tìm những điểm trên $(C)$ có hoành độ lớn hơn $1$ sao cho tiếp tuyến tại đó tạo với hai tiệm cận một tam giác có chu vi nhỏ nhất.

8.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số $y = \frac{{x + 2}}{{x – 3}}.$

b) Tìm trên $(C)$ điểm $M$ để khoảng cách từ $M$ đến tiệm cận đứng bằng $5$ lần khoảng cách từ $M$ đến tiệm cận ngang.

<!-- chunk:26 level:2 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Vấn đề 8: Điểm đối xứng và đường đối xứng.

1. PHƯƠNG PHÁP

Hai điểm $A$ và $B$ phân biệt đối xứng nhau $I \Leftrightarrow I$ là trung điểm của $AB.$

Hai điểm $A$ và $B$ phân biệt đối xứng nhau qua đường thẳng $\Delta$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{AB \bot (\Delta )}\\
{1 \in (\Delta )}
\end{array}} \right.
$$
 ($I$ là trung điểm của $AB$).

Hai đường $(C)$ và $(C’)$ gọi là đối xứng nhau qua đường thẳng $(\Delta )$ nếu: $M \in (C)$ và $M’$ là điểm đối xứng của $M$ qua $(\Delta )$ thì ta luôn có: $M \in (C) \Leftrightarrow M’ \in \left( {C’} \right).$

2. CÁC VÍ DỤ

<!-- chunk:27 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 1: Cho hàm số $y = {x^3} – 3m{x^2} + 3\left( {{m^2} – 1} \right)x + 1 – {m^2}$ $({C_m}).$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 2.$

b) Định $m$ để $({C_m})$ có hai điểm phân biệt đối xứng nhau qua gốc tọa độ.

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 2:$

Khi $m = 2$ thì $(C):y = {x^3} – 6{x^2} + 9x – 3.$

Tập xác định: $D = R.$

Giới hạn: $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to – \infty } y = – \infty .$

Chiều biến thiên:

$y’ = 3{x^2} – 12x + 9.$

$y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 1 \to y = 1}\\
{x = 3 \to y = – 3}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-19.png" alt="">

Hàm số tăng trong $( – \infty ;1)$ và $(3; + \infty )$, giảm trong $(1;3).$

Hàm số đạt cực đại tại $x = 1$, ${y_{CĐ}} = 1$ và đạt cực tiểu tại $x = 3$, ${y_{CT}} = – 3.$

$y” = 6x – 12$, $y” = 0 \Leftrightarrow x = 2 \Rightarrow y = – 1.$

Đồ thị có điểm uốn $I(2;-1).$

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-20.png" alt="">

Nhận xét: Đồ thị nhận điểm uốn $I(-1;-2)$ làm tâm đối xứng.

b) Định $m$ để $\left( {{C_m}} \right)$ có hai điểm phân biệt đối xứng nhau qua gốc tọa độ.

Gọi $A\left( {{x_0};{y_0}} \right) \in \left( {{C_m}} \right)$ $\Rightarrow {y_0} = x_0^3 – 3mx_0^2 + 3\left( {{m^2} – 1} \right){x_0} + 1 – {m^2}$ $(1).$

Ta có: $B$ là điểm đối xứng của $A$ qua $O$ $\Leftrightarrow B( – {x_0}; – {y_0}).$

$B \in \left( {{C_m}} \right)$ $\Leftrightarrow – {y_0} = – x_0^3 – 3mx_0^2 – 3\left( {{m^2} – 1} \right){x_0} + 1 – {m^2}$ $(2).$

Từ $(1)$ và $(2)$ suy ra $– 6mx_0^2 + 2 – 2{m^2} = 0$ $(3).$

Nếu ${x_0} = 0$ thì ${y_0} = 1 – {m^2} = – {y_0}$ $\Rightarrow {y_0} = 0$ nên $A \equiv B \equiv O.$

Do đó: $\left( {{C_m}} \right)$ có hai điểm phân biệt đối xứng nhau qua gốc tọa độ $\Leftrightarrow (3)$ có nghiệm ${x_0} \ne 0.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{2 – 2{m^2} \ne 0}\\
{\Delta ‘ = 6m\left( {2 – 2{m^2}} \right) \ge 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – 1 < m < 0}\\
{m > 1}
\end{array}} \right..
$$

Vậy $m$ thỏa yêu cầu bài toán $\Leftrightarrow – 1 < m < 0$ hay $m > 1.$

<!-- chunk:28 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 2: Cho hàm số $y = {x^3} – 3{x^2} + {m^2}x + m.$

a) Khảo sát hàm số khi $m = 0.$

b) Tìm tất cả các giá trị của $m$ để hàm số có cực đại, cực tiểu và các điểm cực đại, cực tiểu đối xứng nhau qua đường thẳng $y = \frac{{x – 5}}{2}.$

a) Khi $m = 0$ thì $(C):y = {x^3} – 3{x^2}.$

Tập xác định: $D = R.$

Giới hạn: $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to – \infty } y = – \infty .$

Chiều biến thiên:

$y’ = 3{x^2} – 6x.$

$y’ = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0 \to y = 0}\\
{x = 2 \to y = – 4}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-21.png" alt="">

Hàm số tăng trong $( – \infty ;0)$ và $(2; + \infty )$, hàm số giảm trong $(0;2).$

Hàm số đạt cực đại tại $x = 0$, ${y_{CĐ}} = 0$ và đạt cực tiểu tại $x = 2$, ${y_{CT}} = -4.$

$y” = 6x – 6.$

$y” = 0 \Leftrightarrow x = 1 \Rightarrow y = – 2.$

Đồ thị có điểm uốn $I(1;-2).$

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-22.png" alt="">

Nhận xét: Đồ thị nhận điểm uốn $I(1;-2)$ làm tâm đối xứng.

b) Tìm tất cả các giá trị của $m$ để hàm số có cực đại, cực tiểu và các điểm cực đại, cực tiểu đối xứng nhau qua đường thẳng $(d):y = \frac{{x – 5}}{2}.$

Tập xác định: $D = R.$

$y’ = 3{x^2} – 6x + {m^2}.$

$y’ = 0 \Leftrightarrow 3{x^2} – 6x + {m^2} = 0$ $(1).$

Hàm số có cực đại, cực tiểu khi và chỉ khi $(1)$ có hai nghiệm phân biệt.

$\Leftrightarrow \Delta ‘ = 9 – 3{m^2} > 0$ $\Leftrightarrow – \sqrt 3 < m < \sqrt 3 .$

Chia $y$ cho $y’$ ta viết được: $y = \frac{{x – 1}}{3}y’ + \frac{{2{m^2} – 6}}{3}x + \frac{{{m^2} + 3m}}{3}.$

Tọa độ điểm cực trị thỏa hệ:

$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y = \frac{{x – 1}}{3}y’ + \frac{{2{m^2} – 6}}{3}x + \frac{{{m^2} + 3m}}{3}}
\end{array}} \right.
$$
 $\Rightarrow y = \frac{{2{m^2} – 6}}{3}x + \frac{{{m^2} + 3m}}{3}.$

Do đó đường thẳng qua các điểm cực trị là $(\Delta ):y = \frac{{2{m^2} – 6}}{3}x + \frac{{{m^2} + 3m}}{3}.$

Suy ra hai điểm cực trị là $A\left( {{x_A};\frac{{2{m^2} – 6}}{3}{x_A} + \frac{{{m^2} + 3m}}{3}} \right)$, $B\left( {{x_B};\frac{{2{m^2} – 6}}{3}{x_B} + \frac{{{m^2} + 3m}}{3}} \right).$

Gọi $I$ là trung điểm của $AB$ thì $I\left( {\frac{{{x_A} + {x_B}}}{2};\frac{{2{m^2} – 6}}{3}{x_I} + \frac{{{m^2} + 3m}}{3}} \right).$

$\Rightarrow I\left( {1;{m^2} + m – 2} \right)$ (vì ${x_A}$, ${x_B}$ là nghiệm của $(1)$).

Do đó $A$, $B$ đối xứng với nhau qua đường thẳng $(d).$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{I \in (d)}\\
{(d) \bot (\Delta )}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + m – 2 = \frac{{1 – 5}}{2}}\\
{{k_d}.{k_\Delta } = \frac{1}{2} \cdot \frac{{2{m^2} – 6}}{3} = – 1}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{{m^2} + m = 0}\\
{{m^2} = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = 0.$

Vậy $m=0$ thỏa mãn yêu cầu bài toán.

<!-- chunk:29 level:3 source:https://toanmath.com/2019/07/mot-so-bai-toan-thuong-gap-ve-do-thi.html -->
## Ví dụ 3: Cho hàm số $y = \frac{{2x – 4}}{{x – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Tìm phương trình đường cong $(C’)$ đối xứng với $(C)$ qua đường thẳng $y = 2.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

Tập xác định: $D = R\backslash \{ 1\} .$

Giới hạn và tiệm cận:

$$
\left\{ {\begin{array}{l}
{\mathop {\lim }\limits_{x \to {1^ – }} y = \mathop {\lim }\limits_{x \to {1^ – }} \frac{{2x – 4}}{{x – 1}} = + \infty }\\
{\mathop {\lim }\limits_{x \to {1^ + }} y = \mathop {\lim }\limits_{x \to {1^ + }} \frac{{2x – 4}}{{x – 1}} = – \infty }
\end{array}} \right.
$$
 $\Rightarrow x = 1$ là tiệm cận đứng của đồ thị.

$\mathop {\lim }\limits_{x \to \pm \infty } y = \mathop {\lim }\limits_{x \to \pm \infty } \frac{{2x – 4}}{{x – 1}} = 1$ $\Rightarrow y = 2$ là tiệm cận ngang của đồ thị hàm số.

Sự biến thiên:

$y’ = \frac{2}{{{{(x – 1)}^2}}} > 0$, $\forall x \in D.$

Suy ra hàm số đồng biến trên các khoảng xác định.

Bảng biến thiên:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-23.png" alt="">

Hàm số không có cực trị.

Giá trị đặc biệt:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-24.png" alt="">

Đồ thị:

<img link="data_for_rag/toan12/images/mot-so-bai-toan-thuong-gap-ve-do-thi-25.png" alt="">

Nhận xét: Đồ thị $(C)$ nhận giao điểm $I(1;2)$ của hai tiệm cận làm tâm đối xứng.

b) Tìm phương trình đường cong $(C’)$ đối xứng với $(C)$ qua $(d): y = 2.$

Lấy $M'(x’;y’)$ bất kì thuộc $(C’).$ Gọi $H$ là hình chiếu của $M$ trên $(d)$ thì $H(x’;2).$

Gọi $M(x;y)$ là điểm đối xứng của $M’$ qua $(d): y = 2$ $\Leftrightarrow H$ là trung điểm của $MM’.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x = x’}\\
{y = 4 – y’}
\end{array}} \right.
$$
 $\Leftrightarrow M\left( {x’;4 – y’} \right).$

Ta có: $(C)$ và $(C’)$ đối xứng nhau qua $(d)$

$\Leftrightarrow M \in (C).$

$\Leftrightarrow 4 – y’ = \frac{{2x’ – 4}}{{x’ – 1}}$ $\Leftrightarrow y’ = 4 – \frac{{2x’ – 4}}{{x’ – 1}} = \frac{{2x’}}{{x’ – 1}}$ $\Leftrightarrow M’ \in \left( {C’} \right):y = \frac{{2x}}{{x – 1}}.$

Vậy $\left( {C’} \right):y = \frac{{2x}}{{x – 1}}$ là đường cong thỏa yêu cầu bài toán.

## Bài tập

## Bài tập 1. Cho hàm số $y = {x^3} – \frac{3}{2}m{x^2} + \frac{1}{3}{m^3}.$

a) Khảo sát hàm số khi $m = 1.$

b) Định $m$ để hàm số có các điểm cực đại, cực tiểu đối xứng nhau qua đường thẳng $y = x.$

## Bài tập 2. Cho $y = \frac{{3x + 1}}{{x – 3}}$ $(1).$

a) Khảo sát hàm số $(1).$

b) Tìm một hàm số mà đồ thị của nó đối xứng với đồ thị hàm số $(1)$ qua đường thẳng $x + y – 3 = 0.$

c) $C$ là điểm bất kì trên đồ thị $(1).$ Tiếp tuyến với đồ thị tại $C$ cắt tiệm cận đứng và ngang lần lượt tại $A$ và $B.$ Chứng minh $C$ là trung điểm $AB$ và diện tích tam giác tạo bởi tiếp tuyến đó và hai tiệm cận không đổi.

## Bài tập 3. Cho hàm số $y = \frac{{3{x^2}}}{{x – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số.

b) Tìm hai điểm $A$, $B$ thuộc $(C)$ sao cho chúng đối xứng nhau qua đường thẳng có phương trình $y = x – 1.$

## Bài tập 4. Cho hàm số $y = \frac{{{x^2} – 4mx + 5m}}{{x – 1}}.$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m = 1.$

b) Tìm $m$ để trên $\left( {{C_m}} \right)$ có hai điểm đối xứng nhau qua $O.$

## Bài tập 5. Cho hàm số $y = \frac{{{x^2} + (m – 1)x – m}}{{x + 1}}$ $(1).$

a) Khảo sát và vẽ đồ thị $(C)$ của hàm số khi $m=-1.$

b) Tìm $m$ để hàm số có cực đại, cực tiểu.

c) Định $m$ để đồ thị hàm số $(1)$ cắt trục $Ox$ tại hai điểm $M$, $N.$ Chứng tỏ $M$, $N$ không đối xứng nhau qua $O.$