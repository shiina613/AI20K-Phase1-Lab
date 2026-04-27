# Bài toán về phép thử và biến cố

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
Bài viết trình bày lý thuyết và hướng dẫn phương pháp giải các dạng toán về phép thử và biến cố, đây là nội dung cơ bản đầu tiên mà học sinh cần nằm vững khi tìm hiểu chủ đề xác suất trong chương trình Đại số và Giải tích 11 chương 2.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## A. LÝ THUYẾT CẦN GHI NHỚ
1. Phép thử ngẫu nhiên và không gian mẫu

Phép thử ngẫu nhiên (gọi tắt là phép thử, thường được kí hiệu là $T$) là một thí nghiệm hay một hành động mà:

+ Kết quả của nó không đoán trước được.

+ Có thể xác định được tập hợp tất cả các kết quả có thể xảy ra của phép thử đó.

Tập hợp tất cả các kết quả có thể xảy ra của phép thử được gọi là không gian mẫu của phép thử và được kí hiệu bởi chữ $Ω.$

2. Biến cố

Biến cố $A$ liên quan đến phép thử $T$ là biến cố mà việc xảy ra hay không xảy ra của $A$ tùy thuộc vào kết quả của $T.$

Mỗi kết quả của phép thử $T$ làm cho $A$ xảy ra, được gọi là một kết quả thuận lợi cho $A.$

Tập hợp các kết quả thuận lợi cho $A$ được kí hiệu là $Ω_A.$ Khi đó ta nói biến cố $A$ được mô tả bởi tập $Ω_A.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 3. Từ một lô sản phẩm gồm chính phẩm và chế phẩm, lấy ngẫu nhiên một sản phẩm. Việc lấy sản phẩm là phép thử, còn việc lấy được chính phẩm hay phế phẩm là biến cố.

Như vậy, ta thấy rằng một biến cố chỉ có thể xảy ra khi một phép thử gắn liền với nó được thực hiện.

3. Các loại biến cố

Biến cố chắc chắn là biến cố nhất định sẽ xảy ra khi thực hiện một phép thử. Biến cố chắc chắn được ký hiệu là $Ω.$

Ví dụ. Thực hiện phép thử tung một con súc sắc. Gọi $Ω$ là biến cố “Xuất hiện một có số chấm nhỏ hơn hoặc bằng 6”, khi đó $Ω$ là biến cố chắc chắn.

Biến cố không thể có là biến cố nhất định không xảy ra khi thực hiện phép thử. Biến cố không thể có được ký hiệu là $Ø.$

Ví dụ. Tung một con súc sắc, gọi $Ø$ là biến cố “Xuất hiện mặt có $7$ chấm”, khi đó $Ø$ là biến cố không thể có.

Biến cố ngẫu nhiên là biến cố có thể xảy ra hoặc không xảy ra khi thực hiện một phép thử.

Ví dụ. Tung một con súc sắc, gọi $A$ là biến cố “xuất hiện mặt $1$ chấm”, khi đó $A$ là biến cố ngẫu nhiên.

<!-- chunk:3 level:2 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Dạng toán 1. Xác định không gian mẫu của phép thử và các phần tử của không gian mẫu.
Phương pháp:

+ Xác định phép thử $T.$

+ Mô tả các kết quả xuất hiện trong phép thử bằng cách sử dụng các phép đếm (quy tắc cộng, quy tắc nhân) hoán vị, chỉnh hợp, tổ hợp, từ đó xác định được không gian mẫu và tính được số phần tử của không gian mẫu.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 1. Một bình đựng $8$ viên bi trắng và $7$ viên bi đỏ, lấy ngẫu nhiên $3$ viên bi. Tìm số phần tử của không gian mẫu $Ω.$

Lấy $3$ viên bi trong tổng số $15$ viên bi.

Số phần tử của không gian mẫu $Ω$ là: $C_{15}^3 = \frac{{15.14.13}}{{3.2.1}} = 455.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 2. Xác định không gian mẫu và số phần tử của không gian mẫu khi gieo ngẫu nhiên:

a) $1$ con súc sắc.

