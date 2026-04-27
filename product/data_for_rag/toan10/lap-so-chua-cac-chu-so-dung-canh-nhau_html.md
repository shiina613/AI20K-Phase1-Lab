# Lập số chứa các chữ số đứng cạnh nhau

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/lap-so-chua-cac-chu-so-dung-canh-nhau.html -->
Bài viết hướng dẫn phương pháp giải bài toán lập số chứa các chữ số đứng cạnh nhau, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11.

1. PHƯƠNG PHÁP GIẢI TOÁN

+ Gọi số cần lập theo dạng $n = \overline {abc \ldots }$ hoặc $n =$ ▯▯▯… sao cho có số $x$ đứng cạnh số $y.$

+ Coi chữ số $x$, $y$ đứng cạnh nhau là một chữ số kép $T$ nào đó.

+ Tính số cách sắp xếp $T$ và các chữ số còn lại trong $n.$

+ Tính số cách xếp $x$, $y$ trong $T.$

+ Dùng quy tắc nhân suy ra số các số tự nhiên cần lập.

## Bài tập
## Bài 1: Người ta xếp ngẫu nhiên $5$ lá phiếu có ghi số thứ tự từ $1$ đến $5$ cạnh nhau.

## Bài tập 1. Có bao nhiêu cách xếp để các phiếu số chẵn luôn ở cạnh nhau?

## Bài tập 2. Có bao nhiêu cách xếp để các phiếu phân thành hai nhóm chẵn lẻ riêng biệt (chẳng hạn $2$, $4$, $1$, $3$, $5$)?

Lời giải:

## Bài tập 1. Xếp các phiếu số $1$, $2$, $3$, $5$ có $4! = 24$ cách.

Sau đó xếp phiếu số $4$ vào cạnh phiếu số $2$ có $2$ cách.

Vậy có $2.24 = 48$ cách xếp theo yêu cầu đề bài.

2. Khi nhóm chẵn ở bên trái, nhóm lẻ ở bên phải. Số cách xếp cho $2$ số chẵn là $2!$ cách. Số cách xếp cho $3$ số lẻ là: $3!$ cách.

Vậy có $2.6 = 12$ cách.

Tương tự cũng có $12$ cách xếp mà nhóm chẵn ở bên phải, nhóm lẻ ở bên trái.

Vậy có $12 + 12 = 24$ cách.

## Bài 2: Xét những số gồm $9$ chữ số, trong đó có năm chữ số $1$ và bốn chữ số còn là $2$, $3$, $4$, $5.$ Hỏi có bao nhiêu số như thế, nếu:

## Bài tập 1. Năm chữ số $1$ được xếp kề nhau.

## Bài tập 2. Các chữ số được xếp tuỳ ý.

Lời giải:

## Bài tập 1. Gọi $11111$ là số $a.$ Vậy ta cần sắp các số $a$, $2$, $3$, $4$, $5.$

Do đó số có $9$ chữ số trong đó có $5$ chữ số $1$ đứng liền nhau là: $5! = 120$ số.

## Bài tập 2. Lập một số có $9$ chữ số thoả mãn yêu cầu; thực chất là việc xếp các số $2$, $3$, $4$, $5$ vào $4$ vị trí tuỳ ý trong $9$ vị trí ($5$ vị trí còn lại đương nhiên dành cho chữ số $1$ lặp $5$ lần).

Vậy có tất cả $A_9^4 = \frac{{9!}}{{5!}} = 6.7.8.9 = 3024$ số.

## Bài 3: Tìm tất cả các số tự nhiên có đúng $5$ chữ số sao cho trong mỗi số đó chữ số đứng sau lớn hơn chữ số đứng liền trước.

Lời giải:

Theo yêu cầu của bài toán và số $0$ không đứng trước bất kì số nào nên các số có $5$ chữ số chỉ có thể tạo thành từ các số $\{ 1,2,3,4, \ldots ,8,9\} = T.$ Ứng với mỗi bộ $5$ chữ số phân biệt bất kì trong $T$ chỉ có $1$ cách sắp xếp duy nhất thoả mãn đứng sau lớn hơn chữ số liền trước.

Vậy số các số cần tìm là: $C_9^5 = 126$ số.

## Bài 4: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$ có thể thiết lập được bao nhiêu số có $6$ chữ số khác nhau mà hai chữ số $1$ và $6$ không đứng cạnh nhau?

Lời giải:

Số các số tự nhiên gồm $6$ chữ số khác nhau là: $6! = 720$ số.

Trong các số tự nhiên đó ta xét các số tự nhiên có $6$ chữ số khác nhau mà $1$ và $6$ đứng cạnh nhau.

Chữ số $1$ và $6$ đứng cạnh nhau có $6$ cách xếp là $16$ hoặc $61.$

Mỗi cách xếp đó ta coi số $16$ hoặc $61$ là một số, khi đó có $5!$ cách xếp các số $16$, $2$, $3$, $4$, $5.$

Suy ra có $2.5! = 240$ số có $6$ chữ số khác nhau mà $1$ và $6$ đứng cạnh nhau.

Vậy có $720 – 240 = 480$ số có $6$ chữ số khác nhau mà $1$ và $6$ không đứng cạnh nhau.

## Bài 5: Tính số các số tự nhiên đôi một khác nhau có $6$ chữ số tạo thành từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$ sao cho $2$ chữ số $3$ và $4$ đứng cạnh nhau.

Lời giải:

