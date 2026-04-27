# Lập số chia hết cho một số nào đó

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/lap-so-chia-het-cho-mot-so-nao-do.html -->
Bài viết hướng dẫn phương pháp giải bài toán lập số chia hết cho một số nào đó, đây là dạng toán thường gặp trong chương trình Đại số và Giải tích 11: Tổ hợp và xác suất.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/lap-so-chia-het-cho-mot-so-nao-do.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
1. Phương pháp chung

+ Gọi số cần lập theo dạng $n = \overline {abc \ldots } .$

+ Từ dữ liệu của bài toán tìm số các chọn $a$, $b$, $c$ … phù hợp.

+ Sử dụng các công cụ (hoán vị, chỉnh hợp, tổ hợp) kết hợp với hai quy tắc đếm suy ra số các số tự nhiên cần lập.

2. Bổ sung một số dấu hiệu chia hết
 Dấu hiệu chia hết cho $2$: Các số $x$ có tận cùng là $0$, $2$, $4$, $6$, $8$ thì chia hết cho $2.$

Dấu hiệu chia hết cho $3$: Các số $x$ có tổng các chữ số chia hết cho $3$ thì chia hết cho $3.$

Dấu hiệu chia hết cho $4$: Các số $x$ có hai chữ số tận cùng chia hết cho $4$ thì chia hết cho $4.$

Dấu hiệu chia hết cho $5$: Các số $x$ có tận cùng bằng $0$, $5$ thì chia hết cho $5.$

Dấu hiệu chia hết cho $6$: Các chữ số vừa có thể chia hết cho $2$ vừa có thể chia hết cho $3$ thì chia hết cho $6.$

Dấu hiệu chia hết cho $7$:

Quy tắc thứ nhất: Lấy chữ số đầu tiên bên trái nhân với $3$ rồi cộng với chữ số thứ hai rồi trừ cho bội của $7$; được bao nhiêu nhân với $3$ cộng với chữ số thứ ba rồi trừ cho bội của $7$; được bao nhiêu nhân với $3$ cộng với chữ số thứ tư rồi trừ cho bội của $7$ … Nếu kết quả cuối cùng là một số chia hết cho $7$ thì số đã cho chia hết cho $7.$

Quy tắc thứ hai: Lấy chữ số đầu tiên bên phải nhân với $5$ rồi cộng với chữ số thứ hai rồi trừ cho bội của $7$; được bao nhiêu nhân với $5$ cộng với chữ số thứ ba rồi trừ cho bội của $7$; được bao nhiêu nhân với $5$ cộng với chữ số thứ tư rồi trừ cho bội của $7$ … Nếu kết quả cuối cùng là một số chia hết cho $7$ thì số đã cho chia hết cho $7.$

Dấu hiệu chia hết cho $8$: các số $x$ có ba chữ số tận cùng chia hết cho $8$ thì $x$ chia hết cho $8.$

Dấu hiệu chia hết cho $9$: Trong các số $x$ có tổng các chữ số chia hết cho $9$ thì $x$ chia hết cho $9.$

Dấu hiệu chia hết cho $10$: những số $x$ có tận cùng bằng $0$ thì chia hết cho $10.$

<!-- chunk:2 level:1 source:https://toanmath.com/2019/12/lap-so-chia-het-cho-mot-so-nao-do.html -->
## B. BÀI TẬP VẬN DỤNG

## Bài 1: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5.$ Có thể lập được bao nhiêu số tự nhiên gồm $5$ chữ số khác nhau và chia hết cho $3$?

Lời giải:

Gọi $n = \overline {abcde}$ là số tự nhiên cần tìm.

Vì $n$ chia hết cho $3$ nên $a + b + c + d + e$ chia hết cho $3.$

Do đó $a$, $b$, $c$, $d$, $e$ thuộc các tập số sau: $\{ 0;1;2;4;5\}$, $\{ 1;2;3;4;5\} .$

+ Với tập số $\{ 0;1;2;4;5\}$ thì:

Có $4$ cách chọn $a.$

Có $4!$ cách chọn $b$, $c$, $d$, $e.$

Suy ra trường hợp này có $4.4! = 96$ số.

Với tập số $\{ 1;2;3;4;5\}$ thì có $5! = 120$ số.

Vậy tất cả có $96 + 120 = 216$ số.

## Bài 2: Từ các số $0$, $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số tự nhiên gồm $4$ chữ số đôi một khác nhau và số đó chia hết cho $5.$

Lời giải:

Gọi $n = \overline {abcd}$ là số tự nhiên cần tìm.

Vì $n$ chia hết cho $5$ nên $d$ có thể là $0$ hoặc $5.$

+ Nếu $d = 0$, khi đó có $A_5^3 = 60$ số.

+ Nếu $d=5$, khi đó:

Có $4$ cách chọn $a.$

Có $A_4^2 = 12$ cách chọn $b$, $c.$

