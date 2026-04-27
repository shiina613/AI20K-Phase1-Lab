# Lập số chứa hoặc không chứa chữ số nào đó

<!-- chunk:0 level:0 source:https://toanmath.com/2020/01/lap-so-chua-hoac-khong-chua-chu-so-nao-do.html -->
Bài viết hướng dẫn phương pháp giải bài toán lập số chứa hoặc không chứa chữ số nào đó, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và Xác suất.

1. PHƯƠNG PHÁP CHUNG
a. Lập số chứa số $x$ nào đó: Ta thực hiện như sau:

+ Gọi số cần lập theo dạng $n = \overline {abc \ldots }$ hoặc $n =$ ▯▯▯….

+ Tính số cách chèn chữ số $x$ trong $n$ (hay số cách chọn vị trí của $x$ trong $n$).

+ Chọn các chữ số còn lại trong $n.$

+ Dùng quy tắc nhân ta được số các số tự nhiên cần lập.

b. Lập số không chứa số $x$ nào đó: Ta thực hiện như sau:

Cách 1:

+ Gọi số cần lập theo dạng $n = \overline {abc \ldots }$ hoặc $n =$ ▯▯▯….

+ Chọn $a$, $b$, $c$ … (không được chọn số $x$).

Cách 2: Dùng phép đếm gián tiếp:

+ Lập các số dạng tổng quát.

+ Lập các số chứa số $x.$

+ Lấy tổng trừ các số chứa số $x$ suy ra số các số không chứa số $x.$

c. Lưu ý

+ Cũng giống các bài toán đã xét ta có thể sử dụng hai phương pháp đếm.

+ Nếu chữ số $x$ xuất hiện $k$ lần trong $n$ thì có thể sử dụng hoán vị hoặc chỉnh hợp lặp. Hay tìm số cách chọn $k$ vị trí cho $k$ chữ số $x$ (theo công thức số tổ hợp: Vì $k$ chữ số này giống nhau nên không phân biệt vị trí sắp xếp). Sau đó xếp các chữ số còn lại trong $n.$

+ Trong các trường hợp lập số $n$ có chứa nhiều chữ số $x$, $y$, $z$ … thì ta cũng thực hiện tương tự các bước đối với từng chữ số $x$, $y$, $z$ ….

2. BÀI TOÁN ÁP DỤNG

## Bài 1: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7.$ Có thể lập được bao nhiêu số tự nhiên có $5$ chữ số khác nhau và:

a) Bắt đầu bằng chữ số $3.$

b) Chữ số hàng chục bằng $4.$

c) Không bắt đầu bởi số $12.$

d) Luôn có mặt chữ số $5.$

Lời giải:

a) Gọi $n = \overline {abcd}$ là số tự nhiên thỏa yêu cầu bài toán.

Do $n$ bắt đầu bằng chữ số $3$ nên ta có:

Có $1$ cách chọn $a.$

Có $7$ cách chọn $b.$

Có $6$ cách chọn $c.$

Có $5$ cách chọn $d.$

Vậy có $1.7.6.5 = 210$ số.

b) Gọi số tự nhiên cần tìm có dạng: $n = \overline {ab4d} .$

Có $6$ cách chọn $a.$

Có $6$ cách chọn $b.$

Có $5$ cách chọn $d.$

Vậy có: $6.6.5 = 180$ số.

c) Gọi $n = \overline {abcd}$ là số tự nhiên thỏa yêu cầu bài toán.

Cách 1: (Dùng phương pháp đếm trực tiếp)

+ Nếu $a \ne 1$, khi đó $b$, $c$, $d$ chọn tùy ý.

Có $6$ cách chọn $a.$

Có $A_7^3 = 210$ cách chọn $b$, $c$, $d.$

Suy ra trường hợp này có: $6.210 = 1260$ số.

+ Nếu $a=1$, khi đó $b \ne \{ 1;2\}$ và $c$, $d$ chọn tùy ý.

Có $6$ cách chọn $b.$

Có $A_6^2 = 30$ cách chọn $c$, $d.$

Suy ra trường hợp này có: $6.30 = 180$ số.

Vậy tất cả có: $1260 + 180 = 1440$ số tự nhiên có $4$ chữ số khác nhau và không bắt đầu bằng số $12.$

Cách 2: (Dùng phương pháp đếm gián tiếp)

+ Đầu tiên ta tính số các số tự nhiên có $4$ chữ số khác nhau $n = \overline {abcd} .$

Có $7$ cách chọn $a.$

Có $A_7^3 = 210$ cách chọn $b$, $c$, $d.$

Vậy có $7.210 = 1470$ số tự nhiên có $4$ chữ số khác nhau.

+ Tiếp theo tính các số tự nhiên bắt đầu bởi $12$ có dạng: $n = \overline {12cd} .$

Có $A_6^2 = 30$ số.

Suy ra số các số tự nhiên có $4$ chữ số khác nhau và không bắt đầu bởi $12$ là:

$1470 – 30 = 1440$ số.

d) Cách 1:

Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm:

+ Nếu $a = 5$, khi đó có: $A_7^3 = 210$ cách chọn $b$, $c$, $d.$ Tức là có $210$ số.

+ Nếu $a \ne 5$, khi đó:

Có $3$ cách xếp chữ số $5$ trong $n$ (ở các vị trí $b$, $c$ hoặc $d$).

Có $6$ cách chọn $a.$

Có $A_6^2 = 30$ cách chọn $2$ chữ số còn lại trong $n.$

Suy ra có: $3.6.30 = 540$ số.

Vậy tất cả có: $210 + 540 = 750$ số.

Cách 2:

Gọi $n = \overline {abcd}$ là số tự nhiên có $4$ chữ số khác nhau và không có mặt chữ số $5.$

Có $6$ cách chọn $a.$

Có $A_6^3 = 120$ cách chọn $b$, $c$, $d.$

Suy ra có: $6.120 = 720$ số có $4$ chữ số khác nhau và không có mặt chữ số $5.$

Mà có tất cả $1470$ số tự nhiên có $4$ chữ số khác nhau (theo câu c).

Vậy có: $1470 – 720 = 750$ số tự nhiên có $4$ chữ số khác nhau và luôn có mặt chữ số $5.$

## Bài 2: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$ có thể lập được bao nhiêu số tự nhiên, mỗi số gồm $5$ chữ số khác nhau và nhất thiết phải có $2$ chữ số $1$, $5.$

Lời giải:

Gọi $n = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}}$ là số cần lập.

Bước 1: Xếp $1$, $5$ vào $2$ trong $5$ vị trí trong $n:$ có $A_5^2 = 20$ cách.

Bước 2: có $A_5^3 = 60$ cách xếp $3$ trong $5$ số còn lại vào $3$ vị trí còn lại của $n.$

Vậy có $20.60 = 1200$ số.

