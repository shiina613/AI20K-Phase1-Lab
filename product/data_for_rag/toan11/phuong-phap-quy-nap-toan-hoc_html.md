# Phương pháp quy nạp toán học

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
Bài viết hướng dẫn dùng phương pháp quy nạp toán học để chứng minh các dạng toán về đẳng thức, bất đẳng thức, tính chia hết trong số học, một số bài toán hình học …

Phương pháp quy nạp toán học
Cho bài toán: Chứng minh mệnh đề $P(n)$ đúng với mọi số tự nhiên $n\ge {{n}_{0}},$ ${{n}_{0}}\in N$.

Ta có thể sử dụng phương pháp quy nạp toán học như sau:

• Bước 1: Kiểm tra $P({{n}_{0}})$ có đúng hay không, nếu bước này đúng thì ta chuyển qua bước 2.

• Bước 2: Với $k \in N, k\ge {{n}_{0}}$, giả sử $P(k)$ đúng ta cần chứng minh $P(k+1)$ cũng đúng.

Kết luận: $P(n)$ đúng với $\forall n\ge {{n}_{0}}$.

Các dạng toán và ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 1. Chứng mình với mọi số tự nhiên $n \ge 1$ ta luôn có: $1 + 2 + 3 + … + n = \frac{{n(n + 1)}}{2}.$

Đặt $P(n) = 1 + 2 + 3 + … + n$ và $Q(n) = \frac{{n(n + 1)}}{2}$.

Ta cần chứng minh $P(n) = Q(n)$, $\forall n \in N, n \ge 1$.

+ Bước 1: Với $n = 1$ ta có $P(1) = 1$, $Q(1) = \frac{{1(1 + 1)}}{2} = 1$ $\Rightarrow P(1) = Q(1)$ $⇒ P(n) = Q(n)$ đúng với $n = 1.$

+ Bước 2: Giả sử $P(k) = Q(k)$ với $k \in N, k \ge 1$ tức là: $1 + 2 + 3 + … + k = \frac{{k(k + 1)}}{2}$.

Ta cần chứng minh $P(k + 1) = Q(k + 1)$, tức là: $1 + 2 + 3 + … + k + (k + 1)$ $= \frac{{(k + 1)(k + 2)}}{2}$ $(*).$

Thật vậy: $VT(*)$ $= (1 + 2 + 3 + … + k) + (k + 1)$ $= \frac{{k(k + 1)}}{2} + (k + 1)$ $= (k + 1)(\frac{k}{2} + 1)$ $= \frac{{(k + 1)(k + 2)}}{2}$ $= VP(*)$

Vậy đẳng thức cho đúng với mọi $n \ge 1.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 2. Chứng minh với mọi số tự nhiên $n \ge 1$ ta luôn có: $1 + 3 + 5 + … + 2n – 1 = {n^2}.$

+ Với $n = 1$ ta có $VT = 1$, $VP = {1^2} = 1$, suy ra $VT = VP$ $\Rightarrow$ đẳng thức cho đúng với $n = 1.$

+ Giả sử đẳng thức đã cho đúng với $n = k$ với $k \in N, k \ge 1$, tức là: $1 + 3 + 5 + … + 2k – 1 = {k^2}.$

Ta cần chứng minh đẳng thức đã cho đúng với $n = k + 1$, tức là: $1 + 3 + 5 + … + (2k – 1) + (2k + 1)$ $= {\left( {k + 1} \right)^2}$ $(*).$

Thật vậy: $VT(*)$ $= (1 + 3 + 5 + … + 2k – 1) + (2k + 1)$ $= {k^2} + (2k + 1)$ $= {(k + 1)^2}$ $= VP(*)$

Vậy đẳng thức đã cho đúng với mọi $n \ge 1.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 3. Chứng minh rằng $\forall n \ge 1$, ta có bất đẳng thức: $\frac{{1.3.5…\left( {2n – 1} \right)}}{{2.4.6.2n}} < \frac{1}{{\sqrt {2n + 1} }}.$

