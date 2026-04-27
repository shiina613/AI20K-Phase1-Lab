# Lập số thuộc một khoảng hoặc một đoạn cho trước

<!-- chunk:0 level:0 source:https://toanmath.com/2020/01/lap-so-thuoc-mot-khoang-hoac-mot-doan-cho-truoc.html -->
Bài viết hướng dẫn phương pháp giải bài toán lập số thuộc một khoảng hoặc một đoạn cho trước, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11 chương 2: Tổ hợp và Xác suất.

1. PHƯƠNG PHÁP GIẢI TOÁN
• Phương pháp lập số $n$ bé hơn số $N = \overline {{A_1}{A_2}{A_3} \ldots {A_k}}$ có $k$ chữ số:

Trường hợp 1: Nếu số các chữ số trong $n$ nhỏ hơn $k$ chữ số thì các số chữ số trong $n$ được chọn tùy ý.

Trường hợp 2: Nếu $n$ cũng có $k$ chữ số tức là $n$ có dạng $n = \overline {{a_1}{a_2}{a_3} \ldots {a_k}}$ thì có thể chia nhỏ trường hợp này bằng cách:

+ Bước 1: Xét ${a_1} < {A_1}.$ Từ đó chọn:

${a_1}$ thích hợp.

${a_2}$, ${a_3}$, …, ${a_k}$ chọn tùy ý.

+ Bước 2: 
$$
\left\{ {\begin{array}{l}
{{a_1} = {A_1}}\\
{{a_2} < {A_2}}
\end{array}} \right..
$$

Từ đó chọn:

${a_2}$ thích hợp.

${a_3}$, …, ${a_k}$ chọn tùy ý.

Tiếp tục so sánh các hàng tiếp theo sau đó và chọn các chữ số sau đó tương ứng.

Thực hiện phép so sánh và chọn ở các bước trên cho đến hàng cuối cùng thì kết thúc.

Dùng quy tắc cộng cộng tất cả các trường hợp ở các bước vừa xét ta được số các số $n$ cần lập.

• Lập số $n$ lớn hơn số $N$ có $k$ chữ số cũng thực hiện tương tự như trên. Chỉ thay đổi ở trường hợp 1 (nếu có) ta xét số $n$ có số chữ số lớn hơn $k.$

Lưu ý:

+ Lập số $n$ thuộc một khoảng hoặc một đoạn $D$ nào đó thì kết hợp hai phương pháp trên.

+ Một số bài toán khi thực hiện có thể kết thúc ngay ở bước thứ $i$ mà không phải xét đến các bước còn lại.

+ Trong một số bài toán có quá nhiều trường hợp thì có thể dùng phương pháp đếm gián tiếp để thực hiện.

## Bài tập
## Bài 1: Từ tập $A = \{ 1;2;3;4;5;6\}$ có thể lập được bao nhiêu số tự nhiên:

a) Có các chữ số khác nhau và bé hơn $100.$

b) Có các chữ số khác nhau và lớn hơn $5400.$

Lời giải:

a) Số tự nhiên bé hơn $100$ thì có thể có $1$ chữ số hoặc $2$ chữ số.

* Trường hợp 1: Số tự nhiên có $1$ chữ số thì có $6$ số chọn từ $1$ trong các chữ số $1$, $2$, $3$, $4$, $5$, $6.$

* Trường hợp 2: Số tự nhiên có $2$ chữ số khác nhau lập từ $A$ có $A_6^2 = 30$ số.

Vậy tất cả có: $6 + 30 = 36$ số tự nhiên có các chữ số khác nhau và bé hơn $100.$

b) Xét các trường hợp sau:

* Trường hợp 1: Số tự nhiên cần lập có $6$ chữ số khác nhau thì có $6! = 720$ số.

* Trường hợp 2: Số tự nhiên cần lập có $5$ chữ số khác nhau thì có $A_6^5 = 720$ số.

* Trường hợp 3: Số tự nhiên cần lập có $4$ chữ số khác nhau:

Gọi số tự nhiên có dạng: $n = \overline {abcd} > 5400.$

+ Xét $a>5$, khi đó:

Có $1$ cách chọn $a$ (là chữ số $6$).