b) $2$ con súc sắc.

c) $3$ con súc sắc.

Mỗi con súc sắc có $6$ mặt đánh số $1$, $2$, $3$, $4$, $5$, $6.$

a) Khi gieo ngẫu nhiên $1$ con súc sắc thì không gian mẫu: $Ω = \{1, 2, 3, 4, 5, 6\}$ có $6$ phần tử.

b) Khi gieo ngẫu nhiên $2$ con súc sắc thì không gian mẫu có $6.6 = 36$ phần tử:

$\Omega = \left\{ {(1;1),(1;2), \ldots ,(1;6),(2;1),(2;2), \ldots ,(6;6)} \right\}.$

c) Khi gieo ngẫu nhiên $3$ con súc sắc thì không gian mẫu có $6.6.6 = 216$ phần tử:

$\Omega = \left\{ {(1;1;1),(1;1;2), \ldots ,(1;1;6),(1;2;1), \ldots ,(6;6;6)} \right\}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 3. Xác định không gian mẫu và số phần tử của không gian mẫu khi gieo ngẫu nhiên $1$ đồng xu cân đối:

a) $1$ lần.

b) $2$ lần liên tiếp.

c) $3$ lần liên tiếp.

Ta kí hiệu $N$ để chỉ mặt ngửa của đồng xu và $S$ để chỉ mặt sấp của đồng xu.

a) Khi gieo đồng xu $1$ lần thì không gian mẫu $Ω = \{N, S\}$ có $2$ phần tử.

b) Khi gieo đồng xu $2$ lần liên tiếp thì không gian mẫu $Ω = \{NN, NS, SN, SS\}$ có $2.2 = 4$ phần tử.

c) Khi gieo đồng xu $3$ lần liên tiếp thì không gian mẫu có: $2.2.2 = 8$ phần tử:

$Ω = \{NNN, NNS, NSN, NSS, SNN, SNS, SSN, SSS\}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 4. Gieo $3$ con súc sắc xanh, trắng, đỏ. Gọi $x$, $y$, $z$ là số chấm hiện trên mặt của các con súc sắc theo thứ tự xanh, trắng, đỏ.

a) Xác định không gian mẫu, nếu kết quả của mỗi lần gieo là $x + y + z.$

b) Giả sử kết quả của mỗi lần gieo là bộ ba sắp thứ tự $(x; y; z)$, không gian nẫu có bao nhiêu phần tử?

a) Không gian mẫu là: $Ω = \{3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\}.$

b) Vì $x$, $y$, $z$ đều là phần tử của tập hợp $\{1, 2, 3, 4, 5, 6\}$, do đó $x$ có $6$ cách xuất hiện, $y$ có $6$ cách xuất hiện, $z$ có $6$ cách xuất hiện. Vậy không gian mẫu $Ω$ có: $6.6.6 = 216$ phần tử.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 5. Một bình đựng $4$ viên bi xanh và $3$ viên bi đỏ.

a) Lấy ra đồng thời $2$ viên bi. Không gian mẫu có bao nhiêu phần tử?

b) Lấy một viên bi, gọi là $a$, để ra ngoài, rồi lại lấy một viên bi thứ hai, gọi là $b$. Kết quả là cặp sắp thứ tự $(a; b).$ Không gian mẫu có bao nhiêu phần tử?

c) Lấy một viên bi thứ nhất, gọi là $a$, bỏ lại vào bình, rồi lấy ra một viên bi thứ hai, gọi là $b.$ Kết quả là cặp sắp thứ tự $(a; b).$ Không gian mẫu có bao nhiêu phần tử?

a) Tổng số bi có trong bình là $7$ viên bi.

Lấy ra đồng thời $2$ viên bi (do đó không có tính thứ tự), nên đây là một tổ hợp chập $2$ của $7$. Vậy không gian mẫu có $C_7^2 = 21$ phần tử.

b) Lấy viên bi thứ nhất, ta có $7$ cách chọn. Lấy viên bi thứ hai, ta có $6$ cách chọn (vì trong bình chỉ còn $6$ viên bi). Vậy không gian mẫu là $6.7 = 42$ phần tử.