Suy ra có: $4.12 = 48$ số.

Vậy tất cả có $60 + 48 = 108$ số.

## Bài 3: Cho tập $X = \{ 0,1,2,3,4,5,6,7\} .$ Có thể lập được bao nhiêu số $n$ gồm $5$ chữ số khác nhau đôi một từ $X$ (chữ số đầu tiên phải khác $0$) trong mỗi trường hợp sau:

## Bài tập 1. $n$ là số chẵn.

## Bài tập 2. Một trong ba chữ số đầu tiên phải bằng $1.$

Lời giải:

## Bài tập 1. Xem các số chẵn hình thức $\overline {abcde}$ (kể cả $a = 0$), có $4$ cách chọn $e \in \{ 0,2,4,6\}$, vì là số chẵn.

Sau đó chọn $a$, $b$, $c$, $d$ từ $X\backslash \{ e\}$, số cách chọn là $A_7^4 = 840.$

Vậy: có $4.840 = 3360$ số chẵn hình thức.

Ta loại những số có dạng $\overline {0bcde} .$ Có $3$ cách chọn $e$, và $A_6^3$ cách chọn $b$, $c$, $d$ từ $X\backslash \{ 0,e\} .$ Vậy có $3.{\rm{ }}A_6^3 = 360$ số chẵn có dạng $\overline {0bcde} .$

Kết luận: có $3360 – 360 = 3000$ số thoả yêu cầu đề bài.

## Bài tập 2. $n = \overline {abcde} .$

+ Xem các số hình thức $\overline {abcde}$ (kể cả $a= 0$). Có $3$ cách chọn vị trí cho $1.$ Sau đó chọn chữ số khác nhau cho $3$ vị trí còn lại từ $X\backslash \{ 1\}$: có $A_7^4$ cách.

Như thế: có $3.A_7^4 = 2520$ số hình thức thoả yêu cầu đề bài.

+ Xem các số hình thức $\overline {0bcde} .$ Có $2$ cách chọn vị trí cho $1.$ Chọn chữ số khác nhau cho $3$ vị trí còn lại từ $X\backslash \{ 0,1\}$, số cách chọn là $A_6^3.$

Như thế: có $2.A_6^3 = 240$ số hình thức dạng $\overline {0bcde} .$

Kết luận: số các số $n$ thoả yêu cầu đề bài là: $2520 – 240 = 2280$ số.

## Bài 4: Từ $5$ chữ số $0$, $1$, $3$, $5$, $7$ có thể lập được bao nhiêu số gồm $4$ chữ số khác nhau và không chia hết cho $5.$

Lời giải:

+ Trước hết ta tìm số các số gồm $4$ chữ số khác nhau:

Có $4$ khả năng chọn chữ số hàng ngàn (không chọn chữ số $0$).

Có $A_4^3$ khả năng chọn $3$ chữ số cuối.

Vậy có $4.A_4^3 = 4.4! = 96$ số.

+ Tìm số các số gồm $4$ chữ số khác nhau và chia hết cho $5$:

Nếu chữ số tận cùng là $0$: có $A_4^3 = 24$ số.

Nếu chữ số tận cùng là $5$: có $3$ khả năng chọn chữ số hàng nghìn, có $A_3^2 = 6$ khả năng chọn $2$ chữ số cuối.

Vậy có $3.6 = 18$ số.

Do đó có $24 + 18 = 42$ số gồm $4$ chữ số khác nhau và chia hết cho $5.$

Vậy có: $96 – 42 = 54$ số gồm $4$ chữ số khác nhau và không chia hết cho $5.$

## Bài 5: Cho các chữ số $0$, $1$, $2$, $3$, $4$, $5.$ Từ các chữ số đã cho ta có thể lập được:

## Bài tập 1. Bao nhiêu số chẵn có bốn chữ số và bốn chữ số đó khác nhau từng đôi một.

## Bài tập 2. Bao nhiêu số chia hết cho $5$, có ba chữ số và ba chữ số đó khác nhau từng đôi một.

3 Bao nhiêu số chia hết cho $9$, có ba chữ số và ba chữ số đó khác nhau từng đôi một.

Lời giải:

1) Gọi $\overline {abcd}$ là số tự nhiên chẵn gồm $4$ chữ số khác nhau đôi một, khi đó $d$ phải là một số chẵn.

Trường hợp 1: Xét $d = 0$, khi đó số cách chọn các chữ số $a$, $b$, $c$ là: $A_5^3 = 60.$

Trường hợp 2: Xét $d \ne 0$, suy ra có $2$ cách chọn $d.$

Có $4$ cách chọn $a.$

Có $4$ cách chọn $b.$

Có $3$ cách chọn $c.$

Theo quy tắc nhân có: $2.4.4.3 = 96$ số.

Vậy theo quy tắc cộng có: $60 + 96 = 156$ số chẵn.