$b$, $c$, $d$ chọn tùy ý trong $A\backslash \{ 6\}$ thì có $A_5^3 = 60$ cách chọn.

Suy ra có: $1.60 = 60$ số.

+ Xét 
$$
\left\{ {\begin{array}{l}
{a = 5}\\
{b > 4}
\end{array}} \right.
$$
, khi đó:

Có $1$ cách chọn $b$ (là chữ số $6$).

Các chữ số $c$, $d$ chọn tùy ý trong $A\backslash \{ 5;6\}$ thì có $A_4^2 = 12$ cách chọn.

Suy ra có: $1.12 = 12$ số.

Suy ra trường hợp này có: $12 + 60 = 72$ số.

Vậy tất cả có: $720 + 720 + 72 = 1512$ số có các chữ số khác nhau và lớn hơn $5400.$

## Bài 2:

## Bài tập 1. Có bao nhiêu số chẵn có ba chữ số khác nhau được tạo thành từ các chữ số $1$, $2$, $3$, $4$, $5.$

## Bài tập 2. Có bao nhiêu số có ba chữ số khác nhau được tạo thành từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$ mà các số đó nhỏ hơn số $345.$

Lời giải:

## Bài tập 1. Xét các số chẵn $x = \overline {abc}$ với $3$ chữ số khác nhau; $a,b,c \in \{ 1;2;3;4;5\} = E.$

Vì $x$ chẵn nên $c \in \{ 2;4\}$ $\Rightarrow$ có $2$ cách chọn $c.$

Với mỗi cách chọn $c$, có $A_4^2$ cách chọn $\overline {bc} .$

Vậy tất cả có: $2.A_4^2 = 24$ số chẵn.

## Bài tập 2. Xét $x = \overline {abc}$ với $3$ chữ số khác nhau thuộc $E = \{ 1;2;3;4;5;6\} .$

+ Xét $a <3$ khi đó:

Có $2$ cách chọn $a$ (chọn số $1$ hoặc số $2$).

$b$ và $c$ chọn tùy ý từ trong tập $E\backslash \{ a\}$ có $A_5^2$ cách chọn $b$ và $c.$

Loại này có $2.A_5^2 = 40$ số.

+ Xét $a = 3$ khi đó:

Nếu $b$ bằng $1$ hoặc $2$ thì $c$ chọn tùy ý trong tập $E\backslash \{ 3;b\}$, tức là có $4$ cách chọn $c.$

Suy ra có: $2.4 = 8$ số.

Nếu $b = 4$ thì $c$ có $2$ cách chọn là $1$ hoặc $2.$

Suy ra có $2$ số.

Vậy loại này có $8 + 2 = 10$ số.

Vậy tất cả có: $40 + 10 = 50$ số tự nhiên có $3$ chữ số khác nhau và nhỏ hơn số $345.$

## Bài 3: Có bao nhiêu số lẻ gồm $6$ chữ số khác nhau lớn hơn $500000$?

Lời giải:

Xét số lẻ có $6$ chữ số khác nhau, lớn hơn $500000:$

$x = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}} .$

Từ giả thiết $\Rightarrow {a_1} \in \{ 5,6,7,8,9\}$, ${a_6} \in \{ 1,3,5,7,9\} .$

Có $2$ khả năng:

## Bài tập 1. ${a_1}$ lẻ:

${a_1}$ có $3$ cách chọn.

${a_6}$ có $4$ cách chọn.

Sau khi chọn ${a_1}$, ${a_6}$, cần chọn $\overline {{a_2}{a_3}{a_4}{a_5}}$, mỗi cách chọn ứng với một chỉnh hợp chập $4$ của $8$ phần tử.

Vậy khả năng thứ nhất có: $3.4.{\rm{ }}A_8^4 = 20160$ số.

## Bài tập 2. ${a_1}$ chẵn:

${a_1}$ có $2$ cách chọn.

${a_6}$ có $5$ cách chọn.

$\overline {{a_2}{a_3}{a_4}{a_5}}$ có $A_8^4$ cách chọn.

Vậy khả năng thứ hai có: $2.5.A_8^4 = 16800$ số.

Kết luận: Tất cả có: $20160 + 16800 = 36960$ số cần tìm.