c) Lấy viên bi thứ nhất ta có $7$ cách chọn. Lấy viên bi thứ hai, ta có $7$ cách chọn (vì trong bình có $7$ viên bi). Vậy không gian mẫu là: $7.7 = 49$ phần tử.

<!-- chunk:9 level:2 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Dạng 2. Bài tập xác định biến cố và liệt kê các kết quả thuận lợi của biến cố.
Phương pháp: Giả sử $T$ là phép thử có không gian mẫu là $Ω$. Gọi $Ω_A$ là một tập con nào đó của $Ω.$

+ Mỗi khả năng của phép thử $T$ có kết quả được mô tả bởi $Ω_A$ được gọi là một biến cố $A$ liên quan đến phép thử $T$ (hay biến cố $A$ trong phép thử $T$).

+ Biến cố $A$ xảy ra khi và chỉ khi kết quả của $T$ thuộc tập $Ω_A.$

+ Mỗi phần tử của $Ω_A$ được gọi là một kết quả thuận lợi cho $A.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 6. Một con súc sắc được gieo $3$ lần liên tiếp. Quan sát số chấm xuất hiện. Xác định các biến cố sau:

$A$: “Tổng số chấm trong $3$ lần gieo là $6$”.

$B$: “Số chấm trong lần gieo thứ nhất bằng tổng số chấm của lần gieo thứ hai và thứ ba”.

Xác định các biến cố:

$A = \{(1; 1; 4), (1; 4; 1), (4; 1; 1), (1; 2; 3), (2; 3; 1),(1; 3; 2), (2; 1; 3), (3; 2; 1), (3; 1; 2), (2; 2; 2)\}.$ Tập $Ω_A$ có $10$ phần tử.

$B = \{(2; 1; 1), (3; 1; 2), (3; 2; 1), (4; 1; 3), (4; 3; 1),(4; 2; 2),(5; 1; 4), (5; 4; 1), (5; 2; 3), (5; 3; 2),(6; 1; 5),(6; 5; 1), (6; 2; 4), (6; 4; 2), (6; 3; 3)\}$. Tập $Ω_B$ có $15$ phần tử.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 7. Gieo ba con súc sắc đồng chất, cùng kích thước. Gọi $A$ là biến cố xuất hiện ba mặt không giống nhau (không cùng một số nút). Tính $|Ω|$ và $|Ω_A|.$

Số mặt (số nút) xuất hiện khi gieo một con súc sắc là sự lựa chọn ngẫu nhiên một số từ sáu số $1$, $2$, $3$, $4$, $5$, $6.$

Suy ra số cách xuất hiện khi gieo một con súc sắc là: $C_6^1 = 6.$

Do đó: $|\Omega | = C_6^1 \cdot C_6^1.C_6^1 = 6.6.6 = 216.$

Gọi $B$ là biến cố xuất hiện $3$ mặt giống nhau (cùng số nút) thì: $|Ω_B|=6.$

Suy ra: $\left| {{\Omega _A}} \right| = 216 – 6 = 210.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 8. Gieo một con súc sắc hai lần. Phát biểu các biến cố sau dưới dạng mệnh đề:

$A = \{(6; 1), (6; 2), (6; 3), (6; 4), (6; 5), (6; 6)\}.$

$B = \{(2; 6), (6; 2), (3; 5), (5; 3), (4; 4)\}.$

$C = \{(1; 1), (2; 2), (3; 3), (4; 4), (5; 5), (6; 6)\}.$

$A$ là biến cố “Lần gieo đầu xuất hiện mặt $6$ chấm”.

$B$ là biến cố “Tổng số chấm trong hai lần gieo là $8$”.

$C$ là biến cố “Kết quả của hai lần gieo xuất hiện mặt có số chấm giống nhau”.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 9. Gieo ngẫu nhiên một con súc sắc hai lần trên mặt phẳng và quan sát số chấm xuất hiện trên mặt ngửa.

a) Mô tả không gian mẫu.

b) Mô tả biến cố: “Tổng số chấm trên mặt ngửa trong hai lần gieo bằng $4$”.