## Bài 3: Có bao nhiêu số tự nhiên gồm $5$ chữ số, trong đó chữ số $0$ có mặt đúng $2$ lần, chữ số $1$ có mặt đúng $1$ lần và hai chữ số còn lại phân biệt?

Lời giải:

Gọi số cần tìm là: $\overline {abcde}$ và mỗi chữ số tương ứng với $1$ ô trống: ▯▯▯▯▯.

Chọn $2$ ô xếp cho $2$ số $0$ có: $C_4^2$ cách chọn (trừ ô đầu tiên).

Chọn $1$ ô để xếp chữ số $1$ có $3$ cách chọn.

Chọn $2$ ô còn lại chọn từ các chữ số $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ có $A_8^2$ cách chọn.

Vậy có: $C_4^2.3.A_8^2 = 1008$ số.

## Bài 4:

## Bài tập 1. Có bao nhiêu số tự nhiên gồm $6$ chữ số đôi một khác nhau, trong đó có mặt chữ số $0$ nhưng không có mặt chữ số $1.$

## Bài tập 2. Có bao nhiêu số tự nhiên gồm $7$ chữ số, biết rằng chữ số $2$ có mặt đúng $2$ lần, chữ số $3$ có mặt đúng $3$ lần và các chữ số còn lại có mặt không quá một lần.

Lời giải:

## Bài tập 1. Số được xét có dạng: $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}} .$

Xếp chữ số $0$ vào các vị trí từ ${a_2}$ đến ${a_6}:$ có $5$ cách xếp. Còn lại $5$ vị trí, ta chọn $5$ trong $8$ chữ số để xếp vào $5$ vị trí này: có $A_8^5$ cách.

Vậy tất cả có: $5.A_8^5 = 33600$ cách.

## Bài tập 2. Số được xét có dạng: $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}{a_7}} .$

Chọn $2$ vị trí để xếp hai chữ số $2:$ có $C_7^2$ cách.

Chọn $3$ vị trí để xếp ba chữ số $3:$ có $C_5^3$ cách.

Còn $2$ vị trí, chọn $2$ chữ số tuỳ ý để xếp vào $2$ vị trí này: có $2!C_8^2$ cách.

Như vậy nếu xét cả các số bắt đầu bằng chữ số $0$ thì có: $C_7^2.C_5^3.2!C_8^2 = 11760$ số.

Trong các số này, cần loại bỏ các số bắt đầu bởi chữ số $0.$

Đối với các số $\overline {0{a_2}{a_3}{a_4}{a_5}{a_6}{a_7}} :$

Chọn $2$ vị trí để xếp chữ số $2:$ có $C_6^2$ cách.

Chọn $3$ vị trí để xếp ba chữ số $3:$ có $C_4^3$ cách.

Chọn $1$ số để xếp vào vị trí còn lại: có $7$ cách.

Như vậy loại này có: $C_6^2.C_4^3.7 = 420$ số.

Vậy tất cả có: $11760 – 420 = 11340$ số.

## Bài 5: Với các chữ số $1$, $2$, $3$, $4$, $5$, $6$ ta lập các số mà mỗi số có năm chữ số trong đó các chữ số khác nhau từng đôi một. Hỏi:

## Bài tập 1. Có bao nhiêu số trong đó phải có mặt chữ số $2.$

## Bài tập 2. Có bao nhiêu số trong đó phải có mặt hai chữ số $1$ và $6.$

Lời giải:

1) Gọi $n = \overline {abcde}$ là số thỏa mãn yêu cầu bài toán.

Có $5$ cách xếp chữ số $2$ trong các chữ số của $n$, mỗi cách xếp chữ số $2$ có $A_5^4$ cách xếp $4$ chữ số còn lại của $n.$

Vậy có $2.A_5^4 = 240$ số $n.$

2) Gọi $n = \overline {abcde}$ là số thỏa mãn yêu cầu bài toán.

Có $A_5^2$ cách xếp hai chữ số $1$ và $6$ trong các chữ số của $n$, mỗi cách xếp như vậy có $A_4^3$ cách xếp $3$ chữ số còn lại của $n.$

Vậy có: $A_5^2.A_4^3 = 480$ số $n.$

## Bài 6: Có thể lập được bao nhiêu số gồm $8$ chữ số từ các chữ số: $1$, $2$, $3$, $4$, $5$, $6$ trong đó các chữ số $1$ và $6$ đều có mặt $2$ lần, các chữ số khác có mặt $1$ lần.

Lời giải:

Gọi số tự nhiên cần tìm có dạng: $n =$ ▯▯▯▯▯▯▯▯.

Có $8$ ô trống, cần chọn ra $1$ ô điền chữ số $2$, $1$ ô điền chữ số $3$, $1$ ô điền chữ số $4$, $1$ ô điền chữ số $5.$ Sau đó trong $4$ ô còn lại, cần chọn $2$ ô điền chữ số $1$, cuối cùng còn lại $2$ ô điền chữ số $6.$

Chọn $1$ ô điền chữ số $2$ có $8$ cách chọn.

Chọn $1$ ô điền chữ số $3$ có $7$ cách chọn.

Chọn $1$ ô điền chữ số $4$ có $6$ cách chọn.

Chọn $1$ ô điền chữ số $5$ có $5$ cách chọn.

Chọn $2$ ô điền chữ số $1$ có $C_4^2$ cách chọn.

Chọn $2$ ô điền chữ số $6$ có $1$ cách chọn.

Vậy có tất cả có: $8.7.6.5 \cdot C_4^2.1 = 10080$ số thoả yêu cầu đề bài.

## Bài 7: Với các số: $0$, $1$, $2$, $3$, $4$, $5$ có thể thành lập được bao nhiêu số tự nhiên gồm $4$ chữ số khác nhau và trong đó phải có mặt chữ số $0.$

Lời giải:

Số các số tự nhiên gồm $4$ chữ số khác nhau được lập từ $6$ chữ số: $0$, $1$, $2$, $3$, $4$, $5$ là: $5.A_5^3 = 300.$

Trong các số nói trên, số các số tự nhiên không có mặt chữ số $0$ là: $A_5^3 = 120.$

Vậy số các số tự nhiên thoả mãn yêu cầu là: $300 – 120 = 180$ số.

## Bài 8: Cho $8$ chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7.$ Hỏi có thể lập được bao nhiêu số gồm $6$ chữ số khác nhau, trong đó nhất thiết phải có mặt chữ số $4.$

Lời giải:

Cách 1:

Giả sử số cần tìm có dạng: $A = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}} .$

+ Nếu ${a_1} = 4$ thì các chữ số còn lại của $A$ là một trong $7$ chữ số $0$, $1$, $2$, $3$, $5$, $6$, $7.$

Vậy có $A_7^5 = 2520$ số.

+ Nếu ${a_1} \ne 4$ thì vì ${a_1} \ne 0$ nên chỉ có $6$ cách chọn ${a_1}.$