## Bài 4:

## Bài tập 1. Có bao nhiêu số chẵn có ba chữ số khác nhau được tạo thành từ các chữ số $1$, $2$, $3$, $4$, $5.$

## Bài tập 2. Có bao nhiêu số có ba chữ số khác nhau được tạo thành từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$ mà các số đó nhỏ hơn số $345.$

Lời giải:

## Bài tập 1. Xét các số chẵn $x = \overline {abc}$ với $3$ chữ số khác nhau; $a,b,c \in \{ 1;2;3;4;5\} = E.$

Vì $x$ chẵn nên $c \in \{ 2;4\}$ $\Rightarrow c$ có $2$ cách chọn $c.$

Với mỗi cách chọn $c$, có $A_4^2$ cách chọn $\overline {bc} .$

Vậy tất cả có: $2.A_4^2 = 24$ số chẵn.

## Bài tập 2. Xét $x = \overline {abc}$ với $3$ chữ số khác nhau thuộc $E = \{ 1;2;3;4;5;6\} .$

+ Xét $a< 3$ khi đó:

Có $2$ cách chọn a (chọn số $1$ hoặc số $2$).

$b$ và $c$ chọn tùy ý từ trong tập $E\backslash \{ a\}$ có $A_5^2$ cách chọn $b$ và $c.$

Loại này có $2.A_5^2 = 40$ số.

+ Xét $a=3$ khi đó:

Nếu $b$ bằng $1$ hoặc $2$ thì $c$ chọn tùy ý trong tập $E\backslash \{ 3;b\}$, tức là có $4$ cách chọn $c.$

Suy ra có: $2.4 = 8$ số.

Nếu $b = 4$ thì $c$ có $2$ cách chọn là $1$ hoặc $2.$

Suy ra có $2$ số.

Vậy loại này có $8 + 2 = 10$ số.

Vậy tất cả có: $40 + 10 = 50$ số tự nhiên có $3$ chữ số khác nhau và nhỏ hơn số $345.$

## Bài 5: Với các chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ có thể lập được bao nhiêu số chẵn có ba chữ số khác nhau và không lớn hơn $789$?

Lời giải:

Ta xét các trường hợp sau:

## Bài tập 1. Chữ số hàng đơn vị là $2$, $4$, $6$ $\Rightarrow$ có $3$ cách chọn chữ số hàng đơn vị.

a) Chữ số hàng trăm nhỏ hơn $7$: Khi đã chọn chữ số hàng đơn vị, ta còn $5$ cách chọn chữ số hàng trăm. Sau khi đã chọn chữ số hàng đơn vị và hàng trăm, ta còn $7$ cách chọn chữ số hàng chục.

Suy ra số các số thu được là: $3.5.7 = 105$ số.

b) Chữ số hàng trăm bằng $7$: Sau khi chọn chữ số hàng đơn vị, ta còn $6$ cách chọn chữ số hàng chục.

Suy ra số các số thu được là: $3.6 = 18$ số.

## Bài tập 2. Chữ số hàng đơn vị là $8$:

a) Chữ số hàng trăm nhỏ hơn $7$: có $6$ cách chọn chữ số hàng trăm. Sau khi đã chọn chữ số hàng trăm, ta còn $7$ cách chọn chữ số hàng chục.

Suy ra số các số thu được là: $6.7 = 42$ số.

b) Chữ số hàng trăm bằng $7$: có $6$ cách chọn chữ số hàng chục.

Suy ra số các số thu được là: $6$ số.

Vậy tất cả có: $105 + 18 + 42 + 6 = 171$ số.

## Bài 6: Từ các số $0$, $4$, $5$, $7$, $9.$

a) Tìm tất cả các số có bốn chữ số khác nhau.

b) Có bao nhiêu số có $4$ chữ số khác nhau và lớn hơn $5000.$

c) Có bao nhiêu số tự nhiên có $4$ chữ số khác nhau và chia hết cho $5.$

Lời giải:

a) Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm, ta có:

Có $4$ cách chọn $a$, trừ số $0.$

Có $4$ cách chọn $b.$

Có $3$ cách chọn $c.$

Có $2$ cách chọn $d.$