+ Với $n = 1$ ta có bất đẳng thức đã cho trở thành $\frac{1}{2} < \frac{1}{{\sqrt 3 }} \Leftrightarrow 2 > \sqrt 3$ (đúng) $\Rightarrow$ bất đẳng thức đã cho đúng với $n = 1.$

+ Giả sử bất đẳng thức đã cho đúng với $n = k \ge 1$, tức là: $\frac{{1.3.5…\left( {2k – 1} \right)}}{{2.4.6…2k}} < \frac{1}{{\sqrt {2k + 1} }}.$

Ta phải chứng minh bất đẳng thức đã cho đúng với $n = k + 1$, tức là: $\frac{{1.3.5…\left( {2k – 1} \right)\left( {2k + 1} \right)}}{{2.4.6….2k\left( {2k + 2} \right)}}$ $< \frac{1}{{\sqrt {2k + 3} }}$.

Thật vậy, ta có: $\frac{{1.3.5…\left( {2k – 1} \right)\left( {2k + 1} \right)}}{{2.4.6….2k\left( {2k + 2} \right)}}$ $= \frac{{1.3.5…(2k – 1)}}{{2.4.6…2k}}.\frac{{2k + 1}}{{2k + 2}}$ $< \frac{1}{{\sqrt {2k + 1} }}\frac{{2k + 1}}{{2k + 2}}$ $= \frac{{\sqrt {2k + 1} }}{{2k + 2}}.$

Ta chứng minh: $\frac{{\sqrt {2k + 1} }}{{2k + 2}} < \frac{1}{{\sqrt {2k + 3} }}$ $\Leftrightarrow (2k + 1)(2k + 3) < {(2k + 2)^2}$ $\Leftrightarrow 3 > 1$ (luôn đúng).

Vậy bất đẳng thức đã cho đúng với mọi số tự nhiên $n \ge 1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 4. Chứng minh rằng với $\forall n \ge 1, \forall x > 0$ ta có bất đẳng thức: $\frac{{{x^n}({x^{n + 1}} + 1)}}{{{x^n} + 1}} \le {\left( {\frac{{x + 1}}{2}} \right)^{2n + 1}}$. Đẳng thức xảy ra khi nào?

+ Với $n = 1$ ta cần chứng minh: $\frac{{x({x^2} + 1)}}{{x + 1}} \le {\left( {\frac{{x + 1}}{2}} \right)^3}$ $\Leftrightarrow 8x({x^2} + 1) \le {(x + 1)^4}.$

Tức là: ${x^4} – 4{x^3} + 6{x^2} – 4x + 1 \ge 0$ $\Leftrightarrow {(x – 1)^4} \ge 0$ (đúng).

+ Giả sử $\frac{{{x^k}({x^{k + 1}} + 1)}}{{{x^k} + 1}} \le {\left( {\frac{{x + 1}}{2}} \right)^{2k + 1}}$, ta chứng minh: $\frac{{{x^{k + 1}}({x^{k + 2}} + 1)}}{{{x^{k + 1}} + 1}} \le {\left( {\frac{{x + 1}}{2}} \right)^{2k + 3}}$ $(*).$

Thật vậy, ta có: ${\left( {\frac{{x + 1}}{2}} \right)^{2k + 3}}$ $= {\left( {\frac{{x + 1}}{2}} \right)^2}{\left( {\frac{{x + 1}}{2}} \right)^{2k + 1}}$ $\ge {\left( {\frac{{x + 1}}{2}} \right)^2}\frac{{{x^k}({x^{k + 1}} + 1)}}{{{x^k} + 1}}.$

Nên để chứng minh $(*)$ ta chỉ cần chứng minh ${\left( {\frac{{x + 1}}{2}} \right)^2}\frac{{{x^k}({x^{k + 1}} + 1)}}{{{x^k} + 1}}$ $\ge \frac{{{x^{k + 1}}({x^{k + 2}} + 1)}}{{{x^{k + 1}} + 1}}.$

