# Tìm điều kiện để hàm số có cực trị

<!-- chunk:0 level:0 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm điều kiện để hàm số có cực trị trong chương trình Giải tích 12.

1. KIẾN THỨC CẦN NHỚ
Định lý 1: (Dấu hiệu I): Giả sử hàm số $y = f(x)$ có đạo hàm trên một lân cận của điểm ${x_0}$ (có thể trừ tại ${x_0}$).

1. Nếu $f'(x) > 0$ trên khoảng $\left( {{x_0} – \delta ,{x_0}} \right)$ và $f'(x) < 0$ trên khoảng $\left( {{x_0},{x_0} + \delta } \right)$ thì ${x_0}$ là một điểm cực đại của hàm số $f(x).$

2. Nếu $f'(x) < 0$ trên khoảng $\left( {{x_0} – \delta ,{x_0}} \right)$ và $f'(x) > 0$ trên khoảng $\left( {{x_0},{x_0} + \delta } \right)$ thì ${x_0}$ là một điểm cực tiểu của hàm số $f(x).$

Định lí 2 (Dấu hiệu II): Giả sử hàm số $y = f(x)$ có đạo hàm liên tục tới cấp $2$ tại ${x_0}$ và $f’\left( {{x_0}} \right) = 0$, $f”\left( {{x_0}} \right) \ne 0$ thì ${x_0}$ là một điểm cực trị của hàm số. Hơn nữa:

1. Nếu $f”\left( {{x_0}} \right) < 0$ thì hàm số đạt cực đại tại điểm ${x_0}.$

2. Nếu $f”\left( {{x_0}} \right) > 0$ thì hàm số đạt cực tiểu tại điểm ${x_0}.$

2. PHƯƠNG PHÁP CHUNG

Để thực hiện các yêu cầu về điều kiện có cực trị của hàm số $y = f(x)$ ta thực hiện theo các bước:

Bước 1: Miền xác định.

Bước 2: Tính đạo hàm $y’.$

Bước 3: Lựa chọn theo một trong hai hướng:

+ Hướng 1: Nếu xét được dấu của $y’$ thì sử dụng dấu hiệu $I$ với lập luận: Hàm số có $k$ cực trị $\Leftrightarrow$ Phương trình $y’ = 0$ có $k$ nghiệm phân biệt và đổi dấu qua các nghiệm đó.

+ Hướng 2: Nếu không xét được dấu của $y’$ hoặc bài toán yêu cầu cụ thể về cực đại hoặc cực tiểu thì sử dụng dấu hiệu $II$, bằng việc tính thêm $y”.$ Khi đó:

1. Hàm số có cực trị $\Leftrightarrow$ hệ sau có nghiệm thuộc $D$: 
$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y” \ne 0}
\end{array}} \right..
$$

2. Hàm số có cực tiểu $\Leftrightarrow$ hệ sau có nghiệm thuộc $D$: 
$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y” > 0}
\end{array}} \right..
$$