Vậy theo quy tắc nhân có: $4.4.3.2 = 96$ số.

b) Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm.

Vì $n>5000$ do đó $a \ge 5$, còn các chữ số $b$, $c$, $d$ được chọn khác nhau tùy ý.

Có $3$ cách chọn $a$; $b$, $c$, $d$ có $A_4^3$ cách chọn.

Vậy có $3.A_4^3 = 72$ số.

c) Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm.

Vì $n$ chia hết cho $5$ nên $d$ có thể bằng $0$ hoặc bằng $5.$

+ Nếu $d= 0$, khi đó: $a$, $b$, $c$ có $A_4^3 = 24$ cách chọn.

Vậy trường hợp này có $24$ số.

+ Nếu $d=5$, khi đó:

Có $3$ cách chọn $a$, trừ số $0$ và $5.$

Có $3$ cách chọn $b.$

Có $2$ cách chọn $c.$

Vậy trường hợp này có $3.3.2 = 18$ số.

Vậy tất cả có $24 + 18 = 42$ số.

## Bài 7: Từ các số $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$ có thể lập được bao nhiêu số tự nhiên gồm $6$ chữ số lớn hơn $543000$?

Lời giải:

Gọi số tự nhiên cần tìm có dạng: $n = \overline {abcdef} .$

Xét các trường hợp sau:

+ Nếu $a>5$, khi đó:

Có $4$ cách chọn $a.$

Có $10.10.10.10.10 = 100000$ cách chọn $b$, $c$, $d$, $e$, $f.$

Suy ra trường hợp này có: $400000$ số.

+ Nếu 
$$
\left\{ {\begin{array}{l}
{a = 5}\\
{b > 4}
\end{array}} \right.
$$
, khi đó:

Có $5$ cách chọn $b.$

Các chữ số còn lại có $10.10.10.10 = 10000$ cách chọn.

Suy ra loại này có $50000$ số.

+ Nếu 
$$
\left\{ {\begin{array}{l}
{a = 5,b = 4}\\
{c > 3}
\end{array}} \right.
$$
, khi đó:

Có $6$ cách chọn $c.$

Các chữ số còn lại có $10.10.10 = 1000$ cách chọn.

Suy ra loại này có $6000$ số.

+ Nếu 
$$
\left\{ {\begin{array}{l}
{a = 5,b = 4}\\
{c = 3}
\end{array}} \right.
$$
, khi đó:

Có $10.10.10 = 1000$ cách chọn các chữ số $d$, $e$, $f.$

Tức là có $1000$ số có dạng $\overline {543def}$, trong $1000$ số trên có $1000 – 1 = 999$ số lớn hơn $543000.$

Vậy tất cả có: $400000 + 50000 + 6000 + 999 = 456999$ số tự nhiên có $6$ chữ số lớn hơn $543000.$

## Bài 8: Có bao nhiêu số tự nhiên có $4$ chữ số:

a) Khác nhau, và là số tự nhiên lẻ bé hơn $9000.$

b) Có dạng: lẻ, chẵn, lẻ, chẵn.

Lời giải:

a) Gọi số tự nhiên cần tìm có dạng: $n = \overline {abcd} .$

Do $n < 9000$ nên $a < 9.$

Mặt khác do $n$ lẻ nên $d$ phải là chữ số lẻ, do đó ta xét các trường hợp sau:

+ Nếu $d=9$, khi đó:

Có $8$ cách chọn $a.$

Có $8$ cách chọn $b.$

Có $7$ cách chọn $c.$

Suy ra trường hợp này có $8.8.7 = 448$ số.

+ Nếu $d \ne 9$, khi đó:

Có $4$ cách chọn $d$, $d \in \{ 1;3;5;7\} .$

Có $7$ cách chọn $a$, $(a \ne d,a \ne 0,a \ne 9).$

Có $8$ cách chọn $b.$

Có $7$ cách chọn $d.$

Suy ra loại này có $4.7.8.7 = 1568$ số.

Vậy tất cả có $448 + 1568 = 2016$ số tự nhiên lẻ có $4$ chữ số khác nhau và bé hơn $9000.$

b) Gọi số tự nhiên cần tìm có dạng: $n = \overline {abcd} .$