Vì số $4$ phải có đúng một trong $5$ vị trí còn lại là ${a_2}$, ${a_3}$, ${a_4}$, ${a_5}$, ${a_6}.$

Khi đó các vị trí khác (không có chữ số $4$) sẽ chỉ còn $A_6^4$ số khác nhau.

Vậy trường hợp này có $6.5.A_6^4 = 10800$ số.

Vậy tất cả có: $2520 + 10800 = 13320$ số.

Cách 2:

+ Gọi $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}}$ là một số tự nhiên gồm $6$ chữ số khác nhau.

Có $7$ cách chọn ${a_1}.$

Các chữ số còn lại có $A_7^5$ cách chọn.

Vậy có $7.A_7^5 = 17640$ số.

Gọi $\overline {abcdef}$ là số tự nhiên có $6$ chữ số khác nhau và không có mặt chữ số $4.$

Có $6$ cách chọn $a.$

Các chữ số còn lại có $A_6^5$ cách chọn.

Suy ra có: $6.A_6^5 = 4320$ số không có mặt chữ số $4.$

Vậy có: $17640 – 4320 = 13320$ số gồm $6$ chữ số khác nhau và nhất thiết có mặt chữ số $4.$

## Bài 9: Với các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$ có thể lập được bao nhiêu số tự nhiên mà mỗi số có $5$ chữ số khác nhau và trong đó phải có chữ số $5.$

Lời giải:

Gọi $n = \overline {abcde}$ là số tự nhiên có $5$ chữ số khác nhau và có mặt chữ số $5.$ Xét các trường hợp sau:

+ Nếu $a=5$, khi đó $b$, $c$, $d$, $e$ chọn tùy ý trong các số $0$, $1$, $2$, $3$, $4$, $6.$

Số cách chọn $b$, $c$, $d$, $e$ là: $A_6^4.$

+ Nếu $a \ne 5$ khi đó có $5$ cách chọn $a$ từ các số $1$, $2$, $3$, $4$, $6.$

Sau đó xếp chữ số $5$ có $4$ cách chọn vị trí trong các chữ số của $n.$

$3$ chữ số còn lại trong $n$ có: $4$ cách chọn.

Suy ra có: $5.4.A_5^3 = 1200$ số.

Vậy có tất cả $A_6^4 + 1200 = 1560$ số tự nhiên có $5$ chữ số khác nhau và trong đó có mặt chữ số $5.$

## Bài 10:

## Bài tập 1. Có bao nhiêu số tự nhiên gồm $6$ chữ số đôi một khác nhau, trong đó có mặt chữ số $0$ nhưng không có mặt chữ số $1.$

## Bài tập 2. Có bao nhiêu số tự nhiên gồm $7$ chữ số, biết rằng chữ số $2$ có mặt đúng $2$ lần, chữ số $3$ có mặt đúng $3$ lần và các chữ số còn lại có mặt không quá một lần.

Lời giải:

## Bài tập 1. Số được xét có dạng: $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}} .$

Xếp chữ số $0$ vào các vị trí từ ${a_2}$ đến ${a_6}:$ có $5$ cách xếp.

Còn lại $5$ vị trí, ta chọn $5$ trong $8$ chữ số để xếp vào $5$ vị trí này: có $A_8^5$ cách.

Vậy tất cả có: $5.A_8^5 = 33600$ cách.

## Bài tập 2. Số được xét có dạng: $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}{a_7}} .$

Chọn $2$ vị trí để xếp hai chữ số $2:$ có $C_7^2$ cách.

Chọn $3$ vị trí để xếp ba chữ số $3:$ có $C_5^3$ cách.

Còn $2$ vị trí, chọn $2$ chữ số tuỳ ý để xếp vào $2$ vị trí này: có $2!C_8^2$ cách.

Như vậy nếu xét cả các số bắt đầu bằng chữ số $0$ thì có: $C_7^2.C_5^3.2!C_8^2 = 11760$ số.

Trong các số này, cần loại bỏ các số bắt đầu bởi chữ số $0.$

Đối với các số $\overline {0{a_2}{a_3}{a_4}{a_5}{a_6}{a_7}} :$

Chọn $2$ vị trí để xếp chữ số $2:$ có $C_6^2$ cách.

Chọn $3$ vị trí để xếp ba chữ số $3:$ có $C_4^3$ cách.

Chọn $1$ số để xếp vào vị trí còn lại: có $7$ cách.

Như vậy loại này có: $C_6^2.C_4^3.7 = 420$ số.

Vậy tất cả có: $11760 – 420 = 11340$ số.

## Bài 11: Có bao nhiêu số tự nhiên gồm $4$ chữ số sao cho không có chữ số nào lặp lại đúng $3$ lần?

Lời giải:

Số các số tự nhiên có $4$ chữ số là: $9.10.10.10 = 9000$ số.

Ta tìm số các số tự nhiên có $1$ chữ số lặp lại đúng $3$ lần:

+ Số $0$ lặp lại đúng $3$ lần ứng với số tự nhiên $\overline {a000}$ với $a \in \{ 1,2,3, \ldots ,9\}$ $\Rightarrow$ có $9$ số.

+ Số $1$ lặp lại đúng $3$ lần ứng với các số:

$\overline {a111}$ với $a \in \{ 2,3,4, \ldots ,9\}$ $\Rightarrow$ có $8$ số.

$\overline {1b11}$ với $b \in \{ 0,2,3, \ldots ,9\}$ $\Rightarrow$ có $9$ số.

$\overline {11c1}$ với $c \in \{ 0,2,3, \ldots ,9\}$ $\Rightarrow$ có $9$ số.

$\overline {111d}$ với $d \in \{ 0,2,3, \ldots ,9\}$ $\Rightarrow$ có $9$ số.

Suy ra có $8+ 9 + 9 + 9 = 35$ số.

+ Tương tự với mỗi số từ $2$ đến $9$ ta cũng tìm được $35$ số tự nhiên sao cho mỗi chữ số trên lặp lại đúng $3$ lần.

Do đó số các số tự nhiên có một chữ số lặp lại đúng $3$ lần là:

$9 + 9.35 = 324$ số.

Vậy số các số tự nhiên gồm $4$ chữ số mà trong đó không có chữ số nào lặp lại đúng $3$ lần là: $9000 – 324 = 8076$ số.

## Bài 12: Hỏi từ $10$ chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ có thể lập được bao nhiêu số gồm $6$ chữ số khác nhau, sao cho trong các chữ số đó có mặt số $0$ và $1.$

Lời giải:

Gọi số tự nhiên cần tìm có các chữ số tương ứng các ô trống sau: ▯▯▯▯▯▯.

Xét các trường hợp sau:

+ Nếu ô trống thứ nhất bằng $1$, khi đó:

Có $5$ cách xếp chữ số $0$ vào $1$ trong $5$ ô trống còn lại.

Có $A_8^4 = 1680$ cách chọn $4$ chữ số khác $0$ và $1$ để xếp vào $4$ ô trống còn lại.