2) Gọi $\overline {abc}$ là số tự nhiên có $3$ chữ số khác nhau đôi một và $\overline {abc}$ chia hết cho $5.$

Trường hợp 1: Xét $c = 0$, khi đó:

Có $5$ cách chọn $a.$

Có $4$ cách chọn $b.$

Theo quy tắc nhân có: $5.4 = 20$ số tận cùng bằng $0.$

Trường hợp 2: Xét $c =5$, khi đó:

Có $4$ cách chọn $a.$

Có $4$ cách chọn $b.$

Theo quy tắc nhân có: $4.4 =16$ số tận cùng bằng $5.$

Vậy theo quy tắc cộng có: $20+ 16 = 36$ số chia hết cho $5.$

3) Gọi $\overline {abc}$ là số tự nhiên có $3$ chữ số khác nhau đôi một và $\overline {abc}$ chia hết cho $9.$

Khi đó: $a+b+c$ phải chia hết cho $9$, suy ra $a$, $b$, $c$ thuộc một trong các tập số: $\{ 0;4;5\}$, $\{ 2;3;4\}$, $\{ 1;3;5\} .$

+ Với tập số $\{ 0;4;5\}$ lập được $4$ số là: $450$; $540$; $405$; $504.$

+ Với tập số $\{ 2;3;4\}$, $\{ 1;3;5\}$, mỗi tập lập được $3!$ số có $3$ chữ số khác nhau và chia hết cho $9.$

Vậy có: $4 + 2.3! = 16$ số tự nhiên có $3$ chữ số khác nhau đôi một và chia hết cho $9.$

## Bài 6: Có bao nhiêu số lẻ gồm $6$ chữ số, chia hết cho $9$?

Lời giải:

Chữ số lẻ nhỏ nhất có $6$ chữ số và chia hết cho $9$ là: $100017$ và chữ số lẻ lớn nhất có $6$ chữ số và chia hết cho $9$ là: $999999.$

Để lập các số lẻ tiếp theo số $100017$ có $6$ chữ số và chia hết cho $9$ ta chỉ cần cộng số đó với $18.$

Như vậy ta có một cấp số cộng với ${u_1} = 100017$, ${u_n} = 999999$, $d = 18.$

Ta có: ${u_n} = {u_1} + (n – 1)d$ $\Leftrightarrow 999999 = 100017 + (n – 1)18$ $\Leftrightarrow n = 50000.$

Vậy tất cả có $50000$ số lẻ gồm $6$ chữ số, chia hết cho $9.$

## Bài 7:

## Bài tập 1. Có thể tìm được bao nhiêu số gồm $3$ chữ số khác nhau đôi một?

## Bài tập 2. Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$ có thể lập được bao nhiêu số chẵn có $5$ chữ số đôi một khác nhau?

Lời giải:

## Bài tập 1. Có $9$ cách chọn chữ số hàng trăm, $9$ cách chọn chữ số hàng chục, $8$ cách chọn chữ số hàng đơn vị. Vậy có $9.9.8 = 648$ số.

+ Trường hợp 1: Chữ số tận cùng bằng $0.$ Bốn chữ số đứng đầu được chọn tuỳ ý trong $7$ chữ số còn lại nên số các số tạo thành là: $A_7^4 = 840.$

+ Trường hợp 2: Chữ số tận cùng khác $0.$

Chữ số tận cùng có $3$ cách chọn (từ $2$, $4$, $6$).

Chữ số đứng đầu có $6$ cách chọn.

$3$ chữ số còn lại được chọn tuỳ ý trong $6$ chữ số còn lại.

Suy ra số các số tạo thành: $3.6.A_6^3 = 2160.$

Vậy có tất cả: $840 + 2160 = 3000$ số.

## Bài 8: Cho tập $A = \{ 1,2,3,4,5,6\} .$

a) Có bao nhiêu số tự nhiên gồm $6$ chữ số khác nhau lập từ $A$ sao cho tổng $3$ chữ số đầu nhỏ hơn tổng $3$ chữ số sau đúng $1$ đơn vị.

b) Có bao nhiêu số tự nhiên có $4$ chữ số khác nhau lập từ $A$ và chia hết cho $4.$

Lời giải:

a) Ta có: $1+ 2+ 3+ 4+ 5+6 = 21.$

Vì số tự nhiên cần lập có $6$ chữ số khác nhau và tổng $3$ chữ số đầu nhỏ hơn tổng $3$ chữ số sau $1$ đơn vị, do đó tổng $3$ chữ số đầu bằng $10$ và tổng $3$ chữ số sau bằng $11.$

Suy ra $3$ chữ số đầu thuộc một trong các tập số sau: $\{ 1;3;6\}$, $\{ 1;4;5\}$, $\{ 2;3;5\}$, còn lại là $3$ chữ số sau.