Xét số có $5$ chữ số gồm $0$, $1$, $2$, $5$ và chữ số “kép” là $(3,4).$

Loại 1: chữ số hàng trăm ngàn có thể là $0.$

+ Bước 1: sắp $5$ chữ số vào $5$ vị trí có $5! = 120$ cách.

+ Bước 2: với mỗi cách sắp chữ số kép có $2$ hoán vị chữ số $3$ và $4.$

Suy ra có $120.2 = 240$ số.

Loại 2: chữ số hàng trăm ngàn là $0.$

+ Bước 1: sắp $4$ chữ số vào $4$ vị trí còn lại có $4! = 24$ cách.

+ Bước 2: với mỗi cách sắp chữ số kép có $2$ hoán vị chữ số $3$ và $4.$

Suy ra có $24.2 = 48$ số.

Vậy có $240 – 48 = 192$ số.

## Bài 6: Có bao nhiêu số tự nhiên có $6$ chữ số với:

a) Chữ số đầu và chữ số cuối giống nhau?

b) Chữ số đầu và cuối khác nhau?

c) Hai chữ số đầu giống nhau và hai chữ số cuối giống nhau?

Lời giải:

a) Gọi số tự nhiên cần tìm có dạng $n = \overline {abcdea} .$

Có $9$ cách chọn $a.$

Có $10$ cách chọn $b.$

Có $10$ cách chọn $c.$

Có $10$ cách chọn $d.$

Có $10$ cách chọn $e.$

Vậy có $9.10.10.10.10 = 90000$ số.

b) Gọi số tự nhiên cần tìm có dạng $n = \overline {abcdef} .$

Có $9$ cách chọn $a.$

Có $10$ cách chọn $b.$

Có $10$ cách chọn $c.$

Có $10$ cách chọn $d.$

Có $10$ cách chọn $e.$

Có $9$ cách chọn $f$ (do $f$ khác $a$).

Vậy có $9.10.10.10.10.9 = 810000$ số.

c) Gọi số tự nhiên cần tìm có dạng $n = \overline {aabcdd} .$

Có $9$ cách chọn $a.$

Có $10$ cách chọn $b.$

Có $10$ cách chọn $c.$

Có $10$ cách chọn $d.$

Vậy có $9.10.10.10 = 9000$ số.

## Bài 7: Xét số tự nhiên gồm $8$ chữ số. Trong đó có bốn chữ số $2$ và bốn chữ số còn lại là $3$, $4$, $5$, $6.$ Hỏi có bao nhiêu số tự nhiên như thế nếu:

a) Các chữ số $2$ được xếp kề nhau.

b) Các chữ số được xếp tùy ý?

Lời giải:

a) Gọi số tự nhiên cần tìm có các chữ số tương ứng các ô trống ▯▯▯▯▯▯▯▯.

Giả sử bốn chữ số $2$ khi xếp kề nhau là một khối thống nhất $A.$

Do đó số các số tự nhiên thỏa mãn yêu cầu bài toán là số cách xếp $A$, $3$, $4$, $5$, $6$ để được một số tự nhiên có $8$ chữ số.

Vậy có $5! = 120$ số.

b) Do các chữ số được xếp tùy ý nên mỗi số tự nhiên tạo thành là một cách chọn $4$ ô trống để xếp $4$ chữ số $3$, $4$, $5$, $6$ và $4$ ô trống còn lại chỉ có $1$ cách xếp $4$ chữ số $2.$

Vậy có $A_8^4 = 1680$ số.

## Bài 8: Xét những số gồm $8$ chữ số, trong đó có $4$ chữ số $2$ và $4$ chữ số còn lại là $3$, $4$, $5$, $6.$ Hỏi có bao nhiêu số như thế nếu:

a) $4$ chữ số $2$ được xếp kề nhau?

b) Các chữ số được xếp tùy ý?

Lời giải:

a) $4$ chữ số $2$ được xếp kề nhau có thể coi là một khối thống nhất $A.$

Suy ra số các số tự nhiên trên là số cách xếp $A$ và $3$, $4$, $5$, $6.$

Vậy có $5! = 120$ số.

b) Số các số tự nhiên thỏa mãn yêu cầu bài toán là số cách chọn $4$ vị trí để xếp các chữ số $3$, $4$, $5$, $6$, còn các vị trí còn lại có $1$ cách xếp $4$ chữ số $2.$

Vậy có $A_8^4 = 1680$ số.

## Bài 9: Có bao nhiêu số tự nhiên có $5$ chữ số sao cho:

a) Các chữ số đứng sau luôn lớn hơn chữ số đứng liền trước?

b) Các chữ số sau luôn nhỏ hơn chữ số đứng liền trước?

Lời giải:

Rõ ràng số tự nhiên cần tìm có $5$ chữ số khác nhau.

a) Vì các chữ số đứng liền sau luôn lớn hơn chữ số đứng liền trước nên trong số tự nhiên đó không chứa chữ số $0.$

Mỗi cách chọn ra $5$ chữ số từ các số $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ chỉ có $1$ cách sắp xếp để các chữ số đứng sau luôn lớn hơn chữ số đứng liền trước.

Vậy số các số tự nhiên thỏa mãn là: $C_9^5 = 126$ số.

b) Mỗi cách chọn ra $5$ chữ số từ các số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$ chỉ có $1$ cách sắp xếp để các chữ số sau luôn nhỏ hơn chữ số đứng liền trước.

Vậy số các số tự nhiên thỏa mãn là: $C_{10}^5 = 252$ số.