Suy ra trường hợp này có $5.1680 = 8400$ số.

+ Nếu ô trống thứ nhất khác $1$, khi đó:

Có $8$ cách chọn $1$ chữ số xếp vào ô trống thứ nhất.

Có $A_5^2 = 20$ cách chọn $2$ ô để xếp $2$ chữ số $0$ và $1.$

Có $A_7^3 = 210$ cách chọn $3$ chữ số xếp vào $3$ ô trống còn lại.

Suy ra loại này có: $8.20.210 = 33600$ số.

Vậy tất cả có: $8400 + 33600 = 42000$ số.

## Bài 13: Có bao nhiêu số tự nhiên có $4$ chữ số thỏa mãn điều kiện sau:

a) Bắt đầu bằng chữ số $1.$

b) Có đúng $2$ chữ số giống nhau.

Lời giải:

a) Gọi số tự nhiên cần tìm có dạng $n = \overline {1bcd} .$

Có $10$ cách chọn $b.$

Có $10$ cách chọn $c.$

Có $10$ cách chọn $d.$

Vậy có $10.10.10 = 1000$ số.

b) Gọi số tự nhiên cần tìm có dạng $n=$ ▯▯▯▯ (mỗi chữ số tương ứng $1$ ô trống).

Xét các trường hợp sau:

* Trong $n$ có $2$ chữ số giống nhau $a$ và khác chữ số $0.$

Có $9$ cách chọn $2$ chữ số $a$ giống nhau khác $0.$

+ Nếu ô trống đầu tiên là $a$ thì có $3$ cách đặt chữ số $a$ thứ hai trong $3$ ô trống còn lại.

Mỗi cách đặt đó có $A_9^2 = 72$ cách chọn hai chữ số khác $a$ xếp vào $2$ ô trống còn lại.

Suy ra có: $3.72 = 216$ cách.

+ Nếu ô trống đầu tiên khác $a$, khi đó:

Có $8$ cách chọn một chữ số để đặt vào ô trống đầu tiên (trừ $0$ và $a$).

Có $C_3^2 = 3$ cách chọn $2$ ô trống để đặt hai chữ số $a.$

Có $8$ cách chọn $1$ chữ số để xếp vào ô trống còn lại.

Suy ra có: $8.3.3 = 192$ cách.

Vậy trường hợp này có $9.(216 + 192)= 3672$ số.

* Trong $n$ có $2$ chữ số $0.$

Có $C_3^2 = 3$ cách chọn $3$ ô trống để xếp $2$ chữ số $0.$

Có $A_9^2 = 72$ cách chọn $2$ chữ số khác nhau xếp vào $2$ ô trống còn lại.

Vậy trường hợp này có $3.72 = 216$ số.

Vậy tất cả có: $3602 + 216 = 3888$ số.

## Bài 14: Có bao nhiêu số tự nhiên gồm $7$ chữ số sao cho:

a) Trong đó có $2$ chữ số $1$, $3$ chữ số $2$, các chữ số còn lại xuất hiện đúng $1$ lần.

b) Trong đó có $2$ chữ số $0$, $3$ chữ số $2$, các chữ số còn lại xuất hiện đúng $1$ lần.

Lời giải:

a) Gọi số tự nhiên cần tìm có các chữ số tương ứng với các ô trống, dạng:

$n =$ ▯▯▯▯▯▯▯.

Xét các trường hợp sau:

+ $n$ có chứa chữ số $0$, khi đó:

Có $6$ cách chọn ô trống để đặt chữ số $0$ (trừ ô đầu tiên).

Có $C_6^2 = 15$ cách chọn $2$ ô trống để xếp $2$ chữ số $1.$

Có $C_4^3 = 4$ cách chọn $3$ ô trống để xếp $3$ chữ số $2.$

Ô trống còn lại có $7$ cách chọn chữ số (trừ số $0$, $1$, $2$).

Suy ra trường hợp này có: $6.15.4.7 = 2520$ số.

+ $n$ không chứa chữ số $0$, khi đó:

Có $C_7^2 = 21$ cách chọn $2$ ô trống để xếp $2$ chữ số $1.$

Có $C_5^3 = 10$ cách chọn $3$ ô trống để xếp $3$ chữ số $2.$

Có $A_7^2 = 42$ cách chọn $2$ chữ số (trừ số $0$, $1$, $2$) để xếp vào $2$ ô trống còn lại trong $n.$

Suy ra trường hợp này có: $21.10.42 = 8820$ số.

Vậy tất cả có: $2520 + 8820 = 11340$ số thỏa mãn.

b) Gọi số tự nhiên cần tìm có các chữ số tương ứng với các ô trống, dạng:

$n =$ ▯▯▯▯▯▯▯.

Có $C_6^2 = 15$ cách chọn $2$ ô trống để xếp $2$ chữ số $0$ (trừ ô đầu tiên).

Có $C_5^3 = 10$ cách chọn $3$ ô trống để xếp $3$ chữ số $2.$

Có $A_8^2 = 56$ cách chọn $2$ chữ số (trừ chữ số $0$ và $2$) để xếp $2$ ô trống còn lại.

Vậy có $15.10.56 = 8400$ số thỏa mãn.

## Bài 15: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ có thể lập được bao nhiêu số có $6$ chữ số khác nhau sao cho trong đó phải có mặt chữ số $0$ và chữ số $1$?

Lời giải:

Gọi số tự nhiên có các chữ số tương ứng với các ô trống, dạng: ▯▯▯▯▯▯.

Có $5$ cách xếp chữ số $0$ (trừ ô đầu tiên).

Có $5$ cách xếp chữ số $1.$

Có $A_8^4 = 1680$ cách chọn $4$ chữ số (khác $0$ và $1$) để xếp vào $4$ ô trống còn lại.

Vậy có $5.5.1680 = 42000$ số tự nhiên thỏa mãn.

## Bài 16: Từ các số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8.$ Tìm tất cả các số tự nhiên có bốn chữ số khác nhau sao cho:

a) Không tận cùng bằng $6.$

b) Chia hết cho $2.$

Lời giải:

a) Gọi $n = \overline {abcd}$ là số tự nhiên có bốn chữ số khác nhau.

Có $8$ cách chọn $a.$

Các chữ số còn lại trong $n$ có $A_8^3 = 336$ cách chọn.

Suy ra có: $8.336 = 2688$ số.

Trong các số tự nhiên trên ta xét các số tận cùng bằng $6$, nghĩa là số $n$ có dạng $n = \overline {abc6}$, khi đó:

Có $7$ cách chọn $a$, trừ $0$ và $6.$

Các chữ số $b$, $c$ có $A_7^2 = 42$ cách chọn.

Suy ra có: $7.42 = 294$ số tự nhiên có $4$ chữ số khác nhau và tận cùng bằng $6.$