Có $5$ cách chọn $a$, $a \in \{ 1;3;5;7;9\} .$

Có $5$ cách chọn $b$, $b \in \{ 0;2;4;6;8\} .$

Có $5$ cách chọn $c$, $c \in \{ 1;3;5;7;9\} .$

Có $5$ cách chọn $d$, $d \in \{ 0;2;4;6;8\} .$

Vậy có $5.5.5.5 = 625$ số tự nhiên có $4$ chữ số dạng: lẻ, chẵn, lẻ, chẳn.

## Bài 9: Từ các số $1$, $2$, $3$, $4$, $5.$ Có thể lập được bao nhiêu số tự nhiên nằm trong khoảng $(300;500)$, biết rằng:

a) Số tự nhiên đó có $3$ chữ số khác nhau.

b) Số tự nhiên đó có $3$ chữ số không nhất thiết phải khác nhau.

Lời giải:

Gọi $n = \overline {abc}$ là số tự nhiên cần tìm.

a) Do $n \in (300;500)$ nên $a$ chỉ có thể là $3$ hoặc $4$, do đó:

Có $2$ cách chọn $a.$

Có $4$ cách chọn $b.$

Có $3$ cách chọn $c.$

Vậy có: $2.4.3 = 24$ số.

b) Do $n \in (300;500)$ nên $a$ chỉ có thể là $3$ hoặc $4$, và $b$, $c$ được chọn tùy ý.

Có $2$ cách chọn $a.$

Có $5$ cách chọn $b.$

Có $5$ cách chọn $c.$

Vậy có $2.5.5 = 50$ số.

## Bài 10: Có bao nhiêu số tự nhiên lẻ gồm $5$ chữ số khác nhau và lớn hơn $70000.$

Lời giải:

Gọi $n = \overline {abcde}$ là số tự nhiên cần tìm.

Vì $n$ lẻ nên $e \in \{ 1;3;5;7;9\} .$

Vì $n > 70000$ nên $a \in \{ 7;8;9\} .$

+ Nếu $a$ lẻ khi đó:

Có $2$ cách chọn $a$ là $7$ hoặc $9.$

Có $4$ cách chọn $e.$

Có $A_8^3 = 336$ cách chọn $b$, $c$, $d.$

Suy ra trường hợp này có $2.4.336 = 2688$ số.

+ Nếu $a$ chẵn, khi đó:

Có $1$ cách chọn $a$ là số $8.$

Có $5$ cách chọn $e.$

Có $A_8^3 = 336$ cách chọn $b$, $c$, $d.$

Suy ra trường hợp này có $1.5.336 = 1680$ số.

Vậy tất cả có $2688 + 1680 = 4368$ số.

## Bài 11: Cho các chữ số $1$, $2$, $5$, $7$, $8$ có bao nhiêu cách lập ra một số có ba chữ số khác nhau từ $5$ chữ số đã cho, sao cho:

a) Số tạo thành là một số chẵn.

b) Số tạo thành là một số không có chữ số $7.$

c) Số tạo thành là một số nhỏ hơn $278.$

Lời giải:

Gọi $n = \overline {abc}$ là số cần tìm.

a) Vì $n$ chẵn nên $c \in \{ 2;8\}$, do đó:

Có $2$ cách chọn $c.$

Có $4$ cách chọn $a.$

Có $3$ cách chọn $b.$

Vậy có: $2.4.3 = 24$ số chẵn.

b) Số tạo thành không có chữ số $7$ nên mỗi số tạo thành là một cách lấy có thứ tự $3$ chữ số trong $4$ chữ số.

Vậy có: $A_4^3 = 24$ số.

c) Ta xét các trường hợp sau:

+ Nếu $a =1$, khi đó $n = \overline {1bc} < 278$, $\forall b$, $c.$

Có $4$ cách chọn $b.$

Có $3$ cách chọn $c.$

Vậy trường hợp này có $4.3 = 12$ số.

+ Nếu $a= 2$, ta xét:

Khi $b < 7$, thì $c$ chọn tùy ý.

Có $2$ cách chọn $b.$

Có $3$ cách chọn $c.$

Suy ra có $2.3 = 6$ số.

Khi $b=7$, thì $c$ phải nhỏ hơn $8.$