Với mỗi tập số có: $3! = 6$ cách sắp xếp $3$ chữ số đầu và $3! = 6$ cách sắp xếp $3$ chữ số sau.

Vậy có $3.6.6 = 108$ số tự nhiên có $6$ chữ số sao cho tổng $3$ chữ số đầu nhỏ hơn tổng $3$ chữ số sau $1$ đơn vị.

b) Gọi số tự nhiên cần tìm có dạng $n = \overline {abcd} .$

Vì $n$ chia hết cho $4$ nên $\overline {cd}$ phải chia hết cho $4.$

Do đó $\overline {cd}$ có thể là: $12$, $16$, $24$, $32$, $36$, $52$, $56$, $64$ (có $8$ trường hợp của $\overline {cd}$).

Mỗi trường hợp của $\overline {cd}$ có $A_4^2 = 12$ cách chọn $2$ chữ số cho $a$ và $b.$

Vậy có $8.12 = 96$ số có $4$ chữ số khác nhau và chia hết cho $4.$

## Bài 9: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$ có thể lập được bao nhiêu số tự nhiên chẵn mà mỗi số gồm $7$ chữ số khác nhau?

Lời giải:

Các số phải lập là chẵn nên phải có chữ số đứng cuối cùng là $0$ hoặc $2$, $4$, $6$, $8.$

+ Trường hợp chữ số đứng cuối là $0$: thì $6$ chữ số còn lại là một chỉnh hợp chập $6$ của $8$ phần tử. Do đó có $A_8^6$ số thuộc loại này.

+ Trường hợp chữ số đứng cuối là một trong các chữ số $2$, $4$, $6$, $8$: thì $6$ chữ số còn lại là một chỉnh hợp chập $6$ của $8$ phần tử (kể cả số có chữ số $0$ đứng đầu).

Vậy số các số loại này là: $4.\left( {A_8^6 – A_7^5} \right).$

Vậy tất cả có: $A_8^6 + 4\left( {A_8^6 – A_7^5} \right) = 90720$ số.

## Bài 10: Từ chín chữ số $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$, $9$, người ta lập ra các số tự nhiên gồm $9$ chữ số khác nhau mà chữ số hàng trăm là $4.$

a) Có bao nhiêu số tự nhiên như thế?

b) Trong những số đó có bao nhiêu số chia hết cho $25.$

Lời giải:

a) Mỗi số tự nhiên tạo thành là một hoán vị của $8$ số $1$, $2$, $3$, $5$, $6$, $7$, $8$, $9$ (vì số $4$ đã xếp ở hàng trăm).

Vậy có: $8! = 40320$ số.

b) Chú ý: các số tự nhiên có hai chữ số trở lên chia hết cho $25$ thì hai chữ số tận cùng phải chia hết cho $25$ thì hai số tận cùng có thể là $00$ hoặc $25$, hoặc $50$, hoặc $75.$

Do các chữ số khác nhau và khác $0$ nên ta chỉ có $2$ trường hợp của hai số tận cùng thỏa mãn là $25$ hoặc $75.$

Mỗi trường hợp có $6! = 720$ số tạo thành.

Vậy số các số tự nhiên thỏa mãn là: $2.720 = 1440$ số.

## Bài 11: Cho tập $E = \{ 1;2;3;4;5;6;7\} .$ Từ tập $E$ có thể lập được bao nhiêu số chẵn gồm $5$ chữ số khác nhau.

Lời giải:

Gọi $n = \overline {abcde}$ là số tự nhiên cần tìm.

Có $3$ cách chọn $e.$

Có $A_6^4 = 360$ cách chọn các chữ số $a$, $b$, $c$, $d.$

Vậy có: $3.360 = 1080$ số.

## Bài 12: Từ $5$ chữ số $0$, $1$, $2$, $5$, $9$ có thể lập được bao nhiêu số lẻ, mỗi số gồm $4$ chữ số khác nhau.

Lời giải:

Số cần tìm có dạng: $\overline {{a_1}{a_2}{a_3}{a_4}} .$

Chọn ${a_4}$ từ $\{ 1,5,9\}$ $\Rightarrow$ có $3$ cách chọn.

Chọn ${a_1}$ từ $\{ 0,1,2,5,9\} \backslash \left\{ {0,{a_4}} \right\}$ $\Rightarrow$ có $3$ cách chọn.

Chọn ${a_2}$ từ $\{ 0,1,2,5,9\} \backslash \left\{ {{a_1},{a_4}} \right\}$ $\Rightarrow$ có $3$ cách chọn.

Chọn ${a_3}$ từ $\{ 0,1,2,5,9\} \backslash \left\{ {{a_1},{a_2},{a_4}} \right\}$ $\Rightarrow$ có $2$ cách chọn.

Vậy tất cả có: $3.3.3.2 = 54$ số thoả mãn yêu cầu đề bài.