Vậy có $2688 – 294 = 2394$ số tự nhiên có bốn chữ số khác nhau và không tận cùng bằng $6.$

b) Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm.

Vì $n$ chia hết cho $2$ nên $n$ tận cùng bằng số chẵn.

+ Nếu $d = 0$, khi đó: $a$, $b$, $c$ có $A_8^3 = 336$ cách chọn.

Suy ra trường hợp này có $336$ số.

+ Nếu $d \ne 0$, khi đó:

Có $4$ cách chọn $d.$

Có $7$ cách chọn $a.$

Có $A_7^2$ cách chọn $b$, $c.$

Suy ra trường hợp này có: $4.7.A_7^2 = 1176$ số.

Vậy tất cả có: $336 + 1176 = 1512$ số tự nhiên có $4$ chữ số khác nhau và chia hết cho $2.$

## Bài 17: Có bao nhiêu số tự nhiên gồm $7$ chữ số, chỉ tạo bởi các chữ số $1$, $2$, $3$ với điều kiện chữ số $2$ xuất hiện đúng $2$ lần trong số tự nhiên đó.

Lời giải:

Gọi số tự nhiên gồm $7$ chữ số và mỗi chữ số tương ứng với một ô trống:

$n =$ ▯▯▯▯▯▯▯.

Đầu tiên ta chọn $2$ ô trống để xếp $2$ chữ số $2$ thì có $C_7^2 = 21$ cách chọn.

Còn $5$ ô trống còn lại, mỗi ô trống có $2$ cách xếp $1$ hoặc $3$, suy ra có ${2^5} = 32$ cách xếp.

Vậy có $21.32 = 672$ số tự nhiên thỏa mãn.

## Bài 18: Với tập $E = \{ 1,2,3,4,5,6,7\}$ có thể lập được bao nhiêu số gồm $5$ chữ số phân biệt và:

a. Trong đó có chữ số $7.$

b. Trong đó có chữ số $7$ và chữ số hàng ngàn luôn là chữ số $1.$

Lời giải:

a) Gọi số cần tìm là $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}}$ $\left( {{a_1} \ne 0} \right).$

Giả sử ${a_1} = 7$ khi đó số cần tìm có dạng: $\overline {7{a_2}{a_3}{a_4}{a_5}} .$

Vì ${a_2}$, ${a_3}$, ${a_4}$, ${a_5}$ là $1$ bộ phận phân biệt thứ tự được chọn từ $E\backslash \{ 7\}$ nên có $A_6^4 = 360$ số.

Do số $7$ ở vị trí bất kỳ nên ta có thể đổi chỗ của các vị trí ${a_1}$, ${a_2}$, ${a_3}$, ${a_4}$, ${a_5}.$

Vậy có $5A_6^4 = 1800$ cách chọn hay có $1800$ số thoả mãn yêu cầu bài toán.

b) Gọi số cần tìm là $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}}$ $\left( {{a_1} \ne 0} \right).$

Do chữ số hàng nghìn bằng $1$ nên ${a_2} = 1.$

Chọn $1$ vị trí trong $4$ vị trí còn lại là chữ số $7$ nên có $4$ cách chọn.

Ba vị trí còn lại là bộ phận phân biệt thứ tự được chọn từ $E\backslash \{ 1,7\}$ nên có $A_5^3$ cách chọn.

Vậy: số các số gồm $5$ chữ số phân biệt hình thành từ tập $E$ trong đó có chữ số $7$ và chữ số hàng ngàn là chữ số $1$ là: $1.4.A_5^3 = 240$ số.

## Bài 19: Với $5$ chữ số $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số gồm $5$ chữ số đôi một khác nhau:

a. Không bắt đầu từ chữ số $1.$

b. Không bắt đầu từ $123.$

Lời giải:

Đặt $E = \{ 1,2,3,4,5\} .$

a.

* Gọi số tự nhiên gồm $5$ chữ số đôi một khác nhau là: $\overline {{a_1}{a_2}{a_3}{a_4}{a_5}}$ $\left( {{a_1} \ne 0} \right).$

${a_1}$ có $5$ cách chọn.

${a_2}$ có $4$ cách chọn.

${a_3}$ có $3$ cách chọn.

${a_4}$ có $2$ cách chọn.

${a_5}$ có $1$ cách chọn.

Vậy có: $5.4.3.2.1 = 120$ số.

* Gọi số tự nhiên gồm $5$ chữ số đôi một khác nhau, bắt đầu bằng chữ số $1$ là: $\overline {1abcd}$ thì:

$a$ có $4$ cách chọn (vì $a \in E\backslash \{ 1\}$).

$b$ có $3$ cách chọn (vì $b \in E\backslash \{ 1,a\}$).

$c$ có $2$ cách chọn (vì $c \in E\backslash \{ 1,a,b\}$).

$d$ có $1$ cách chọn (vì $d \in E\backslash \{ 1,a,b,c\}$).

Suy ra có: $4.3.2.1$ số bắt đầu từ chữ số $1.$

Vậy: số các số tự nhiên gồm $5$ chữ số khác nhau, không bắt đầu bằng chữ số $1$ là: $120 – 24 = 96$ số.

b. Gọi số tự nhiên gồm $5$ chữ số bắt đầu bằng chữ số $123$ là: $\overline {123xy}$ gồm $5$ chữ số khác nhau.

$x$ có $2$ cách chọn (vì $x \in E\backslash \{ 1,2,3\}$).

$y$ có $1$ cách chọn (vì $y \in E\backslash \{ 1,2,3,x\}$).

Suy ra có $2.1 = 2$ số.

Vậy các số tự nhiên gồm $5$ chữ số khác nhau, không bắt đầu bằng chữ số $123$ gồm có $120 – 2 = 118$ số.

## Bài 20: Tính số các số tự nhiên có $4$ chữ số đôi một khác nhau được thành lập từ $0$, $1$, $2$, $3$, $4$, $5$ sao cho trong mỗi số đó đều có mặt ít nhất chữ số $1$ hoặc $2.$

Lời giải:

+ Loại 1: chữ số ${a_1}$ có thể là $0.$

Sắp $4$ trong $6$ chữ số vào $4$ vị trí có $A_6^4 = 360$ cách.

Sắp $4$ chữ số $0$, $3$, $4$, $5$ vào $4$ vị trí có $4! = 24$ cách.

Suy ra có $360 – 24 = 336$ số.

+ Loại 2: chữ số ${a_1}$ là $0$ (vị trí ${a_1}$ đã có chữ số $0$).

Sắp $3$ trong $5$ chữ số vào $3$ vị trí có $A_5^3 = 60$ cách. Sắp $3$ chữ số $3$, $4$, $5$ vào $3$ vị trí có $3! = 6$ cách. Suy ra có $60 – 6 = 54$ số.

Vậy có $336 – 54 = 282$ số.

Cách khác:

+ Loại 1: Số tự nhiên có $4$ chữ số tùy ý.

