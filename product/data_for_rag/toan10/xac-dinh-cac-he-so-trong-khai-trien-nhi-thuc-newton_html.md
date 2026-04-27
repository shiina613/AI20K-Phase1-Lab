# Xác định các hệ số trong khai triển nhị thức Newton

<!-- chunk:0 level:0 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
Bài viết hướng dẫn phương pháp giải bài toán xác định các hệ số trong khai triển nhị thức Newton, các dạng toán được đề cập trong bài viết gồm: xác định hệ số trong khai triển nhị thức Newton 2 số hạng, 3 số hạng, xác định hệ số lớn nhất trong khai triển nhị thức Niutơn … trong mỗi dạng toán, đều có hướng dẫn cụ thể phương pháp, các ví dụ minh họa với lời giải chi tiết, phần cuối bài viết là tuyển tập các bài toán hay và khó để bạn đọc nắm chắc kỹ thuật giải dạng toán này.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## A. Phương pháp xác định các hệ số trong khai triển nhị thức Newton.

1. Tìm hệ số của số hạng chứa ${x^m}$ trong khai triển ${\left( {a{x^p} + b{x^q}} \right)^n}.$

Phương pháp:

Cho khai triển: ${\left( {a{x^p} + b{x^q}} \right)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} {\left( {a{x^p}} \right)^{n – k}}{\left( {b{x^q}} \right)^k}$ $= \sum\limits_{k = 0}^n {C_n^k} {a^{n – k}}{b^k}{x^{np – pk + qk}}.$

Số hạng chứa ${x^m}$ ứng với giá trị $k$ thỏa $np – pk + qk = m.$

Từ đó tìm $k = \frac{{m – np}}{{p – q}}.$

Vậy hệ số của số hạng chứa ${x^m}$ là: $C_n^k{a^{n – k}}{b^k}$ với giá trị $k$ đã tìm được ở trên.

Nếu $k$ không nguyên hoặc $k > n$ thì trong khai triển không chứa $x^m$, hệ số phải tìm bằng $0.$

Lưu ý: Tìm số hạng không chứa $x$ thì ta đi tìm giá trị $k$ thỏa $np – pk + qk = 0.$

<!-- chunk:2 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 1: Trong khai triển $\left( {2\sqrt[3]{x} – \frac{3}{{\sqrt x }}} \right)$, $(x > 0)$ số hạng không chứa $x$ sau khi khai triển là?

A. $4354560.$

B. $13440.$

C. $60466176.$

D. $20736.$

Chọn A.