Hay ${\left( {\frac{{x + 1}}{2}} \right)^2}{({x^{k + 1}} + 1)^2}$ $\ge x({x^{k + 2}} + 1)({x^k} + 1)$ $(**).$

Khai triển $(**)$, biến đổi và rút gọn ta thu được: ${x^{2k + 2}}{(x – 1)^2}$ $– 2{x^{k + 1}}{(x – 1)^2} + {(x – 1)^2} \ge 0$ $\Leftrightarrow {(x – 1)^2}{({x^{k + 1}} – 1)^2} \ge 0$, bất đẳng thức này hiển nhiên đúng.

Đẳng thức xảy ra $\Leftrightarrow x = 1.$

Vậy bài toán được chứng minh.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 5. Cho $n$ là số tự nhiên dương. Chứng minh rằng: ${a_n} = {16^n} – 15n – 1 \vdots 225$.

+ Với $n = 1$ ta có: ${a_1} = 0 \Rightarrow {a_1} \vdots 225.$

+ Giả sử ${a_k} = {16^k} – 15k – 1 \vdots 225$, ta chứng minh: ${a_{k + 1}} = {16^{k + 1}} – 15(k + 1) – 1 \vdots 225.$

Thật vậy: ${a_{k + 1}} = {16.16^k} – 15k – 16$ $= {16^k} – 15k – 1 – 15\left( {{{16}^k} – 1} \right)$ $= {a_k} – 15\left( {{{16}^k} – 1} \right).$

Vì ${16^k} – 1$ $= 15.\left( {{{16}^{k – 1}} + {{16}^{k – 2}} + … + 1} \right) \vdots 15$ và ${a_k} \vdots 225.$

Nên ta suy ra ${a_{k + 1}} \vdots 225.$

Vậy bài toán được chứng minh.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 6. Chứng minh rằng với mọi số tự nhiên $n \ge 1$ thì $A(n) = {7^n} + 3n – 1$ luôn chia hết cho $9.$

+ Với $n = 1$ $\Rightarrow A(1) = {7^1} + 3.1 – 1 = 9$ $\Rightarrow A(1) \vdots 9.$

+ Giả sử $A(k) \vdots 9$, $\forall k \ge 1$, ta chứng minh $A(k + 1) \vdots 9.$

Thật vậy: $A(k + 1) = {7^{k + 1}} + 3(k + 1) – 1$ $= {7.7^k} + 21k – 7 – 18k + 9$

$\Rightarrow A(k + 1) = 7A(k) – 9(2k – 1)$.