Bước 1: Chọn $1$ trong $5$ chữ số khác $0$ sắp vào ${a_1}$ có $5$ cách.

Bước 2: Chọn $3$ trong $5$ chữ số khác ${a_1}$ sắp vào $3$ vị trí còn lại có $A_5^3 = 60$ cách.

Suy ra có $5.60 = 300$ số.

+ Loại 2: Số tự nhiên có $4$ chữ số gồm $0$, $3$, $4$, $5$ (không có $1$ và $2$).

Bước 1: Chọn $1$ trong $3$ chữ số khác $0$ sắp vào ${a_1}$ có $3$ cách.

Bước 2: Sắp $3$ chữ số còn lại vào $3$ vị trí $3! = 6$ cách.

Suy ra có $3.6 = 18$ số.

Vậy có $300 – 18 = 282$ số.

## Bài 21: Tính số các số tự nhiên gồm $7$ chữ số được chọn từ $1$, $2$, $3$, $4$, $5$ sao cho chữ số $2$ có mặt đúng $2$ lần, chữ số $3$ có mặt đúng $3$ lần và các chữ số còn lại có mặt không quá $1$ lần.

Lời giải:

Xem số có $7$ chữ số như $7$ vị trí thẳng hàng.

+ Bước 1: chọn $2$ trong $7$ vị trí để sắp $2$ chữ số $2$ (không hoán vị) có $C_7^2 = 21$ cách.

+ Bước 2: chọn $3$ trong $5$ vị trí còn lại để sắp $3$ chữ số $3$ (không khoán vị) có $C_5^3 = 10$ cách.

+ Bước 3: chọn $2$ trong $3$ chữ số $1$, $4$, $5$ để sắp vào $2$ vị trí còn lại (có hoán vị) có $A_3^2 = 6$ cách.

Vậy có $21.10.6 = 1260$ số.

## Bài 22: Tính số các số tự nhiên gồm $5$ chữ số phân biệt và một trong $3$ chữ số đầu tiên là $1$ được thành lập từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7.$

Lời giải:

+ Loại 1: chữ số ${a_1}$ có thể là $0.$

Bước 1: chọn $1$ trong $3$ vị trí đầu để sắp chữ số $1$ có $3$ cách.

Bước 2: chọn $4$ trong $7$ chữ số (trừ chữ số $1$) để sắp vào các vị trí còn lại có $A_7^4 = 840$ cách. Suy ra có $3.840 = 2520$ số.

+ Loại 2: chữ số ${a_1}$ là $0.$

Bước 1: chọn $1$ trong $2$ vị trí thứ $2$ và $3$ để sắp chữ số $1$ có $2$ cách.

Bước 2: chọn $3$ trong $6$ chữ số (trừ $0$ và $1$) để sắp vào các vị trí còn lại có A_{6}^{3}=120 cách. Suy ra có $2.120 = 240$ số.

Vậy có $2520 – 240 = 2280$ số.

## Bài 23: Tính số tập hợp con của $X = \{ 0;1;2;3;4;5;6\}$ chứa $1$ mà không chứa $0.$

Lời giải:

+ Số tập hợp con không chứa phần tử nào của $X\backslash \{ 0;1\}$ là $C_5^0.$

+ Số tập hợp con chứa $1$ phần tử của $X\backslash \{ 0;1\}$ là $C_5^1.$

+ Số tập hợp con chứa $2$ phần tử của $X\backslash \{ 0;1\}$ là $C_5^2.$

+ Số tập hợp con chứa $3$ phần tử của $X\backslash \{ 0;1\}$ là $C_5^3.$

+ Số tập hợp con chứa $4$ phần tử của $X\backslash \{ 0;1\}$ là $C_5^4.$

+ Số tập hợp con chứa $5$ phần tử của $X\backslash \{ 0;1\}$ là $C_5^5.$

Suy ra số tập hợp con của $X\backslash \{ 0;1\}$ là $C_5^0 + C_5^1 + C_5^2 + C_5^3 + C_5^4 + C_5^5 = 32.$

Ta hợp các tập hợp con này với $\{ 1\}$ thì được $32$ tập hợp thỏa bài toán.

## Bài 24: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$ lập được bao nhiêu số tự nhiên gồm $5$ chữ số sao cho:

a) Các chữ số đều khác nhau.

b) Chữ số đầu tiên là $3.$

c) Các chữ số khác nhau và không tận cùng bằng chữ số $4.$

Lời giải:

a) Mỗi số có $5$ chữ số khác nhau được thành lập tương ứng với một chỉnh hợp chập $5$ của $7$ phần tử $\Rightarrow$ Có $A_7^5 = 2520$ số.

b) Gọi số cần thiết lập là $\overline {abcde} .$

Chữ số đầu tiên là $3$ $\Rightarrow a$ có $1$ cách chọn.

$b$, $c$, $d$, $e$ đều có $7$ cách chọn.

Suy ra có $1.7.7.7.7 = 2401$ số.

c) Gọi số cần thiết lập là $\overline {abcde} .$

Chữ số cuối cùng khác $4$ $\Rightarrow$ $e$ có $6$ cách chọn (trừ số 4).

$a$ có $6$ cách chọn.

$b$ có $5$ cách chọn.

$c$ có $4$ cách chọn.

$d$ có $3$ cách chọn.

Suy ra có $6.6.5.4.3 = 2160$ số.

## Bài 25: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$ lập được bao nhiêu số có $4$ chữ số sao cho số tạo thành gồm các chữ số khác nhau và nhất thiết có chữ số $5.$

Lời giải:

Cách 1: Thành lập số có $3$ chữ số khác nhau và không có mặt chữ số $5.$

Suy ra có $A_6^3 = 120$ số.

Với mỗi số vừa thành lập có $4$ vị trí để xen số $5$ tạo thành số có $4$ chữ số khác nhau và có mặt chữ số $5.$

Suy ra có $120.4 = 480$ số.

Cách 2:

Số cần tìm có $1$ trong bốn dạng $\overline {5bcd}$, $\overline {a5bc}$, $\overline {ab5d}$, $\overline {abc5} .$

Mỗi dạng có $120$, suy ra có $480$ số.

## Bài 26: Với $5$ chữ số $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số gồm $8$ chữ số, trong đó chữ số $1$ có mặt đúng $3$ lần, chữ số $2$ có mặt đúng $2$ lần và mỗi chữ số còn lại có mặt đúng một lần?

Lời giải:

Gọi số tự nhiên cần tìm có các chữ số tương ứng các ô trống: ▯▯▯▯▯▯▯▯.

Có $C_8^3$ cách chọn $3$ ô trống để xếp $3$ chữ số $1.$

Có $C_5^2$ cách chọn $2$ ô trống để xếp $2$ chữ số $2.$

Có $3!$ cách xếp các chữ số $3$, $4$, $5$ vào $3$ ô trống còn lại.