3. Hàm số có cực đại $\Leftrightarrow$ hệ sau có nghiệm thuộc $D$: 
$$
\left\{ {\begin{array}{l}
{y’ = 0}\\
{y” < 0}
\end{array}.} \right.
$$

4. Hàm số đạt cực tiểu tại ${x_0}$ điều kiện là: 
$$
\left\{ {\begin{array}{l}
{{x_0} \in D}\\
{{x_0}{\rm{\:là\:điểm\:tới\:hạn}}}\\
{y”\left( {{x_0}} \right) > 0}
\end{array}} \right..
$$

5. Hàm số đạt cực đại tại ${x_0}$ điều kiện là: 
$$
\left\{ {\begin{array}{l}
{{x_0} \in D}\\
{{x_0}{\rm{\:là\:điểm\:tới\:hạn}}}\\
{y”\left( {{x_0}} \right) < 0}
\end{array}} \right..
$$

(Điểm tới hạn: tại đó $f’\left( {{x_0}} \right)$ không xác định hoặc bằng $0$).

## Bài tập

<!-- chunk:1 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 1. Cho hàm số: $y = {x^3} + 3m{x^2} + 3\left( {{m^2} – 1} \right)x + {m^3} – 3m.$ Chứng minh rằng với mọi $m$ hàm số đã cho luôn có cực đại và cực tiểu, đồng thời chứng minh rằng khi $m$ thay đổi các điểm cực đại và cực tiểu của đồ thị hàm số luôn chạy trên hai đường thẳng cố định.

Miền xác định $D = R.$

Đạo hàm: $y’ = 3{x^2} + 6mx + 3\left( {{m^2} – 1} \right).$

$y’ = 0$ $\Leftrightarrow 3{x^2} + 6mx + 3\left( {{m^2} – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – m – 1}\\
{x = – m + 1}
\end{array}} \right..
$$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-ham-so-co-cuc-tri-1.png" alt="">

Vậy với mọi $m$ hàm số:

+ Đạt cực đại tại $x = – m – 1$ và ${y_{CĐ}} = 2$, đồng thời khi $m$ thay đổi điểm cực đại $B( – m – 1;2)$ luôn chạy trên đường thẳng cố định $y – 2 = 0.$

+ Đạt cực tiểu tại $x = – m + 1$ và ${y_{CT}} = – 2$, đồng thời khi $m$ thay đổi điểm cực tiểu $A( – m + 1; – 2)$ luôn chạy trên đường thẳng cố định $y + 2 = 0.$

<!-- chunk:2 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 2. Cho hàm số: $y = \frac{2}{3}{x^3} + (\cos a – 3\sin a){x^2} – 8(\cos 2a + 1)x + 1.$

a. Chứng minh rằng với mọi $a$ hàm số đã cho luôn có cực đại và cực tiểu.

b. Giả sử đạt cực đại và cực tiểu tại ${x_1}$, ${x_2}.$ Chứng minh rằng $x_1^2 + x_2^2 \le 18.$

a. Ta có:

Miền xác định $D = R.$

Đạo hàm: $y’ = 2{x^2} + 2(\cos a – 3\sin a)x – 8(\cos 2a + 1)$ $= 2{x^2} + 2(\cos a – 3\sin a)x – 16{\cos ^2}a.$

$y’ = 0$ $\Leftrightarrow {x^2} + (\cos a – 3\sin a)x – 8{\cos ^2}a = 0.$

Ta có $\Delta = {(\cos a – 3\sin a)^2} + 32{\cos ^2}a > 0$, $\forall a$ do đó phương trình $y’ = 0$ luôn có hai nghiệm phân biệt.

Vậy với mọi $m$ hàm số đã cho luôn có cực đại và cực tiểu.

b. Giả sử hàm số đạt cực đại và cực tiểu tại ${x_1}$, ${x_2}$ ta có:

$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = 3\sin a – \cos a}\\
{{x_1}{x_2} = – 8{{\cos }^2}a}
\end{array}} \right..
$$

Từ đó: $x_1^2 + x_2^2$ $= {\left( {{x_1} + {x_2}} \right)^2} – 2{x_1}{x_2}$ $= {(3\sin a – \cos a)^2} + 16{\cos ^2}a$ $= 13 + 4\cos 2a – 3\sin 2a$ $\le 13 + \sqrt {{4^2} + {3^2}} = 18.$

<!-- chunk:3 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 3. Cho hàm số: $y = 2{x^3} – 3(2m + 1){x^2} + 6m(m + 1)x + 1.$

a. Khảo sát sự biến thiên của hàm số với $m = – \frac{1}{2}.$

b. Chứng minh rằng với mọi $m$ hàm số luôn có cực đại và cực tiểu và hoành độ các điểm cực đại và cực tiểu thoả mãn ${x_1} – {x_2}$ không phụ thuộc tham số $m.$

Miền xác định $D = R.$

Đạo hàm: $y’ = 6{x^2} – 6(2m + 1)x + 6m(m + 1).$

$y’ = 0$ $\Leftrightarrow 6{x^2} – 6(2m + 1)x + 6m(m + 1) = 0.$

$\Leftrightarrow f(x) = {x^2} – (2m + 1)x + m(m + 1) = 0$ $(1).$

Trước hết hàm số có cực đại và cực tiểu $\Leftrightarrow (1)$ có hai nghiệm phân biệt.

$\Leftrightarrow \Delta > 0$ $\Leftrightarrow {(2m + 1)^2} – 4m(m + 1) > 0$ $\Leftrightarrow 1 > 0$ luôn đúng.

Khi đó phương trình $(1)$ có hai nghiệm phân biệt là:

$$
\left[ {\begin{array}{l}
{{x_1} = m}\\
{{x_2} = m + 1}
\end{array}} \right.
$$
 $\Rightarrow {x_1} – {x_2} = – 1$ không phụ thuộc tham số $m.$

<!-- chunk:4 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 4. Cho hàm số $y = {x^3} – 3m{x^2} + 4{m^3}.$ Để các điểm cực đại và cực tiểu của đồ thị hàm số đối xứng nhau qua đường thẳng $y = x$ thì $m$ nhận giá trị:

A. $m = \pm \frac{1}{{\sqrt 2 }}.$

B. $m = 0.$

C. $m = \pm 2.$

D. $m = \pm 3.$

Đáp số trắc nghiệm A.

Lời giải tự luận:

Ta lần lượt có:

+ Miền xác định $D = R.$

+ Đạo hàm: $y’ = 3{x^2} – 6mx$, $y’ = 0$ $\Leftrightarrow 3{x^2} – 6mx = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{{x_1} = 0}\\
{{x_2} = 2m}
\end{array}} \right.
$$
 $(1).$

Trước hết hàm số có cực đại và cực tiểu $\Leftrightarrow (1)$ có hai nghiệm phân biệt $\Leftrightarrow m \ne 0.$

Khi đó toạ độ các điểm cực trị là $A\left( {0;4{m^3}} \right)$ và $B(2m;0).$

Để các điểm cực đại và cực tiểu của đồ thị hàm số đối xứng với nhau qua đường thẳng $(d): y = x$:

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{AB \bot (d)}\\
{{\rm{trung\:điểm\:}}I{\rm{\:của\:}}AB{\rm{\:thuộc\:}}(d)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{\overrightarrow {AB} \bot \overrightarrow {{a_d}} }\\
{I\left( {m;2{m^3}} \right) \in (d)}
\end{array}} \right..
$$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{2m – 4{m^3} = 0}\\
{m – 2{m^3} = 0}
\end{array}} \right.
$$
 $\Leftrightarrow m = \pm \frac{1}{{\sqrt 2 }}$ (vì $m \ne 0$).

Vậy với $m = \pm \frac{1}{{\sqrt 2 }}$ thoả mãn điều kiện đầu bài.

Lựa chọn đáp án bằng phép thử:
 Trước tiên ta có:

$y’ = 3{x^2} – 6mx$, $y’ = 0$ $\Leftrightarrow 3{x^2} – 6mx = 0$ $(*).$

$y” = 6x – 6m$, $y” = 0$ $\Leftrightarrow x = m$ $\Rightarrow$ điểm uốn $U\left( {m;2{m^3}} \right).$