Vì 
$$
\left\{ \begin{array}{l}
A(k) \vdots 9\\
9(2k – 1) \vdots 9
\end{array} \right. \Rightarrow A(k + 1) \vdots 9.
$$

Vậy $A(n)$ chia hết cho $9$ với mọi số tự nhiên $n \ge 1.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 7. Cho $n$ là số tự nhiên dương. Chứng minh rằng: ${B_n} = \left( {n + 1} \right)\left( {n + 2} \right)\left( {n + 3} \right) \ldots .\left( {3n} \right)$ $\vdots {3^n}.$

+ Với $n = 1$, ta có: ${B_1} = 2.3 \vdots 3.$

+ Giả sử mệnh đề đúng với $n = k$, tức là: ${B_k}$ $= \left( {k + 1} \right)\left( {k + 2} \right)\left( {k + 3} \right) \ldots \left( {3k} \right) \vdots {3^k}.$

Ta chứng minh: ${B_{k + 1}} = \left( {k + 2} \right)\left( {k + 3} \right)\left( {k + 4} \right)$ $\ldots \left[ {3\left( {k{\rm{ }} + {\rm{ }}1} \right)} \right] \vdots {3^{k + 1}}.$

Ta có: ${B_{k + 1}} = 3\left( {k + 1} \right)\left( {k + 2} \right)\left( {k + 3} \right)$ $\ldots \left( {3k} \right)\left( {3k + 1} \right)\left( {3k + 2} \right)$ $= 3{B_k}\left( {3k + 1} \right)\left( {3k + 2} \right).$

Mà ${B_k} \vdots {3^k}$ nên suy ra ${B_{k + 1}} \vdots {3^{k + 1}}.$

Vậy bài toán được chứng minh.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 8. Trong mặt mặt phẳng cho $n$ điểm rời nhau $(n > 2)$ tất cả không nằm trên một đường thẳng. Chứng minh rằng tất cả các đường thẳng nối hai điểm trong các điểm đã cho tạo ra số đường thẳng khác nhau không nhỏ hơn $n.$

Giả sử mệnh đề đúng với $n=k\ge 3$ điểm.

Ta chứng minh nó cũng đúng cho $n=k+1$ điểm.

Ta có thể chứng minh rằng tồn tại ít nhất một đường thẳng chỉ chứa có hai điểm. Ta kí hiệu đường thẳng đi qua hai điểm ${{A}_{n}}$ và ${{A}_{n+1}}$ là ${{A}_{n}}{{A}_{n+1}}$. Nếu những điểm ${{A}_{1}},{{A}_{2}},…,{{A}_{n}}$ nằm trên một đường thẳng thì số lượng các đường thẳng sẽ đúng là $n+1$: Gồm $n$ đường thẳng nối ${{A}_{n+1}}$ với các điểm ${{A}_{1}},{{A}_{2}},…,{{A}_{n}}$ và đường thẳng chúng nối chung. Nếu ${{A}_{1}},{{A}_{2}},…,{{A}_{n}}$ không nằm trên một đường thẳng thì theo giả thiết quy nạp có $n$ đường thẳng khác nhau. Bây giờ ta thêm các đường thẳng nối ${{A}_{n+1}}$ với các điểm ${{A}_{1}},{{A}_{2}},…,{{A}_{n}}$. Vì đường thẳng ${{A}_{n}}{{A}_{n+1}}$ không chứa một điểm nào trong ${{A}_{1}},{{A}_{2}},…,{{A}_{n-1}}$, nên đường thẳng này khác hoàn toàn với $n$ đường thẳng tạo ra bởi ${{A}_{1}},{{A}_{2}},…,{{A}_{n}}$. Như vậy số đường thẳng tạo ra cũng không nhỏ hơn $n+1$.

<!-- chunk:9 level:3 source:https://toanmath.com/2018/06/phuong-phap-quy-nap-toan-hoc.html -->
## Ví dụ 9. Chứng minh rằng tổng các trong một $n$-giác lồi $(n\ge 3)$ bằng $(n-2){{180}^{0}}$.

+ Với $n=3$ ta có tổng ba góc trong tam giác bằng ${{180}^{0}}.$

+ Giả sử công thức đúng cho tất cả $k$-giác, với $k<n$, ta phải chứng minh mệnh đề cũng đúng cho $n$-giác. Ta có thể chia $n$-giác bằng một đường chéo thành ra hai đa giác. Nếu số cạnh của một đa giác là $k+1$, thì số cạnh của đa giác kia là $n – k + 1$, hơn nữa cả hai số này đều nhỏ hơn $n$. Theo giả thiết quy nạp tổng các góc của hai đa giác này lần lượt là $\left( k-1 \right){{180}^{0}}$ và $\left( n-k-1 \right){{180}^{0}}.$

Tổng các góc của $n$-giác bằng tổng các góc của hai đa giác trên, nghĩa là $\left( {k–1 + n – k–1} \right){180^0}$ $= \left( {n – 2} \right){180^0}.$

Suy ra mệnh đề đúng với mọi $n\ge 3.$