${\left( {2\sqrt[3]{x} – \frac{3}{{\sqrt x }}} \right)^{10}}$ $= {\left( {2{x^{\frac{1}{3}}} – 3{x^{ – \frac{1}{2}}}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {2{x^{\frac{1}{3}}}} \right)^{10 – k}}{\left( { – 3{x^{ – \frac{1}{2}}}} \right)^k}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {2^{10 – k}}{( – 3)^k}{x^{\frac{{10 – k}}{3}}}{x^{\frac{k}{2}}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {2^{10 – k}}{( – 3)^k}{x^{\frac{{20 – 5k}}{6}}}.$

Theo yêu cầu đề bài ta có $20 – 5k = 0$ $\Leftrightarrow k = 4.$

Vậy số hạng không chứa $x$ trong khai triển là $C_{10}^4{.2^6}{.3^4} = 210.256.81 = 435460.$

<!-- chunk:3 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 2: Cho $n$ là số dương thỏa mãn $5C_n^{n – 1} = C_n^3.$ Số hạng chứa ${x^5}$ trong khai triển nhị thức Newton $P = {\left( {\frac{{n{x^2}}}{{14}} – \frac{1}{x}} \right)^n}$ với $x \ne 0$ là?

A. $– \frac{{35}}{{16}}.$

B. $– \frac{{16}}{{35}}.$

C. $– \frac{{35}}{{16}}{x^5}.$

D. $– \frac{{16}}{{35}}{x^5}.$

Chọn C.

Điều kiện $n \in N$, $n \ge 3.$

Ta có: $5C_n^{n – 1} = C_n^3$ $\Leftrightarrow \frac{{5.n!}}{{1!.(n – 1)!}} = \frac{{n!}}{{3!.(n – 3)!}}$ $\Leftrightarrow \frac{5}{{(n – 3)!(n – 2)(n – 1)}} = \frac{1}{{6(n – 3)!}}$ $\Leftrightarrow {n^2} – 3n – 28 = 0$ 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{n = 7\:{\rm{(thỏa\:mãn)}}}\\
{n = – 4\:{\rm{(loại)}}}
\end{array}} \right.
$$

Với $n = 7$ ta có $P = {\left( {\frac{{{x^2}}}{2} – \frac{1}{x}} \right)^7}.$

$P = {\left( {\frac{{{x^2}}}{2} – \frac{1}{x}} \right)^7}$ $= \sum\limits_{k = 0}^7 {C_7^k} {\left( {\frac{{{x^2}}}{2}} \right)^{7 – k}}{\left( { – \frac{1}{x}} \right)^k}$ $= \sum\limits_{k = 0}^7 {C_7^k} \frac{1}{{{2^k}}} \cdot {( – 1)^{7 – k}}{x^{14 – 3k}}.$

Số hạng chứa ${x^5}$ tương ứng với $14 – 3k = 5$ $\Leftrightarrow k = 3.$

Vậy số hạng chứa ${x^5}$ trong khai triển là $C_7^4 \cdot \frac{1}{{{2^4}}} \cdot {( – 1)^3} = – \frac{{35}}{{16}}.$

2. Xác định hệ số lớn nhất trong khai triển nhị thức Niutơn.
Phương pháp: Giả sử sau khi khai triển ta được đa thức $P(x) = {a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_n}{x^n}.$

Xét các khả năng sau:

a. Nếu ${a_k} > 0$ $\forall k$ (trường hợp ${a_k} < 0$ $\forall k$ tương tự).

Ta xét bất phương trình ${a_k} \le {a_{k + 1}}$, thông thường giải ra được nghiệm $k \le {k_0} \in N$. Do $k$ nguyên nên $k = 0,1, \ldots ,{k_0}$. Từ đó suy ra bất phương trình ${a_k} > {a_{k + 1}}$ có nghiệm $k > {k_0}.$

• Nếu ${a_k} = {a_{k + 1}}$ $\Leftrightarrow k = {k_0}$ thì ta có: ${a_0} < {a_1} < \ldots < {a_{{k_0} – 1}} < {a_{{k_0}}}$ $= {a_{{k_0} + 1}} > {a_{{k_0} + 2}} > \ldots > {a_n}.$

Khi đó ta tìm được hai hệ số lớn nhất là ${a_{{k_0}}} = {a_{{k_0} + 1}}.$

• Nếu phương trình ${a_k} = {a_{k + 1}}$ vô nghiệm thì ta có: ${a_0} < {a_1} < \ldots < {a_{{k_0} – 1}} < {a_{{k_0}}}$ $> {a_{{k_0} + 1}} > {a_{{k_0} + 2}} > \ldots > {a_n}.$

Khi đó ta có ${a_{{k_0}}}$ là hệ số lớn nhất trong khai triển của nhị thức.

b. Nếu ${a_{2k}} > 0$ $\forall k$ và ${a_{2k + 1}} < 0$ $\forall k$ (trường hợp ${a_{2k}} < 0$ $\forall k$ và ${a_{2k + 1}} > 0$ $\forall k$ tương tự) thì khi đó bài toán trở thành tìm số lớn nhất trong các số ${a_{2k}}$. Ta cũng xét bất phương trình ${a_{2k}} \le {a_{2k + 2}}$ rồi làm tương tự như phần 1.

<!-- chunk:4 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 1: Tìm hệ số có giá trị lớn nhất trong khai triển đa thức: $P(x) = {(2x + 1)^{13}}$ $= {a_0}{x^{13}} + {a_1}{x^{12}} + \ldots + {a_{13}}.$

A. $8.$

B. $4536.$

C. $4528.$

D. $4520.$

Chọn A.

Ta có hệ số tổng quát sau khi khai triển nhị thức ${(2x + 1)^{13}}$ là ${a_n} = C_{13}^n{.2^{13 – n}}.$

Suy ra: ${a_{n – 1}} = C_{13}^{n – 1}{.2^{14 – n}}$, $(n = 1,2,3, \ldots ,13).$

Xét bất phương trình với ẩn số $n$ ta có ${a_{n – 1}} \le {a_n}$ $\Leftrightarrow C_{13}^{n – 1}{.2^{14 – n}} \le C_n^{13}{.2^{13 – n}}$ $\Leftrightarrow \frac{{2.13!}}{{(n – 1)!(14 – n)!}} \le \frac{{13!}}{{n!(13 – n)!}}$ $\Leftrightarrow \frac{2}{{14 – n}} \le \frac{1}{n}$ $\Leftrightarrow n \le \frac{{14}}{3} \notin N.$

Do đó bất đẳng thức ${a_{n – 1}} \le {a_n}$ đúng với $n \in \{ 1,2,3,4\}$ và dấu đẳng thức không xảy ra.

Nên bất đẳng thức ${a_{n – 1}} > {a_n}$ đúng với $n \in \{ 5,6,7,8,9,10,11,12,13\} .$

Ta được ${a_0} < {a_1} < {a_2} < {a_3} < {a_4}$ và ${a_4} > {a_5} > {a_6} > \ldots > {a_{13}}.$

Từ đây ta có hệ số có giá trị lớn nhất trong khai triển nhị thức là: ${a_4} = C_{13}^4{.2^9} = 366080.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 2: Trong khai triển biểu thức $F = {\left( {\sqrt 3 + \sqrt[3]{2}} \right)^9}$ số hạng nguyên có giá trị lớn nhất là?

A. $8.$

B. $4536.$

C. $4528.$

D. $4520.$

Chọn B.

Ta có số hạng tổng quát ${T_{k + 1}} = C_9^k{(\sqrt 3 )^{9 – k}}{(\sqrt[3]{2})^k}.$

Ta thấy hai bậc của căn thức là $2$ và $3$ là hai số nguyên tố, do đó để ${T_{k + 1}}$ là một số nguyên thì:

$$
\left\{ {\begin{array}{l}
{k \in N}\\
{0 \le k \le 9}\\
{(9 – k) \vdots 2}\\
{k \vdots 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left[ {\begin{array}{l}
{k = 3 \Rightarrow {T_4} = C_9^3{{(\sqrt 3 )}^6}{{(\sqrt[3]{2})}^3} = 4536}\\
{k = 9 \Rightarrow {T_{10}} = C_9^9{{(\sqrt 3 )}^0}{{(\sqrt[3]{2})}^9} = 8}
\end{array}} \right.
$$

Vậy trong khai triển có hai số hạng nguyên là ${T_4} = 4536$ và ${T_{10}} = 8.$

3. Xác định hệ số của số hạng trong khai triển $P(x) = {\left( {a{x^t} + b{x^p} + c{x^q}} \right)^n}.$
Phương pháp: Xác định hệ số của số hạng chứa ${x^m}$ trong khai triển $P(x) = {\left( {a{x^t} + b{x^p} + c{x^q}} \right)^n}.$

Ta làm như sau: $P(x) = {\left( {a{x^t} + b{x^p} + c{x^q}} \right)^n}$ $= \sum\limits_{k = 0}^n {C_n^k} {\left( {a{x^t}} \right)^{n – k}}{\left( {b{x^p} + c{x^q}} \right)^k}$ $= \sum\limits_{k = 0}^n {\sum\limits_{i = 0}^k {C_n^k} } {a^{n – k}}{x^{t(n – k)}}C_k^i{b^{k – i}}{c^i}{x^{p(k – i) + qi}}$ $= \sum\limits_{k = 0}^n {\sum\limits_{i = 0}^k {C_n^k} } C_k^i{a^{n – k}}{b^{k – i}}{c^i}{x^{t(n – k) + p(k – i) + qi}}$ (do ${\left( {b{x^p} + c{x^q}} \right)^k}$ $= \sum\limits_{i = 0}^k {C_k^i} {\left( {b{x^p}} \right)^{k – i}}{\left( {c{x^q}} \right)^i}$ $= \sum\limits_{i = 0}^k {C_k^i} {b^{k – i}}{c^i}{x^{p(k – i) + qi}}$).

Suy ra số hạng tổng quát của khai triển là: $C_n^kC_i^k{a^{n – k}}{b^{k – i}}{c^i}{x^{t(n – k) + p(k – i) + qi}}.$

Từ số hạng tổng quát của hai khai triển trên ta tính được hệ số của ${x^m}.$

<!-- chunk:6 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 1: Hệ số của số hạng chứa ${x^4}$ trong khai triển $P(x) = {\left( {3{x^2} + x + 1} \right)^{10}}$ là:

A. $1695.$

B. $1485.$

C. $405.$

D. $360.$

Chọn A.

Ta có số hạng tổng quát của khai triển là: $C_{10}^kC_k^i{3^{10 – k}}{1^{k – i}}{1^i}{x^{2(10 – k) + 1(k – i) + 0i}}$ $= C_{10}^kC_k^i{3^{10 – k}}{x^{20 – k – i}}.$

Số hạng chứa ${x^4}$ tương ứng với $20 – k – i = 4$ $\Rightarrow k = 16 – i.$

Với $0 \le k \le 10$, $0 \le i \le k$ nên ta có $(i;k) \in \{ (6;10);(7;9);(8;8)\} .$

Vậy hệ số của ${x^4}$ trong khai triển $P(x) = {\left( {3{x^2} + x + 1} \right)^{10}}$ là: $C_{10}^{10}C_{10}^6{3^0} + C_{10}^9C_9^73 + C_{10}^8C_8^8{3^2} = 1695.$

Nhận xét: Chú ý khi ra nhiều trường hợp của $(i, k)$ thì ta cộng hệ số các trường hợp với nhau để có kết quả.

<!-- chunk:7 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 2: Tìm số hạng chứa ${x^{13}}$ trong khai triển thành các đa thức của ${\left( {x + {x^2} + {x^3}} \right)^{10}}$ là:

A. $135.$

B. $45.$

C. $135x^{13}.$

D. $45x^{13}.$

Chọn C.

Ta có số hạng tổng quát của khai triển là: $C_{10}^kC_k^i{1^{10 – k}}{1^{k – i}}{1^i}{x^{10 – k + 2(k – i) + 3i}}$ $= C_{10}^kC_k^i{x^{10 + k + i}}.$

Số hạng chứa ${x^{13}}$ tương ứng với $10 + k + i = 13$ $\Rightarrow k = 3 – i.$

Với $0 \le k \le 10$, $0 \le i \le k$ nên ta có $(i;k) \in \{ (0;3);(1;2)\} .$

Vậy hệ số của ${x^{13}}$ trong khai triển $P(x) = {\left( {x + {x^2} + {x^3}} \right)^{10}}$ là: $C_{10}^3C_3^0 + C_{10}^2C_2^1 = 210.$

<!-- chunk:8 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 1. Trong khai triển ${\left( {8{a^2} – \frac{1}{2}b} \right)^6}$, hệ số của số hạng chứa ${a^9}{b^3}$ là:

A. $– 80{a^9}{b^3}.$

B. $– 64{a^9}{b^3}.$

C. $– 1280{a^9}{b^3}.$

D. $60{a^6}{b^4}.$

Chọn C.

Số hạng tổng quát trong khai triển trên là ${T_{k + 1}} = {( – 1)^k}C_6^k{8^{6 – k}}{a^{12 – 2k}}{2^{ – k}}{b^k}.$

Yêu cầu bài toán xảy ra khi $k = 3.$

Khi đó hệ số của số hạng chứa ${a^9}{b^3}$ là: $– 1280{a^9}{b^3}.$

<!-- chunk:9 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 2: Hệ số của ${x^3}{y^3}$ trong khai triển ${(1 + x)^6}{(1 + y)^6}$ là:

A. $20.$

B. $800.$

C. $36.$

D. $400.$

Chọn D.

Số hạng tổng quát trong khai triển trên là ${T_{k + 1}} = C_6^k{x^k}.C_6^m{y^m}.$

Yêu cầu bài toán xảy ra khi $k = m = 3.$

Khi đó hệ số của số hạng chứa ${x^3}{y^3}$ là $C_6^3C_6^3 = 400.$

<!-- chunk:10 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 3: Xác định hệ số của ${x^8}$ trong các khai triển sau: $f(x) = 8{(1 + 8x)^8}$ $– 9{(1 + 9x)^9} + 10{(1 + 10x)^{10}}.$

A. $8.C_8^0{.8^8} – C_9^1{.9^8} + 10.C_{10}^8{.10^8}.$

B. $C_8^0{.8^8} – C_{9.}^1{.9^8} + C_{10}^8{.10^8}.$

C. $C_8^0{.8^8} – 9.C_9^1{.9^8} + 10.C_{10}^8{.10^8}.$

D. $8.C_8^0{.8^8} – 9.C_9^1{9^8} + 10.C_{10}^8{.10^8}.$

Chọn D.

Ta có:

${(1 + 8x)^8} = \sum\limits_{k = 0}^8 {C_8^k} {8^{8 – k}}{x^{8 – k}}.$

${(1 + 9x)^9} = \sum\limits_{k = 0}^9 {C_9^k} {9^{9 – k}}{x^{9 – k}}.$

${(1 + 10x)^{10}} = \sum\limits_{k = 0}^{10} {C_{10}^k} {10^{10 – k}}{x^{10 – k}}.$

Nên hệ số chứa ${x^8}$ là: $8.C_8^0{.8^8} – 9.C_9^1{.9^8} + 10.C_{10}^8{.10^8}.$

<!-- chunk:11 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 4: Tìm hệ số của ${x^7}$ trong khai triển thành đa thức của ${(2 – 3x)^{2n}}$, biết $n$ là số nguyên dương thỏa mãn: $C_{2n + 1}^1 + C_{2n + 1}^3 + C_{2n + 1}^5$ $+ \ldots + C_{2n + 1}^{2n + 1} = 1024.$

A. $2099529.$

B. $-2099520.$

C. $-2099529.$

D. $2099520.$

Chọn B.

Ta có: 
$$
\left\{ {\begin{array}{l}
{\sum\limits_{k = 0}^{2n + 1} {C_{2n + 1}^k} = {2^{2n + 1}}}\\
{\sum\limits_{i = 0}^n {C_{2n + 1}^{2i + 1}} = \sum\limits_{i = 0}^n {C_{2n + 1}^{2i}} }
\end{array}} \right.
$$
 $\Rightarrow \sum\limits_{i = 0}^n {C_{2n + 1}^{2i + 1}} = {2^{2n}} = 1024$ $\Rightarrow n = 5.$

Suy ra ${(2 – 3x)^{2n}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {2^{10 – k}}{( – 3)^k}{x^k}.$

Hệ số của ${x^7}$ là $C_{10}^7{.2^3}.{( – 3)^7} = – 2099520.$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 5: Tìm hệ số của ${x^5}$ trong khai triển đa thức của: $x{(1 – 2x)^5} + {x^2}{(1 + 3x)^{10}}.$

A. $3320.$

B. $2130.$

C. $3210.$

D. $1313.$

Chọn A.

Đặt $f(x) = x{(1 – 2x)^5} + {x^2}{(1 + 3x)^{10}}.$

Ta có: $f(x) = x\sum\limits_{k = 0}^5 {C_5^k} {( – 2)^k}{x^k} + {x^2}\sum\limits_{i = 0}^{10} {C_{10}^i} {(3x)^i}$ $= \sum\limits_{k = 0}^5 {C_5^k} {( – 2)^k}{x^{k + 1}} + \sum\limits_{i = 0}^{10} {C_{10}^i} {3^i}{x^{i + 2}}.$

Vậy hệ số của ${x^5}$ trong khai triển đa thức của $f(x)$ ứng với $k = 4$ và $i = 3$ là: $C_5^4{( – 2)^4} + C_{10}^3{3^3} = 3320.$

<!-- chunk:13 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 6: Với $n$ là số nguyên dương, gọi ${a_{3n – 3}}$ là hệ số của ${x^{3n – 3}}$ trong khai triển thành đa thức của ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}$. Tìm $n$ để ${a_{3n – 3}} = 26n.$

A. $n=3.$

B. $n=4.$

C. $n=5.$

D. $n=2.$

Chọn C.

Cách 1: Ta có:

${\left( {{x^2} + 1} \right)^n}$ $= C_n^0{x^{2n}} + C_n^1{x^{2n – 2}} + C_n^2{x^{2n – 4}} + \ldots + C_n^n.$

${(x + 2)^n}$ $= C_n^0{x^n} + 2C_n^1{x^{n – 1}} + {2^2}C_n^2{x^{n – 2}} + \ldots + {2^n}C_n^n.$

Dễ dàng kiểm tra $n = 1$, $n = 2$ không thoả mãn điều kiện bài toán.

Với $n ≥ 3$ thì dựa vào khai triển ta chỉ có thể phân tích ${x^{3n – 3}}$ $= {x^{2n}}{x^{n – 3}}$ $= {x^{2n – 2}}{x^{n – 1}}.$

Do đó hệ số của ${x^{3n – 3}}$ trong khai triển thành đa thức của ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}$ là: ${a_{3n – 3}} = {2^3}C_n^0C_n^3 + 2C_n^1C_n^1.$

Suy ra ${a_{3n – 3}} = 26n$ $\Leftrightarrow \frac{{2n\left( {2{n^2} – 3n + 4} \right)}}{3} = 26n$ $\Leftrightarrow n = – \frac{7}{2}$ hoặc $n = 5.$

Vậy $n = 5$ là giá trị cần tìm.

Cách 2:

Ta có: ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}$ $= {x^{3n}}{\left( {1 + \frac{1}{{{x^2}}}} \right)^n}{\left( {1 + \frac{2}{x}} \right)^n}$ $= {x^{3n}}\sum\limits_{i = 0}^n {C_n^i} {\left( {\frac{1}{{{x^2}}}} \right)^i}\sum\limits_{k = 0}^n {C_n^k} {\left( {\frac{2}{x}} \right)^k}$ $= {x^{3n}}\left[ {\sum\limits_{i = 0}^n {C_n^i} {x^{ – 2i}}\sum\limits_{k = 0}^n {C_n^k} {2^k}{x^{ – k}}} \right].$

Trong khai triển trên, luỹ thừa của $x$ là $3n – 3$ khi $– 2i – k = – 3$ $\Leftrightarrow 2i + k = 3.$

Ta chỉ có hai trường hợp thoả mãn điều kiện này là $i = 0$, $k = 3$ hoặc $i = 1$, $k = 1$ (vì $i,k$ nguyên).

Hệ số của ${x^{3n – 3}}$ trong khai triển thành đa thức của ${\left( {{x^2} + 1} \right)^n}{(x + 2)^n}$ là: ${a_{3n – 3}} = C_n^0C_n^3{2^3} + C_n^1C_n^12.$

Do đó: ${a_{3n – 3}} = 26n$ $\Leftrightarrow \frac{{2n\left( {2{n^2} – 3n + 4} \right)}}{3} = 26n$ $\Leftrightarrow n = – \frac{7}{2}$ hoặc $n = 5.$

Vậy $n = 5$ là giá trị cần tìm.

<!-- chunk:14 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 7: Tìm hệ số của số hạng chứa ${x^{26}}$ trong khai triển nhị thức Newton của ${\left( {\frac{1}{{{x^4}}} + {x^7}} \right)^n}$, biết $C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n$ $= {2^{20}} – 1.$

A. $210.$

B. $213.$

C. $414.$

D. $213.$

Chọn A.

Do $C_{2n + 1}^k = C_{2n + 1}^{2n + 1 – k}$, $\forall k = 0,1,2, \ldots ,2n + 1.$

$\Rightarrow C_{2n + 1}^0 + C_{2n + 1}^1 + \ldots + C_{2n + 1}^n$ $= C_{2n + 1}^{n + 1} + C_{2n + 1}^{n + 2} + \ldots + C_{2n + 1}^{2n + 1}.$

Mặc khác: $C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^{2n + 1} = {2^{2n + 1}}.$

$\Rightarrow 2\left( {C_{2n + 1}^0 + C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n} \right) = {2^{2n + 1}}.$

$\Rightarrow C_{2n + 1}^1 + C_{2n + 1}^2 + \ldots + C_{2n + 1}^n$ $= {2^{2n}} – C_{2n + 1}^0$ $= {2^{2n}} – 1.$

$\Rightarrow {2^{2n}} – 1 = {2^{20}} – 1$ $\Rightarrow n = 10.$

Khi đó: ${\left( {\frac{1}{{{x^4}}} + {x^7}} \right)^{10}}$ $= {\left( {{x^{ – 4}} + {x^7}} \right)^{10}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {\left( {{x^{ – 4}}} \right)^{10 – k}}{x^{7k}}$ $= \sum\limits_{k = 0}^{10} {C_{10}^k} {x^{11k – 40}}.$

Hệ số chứa ${x^{26}}$ ứng với giá trị $k$ thỏa mãn: $11k – 40 = 26$ $\Rightarrow k = 6.$

Vậy hệ số chứa ${x^{26}}$ là: $C_{10}^6 = 210.$

<!-- chunk:15 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 8: Trong khai triển của ${\left( {\frac{1}{3} + \frac{2}{3}x} \right)^{10}}$ thành đa thức ${a_0} + {a_1}x + {a_2}{x^2} + \ldots + {a_9}{x^9} + {a_{10}}{x^{10}}$, hãy tìm hệ số ${a_k}$ lớn nhất $(0 \le k \le 10).$

A. ${a_{10}} = 3003\frac{{{2^{10}}}}{{{3^{15}}}}.$

B. ${a_5} = 3003\frac{{{2^{10}}}}{{{3^{15}}}}.$

C. ${a_4} = 3003\frac{{{2^{10}}}}{{{3^{15}}}}.$

D. ${a_9} = 3003\frac{{{2^{10}}}}{{{3^{15}}}}.$

Chọn A.

Ta có: ${\left( {\frac{1}{3} + \frac{2}{3}x} \right)^{15}}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} {\left( {\frac{1}{3}} \right)^{15 – k}}{\left( {\frac{2}{3}x} \right)^k}$ $= \sum\limits_{k = 0}^{15} {C_{15}^k} \frac{{{2^k}}}{{{3^{15}}}}{x^k}.$

Hệ số của ${x^k}$ trong khai triển ${a_k} = \frac{1}{{{3^{15}}}}C_{15}^k{2^k}.$

Ta có: ${a_{k – 1}} < {a_k}$ $\Leftrightarrow C_{15}^{k – 1}{2^{k – 1}} < C_{15}^k{2^k}$ $\Leftrightarrow C_{15}^{k – 1} < 2C_{15}^k$ $\Leftrightarrow k < \frac{{32}}{3}$ $\Rightarrow k \le 10.$

Từ đó: ${a_0} < {a_1} < \ldots < {a_{10}}.$

Đảo dấu bất đẳng thức trên, ta được:

${a_{k – 1}} < {a_k}$ $\Leftrightarrow k > \frac{{32}}{3}$ $\Rightarrow {a_{10}} > {a_{11}} > \ldots > {a_{15}}.$

Vậy hệ số lớn nhất phải tìm là: ${a_{10}} = \frac{{{2^{10}}}}{{{3^{15}}}}C_{15}^{10} = 3003\frac{{{2^{10}}}}{{{3^{15}}}}.$

<!-- chunk:16 level:2 source:https://toanmath.com/2018/11/xac-dinh-cac-he-so-trong-khai-trien-nhi-thuc-newton.html -->
## Bài toán 9: Cho khai triển ${(1 + 2x)^n}$ $= {a_0} + {a_1}x + \ldots + {a_n}{x^n}$, trong đó $n \in {N^*}$. Tìm số lớn nhất trong các số ${a_0},{a_1}, \ldots ,{a_n}$ biết các hệ số ${a_0},{a_1}, \ldots ,{a_n}$ thỏa mãn hệ thức: ${a_0} + \frac{{{a_1}}}{2} + \ldots + \frac{{{a_n}}}{{{2^n}}} = 4096.$

A. $324512.$

B. $126720.$

C. $130272.$

D. $130127.$

Chọn B.

Đặt $f(x) = {(1 + 2x)^n}$ $= {a_0} + {a_1}x + \ldots + {a_n}{x^n}.$

$\Rightarrow {a_0} + \frac{{{a_1}}}{2} + \ldots + \frac{{{a_n}}}{{{2^n}}}$ $= f\left( {\frac{1}{2}} \right) = {2^n}$ $\Rightarrow {2^n} = 4096$ $\Leftrightarrow n = 12.$

Với mọi $k \in \{ 0,1,2, \ldots ,11\}$ ta có: ${a_k} = {2^k}C_{12}^k$, ${a_{k + 1}} = {2^{k + 1}}C_{12}^{k + 1}.$

$\Leftrightarrow \frac{{{a_k}}}{{{a_{k + 1}}}} < 1$ $\Leftrightarrow \frac{{{2^k}C_{12}^k}}{{{2^{k + 1}}C_{12}^{k + 1}}} < 1$ $\Leftrightarrow \frac{{k + 1}}{{2(12 – k)}} < 1$ $\Leftrightarrow k < \frac{{23}}{3}.$

Mà $k \in Z$ $\Rightarrow k \le 7.$ Do đó ${a_0} < {a_1} < \ldots < {a_8}.$

Tương tự: $\frac{{{a_k}}}{{{a_{k + 1}}}} > 1$ $\Leftrightarrow k > 7$ $\Rightarrow {a_8} > {a_9} > \ldots > {a_{12}}.$

Số lớn nhất trong các số ${a_0},{a_1}, \ldots ,{a_{12}}$ là ${a_8} = {2^8}C_{12}^8 = 126720.$