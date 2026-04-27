# Tìm điều kiện để phương trình f(x) = g(m) có n nghiệm liên quan đến giá trị tuyệt đối

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
Bài viết hướng dẫn phương pháp giải bài toán tìm điều kiện để phương trình f(x) = g(m) có n nghiệm liên quan đến giá trị tuyệt đối trong chương trình Giải tích 12: ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## I. PHƯƠNG PHÁP GIẢI TOÁN

Để giải quyết phương trình có liên quan đến giá trị tuyệt đối. Ta thường sử dụng một trong hai cách sau đây:

+ Sử dụng đồ thị hàm số trị tuyệt đối để giải và biện luận các phương trình dạng này.

+ Bỏ dấu giá trị tuyệt đối theo qui tắc: 
$$
\left| A \right| = \left\{ {\begin{array}{l}
A&{{\rm{khi}}\:\:A \ge 0}\\
{ – A}&{{\rm{khi}}\:\:A < 0}
\end{array}} \right..
$$

Sau đó khảo sát sự biến thiên của hàm số để xác định điều kiện tham số cần tìm.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## Ví dụ 1. Tìm điều kiện của tham số $m$ để phương trình $\left| {x – 1} \right|\left( {{x^2} – 2x} \right) = m.$

a) Có nghiệm.

b) Có hai nghiệm phân biệt.

c) Có ba nghiệm phân biệt.

d) Có bốn nghiệm phân biệt.

Cách 1: Ta vẽ đồ thị hàm số $y = \left| {x – 1} \right|\left( {{x^2} – 2x – 2} \right).$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-1.png" alt="">

Quan sát đồ thị hàm số, ta thấy:

+ Phương trình bài ra có nghiệm khi $m \ge – 2.$

+ Phương trình bài ra có hai nghiệm phân biệt khi 
$$
\left[ {\begin{array}{l}
{m = – 2}\\
{m > 0}
\end{array}} \right..
$$

+ Phương trình bài ra có ba nghiệm phân biệt khi $m = 0.$

+ Phương trình bài ra có bốn nghiệm phân biệt khi $– 2 < m < 0.$

Cách 2: Bài tập này ta cũng có thể đặt ẩn phụ $t = |x – 1|.$

Khi đó $\left| {x – 1} \right|\left( {{x^2} – 2x} \right) = m$ $\Leftrightarrow \left| {x – 1} \right|\left[ {{{(x – 1)}^2} – 3} \right] = m.$

Đặt $t = \left| {x – 1} \right| \ge 0.$ Ta có phương trình $m = {t^3} – 3t.$

Xét hàm số $f(t) = {t^3} – 3t$ với $t \ge 0.$

Ta có: $f'(t) = 3{t^2} – 3 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{t = 1}\\
{t = – 1\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-2.png" alt="">

Với chú ý: $t = 0$ $\Leftrightarrow x = 0$, $t > 0$ thì có hai nghiệm $x$ tương ứng.

Khi đó ta có kết luận bài toán giống như cách 1.

<!-- chunk:3 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## Ví dụ 2. Tìm điều kiện của tham số $m$ để phương trình $\left| {{x^4} – 2{x^2} – 3} \right| = 2m + 3$ thỏa mãn:

a) Có năm nghiệm phân biệt.

b) Có bốn nghiệm phân biệt.

c) Có sáu nghiệm phân biệt.

d) Có hai nghiệm phân biệt.

Ta vẽ đồ thị hàm số $y = \left| {{x^4} – 2{x^2} – 3} \right|.$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-3.png" alt="">

Từ đồ thị hàm số $y = \left| {{x^4} – 2{x^2} – 3} \right|$, ta thấy:

+ Phương trình bài ra có năm nghiệm phân biệt khi $2m + 3 = 3$ $\Leftrightarrow m = 0.$

+ Phương trình bài ra có bốn nghiệm phân biệt khi:

$$
\left[ {\begin{array}{l}
{0 < 2m + 3 < 3}\\
{2m + 3 = 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{ – \frac{3}{2} < m < 0}\\
{m = \frac{1}{2}}
\end{array}} \right..
$$

+ Phương trình bài ra có sáu nghiệm phân biệt khi:

$3 < 2m + 3 < 4$ $\Leftrightarrow 0 < m < \frac{1}{2}.$

+ Phương trình bài ra có hai nghiệm phân biệt khi:

$$
\left[ {\begin{array}{l}
{2m + 3 = 0}\\
{2m + 3 > 4}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{m = – \frac{3}{2}}\\
{m > \frac{1}{2}}
\end{array}} \right..
$$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## Ví dụ 3. Cho phương trình $\left| {{x^3} – 3{x^2} + 4} \right| = m.$ Tính tổng tất cả các giá trị của tham số $m$ sao cho phương trình đã cho có hai nghiệm ${x_1}$, ${x_2}$ phân biệt thỏa mãn $– 1 < {x_1} < {x_2} < 2.$

Vẽ đồ thị hàm số $y = \left| {{x^3} – 3{x^2} + 4} \right|$, ta có:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-4.png" alt="">

Quan sát đồ thị hàm số, ta thấy để phương trình bài ra có đúng hai nghiệm ${x_1}$, ${x_2}$ phân biệt thỏa mãn $– 1 < {x_1} < {x_2} < 2$ thì $0 < m < 4.$ Mà $m \in Z$ $\Rightarrow m \in \{ 1;2;3\} .$

Do đó tổng các giá trị tham số $m$ thỏa mãn bài toán là $1+2+3=6.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## Ví dụ 4. Tìm điều kiện của tham số $m$ để phương trình $\left| {{x^2} – 2x} \right| + 4x – 5 – m = 0$ thỏa mãn:

a) Có nghiệm.

a) Có hai nghiệm phân biệt.

Ta có $\left| {{x^2} – 2x} \right| + 4x – 5 – m = 0$ $\Leftrightarrow m = \left| {{x^2} – 2x} \right| + 4x – 5.$

Xét hàm số $f(x) = \left| {{x^2} – 2x} \right| + 4x – 5$ 
$$
= \left\{ {\begin{array}{l}
{{x^2} – 2x + 4x – 5\:\:{\rm{khi}}\:\:x \le 0,x \ge 2}\\
{ – {x^2} + 2x + 4x – 5\:\:{\rm{khi}}\:\:0 < x < 2}
\end{array}} \right..
$$

$$
= \left\{ {\begin{array}{l}
{{x^2} + 2x – 5\:\:{\rm{khi}}\:\:x \le 0,x \ge 2}\\
{ – {x^2} + 6x – 5\:\:{\rm{khi}}\:\:0 < x < 2}
\end{array}} \right..
$$

Suy ra 
$$
f'(x) = \left\{ {\begin{array}{l}
{2x + 2\:\:{\rm{khi}}\:\:x \le 0,x \ge 2}\\
{ – 2x + 6\:\:{\rm{khi}}\:\:0 < x < 2}
\end{array}} \right..
$$

Do đó $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 1}\\
{x = 3\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-5.png" alt="">

Từ bảng biến thiên của hàm số, ta thấy:

+ Phương trình bài ra có nghiệm khi $m \ge – 6.$

+ Phương trình bài ra có hai nghiệm phân biệt khi $m > -6.$

Chú ý: Tại $x = 0$ hoặc $x = 2$ thì hàm số không có đạo hàm, tuy nhiên hai giá trị này vẫn thuộc tập xác định của hàm số và trong trường hợp lấy làm nghiệm thì nó vẫn là các nghiệm của bài toán.

<!-- chunk:6 level:3 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## Ví dụ 5. Cho phương trình $\left| {x – 1} \right| + 2{x^2} – 7x – m + 3 = 0.$ Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình đã cho có nghiệm trên đoạn $[ – 3;5].$

Ta có $\left| {x – 1} \right| + 2{x^2} – 7x – m + 3 = 0$ $\Leftrightarrow m = \left| {x – 1} \right| + 2{x^2} – 7x + 3.$

Xét hàm số $f(x) = \left| {x – 1} \right| + 2{x^2} – 7x + 3.$

$$
= \left\{ {\begin{array}{l}
{x – 1 + 2{x^2} – 7x + 3\:\:{\rm{khi}}\:\:x \ge 1}\\
{ – x + 1 + 2{x^2} – 7x + 3\:\:{\rm{khi}}\:\:x < 1}
\end{array}} \right..
$$

$$
= \left\{ {\begin{array}{l}
{2{x^2} – 6x + 2\:\:{\rm{khi}}\:\:x \ge 1}\\
{2{x^2} – 8x + 4\:\:{\rm{khi}}\:\:x < 1}
\end{array}} \right..
$$

Suy ra: 
$$
f'(x) = \left\{ {\begin{array}{l}
{4x – 6\:\:{\rm{khi}}\:\:x \ge 1}\\
{4x – 8\:\:{\rm{khi}}\:\:x < 1}
\end{array}} \right..
$$

Do đó $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = \frac{3}{2}}\\
{x = 2\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-6.png" alt="">

Từ bảng biến thiên của hàm số, ta suy ra để phương trình bài ra có hai nghiệm phân biệt trên đoạn $[-3;5]$ khi $m \in \left( { – \frac{5}{2};22} \right].$ Do đó có $25$ giá trị nguyên của $m$ thỏa mãn bài toán là: $m \in \{ – 2; – 1;0;1;2; \ldots ;22\} .$

<!-- chunk:7 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## III. BÀI TẬP TRẮC NGHIỆM
## Bài 1. Tìm điều kiện của tham số $m$ để phương trình $3m = \left| {{x^3} – 6{x^2} + 9x – 7} \right|$ có bốn nghiệm phân biệt.

A. $m \in \left( {1;\frac{7}{3}} \right).$

B. $m \in \left( {\frac{7}{3}; + \infty } \right).$

C. $m \in (0;1).$

D. $m \in ( – \infty ;0).$

Ta có: $3m = \left| {{x^3} – 6{x^2} + 9x – 7} \right|$ $\Leftrightarrow m = \left| {\frac{1}{3}{x^3} – 2{x^2} + 3x – \frac{7}{3}} \right|.$

Vẽ đồ thị hàm số $f(x) = \left| {\frac{1}{3}{x^3} – 2{x^2} + 3x – \frac{7}{3}} \right|.$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-7.png" alt="">

Từ đồ thị hàm số ta thấy, phương trình bài ra có bốn nghiệm phân biệt khi $1 < m < \frac{7}{3}.$

> **Đáp án: B**

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để phương trình $m = \left| {{x^3} – 3{x^2} – 4} \right| – 2$ có bốn nghiệm phân biệt.

A. $m \in (4;8).$

B. $m \in (2;6).$

C. $m \in (0;4).$

D. $m \in (8; + \infty ).$

Ta có $m = \left| {{x^3} – 3{x^2} – 4} \right| – 2$ $\Leftrightarrow m + 2 = \left| {{x^3} – 3{x^2} – 4} \right|.$

Vẽ đồ thị hàm số $f(x) = \left| {{x^3} – 3{x^2} – 4} \right|.$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-8.png" alt="">

Từ đồ thị hàm số, ta có phương trình bài ra có bốn nghiệm phân biệt khi: $4 < m + 2 < 8$ $\Leftrightarrow 2 < m < 6.$

> **Đáp án: B**

## Bài 3. Tìm các giá trị của tham số $m$ để phương trình $2 – 3m = \left| {{x^4} – 2{x^2} – 1} \right|$ có năm nghiệm phân biệt.

A. $m = -2.$

B. $m = – \frac{2}{3}.$

C. $m = 0.$

D. $m = 5.$

Ta vẽ đồ thị hàm số $y = \left| {{x^4} – 2{x^2} – 1} \right|.$

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-9.png" alt="">

Từ đồ thị hàm số, ta thấy phương trình bài ra có $5$ nghiệm phân biệt khi $2 – 3m = 2$ $\Leftrightarrow m = 0.$

> **Đáp án: C**

## Bài 4. Có bao nhiêu giá trị nguyên của tham số $m$ sao cho phương trình $\left| {x – 3} \right| + {x^2} + 3x – 5 – m = 0$ có hai nghiệm phân biệt trên khoảng $(-6;5).$

A. $23.$

B. $24.$

C. $28.$

D. $30.$

Ta có $|x – 3| + {x^2} + 3x – 5 – m = 0$ $\Leftrightarrow |x – 3| + {x^2} + 3x – 5 = m.$

Xét hàm số $f(x) = |x – 3| + {x^2} + 3x – 5$ 
$$
= \left\{ {\begin{array}{l}
{x – 3 + {x^2} + 3x – 5\:\:{\rm{khi}}\:\:x \ge 3}\\
{ – x + 3 + {x^2} + 3x – 5\:\:{\rm{khi}}\:\:x < 3}
\end{array}} \right..
$$

$$
= \left\{ {\begin{array}{l}
{{x^2} + 4x – 8\:\:{\rm{khi}}\:\:x \ge 3.}\\
{{x^2} + 2x – 2\:\:{\rm{khi}}\:\:x < 3}
\end{array}} \right..
$$

Khi đó 
$$
f'(x) = \left\{ {\begin{array}{l}
{2x + 4\:\:{\rm{khi}}\:\:x \ge 3}\\
{2x + 2\:\:{\rm{khi}}\:\:x < 3}
\end{array}} \right..
$$

Do đó $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 2\:\:{\rm{(loại)}}}\\
{x = – 1}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-10.png" alt="">

Từ bảng biến thiên của hàm số, ta thấy phương trình bài ra có hai nghiệm phân biệt trên khoảng $( – 6;5)$ khi $m \in ( – 3;22).$

Do đó $m \in \{ – 2; – 1;0; \ldots ;21\} .$

Có tất cả $24$ giá trị nguyên cần tìm.

> **Đáp án: B**

## Bài 5. Tính tổng các giá trị nguyên của tham số $m$ để phương trình $\left| {{x^2} + 2x} \right| + 4x – 2m + 1 = 0$ có hai nghiệm phân biệt trên đoạn $[-4;4].$

A. $-7.$

B. $-15.$

C. $23.$

D. $33.$

Ta có $\left| {{x^2} + 2x} \right| + 4x – 2m + 1 = 0$ $\Leftrightarrow \left| {{x^2} + 2x} \right| + 4x + 1 = 2m.$

Xét hàm số $f(x) = \left| {{x^2} + 2x} \right| + 4x + 1$ 
$$
= \left\{ {\begin{array}{l}
{{x^2} + 2x + 4x + 1\:\:{\rm{khi}}\:\:x \le – 2,x \ge 0}\\
{ – {x^2} – 2x + 4x + 1\:\:{\rm{khi}}\:\: – 2 < x < 0}
\end{array}} \right..
$$

$$
= \left\{ {\begin{array}{l}
{{x^2} + 6x + 1\:\:{\rm{khi}}\:\:x \le – 2,x \ge 0}\\
{ – {x^2} + 2x + 1\:\:{\rm{khi}}\:\: – 2 < x < 0}
\end{array}} \right..
$$

Suy ra: 
$$
f'(x) = \left\{ {\begin{array}{l}
{2x + 6\:\:{\rm{khi}}\:\:x \le – 2,x \ge 0}\\
{ – 2x + 2\:\:{\rm{khi}}\:\: – 2 < x < 0}
\end{array}} \right..
$$

Do đó $f'(x) = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{x = – 3}\\
{x = 1\:\:{\rm{(loại)}}}
\end{array}} \right..
$$

Bảng biến thiên của hàm số:

<img link="data_for_rag/toan12/images/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi-11.png" alt="">

Từ bảng biến thiên của hàm số, ta thấy phương trình bài ra có hai nghiệm phân biệt trên đoạn $[-4;4]$ khi $– 8 < m \le – 7.$  Vì $m \in Z$ $\Rightarrow m = – 7.$

> **Đáp án: A**

<!-- chunk:8 level:1 source:https://toanmath.com/2019/11/tim-dieu-kien-de-phuong-trinh-fx-gm-co-n-nghiem-lien-quan-den-gia-tri-tuyet-doi.html -->
## IV. BÀI TẬP TỰ LUYỆN
## Bài 1. Tìm tất cả các giá trị của tham số $m$ để phương trình $\left| {{x^3} – 3x + 1} \right| = m – 5$ có bốn nghiệm phân biệt.

A. $(6;8).$

B. $[1;3].$

C. $(8;12).$

D. $[5;6].$

## Bài 2. Tìm tất cả các giá trị của tham số $m$ để phương trình $\left| {2{x^3} – 6x + 3} \right| = 2m + 1$ có sáu nghiệm phân biệt.

A. $\left( { – 1; – \frac{1}{2}} \right).$

B. $\left( { – \frac{1}{2};0} \right).$

C. $(0;1).$

D. $(1;3).$

## Bài 3. Tìm tất cả các giá trị của tham số $m$ để phương trình $\left| {{x^4} – 2{x^2} – 5} \right| = m – 2$ có hai nghiệm phân biệt.

A. $(8; + \infty ).$

B. $(2;7).$

C. $(7;8).$

D. $\{ 2\} \cup (8; + \infty ).$

## Bài 4. Tìm tất cả các giá trị của tham số $m$ để phương trình $\left| {x + 2} \right|\left( {{x^2} – 2x + 1} \right) = m – 1$ có bốn nghiệm phân biệt.

A. $(0;1).$

B. $(5;7).$

C. $(0;4).$

D. $(4;5).$

## Bài 5. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $\left| {x – 5} \right|\left( {{x^2} – 4x + 4} \right) = m – 6$ có bốn nghiệm phân biệt.

A. $4.$

B. $5.$

C. $3.$

D. $2.$

## Bài 6. Tìm tất cả các giá trị của tham số $m$ để phương trình $\left| {x + 3} \right| + {x^2} – 3x – 4 – m = 0$ có nghiệm.

A. $m \le – 1.$

B. $m \ge – 2.$

C. $m > – 3.$

D. $m < 5.$

## Bài 7. Có bao nhiêu giá trị nguyên của tham số $m$ để phương trình $|x + 1| + 2{x^2} – 7x + 3 – m = 0$ có hai nghiệm phân biệt trên đoạn $[-1;3].$

A. $4.$

B. $3.$

C. $5.$

D. $6.$

## Bài 8. Có bao nhiêu giá trị nguyên dương của tham số $m$ để phương trình $|x – 3| – {x^2} + 3x + 1 – m = 0$ có hai nghiệm phân biệt.

A. $3.$

B. $4.$

C. $5.$

D. $6.$

## Bài 9. Tính tổng các giá trị nguyên của tham số $m$ để phương trình $\left| {{x^2} – 2x + 3} \right| + 4x – 3 – m = 0$ có hai nghiệm phân biệt trên đoạn $[-3;1].$

A. $P = -1.$

B. $P = 3.$

C. $P = 6.$

D. $P = 3.$

## Bài 10. Tính tổng các giá trị nguyên âm của tham số $m$ để phương trình $\left| {{x^2} + 3x + 2} \right| + x – 2 – m = 0$ có hai nghiệm phân biệt.

A. $P = -6.$

B. $P = -3.$

C. $P = -1.$

D. $P = -10.$

## V. BẢNG ĐÁP ÁN BÀI TẬP TỰ LUYỆN

1. A.

2. B.

3. D.

4. D.

5. C.

6. B.

7. A.

8. B.

9. C.

10. A.