## Bài 13: Người ta viết các chữ số $0$, $1$, $2$, $3$, $4$, $5$ lên các tấm phiếu, sau đó xếp thứ tự ngẫu nhiên thành một hàng.

## Bài tập 1. Có bao nhiêu số lẻ gồm $6$ chữ số được sắp thành?

## Bài tập 2. Có bao nhiêu số chẵn gồm $6$ chữ số được sắp thành?

Lời giải:

Số có $6$ chữ số khác nhau có dạng: $\overline {abcdef}$ với $a \ne 0.$

## Bài tập 1. Vì số tạo thành là số lẻ nên $f \in \{ 1,3,5\} .$

Do đó: $f$ có $3$ cách chọn.

$a$ có $4$ cách chọn (trừ $0$ và $f$).

$b$ có $4$ cách chọn (trừ $a$ và $f$).

$c$ có $3$ cách chọn (trừ $a$, $b$, $f$).

$d$ có $2$ cách chọn (trừ $a$, $b$, $c$, $f$).

$e$ có $1$ cách chọn (trừ $a$, $b$, $c$, $d$, $f$).

Vậy: có $3.4.4.3.2.1 = 288$ số.

## Bài tập 2. Vì số tạo thành là số chẵn nên $f \in \{ 0,2,4\} .$

+ Khi $f = 0$ thì $(a,b,c,d,e)$ là một hoán vị của $(1,2,3,4,5).$ Do đó có $5!$ số.

+ Khi $f \in \{ 2,4\}$ thì:

$f$ có $2$ cách chọn.

$a$ có $4$ cách chọn.

$b$ có $4$ cách chọn.

$c$ có $3$ cách chọn.

$d$ có $2$ cách chọn.

$e$ có $1$ cách chọn.

Do đó có $2.4.4.3.2.1 = 192$ số.

Vậy: có $120 + 192 = 312$ số chẵn.

## Bài 14: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số gồm $3$ chữ số đôi một khác nhau không chia hết cho $9.$

Lời giải:

Gọi $n = \overline {abc}$ là số tự nhiên có $3$ chữ số khác nhau, khi đó:

Có $5$ cách chọn $a.$

Có $A_5^2 = 20$ cách chọn $2$ chữ số xếp vào $b$, $c.$

Suy ra có $5.20 = 100$ số.

Xét các số tự nhiên dạng $n = \overline {abc}$ có $3$ chữ số khác nhau và chia hết cho $9.$

Suy ra $a+b+c$ phải chia hết cho $9.$

Do đó $a$, $b$, $c$ thuộc một trong các tập số sau: $\{ 0;4;5\}$, $\{ 1;3;5\}$, $\{ 2;3;4\} .$

+ Xét $a$, $b$, $c$ thuộc tập số $\{ 0;4;5\} :$

Có $2$ cách chọn $a.$

Có $2$ cách chọn $b.$

Có $1$ cách chọn $c.$

Suy ra có $2.2.1 = 4$ số.

+ Xét $a$, $b$, $c$ thuộc một trong $2$ tập số $\{ 1;3;5\}$, $\{ 2;3;4\}$:

Mỗi tập số có thể lập được $3! = 6$ số tự nhiên có $3$ chữ số khác nhau.

Suy ra có $2.6 = 12$ số.

Vậy tất cả có $4 + 12 = 16$ số tự nhiên có $3$ chữ số khác nhau và chia hết cho $9.$

Vậy có $100 – 16 = 84$ số tự nhiên có $3$ chữ số khác nhau và không chia hết cho $9.$

## Bài 15: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$ có thể lập được bao nhiêu số tự nhiên chẵn mà mỗi số gồm $7$ chữ số khác nhau?

Lời giải:

Các số phải lập là chẵn nên phải có chữ số đứng cuối cùng là $0$ hoặc $2$, $4$, $6$, $8.$

+ Trường hợp chữ số đứng cuối là $0$: thì $6$ chữ số còn lại là một chỉnh hợp chập $6$ của $8$ phần tử. Do đó có $A_8^6$ số thuộc loại này.

+ Trường hợp chữ số đứng cuối là một trong các chữ số $2$, $4$, $6$, $8$: thì $6$ chữ số còn lại là một chỉnh hợp chập $6$ của $8$ phần tử (kể cả số có chữ số $0$ đứng đầu). Vậy số các số loại này là: $4\left( {A_8^6 – A_7^5} \right).$

Vậy tất cả có: $A_8^6 + 4\left( {A_8^6 – A_7^5} \right) = 90720$ số.

## Bài 16: Xét dãy số gồm $7$ chữ số khác nhau (mỗi chữ số được chọn từ $0$, $1$, ….,$8$, $9$) thỏa chữ số đầu tiên bằng $7$, chữ số cuối không chia hết cho $5.$ Hỏi có bao nhiêu cách chọn.

Lời giải:

Gọi số tự nhiên cần lập có dạng $n = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}{a_7}} .$