c) Mô tả biến cố: “Số chấm trên mặt ngửa của hai lần gieo bằng nhau”.

a) Phép thử là gieo ngẫu nhiên một con súc sắc hai lần trên mặt phẳng.

Không gian mẫu là tập các cặp số $(i, j)$ với $i$, $j$ là các số $1$, $2$, $3$, $4$, $5$, $6.$

Đối với lần gieo thứ nhất, có $6$ khả năng xuất hiện các mặt $1$, $2$, $3$, $4$, $5$, $6.$ Ở lần gieo thứ hai, cũng có $6$ khả năng xuất hiện các mặt này. Theo quy tắc nhân, ta có $6.6 = 36$ kết quả đồng khả năng.

Suy ra không gian mẫu gồm $36$ phần tử như sau: $Ω = \{(1; 1), (1; 2), (1; 3), (1; 4), (1; 5), (1; 6),(2; 1), (2; 2), (2; 3), (2; 4), (2; 5), (2; 6),$$(3; 1), (3; 2), (3; 3), (3; 4), (3; 5), (3; 6),$$(4; 1), (4; 2), (4; 3), (4; 4), (4; 5), (4; 6),$$(5; 1), (5; 2), (5; 3), (5; 4), (5; 5), (5; 6),$$(6; 1), (6; 2), (6; 3), (6; 4), (6; 5), (6; 6)\}.$

Tổng quát: Phép thử “Gieo một con súc sắc cân đối và đồng chất $n$ lần” thì số phần tử của không gian mẫu là: $|\Omega | = {6^n}.$

b) Gọi $A$ là biến cố: “Tổng số chấm trên mặt ngửa bằng $4$” thì $A = \{(1; 3), (2; 2), (3; 1)\}.$ Ta nói có $3$ kết quả thuận lợi cho biến cố $A.$ Vậy $|Ω_A| = 3.$

c) Gọi $B$ là biến cố: “Số chấm trên mặt ngửa của hai con súc sắc bằng nhau” thì: $B = \{(1; 1), (2; 2), (3; 3), (4; 4), (5; 5), (6; 6)\}.$ Ta nói có $6$ kết quả thuận lợi cho biến cố $B.$ Vậy $|Ω_B| = 6.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 10. Gieo một đồng xu cân đối ba lần liên tiếp.

a) Mô tả không gian mẫu.

b) Xác định các biến cố:

$A$: “Lần đầu xuất hiện mặt sấp”.

$B$: “Mặt sấp xuất hiện đúng một lần”.

$C$: Mặt ngửa xuất hiện ít nhất một lần”.

a) Kết quả của ba lần gieo là một dãy có thứ tự các kết quả của từng lần gieo.

Do đó: $Ω= \{SSS, SSN, NSS, SNS, NNS, NSN, SNN, NNN\}.$

b)

$A = \{SSS, SSN, SNS, SNN\}.$ Tập $Ω_A$ có $4$ phần tử.

$B = \{SNN, NSN, NNS\}.$ Tập $Ω_B$ có $3$ phần tử.

$C = \{NNN, NNS, SNN, NSN, NSS, SSN, SNS\}$. Tập $Ω_C$ có $7$ phần tử.

<!-- chunk:15 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 11. Gieo một đồng xu sau đó gieo một con súc sắc. Quan sát sự xuất hiện mặt sấp $(S)$, mặt ngửa $(N)$ của đồng xu và số chấm xuất hiện của con súc sắc.

a) Xây dựng không gian mẫu.

b) Xác định các biến cố sau:

$A$: “Đồng xu xuất hiện mặt sấp và con súc sắc xuất hiện mặt có số chấm chẵn”.

$B$: “Mặt ngửa của đồng xu và mặt có số chấm lẻ của con súc sắc xuất hiện”.

$C$: “Mặt $6$ chấm xuất hiện”.

a) Không gian mẫu là: $Ω = \{S1, S2, S3, S4, S5, S6,$ $N1, N2, N3, N4, N5, N6\}.$