Vậy có $C_8^3.C_5^2.3! = 3360$ số.

## Bài 27: Với các chữ số $0$, $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số gồm $8$ chữ số, trong đó chữ số $1$ có mặt $3$ lần, mỗi chữ số khác có mặt đúng $1$ lần.

Lời giải:

Gọi số tự nhiên cần tìm có các chữ số tương ứng các ô trống: ▯▯▯▯▯▯▯▯.

Có $7$ cách xếp chữ số $0$, trừ ô đầu tiên.

Có $C_7^3$ cách chọn $3$ ô trống để xếp $3$ chữ số $1.$

Có $4!$ cách xếp các chữ số $2$, $3$, $4$, $5$ vào $4$ ô trống còn lại.

Vậy có $7.C_7^3.4! = 5880$ số.

## Bài 28: Với $6$ chữ số $0$, $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số có $5$ chữ số khác nhau và thoả mãn:

a/ Số chẵn.

b/ Bắt đầu bằng số $24.$

c/ Bắt đầu bằng số $345.$

d/ Bắt đầu bằng số $1$? Từ đó suy ra các số không bắt đầu bằng số $1$?

Lời giải:

a) Gọi số tự nhiên cần tìm có dạng $n = \overline {abcde}$, xét các trường hợp sau:

+ Nếu $e = 0$, khi đó có $A_5^4 = 120$ cách chọn $4$ chữ số xếp vào $a$, $b$, $c$, $d.$

Suy ra trường hợp này có $120$ số.

+ Nếu $e \ne 0$, khi đó:

Có $2$ cách chọn $e.$

Có $4$ cách chọn $a.$

Có $A_4^3 = 24$ cách chọn $3$ chữ số xếp vào $b$, $c$, $d.$

Suy ra trường hợp này có $2.4.24 = 192$ số.

Vậy tất cả có $120 + 192 = 312$ số.

b) Gọi số cần tìm có dạng $n = \overline {24abc} .$

Có $A_4^3 = 24$ cách chọn $3$ chữ số xếp vào $a$, $b$, $c.$

Vậy có $24$ số.

c) Gọi số cần tìm có dạng $n = \overline {345ab} .$

Có $A_3^2 = 6$ cách chọn $2$ chữ số xếp vào $a$, $b$

Vậy có $6$ số.

d) Gọi số cần tìm có dạng $n = \overline {1abcd} .$

Có $A_5^4 = 120$ cách chọn $4$ chữ số xếp vào $a$, $b$, $c$, $d.$

Vậy có $120$ số có $5$ chữ số khác nhau và bắt đầu bằng $1.$

Gọi $\overline {abcde}$ là số tự nhiên có $5$ chữ số khác nhau.

Có $5$ cách chọn $a.$

Có $A_5^4 = 120$ cách chọn $4$ chữ số xếp vào $b$, $c$, $d$, $e.$

Suy ra có $5.120 = 720$ số.

Vậy có $720 – 120 = 600$ số tự nhiên có $6$ chữ số khác nhau và không bắt đầu bằng $1.$

## Bài 29: Cho tập $A = \{ 1;2;3;4;5;6\}$ có thể lập được bao nhiêu số tự nhiên:

a) Có $4$ chữ số.

b) Có $4$ chữ số khác nhau đôi một.

c) Có $4$ chữ số khác nhau và bắt đầu bằng chữ số $5.$

d) Có $4$ chữ số khác nhau và chia hết cho $5.$

Lời giải:

a) Có ${6^4} = 1296.$

b) Có $A_6^4 = 360$ số.

c) Có $A_5^3 = 60$ số.

d) Có $A_5^3 = 60$ số.

## Bài 30: Từ các chữ số $0$; $1$; $2$; $3$; $4$; $5$ có thể lập được bao nhiêu số tự nhiên có $4$ chữ số khác nhau sao cho:

a) Chữ số hàng trăm là $3.$

b) Luôn có mặt chữ số $1$ và chữ số hàng nghìn là $2.$

Lời giải:

a) Gọi chữ số tự nhiên cần tìm có dạng $n = \overline {abcd} .$

Theo đề ta có $b = 3$, do đó:

Có $4$ cách chọn $a.$

Có $A_4^2 = 12$ cách chọn $2$ chữ số xếp vào $c$, $d.$

Vậy có $4.12 = 48$ số.

b) Gọi chữ số tự nhiên cần tìm có dạng $n = \overline {abcd} .$

Theo đề ta có $a= 4$, do đó:

Có $3$ cách chọn vị trí để xếp chữ số $1.$

Có $A_4^2 = 12$ cách chọn $2$ chữ số xếp vào $2$ vị trí còn lại trong $n.$

Vậy có $3.12 = 36$ số.

## Bài 31: Có bao nhiêu số tự nhiên gồm bốn chữ số, sao cho không có chữ số nào lặp lại đúng $3$ lần.

Lời giải:

Bước 1: Tính các số tự nhiên có $4$ chữ số (các chữ số có thể giống nhau và không cần chú ý đến điều kiện lặp lại $3$ lần).

Gọi số tự nhiên đó là: $n = \overline {abcd}$, khi đó:

Có $9$ cách chọn $a.$

Có $10$ cách chọn $b.$

Có $10$ cách chọn $c.$

Có $10$ cách chọn $d.$

Vậy có $9.10.10.10 = 9000$ số.

Bước 2: Tính các số tự nhiên có $4$ chữ số và có chữ số lặp lại đúng $3$ lần.

+ Trường hợp 1: $a = b = c \ne d.$

Có $9$ cách chọn $a$, trừ số $0.$

Có $1$ cách chọn $b$, $c.$

Có $9$ cách chọn $d.$

Vậy ta có: $9.1.9 = 81$ số.

+ Trường hợp 2: $a = b = d \ne c.$

Có $9$ cách chọn $a$, trừ số $0.$

Có $1$ cách chọn $b$, $d.$

Có $9$ cách chọn $c.$

Vậy ta có: $9.1.9 = 81$ số.

+ Trường hợp 3: $a = c = d \ne b.$

Có $9$ cách chọn $a$, trừ số $0.$

Có $1$ cách chọn $c$, $d.$

Có $9$ cách chọn $b.$

Vậy ta có: $9.1.9 = 81$ số.

+ Trường hợp 4: $b = c = d \ne a.$

Có $9$ cách chọn $a$, trừ số $0.$

Có $9$ cách chọn $b.$

Có $1$ cách chọn $c$, $d.$

Vậy ta có: $9.1.9 = 81$ số.

Suy ra có tất cả $81 + 81 + 81 + 81 = 324$ số tự nhiên có $4$ chữ số và có chữ số lặp lại đúng $3$ lần.

Vậy có: $9000 – 324 = 8676$ số tự nhiên có $4$ chữ số mà không có chữ số nào lặp lại đúng $3$ lần.

## Bài 32: Từ tập hợp số $\{ 1;2;3;4;5\} .$ Có bao nhiêu cách chọn một số tự nhiên:

a) Có hai chữ số đôi một khác nhau?

b) $3$ chữ số đôi một khác nhau và luôn có mặt chữ số $5$?

c) Có $4$ chữ số đôi một khác nhau và luôn có mặt chữ số $2$?

Lời giải:

a) Có $A_5^2 = 20$ số.

b) Gọi $n = \overline {abc}$ là số tự nhiên cần tìm.

Có $3$ cách xếp chữ số $5$ trong $n.$

Có $A_4^2 = 12$ cách chọn $2$ chữ số xếp vào các vị trí còn lại trong $n.$

Vậy có $3.12 = 36$ số tự nhiên có $3$ chữ số khác nhau và luôn có mặt chữ số $5.$

c) Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm.

Có $4$ cách chọn vị trí để xếp chữ số $2$ trong $n.$

Có $A_4^3 = 24$ cách chọn $3$ chữ số xếp vào các vị trí còn lại trong $n.$

Vậy có $4.24 = 96$ số.

## Bài 33: Từ các số $0$, $2$, $4$, $5$, $6$, $8$, $9.$ Ta có thể lập được bao nhiêu số tự nhiên:

a) Có $3$ chữ số và đôi một khác nhau.

b) Có $4$ chữ số đôi một khác nhau và luôn có mặt số $5.$

Lời giải:

a) Gọi số tự nhiên cần lập có dạng $n = \overline {abc} .$

Có $6$ cách chọn $a.$

Có $6$ cách chọn $b.$

Có $5$ cách chọn $c.$

Vậy có $6.6.5 = 180$ số.

b) Gọi $n = \overline {abcd}$ là số tự nhiên có $4$ chữ số khác nhau, khi đó:

Có $6$ cách chọn $a.$

Có $A_6^3 = 120$ cách chọn $3$ chữ số xếp vào $b$, $c$, $d.$

Suy ra có $6.120 = 720$ số.

Xét các số tự nhiên dạng $n = \overline {abcd}$ có $4$ chữ số khác nhau mà không có mặt chữ số $5.$

Có $5$ cách chọn $a.$

Có $A_5^3 = 60$ cách chọn $3$ chữ số xếp vào $b$, $c$, $d.$

Suy ra có $5.60 = 300$ số.

Vậy có $720 – 300 = 420$ số tự nhiên có $4$ chữ số khác nhau và luôn có mặt chữ số $5.$

## Bài 34: Từ các số $0$, $1$, $2$, $3$, $4$, $5$, $6$ có bao nhiêu cách lập một số tự nhiên:

a) Số có $4$ chữ số đôi một khác nhau.

b) Số có $5$ chữ số.

c) Số có $3$ chữ số chia hết cho $5.$

d) Số có $4$ chữ số trong đó luôn có chữ số $1.$

Lời giải:

a) Gọi số tự nhiên cần lập có dạng: $n = \overline {abcd} .$

Có $6$ cách chọn $a.$

Có $A_6^3 = 120$ cách chọn $4$ chữ số xếp vào $a$, $b$, $c.$

Vậy có $6.120 = 720$ số.

b) Gọi số tự nhiên cần lập có dạng: $n = \overline {abcde} .$

Có $6$ cách chọn $a.$

Có ${7^4}$ cách chọn $4$ chữ số còn lại xếp vào $b$, $c$, $d$, $e.$

Vậy có 6.7^{4}=14406 số.

c) Gọi số tự nhiên cần lập có dạng: $n = \overline {abcd} .$

Có $2$ cách chọn $d.$

Có $7$ cách chọn $a.$

Có $7$ cách chọn $b.$

Có $7$ cách chọn $c.$

Vậy có $2.7.7.7 = 686$ số.

d) Gọi số tự nhiên cần lập có dạng: $n = \overline {abcd} .$

+ Nếu $a = 1$, khi đó:

Có $7$ cách chọn $b.$

Có $7$ cách chọn $c.$

Có $7$ cách chọn $d.$

Suy ra có $7.7.7 = 343$ số.

+ Nếu $a \ne 1$, khi đó:

Có $5$ cách chọn $a.$

Chữ số $1$ có $3$ cách chọn vị trí trong $n$

Có $7.7 = 49$ cách chọn $2$ chữ số còn lại.

Suy ra có $5.3.49 = 735$ số.

Vậy tất cả có $343 + 735 = 1078$ số.

## Bài 35: Từ các số: $0$, $1$, $2$, $3$, $4$, $5$, $6$ có bao nhiêu cách lập một số tự nhiên:

a) Có $2$ chữ số khác nhau và luôn có mặt chữ số $2.$

b) Có $3$ chữ số khác nhau và chia hết cho $3.$

Lời giải:

a) Gọi số tự nhiên có dạng $n = \overline {ab} .$

+ Nếu $a = 2$, thì có $6$ cách chọn $b$, tức là có $6$ số $n.$

+ Nếu $b = 2$, thì có $5$ cách chọn $a$, tức là có $5$ số $n.$

Vậy có $6 + 5 = 11$ số.

b) Gọi số tự nhiên có dạng $n = \overline {abc} .$

Do $n$ chia hết cho $3$ nên $a + b + c$ phải chia hết cho $3.$

Do đó $a$, $b$, $c$ thuộc một trong các bộ số sau: $\{ 0;1;2\}$, $\{ 0;1;5\}$, $\{ 0;2;4\}$, $\{ 0;3;6\}$, $\{ 0:4;5\}$, $\{ 1;2;3\}$, $\{ 1;2;6\}$, $\{ 1;3;5\}$, $\{ 1;5;6\}$, $\{ 2;3;4\}$, $\{ 3;4;5\}$, $\{ 4;5;6\} .$

+ Xét $5$ tập hợp có chứa chữ số $0$, mỗi tập hợp có thể lập được $2.2.1 = 4$ số tự nhiên có $3$ chữ số khác nhau.

Suy ra có $5.4 = 20$ số.

+ Xét $7$ tập hợp không chứa chữ số $0$, mỗi tập hợp có thể lập được $3! = 6$ số tự nhiên có $3$ chữ số khác nhau.

Suy ra có $7.6 = 42$ số.

Vậy tất cả có $20 + 42 = 62$ số tự nhiên có $3$ chữ số khác nhau và chia hết cho $3.$

## Bài 36: Có bao nhiêu số chẵn có $6$ chữ số đôi một khác nhau với số đầu tiên là chữ số lẻ?

Lời giải:

Gọi số tự nhiên cần lập có dạng: $n = \overline {abcdef} .$

Có $5$ cách chọn $a.$

Có $5$ cách chọn $f.$

Có $A_8^4 = 1680$ cách chọn các chữ số xếp cho $b$, $c$, $d$, $e.$

Vậy theo quy tắc nhân có: $5.5.1680 = 42000$ số thỏa mãn yêu cầu bài toán.