Có $1$ cách chọn ${a_1}$, là chữ số $7.$

Có $7$ cách chọn ${a_7}$, trừ các chữ số $0$, $5$, $7.$

Có $A_8^5 = 6720$ cách chọn $5$ chữ số xếp vào các vị trí còn lại trong $n.$

Vậy có $7.6720 = 47040$ số.

## Bài 17: Có $100$ tấm bìa hình vuông được đánh số từ $1$ đến $100.$ Ta lấy ngẫu nhiên một tấm bìa. Tính xác suất để lấy được:

a) Một tấm bìa có số không chứa chữ số $5.$

b) Một tấm bìa có số chia hết cho $2$ hoặc $5$ hoặc cả $2$ và $5.$

Lời giải:

Chọn ngẫu nhiên một tấm bìa thì có $100$ cách.

a) Số tấm bìa được đánh số có một chữ số không chứa chữ số $5$ là $8$ tấm ($1$, $2$, $3$, $4$, $6$, $7$, $8$, $9$).

Số tấm bìa được đánh số có $2$ chữ số không chứa chữ số $5$ có dạng $\overline {ab}$ $(a,b \ne 5).$

Có $8$ cách chọn $a$ (trừ $0$ và $5$).

Có $9$ cách chọn $b.$

Suy ra có: $8.9 = 72$ tấm bìa.

Vậy tất cả có $8 + 72 = 80$ tấm bìa không chứa chữ số $5.$

Và chọn ngẫu nhiên một tấm bìa như thế thì có $80$ cách.

Vậy xác suất chọn được một tấm bìa không chứa chữ số $5$ là: $\frac{{80}}{{100}} = 0,8.$

b) Số tấm bìa có ghi số không chia hết cho $2$ hoặc $5$ là số tấm bìa có ghi số không tận cùng bằng chữ số chẵn hoặc chữ số $5.$

Số tấm bìa có ghi số không chia hết cho $2$ hoặc $5$ có $1$ chữ số là $4$ tấm (ghi số $1$, $3$, $7$, $9$).

Số tấm bìa có ghi số không chia hết cho $2$ hoặc $5$ có $2$ chữ số có dạng: $\overline {ab}$ (với $b$ lẻ và $b$ khác $5$).

Có $9$ cách chọn $a.$

Có $4$ cách chọn $b.$

Suy ra có: $4.9 = 36$ tấm.

Vậy tất cả có $4 + 36 = 40$ tấm bìa có số không chia hết cho $2$ hoặc $5.$

Suy ra có: $100 – 40 = 60$ tấm bìa có ghi số chia hết cho $2$ hoặc $5$ hoặc cả $2$ và $5.$

Vậy xác suất của lấy được một tấm bìa có số chia hết cho $2$ hoặc $5$ hoặc cả $2$ và $5$ là: $\frac{{60}}{{100}} = 0,6.$

## Bài 18: Có bao nhiêu số tự nhiên $X$ có $5$ chữ số khác nhau và nhất thiết phải có mặt chữ số $1$ và $X$ chia hết cho $2.$

Lời giải:

Gọi số tự nhiên cần tìm có dạng: $X = \overline {abcde} .$

Ta nhận thấy $X$ chia hết cho $2$ nên $e$ không thể là chữ số $1$ được, do đó ta xét các trường hợp sau:

Nếu $e = 0$, khi đó:

Có $4$ cách chọn vị trí trong $X$ để xếp chữ số $1.$

Có $A_8^3 = 336$ cách chọn $3$ chữ số để xếp vào các chữ số còn lại trong $X.$

Suy ra trường hợp này có: $4.336 = 1344$ số.

Nếu $e \ne 0$, khi đó ta xét $2$ trường hợp nhỏ sau:

+ Nếu $a=1$, khi đó:

Có $4$ cách chọn $e.$

Có $A_8^3 = 336$ cách chọn $3$ chữ số để xếp vào các chữ số còn lại trong $X.$

Suy ra có: $4.336 = 1344$ số.

Nếu $a \ne 1$, khi đó:

Có $4$ cách chọn $e.$

Có $7$ cách chọn $a$ (khác $e$, khác $0$ và khác $1$).

Có $3$ cách chọn vị trí để xếp chữ số $1$ (trừ $a$ và $e$).

Có $A_7^2 = 42$ cách chọn $2$ chữ số để xếp vào các chữ số còn lại trong $X.$

Suy ra có: $4.7.3.42 = 3528$ số.

Suy ra trường hợp này có: $1344 + 3528 = 4872$ số.

Vậy tất cả có: $1344 + 4872 = 6216$ số $X.$

## Bài 19: Từ các chữ số $1$; $3$; $4$; $5$; $6$ có thể lập được bao nhiêu số tự nhiên gồm $3$ chữ số khác nhau và số tự nhiên đó chia hết cho $3.$

Lời giải:

Gọi $n = \overline {abc}$ là số tự nhiên thỏa yêu cầu bài toán.

Do $n$ chia hết có $3$ nên $a + b + c$ phải chia hết cho $3.$

Suy ra $a$, $b$, $c$ thuộc một trong các tập số sau: $\{ 1;3;5\}$, $\{ 1;5;6\}$, $\{ 3;4;5\}$, $\{ 4;5;6\} .$

Mỗi tập số có thể lập được $3! = 6$ số tự nhiên có $3$ chữ số khác nhau và chia hết cho $3.$

Vậy có $4.6 = 24$ số.

## Bài 20: Cho tập $E = \{ 1;2;3;4;5;6;7\} .$ Có bao nhiêu số tự nhiên gồm $4$ chữ số khác nhau lập từ $A$ sao cho số tự nhiên đó chia hết cho $6$ và có mặt chữ số $1.$

Lời giải:

Gọi số tự nhiên có dạng $n = \overline {abcd} .$

Số tự nhiên chia hết cho $6$ là số tự nhiên vừa chia hết cho $2$ và chia hết cho $3.$

Do đó $d$ chẵn và $a+b+c+d$ phải chia hết cho $3$, và luôn có mặt chữ số $1.$

Suy ra $a$, $b$, $c$, $d$ thuộc một trong các tập số sau: $\{ 1;2;3;6\}$, $\{ 1;2;4;5\}$, $\{ 1;2;5;7\}$, $\{ 1;3;4;7\}$, $\{ 1;3;5;6\} .$

+ Xét $3$ tập hợp chứa $1$ chữ số chẵn là: $\{ 1;2;5;7\}$, $\{ 1;3;4;7\}$, $\{ 1;3;5;6\} .$

Mỗi tập hợp có $1$ cách chọn $d$, và $3!$ cách xếp $3$ chữ số còn lại.

Suy ra có $3.1.3! = 18$ số.

+ Xét $2$ tập chứa $2$ chữ số chẵn là: $\{ 1;2;3;6\}$, $\{ 1;2;4;5\} .$

Mỗi tập hợp có $2$ cách chọn $d$, và $3!$ cách xếp $3$ chữ số còn lại.

Suy ra có $2.2.3!=24$ số.

Vậy tất cả có $18 + 24 = 42$ số tự nhiên có $4$ chữ số khác nhau, chia hết cho $6$ và luôn có mặt chữ số $1.$

## Bài 21: Cho $5$ chữ số $0$; $1$; $2$; $3$; $6.$ Từ $5$ chữ số trên có thể lập được bao nhiêu số tự nhiên có $3$ chữ số khác nhau và số tự nhiên đó không chia hết cho $6.$

Lời giải:

Gọi $n = \overline {abcde}$ là số tự nhiên có $5$ chữ số khác nhau và không chia hết cho $6.$

Số $n$ phải không chia hết cho $3$ hoặc không chia hết cho $2.$

Ta nhận thấy $0 + 1 + 2 + 3 + 6 = 12$ chia hết cho $3$, do đó $n$ luôn chia hết cho $3.$

Do đó để $n$ không chia hết cho $6$ thì $n$ phải là một số tự nhiên lẻ, khi đó:

Có $2$ cách chọn $e.$

Có $3$ cách chọn $a.$

Có $3!$ cách chọn $3$ chữ số còn lại xếp vào $b$, $c$, $d.$

Vậy có $2.3.3! = 36$ số tự nhiên có $5$ chữ số khác nhau và không chia hết cho $6.$

## Bài 22: Có bao nhiêu số tự nhiên có $5$ chữ số khác nhau và không chia hết cho $10.$

Lời giải:

Số tự nhiên cần tìm có dạng $n = \overline {abcde} .$

Do $n$ không chia hết cho $10$ nên $e \ne 0$, khi đó:

Có $9$ cách chọn $a.$

Có $8$ cách chọn $e.$

Có $A_8^3 = 336$ cách chọn ra $3$ chữ số xếp vào $b$, $c$, $d.$

Vậy có $9.8.336 = 24192$ số tự nhiên có $5$ chữ số khác nhau và không chia hết cho $10.$

## Bài 23: Có tất cả bao nhiêu số tự nhiên có $5$ chữ số khác nhau, sao cho:

a) Chia hết cho $5$ và bắt đầu bằng $5.$

b) Chia hết cho $2$ và bắt đầu bằng $4.$

Lời giải:

Gọi $n = \overline {abcde} .$

a) Chữ số đầu tiên bằng $5$ nên $a= 5$ và chia hết cho $5$ nên $e = 0.$

Có $8$ cách chọn $b.$

Có $7$ cách chọn $c.$

Có $6$ cách chọn $d.$

Vậy có: $8.7.6 = 336$ số.

b) Số tự nhiên có dạng $n = \overline {4bcde} .$

Do $n$ chia hết cho $2$ nên $e \in \{ 0;2;6;8\} .$