Khi đó:

+ Với $m = 0$ thì $(*)$ không có hai nghiệm phân biệt (nghiệm kép $x = 0$). Suy ra hàm số không có cực đại và cực tiểu nên đáp án B bị loại.

+ Với $m = 2$ thì điểm uốn $U(2;16)$ không thuộc đường thẳng $y = x.$ Suy ra đáp án C bị loại.

+ Với $m = 3$ thì điểm uốn $U(3;54)$ không thuộc đường thẳng $y = x.$ Suy ra đáp án D bị loại.

Do đó việc lựa chọn đáp án A là đúng đắn.

<!-- chunk:5 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 5. Cho hàm số $y = {x^4} – 2m{x^2} + 2m + {m^4}.$ Để hàm số có các điểm cực đại, cực tiểu lập thành một tam giác đều thì $m$ nhận giá trị:

A. $m = 0.$

B. $m = 1.$

C. $m = 4.$

D. $m = \sqrt[3]{3}.$

Đáp số trắc nghiệm D.

Lời giải tự luận:
Ta lần lượt có:

+ Miền xác định $D = R.$

+ Đạo hàm: $y’ = 4{x^3} – 4mx$ $= 4x\left( {{x^2} – m} \right)$, $y’ = 0$ $\Leftrightarrow x\left( {{x^2} – m} \right) = 0$ $(1).$

Hàm số có cực đại, cực tiểu khi và chỉ khi $(1)$ có ba nghiệm phân biệt $\Leftrightarrow m > 0.$

Khi đó $(1)$ có ba nghiệm phân biệt $x = 0$, $x = \pm \sqrt m$ và toạ độ ba điểm cực trị:

$A\left( {0;2m + {m^4}} \right)$, $B\left( { – \sqrt m ;{m^4} – {m^2} + 2m} \right)$, $C\left( {\sqrt m ;{m^4} – {m^2} + 2m} \right).$

Ta có $\Delta ABC$ đều khi và chỉ khi:

$$
\left\{ {\begin{array}{l}
{AB = AC{\rm{\:(luôn\:đúng)}}}\\
{AB = BC}
\end{array}} \right.
$$
 $\Leftrightarrow A{B^2} = B{C^2}$ $\Leftrightarrow m + {m^4} = 4m$ $\Leftrightarrow m = \sqrt[3]{3}$ (vì $m \ne 0$).

Vậy với $m = \sqrt[3]{3}$ thoả mãn điều kiện đầu bài.

Lựa chọn đáp án bằng phép thử:

Trước tiên ta có: $y’ = 4{x^3} – 4mx$ $= 4x\left( {{x^2} – m} \right)$, $y’ = 0$ $\Leftrightarrow x\left( {{x^2} – m} \right) = 0$ $(*).$

Khi đó:

+ Với $m = 0$ thì $(*)$ chỉ có một nghiệm ($x = 0$). Suy ra hàm số không có đủ ba cực trị để tạo thành tam giác nên đáp án A bị loại.

+ Với $m = 1$ thì từ nghiệm của $(*)$ ta được tọa độ ba điểm cực trị là: $A(0;3)$, $B( – 1;2)$, $C(1;2)$ $\Rightarrow A{B^2} = 1 + 1 = 2$ và $B{C^2} = 4$ $\Rightarrow \Delta ABC$ không đều. Suy ra đáp án B bị loại.

+ Với $m = 4$ thì từ nghiệm của $(*)$ ta được tọa độ ba điểm cực trị là: $A(0;264)$, $B( – 2;248)$, $C(2;248)$ $\Rightarrow A{B^2} = 4 + 256 = 260$ và $B{C^2} = 8$ $\Rightarrow \Delta ABC$ không đều. Suy ra đáp án C bị loại.

Do đó việc lựa chọn đáp án D là đúng đắn.

<!-- chunk:6 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 6. Cho hàm số: $y = k{x^4} + (k – 1){x^2} + 1 – 2k.$ Xác định các giá trị của tham số $k$ để hàm số chỉ có một điểm cực trị.

A. $k \in (0;1).$

B. $k \in ( – \infty ;0] \cup [1; + \infty ).$

C. $k \in ( – 1;1).$

D. $k \in ( – \infty ; – 1] \cup [1; + \infty ).$

Miền xác định $D = R.$

Đạo hàm: $y’ = 4k{x^3} + 2(k – 1)x$ $= 2x\left( {2k{x^2} + k – 1} \right).$

$y’ = 0$ $\Leftrightarrow 2x\left( {2k{x^2} + k – 1} \right) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = 0}\\
{f(x) = 2k{x^2} + k – 1 = 0}
\end{array}} \right..
$$