Có $2$ cách chọn $c$, nghĩa là có $2$ số $n.$

Vậy trường hợp này có $6 + 2 = 8$ số.

Vậy tất cả có $12 + 8 = 20$ số nhỏ hơn $278.$

## Bài 12: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$ lập thành số tự nhiên chẵn có $5$ chữ số phân biệt nhỏ hơn $25000.$ Tính số các số lập được.

Lời giải:

Gọi số cần lập là $A = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}}$ với $1 \le {a_1} \le 2.$

+ Trường hợp 1: ${a_1} = 1.$

Có $4$ cách chọn ${a_5}$ và $A_5^3$ cách chọn các chữ số còn lại nên có $4.A_5^3 = 240$ số.

+ Trường hợp 2: ${a_1} = 2$, ${a_2}$ lẻ.

Có $2$ cách chọn ${a_2}$, $3$ cách chọn ${a_5}$ và $A_4^2$ cách chọn các chữ số còn lại nên có $2.3.A_4^2 = 72$ số.

+ Trường hợp 3: ${a_1} = 2$, ${a_2}$ chẵn.

Có $2$ cách chọn ${a_2}$, $2$ cách chọn ${a_5}$ và $A_4^2$ cách chọn các chữ số còn lại nên có $2.2.A_4^2 = 48$ số.

Vậy có $240 + 72 + 48 = 360$ số.

## Bài 13: Từ các chữ số $0$; $1$; $2$; $3$; $4$; $5$ có thể lập được bao nhiêu số tự nhiên có $3$ chữ số khác nhau và bé hơn $341.$

Lời giải:

Gọi $n = \overline {abc}$ là số tự nhiên cần tìm.

Xét các trường hợp sau:

+ Nếu $a < 3$, khi đó:

Có $2$ cách chọn $a.$

Có $A_5^2 = 20$ cách chọn $2$ chữ số xếp vào $b$, $c.$

Suy ra có $2.20 = 40$ số.

+ Nếu $a = 3$, suy ra: $n = \overline {3bc} .$

Nếu $b < 4$, thì có $3$ cách chọn $b$ và $4$ cách chọn $c.$ Suy ra có $3.4 = 12$ số.

Nếu $b = 4$, thì $n = \overline {34c}$, suy ra có $1$ cách chọn $c$ (là chữ số $0$). Do đó có $1$ số, suy ra trường hợp này có $12 + 1 = 13$ số.

Vậy tất cả có $40 + 13 = 53$ số.

## Bài 14: Từ các số: $0$, $4$, $5$, $7$, $8$, $9.$ Ta có thể lập được bao nhiêu số tự nhiên:

a) Có $4$ chữ số đôi một khác nhau.

b) Có $3$ chữ số khác nhau và luôn có mặt chữ số $9.$

c) Có $3$ chữ số và lớn hơn $400.$

Lời giải:

a) Gọi số tự nhiên cần lập có dạng: $n = \overline {abcd} .$

Có $5$ cách chọn $a.$

Có $A_5^3 = 60$ cách chọn $3$ chữ số xếp vào $b$, $c$, $d.$

Vậy có $5.60 = 300$ số.

b) Gọi $n = \overline {abc}$ là số tự nhiên có $3$ chữ số.

Có $5$ cách chọn $a.$

Có $6$ cách chọn $b.$

Có $6$ cách chọn $c.$

Suy ra có $5.6.6=180$ số.

Xét các số tự nhiên dạng $n = \overline {abc}$ mà không có mặt chữ số $9$, khi đó:

Có $4$ cách chọn $a.$

Có $5$ cách chọn $b.$

Có $5$ cách chọn $c.$

Suy ra có $4.5.5 = 100$ số tự nhiên có $3$ chữ số mà không có mặt chữ số $9.$

Vậy có $180 – 100 = 80$ số tự nhiên có $3$ chữ số trong đó luôn có mặt chữ số $9.$

c) Xét các số tự nhiên có dạng $n = \overline {abc}$, với $a \ge 4.$

Có $5$ cách chọn $a.$

Có $6$ cách chọn $b.$

Có $6$ cách chọn $c.$

Suy ra có $5.6.6 = 180$ số.