+ Nếu $e =0$, khi đó có: $A_8^3 = 336$ cách chọn các chữ số $b$, $c$, $d.$

Suy ra trường hợp này có $336$ số.

+ Nếu $e \ne 0$, khi đó:

Có $3$ cách chọn $e.$

Có $A_8^3 = 336$ cách chọn các chữ số $b$, $c$, $d.$

Vậy trường hợp này có $3.336 = 1008$ số.

Vậy tất cả có: $336 + 1008 = 1344$ số.

## Bài 24: Từ các chữ số $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số tự nhiên có $5$ chữ số khác nhau và chia hết cho $8$?.

Lời giải:

Gọi số tự nhiên cần lập có dạng $n = \overline {abcde} .$

Vì $n$ chia hết cho $8$ nên $\overline {cde}$ phải chia hết cho $8$, do đó $\overline {cde}$ có thể là: $152$, $232$, $352$, $432$, $512.$

Mỗi trường hợp của $\overline {cde}$ có $2!$ cách chọn $a$ và $b.$

Vậy có: $5.2! = 10$ số.

## Bài 25: Từ các chữ số $1$, $2$, $3$, $4$, $5$, $6$ có thể lập được bao nhiêu số tự nhiên có $3$ chữ số khác nhau và chia hết cho $15$?.

Lời giải:

Gọi số tự nhiên cần lập có dạng: $n = \overline {abc} .$

Vì $n$ chia hết cho $15$ nên $n$ vừa chia hết cho $3$ và vừa chia hết cho $5.$

Do đó ta có: 
$$
\left\{ {\begin{array}{l}
{c = 5}\\
{a + b + c \vdots 3}
\end{array}} \right.
$$
 
$$
\Leftrightarrow \left\{ {\begin{array}{l}
{c = 5}\\
{a + b + 5 \vdots 3}
\end{array}} \right..
$$

Vậy $a$, $b$ thuộc một trong các tập số sau: $\{ 1;3\}$, $\{ 1;6\}$, $\{ 3;4\}$, $\{ 4;6\} .$

Mỗi tập số trên có $2!$ cách chọn $a$, $b.$

Vậy có $4.2!= 8$ số.

## Bài 26: Có bao nhiêu số tự nhiên có $5$ chữ số khác nhau và chia hết cho $20$?

Lời giải: Gọi số tự nhiên cần lập có dạng: $n = \overline {abcde} .$

Vì $n$ chia hết cho $20$ nên $n$ vừa chia hết cho $10$ và được bao nhiêu thì chia hết cho $2.$ Nghĩa là trong số tự nhiên $n$ phải có $e = 0$ và $d$ là một chữ số chẵn.

Khi đó:

Có $1$ cách chọn $e.$

Có $4$ cách chọn $d.$

Có $A_8^3 = 336$ cách chọn $3$ chữ số xếp vào $a$, $b$, $c.$

Vậy có: $4.336 = 1344$ số có $5$ chữ số khác nhau và chia hết cho $20.$

## Bài 27: Từ các chữ số $0$, $1$, $2$, $3$, $4$, $5$ có thể lập được bao nhiêu số gồm $3$ chữ số đôi một khác nhau không chia hết cho $18.$

Lời giải:

Gọi $n = \overline {abc}$ là số tự nhiên có $3$ chữ số khác nhau, khi đó:

Có $5$ cách chọn $a.$

Có $A_5^2 = 20$ cách chọn $2$ chữ số xếp vào $b$, $c.$

Suy ra có $5.20 = 100$ số.

Xét các số tự nhiên dạng $n = \overline {abc}$ có $3$ chữ số khác nhau và chia hết cho $18.$

Do $n$ chia hết cho $18$ nên $n$ vừa chia hết cho $9$ và vừa chia hết cho $2.$

Suy ra $c$ là một chữ số chẵn và $a + b + c$ phải chia hết cho $9.$

Do đó $a$, $b$, $c$ thuộc một trong các tập số sau: $\{ 0;4;5\}$, $\{ 2;3;4\} .$

+ Xét $a$, $b$, $c$ thuộc tập số $\{ 0;4;5\} :$

Có thể lập được $3$ số thỏa mãn là: $450$ hoặc $540$ hoặc $504.$

Suy ra có $2.2.1 = 4$ số.

Xét $a$, $b$, $c$ thuộc tập số $\{ 2;3;4\} :$

Do $c$ chẵn nên có $2$ cách chọn $c.$

Có $2$ cách chọn $a.$

Có $1$ cách chọn $b.$

Suy ra trường hợp này có $2.2.1 = 4$ số.

Vậy tất cả có $3 + 4 = 7$ số tự nhiên có $3$ chữ số khác nhau và chia hết cho $18.$

Suy ra có $100 – 7 = 93$ số tự nhiên có $3$ chữ số khác nhau và không chia hết cho $18.$