b) $A = \{S2, S4, S6\}$, $B = \{N1, N3, N6\}$, $C = \{S6, N6\}.$

<!-- chunk:16 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 12. Từ một hộp chứa năm quả cầu được đánh số $1$, $2$, $3$, $4$, $5$ lấy ngẫu nhiên liên tiếp hai lần mỗi lần một quả và xếp theo thứ tự từ trái sang phải.

a) Xây dựng không gian mẫu.

b) Xác định các biến cố sau:

$A$: “Chữ số sau lớn hơn chữ số trước”.

$B$: “Chữ số trước gấp đôi chữ số sau”.

$C$: “Hai chữ số bằng nhau”.

a) Vì việc lấy ngẫu nhiên liên tiếp hai lần mỗi lần lấy một quả và xếp thứ tự nên mỗi lần lấy ta được một chỉnh hợp chập $2$ của $5$ chữ số:

$Ω = \{12, 21, 13, 31, 14, 41, 15, 51, 23, 32,$ $24, 42, 25, 52, 34, 43, 35, 53, 45, 54\}.$

b) $A = \{12, 13, 14, 15, 23, 24, 25, 34, 35, 45\}$, $B = \{21, 42\}$, $C = Ø.$

<!-- chunk:17 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 13. Một hộp chứa bốn cái thẻ được đánh số $1$, $2$, $3$, $4$. Lấy ngẫu nhiên hai thẻ.

a) Mô tả không gian mẫu.

b) Xác định các biến cố sau:

$A$: “Tổng các số trên hai thẻ là số chẵn”.

$B$: “Tích các số trên hai thẻ là số chẵn”.

a) $Ω = \{(1; 2), (1; 3), (1; 4), (2; 3), (2; 4), (3; 4)\}.$

b) $A = \{(1; 3), (2; 4)\}$, $B = \{(1; 2), (1; 4), (2; 3), (2, 4), (3; 4)\}.$

<!-- chunk:18 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 14. Từ một hộp chứa $10$ cái thẻ, trong đó các thẻ đánh số $1$, $2$, $3$, $4$, $5$ màu đỏ, thẻ đánh số $6$ màu xanh và các thẻ đánh số $7$, $8$, $9$, $10$ màu trắng. Lấy ngẫu nhiên một thẻ.

a) Mô tả không gian mẫu.

b) Kí hiệu $A$, $B$, $C$ là các biến cố sau:

$A$: “Lấy được thẻ màu đỏ”.

$B$: “Lấy được thẻ màu trắng”.

$C$: “Lấy được thẻ ghi số chẵn”.

Hãy biểu diễn các biến cố $A$, $B$, $C$ bởi các tập hợp con tương ứng của không gian mẫu.

a) Không gian mẫu $Ω$ được mô tả bởi tập $Ω = \{1, 2,…, 10\}.$

b)

$A = \{1, 2, 3, 4, 5\}$ là biến cố: “Lấy được thẻ màu đỏ”.

$B = \{7, 8, 9, 10\}$ là biến cố: “Lấy được thẻ màu trắng”.

$C = \{2, 4, 6, 8, 10\}$ là biến cố: “Lấy được thẻ ghi số chẵn”.

<!-- chunk:19 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 15. Trong bình có $6$ viên bi kích thước khác nhau, trong đó có $4$ viên bi trắng và $2$ viên bi vàng. Lấy ngẫu nhiên $3$ viên bi.

a) Mô tả không gian mẫu.

b) Mô tả biến cố: “Có $2$ viên bi trắng”.

c) Biến cố: “Có nhiều nhất $2$ viên bi trắng” có bao nhiêu khả năng thuận lợi?

a) Kí hiệu $4$ viên bi trắng là $T_1$, $T_2$, $T_3$, $T_4$, $2$ viên bi vàng là $V_1$, $V_2$.

Mỗi cách lấy $3$ viên bi là một tổ hợp chập $3$ của $6$ phần tử là các viên bi.

Vậy không mẫu gồm có $C_6^3 = 20$ phần tử:

$Ω = \{{T_1}{T_2}{T_3}, {T_1}{T_2}{T_4}, {T_1}{T_3}{T_4}, {T_2}{T_3}{T_4}, {T_1}{T_2}{V_1},$ ${T_1}{T_3}{V_1}, {T_1}{T_4}{V_1}, {T_2}{T_3}{V_1}, {T_2}{T_4}{V_1}, {T_3}{T_4}{V_1},$ ${T_1}{T_2}{V_2}, {T_1}{T_3}{V_2}, {T_1}{T_4}{V_2}, {T_2}{T_3}{V_2}, {T_2}{T_4}{V_2},$ ${T_3}{T_4}{V_2}, {V_1}{V_2}{T_1}, {V_1}{V_2}{T_2}, {V_1}{V_2}{T_3}, {V_1}{V_2}{T_4}\}.$

b) Gọi $A$ là biến cố: “Trong $3$ viên bi lấy ra có $2$ viên bi trắng” thì:

$Ω_A = \{ {T_1}{T_2}{V_1},{T_1}{T_3}{V_1},{T_1}{T_4}{V_1},{T_2}{T_3}{V_1},$ ${T_2}{T_4}{V_1},{T_3}{T_4}{V_1},{T_1}{T_2}{V_2},{T_1}{T_3}{V_2},$ ${T_1}{T_4}{V_2},{T_2}{T_3}{V_2},{T_2}{T_4}{V_2},{T_3}{T_4}{V_2}\}.$

c) Gọi $B$ là biến cố: “Trong $3$ viên bi lấy ra có nhiều nhất $2$ viên bi trắng”, thì có $2$ cách sau:

+ $1$ viên bi trắng và $2$ viên bi vàng.

+ $2$ viên bi trắng và $1$ viên bi vàng.

Vậy $\left| {{\Omega _B}} \right| = C_4^2 \cdot C_2^1 + C_4^1 \cdot C_2^2 = 12 + 4 = 16.$

<!-- chunk:20 level:3 source:https://toanmath.com/2018/09/bai-toan-ve-phep-thu-va-bien-co.html -->
## Ví dụ 16. Gieo một con súc sắc được chế tạo cân đối và đồng chất ba lần liên tiếp. Gọi $A$ là biến cố: “Tổng số chấm trên mặt xuất hiện của con súc sắc trong ba lần gieo bằng $9$”.

a) Mô tả không gian mẫu.

b) Mô tả tập $Ω_A$ các kết quả thuận lợi cho $A.$

a) Nếu kí hiệu $a$, $b$, $c$ theo thứ tự là số chấm xuất hiện trên mặt con súc sắc ở lần gieo thứ nhất, thứ hai và thứ ba thì mỗi kết quả của phép thử $T$ (gieo một con súc sắc được chế tạo cân đối đồng chất ba lần liên tiếp) là một bộ ba số $(a; b; c)$ trong đó $a$, $b$, $c$ là các số nguyên dương không lớn hơn $6.$

Vậy $Ω = \{(a; b; c) | 1 < a, b, c < 6, a, b, c$ nguyên dương $\}.$

b) $Ω_A = \{(a; b; c) | a, b, c < 6, a + b + c = 9; a, b, c$ nguyên dương $\}.$

Ta cần đếm số kết quả thuận lợi. Ta cần liệt kê các bộ ba $(a; b; c)$ với $a$, $b$, $c$ nguyên dương không lớn hơn $6$ và có tổng bằng $9$. Đó là:

+ Bộ $(1; 2; 6)$ và các hoán vị của nó. Có $6$ bộ như vậy.

+ Bộ $(1; 3; 5)$ và các hoán vị của nó. Có $6$ bộ như vậy.

+ Bộ $(1; 4; 4)$ và các hoán vị của nó. Có $3$ bộ như vậy.

+ Bộ $(2; 2; 5)$ và các hoán vị của nó. Có $3$ bộ như vậy.

+ Bộ $(2; 3; 4)$ và các hoán vị của nó. Có $6$ bộ như vậy.

+ Bộ $(3; 3; 3)$.

Vậy số kết quả thuận lợi là $6 + 6 + 6 + 3 + 3 + 1 = 25.$