Trong các số tự nhiên trên chỉ có duy nhất $1$ số là $400$ không thỏa mãn yêu cầu bài toán.

Vậy có $180 – 1= 179$ số tự nhiên có $4$ chữ số và lớn hơn $400.$

## Bài 15: Từ các số $0$, $2$, $3$, $4$, $5$, $6.$ Ta có thể lập được bao nhiêu số tự nhiên:

a) Là số chẵn có $3$ chữ số.

b) Số có $4$ chữ số và luôn có mặt chữ số $5.$

c) Số có $3$ chữ số và lớn hơn $250.$

Lời giải:

a) Gọi số tự nhiên cần lập có dạng: $n = \overline {abc} .$

Có $4$ cách chọn $c.$

Có $5$ cách chọn $a.$

Có $6$ cách chọn $b.$

Vậy có $4.5.6 = 120$ số tự nhiên chẵn có $3$ chữ số.

b) Gọi $n = \overline {abcd}$ là số tự nhiên có $4$ chữ số:

Có $5$ cách chọn $a.$

Có $6$ cách chọn $b.$

Có $6$ cách chọn $c.$

Có $6$ cách chọn $d.$

Suy ra có $5.6.6.6 = 1080$ số.

Xét các số tự nhiên dạng $n = \overline {abcd}$ mà không có mặt chữ số $5$, khi đó:

Có $4$ cách chọn $a.$

Có $5$ cách chọn $b.$

Có $5$ cách chọn $c.$

Có $5$ cách chọn $d.$

Suy ra có $4.5.5.5 = 500$ số có $4$ chữ số mà không có mặt chữ số $5.$

Vậy có $1080 – 500 = 580$ số tự nhiên có $4$ chữ số và luôn có mặt chữ số $5.$

c) Gọi số tự nhiên cần lập có dạng: $n = \overline {abc} .$ Xét các trường hợp sau:

+ Nếu $a> 2$, khi đó:

Có $4$ cách chọn $a.$

Có $A_5^2 = 20$ cách chọn $b$, $c.$

Suy ra trường hợp này có $4.20 = 80$ số.

+ Nếu 
$$
\left\{ {\begin{array}{l}
{a = 2}\\
{b > 5}
\end{array}} \right.
$$
, khi đó:

Có $1$ cách chọn $b.$

Có $4$ cách chọn $c.$

Suy ra trường hợp này có $4$ số.

+ Nếu 
$$
\left\{ {\begin{array}{l}
{a = 2}\\
{b = 5}
\end{array}} \right.
$$
, khi đó: có $3$ cách chọn $c.$

Suy ra trường hợp này có $3$ số.

Vậy tất cả có $20 + 4 + 3 = 27$ số.

## Bài 16:

a/ Từ các số: $0$, $1$, $2$, $3$, $4$, $5$, $6$ có thể lập được bao nhiêu số lẻ có $3$ chữ số khác nhau nhỏ hơn $400$?

b/ Từ các chữ số $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số có $3$ chữ số khác nhau nằm trong khoảng $(300;500).$

Lời giải:

a) Gọi $n = \overline {abc}$ là số tự nhiên cần tìm.

Do $n< 400$ nên $n< 4$, xét các trường hợp sau:

+ Nếu $a$ chẵn, khi đó:

Có $1$ cách chọn $a$, là chữ số $2.$

Có $3$ cách chọn $c$, $c \in \{ 1;3;5\} .$

Có $5$ cách chọn $b.$

Suy ra trường hợp này có $1.3.5 = 15$ số.

Nếu $a$ lẻ, khi đó:

Có $2$ cách chọn $a$, $a \in \{ 1;3\} .$

Có $2$ cách chọn $c.$

Có $5$ cách chọn $b.$

Suy ra trường hợp này có $2.2.5 = 20$ số.

Vậy tất cả có $15 + 20 = 35$ số.

b) Gọi $n = \overline {abc}$ là số tự nhiên cần tìm.

Do $n \in (300;500)$ nên:

Có $2$ cách chọn $a$, là chữ số $3$ hoặc $4.$

Có $A_4^2 = 12$ cách chọn $2$ chữ số xếp vào $b$, $c.$

Vậy có $2.12 = 24$ số.