Hàm số chỉ có một điểm cực trị 
$$
\Leftrightarrow \left[ \begin{array}{l}
f(x) = 0{\rm{\:vô\:nghiệm\:\:}}(1)\\
\left\{ {\begin{array}{l}
{k \ne 0}\\
{\left[ {\begin{array}{l}
{f(x) = 0{\rm{\:có\:nghiệm\:kép\:\:}}(2)}\\
{f(0) = 0}
\end{array}} \right.}
\end{array}} \right.
\end{array} \right..
$$

Giải $(1)$: Ta xét:

+ Với $k = 0$ ta có: $f(x) = 0$ $\Leftrightarrow – 1 = 0$ mâu thuẫn. Vậy với $k = 0$ phương trình $f(x) = 0$ vô nghiệm.

+ Với $k \ne 0$: để $f(x) = 0$ vô nghiệm điều kiện là:

$\Delta < 0$ $\Leftrightarrow – 8k(k – 1) < 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k > 1}\\
{k < 0}
\end{array}} \right..
$$

Giải $(2)$: Ta được: 
$$
\left\{ {\begin{array}{l}
{k \ne 0}\\
{\left[ {\begin{array}{l}
{\Delta = 0}\\
{f(0) = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{k \ne 0}\\
{\left[ {\begin{array}{l}
{ – 8k(k – 1) = 0}\\
{k – 1 = 0}
\end{array}} \right.}
\end{array}} \right.
$$
 $\Leftrightarrow k = 1.$

Vậy hàm số chỉ có một điểm cực trị khi $k \in ( – \infty ;0] \cup [1; + \infty ).$

<!-- chunk:7 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 7. Cho hàm số: $y = \frac{1}{2}{x^4} – \frac{1}{3}{x^3} – mx + 2.$

a. Tìm $m$ để đồ thị hàm số có cực đại, cực tiểu.

A. $m > \frac{1}{2}.$

B. $0 < m < \frac{1}{2}.$

C. $m < – \frac{1}{{27}}.$

D. $– \frac{1}{{27}} < m < 0.$

b. Với kết quả ở câu a chứng tỏ rằng khi đó tổng bình phương hoành độ các điểm cực trị là một hằng số.

Miền xác định $D = R.$

Đạo hàm: $y’ = 2{x^3} – {x^2} – m$, $y’ = 0$ $\Leftrightarrow 2{x^3} – {x^2} – m = 0$ $\Leftrightarrow 2{x^3} – {x^2} = m$ $(1).$

a. Để đồ thị hàm số có cực đại, cực tiểu:

$\Leftrightarrow$ phương trình $(1)$ có ba nghiệm phân biệt.

$\Leftrightarrow$ đường thẳng $y = m$ cắt đồ thị hàm số $y = 2{x^3} – {x^2}$ tại ba điểm phân biệt.

Xét hàm số $y = 2{x^3} – {x^2}$ có miền xác định $D = R.$

+ Đạo hàm: $y’ = 6{x^2} – 2x$, $y’ = 0$ $\Leftrightarrow 6{x^2} – 2x = 0$ $\Leftrightarrow x = 0$ hoặc $x = \frac{1}{3}.$

+ Giới hạn: $\mathop {\lim }\limits_{x \to – \infty } y = – \infty$ và $\mathop {\lim }\limits_{x \to + \infty } y = + \infty .$

+ Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-ham-so-co-cuc-tri-2.png" alt="">

Dựa vào bảng biến thiên ta nhận được điều kiện để đồ thị hàm số có cực đại, cực tiểu là $– \frac{1}{{27}} < m < 0.$

b. Khi đó hoành độ các cực trị là nghiệm của phương trình $(1)$ và thoả mãn:

$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} + {x_3} = \frac{1}{2}}\\
{{x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1} = 0}\\
{{x_1}{x_2}{x_3} = \frac{m}{2}}
\end{array}} \right..
$$

Suy ra: $x_1^2 + x_2^2 + x_3^2$ $= {\left( {{x_1} + {x_2} + {x_3}} \right)^2}$ $– 2\left( {{x_1}{x_2} + {x_2}{x_3} + {x_3}{x_1}} \right) = \frac{1}{4}.$

Vậy khi hàm số có cực đại và cực tiểu thì tổng bình phương hoành độ các điểm cực trị là một hằng số.

<!-- chunk:8 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 8. Cho hàm số: $y = \frac{{2{x^2} + 3x + m – 2}}{{x + 2}}.$

Chứng tỏ rằng nếu hàm số đạt cực đại tại ${x_1}$ và cực tiểu tại ${x_2}$ thì ta có: $\left| {y\left( {{x_1}} \right) – y\left( {{x_2}} \right)} \right| = 4\left| {{x_1} – {x_2}} \right|.$

Miền xác định $D = R\backslash \{ – 2\} .$

Đạo hàm: $y’ = \frac{{2{x^2} + 8x – m + 8}}{{{{(x + 2)}^2}}}$, $y’ = 0$ $\Leftrightarrow f(x) = 2{x^2} + 8x – m + 8 = 0$ $(1).$

Hàm số có cực đại, cực tiểu $\Leftrightarrow (1)$ có hai nghiệm phân biệt khác $-2.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{f( – 2) \ne 0}\\
{\Delta ‘ > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{ – m \ne 0}\\
{2m > 0}
\end{array}} \right.
$$
 $\Leftrightarrow m > 0.$

Khi đó phương trình $(1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$, ta có:

$y\left( {{x_1}} \right) = \frac{{2x_1^2 + 3{x_1} + m – 2}}{{{x_1} + 2}}$ $= 4{x_1} + 3.$

$y\left( {{x_2}} \right) = \frac{{2x_2^2 + 3{x_2} + m – 2}}{{{x_2} + 2}}$ $= 4{x_2} + 3.$

Từ đó: $\left| {y\left( {{x_1}} \right) – y\left( {{x_2}} \right)} \right|$ $= \left| {4{x_1} – 4{x_2}} \right|$ $= 4\left| {{x_1} – {x_2}} \right|.$

<!-- chunk:9 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 9. Hàm số $y = \frac{{{x^2} – m(m + 1)x + {m^3} + 1}}{{x – m}}$ có cực đại và cực tiểu khi:

A. $m = 1.$

B. $m = 2.$

C. $m = 4.$

<!-- chunk:10 level:1 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## D. Mọi $m.$

Đáp số trắc nghiệm D.

Lời giải tự luận:

Ta lần lượt có:

+ Miền xác định $D = R\backslash \{ m\} .$

+ Viết lại hàm số dưới dạng:

$y = x – {m^2} + \frac{1}{{x – m}}$ $\Rightarrow y’ = 1 – \frac{1}{{{{(x – m)}^2}}}.$

$y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{{{(x – m)}^2}}} = 0$ $\Leftrightarrow {(x – m)^2} – 1 = 0$ $\Leftrightarrow x = m \pm 1 \in D.$

Tức là $y’ = 0$ có hai nghiệm phân biệt thuộc $D$ và đổi dấu qua hai nghiệm này, do đó hàm số luôn có cực đại và cực tiểu.

Lựa chọn đáp án bằng phép thử:

Lấy $m = 0$ hàm số có dạng:

$y = \frac{{{x^2} + 1}}{x} = x + \frac{1}{x}$ $\Rightarrow y’ = 1 – \frac{1}{{{x^2}}}.$

$y’ = 0$ $\Leftrightarrow 1 – \frac{1}{{{x^2}}} = 0$ $\Leftrightarrow {x^2} – 1 = 0$ $\Leftrightarrow x = \pm 1 \in D.$

Tức là $y’ = 0$ có hai nghiệm phân biệt thuộc $D$ và đổi dấu qua hai nghiệm này, do đó hàm số có cực đại và cực tiểu tại $m = 0$ (chỉ có ở đáp án D).

Do đó việc lựa chọn đáp án D là đúng đắn.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 10. Xác định giá trị của tham số để các hàm số sau có cực trị:

$y = \frac{{{x^2} + 2mx – m}}{{x + m}}$ với $m$ là tham số.

A. $m > 2.$

B. $m < 0.$

C. $0 < m < 1.$

D. $– 1 < m < 0.$

Miền xác định $D = R\backslash \{ – m\} .$

Đạo hàm $y’ = \frac{{{x^2} + 2mx + 2{m^2} + m}}{{{{(x + m)}^2}}}$, $y’ = 0$ $\Leftrightarrow {x^2} + 2mx + 2{m^2} + m = 0.$

Để hàm số có cực trị điều kiện là: $y’ = 0$ có hai nghiệm phân biệt.

$\Leftrightarrow \Delta ‘ > 0$ $\Leftrightarrow – {m^2} – m > 0$ $\Leftrightarrow – 1 < m < 0.$

Vậy với $-1 < m < 0$ thoả mãn điều kiện đầu bài.

> **Đáp án: D**

<!-- chunk:12 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 11. Cho hàm số: $y = \frac{{{x^2} + mx – 2}}{{mx – 1}}.$

Xác định $m$ để:

a. Hàm số có cực trị.

A. $|m| < 1.$

B. $|m| > 2.$

C. $1 < m < 2.$

D. $– 2 < m < 1.$

b. Hàm số có cực đại, cực tiểu với hoành độ thoả mãn ${x_1} + {x_2} = 4{x_1}{x_2}.$

A. $m = \frac{1}{2}.$

B. $m = \frac{5}{2}.$

C. $m = \frac{3}{2}.$

D. $m = – \frac{3}{2}.$

c. Hàm số có cực đại, cực tiểu với hoành độ dương.

A. $0 < m < 1.$

B. $m > 2.$

C. $0 < m < 2.$

D. $– 2 < m < 0.$

Miền xác định $D = R\backslash \left\{ {\frac{1}{m}} \right\}.$

Đạo hàm: $y’ = \frac{{m{x^2} – 2x + m}}{{{{(mx – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow f(x) = m{x^2} – 2x + m = 0$ $(1).$

a. Xét hai trường hợp:

Trường hợp 1. Nếu $m = 0$ ta được: $y’ = – 2x$, $y’ = 0$ $\Leftrightarrow x = 0.$

Vì qua $x = 0$ đạo hàm $y’$ đổi dấu, do đó $m = 0$ thoả mãn.

Trường hợp 2. Nếu $m \ne 0.$

Điều kiện là phương trình $(1)$ có hai nghiệm phân biệt.

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \ne 0}\\
{\Delta ‘ > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{1 – {m^2} > 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{|m| < 1}
\end{array}} \right..
$$

Vậy với $|m| < 1$ hàm số có cực trị.

b. Trước hết hàm số có cực đại, cực tiểu $\Leftrightarrow$ phương trình $(1)$ có hai nghiệm phân biệt khác $\frac{1}{m}.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \ne 0}\\
{\Delta ‘ > 0}\\
{f( – 1/m) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{1 – {m^2} > 0}\\
{m – 1/m \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{|m| < 1}
\end{array}} \right.
$$
 $(*).$

Khi đó phương trình $(1)$ có hai nghiệm ${x_1}$ và ${x_2}$ thoả mãn: 
$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = \frac{2}{m}}\\
{{x_1}.{x_2} = 1}
\end{array}} \right..
$$

Suy ra: ${x_1} + {x_2} = 4{x_1}{x_2}$ $\Leftrightarrow \frac{2}{m} = 4$ $\Leftrightarrow m = \frac{1}{2}$ thoả mãn điều kiện $(*).$

Vậy với $m = \frac{1}{2}$ thoả mãn điều kiện đầu bài.

c. Hàm số có cực đại, cực tiểu với hoành độ dương $\Leftrightarrow$ phương trình $(1)$ có hai nghiệm phân biệt dương khác $\frac{1}{m}.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{a \ne 0}\\
{\Delta ‘ > 0}\\
{af(0) > 0}\\
{0 < S/2}\\
{f( – 1/m) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{1 – {m^2} > 0}\\
{{m^2} > 0}\\
{1/m > 0}\\
{m – 1/m \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow 0 < m < 1.$

Vậy với $0 < m < 1$ thoả mãn điều kiện đầu bài.

Đáp án trắc nghiệm: a. A – b. A – c. A.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 12. Cho hàm số: $y = \frac{{m{x^2} + x + m}}{{x + 1}}.$

a. Khảo sát sự biến thiên của hàm số với $m = 1.$

b. Tìm $m$ để hàm số không có cực trị.

A. ${m \le \frac{3}{2}}.$

B. ${m \ge 1.}$

C. ${m \ge 6.}$

D. ${0 \le m \le \frac{1}{2}.}$

Đáp án trắc nghiệm: b. D.

a. Bạn đọc tự giải.

b. Miền xác định $D = R\backslash \{ – 1\} .$

Viết lại hàm số dưới dạng: $y = mx – m + 1 + \frac{{2m – 1}}{{x + 1}}.$

Đạo hàm: $y’ = m – \frac{{2m – 1}}{{{{(x + 1)}^2}}}$ $= \frac{{m{x^2} + 2mx – m + 1}}{{{{(x + 1)}^2}}}.$

$y’ = 0$ $\Leftrightarrow f(x) = m{x^2} + 2x – m + 1 = 0.$

Để hàm số không có cực trị điều kiện là:

$$
\left[ {\begin{array}{l}
{{\rm{Hàm\:số\:suy\:biến}}}\\
{y’ \ge 0{\rm{\:với\:mọi\:}}x \in D}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{2m – 1 = 0}\\
{\Delta ‘ \le 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = 0}\\
{2m – 1 = 0}\\
{2{m^2} – m \le 0}
\end{array}} \right.
$$
 $\Leftrightarrow 0 \le m \le \frac{1}{2}.$

Vậy với $0 \le m \le \frac{1}{2}$ thoả mãn điều kiện đầu bài.

<!-- chunk:14 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 13. Cho hàm số: $y = \frac{{m{x^2} + \left( {{m^2} + 1} \right)x + 4{m^3} + m}}{{x + m}}.$ Xác định $m$ để hàm số có một điểm cực trị thuộc góc phần tư thứ $(II)$, một điểm cực trị thuộc góc phần tư thứ $(IV).$

A. $m < – \frac{1}{{\sqrt 5 }}.$

B. $m < \frac{1}{3}.$

C. $m > \sqrt 2 .$

D. $\sqrt 2 < m < 6.$

Miền xác định $D = R\backslash \{ – m\} .$

Đạo hàm: $y’ = \frac{{m{x^2} + 2{m^2}x – 3{m^3}}}{{{{(x + m)}^2}}}$, $y’ = 0$ $\Leftrightarrow f(x) = m{x^2} + 2{m^2}x – 3{m^3} = 0$ $(1).$

Để hàm số có hai cực trị điều kiện là: $(1)$ có hai nghiệm phân biệt khác $– m$ 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\Delta ‘ > 0}\\
{f( – m) \ne 0}
\end{array}} \right.
$$
 $\Leftrightarrow m \ne 0.$

Khi đó phương trình $(1)$ có hai nghiệm phân biệt ${x_1} = m$, ${x_2} = – 3m$ và toạ độ hai điểm cực trị là: $A\left( {m;3{m^2} + 1} \right)$, $B\left( { – 3m; – 5{m^2} + 1} \right).$

Để hàm số có một điểm cực trị thuộc góc phần tư thứ $(II)$ và một điểm cực trị thuộc góc phần tư thứ $(IV)$ ta phải có:

$$
\left\{ {\begin{array}{l}
{A \in P(II)}\\
{B \in P(IV)}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{c}
{m < 0{\rm{\:và\:}}3{m^2} + 1 > 0}\\
{ – 3m > 0{\rm{\:và\:}} – 5{m^2} + 1 < 0}
\end{array}} \right.
$$
 $\Leftrightarrow m < – \frac{1}{{\sqrt 5 }}.$

Vậy với $m < – \frac{1}{{\sqrt 5 }}$ thoả mãn điều kiện đầu bài.

Đáp án trắc nghiệm: A.

<!-- chunk:15 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 14. Cho hàm số: $y = \frac{{m{x^2} + 3mx + 2m + 1}}{{x – 1}}.$ Xác định các giá trị của tham số $m$ để hàm số có cực đại, cực tiểu và hai điểm đó nằm về hai phía đối với trục $Ox.$

A. $0 < m < 1.$

B. $1 < m < 4.$

C. $0 < m < 4.$

D. $m > \frac{5}{4}.$

Miền xác định $D = R\backslash \{ 1\} .$

Đạo hàm: $y’ = \frac{{m{x^2} – 2mx – 5m – 1}}{{{{(x – 1)}^2}}}$, $y’ = 0$ $\Leftrightarrow m{x^2} – 2mx – 5m – 1 = 0$ $(1).$

Hàm số có cực trị $\Leftrightarrow$ phương trình $(1)$ có hai nghiệm phân biệt khác $1.$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{\Delta ‘ > 0}\\
{f(1) \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m \ne 0}\\
{6{m^2} + m > 0}\\
{ – 6m – 1 \ne 0}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 0}\\
{m < – \frac{1}{6}}
\end{array}} \right.
$$
 $(2).$

Tới đây chúng ta có thể lựa chọn một trong hai cách trình bày sau:

Cách 1: Với điều kiện $(2)$ phương trình $(1)$ có hai nghiệm phân biệt ${x_1}$, ${x_2}$ thoả mãn:

$$
\left\{ {\begin{array}{l}
{{x_1} + {x_2} = 2}\\
{{x_1}.{x_2} = – \frac{{5m + 1}}{m}}
\end{array}} \right..
$$

Ta có:

$y\left( {{x_1}} \right) = \frac{{mx_1^2 + 3m{x_1} + 2m + 1}}{{{x_1} – 1}}$ $= 2m{x_1} + 3m.$

$y\left( {{x_2}} \right) = \frac{{mx_2^2 + 3m{x_2} + 2m + 1}}{{{x_2} – 1}}$ $= 2m{x_2} + 3m.$

Hai điểm cực đại, cực tiểu nằm về hai phía đối với trục $Ox$:

$\Leftrightarrow y\left( {{x_1}} \right)y\left( {{x_2}} \right) < 0$ $\Leftrightarrow \left( {2m{x_1} + 3m} \right)\left( {2m{x_2} + 3m} \right) < 0.$

$\Leftrightarrow {m^2}\left[ {4{x_1}{x_2} + 6\left( {{x_1} + {x_2}} \right) + 9} \right] < 0.$

$\Leftrightarrow {m^2} – 4m < 0$ $\Leftrightarrow 0 < m < 4$ $(3).$

Kết hợp $(2)$ và $(3)$ ta được $0 < m < 4.$

Vậy với $0 < m < 4$ thoả mãn điều kiện đầu bài.

Cách 2: Sử dụng đồ thị.

Hai điểm cực đại, cực tiểu nằm về hai phía đối với trục $Ox.$

$\Leftrightarrow y = 0$ vô nghiệm $\Leftrightarrow m{x^2} + 3mx + 2m + 1 = 0$ vô nghiệm.

$\Leftrightarrow \Delta < 0$ $\Leftrightarrow 9{m^2} – 4m(2m + 1) < 0$ $\Leftrightarrow {m^2} – 4m < 0.$

$\Leftrightarrow 0 < m < 4$ $(4).$

Kết hợp $(2)$ và $(4)$ ta được $0 < m < 4.$

Vậy với $0 < m < 4$ thoả mãn điều kiện đầu bài.

> **Đáp án: C**

<!-- chunk:16 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 15. Cho hàm số: $y = 2x + \left| {{x^2} – 4x + 4m} \right|.$

a. Khảo sát sự biến thiên của hàm số với $m = 1.$

b. Tìm $m$ để hàm số có cực đại.

A. $m < \frac{3}{4}.$

B. $m < \frac{1}{3}.$

C. $m > 2.$

D. $1 < m < 2.$

a. Bạn đọc tự giải.

b. Nhận xét rằng hàm số $y = a{x^2} + bx + c$ có cực đại $\Leftrightarrow a < 0.$

Xét $g(x) = {x^2} – 4x + 4m$, ta có $\Delta ‘ = 4(1 – m).$

Ta đi xét các trường hợp sau:

Trường hợp 1: Nếu $\Delta ‘ \le 0$ $\Leftrightarrow 1 – m \le 0$ $\Leftrightarrow m \ge 1.$

Khi đó $g(x) \ge 0$, $\forall x$, vậy hàm số có dạng:

$y = {x^2} – 2x + 4m.$

Hàm số không thể có cực đại. Vậy không thoả mãn điều kiện đầu bài.

Trường hợp 2: Nếu $\Delta ‘ > 0$ $\Leftrightarrow 1 – m > 0$ $\Leftrightarrow m < 1.$

Khi đó $g(x) = 0$ có hai nghiệm phân biệt là: $x = 2 \pm 2\sqrt {1 – m} .$

Ta có bảng xét dấu của $g(x)$ như sau:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-ham-so-co-cuc-tri-3.png" alt="">

Nhận xét rằng:

+ Nếu $x \le {x_1}$ hoặc $x \ge {x_2}$ hàm số có dạng $y = {x^2} – 2x + 4m.$

Hàm số không thể có cực đại. Vậy không thoả mãn điều kiện đầu bài.

+ Nếu ${x_1} < x < {x_2}$ hàm số có dạng $y = – {x^2} + 6x – 4m.$

Miền xác định $D = \left( {{x_1};{x_2}} \right).$

Đạo hàm: $y’ = – 2x + 6$, $y’ = 0$ $\Leftrightarrow – 2x + 6 = 0$ $\Leftrightarrow x = 3.$

Hàm số có cực đại khi:

${x_1} < 3 < {x_2}$ $\Leftrightarrow 2 – 2\sqrt {1 – m} < 3 < 2 + 2\sqrt {1 – m}$ $\Leftrightarrow \frac{1}{2} < \sqrt {1 – m}$ $\Leftrightarrow m < \frac{3}{4}.$

Vậy với $m < \frac{3}{4}$ hàm số có cực đại.

<!-- chunk:17 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 16. Cho hàm số: $y = x + \left| {{x^2} – 2x + 2m} \right|.$

Tìm $m$ để hàm số có cực đại và số cực đại ${y_{CĐ}} < 13.$

A. $0 < m < \frac{3}{4}.$

B. $m > 2.$

C. $m < 9.$

D. $– \frac{{43}}{4} < m < \frac{3}{4}.$

Xét $g(x) = {x^2} – 2x + m$, ta có $\Delta ‘ = 1 – m.$

Ta đi xét các trường hợp sau:

Trường hợp 1: Nếu $\Delta ‘ \le 0$ $\Leftrightarrow 1 – m \le 0$ $\Leftrightarrow m \ge 1.$

Khi đó $g(x) \ge 0$, $\forall x$, vậy hàm số có dạng: $y = x + {x^2} – 2x + m$ $\Leftrightarrow y = {x^2} – x + m.$

Hàm số không thể có cực đại.

Vậy không thoả mãn điều kiện đầu bài.

Trường hợp 2: Nếu $\Delta ‘ > 0$ $\Leftrightarrow 1 – m > 0$ $\Leftrightarrow m < 1.$

Khi đó phương trình $g(x) = 0$ có hai nghiệm phân biệt là:

${x_1} = 1 – \sqrt {1 – m}$ và ${x_2} = 1 + \sqrt {1 – m} .$

Hàm số được viết lại dưới dạng: 
$$
y = \left\{ \begin{array}{l}
{x^2} – x + m{\rm{\:với\:}}x < {x_1}{\rm{\:hoặc\:}}x > {x_2}\\
– {x^2} + 3x – m{\rm{\:với\:}}{x_1} \le x \le {x_2}
\end{array} \right..
$$

Đạo hàm: 
$$
y’ = \left\{ {\begin{array}{l}
{2x – 1{\rm{\:với\:}}x < {x_1}{\rm{\:hoặc\:}}x > {x_2}}\\
{ – 2x + 3{\rm{\:với\:}}{x_1} \le x \le {x_2}}
\end{array}} \right..
$$

Xét các khả năng:

a. Nếu $\frac{1}{2} \le 1 – \sqrt {1 – m}$ thì $\sqrt {1 – m} \le \frac{1}{2}$ $\Leftrightarrow m \ge \frac{3}{4}$ $\Rightarrow {x_2} = 1 + \sqrt {1 – m} \le \frac{3}{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-ham-so-co-cuc-tri-4.png" alt="">

Hàm số không có cực đại.

b. Nếu $\frac{1}{2} > 1 – \sqrt {1 – m}$ thì $\sqrt {1 – m} > \frac{1}{2}$ $\Leftrightarrow m < \frac{3}{4}$ $\Rightarrow {x_2} = 1 + \sqrt {1 – m} > \frac{3}{2}.$

Bảng biến thiên:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-ham-so-co-cuc-tri-5.png" alt="">

Hàm số đạt cực đại tại $x = \frac{3}{2}.$ Khi đó để ${y_{CĐ}} < 13$ điều kiện là:

$y\left( {\frac{3}{2}} \right) < 13$ $\Leftrightarrow \frac{9}{4} – m < 13$ $\Leftrightarrow m > – \frac{{43}}{4}.$

Vậy với $– \frac{{43}}{4} < m < \frac{3}{4}$ thoả mãn điều kiện đầu bài.

> **Đáp án: D**

<!-- chunk:18 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 17. Cho hàm số: $y = \frac{{x + a}}{{\sqrt {{x^2} + 1} }}.$ Tìm $a$ để:

a. Hàm số không có cực trị.

A. $a = 0.$

B. $a = 1.$

C. $a = 2.$

D. $a = 3.$

b. Hàm số có cực tiểu.

A. $a > 0.$

B. $a < 0.$

C. $a > 1.$

D. $0 < a < 1.$

Miền xác định $D = R.$

Đạo hàm: $y’ = \frac{{ – ax + 1}}{{\left( {{x^2} + 1} \right)\sqrt {{x^2} + 1} }}$, $y’ = 0$ $\Leftrightarrow 1 – ax = 0$ $(1).$

a. Hàm số không có cực trị $\Leftrightarrow$ phương trình $(1)$ vô nghiệm $\Leftrightarrow a = 0.$

b. Hàm số có cực tiểu $\Leftrightarrow (1)$ có nghiệm và qua đó $y’$ đổi dấu từ âm sang dương $\Leftrightarrow a < 0.$

<!-- chunk:19 level:4 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## Bài tập 18. Cho hàm số: $y = – 2x + 2 + m\sqrt {{x^2} – 4x + 5} .$

Tìm $m$ để hàm số có cực đại.

A. $m > 0.$

B. $m < -2.$

C. $m > -2.$

<!-- chunk:20 level:1 source:https://toanmath.com/2019/10/tim-dieu-kien-de-ham-so-co-cuc-tri.html -->
## D. Vô nghiệm.

Miền xác định $D = R.$

Đạo hàm: $y’ = – 2 + m.\frac{{x – 2}}{{\sqrt {{x^2} – 4x + 5} }}$ và $y” = \frac{m}{{{{\left( {{x^2} – 4x + 5} \right)}^{3/2}}}}.$

Dấu $y’$ phụ thuộc $m$ nên điều kiện cần để hàm số có cực đại là $m < 0.$

Khi đó hàm số có cực đại $\Leftrightarrow$ phương trình $y’ = 0$ có nghiệm.

Ta có: $y’ = 0$ $\Leftrightarrow 2\sqrt {{x^2} – 4x + 5} = m(x – 2).$

$$
\Leftrightarrow \left\{ {\begin{array}{l}
{m(x – 2) \ge 0}\\
{4\left( {{x^2} – 4x + 5} \right) = {m^2}{{(x – 2)}^2}}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{x – 2 \le 0}\\
{\left( {{m^2} – 4} \right){{(x – 2)}^2} = 4}
\end{array}} \right..
$$

Do đó để $y’ = 0$ có nghiệm điều kiện là: $\frac{4}{{{m^2} – 4}} > 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m > 2}\\
{m < – 2}
\end{array}} \right..
$$

Vậy hàm số có cực đại khi $m < -2$ và khi đó hoành độ điểm cực đại là: $x = 2 – \frac{2}{{\sqrt {{m^2} – 4} }}.$